const dateFormatter = new Intl.DateTimeFormat('en-US', {
  month: 'short',
  day: 'numeric',
  year: 'numeric'
})

const timeFormatter = new Intl.DateTimeFormat('en-US', {
  hour: 'numeric',
  minute: '2-digit'
})

const parseDate = value => {
  if (!value) return null
  if (value instanceof Date) return Number.isNaN(value.getTime()) ? null : value

  const raw = String(value).trim()
  const dateOnly = raw.match(/^(\d{4})-(\d{2})-(\d{2})$/)
  const date = dateOnly
    ? new Date(Number(dateOnly[1]), Number(dateOnly[2]) - 1, Number(dateOnly[3]))
    : new Date(raw)
  return Number.isNaN(date.getTime()) ? null : date
}

export const formatOperationDate = value => {
  const date = parseDate(value)
  return date ? dateFormatter.format(date) : value ? 'Date unavailable' : 'Not specified'
}

export const formatOperationTime = value => {
  if (!value) return 'Not specified'

  const raw = String(value).trim()
  const match = raw.match(/^(\d{1,2}):(\d{2})(?::\d{2})?\s*(AM|PM)?$/i)

  if (match) {
    let hours = Number(match[1])
    const minutes = Number(match[2])
    const meridiem = match[3]?.toUpperCase()

    if (hours > 23 || minutes > 59) return 'Time unavailable'
    if (meridiem) {
      hours = hours % 12 + (meridiem === 'PM' ? 12 : 0)
    }

    const date = new Date(2000, 0, 1, hours, minutes)
    return timeFormatter.format(date)
  }

  const date = parseDate(raw)
  return date ? timeFormatter.format(date) : 'Time unavailable'
}

export const formatOperationDateTime = value => {
  if (!value) return 'Not submitted'

  const raw = String(value).trim()
  const dateOnly = /^(?:\d{4}-\d{2}-\d{2}|\d{1,2}\/\d{1,2}\/\d{2,4}|[A-Za-z]{3,9}\s+\d{1,2},?\s+\d{4})$/.test(raw)
  if (dateOnly) return formatOperationDate(raw)

  const date = parseDate(value)
  return date
    ? `${dateFormatter.format(date)} · ${timeFormatter.format(date)}`
    : 'Date unavailable'
}
