<template>
  <div class="w-full min-w-0 space-y-7">

    <!-- =========================================================
         WELCOME HEADER
    ========================================================== -->
    <section class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">

        <div>
          <p class="text-sm font-medium text-[#8B1E23] mb-1">
            FIRENOTIFY PERSONNEL PORTAL
          </p>

          <h2 class="text-2xl lg:text-3xl font-bold text-slate-900">
            Welcome back, {{ currentUser?.firstName }} {{ currentUser?.lastName }}!
          </h2>

          <p class="mt-2 text-base text-slate-500">
            Monitor your assigned tasks, reports, and station activities.
          </p>

          <p class="text-xs text-slate-400 mt-2">
            {{ currentDate }}
          </p>
        </div>

        <!-- DUTY STATUS -->
        <div class="flex items-center gap-3 px-5 py-4 rounded-xl bg-[#8B1E23] text-white">
          <div class="h-11 w-11 rounded-full bg-white/10 flex items-center justify-center">
            <span
              v-html="ICONS.siren"
              class="h-6 w-6 text-[#F4C542]"
            ></span>
          </div>

          <div>
            <p class="text-xs text-white/70">
              Current Status
            </p>

            <p class="text-base font-bold">
              {{ dutyStatus }}
            </p>
          </div>
        </div>

      </div>
    </section>


    <!-- =========================================================
         STATISTICS
    ========================================================== -->
    <section class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-5">

      <!-- TODAY'S TASKS -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">

          <div>
            <p class="text-sm font-medium text-slate-500">
              Today's Tasks
            </p>

            <p class="text-3xl font-bold text-slate-900 mt-2">
              {{ taskStats.total.toString().padStart(2, '0') }}
            </p>

            <p class="text-xs text-blue-600 font-semibold mt-2">
              {{ taskStats.pending }} pending
            </p>
          </div>

          <div class="h-12 w-12 rounded-xl bg-blue-50 flex items-center justify-center">
            <span
              v-html="ICONS.tasks"
              class="h-6 w-6 text-blue-600"
            ></span>
          </div>

        </div>
      </div>


      <!-- COMPLETED -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">

          <div>
            <p class="text-sm font-medium text-slate-500">
              Completed
            </p>

            <p class="text-3xl font-bold text-slate-900 mt-2">
              {{ taskStats.completed.toString().padStart(2, '0') }}
            </p>

            <p class="text-xs text-green-600 font-semibold mt-2">
              This week
            </p>
          </div>

          <div class="h-12 w-12 rounded-xl bg-green-50 flex items-center justify-center">
            <span class="text-xl text-green-600">
              ✓
            </span>
          </div>

        </div>
      </div>


      <!-- REPORTS -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">

          <div>
            <p class="text-sm font-medium text-slate-500">
              Reports To Submit
            </p>

            <p class="text-3xl font-bold text-slate-900 mt-2">
              {{ reportCount.toString().padStart(2, '0') }}
            </p>

            <p class="text-xs text-yellow-600 font-semibold mt-2">
              Needs attention
            </p>
          </div>

          <div class="h-12 w-12 rounded-xl bg-yellow-50 flex items-center justify-center">
            <span
              v-html="ICONS.reports"
              class="h-6 w-6 text-yellow-600"
            ></span>
          </div>

        </div>
      </div>


      <!-- URGENT -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">

          <div>
            <p class="text-sm font-medium text-slate-500">
              Urgent
            </p>

            <p class="text-3xl font-bold text-slate-900 mt-2">
              {{ urgentCount.toString().padStart(2, '0') }}
            </p>

            <p class="text-xs text-red-600 font-semibold mt-2">
              Immediate action
            </p>
          </div>

          <div class="h-12 w-12 rounded-xl bg-red-50 flex items-center justify-center">
            <span class="text-xl text-red-600 font-bold">
              !
            </span>
          </div>

        </div>
      </div>

    </section>


    <!-- =========================================================
         MAIN CONTENT
    ========================================================== -->
    <section class="grid grid-cols-1 xl:grid-cols-3 gap-6">

      <!-- LEFT COLUMN -->
      <div class="xl:col-span-2 space-y-6">

        <!-- =====================================================
             TODAY'S ASSIGNMENT
        ====================================================== -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <div class="flex items-center justify-between border-b border-slate-200 pb-5">

            <div>
              <h2 class="text-xl font-bold text-slate-900">
                Today's Assignment
              </h2>

              <p class="text-sm text-slate-500 mt-1">
                Your scheduled duty for today
              </p>
            </div>

            <span class="px-3 py-1 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">
              {{ todayAssignment.time }}
            </span>

          </div>


          <div class="mt-5 p-5 rounded-xl bg-blue-50 border border-blue-100">

            <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">

              <div>
                <p class="text-sm font-semibold text-blue-700">
                  {{ todayAssignment.type }}
                </p>

                <h3 class="text-lg font-bold text-slate-900 mt-1">
                  {{ todayAssignment.location }}
                </h3>

                <p class="text-sm text-slate-500 mt-2">
                  {{ todayAssignment.description }}
                </p>
              </div>

              <button
                @click="viewTask(todayAssignment)"
                class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D] transition"
              >
                View Task
              </button>

            </div>

          </div>
        </div>


        <!-- =====================================================
             UPCOMING ACTIVITIES
        ====================================================== -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <div class="border-b border-slate-200 pb-5">
            <h2 class="text-xl font-bold text-slate-900">
              Upcoming Activities
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              Your next scheduled station activities
            </p>
          </div>

          <div class="mt-5 space-y-4">

            <div
              v-for="activity in upcomingActivities"
              :key="activity.id"
              class="flex items-center gap-4 p-4 rounded-xl border border-slate-200 hover:bg-slate-50 transition"
            >

              <div
                class="h-12 w-12 rounded-xl flex items-center justify-center shrink-0"
                :class="activity.iconBg"
              >
                <span
                  v-html="ICONS[activity.icon]"
                  class="h-6 w-6"
                  :class="activity.iconColor"
                ></span>
              </div>

              <div class="flex-1 min-w-0">

                <p class="font-bold text-slate-900">
                  {{ activity.title }}
                </p>

                <p class="text-sm text-slate-500 mt-1">
                  {{ activity.schedule }}
                </p>

              </div>

              <span
                class="px-3 py-1 rounded-full text-xs font-bold shrink-0"
                :class="activity.statusClass"
              >
                {{ activity.status }}
              </span>

            </div>

          </div>
        </div>


        <!-- =====================================================
             RECENT ACTIVITY
        ====================================================== -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <div class="border-b border-slate-200 pb-5">

            <h2 class="text-xl font-bold text-slate-900">
              Recent Task Activity
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              Recent updates on your assigned duties
            </p>

          </div>

          <div class="mt-5 space-y-4">

            <div
              v-for="activity in recentActivities"
              :key="activity.id"
              class="flex items-start gap-4"
            >

              <div
                class="h-10 w-10 rounded-full flex items-center justify-center shrink-0"
                :class="activity.iconBg"
              >
                <span
                  class="font-bold"
                  :class="activity.iconColor"
                >
                  {{ activity.icon }}
                </span>
              </div>

              <div>
                <p class="text-sm font-semibold text-slate-900">
                  {{ activity.title }}
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  {{ activity.time }}
                </p>
              </div>

            </div>

          </div>
        </div>

      </div>


      <!-- =========================================================
           RIGHT COLUMN
      ========================================================== -->
      <div class="space-y-6">

        <!-- DUTY STATUS -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <h2 class="text-lg font-bold text-slate-900">
            Duty Status
          </h2>

          <div class="mt-5 p-5 rounded-xl bg-green-50 border border-green-100">

            <div class="flex items-center gap-3">

              <div class="h-3 w-3 rounded-full bg-green-500"></div>

              <p class="font-bold text-green-700">
                Currently {{ dutyStatus }}
              </p>

            </div>

            <p class="text-sm text-slate-500 mt-3">
              Station 1 · BFP Balingasag
            </p>

            <p class="text-sm text-slate-500 mt-1">
              Shift: 08:00 AM – 05:00 PM
            </p>

          </div>

        </div>


        <!-- WEEKLY PROGRESS -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <h2 class="text-lg font-bold text-slate-900">
            Weekly Progress
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Task completion this week
          </p>

          <div class="mt-5">

            <div class="flex items-center justify-between text-sm mb-2">

              <span class="font-medium text-slate-600">
                Completed Tasks
              </span>

              <span class="font-bold text-slate-900">
                {{ completionPercentage }}%
              </span>

            </div>

            <div class="h-3 bg-slate-100 rounded-full overflow-hidden">

              <div
                class="h-full bg-[#8B1E23] rounded-full transition-all duration-500"
                :style="{ width: `${completionPercentage}%` }"
              ></div>

            </div>

            <p class="text-xs text-slate-500 mt-3">
              {{ taskStats.completed }} of {{ taskStats.weeklyTotal }}
              assigned tasks completed
            </p>

          </div>

        </div>


        <!-- STATION INFORMATION -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <h2 class="text-lg font-bold text-slate-900">
            Station Information
          </h2>

          <div class="mt-5 space-y-4">

            <div>
              <p class="text-xs text-slate-500">
                Station
              </p>

              <p class="font-semibold text-slate-900 mt-1">
                BFP Balingasag
              </p>
            </div>

            <div>
              <p class="text-xs text-slate-500">
                Personnel Position
              </p>

              <p class="font-semibold text-slate-900 mt-1">
                {{ currentUser?.role || 'Fire Officer' }}
              </p>
            </div>

            <div>
              <p class="text-xs text-slate-500">
                Station Contact
              </p>

              <p class="font-semibold text-slate-900 mt-1">
                BFP Station Office
              </p>
            </div>

          </div>

        </div>


        <!-- =====================================================
             NOTIFICATIONS
        ====================================================== -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <div class="flex items-center justify-between">

            <h2 class="text-lg font-bold text-slate-900">
              Notifications
            </h2>

            <span
              v-if="unreadNotifications > 0"
              class="px-2 py-1 rounded-full bg-red-50 text-red-700 text-xs font-bold"
            >
              {{ unreadNotifications }} New
            </span>

          </div>

          <div class="mt-5 space-y-4">

            <div
              v-for="notification in notifications"
              :key="notification.id"
              @click="markNotificationRead(notification.id)"
              class="p-3 rounded-xl cursor-pointer transition hover:shadow-sm"
              :class="[
                notification.read
                  ? 'bg-slate-50 opacity-70'
                  : notification.bg
              ]"
            >

              <div class="flex items-start justify-between gap-3">

                <div>

                  <p class="text-sm font-semibold text-slate-900">
                    {{ notification.title }}
                  </p>

                  <p class="text-xs text-slate-500 mt-1">
                    {{ notification.message }}
                  </p>

                </div>

                <span
                  v-if="!notification.read"
                  class="h-2 w-2 rounded-full bg-[#8B1E23] shrink-0 mt-1"
                ></span>

              </div>

            </div>

          </div>

          <button
            @click="markAllNotificationsRead"
            class="w-full mt-4 py-2.5 rounded-xl border border-slate-200 text-sm font-semibold text-slate-600 hover:bg-slate-50 transition"
          >
            Mark all as read
          </button>

        </div>

      </div>

    </section>


    <!-- =========================================================
         TASK DETAILS MODAL
    ========================================================== -->
    <div
      v-if="selectedTask"
      class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/40 px-4"
      @click.self="closeTask"
    >

      <div class="w-full max-w-lg bg-white rounded-2xl shadow-2xl overflow-hidden">

        <div class="h-2 bg-[#8B1E23]"></div>

        <div class="p-6">

          <div class="flex items-start justify-between gap-4">

            <div>
              <p class="text-xs font-bold text-[#8B1E23]">
                ASSIGNED TASK
              </p>

              <h2 class="text-xl font-bold text-slate-900 mt-1">
                {{ selectedTask.type }}
              </h2>
            </div>

            <button
              @click="closeTask"
              class="h-9 w-9 rounded-lg hover:bg-slate-100 text-slate-500"
            >
              ✕
            </button>

          </div>

          <div class="mt-6 space-y-4">

            <div>
              <p class="text-xs text-slate-500">
                Location
              </p>

              <p class="font-semibold text-slate-900 mt-1">
                {{ selectedTask.location }}
              </p>
            </div>

            <div>
              <p class="text-xs text-slate-500">
                Schedule
              </p>

              <p class="font-semibold text-slate-900 mt-1">
                {{ selectedTask.time }}
              </p>
            </div>

            <div>
              <p class="text-xs text-slate-500">
                Description
              </p>

              <p class="text-sm text-slate-600 mt-1 leading-relaxed">
                {{ selectedTask.description }}
              </p>
            </div>

          </div>

          <div class="flex justify-end gap-3 mt-7">

            <button
              @click="closeTask"
              class="px-5 py-2.5 rounded-xl border border-slate-300 text-slate-700 font-semibold hover:bg-slate-50"
            >
              Close
            </button>

            <button
              @click="acknowledgeTask"
              class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white font-semibold hover:bg-[#72181D]"
            >
              Acknowledge Task
            </button>

          </div>

        </div>
      </div>
    </div>

  </div>
</template>


<script setup>
import { computed, ref, onMounted, onBeforeUnmount } from 'vue'

const props = defineProps({
  currentUser: {
    type: Object,
    required: false,
    default: null
  },

  ICONS: {
    type: Object,
    required: true
  }
})

const USERS_KEY = 'fireNotifyRegisteredUsers'
const CURRENT_USER_KEY = 'fireNotifyCurrentUser'
const ACTIVITIES_KEY = 'fireNotifyActivities'
const TASKS_KEY = 'firenotify_tasks'
const REPORTS_KEY = 'firenotify_reports'
const NOTIFICATION_KEYS = [
  'firenotify_notifications',
  'fireNotifyNotifications',
  'fireNotifyNotificationsData',
  'notifications'
]
const UPDATE_EVENTS = [
  'fireNotifyUsersUpdated',
  'fireNotifyRegisteredUsersUpdated',
  'fireNotifyActivitiesUpdated',
  'fireNotifyTasksUpdated',
  'fireNotifyReportsUpdated',
  'fireNotifyNotificationsUpdated'
]

const users = ref([])
const activities = ref([])
const tasks = ref([])
const reports = ref([])
const notifications = ref([])
const selectedTask = ref(null)
let refreshTimer = null

const readArray = (key) => {
  try {
    const value = JSON.parse(localStorage.getItem(key) || '[]')
    return Array.isArray(value) ? value : []
  } catch {
    return []
  }
}

const normalizeText = (value) => String(value ?? '').trim()
const toLower = (value) => normalizeText(value).toLowerCase()

const getCurrentUser = () => {
  if (props.currentUser) {
    return props.currentUser
  }

  try {
    return JSON.parse(localStorage.getItem(CURRENT_USER_KEY) || 'null') || null
  } catch {
    return null
  }
}

const getUserIdentityValues = (user) => {
  if (!user) return []

  const values = [
    user.id,
    user.userId,
    user.identifier,
    user.email,
    user.username,
    user.name,
    `${user.firstName || ''} ${user.lastName || ''}`.trim()
  ]

  return values.map(value => toLower(value)).filter(Boolean)
}

const matchesAnyValue = (value, candidates) => {
  if (!value || !candidates.length) return false

  const target = toLower(value)
  return candidates.includes(target)
}

const recordMatchesCurrentUser = (record) => {
  const user = getCurrentUser()
  if (!user) return false

  const candidates = getUserIdentityValues(user)
  if (!candidates.length) return false

  const values = [
    record?.assignedToId,
    record?.assignedTo,
    record?.assignedToUsername,
    record?.assignedToEmail,
    record?.assignedToName,
    record?.personnelId,
    record?.userId,
    record?.username,
    record?.email,
    record?.identifier,
    record?.ownerId,
    record?.assigneeId,
    record?.submittedBy,
    record?.name
  ]

  if (Array.isArray(record?.assignedPersonnel)) {
    record.assignedPersonnel.forEach(person => {
      values.push(person?.id)
      values.push(person?.userId)
      values.push(person?.username)
      values.push(person?.identifier)
      values.push(person?.email)
      values.push(person?.name)
      values.push(person?.firstName && person?.lastName ? `${person.firstName} ${person.lastName}` : '')
    })
  }

  if (Array.isArray(record?.assignedUsers)) {
    record.assignedUsers.forEach(person => {
      values.push(person?.id)
      values.push(person?.userId)
      values.push(person?.username)
      values.push(person?.identifier)
      values.push(person?.email)
      values.push(person?.name)
    })
  }

  return values.some(value => matchesAnyValue(value, candidates))
}

const notificationMatchesCurrentUser = (notification) => {
  const user = getCurrentUser()
  if (!user) return true

  const candidates = getUserIdentityValues(user)
  if (!candidates.length) return true

  const values = [
    notification?.assignedToId,
    notification?.assignedTo,
    notification?.assignedToUsername,
    notification?.assignedToEmail,
    notification?.userId,
    notification?.username,
    notification?.identifier,
    notification?.email,
    notification?.personnelId,
    notification?.recipientId,
    notification?.recipientUsername,
    notification?.recipientEmail
  ]

  return values.some(value => matchesAnyValue(value, candidates)) || !values.some(Boolean)
}

const parseDateValue = (value) => {
  if (!value) return null

  if (value instanceof Date) {
    return Number.isNaN(value.getTime()) ? null : value
  }

  const parsed = new Date(String(value).replace(/•/g, ' ').trim())
  return Number.isNaN(parsed.getTime()) ? null : parsed
}

const statusKey = (status) => toLower(status)

const isCompletedStatus = (status) => {
  const value = statusKey(status)
  return [
    'completed',
    'complete',
    'done',
    'finished',
    'approved',
    'reviewed',
    'submitted',
    'closed',
    'resolved'
  ].includes(value)
}

const isPendingStatus = (status) => {
  const value = statusKey(status)
  return [
    'pending',
    'scheduled',
    'in progress',
    'not started',
    'waiting',
    'assigned',
    'for review',
    'submitted'
  ].includes(value)
}

const isOverdueStatus = (record) => {
  const status = statusKey(record?.status)
  if (status === 'overdue') return true

  const dueDate = parseDateValue(record?.deadline || record?.dueDate || record?.date || record?.scheduleDate || record?.scheduledDate)
  if (!dueDate) return false

  return dueDate < new Date() && !isCompletedStatus(record?.status)
}

const badgeClassForStatus = (status) => {
  const value = statusKey(status)

  if (['completed', 'complete', 'approved', 'reviewed', 'submitted'].includes(value)) {
    return 'bg-green-50 text-green-700'
  }

  if (['overdue'].includes(value)) {
    return 'bg-red-50 text-red-700'
  }

  if (['in progress', 'pending', 'scheduled'].includes(value)) {
    return 'bg-yellow-50 text-yellow-700'
  }

  return 'bg-blue-50 text-blue-700'
}

const iconForActivity = (status) => {
  const value = statusKey(status)

  if (['completed', 'complete', 'approved', 'reviewed'].includes(value)) {
    return { icon: 'check', iconBg: 'bg-green-50', iconColor: 'text-green-600' }
  }

  if (value === 'overdue') {
    return { icon: 'clock', iconBg: 'bg-red-50', iconColor: 'text-[#8B1E23]' }
  }

  if (value === 'in progress') {
    return { icon: 'clock', iconBg: 'bg-blue-50', iconColor: 'text-blue-600' }
  }

  return { icon: 'clock', iconBg: 'bg-yellow-50', iconColor: 'text-yellow-600' }
}

const normalizeTaskForModal = (task = {}) => ({
  ...task,
  id: task.id || task.taskId || task._id || `TASK-${Date.now()}`,
  type: task.title || task.type || task.taskTitle || 'Assigned Task',
  location: task.location || task.station || task.assignmentLocation || 'Station',
  time: task.deadline || task.dueDate || task.date || task.schedule || task.time || 'Not set',
  description: task.description || task.instructions || task.note || 'No task details available.'
})

const normalizeActivityForCard = (activity, index) => {
  const status = activity.status || 'Scheduled'
  const base = iconForActivity(status)

  return {
    id: activity.id || `${activity.title || 'activity'}-${index}`,
    title: activity.title || activity.name || activity.type || 'Station Activity',
    schedule: activity.schedule || activity.date || activity.time || 'No schedule',
    status: status,
    icon: base.icon,
    iconBg: base.iconBg,
    iconColor: base.iconColor,
    statusClass: badgeClassForStatus(status)
  }
}

const normalizeRecentActivity = (activity, index) => {
  const status = activity.status || 'Scheduled'
  const base = iconForActivity(status)

  return {
    id: activity.id || `${activity.title || 'activity'}-${index}`,
    title: activity.title || activity.name || activity.type || 'Activity update',
    time: activity.updatedAt || activity.createdAt || activity.date || 'Recently',
    icon: base.icon === 'check' ? '✓' : '↻',
    iconBg: base.iconBg,
    iconColor: base.iconColor
  }
}

const readNotifications = () => {
  for (const key of NOTIFICATION_KEYS) {
    const value = readArray(key)
    if (value.length) return value
  }

  for (let index = 0; index < localStorage.length; index++) {
    const key = localStorage.key(index) || ''
    if (!key.toLowerCase().includes('notification')) continue

    const value = readArray(key)
    if (value.length) return value
  }

  return []
}

const persistNotifications = (items) => {
  for (const key of NOTIFICATION_KEYS) {
    try {
      localStorage.setItem(key, JSON.stringify(items))
      return
    } catch {
      // continue to next preferred key
    }
  }

  try {
    localStorage.setItem('firenotify_notifications', JSON.stringify(items))
  } catch {
    // no-op
  }
}

const refreshDashboard = () => {
  users.value = readArray(USERS_KEY)
  activities.value = readArray(ACTIVITIES_KEY)
  tasks.value = readArray(TASKS_KEY)
  reports.value = readArray(REPORTS_KEY)
  notifications.value = readNotifications().filter(item => notificationMatchesCurrentUser(item) || !Object.keys(item || {}).some(key => ['assignedToId', 'assignedToUsername', 'assignedToEmail', 'userId', 'recipientId', 'personnelId'].includes(key)))
}

const assignedActivities = computed(() => {
  return activities.value.filter(activity => recordMatchesCurrentUser(activity))
})

const assignedTasks = computed(() => {
  return tasks.value.filter(task => recordMatchesCurrentUser(task))
})

const assignedReports = computed(() => {
  return reports.value.filter(report => recordMatchesCurrentUser(report))
})

const pendingActivities = computed(() => {
  return assignedActivities.value.filter(item => {
    const status = item?.status || 'Scheduled'
    return isPendingStatus(status) || (!status && item?.date)
  }).length
})

const completedActivities = computed(() => {
  return assignedActivities.value.filter(item => isCompletedStatus(item?.status)).length
})

const overdueActivities = computed(() => {
  return assignedActivities.value.filter(item => isOverdueStatus(item)).length
})

const activityCompliance = computed(() => {
  if (!assignedActivities.value.length) return 0
  return Math.round((completedActivities.value / assignedActivities.value.length) * 100)
})

const pendingTasks = computed(() => {
  return assignedTasks.value.filter(item => isPendingStatus(item?.status) || item?.status === 'In Progress').length
})

const completedTasks = computed(() => {
  return assignedTasks.value.filter(item => isCompletedStatus(item?.status)).length
})

const overdueTasks = computed(() => {
  return assignedTasks.value.filter(item => isOverdueStatus(item)).length
})

const taskStats = computed(() => ({
  total: assignedTasks.value.length,
  pending: pendingTasks.value,
  completed: completedTasks.value,
  weeklyTotal: Math.max(assignedTasks.value.length, 1)
}))

const completionPercentage = computed(() => {
  const total = taskStats.value.weeklyTotal
  if (!total) return 0
  return Math.round((taskStats.value.completed / total) * 100)
})

const pendingReports = computed(() => {
  return assignedReports.value.filter(item => {
    const status = statusKey(item?.status)
    return ['pending', 'submitted', 'for review', 'in progress', 'draft'].includes(status)
  }).length
})

const reviewedReports = computed(() => {
  return assignedReports.value.filter(item => {
    const status = statusKey(item?.status)
    return ['approved', 'reviewed', 'completed', 'complete', 'resolved'].includes(status)
  }).length
})

const reportCompliance = computed(() => {
  if (!assignedReports.value.length) return 0
  return Math.round((reviewedReports.value / assignedReports.value.length) * 100)
})

const reportCount = computed(() => pendingReports.value)
const urgentCount = computed(() => overdueTasks.value + overdueActivities.value + pendingReports.value)

const unreadNotifications = computed(() => {
  return notifications.value.filter(notification => !notification.read).length
})

const currentDate = computed(() => {
  return new Intl.DateTimeFormat('en-US', {
    weekday: 'long',
    month: 'long',
    day: 'numeric',
    year: 'numeric'
  }).format(new Date())
})

const dutyStatus = computed(() => {
  const user = getCurrentUser()
  if (!user) return 'On Duty'
  return user.status === 'Inactive' || user.status === 'Off Duty' ? 'Off Duty' : 'On Duty'
})

const todayAssignment = computed(() => {
  const scheduledTask = assignedTasks.value.find(task => !isCompletedStatus(task?.status)) || assignedTasks.value[0]

  if (scheduledTask) {
    return {
      type: scheduledTask.title || scheduledTask.type || 'Assigned Task',
      location: scheduledTask.location || scheduledTask.station || 'Assigned Station',
      time: scheduledTask.deadline || scheduledTask.dueDate || scheduledTask.date || scheduledTask.schedule || scheduledTask.time || 'No due date',
      description: scheduledTask.description || scheduledTask.instructions || 'No task details available.'
    }
  }

  const scheduledActivity = assignedActivities.value.find(item => !isCompletedStatus(item?.status)) || assignedActivities.value[0]

  if (scheduledActivity) {
    return {
      type: scheduledActivity.type || 'Station Activity',
      location: scheduledActivity.location || 'Assigned Station',
      time: scheduledActivity.date || scheduledActivity.schedule || scheduledActivity.time || 'No schedule',
      description: scheduledActivity.description || 'No activity details available.'
    }
  }

  return {
    type: 'No active assignment',
    location: 'Awaiting assignment',
    time: 'No due date',
    description: 'There are no current personnel assignments for this user.'
  }
})

const upcomingActivities = computed(() => {
  return assignedActivities.value.slice(0, 3).map((activity, index) => normalizeActivityForCard(activity, index))
})

const recentActivities = computed(() => {
  return [...assignedActivities.value]
    .sort((a, b) => {
      const aTime = parseDateValue(a.updatedAt || a.createdAt || a.date)?.getTime() || 0
      const bTime = parseDateValue(b.updatedAt || b.createdAt || b.date)?.getTime() || 0
      return bTime - aTime
    })
    .slice(0, 3)
    .map((activity, index) => normalizeRecentActivity(activity, index))
})

const viewTask = (task) => {
  selectedTask.value = normalizeTaskForModal(task)
}

const closeTask = () => {
  selectedTask.value = null
}

const acknowledgeTask = () => {
  if (!selectedTask.value) return

  const recordId = String(selectedTask.value.id || '')
  const updatedTasks = tasks.value.map(task => {
    const taskId = String(task.id || task.taskId || task._id || '')
    if (!recordId || taskId !== recordId) return task

    return {
      ...task,
      status: 'Completed',
      completedAt: new Date().toISOString()
    }
  })

  tasks.value = updatedTasks
  localStorage.setItem(TASKS_KEY, JSON.stringify(updatedTasks))
  window.dispatchEvent(new CustomEvent('fireNotifyTasksUpdated'))
  selectedTask.value = null
}

const markNotificationRead = (id) => {
  notifications.value = notifications.value.map(item => {
    if (String(item.id) !== String(id)) return item
    return { ...item, read: true }
  })

  persistNotifications(notifications.value)
  window.dispatchEvent(new CustomEvent('fireNotifyNotificationsUpdated'))
}

const markAllNotificationsRead = () => {
  notifications.value = notifications.value.map(item => ({ ...item, read: true }))
  persistNotifications(notifications.value)
  window.dispatchEvent(new CustomEvent('fireNotifyNotificationsUpdated'))
}

const toggleDutyStatus = () => {
  dutyStatus.value = dutyStatus.value === 'On Duty' ? 'Off Duty' : 'On Duty'
}

onMounted(() => {
  refreshDashboard()

  window.addEventListener('storage', refreshDashboard)
  window.addEventListener('focus', refreshDashboard)

  UPDATE_EVENTS.forEach(eventName => {
    window.addEventListener(eventName, refreshDashboard)
  })

  refreshTimer = setInterval(refreshDashboard, 800)
})

onBeforeUnmount(() => {
  window.removeEventListener('storage', refreshDashboard)
  window.removeEventListener('focus', refreshDashboard)

  UPDATE_EVENTS.forEach(eventName => {
    window.removeEventListener(eventName, refreshDashboard)
  })

  if (refreshTimer) {
    clearInterval(refreshTimer)
  }
})
</script>
