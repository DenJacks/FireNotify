const TASKS_URL = 'http://127.0.0.1:8000/api/tasks/'

const statusLabels = {
  ASSIGNED: 'Assigned',
  IN_PROGRESS: 'In Progress',
  FOR_VERIFICATION: 'For Verification',
  RETURNED: 'Returned',
  VERIFIED: 'Verified',
  COMPLETED: 'Completed'
}

const statusValues = Object.fromEntries(
  Object.entries(statusLabels).map(([value, label]) => [label, value])
)

export const normalizeTask = task => {
  const assignedPerson = task.assigned_to ?? task.assigned_personnel ?? task.assignedToId ?? ''
  const assignedPersonId = assignedPerson && typeof assignedPerson === 'object'
    ? assignedPerson.id ?? assignedPerson.userId ?? ''
    : assignedPerson
  const dueDate = task.due_date || task.dueDate || ''
  const status = statusLabels[task.status] || task.status || 'Assigned'
  const finalStatus = ['COMPLETED', 'VERIFIED', 'FOR_VERIFICATION'].includes(task.status)
  const deadline = dueDate ? new Date(`${dueDate}T23:59:59`) : null
  const overdue = !finalStatus && deadline && !Number.isNaN(deadline.getTime()) && deadline < new Date()

  return {
    ...task,
    status: overdue ? 'Overdue' : status,
    priority: String(task.priority || 'Medium').toLowerCase().replace(/^./, letter => letter.toUpperCase()),
    type: task.task_type || task.type || 'General Task',
    dueDate,
    time: task.due_time || task.time || '',
    assignedToId: assignedPersonId,
    assignedTo: assignedPerson,
    assignedById: task.created_by ?? task.assignedById ?? '',
    revisionNote: task.revision_note || task.revisionNote || ''
  }
}

const toTaskPayload = (task, partial = false) => {
  const fields = {
    title: task.title,
    description: task.description || '',
    task_type: task.task_type || task.type || 'General Task',
    priority: String(task.priority || 'Medium').toUpperCase(),
    location: task.location || '',
    due_date: task.due_date || task.dueDate,
    due_time: task.due_time || task.time || null,
    assigned_to: task.assigned_to ?? task.assignedToId ?? null,
    created_by: task.created_by ?? task.assignedById ?? null,
    status: statusValues[task.status] || task.status,
    progress: Number(task.progress || 0),
    accomplishment: task.accomplishment || '',
    revision_note: task.revision_note || task.revisionNote || ''
  }

  if (!partial) return fields

  const aliases = {
    title: ['title'],
    description: ['description'],
    task_type: ['task_type', 'type'],
    priority: ['priority'],
    location: ['location'],
    due_date: ['due_date', 'dueDate'],
    due_time: ['due_time', 'time'],
    assigned_to: ['assigned_to', 'assignedToId'],
    created_by: ['created_by', 'assignedById'],
    status: ['status'],
    progress: ['progress'],
    accomplishment: ['accomplishment'],
    revision_note: ['revision_note', 'revisionNote']
  }

  return Object.fromEntries(Object.entries(fields).filter(([field]) =>
    aliases[field].some(alias => Object.hasOwn(task, alias))
  ))
}

const request = async (url, options = {}) => {
  const response = await fetch(url, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...options.headers
    }
  })

  if (!response.ok) {
    const payload = await response.json().catch(() => ({}))
    throw new Error(payload.detail || payload.error || `Task API HTTP ${response.status}`)
  }

  return response.status === 204 ? null : response.json()
}

export const getTasks = async () => {
  const tasks = await request(TASKS_URL)
  if (!Array.isArray(tasks)) throw new Error('Invalid tasks response')
  return tasks.map(normalizeTask)
}

export const createTask = async task => normalizeTask(await request(TASKS_URL, {
  method: 'POST',
  body: JSON.stringify(toTaskPayload(task))
}))

export const updateTask = async (id, changes) => normalizeTask(await request(`${TASKS_URL}${id}/`, {
  method: 'PATCH',
  body: JSON.stringify(toTaskPayload(changes, true))
}))

export const deleteTask = id => request(`${TASKS_URL}${id}/`, { method: 'DELETE' })