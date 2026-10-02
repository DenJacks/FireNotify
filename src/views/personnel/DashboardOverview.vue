<script setup>
import { computed, onMounted, onUnmounted, ref } from 'vue'

const props = defineProps({
  currentUser: { type: Object, default: null },
  dutyStatus: { type: String, default: 'Duty status unavailable' },
  currentDate: { type: String, default: '' },
  activities: { type: Array, default: () => [] },
  tasks: { type: Array, default: () => [] },
  reports: { type: Array, default: () => [] },
  notifications: { type: Array, default: () => [] },
  completedActivities: { type: Number, default: 0 },
  overdueActivities: { type: Number, default: 0 },
  activityCompliance: { type: Number, default: 0 },
  completedTasks: { type: Number, default: 0 },
  overdueTasks: { type: Number, default: 0 },
  completionPercentage: { type: Number, default: 0 },
  reviewedReports: { type: Number, default: 0 },
  reportCompliance: { type: Number, default: 0 },
  pendingTasks: { type: Number, default: 0 },
  pendingReports: { type: Number, default: 0 },
  unreadNotifications: { type: Number, default: 0 },
  selectedTask: { type: Object, default: null }
})

const emit = defineEmits(['view-task', 'close-task', 'acknowledge-task', 'mark-notification-read', 'mark-all-notifications-read'])
const normalize = value => String(value || '').trim().toLowerCase()
const completedStatuses = ['completed', 'complete', 'done', 'finished', 'approved', 'reviewed', 'verified', 'submitted', 'closed', 'resolved']
const isComplete = item => completedStatuses.includes(normalize(item?.status))
const dateValue = item => item?.deadline || item?.dueDate || item?.due_date || item?.activity_date || item?.date || item?.schedule || item?.scheduledDate || item?.time || ''
const parsedDate = value => {
  const date = value ? new Date(String(value).replace(/•/g, ' ').trim()) : null
  return date && !Number.isNaN(date.getTime()) ? date : null
}
const titleOf = item => item?.title || item?.name || item?.report_title || item?.type || item?.taskTitle || 'Assigned item'
const priorityItems = computed(() => {
  const now = new Date()
  const tomorrow = new Date(now)
  tomorrow.setHours(23, 59, 59, 999)
  tomorrow.setDate(tomorrow.getDate() + 1)
  const items = []
  const add = (item, kind) => {
    if (isComplete(item)) return
    const due = parsedDate(dateValue(item))
    const status = normalize(item?.status)
    const actionStatus = ['returned', 'delayed', 'for review', 'pending', 'draft', 'assigned', 'in progress', 'ongoing'].includes(status)
    const overdue = Boolean(due && due < now && !/^\d{4}-\d{2}-\d{2}$/.test(String(dateValue(item))))
      || Boolean(due && /^\d{4}-\d{2}-\d{2}$/.test(String(dateValue(item))) && due < new Date(new Date().setHours(0, 0, 0, 0)))
    if (!overdue && !(due && due <= tomorrow) && !actionStatus) return
    items.push({ item, kind, title: titleOf(item), due, overdue, status })
  }
  props.activities.forEach(item => add(item, 'Activity'))
  props.tasks.forEach(item => add(item, 'Task'))
  props.reports.forEach(item => add(item, 'Report'))
  return items.sort((left, right) => {
    if (left.overdue !== right.overdue) return left.overdue ? -1 : 1
    return (left.due?.getTime() || Number.MAX_SAFE_INTEGER) - (right.due?.getTime() || Number.MAX_SAFE_INTEGER)
  }).slice(0, 6)
})
const recentNotifications = computed(() => [...props.notifications].sort((left, right) => {
  const leftDate = parsedDate(left.created_at || left.createdAt || left.timestamp || left.date)?.getTime() || 0
  const rightDate = parsedDate(right.created_at || right.createdAt || right.timestamp || right.date)?.getTime() || 0
  return rightDate - leftDate
}).slice(0, 4))
const dueLabel = priority => {
  if (priority.overdue) return 'Overdue'
  if (!priority.due) return priority.status ? priority.status.replace(/\b\w/g, letter => letter.toUpperCase()) : 'Needs attention'
  const today = new Date()
  const dueDay = new Date(priority.due)
  const todayKey = new Date(today.getFullYear(), today.getMonth(), today.getDate()).getTime()
  const dueKey = new Date(dueDay.getFullYear(), dueDay.getMonth(), dueDay.getDate()).getTime()
  if (dueKey === todayKey) return 'Due today'
  const tomorrowKey = todayKey + 86400000
  if (dueKey === tomorrowKey) return 'Due tomorrow'
  return new Intl.DateTimeFormat('en-US', { month: 'short', day: 'numeric' }).format(priority.due)
}
const notificationTime = item => {
  const date = parsedDate(item.created_at || item.createdAt || item.timestamp || item.date)
  return date ? new Intl.DateTimeFormat('en-US', { month: 'short', day: 'numeric' }).format(date) : ''
}
const notificationType = item => item.notification_type || item.type || 'Update'
const userName = computed(() => props.currentUser?.name || `${props.currentUser?.firstName || props.currentUser?.first_name || ''} ${props.currentUser?.lastName || props.currentUser?.last_name || ''}`.trim() || props.currentUser?.username || 'Personnel')
const userRank = computed(() => props.currentUser?.rank || props.currentUser?.employeeRank || 'Rank not set')
const userDutyStatus = computed(() => props.currentUser?.dutyStatus || props.currentUser?.duty_status || props.dutyStatus)
const countStatus = (records, statuses) => records.filter(item => statuses.includes(normalize(item?.status))).length
const returnedReports = computed(() => countStatus(props.reports, ['returned']))
const submittedReports = computed(() => countStatus(props.reports, ['submitted', 'for review']))
const verifiedActivities = computed(() => props.completedActivities)
const activityRows = computed(() => [
  { label: 'Scheduled', value: countStatus(props.activities, ['scheduled']), tone: 'bg-slate-400' },
  { label: 'Ongoing', value: countStatus(props.activities, ['ongoing']), tone: 'bg-blue-700' },
  { label: 'Completed', value: verifiedActivities.value, tone: 'bg-emerald-700' },
  { label: 'For verification', value: countStatus(props.activities, ['for verification', 'for_verification']), tone: 'bg-amber-500' },
  { label: 'Overdue', value: props.overdueActivities, tone: 'bg-red-700' }
])
const reportRows = computed(() => [
  { label: 'Pending', value: countStatus(props.reports, ['pending', 'pending submission']), tone: 'bg-amber-500' },
  { label: 'Submitted', value: submittedReports.value, tone: 'bg-blue-700' },
  { label: 'Verified', value: props.reviewedReports, tone: 'bg-emerald-700' },
  { label: 'Returned', value: returnedReports.value, tone: 'bg-orange-600' }
])
const taskRows = computed(() => [
  { label: 'Assigned', value: countStatus(props.tasks, ['assigned', 'pending']), tone: 'bg-slate-500' },
  { label: 'In progress', value: countStatus(props.tasks, ['in progress', 'ongoing']), tone: 'bg-blue-700' },
  { label: 'For verification', value: countStatus(props.tasks, ['for verification']), tone: 'bg-amber-500' },
  { label: 'Completed', value: props.completedTasks, tone: 'bg-emerald-700' },
  { label: 'Overdue', value: props.overdueTasks, tone: 'bg-red-700' }
])
const currentTime = ref(new Date())
const clockTime = computed(() => new Intl.DateTimeFormat('en-US', {
  hour: 'numeric', minute: '2-digit', second: '2-digit'
}).format(currentTime.value))
const clockDate = computed(() => new Intl.DateTimeFormat('en-US', {
  weekday: 'long', month: 'long', day: 'numeric', year: 'numeric'
}).format(currentTime.value))
let clockTimer = null

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
    <header class="flex flex-col justify-between gap-4 border-b border-[#8B1E23]/20 pb-4 sm:flex-row sm:items-center">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-wider text-[#8B1E23]">FireNotify <span class="px-1 text-[#D5A91F]">/</span> Personnel Operations</p>
        <h1 class="mt-1 text-2xl font-bold leading-tight text-slate-900">Welcome back, {{ userName }}</h1>
        <p class="mt-1 flex items-center gap-2 text-sm text-slate-600"><span class="font-semibold text-slate-700">{{ userRank }}</span><span class="text-[#D5A91F]">•</span><span>{{ userDutyStatus }}</span></p>
      </div>
      <div class="flex w-fit items-center gap-3 rounded-lg border border-[#E6DED2] bg-white px-3.5 py-2 shadow-sm">
        <span class="grid h-9 w-9 place-items-center rounded-md bg-[#F8F2E8] text-[#8B1E23]"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" class="h-5 w-5" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="8.5"/><path stroke-linecap="round" d="M12 7v5l3.5 2"/></svg></span>
        <div class="tabular-nums"><p class="text-base font-bold tracking-wide text-[#331817]">{{ clockTime }}</p><p class="text-xs font-medium text-slate-500">{{ clockDate }}</p></div>
      </div>
    </header>

    <section aria-label="Personnel summary" class="grid grid-cols-1 gap-3 sm:grid-cols-2 xl:grid-cols-4">
      <article v-for="metric in [
        { label: 'Activities', value: activities.length, detail: 'Assigned to you', icon: 'activities', tone: 'border-t-[#8B1E23]', iconTone: 'bg-red-50 text-[#8B1E23]' },
        { label: 'Reports', value: pendingReports, detail: 'Need submission or review', icon: 'reports', tone: 'border-t-[#C49A27]', iconTone: 'bg-amber-50 text-amber-800' },
        { label: 'Tasks', value: pendingTasks, detail: 'Current assignments', icon: 'tasks', tone: 'border-t-[#9B6B18]', iconTone: 'bg-yellow-50 text-yellow-800' },
        { label: 'Alerts', value: unreadNotifications, detail: 'Unread notifications', icon: 'alerts', tone: unreadNotifications ? 'border-t-red-700' : 'border-t-emerald-600', iconTone: unreadNotifications ? 'bg-red-50 text-red-700' : 'bg-emerald-50 text-emerald-700' }
      ]" :key="metric.label" class="group flex min-h-[94px] items-center gap-3 rounded-lg border border-slate-200 border-t-[3px] bg-white px-4 py-3 shadow-sm transition duration-150 hover:-translate-y-0.5 hover:border-slate-300 hover:shadow-md" :class="metric.tone">
        <span class="grid h-10 w-10 shrink-0 place-items-center rounded-md" :class="metric.iconTone">
          <svg v-if="metric.icon === 'activities'" aria-hidden="true" viewBox="0 0 24 24" fill="none" class="h-5 w-5" stroke="currentColor" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M8 5h8m-8 4h8m-8 4h5m-8-9h14v15H5V4Z" /></svg>
          <svg v-else-if="metric.icon === 'reports'" aria-hidden="true" viewBox="0 0 24 24" fill="none" class="h-5 w-5" stroke="currentColor" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M7 3.75h7l4 4V20H7a2 2 0 0 1-2-2V5.75a2 2 0 0 1 2-2Zm7 0v4h4m-7 4h4m-4 3h4" /></svg>
          <svg v-else-if="metric.icon === 'tasks'" aria-hidden="true" viewBox="0 0 24 24" fill="none" class="h-5 w-5" stroke="currentColor" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="m8.5 12.5 2.25 2.25L16 9.5M5 4.75h14v15H5v-15Z" /></svg>
          <svg v-else aria-hidden="true" viewBox="0 0 24 24" fill="none" class="h-5 w-5" stroke="currentColor" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3.5a6 6 0 0 0-6 6v3l-1.5 2.5h15L18 12.5v-3a6 6 0 0 0-6-6Zm-2.5 14a2.5 2.5 0 0 0 5 0" /></svg>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-semibold uppercase tracking-wide text-slate-500">{{ metric.label }}</p>
          <p class="mt-0.5 text-2xl font-bold leading-none tabular-nums text-slate-900">{{ metric.value }}</p>
          <p class="mt-1 truncate text-xs text-slate-500">{{ metric.detail }}</p>
        </div>
      </article>
    </section>

    <section class="overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm">
      <header class="flex flex-col justify-between gap-3 border-b border-slate-200 bg-[#FBF9F5] px-4 py-3.5 sm:flex-row sm:items-center sm:px-5">
        <div><p class="text-xs font-semibold uppercase tracking-wider text-[#8B1E23]">Personal readiness</p><h2 class="mt-0.5 text-base font-bold text-[#331817]">My Readiness &amp; Compliance</h2></div>
        <div class="flex items-center gap-2 text-sm"><span class="text-slate-600">My Status</span><span class="rounded-full px-2.5 py-1 text-xs font-semibold" :class="userDutyStatus === 'On Duty' ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-900'">{{ userDutyStatus }}</span><span class="text-xs text-slate-500">{{ userRank }}</span></div>
      </header>
      <div class="grid gap-x-6 gap-y-4 p-4 sm:grid-cols-2 sm:p-5 xl:grid-cols-3">
        <div v-for="metric in [
          { label: 'Activity compliance', value: activityCompliance, tone: 'bg-[#8B1E23]' },
          { label: 'Report compliance', value: reportCompliance, tone: 'bg-amber-600' },
          { label: 'Task completion', value: completionPercentage, tone: 'bg-blue-700' }
        ]" :key="metric.label" class="space-y-1.5"><div class="flex items-center justify-between gap-2"><span class="text-xs font-medium text-slate-700">{{ metric.label }}</span><span class="text-xs font-bold tabular-nums text-slate-900">{{ metric.value }}%</span></div><div class="h-1.5 overflow-hidden rounded-full bg-slate-100"><div class="h-full rounded-full" :class="metric.tone" :style="{ width: `${metric.value}%` }"></div></div></div>
        <div class="flex items-center justify-between gap-2 border-t border-slate-200 pt-3 sm:col-span-2 xl:col-span-1 xl:border-l xl:border-t-0 xl:pl-5 xl:pt-0"><span class="text-xs font-semibold text-slate-700">Overdue items</span><span class="rounded-full px-2 py-1 text-xs font-bold tabular-nums" :class="overdueActivities + overdueTasks ? 'bg-red-50 text-red-800' : 'bg-emerald-50 text-emerald-800'">{{ overdueActivities + overdueTasks }}</span><span class="text-xs text-slate-500">{{ userRank }} · {{ currentUser?.status || 'Active' }}</span></div>
      </div>
    </section>

    <div class="grid min-w-0 items-stretch gap-4 lg:grid-cols-[1.15fr_0.85fr]">
    <section class="overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm">
      <div class="mb-3 flex items-end justify-between gap-3 border-b border-slate-100 pb-3">
        <div class="px-4 pt-4 sm:px-5">
          <p class="text-[11px] font-semibold uppercase tracking-[0.07em] text-[#8B1E23]">Next actions</p>
          <h2 class="mt-0.5 text-base font-bold text-slate-900">Today's Priorities</h2>
        </div>
        <span v-if="priorityItems.length" class="mr-4 rounded-md bg-[#FAF7F1] px-2.5 py-1 text-xs font-bold tabular-nums text-[#8B1E23] sm:mr-5">{{ priorityItems.length }} active</span>
      </div>
      <ul v-if="priorityItems.length" class="divide-y divide-slate-100 px-4 sm:px-5">
        <li v-for="priority in priorityItems" :key="`${priority.kind}-${priority.item.id || priority.title}`" class="flex min-w-0 items-center gap-3 py-3">
          <button v-if="priority.kind === 'Task'" type="button" class="grid h-9 w-9 shrink-0 place-items-center rounded-lg bg-[#F9F2DA] text-[#8B1E23] transition hover:bg-[#F2E6B8]" :aria-label="`View task ${priority.title}`" @click="emit('view-task', priority.item)">
            <svg aria-hidden="true" viewBox="0 0 20 20" fill="none" class="h-4 w-4" stroke="currentColor" stroke-width="1.7"><path stroke-linecap="round" stroke-linejoin="round" d="m6.5 10.5 2.25 2.25L13.5 8m-9-4h11v12h-11V4Z" /></svg>
          </button>
          <span v-else class="grid h-9 w-9 shrink-0 place-items-center rounded-lg bg-[#F9F2DA] text-[#8B1E23]">
            <svg v-if="priority.kind === 'Activity'" aria-hidden="true" viewBox="0 0 20 20" fill="none" class="h-4 w-4" stroke="currentColor" stroke-width="1.7"><path stroke-linecap="round" stroke-linejoin="round" d="M6 4h8m-8 4h8m-8 4h5M4 2.75h12v14.5H4V2.75Z" /></svg>
            <svg v-else aria-hidden="true" viewBox="0 0 20 20" fill="none" class="h-4 w-4" stroke="currentColor" stroke-width="1.7"><path stroke-linecap="round" stroke-linejoin="round" d="M6 2.75h6l3 3v11.5H6a1.5 1.5 0 0 1-1.5-1.5v-11A1.5 1.5 0 0 1 6 2.75Zm6 0v3h3m-6 3h3m-3 3h4" /></svg>
          </span>
          <div class="min-w-0 flex-1">
            <p class="truncate text-sm font-semibold text-slate-900">{{ priority.title }}</p>
            <p class="mt-0.5 text-xs text-slate-500">{{ priority.kind }}<span v-if="priority.item.location || priority.item.station"> <span class="px-1 text-slate-300">·</span> {{ priority.item.location || priority.item.station }}</span></p>
          </div>
          <span class="shrink-0 rounded-full px-2 py-1 text-[10px] font-bold" :class="priority.overdue ? 'bg-red-50 text-red-700' : 'bg-amber-50 text-amber-800'">{{ priority.overdue ? 'OVERDUE' : dueLabel(priority) }}</span>
        </li>
      </ul>
      <p v-else class="mx-4 flex items-center gap-2 py-7 text-sm text-slate-500 sm:mx-5"><span class="grid h-7 w-7 place-items-center rounded-full bg-emerald-50 text-emerald-700">✓</span>No priorities for today</p>
    </section>

    <section class="overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm">
      <div class="mb-1 flex items-center justify-between gap-3 border-b border-slate-100 px-4 py-4 sm:px-5">
        <div class="min-w-0">
          <p class="text-[11px] font-semibold uppercase tracking-[0.07em] text-[#8B1E23]">Inbox</p>
          <h2 class="mt-0.5 text-base font-bold text-slate-900">Recent Notifications</h2>
        </div>
        <button v-if="unreadNotifications" type="button" class="shrink-0 rounded-md border border-slate-200 px-2.5 py-1.5 text-xs font-semibold text-[#8B1E23] transition hover:border-[#8B1E23]/40 hover:bg-red-50" @click="emit('mark-all-notifications-read')">Mark all read</button>
      </div>
      <ul v-if="recentNotifications.length" class="divide-y divide-slate-100 px-4 sm:px-5">
        <li v-for="notification in recentNotifications" :key="notification.id" class="flex min-w-0 items-start gap-3 py-3">
          <span class="mt-1 grid h-8 w-8 shrink-0 place-items-center rounded-lg" :class="notification.read || notification.is_read ? 'bg-slate-100 text-slate-500' : 'bg-red-50 text-[#8B1E23]'">
            <svg aria-hidden="true" viewBox="0 0 20 20" fill="none" class="h-4 w-4" stroke="currentColor" stroke-width="1.6"><path stroke-linecap="round" stroke-linejoin="round" d="M3.5 5.5h13v9h-13v-9Zm0 .5 6.5 5 6.5-5" /></svg>
          </span>
          <button type="button" class="min-w-0 flex-1 text-left" @click="emit('mark-notification-read', notification.id)">
            <span class="flex min-w-0 items-center gap-2">
              <span class="truncate text-[10px] font-bold uppercase tracking-[0.06em] text-[#8B1E23]">{{ notificationType(notification) }}</span>
              <span v-if="!(notification.read || notification.is_read)" class="h-1.5 w-1.5 shrink-0 rounded-full bg-[#8B1E23]"></span>
            </span>
            <span class="mt-0.5 block truncate text-sm font-semibold text-slate-900">{{ notification.title || 'FireNotify update' }}</span>
            <span class="mt-0.5 block line-clamp-2 text-xs text-slate-600">{{ notification.message || notification.detail || 'You have a new update.' }}</span>
          </button>
          <span v-if="notificationTime(notification)" class="shrink-0 pt-1 text-xs tabular-nums text-slate-500">{{ notificationTime(notification) }}</span>
        </li>
      </ul>
      <p v-else class="mx-4 py-7 text-sm text-slate-500 sm:mx-5">No recent notifications</p>
    </section>
    </div>

    <div v-if="selectedTask" class="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/50 p-4" @click.self="emit('close-task')">
      <section role="dialog" aria-modal="true" aria-labelledby="task-dialog-title" class="w-full max-w-lg overflow-hidden rounded-lg bg-white shadow-xl">
        <div class="h-1.5 bg-[#8B1E23]"></div>
        <div class="p-5 sm:p-6">
          <div class="flex items-start justify-between gap-4">
            <div>
              <p class="text-xs font-bold uppercase tracking-wide text-[#8B1E23]">Assigned task</p>
              <h2 id="task-dialog-title" class="mt-1 text-xl font-bold text-slate-900">{{ selectedTask.type }}</h2>
            </div>
            <button type="button" aria-label="Close task details" class="rounded p-2 text-slate-500 hover:bg-slate-100" @click="emit('close-task')">×</button>
          </div>
          <dl class="mt-5 space-y-4 text-sm">
            <div><dt class="text-xs text-slate-500">Location</dt><dd class="mt-1 font-semibold text-slate-900">{{ selectedTask.location }}</dd></div>
            <div><dt class="text-xs text-slate-500">Schedule</dt><dd class="mt-1 font-semibold text-slate-900">{{ selectedTask.time }}</dd></div>
            <div><dt class="text-xs text-slate-500">Description</dt><dd class="mt-1 text-slate-700">{{ selectedTask.description }}</dd></div>
          </dl>
          <div class="mt-6 flex justify-end gap-2">
            <button type="button" class="rounded border border-slate-300 px-4 py-2 text-sm font-semibold text-slate-700 hover:bg-slate-50" @click="emit('close-task')">Close</button>
            <button type="button" class="rounded bg-[#8B1E23] px-4 py-2 text-sm font-semibold text-white hover:bg-[#72181D]" @click="emit('acknowledge-task')">Acknowledge Task</button>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>
