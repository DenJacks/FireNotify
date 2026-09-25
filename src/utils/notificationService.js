const NOTIFICATION_KEY = 'firenotify_notifications'
const USERS_KEY = 'fireNotifyRegisteredUsers'
const DISMISSED_KEY = 'fireNotifyDismissedNotifications'
const PERSONNEL_SETTINGS_KEY = 'firenotify_personnel_settings'

import { resolvePersonnelName } from './personnelName.js'

export const NOTIFICATION_EVENTS = [
  'fireNotifyNotificationsUpdated',
  'fireNotifySupportTicketsUpdated',
  'fireNotifyUsersUpdated',
  'fireNotifyRegisteredUsersUpdated',
  'fireNotifyActivitiesUpdated',
  'fireNotifyTasksUpdated',
  'fireNotifyReportsUpdated'
]

const normalize = value => String(value ?? '').trim().toLowerCase()

const readArray = key => {
  try {
    const parsed = JSON.parse(localStorage.getItem(key) || '[]')
    return Array.isArray(parsed) ? parsed : []
  } catch {
    return []
  }
}

const readObject = key => {
  try {
    const parsed = JSON.parse(localStorage.getItem(key) || '{}')
    return parsed && typeof parsed === 'object' && !Array.isArray(parsed) ? parsed : {}
  } catch {
    return {}
  }
}

export const readNotifications = () => readArray(NOTIFICATION_KEY)

const readDismissedIds = () => {
  try {
    const parsed = JSON.parse(localStorage.getItem(DISMISSED_KEY) || '[]')
    return new Set(Array.isArray(parsed) ? parsed.map(String) : [])
  } catch {
    return new Set()
  }
}

export const isNotificationRead = notification => {
  if (typeof notification?.read === 'boolean') return notification.read
  if (typeof notification?.isRead === 'boolean') return notification.isRead
  return normalize(notification?.status) === 'read'
}

export const notificationIdentities = user => [
  user?.id,
  user?.userId,
  user?.identifier,
  user?.username,
  user?.email
].map(normalize).filter(Boolean)

const assignmentIdentities = value => {
  const values = Array.isArray(value) ? value : [value]
  return values.flatMap(item => [
    item,
    item?.id,
    item?.userId,
    item?.identifier,
    item?.username,
    item?.email
  ]).map(normalize).filter(Boolean)
}

const assignedRecipients = (record, users) => {
  const assignments = record?.assignedPersonnel || record?.assignedUsers
  const values = Array.isArray(assignments) && assignments.length
    ? assignments
    : [record?.assignedToId || record?.assignedToUsername || record?.assignedToEmail || record?.assignedTo]

  const identities = assignmentIdentities(values)
  return users.filter(user => {
    const userIdentities = notificationIdentities(user)
    return userIdentities.some(identity => identities.includes(identity))
  })
}

const parseDate = value => {
  if (!value) return null
  const date = value instanceof Date ? new Date(value) : new Date(String(value).replace('•', ' '))
  return Number.isNaN(date.getTime()) ? null : date
}

const deadlineOf = record => record?.deadline || record?.dueDate || record?.deadlineDate || record?.date || record?.schedule || ''

const isFinal = record => [
  'verified', 'completed', 'complete', 'approved', 'closed', 'resolved', 'done', 'finished'
].includes(normalize(record?.status || record?.submissionStatus))

const titleOf = record => record?.title || record?.name || record?.activityName || 'Untitled record'

const event = ({ id, recipientId, type, title, message, sourceType, sourceId, priority = 'NORMAL', createdAt }) => ({
  id,
  title,
  message,
  detail: message,
  type,
  priority,
  status: 'unread',
  read: false,
  isRead: false,
  recipientId,
  assignedToId: recipientId,
  sourceType,
  sourceId,
  createdAt: createdAt || new Date().toISOString()
})

const recordNotifications = (record, sourceType, users, now) => {
  const title = titleOf(record)
  const sourceId = record?.id
  if (!sourceId) return []

  return assignedRecipients(record, users).flatMap(recipient => {
    const recipientId = recipient.id || recipient.userId || recipient.identifier || recipient.email
    if (!recipientId) return []

    const base = `${sourceType.toLowerCase()}-${sourceId}-${recipientId}`
    const notifications = []
    const status = normalize(record.status || record.submissionStatus)
    const deadline = parseDate(deadlineOf(record))

    notifications.push(event({
      id: `${base}-assigned`,
      recipientId,
      type: sourceType === 'Task' ? 'Task Alerts' : sourceType === 'Activity' ? 'Activity Reminders' : 'Report Alerts',
      title: sourceType === 'Task' ? 'New Task Assigned' : sourceType === 'Activity' ? 'New Activity Assigned' : 'New Report Requirement',
      message: `${title} has been assigned to you.`,
      sourceType,
      sourceId,
      createdAt: record.assignedAt || record.createdAt
    }))

    if (deadline && !isFinal(record)) {
      const difference = deadline.getTime() - now.getTime()
      const dayKey = deadline.toISOString().slice(0, 10)
      const prefix = sourceType === 'Task' ? 'Task' : sourceType === 'Activity' ? 'Activity' : 'Report'

      if (difference < 0) {
        notifications.push(event({
          id: `${base}-overdue-${dayKey}`,
          recipientId,
          type: 'Deadline Alerts',
          title: `${prefix} Overdue`,
          message: `${title} has passed its deadline.`,
          sourceType,
          sourceId,
          priority: 'URGENT',
          createdAt: deadline.toISOString()
        }))
      } else if (difference <= 24 * 60 * 60 * 1000) {
        notifications.push(event({
          id: `${base}-due-soon-${dayKey}`,
          recipientId,
          type: 'Deadline Alerts',
          title: `${prefix} Deadline Approaching`,
          message: `${title} is due soon.`,
          sourceType,
          sourceId,
          priority: 'HIGH',
          createdAt: deadline.toISOString()
        }))
      }
    }

    if (status === 'returned' || status === 'needs revision' || status === 'revision required') {
      const revisionKey = record.returnedAt || record.revisionCount || record.revisionNote || 'current'
      notifications.push(event({
        id: `${base}-returned-${revisionKey}`,
        recipientId,
        type: sourceType === 'Report' ? 'Report Alerts' : sourceType === 'Task' ? 'Task Alerts' : 'Activity Reminders',
        title: sourceType === 'Report' ? 'Report Returned' : sourceType === 'Task' ? 'Task Returned' : 'Activity Returned',
        message: `${title} was returned for revision${record.revisionNote ? `: ${record.revisionNote}` : '.'}`,
        sourceType,
        sourceId,
        priority: 'HIGH',
        createdAt: record.returnedAt
      }))
    }

    if (status === 'verified' || status === 'approved' || status === 'completed') {
      notifications.push(event({
        id: `${base}-verified-${record.verifiedAt || record.completedAt || status}`,
        recipientId,
        type: sourceType === 'Report' ? 'Report Alerts' : sourceType === 'Task' ? 'Task Alerts' : 'Activity Reminders',
        title: sourceType === 'Report' ? 'Report Verified' : sourceType === 'Task' ? 'Task Verified' : 'Activity Verified',
        message: `${title} has been verified.`,
        sourceType,
        sourceId,
        createdAt: record.verifiedAt || record.completedAt || record.updatedAt
      }))
    }

    return notifications
  })
}

const adminRecipients = currentUser => {
  const users = readArray(USERS_KEY).filter(user => normalize(user?.role) === 'admin')
  if (currentUser && normalize(currentUser.role) === 'admin') {
    const currentId = notificationIdentities(currentUser)[0]
    if (currentId && !users.some(user => notificationIdentities(user).includes(currentId))) {
      users.push(currentUser)
    }
  }
  return users
}

const adminSubmissionNotifications = (record, sourceType, recipients, users) => {
  const title = titleOf(record)
  const sourceId = record?.id
  if (!sourceId) return []

  const status = normalize(record.status || record.submissionStatus)
  const submitter = resolvePersonnelName(
    record.submittedByUser || record.submittedBy || record.personnelName || record.assignedPersonnel || record.assignedToId,
    users,
    'Personnel'
  )
  const notifications = []

  let eventType = ''
  let eventTitle = ''
  let message = ''
  let eventKey = ''
  let createdAt = record.submittedAt || record.updatedAt || record.createdAt

  if (status === 'for verification' || status === 'for review') {
    const resubmitted = record.returnedAt && record.submittedAt &&
      parseDate(record.submittedAt)?.getTime() > parseDate(record.returnedAt)?.getTime()
    eventType = resubmitted ? 'resubmitted' : 'submitted'
    eventTitle = sourceType === 'Task'
      ? (resubmitted ? 'Task Resubmitted' : 'Task Submitted for Verification')
      : sourceType === 'Activity'
        ? (resubmitted ? 'Activity Resubmitted' : 'Activity Submitted for Verification')
        : (resubmitted ? 'Report Resubmitted' : 'Report Submitted')
    message = sourceType === 'Report'
      ? `${title} was submitted by ${submitter}.`
      : `${title} was ${resubmitted ? 'resubmitted for verification' : 'submitted for verification'} by ${submitter}.`
    eventKey = record.submittedAt || record.updatedAt || status
  }

  const deadline = parseDate(deadlineOf(record))
  if (deadline && deadline.getTime() < Date.now() && !isFinal(record)) {
    eventType = 'overdue'
    eventTitle = `${sourceType} Overdue`
    message = `${title} has passed its deadline and requires attention.`
    eventKey = deadline.toISOString().slice(0, 10)
    createdAt = deadline.toISOString()
  }

  if (!eventType) return []

  recipients.forEach(recipient => {
    const recipientId = recipient.id || recipient.userId || recipient.identifier || recipient.email
    if (!recipientId) return
    notifications.push(event({
      id: `admin-${sourceType.toLowerCase()}-${sourceId}-${eventType}-${eventKey}-${recipientId}`,
      recipientId,
      type: eventType === 'overdue' ? 'Deadline Alerts' : sourceType === 'Report' ? 'Reports & Compliance' : sourceType === 'Task' ? 'Task Alerts' : 'Activity Reminders',
      title: eventTitle,
      message,
      sourceType,
      sourceId,
      priority: eventType === 'overdue' ? 'URGENT' : 'HIGH',
      createdAt
    }))
  })

  return notifications
}

const deriveAllPersonnelNotifications = (now = new Date()) => {
  const users = readArray(USERS_KEY)
  const dismissedIds = readDismissedIds()

  const allRecords = [
    ...readArray('firenotify_tasks').map(record => ({ record, sourceType: 'Task' })),
    ...readArray('fireNotifyActivities').map(record => ({ record, sourceType: 'Activity' })),
    ...readArray('firenotify_reports').map(record => ({ record, sourceType: 'Report' }))
  ]

  return allRecords
    .flatMap(({ record, sourceType }) => recordNotifications(record, sourceType, users, now))
    .filter(notification => !dismissedIds.has(String(notification.id)))
}

const deriveAllAdminNotifications = (currentUser, now = new Date()) => {
  const users = readArray(USERS_KEY)
  const dismissedIds = readDismissedIds()
  const recipients = adminRecipients(currentUser)
  const allRecords = [
    ...readArray('firenotify_tasks').map(record => ({ record, sourceType: 'Task' })),
    ...readArray('fireNotifyActivities').map(record => ({ record, sourceType: 'Activity' })),
    ...readArray('firenotify_reports').map(record => ({ record, sourceType: 'Report' }))
  ]

  return allRecords
    .flatMap(({ record, sourceType }) =>
      adminSubmissionNotifications(record, sourceType, recipients, users)
    )
    .filter(notification => !dismissedIds.has(String(notification.id)))
}

export const derivePersonnelNotifications = (currentUser, now = new Date()) => {
  const recipients = notificationIdentities(currentUser)
  return deriveAllPersonnelNotifications(now)
    .filter(notification => recipients.includes(normalize(notification.recipientId)))
}

export const mergeDerivedPersonnelNotifications = currentUser => {
  const dismissedIds = readDismissedIds()
  const existing = readNotifications().filter(item => !dismissedIds.has(String(item.id)))
  const derived = [
    ...deriveAllPersonnelNotifications(),
    ...deriveAllAdminNotifications(currentUser)
  ]
  const existingById = new Map(existing.map(item => [String(item.id), item]))

  derived.forEach(item => {
    const previous = existingById.get(item.id)
    existingById.set(item.id, previous ? { ...item, ...previous, recipientId: item.recipientId, sourceType: item.sourceType, sourceId: item.sourceId } : item)
  })

  const next = Array.from(existingById.values())
  const previousSerialized = JSON.stringify(existing)
  const nextSerialized = JSON.stringify(next)

  if (previousSerialized !== nextSerialized) {
    localStorage.setItem(NOTIFICATION_KEY, nextSerialized)
    window.dispatchEvent(new CustomEvent('fireNotifyNotificationsUpdated'))
  }

  return next
}

export const persistNotifications = items => {
  localStorage.setItem(NOTIFICATION_KEY, JSON.stringify(items))
  window.dispatchEvent(new CustomEvent('fireNotifyNotificationsUpdated'))
}

export const getPersonnelNotifications = currentUser => {
  return getNotificationsForUser(currentUser)
}

export const getNotificationsForUser = currentUser => {
  const identities = notificationIdentities(currentUser)
  const settings = currentUser?.role === 'admin' ? {} : readObject(PERSONNEL_SETTINGS_KEY)
  return readNotifications().filter(item => {
    if (!item?.recipientId && !item?.assignedToId) return false
    const belongsToUser = [item.recipientId, item.assignedToId, item.userId].map(normalize).some(identity => identities.includes(identity))
    if (!belongsToUser) return false
    const type = normalize(item.type)
    if (type.includes('task') && settings.taskNotifications === false) return false
    if (type.includes('activity') && settings.activityNotifications === false) return false
    if (type.includes('report') && settings.reportNotifications === false) return false
    if (type.includes('deadline') && settings.deadlineReminders === false) return false
    if (type.includes('support') && settings.supportNotifications === false) return false
    return !(type.includes('system') && settings.systemNotifications === false)
  })
}

export const getUnreadCountForUser = currentUser => getNotificationsForUser(currentUser).filter(item => !isNotificationRead(item)).length

export const getUnreadPersonnelCount = currentUser => getPersonnelNotifications(currentUser).filter(item => !isNotificationRead(item)).length

export const markNotificationReadForUser = (notificationId, currentUser, read = true) => {
  const identities = notificationIdentities(currentUser)
  const next = readNotifications().map(item => {
    const belongsToUser = [item.recipientId, item.assignedToId, item.userId].map(normalize).some(identity => identities.includes(identity))
    if (!belongsToUser || String(item.id) !== String(notificationId)) return item
    return { ...item, read, isRead: read, status: read ? 'read' : 'unread' }
  })
  persistNotifications(next)
  return next
}

export const markAllNotificationsReadForUser = (currentUser, read = true) => {
  const identities = notificationIdentities(currentUser)
  const next = readNotifications().map(item => {
    const belongsToUser = [item.recipientId, item.assignedToId, item.userId].map(normalize).some(identity => identities.includes(identity))
    return belongsToUser ? { ...item, read, isRead: read, status: read ? 'read' : 'unread' } : item
  })
  persistNotifications(next)
  return next
}

export const deleteNotificationForUser = (notificationId, currentUser) => {
  const identities = notificationIdentities(currentUser)
  const next = readNotifications().filter(item => {
    const belongsToUser = [item.recipientId, item.assignedToId, item.userId].map(normalize).some(identity => identities.includes(identity))
    return !belongsToUser || String(item.id) !== String(notificationId)
  })
  const dismissedIds = readDismissedIds()
  dismissedIds.add(String(notificationId))
  localStorage.setItem(DISMISSED_KEY, JSON.stringify([...dismissedIds]))

  persistNotifications(next)

  return next
}

export const deleteAllNotificationsForUser = currentUser => {
  const identities = notificationIdentities(currentUser)
  const current = readNotifications()
  const dismissedIds = readDismissedIds()
  const next = current.filter(item => {
    const belongsToUser = [item.recipientId, item.assignedToId, item.userId].map(normalize).some(identity => identities.includes(identity))
    if (belongsToUser) dismissedIds.add(String(item.id))
    return !belongsToUser
  })

  localStorage.setItem(DISMISSED_KEY, JSON.stringify([...dismissedIds]))
  persistNotifications(next)
  return next
}

export const markPersonnelNotificationRead = (notificationId, currentUser, read = true) =>
  markNotificationReadForUser(notificationId, currentUser, read)

export const markAllPersonnelNotificationsRead = (currentUser, read = true) =>
  markAllNotificationsReadForUser(currentUser, read)

export const deletePersonnelNotification = (notificationId, currentUser) =>
  deleteNotificationForUser(notificationId, currentUser)

export const readNotificationSettings = currentUser => {
  const key = `fireNotifyNotificationSettings:${currentUser?.id || currentUser?.identifier || 'unknown'}`
  return readObject(key)
}
