<script setup>
import { computed, onMounted, onUnmounted, ref } from 'vue'

const props = defineProps({
  currentUser: { type: Object, default: null },
  personnel: { type: Array, default: () => [] },
  totalPersonnel: { type: Number, default: 0 },
  activePersonnel: { type: Number, default: 0 },
  activities: { type: Array, default: () => [] },
  reports: { type: Array, default: () => [] },
  pendingReports: { type: Number, default: 0 },
  activityCompliance: { type: Number, default: 0 },
  reportCompliance: { type: Number, default: 0 },
  deadlineCompliance: { type: Number, default: 0 },
  verifiedActivities: { type: Number, default: 0 },
  overdueActivities: { type: Number, default: 0 },
  overdueDeadlines: { type: Number, default: 0 },
  overdueReports: { type: Array, default: () => [] },
  reviewedReports: { type: Number, default: 0 },
  totalDeadlines: { type: Number, default: 0 },
  unreadNotifications: { type: Number, default: 0 },
  recentActivities: { type: Array, default: () => [] },
  recentReports: { type: Array, default: () => [] },
  activityPerson: { type: Function, default: () => '' },
  reportPerson: { type: Function, default: () => '' },
  tasks: { type: Array, default: () => [] },
  notifications: { type: Array, default: () => [] }
})

const normalize = value => String(value || '').trim().toLowerCase()
const isComplete = value => ['completed', 'complete', 'done', 'finished', 'closed', 'approved', 'reviewed', 'resolved', 'verified'].includes(normalize(value))
const recordDate = item => item?.deadline || item?.dueDate || item?.activity_date || item?.activityDate || item?.date || item?.updatedAt || item?.updated_at || item?.createdAt || item?.created_at || item?.submitted_at || ''
const parsedDate = value => {
  const date = value ? new Date(String(value).replace(/•/g, ' ').trim()) : null
  return date && !Number.isNaN(date.getTime()) ? date : null
}
const isOverdue = item => {
  if (isComplete(item?.status) || normalize(item?.status) === 'overdue') return normalize(item?.status) === 'overdue'
  const date = parsedDate(recordDate(item))
  if (!date) return false
  if (/^\d{4}-\d{2}-\d{2}$/.test(String(recordDate(item)))) date.setHours(23, 59, 59, 999)
  return date < new Date()
}
const titleOf = item => item?.title || item?.name || item?.report_title || item?.type || 'Untitled item'
const pendingPersonnel = computed(() => props.personnel.filter(user => normalize(user?.status) === 'pending'))

const urgentItems = computed(() => {
  const items = []
  props.activities.forEach(item => {
    const status = normalize(item?.status)
    if (isOverdue(item)) items.push({ id: `activity-overdue-${item.id}`, title: titleOf(item), detail: 'Overdue activity', tone: 'red' })
    else if (['for verification', 'for_verification'].includes(status)) items.push({ id: `activity-review-${item.id}`, title: titleOf(item), detail: 'Activity awaiting verification', tone: 'amber' })
  })
  props.tasks.filter(isOverdue).forEach(item => items.push({ id: `task-${item.id}`, title: titleOf(item), detail: 'Overdue task', tone: 'red' }))
  props.reports.forEach(item => {
    const status = normalize(item?.status)
    if (isOverdue(item)) items.push({ id: `report-overdue-${item.id}`, title: titleOf(item), detail: 'Overdue report', tone: 'red' })
    else if (['for review', 'returned', 'pending submission'].includes(status)) items.push({ id: `report-review-${item.id}`, title: titleOf(item), detail: status === 'returned' ? 'Report returned for revision' : 'Report awaiting review', tone: 'amber' })
  })
  pendingPersonnel.value.forEach(user => items.push({
    id: `approval-${user.id}`,
    title: user.name || `${user.first_name || user.firstName || ''} ${user.last_name || user.lastName || ''}`.trim() || user.username || 'Personnel account',
    detail: 'Account approval pending',
    tone: 'amber'
  }))
  props.notifications.filter(item => {
    const unread = !(item?.read || item?.isRead || item?.is_read)
    return unread && /urgent|overdue|verification|review|approval|pending/i.test(`${item?.title || ''} ${item?.message || ''} ${item?.notification_type || ''}`)
  }).forEach(item => items.push({ id: `notification-${item.id}`, title: item.title || 'Operational alert', detail: item.message || 'Unread notification', tone: 'amber' }))
  return items
})

const recentTimestamp = item => item?.updatedAt || item?.updated_at || item?.createdAt || item?.created_at || item?.submitted_at || item?.submittedDate || item?.activity_date || item?.date || item?.deadline || item?.dueDate || ''
const recentItems = computed(() => [
  ...props.recentActivities.map(item => ({ ...item, kind: 'Activity' })),
  ...props.recentReports.map(item => ({ ...item, kind: 'Report' })),
  ...props.tasks.map(item => ({ ...item, kind: 'Task' })),
  ...props.notifications.map(item => ({ ...item, kind: 'Notification' }))
].sort((left, right) => (parsedDate(recentTimestamp(right))?.getTime() || 0) - (parsedDate(recentTimestamp(left))?.getTime() || 0)).slice(0, 5))

const activityCount = status => props.activities.filter(item => normalize(item?.status) === status).length
const verificationCount = computed(() => props.activities.filter(item => ['for verification', 'for_verification'].includes(normalize(item?.status))).length)
const scheduledCount = computed(() => activityCount('scheduled'))
const ongoingCount = computed(() => activityCount('ongoing'))
const delayedCount = computed(() => props.overdueActivities + props.activities.filter(item => normalize(item?.status) === 'delayed' && !isOverdue(item)).length)
const alertCount = computed(() => urgentItems.value.length)
const countStatus = (records, statuses) => records.filter(item => statuses.includes(normalize(item?.status))).length
const pendingApprovalCount = computed(() => pendingPersonnel.value.length)
const approvedPersonnelCount = computed(() => countStatus(props.personnel, ['approved']))
const inactivePersonnelCount = computed(() => Math.max(0, props.totalPersonnel - props.activePersonnel))
const reportStatusCounts = computed(() => ({
  pending: countStatus(props.reports, ['pending', 'pending submission']),
  submitted: countStatus(props.reports, ['submitted']),
  verified: props.reviewedReports,
  returned: countStatus(props.reports, ['returned']),
  overdue: props.overdueReports.length
}))
const taskStatusCounts = computed(() => ({
  assigned: countStatus(props.tasks, ['assigned', 'pending']),
  inProgress: countStatus(props.tasks, ['in progress', 'ongoing']),
  verification: countStatus(props.tasks, ['for verification']),
  completed: countStatus(props.tasks, ['verified', 'completed', 'complete']),
  overdue: props.tasks.filter(item => isOverdue(item)).length
}))
const taskCompliance = computed(() => props.tasks.length
  ? Math.round((taskStatusCounts.value.completed / props.tasks.length) * 100)
  : 0)
const percentOf = (value, total) => total ? Math.min(100, Math.round(value / total * 100)) : 0
const personnelRows = computed(() => [
  { label: 'Registered', value: props.totalPersonnel },
  { label: 'Active', value: props.activePersonnel },
  { label: 'Pending approval', value: pendingApprovalCount.value },
  { label: 'Approved', value: approvedPersonnelCount.value },
  { label: 'Inactive / other', value: inactivePersonnelCount.value }
])
const activityRows = computed(() => [
  { label: 'Scheduled', value: scheduledCount.value, tone: 'bg-slate-400' },
  { label: 'Ongoing', value: ongoingCount.value, tone: 'bg-blue-700' },
  { label: 'Completed', value: props.verifiedActivities, tone: 'bg-emerald-700' },
  { label: 'For verification', value: verificationCount.value, tone: 'bg-amber-500' },
  { label: 'Overdue / delayed', value: delayedCount.value, tone: 'bg-red-700' }
])
const reportRows = computed(() => [
  { label: 'Pending', value: reportStatusCounts.value.pending, tone: 'bg-amber-500' },
  { label: 'Submitted', value: reportStatusCounts.value.submitted, tone: 'bg-blue-700' },
  { label: 'Verified', value: reportStatusCounts.value.verified, tone: 'bg-emerald-700' },
  { label: 'Returned', value: reportStatusCounts.value.returned, tone: 'bg-orange-600' },
  { label: 'Overdue', value: reportStatusCounts.value.overdue, tone: 'bg-red-700' }
])
const taskRows = computed(() => [
  { label: 'Assigned', value: taskStatusCounts.value.assigned, tone: 'bg-slate-500' },
  { label: 'In progress', value: taskStatusCounts.value.inProgress, tone: 'bg-blue-700' },
  { label: 'For verification', value: taskStatusCounts.value.verification, tone: 'bg-amber-500' },
  { label: 'Completed', value: taskStatusCounts.value.completed, tone: 'bg-emerald-700' },
  { label: 'Overdue', value: taskStatusCounts.value.overdue, tone: 'bg-red-700' }
])
const operationalStatus = computed(() => [
  { label: 'Personnel active', detail: `${props.activePersonnel} of ${props.totalPersonnel}`, value: props.totalPersonnel ? Math.round(props.activePersonnel / props.totalPersonnel * 100) : 0, tone: 'bg-[#8B1E23]' },
  { label: 'Activity compliance', detail: `${props.verifiedActivities} verified`, value: props.activityCompliance, tone: 'bg-emerald-700' },
  { label: 'Report compliance', detail: `${props.reviewedReports} verified`, value: props.reportCompliance, tone: 'bg-amber-600' },
  { label: 'Task completion', detail: `${taskStatusCounts.value.completed} completed`, value: taskCompliance.value, tone: 'bg-blue-700' },
  { label: 'Deadline compliance', detail: `${props.overdueDeadlines + props.overdueReports.length} overdue`, value: props.deadlineCompliance, tone: 'bg-red-700' }
])
const currentTime = ref(new Date())
const clockTime = computed(() => currentTime.value.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit', second: '2-digit' }))
const clockDate = computed(() => currentTime.value.toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' }))
let clockTimer = null
const recentTitle = item => item.kind === 'Notification' ? item.title || item.message || 'Notification' : titleOf(item)
const recentTime = item => {
  const date = parsedDate(recentTimestamp(item))
  return date
    ? new Intl.DateTimeFormat('en-US', { month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' }).format(date)
    : item.status || 'Recently updated'
}
const recentDescription = item => item.kind === 'Notification'
  ? item.message || 'Operational notification'
  : item.description || item.status || `${item.kind} record updated`
const recentPerson = item => item.kind === 'Activity'
  ? props.activityPerson(item)
  : item.kind === 'Report'
    ? props.reportPerson(item)
    : item.kind === 'Task'
      ? props.activityPerson(item)
      : item.assignedToName || item.assignedToUsername || item.assigned_to_name || ''
const statusTone = status => {
  const value = normalize(status)
  if (['overdue', 'delayed', 'rejected', 'cancelled'].some(token => value.includes(token))) return 'bg-red-100 text-red-800'
  if (['completed', 'verified', 'approved', 'resolved'].some(token => value.includes(token))) return 'bg-emerald-100 text-emerald-800'
  if (['for verification', 'for review', 'returned', 'pending'].some(token => value.includes(token))) return 'bg-amber-100 text-amber-900'
  return 'bg-blue-100 text-blue-800'
}

onMounted(() => {
  clockTimer = window.setInterval(() => {
    currentTime.value = new Date()
  }, 1000)
})

onUnmounted(() => {
  if (clockTimer !== null) {
    window.clearInterval(clockTimer)
    clockTimer = null
  }
})
</script>

<template>
  <div class="min-w-0 space-y-4 text-slate-800">
    <header class="flex flex-col justify-between gap-4 border-b border-[#6a3630]/20 pb-4 sm:flex-row sm:items-center">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-wider text-[#8B1E23]">FireNotify <span class="px-1 text-[#D8B65A]">/</span> Administration</p>
        <h1 class="mt-1 text-2xl font-bold leading-tight text-[#331817]">Welcome back, {{ currentUser?.name || currentUser?.first_name || 'Admin' }}</h1>
        <p class="mt-1 text-sm text-slate-600">BFP Operations Overview</p>
      </div>
      <div class="flex flex-col items-end gap-2">
        <span class="inline-flex items-center gap-2 text-xs font-semibold text-emerald-800"><span class="h-2 w-2 rounded-full bg-emerald-600"></span>System Online</span>
        <div class="flex w-fit items-center gap-3 rounded-lg border border-[#E6DED2] bg-white px-3.5 py-2 shadow-sm">
          <span class="grid h-9 w-9 place-items-center rounded-md bg-[#F8F2E8] text-[#8B1E23]">
            <svg aria-hidden="true" viewBox="0 0 24 24" fill="none" class="h-5 w-5" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="8.5"/><path stroke-linecap="round" d="M12 7v5l3.5 2"/></svg>
          </span>
          <div class="tabular-nums">
            <p class="text-base font-bold tracking-wide text-[#331817]">{{ clockTime }}</p>
            <p class="text-xs font-medium text-slate-500">{{ clockDate }}</p>
          </div>
        </div>
      </div>
    </header>

    <section aria-label="Key performance indicators" class="grid grid-cols-1 gap-3 sm:grid-cols-2 xl:grid-cols-4">
      <article v-for="metric in [
        { label: 'Personnel', value: totalPersonnel, note: `${activePersonnel} active`, icon: 'personnel', accent: 'border-t-[#8B1E23]', iconTone: 'bg-red-50 text-[#8B1E23]' },
        { label: 'Activities', value: activities.length, note: `${ongoingCount} currently ongoing`, icon: 'activities', accent: 'border-t-[#C49A27]', iconTone: 'bg-amber-50 text-amber-800' },
        { label: 'Reports', value: reports.length, note: `${pendingReports} pending`, icon: 'reports', accent: 'border-t-[#9B6B18]', iconTone: 'bg-yellow-50 text-yellow-800' },
        { label: 'Tasks', value: tasks.length, note: `${taskStatusCounts.completed} completed`, icon: 'tasks', accent: 'border-t-blue-700', iconTone: 'bg-blue-50 text-blue-800' }
      ]" :key="metric.label" class="group flex min-h-[94px] items-center gap-3 rounded-lg border border-slate-200 border-t-[3px] bg-white px-4 py-3 shadow-sm transition duration-150 hover:-translate-y-0.5 hover:shadow-md" :class="metric.accent">
        <span class="grid h-10 w-10 shrink-0 place-items-center rounded-md" :class="metric.iconTone">
          <svg v-if="metric.icon === 'personnel'" aria-hidden="true" viewBox="0 0 24 24" fill="none" class="h-5 w-5" stroke="currentColor" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M16 20v-1.5a3.5 3.5 0 0 0-3.5-3.5h-5A3.5 3.5 0 0 0 4 18.5V20m6-8a4 4 0 1 0 0-8 4 4 0 0 0 0 8Zm7-7.7a4 4 0 0 1 0 7.4m3 8.3v-1.5a3.5 3.5 0 0 0-2.5-3.35" /></svg>
          <svg v-else-if="metric.icon === 'activities'" aria-hidden="true" viewBox="0 0 24 24" fill="none" class="h-5 w-5" stroke="currentColor" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M8 5h8m-8 4h8m-8 4h5m-8-9h14v15H5V4Z" /></svg>
          <svg v-else-if="metric.icon === 'reports'" aria-hidden="true" viewBox="0 0 24 24" fill="none" class="h-5 w-5" stroke="currentColor" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M7 3.75h7l4 4V20H7a2 2 0 0 1-2-2V5.75a2 2 0 0 1 2-2Zm7 0v4h4m-7 4h4m-4 3h4" /></svg>
          <svg v-else aria-hidden="true" viewBox="0 0 24 24" fill="none" class="h-5 w-5" stroke="currentColor" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="m8.5 12.5 2.25 2.25L16 9.5M5 4.75h14v15H5v-15Z" /></svg>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-semibold uppercase tracking-wide text-slate-500">{{ metric.label }}</p>
          <p class="mt-0.5 text-2xl font-bold leading-none tabular-nums text-slate-900">{{ metric.value }}</p>
          <p class="mt-1 truncate text-xs text-slate-500">{{ metric.note }}</p>
        </div>
      </article>
    </section>

    <section class="overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm">
      <header class="border-b border-slate-200 bg-[#FBF9F5] px-4 py-3.5 sm:px-5">
        <p class="text-xs font-semibold uppercase tracking-wider text-[#8B1E23]">System readiness</p>
        <h2 class="mt-0.5 text-base font-bold text-[#331817]">Readiness &amp; Compliance</h2>
      </header>
      <div class="grid gap-x-6 gap-y-4 p-4 sm:grid-cols-2 sm:p-5 xl:grid-cols-3">
        <div v-for="item in operationalStatus" :key="item.label" class="space-y-1.5">
          <div class="flex items-center justify-between gap-2"><span class="text-xs font-medium text-slate-700">{{ item.label }}</span><span class="text-xs font-bold tabular-nums text-slate-900">{{ item.value }}%</span></div>
          <div class="h-1.5 overflow-hidden rounded-full bg-slate-100"><div class="h-full rounded-full" :class="item.tone" :style="{ width: `${item.value}%` }"></div></div>
          <p class="text-xs text-slate-500">{{ item.detail }}</p>
        </div>
        <div class="flex items-center justify-between border-t border-slate-200 pt-3 sm:col-span-2 xl:col-span-1 xl:border-l xl:border-t-0 xl:pl-5 xl:pt-0">
          <span class="text-xs font-semibold text-slate-700">Overdue items</span>
          <span class="rounded-full px-2 py-1 text-xs font-bold tabular-nums" :class="overdueDeadlines + overdueReports.length ? 'bg-red-50 text-red-800' : 'bg-emerald-50 text-emerald-800'">{{ overdueDeadlines + overdueReports.length }}</span>
        </div>
      </div>
    </section>

    <section class="overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm">
      <header class="flex items-center justify-between gap-3 border-b border-slate-200 bg-[#FBF9F5] px-4 py-3.5 sm:px-5"><div><p class="text-xs font-semibold uppercase tracking-wider text-[#8B1E23]">Latest records</p><h2 class="mt-0.5 text-base font-bold text-[#331817]">Recent Activity</h2></div><span class="text-xs text-slate-500">{{ recentItems.length }} updates</span></header>
      <div v-if="recentItems.length" class="relative px-4 sm:px-5">
        <span aria-hidden="true" class="absolute bottom-5 left-[35px] top-5 w-px bg-[#E9E1D6]"></span>
        <ul class="divide-y divide-slate-100">
          <li v-for="item in recentItems" :key="`${item.kind}-${item.id}`" class="relative flex min-w-0 items-start gap-3 py-3">
            <span class="z-10 grid h-8 w-8 shrink-0 place-items-center rounded-full border border-[#E9E1D6] bg-white text-[10px] font-bold text-[#8B1E23] shadow-sm">{{ item.kind.slice(0, 1) }}</span>
            <div class="min-w-0 flex-1">
              <div class="flex min-w-0 flex-wrap items-center gap-x-2 gap-y-1"><span class="rounded bg-[#F8F5F0] px-1.5 py-0.5 text-[10px] font-semibold uppercase tracking-wide text-slate-600">{{ item.kind }}</span><span v-if="item.status" class="rounded-full px-2 py-0.5 text-[10px] font-semibold" :class="statusTone(item.status)">{{ item.status }}</span><span class="ml-auto text-xs tabular-nums text-slate-500">{{ recentTime(item) }}</span></div>
              <p class="mt-1 truncate text-sm font-semibold text-slate-900">{{ recentTitle(item) }}</p>
              <p class="mt-0.5 truncate text-xs text-slate-500">{{ recentDescription(item) }}<span v-if="recentPerson(item)"> · {{ recentPerson(item) }}</span></p>
            </div>
          </li>
        </ul>
      </div>
      <p v-else class="px-4 py-5 text-sm text-slate-500 sm:px-5">No recent activity</p>
    </section>
  </div>
</template>
