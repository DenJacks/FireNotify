const SETTINGS_KEY = 'firenotify_personnel_settings'
export const SETTINGS_UPDATED_EVENT = 'fireNotifyPersonnelSettingsUpdated'

export const DEFAULT_PERSONNEL_SETTINGS = {
  theme: 'light',
  fontSize: 'medium',
  reduceMotion: false,
  highContrast: false,
  largeText: false,
  largerTargets: false,
  taskNotifications: true,
  activityNotifications: true,
  reportNotifications: true,
  deadlineReminders: true,
  supportNotifications: true,
  systemNotifications: true,
  notificationSound: false,
  showNotificationBadge: true
}

const readSettings = () => {
  try {
    const saved = JSON.parse(localStorage.getItem(SETTINGS_KEY) || '{}')
    return { ...DEFAULT_PERSONNEL_SETTINGS, ...(saved && typeof saved === 'object' ? saved : {}) }
  } catch {
    return { ...DEFAULT_PERSONNEL_SETTINGS }
  }
}

export const getPersonnelSettings = () => readSettings()

export const savePersonnelSettings = updates => {
  const settings = { ...readSettings(), ...updates }
  localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings))
  window.dispatchEvent(new CustomEvent(SETTINGS_UPDATED_EVENT, { detail: settings }))
  return settings
}

export const resetPersonnelSettings = keys => {
  const updates = {}
  const fields = Array.isArray(keys) ? keys : Object.keys(DEFAULT_PERSONNEL_SETTINGS)
  fields.forEach(key => { updates[key] = DEFAULT_PERSONNEL_SETTINGS[key] })
  return savePersonnelSettings(updates)
}

export const applyPersonnelSettings = settings => {
  const root = document.documentElement
  const resolvedTheme = settings.theme === 'system'
    ? (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')
    : settings.theme

  root.dataset.personnelTheme = resolvedTheme
  root.dataset.personnelFontSize = settings.fontSize
  root.classList.toggle('fn-reduce-motion', settings.reduceMotion)
  root.classList.toggle('fn-high-contrast', settings.highContrast)
  root.classList.toggle('fn-large-text', settings.largeText)
  root.classList.toggle('fn-larger-targets', settings.largerTargets)
}

export const initializePersonnelSettings = () => {
  const settings = readSettings()
  applyPersonnelSettings(settings)
  return settings
}

export { SETTINGS_KEY }
