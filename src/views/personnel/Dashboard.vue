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
            Welcome back, {{ currentUser?.firstName || 'Juan' }}!
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
import { computed, ref } from 'vue'


/* =========================================================
   PROPS
========================================================= */

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


/* =========================================================
   SHARED DATA
========================================================= */

const dutyStatus = ref('On Duty')

const reportCount = ref(3)
const urgentCount = ref(2)

const selectedTask = ref(null)


/* =========================================================
   TODAY'S ASSIGNMENT
========================================================= */

const todayAssignment = {
  type: 'FIRE SAFETY INSPECTION',
  location: 'Public Market Complex',
  time: '09:00 AM',
  description:
    'Scheduled inspection and fire safety compliance checking.'
}


/* =========================================================
   TASK STATISTICS
========================================================= */

const taskStats = ref({
  total: 4,
  pending: 2,
  completed: 6,
  weeklyTotal: 8
})


const completionPercentage = computed(() => {
  if (!taskStats.value.weeklyTotal) return 0

  return Math.round(
    (taskStats.value.completed /
      taskStats.value.weeklyTotal) *
      100
  )
})


/* =========================================================
   UPCOMING ACTIVITIES
========================================================= */

const upcomingActivities = ref([
  {
    id: 1,
    title: 'Fire Drill Evaluation',
    schedule: 'Tomorrow · 08:30 AM',
    status: 'Upcoming',
    icon: 'clock',
    iconBg: 'bg-red-50',
    iconColor: 'text-[#8B1E23]',
    statusClass: 'bg-yellow-50 text-yellow-700'
  },

  {
    id: 2,
    title: 'Monthly Station Report',
    schedule: 'September 15 · 04:00 PM',
    status: 'Scheduled',
    icon: 'reports',
    iconBg: 'bg-green-50',
    iconColor: 'text-green-600',
    statusClass: 'bg-blue-50 text-blue-700'
  },

  {
    id: 3,
    title: 'Personnel Training',
    schedule: 'September 18 · 09:00 AM',
    status: 'Training',
    icon: 'roster',
    iconBg: 'bg-purple-50',
    iconColor: 'text-purple-600',
    statusClass: 'bg-purple-50 text-purple-700'
  }
])


/* =========================================================
   RECENT ACTIVITIES
========================================================= */

const recentActivities = ref([
  {
    id: 1,
    title: 'Fire Safety Inspection completed',
    time: 'Today · 10:42 AM',
    icon: '✓',
    iconBg: 'bg-green-100',
    iconColor: 'text-green-600'
  },

  {
    id: 2,
    title: 'Emergency Response Drill updated',
    time: 'Yesterday · 03:20 PM',
    icon: '↻',
    iconBg: 'bg-blue-100',
    iconColor: 'text-blue-600'
  },

  {
    id: 3,
    title: 'Monthly report requires submission',
    time: 'Yesterday · 01:15 PM',
    icon: '!',
    iconBg: 'bg-yellow-100',
    iconColor: 'text-yellow-600'
  }
])


/* =========================================================
   NOTIFICATIONS
========================================================= */

const notifications = ref([
  {
    id: 1,
    title: 'Task deadline approaching',
    message: 'Monthly report is due tomorrow.',
    bg: 'bg-red-50',
    read: false
  },

  {
    id: 2,
    title: 'New task assigned',
    message: 'Fire drill evaluation has been assigned.',
    bg: 'bg-blue-50',
    read: false
  },

  {
    id: 3,
    title: 'Reminder',
    message: 'Personnel training is scheduled this week.',
    bg: 'bg-yellow-50',
    read: false
  }
])


/* =========================================================
   COMPUTED VALUES
========================================================= */

const unreadNotifications = computed(() => {
  return notifications.value.filter(
    notification => !notification.read
  ).length
})


const currentDate = computed(() => {
  return new Intl.DateTimeFormat('en-US', {
    weekday: 'long',
    month: 'long',
    day: 'numeric',
    year: 'numeric'
  }).format(new Date())
})


/* =========================================================
   TASK FUNCTIONS
========================================================= */

const viewTask = (task) => {
  selectedTask.value = task
}


const closeTask = () => {
  selectedTask.value = null
}


const acknowledgeTask = () => {
  if (!selectedTask.value) return

  taskStats.value.pending = Math.max(
    0,
    taskStats.value.pending - 1
  )

  selectedTask.value = null
}


/* =========================================================
   NOTIFICATION FUNCTIONS
========================================================= */

const markNotificationRead = (id) => {
  const notification = notifications.value.find(
    item => item.id === id
  )

  if (notification) {
    notification.read = true
  }
}


const markAllNotificationsRead = () => {
  notifications.value.forEach(
    notification => {
      notification.read = true
    }
  )
}


/* =========================================================
   FUTURE STATUS FUNCTION
========================================================= */

const toggleDutyStatus = () => {
  dutyStatus.value =
    dutyStatus.value === 'On Duty'
      ? 'Off Duty'
      : 'On Duty'
}
</script>