const TICKETS_KEY = 'firenotify_support_tickets'
const USERS_KEY = 'fireNotifyRegisteredUsers'
const NOTIFICATIONS_KEY = 'firenotify_notifications'

export const SUPPORT_UPDATED_EVENT = 'fireNotifySupportTicketsUpdated'

const normalize = value => String(value ?? '').trim().toLowerCase()

const readArray = key => {
  try {
    const value = JSON.parse(localStorage.getItem(key) || '[]')
    return Array.isArray(value) ? value : []
  } catch {
    return []
  }
}

const writeTickets = tickets => {
  localStorage.setItem(TICKETS_KEY, JSON.stringify(tickets))
  window.dispatchEvent(new CustomEvent(SUPPORT_UPDATED_EVENT))
}

const userId = user => user?.id || user?.userId || user?.identifier || user?.email || ''
const userName = user => user?.name || `${user?.firstName || ''} ${user?.lastName || ''}`.trim() || user?.username || user?.identifier || 'Personnel'
const userEmail = user => user?.email || user?.identifier || user?.username || ''

const notify = ({ id, recipientId, title, message, sourceId }) => {
  if (!recipientId) return
  const notifications = readArray(NOTIFICATIONS_KEY)
  if (notifications.some(item => String(item.id) === String(id))) return

  notifications.unshift({
    id,
    recipientId,
    assignedToId: recipientId,
    title,
    message,
    detail: message,
    type: 'Support Alerts',
    priority: 'NORMAL',
    status: 'unread',
    read: false,
    isRead: false,
    sourceType: 'Support Ticket',
    sourceId,
    createdAt: new Date().toISOString()
  })

  localStorage.setItem(NOTIFICATIONS_KEY, JSON.stringify(notifications))
  window.dispatchEvent(new CustomEvent('fireNotifyNotificationsUpdated'))
}

const notifyAdmins = (ticket, eventType, title, message) => {
  readArray(USERS_KEY)
    .filter(user => normalize(user?.role) === 'admin')
    .forEach(admin => {
      const id = userId(admin)
      notify({
        id: `support-${ticket.id}-${eventType}-${id}`,
        recipientId: id,
        title,
        message,
        sourceId: ticket.id
      })
    })
}

export const getSupportTickets = () => readArray(TICKETS_KEY)

export const getTicketsForUser = user => {
  const id = normalize(userId(user))
  return getSupportTickets().filter(ticket => normalize(ticket.userId) === id)
}

export const createSupportTicket = ({ user, subject, category, priority, description, attachment, module = '', referenceId = '' }) => {
  const tickets = getSupportTickets()
  const largest = tickets.reduce((max, ticket) => {
    const number = Number(String(ticket.ticketNumber || '').replace(/\D/g, ''))
    return Number.isFinite(number) ? Math.max(max, number) : max
  }, 0)
  const now = new Date().toISOString()
  const ticket = {
    id: `support-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
    ticketNumber: `SUP-${String(largest + 1).padStart(4, '0')}`,
    userId: userId(user),
    userName: userName(user),
    userEmail: userEmail(user),
    subject: subject.trim(),
    category,
    priority,
    description: description.trim(),
    attachment: attachment || null,
    module,
    referenceId,
    status: 'Open',
    messages: [{
      id: `message-${Date.now()}`,
      senderId: userId(user),
      sender: userName(user),
      role: 'Personnel',
      message: description.trim(),
      createdAt: now,
      readByAdmin: false,
      readByPersonnel: true
    }],
    createdAt: now,
    updatedAt: now,
    resolvedAt: null,
    closedAt: null
  }

  writeTickets([ticket, ...tickets])
  notifyAdmins(ticket, 'created', 'New Support Request', `${ticket.ticketNumber}: ${ticket.subject}`)
  return ticket
}

export const addTicketReply = ({ ticketId, user, message }) => {
  const tickets = getSupportTickets()
  const ticket = tickets.find(item => item.id === ticketId)
  if (!ticket || !message.trim() || normalize(ticket.userId) !== normalize(userId(user))) return null

  const now = new Date().toISOString()
  const isAdmin = normalize(user?.role) === 'admin'
  const reply = {
    id: `message-${Date.now()}-${Math.random().toString(36).slice(2, 6)}`,
    senderId: userId(user),
    sender: userName(user),
    role: isAdmin ? 'Admin' : 'Personnel',
    message: message.trim(),
    createdAt: now,
    readByAdmin: isAdmin,
    readByPersonnel: !isAdmin
  }

  ticket.messages = [...(ticket.messages || []), reply]
  ticket.updatedAt = now
  if (ticket.status === 'Waiting for Personnel' && !isAdmin) ticket.status = 'In Review'
  writeTickets(tickets)

  if (isAdmin) {
    notify({ id: `support-${ticket.id}-reply-${reply.id}`, recipientId: ticket.userId, title: 'Admin Replied to Support Ticket', message: `Admin replied to ${ticket.ticketNumber}.`, sourceId: ticket.id })
  } else {
    notifyAdmins(ticket, `reply-${reply.id}`, 'Personnel Replied to Support Ticket', `${ticket.ticketNumber}: ${ticket.subject}`)
  }
  return ticket
}

export const updateTicketStatus = ({ ticketId, user, status }) => {
  if (normalize(user?.role) !== 'admin') return null
  const allowed = ['Open', 'In Review', 'Waiting for Personnel', 'Resolved', 'Closed']
  if (!allowed.includes(status)) return null
  const tickets = getSupportTickets()
  const ticket = tickets.find(item => item.id === ticketId)
  if (!ticket) return null
  const now = new Date().toISOString()
  ticket.status = status
  ticket.updatedAt = now
  if (status === 'Resolved') ticket.resolvedAt = now
  if (status === 'Closed') ticket.closedAt = now
  writeTickets(tickets)
  notify({ id: `support-${ticket.id}-status-${status}-${now}`, recipientId: ticket.userId, title: `Support Ticket ${status}`, message: `${ticket.ticketNumber} is now ${status}.`, sourceId: ticket.id })
  return ticket
}

export const confirmTicketResolution = ({ ticketId, user }) => {
  const tickets = getSupportTickets()
  const ticket = tickets.find(item => item.id === ticketId)
  if (!ticket || normalize(ticket.userId) !== normalize(userId(user)) || ticket.status !== 'Resolved') return null
  const now = new Date().toISOString()
  ticket.status = 'Closed'
  ticket.closedAt = now
  ticket.updatedAt = now
  writeTickets(tickets)
  return ticket
}

export const submitTicketFeedback = ({ ticketId, user, rating, comment = '' }) => {
  const score = Number(rating)
  if (!Number.isInteger(score) || score < 1 || score > 5) return null

  const tickets = getSupportTickets()
  const ticket = tickets.find(item => item.id === ticketId)
  if (!ticket || normalize(ticket.userId) !== normalize(userId(user))) return null
  if (!['Resolved', 'Closed'].includes(ticket.status) || ticket.feedback) return null

  ticket.feedback = {
    rating: score,
    comment: String(comment).trim().slice(0, 500),
    createdAt: new Date().toISOString()
  }
  ticket.updatedAt = ticket.feedback.createdAt
  writeTickets(tickets)
  return ticket
}

export const deleteSupportTicket = ({ ticketId, user }) => {
  const tickets = getSupportTickets()
  const ticket = tickets.find(item => item.id === ticketId)
  if (!ticket || normalize(ticket.userId) !== normalize(userId(user)) || !['Open'].includes(ticket.status)) return false
  writeTickets(tickets.filter(item => item.id !== ticketId))
  return true
}

export const markTicketRead = ({ ticketId, user }) => {
  const tickets = getSupportTickets()
  const ticket = tickets.find(item => item.id === ticketId)
  if (!ticket) return null
  const isAdmin = normalize(user?.role) === 'admin'
  ticket.messages = (ticket.messages || []).map(message => ({
    ...message,
    [isAdmin ? 'readByAdmin' : 'readByPersonnel']: true
  }))
  writeTickets(tickets)
  return ticket
}
