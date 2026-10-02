const API_URL = 'http://127.0.0.1:8000/api'

const readResponse = async response => {
  if (!response.ok) {
    const payload = await response.json().catch(() => ({}))
    const detail = payload.detail || payload.error || Object.values(payload).flat().join(' ')
    throw new Error(detail || `Reports API HTTP ${response.status}`)
  }
  return response.status === 204 ? null : response.json()
}

const jsonRequest = (url, method, body) => fetch(url, {
  method,
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(body)
})

export const getReports = async () => {
  const reports = await readResponse(await fetch(`${API_URL}/reports/`))
  if (!Array.isArray(reports)) throw new Error('Invalid reports response')
  return reports
}

export const createReport = async report => readResponse(await jsonRequest(
  `${API_URL}/reports/`,
  'POST',
  report
))

export const updateReport = async (id, report) => readResponse(await jsonRequest(
  `${API_URL}/reports/${id}/`,
  'PATCH',
  report
))

export const deleteReport = async id => readResponse(await fetch(`${API_URL}/reports/${id}/`, {
  method: 'DELETE'
}))

export const getReportSubmissions = async personnelId => {
  const query = personnelId ? `?personnel=${encodeURIComponent(personnelId)}` : ''
  const submissions = await readResponse(await fetch(`${API_URL}/report-submissions/${query}`))
  if (!Array.isArray(submissions)) throw new Error('Invalid report submissions response')
  return submissions
}

export const getPersonnelReportSubmissions = personnelId =>
  personnelId ? getReportSubmissions(personnelId) : Promise.resolve([])

export const updateReportSubmission = async (id, values, personnelId = null) => {
  const query = personnelId ? `?personnel=${encodeURIComponent(personnelId)}` : ''
  const url = `${API_URL}/report-submissions/${id}/${query}`
  let response

  if (values.attachment instanceof File) {
    const formData = new FormData()
    Object.entries(values).forEach(([key, value]) => {
      if (value !== undefined && value !== null) formData.append(key, value)
    })
    response = await fetch(url, { method: 'PATCH', body: formData })
  } else {
    response = await jsonRequest(url, 'PATCH', values)
  }

  return readResponse(response)
}