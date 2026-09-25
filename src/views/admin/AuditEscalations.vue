<script setup>
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'

import { resolvePersonnelName } from '../../utils/personnelName.js'

const props = defineProps({
  currentUser: { type: Object, default: null },
  registeredUsers: { type: Array, default: () => [] }
})

const STORAGE_KEYS = {
  tasks: 'firenotify_tasks',
  activities: 'fireNotifyActivities',
  reports: 'firenotify_reports',
  escalationMeta: 'fireNotifyEscalationMetadata'
}

const UPDATE_EVENTS = [
  'fireNotifyActivitiesUpdated',
  'fireNotifyTasksUpdated',
  'fireNotifyReportsUpdated',
  'fireNotifyRegisteredUsersUpdated',
  'fireNotifyUsersUpdated',
  'fireNotifyNotificationsUpdated'
]

const records = ref([])
const escalationMetadata = ref({})
const searchQuery = ref('')
const issueFilter = ref('All')
const sourceFilter = ref('All')
const selectedRecord = ref(null)
const toastMessage = ref('')
let refreshTimer = null

const readArray = key => {
  try {
    const value = JSON.parse(localStorage.getItem(key) || '[]')
    return Array.isArray(value) ? value : []
  } catch {
    return []
  }
}

const readObject = key => {
  try {
    const value = JSON.parse(localStorage.getItem(key) || '{}')
    return value && typeof value === 'object' && !Array.isArray(value) ? value : {}
  } catch {
    return {}
  }
}

const normalize = value => String(value ?? '').trim().toLowerCase()
const statusOf = record => normalize(record?.status || record?.submissionStatus)
const titleOf = record => record?.title || record?.name || record?.activityName || 'Untitled record'
const deadlineOf = record => record?.deadline || record?.dueDate || record?.deadlineDate || record?.date || record?.schedule || ''
const assignedValueOf = record => record?.assignedPersonnel || record?.assignedToId || record?.assignedToName || record?.assignedTo || record?.personnel || record?.submittedBy || ''
const personnelOf = record => resolvePersonnelName(assignedValueOf(record), props.registeredUsers, 'Personnel unavailable')

const parseDate = value => {
  if (!value) return null
  const date = value instanceof Date ? new Date(value) : new Date(String(value).replace('•', ' '))
  return Number.isNaN(date.getTime()) ? null : date
}

const isFinalStatus = record => [
  'verified', 'completed', 'complete', 'approved', 'closed', 'resolved', 'done', 'finished'
].includes(statusOf(record))

const returnCountOf = record => {
  const history = record?.revisionHistory || record?.returnHistory || record?.returns
  return Math.max(
    Number(record?.revisionCount || 0),
    Number(record?.returnCount || 0),
    Array.isArray(history) ? history.length : 0
  )
}

const buildSourceRecords = () => {
  records.value = [
    ...readArray(STORAGE_KEYS.tasks).map(record => ({ ...record, sourceType: 'Task' })),
    ...readArray(STORAGE_KEYS.activities).map(record => ({ ...record, sourceType: 'Activity' })),
    ...readArray(STORAGE_KEYS.reports).map(record => ({ ...record, sourceType: 'Report' }))
  ]
}

const issueFor = record => {
  const status = statusOf(record)
  const deadline = parseDate(deadlineOf(record))

  if (status === 'for verification' || status === 'for review') return 'Pending Verification'
  if (status === 'returned' || status === 'needs revision' || status === 'revision required') return 'Returned / Needs Revision'
  if (deadline && deadline.getTime() < Date.now() && !isFinalStatus(record)) return 'Overdue'
  return ''
}

const sourceRecords = computed(() => records.value)

const escalationRecords = computed(() => sourceRecords.value
  .map(record => {
    const issue = issueFor(record)
    if (!issue) return null

    const key = `${record.sourceType}:${record.id}:${issue}`
    const metadata = escalationMetadata.value[key] || {}

    if (metadata.status === 'RESOLVED') return null

    return {
      ...record,
      key,
      issue,
      repeated: returnCountOf(record) > 1,
      personnel: personnelOf(record),
      title: titleOf(record),
      deadline: deadlineOf(record),
      detectedAt: record.returnedAt || record.submittedAt || record.updatedAt || record.createdAt || deadlineOf(record),
      escalationStatus: metadata.status || 'OPEN'
    }
  })
  .filter(Boolean))

const filteredEscalations = computed(() => {
  const query = normalize(searchQuery.value)

  return escalationRecords.value.filter(record => {
    const matchesSearch = !query || [record.title, record.personnel, record.issue, record.sourceType, record.id]
      .some(value => normalize(value).includes(query))
    const matchesIssue = issueFilter.value === 'All' || record.issue === issueFilter.value
    const matchesSource = sourceFilter.value === 'All' || record.sourceType === sourceFilter.value
    return matchesSearch && matchesIssue && matchesSource
  })
})

const pendingVerificationCount = computed(() => escalationRecords.value.filter(item => item.issue === 'Pending Verification').length)
const overdueCount = computed(() => escalationRecords.value.filter(item => item.issue === 'Overdue').length)
const returnedCount = computed(() => escalationRecords.value.filter(item => item.issue === 'Returned / Needs Revision').length)

const auditEvents = computed(() => sourceRecords.value
  .flatMap(record => {
    const events = []
    const add = (event, timestamp, status = record.status || record.submissionStatus) => {
      if (timestamp) {
        events.push({
          id: `${record.sourceType}:${record.id}:${event}`,
          timestamp,
          event,
          record: titleOf(record),
          sourceType: record.sourceType,
          sourceId: record.id,
          personnel: personnelOf(record),
          status: status || 'Recorded'
        })
      }
    }

    add('Record created', record.createdAt)
    add('Assignment recorded', record.assignedAt, 'Assigned')
    add('Started', record.startedAt, 'In Progress')
    add('Submitted for verification', record.submittedAt, 'For Verification')
    add('Returned for revision', record.returnedAt, 'Returned')
    add('Verified', record.verifiedAt, 'Verified')

    if (!events.length) {
      add(`Current status: ${record.status || record.submissionStatus || 'Unknown'}`, record.updatedAt)
    }

    return events
  })
  .sort((left, right) => (parseDate(right.timestamp)?.getTime() || 0) - (parseDate(left.timestamp)?.getTime() || 0)))

const formatDateTime = value => {
  const date = parseDate(value)
  return date ? date.toLocaleString('en-US', { month: 'short', day: 'numeric', year: 'numeric', hour: 'numeric', minute: '2-digit' }) : 'Not recorded'
}

const formatDate = value => {
  const date = parseDate(value)
  return date ? date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }) : 'No deadline'
}

const priorityOf = record => {
  if (issueFor(record) === 'Overdue' || returnCountOf(record) > 1) return 'High'
  if (issueFor(record) === 'Pending Verification' || issueFor(record) === 'Returned / Needs Revision') return 'Medium'
  return 'Low'
}

const issueClass = issue => issue === 'Overdue'
  ? 'bg-red-100 text-red-700'
  : issue === 'Pending Verification'
    ? 'bg-yellow-100 text-yellow-700'
    : 'bg-orange-100 text-orange-700'

const priorityClass = priority => ({
  High: 'bg-red-100 text-red-700',
  Medium: 'bg-yellow-100 text-yellow-700',
  Low: 'bg-blue-100 text-blue-700'
}[priority] || 'bg-slate-100 text-slate-700')

const loadData = () => {
  escalationMetadata.value = readObject(STORAGE_KEYS.escalationMeta)
  buildSourceRecords()
}

const saveMetadata = () => {
  localStorage.setItem(STORAGE_KEYS.escalationMeta, JSON.stringify(escalationMetadata.value))
}

const showNotification = message => {
  toastMessage.value = message
  window.setTimeout(() => { toastMessage.value = '' }, 2500)
}

const setEscalationStatus = (record, status) => {
  escalationMetadata.value = {
    ...escalationMetadata.value,
    [record.key]: { ...(escalationMetadata.value[record.key] || {}), status }
  }
  saveMetadata()
  showNotification(`Escalation marked ${status.toLowerCase()}.`)
}

const refresh = () => loadData()

onMounted(() => {
  loadData()
  UPDATE_EVENTS.forEach(eventName => window.addEventListener(eventName, refresh))
  window.addEventListener('storage', refresh)
  refreshTimer = window.setInterval(refresh, 30000)
})

onBeforeUnmount(() => {
  UPDATE_EVENTS.forEach(eventName => window.removeEventListener(eventName, refresh))
  window.removeEventListener('storage', refresh)
  window.clearInterval(refreshTimer)
})
</script>

<template>
  <div class="space-y-6">
    <transition name="fade">
      <div v-if="toastMessage" class="fixed top-6 right-6 z-[100] bg-slate-900 text-white px-5 py-3 rounded-xl shadow-lg text-sm font-semibold">{{ toastMessage }}</div>
    </transition>
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
        <div>
          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">Governance Overview</p>
          <h2 class="text-2xl font-bold text-slate-900 mt-1">Audit & Escalations</h2>
          <p class="text-base text-slate-500 mt-1">Live monitoring of tasks, activities, and reports.</p>
        </div>
        <span class="px-4 py-2 rounded-xl bg-green-50 border border-green-200 text-sm font-bold text-green-700">Live data</span>
      </div>
    </section>

    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><p class="text-3xl font-bold text-[#8B1E23]">{{ escalationRecords.length }}</p><p class="text-sm text-slate-500 mt-1">Active Escalations</p></div>
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><p class="text-3xl font-bold text-yellow-600">{{ pendingVerificationCount }}</p><p class="text-sm text-slate-500 mt-1">Pending Verification</p></div>
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><p class="text-3xl font-bold text-red-600">{{ overdueCount }}</p><p class="text-sm text-slate-500 mt-1">Overdue</p></div>
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><p class="text-3xl font-bold text-orange-600">{{ returnedCount }}</p><p class="text-sm text-slate-500 mt-1">Returned / Needs Revision</p></div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">
      <div class="flex flex-col lg:flex-row gap-4">
        <input v-model="searchQuery" type="text" placeholder="Search live records, personnel, or issue..." class="flex-1 px-4 py-3 border border-slate-200 rounded-xl outline-none focus:border-[#8B1E23]" />
        <select v-model="issueFilter" class="px-4 py-3 border border-slate-200 rounded-xl bg-white outline-none"><option value="All">All Issues</option><option value="Overdue">Overdue</option><option value="Pending Verification">Pending Verification</option><option value="Returned / Needs Revision">Returned / Needs Revision</option></select>
        <select v-model="sourceFilter" class="px-4 py-3 border border-slate-200 rounded-xl bg-white outline-none"><option value="All">All Sources</option><option value="Task">Tasks</option><option value="Activity">Activities</option><option value="Report">Reports</option></select>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex items-center justify-between border-b border-slate-200 pb-5"><div><h2 class="text-xl font-bold text-slate-900">Active Escalations</h2><p class="text-sm text-slate-500 mt-1">Exceptions derived from current operational records.</p></div><span class="px-3 py-1 rounded-full bg-red-100 text-red-700 text-xs font-bold">{{ filteredEscalations.length }} Active</span></div>
      <div v-if="filteredEscalations.length" class="mt-5 overflow-x-auto"><table class="w-full text-left"><thead><tr class="border-b border-slate-200 text-xs font-bold uppercase tracking-wide text-slate-400"><th class="pb-4 pr-4">Issue</th><th class="pb-4 pr-4">Source</th><th class="pb-4 pr-4">Personnel</th><th class="pb-4 pr-4">Due Date</th><th class="pb-4 pr-4">Detected</th><th class="pb-4 pr-4">Status</th><th class="pb-4 text-right">Action</th></tr></thead><tbody class="divide-y divide-slate-100"><tr v-for="record in filteredEscalations" :key="record.key"><td class="py-4 pr-4"><p class="font-bold text-slate-900">{{ record.title }}</p><span class="inline-block mt-1 px-2 py-1 rounded-full text-xs font-bold" :class="issueClass(record.issue)">{{ record.issue }}</span><span v-if="record.repeated" class="ml-2 text-xs font-bold text-red-600">Repeated returns</span></td><td class="py-4 pr-4"><p class="text-sm font-semibold text-slate-700">{{ record.sourceType }}</p><p class="text-xs text-slate-400">{{ record.id }}</p></td><td class="py-4 pr-4 text-sm text-slate-700">{{ record.personnel }}</td><td class="py-4 pr-4 text-sm text-slate-600">{{ formatDate(record.deadline) }}</td><td class="py-4 pr-4 text-sm text-slate-600">{{ formatDateTime(record.detectedAt) }}</td><td class="py-4 pr-4"><span class="px-2 py-1 rounded-full text-xs font-bold" :class="priorityClass(priorityOf(record))">{{ record.escalationStatus }}</span></td><td class="py-4 text-right"><button @click="selectedRecord = record" class="px-3 py-2 rounded-lg bg-slate-100 text-slate-700 text-xs font-bold hover:bg-slate-200">View Record</button></td></tr></tbody></table></div>
      <div v-else class="py-12 text-center"><p class="text-3xl text-green-600">✓</p><p class="font-bold text-slate-700 mt-2">No active escalations</p><p class="text-sm text-slate-500 mt-1">All monitored records are currently within compliance.</p></div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><div class="border-b border-slate-200 pb-5"><h2 class="text-xl font-bold text-slate-900">Audit Log</h2><p class="text-sm text-slate-500 mt-1">Events derived from timestamps stored on operational records.</p></div><div v-if="auditEvents.length" class="mt-5 overflow-x-auto"><table class="w-full text-left"><thead><tr class="border-b border-slate-200 text-xs font-bold uppercase tracking-wide text-slate-400"><th class="pb-4 pr-4">Date / Time</th><th class="pb-4 pr-4">Event</th><th class="pb-4 pr-4">Record</th><th class="pb-4 pr-4">Personnel</th><th class="pb-4">Status</th></tr></thead><tbody class="divide-y divide-slate-100"><tr v-for="event in auditEvents" :key="event.id"><td class="py-4 pr-4 text-sm text-slate-600">{{ formatDateTime(event.timestamp) }}</td><td class="py-4 pr-4 text-sm font-semibold text-slate-800">{{ event.event }}</td><td class="py-4 pr-4"><p class="text-sm font-semibold text-slate-700">{{ event.record }}</p><p class="text-xs text-slate-400">{{ event.sourceType }} · {{ event.sourceId }}</p></td><td class="py-4 pr-4 text-sm text-slate-700">{{ event.personnel }}</td><td class="py-4 text-sm text-slate-600">{{ event.status }}</td></tr></tbody></table></div><div v-else class="py-10 text-center text-sm text-slate-500">No audit events available.</div></section>

    <div v-if="selectedRecord" class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4" @click.self="selectedRecord = null"><div class="bg-white rounded-2xl shadow-2xl w-full max-w-xl max-h-[90vh] overflow-y-auto"><div class="p-6 border-b border-slate-200 flex justify-between"><div><p class="text-xs font-bold text-[#8B1E23]">{{ selectedRecord.sourceType }} · {{ selectedRecord.id }}</p><h2 class="text-xl font-bold text-slate-900 mt-1">{{ selectedRecord.title }}</h2></div><button @click="selectedRecord = null" class="text-2xl text-slate-400">×</button></div><div class="p-6 space-y-5"><div class="flex flex-wrap gap-2"><span class="px-3 py-1 rounded-full text-xs font-bold" :class="issueClass(selectedRecord.issue)">{{ selectedRecord.issue }}</span><span class="px-3 py-1 rounded-full text-xs font-bold" :class="priorityClass(priorityOf(selectedRecord))">{{ priorityOf(selectedRecord) }} priority</span></div><div class="grid grid-cols-2 gap-5"><div><p class="text-xs uppercase font-bold text-slate-400">Assigned Personnel</p><p class="font-semibold text-slate-800 mt-1">{{ selectedRecord.personnel }}</p></div><div><p class="text-xs uppercase font-bold text-slate-400">Current Status</p><p class="font-semibold text-slate-800 mt-1">{{ selectedRecord.status || selectedRecord.submissionStatus || 'Not recorded' }}</p></div><div><p class="text-xs uppercase font-bold text-slate-400">Deadline</p><p class="font-semibold text-slate-800 mt-1">{{ formatDate(selectedRecord.deadline) }}</p></div><div><p class="text-xs uppercase font-bold text-slate-400">Detected</p><p class="font-semibold text-slate-800 mt-1">{{ formatDateTime(selectedRecord.detectedAt) }}</p></div></div><div v-if="selectedRecord.description || selectedRecord.accomplishment || selectedRecord.submissionNote || selectedRecord.revisionNote"><p class="text-xs uppercase font-bold text-slate-400">Record details</p><p class="text-sm text-slate-600 mt-1">{{ selectedRecord.description || selectedRecord.accomplishment || selectedRecord.submissionNote || selectedRecord.revisionNote }}</p></div></div><div class="p-6 border-t border-slate-200 flex flex-wrap justify-end gap-3"><button v-if="selectedRecord.escalationStatus === 'OPEN'" @click="setEscalationStatus(selectedRecord, 'ACKNOWLEDGED')" class="px-4 py-2 rounded-xl bg-yellow-100 text-yellow-800 font-bold">Acknowledge</button><button v-if="selectedRecord.escalationStatus === 'ACKNOWLEDGED'" @click="setEscalationStatus(selectedRecord, 'UNDER REVIEW')" class="px-4 py-2 rounded-xl bg-blue-100 text-blue-800 font-bold">Under Review</button><button @click="setEscalationStatus(selectedRecord, 'RESOLVED')" class="px-4 py-2 rounded-xl bg-green-100 text-green-800 font-bold">Resolve</button><button @click="selectedRecord = null" class="px-4 py-2 rounded-xl bg-slate-100 text-slate-700 font-bold">Close</button></div></div></div>
  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active { transition: opacity 0.2s ease; }
.fade-enter-from,
.fade-leave-to { opacity: 0; }
</style>
