const NOTIFICATIONS_URL = 'http://127.0.0.1:8000/api/notifications/'

const request = async (url, options = {}) => {
  const response = await fetch(url, {
    ...options,
    headers: { 'Content-Type': 'application/json', ...options.headers }
  })
  if (!response.ok) throw new Error(`Notifications API HTTP ${response.status}`)
  return response.status === 204 ? null : response.json()
}

export const getNotifications = async user => {
  if (!user?.id) return []
  const records = await request(`${NOTIFICATIONS_URL}?recipient=${encodeURIComponent(user.id)}`)
  if (!Array.isArray(records)) return []
  return records.map(item => ({
    ...item,
    type: item.notification_type,
    detail: item.message,
    read: item.is_read,
    recipientId: item.recipient,
    createdAt: item.created_at
  }))
}

export const setNotificationRead = (notification, user, isRead) => request(
  `${NOTIFICATIONS_URL}${notification.id}/?recipient=${encodeURIComponent(user.id)}`,
  { method: 'PATCH', body: JSON.stringify({ is_read: isRead }) }
)

export const deleteNotification = (notification, user) => request(
  `${NOTIFICATIONS_URL}${notification.id}/?recipient=${encodeURIComponent(user.id)}`,
  { method: 'DELETE' }
)

export const markAllNotificationsRead = user => request(`${NOTIFICATIONS_URL}mark-all-read/`, {
  method: 'POST',
  body: JSON.stringify({ recipient: user?.id })
})