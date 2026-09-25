const USERS_STORAGE_KEY = 'fireNotifyRegisteredUsers'
const FALLBACK_NAME = 'Personnel unavailable'

const normalize = value => String(value ?? '').trim().toLowerCase()

const titleCase = value => String(value)
  .trim()
  .replace(/\s+/g, ' ')
  .replace(/(^|[\s'-])([a-z])/g, (_, prefix, letter) => `${prefix}${letter.toUpperCase()}`)

const readStoredUsers = () => {
  if (typeof localStorage === 'undefined') return []

  try {
    const parsed = JSON.parse(localStorage.getItem(USERS_STORAGE_KEY) || '[]')
    return Array.isArray(parsed) ? parsed : []
  } catch {
    return []
  }
}

const identityValues = value => [
  ...(typeof value === 'string' || typeof value === 'number' ? [value] : []),
  value?.id,
  value?.userId,
  value?.identifier,
  value?.username,
  value?.email,
  value?.name,
  value?.firstName && value?.lastName
    ? `${value.firstName} ${value.lastName}`
    : ''
].map(normalize).filter(Boolean)

const personName = value => {
  if (!value || typeof value !== 'object') return ''

  return value.name ||
    `${value.firstName || ''} ${value.lastName || ''}`.trim()
}

const parseValue = value => {
  if (typeof value !== 'string') return value

  const text = value.trim()
  if (!text) return ''

  try {
    return JSON.parse(text)
  } catch {
    return value
  }
}

const findRegisteredUser = (value, registeredUsers) => {
  const identities = identityValues(value)
  if (!identities.length) return null

  return registeredUsers.find(user =>
    identityValues(user).some(identity => identities.includes(identity))
  ) || null
}

const resolveSinglePersonnelName = (value, registeredUsers) => {
  const parsed = parseValue(value)
  const users = Array.isArray(registeredUsers) && registeredUsers.length
    ? registeredUsers
    : readStoredUsers()

  if (!parsed || (typeof parsed !== 'object' && typeof parsed !== 'string')) {
    return ''
  }

  const registeredUser = findRegisteredUser(parsed, users)
  const name = personName(registeredUser) || personName(parsed)
  const plainName = typeof parsed === 'string' && /\s/.test(parsed)
    ? parsed
    : ''

  return titleCase(name || plainName)
}

export const resolvePersonnelNames = (value, registeredUsers = []) => {
  const parsed = parseValue(value)
  const values = Array.isArray(parsed) ? parsed : [parsed]

  return values
    .map(item => resolveSinglePersonnelName(item, registeredUsers))
    .filter(Boolean)
}

export const resolvePersonnelName = (value, registeredUsers = [], fallback = FALLBACK_NAME) => {
  const names = resolvePersonnelNames(value, registeredUsers)
  return names.length ? names.join(', ') : fallback
}

export { FALLBACK_NAME }
