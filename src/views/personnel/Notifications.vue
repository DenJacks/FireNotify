<template>
  <div class="w-full min-w-0 space-y-6">

    <!-- HEADER -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
        <div>
          <div class="flex items-center gap-3">
            <div class="h-11 w-11 rounded-xl bg-red-50 flex items-center justify-center">
              <span
                v-html="ICONS.siren"
                class="h-6 w-6 text-[#8B1E23]"
              ></span>
            </div>

            <div>
              <h2 class="text-2xl font-bold text-slate-900">
                Notifications
              </h2>

              <p class="text-sm text-slate-500 mt-1">
                Important announcements, reminders, and system alerts
              </p>
            </div>
          </div>
        </div>

        <button
          @click="markAllAsRead"
          :disabled="unreadCount === 0"
          class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-semibold
                 hover:bg-[#72181D] transition disabled:opacity-40
                 disabled:cursor-not-allowed"
        >
          Mark All as Read
        </button>
      </div>
    </section>


    <!-- STATISTICS -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">

      <!-- UNREAD -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-slate-500">Unread</p>

            <p class="text-3xl font-bold text-[#8B1E23] mt-1">
              {{ String(unreadCount).padStart(2, '0') }}
            </p>
          </div>

          <div class="h-11 w-11 rounded-full bg-red-100 flex items-center justify-center">
            <span
              v-html="ICONS.siren"
              class="h-5 w-5 text-[#8B1E23]"
            ></span>
          </div>
        </div>
      </div>


      <!-- TASK ALERTS -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-slate-500">Task Alerts</p>

            <p class="text-3xl font-bold text-slate-900 mt-1">
              {{ String(taskAlertCount).padStart(2, '0') }}
            </p>
          </div>

          <div class="h-11 w-11 rounded-full bg-blue-100 flex items-center justify-center">
            <span
              v-html="ICONS.tasks"
              class="h-5 w-5 text-blue-600"
            ></span>
          </div>
        </div>
      </div>


      <!-- REPORT ALERTS -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-slate-500">Report Alerts</p>

            <p class="text-3xl font-bold text-slate-900 mt-1">
              {{ String(reportAlertCount).padStart(2, '0') }}
            </p>
          </div>

          <div class="h-11 w-11 rounded-full bg-amber-100 flex items-center justify-center">
            <span
              v-html="ICONS.reports"
              class="h-5 w-5 text-amber-600"
            ></span>
          </div>
        </div>
      </div>


      <!-- SYSTEM ALERTS -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-slate-500">System Alerts</p>

            <p class="text-3xl font-bold text-slate-900 mt-1">
              {{ String(systemAlertCount).padStart(2, '0') }}
            </p>
          </div>

          <div class="h-11 w-11 rounded-full bg-green-100 flex items-center justify-center">
            <span
              v-html="ICONS.check"
              class="h-5 w-5 text-green-600"
            ></span>
          </div>
        </div>
      </div>

    </section>


    <!-- SEARCH AND FILTERS -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">

        <!-- SEARCH -->
        <div class="lg:col-span-1">
          <label class="text-sm font-semibold text-slate-700">
            Search Notifications
          </label>

          <div class="relative mt-2">
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Search notifications..."
              class="w-full px-4 py-3 rounded-xl border border-slate-300
                     focus:outline-none focus:ring-2 focus:ring-[#8B1E23]"
            />
          </div>
        </div>


        <!-- TYPE -->
        <div>
          <label class="text-sm font-semibold text-slate-700">
            Notification Type
          </label>

          <select
            v-model="selectedType"
            class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300
                   bg-white text-slate-700 focus:outline-none
                   focus:ring-2 focus:ring-[#8B1E23]"
          >
            <option value="All">All Notifications</option>
            <option value="Task Alerts">Task Alerts</option>
            <option value="Report Alerts">Report Alerts</option>
            <option value="Activity Reminders">Activity Reminders</option>
            <option value="System Alerts">System Alerts</option>
          </select>
        </div>


        <!-- STATUS -->
        <div>
          <label class="text-sm font-semibold text-slate-700">
            Status
          </label>

          <select
            v-model="selectedStatus"
            class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300
                   bg-white text-slate-700 focus:outline-none
                   focus:ring-2 focus:ring-[#8B1E23]"
          >
            <option value="All">All</option>
            <option value="Unread">Unread</option>
            <option value="Read">Read</option>
          </select>
        </div>

      </div>
    </section>


    <!-- NOTIFICATIONS + SIDEBAR -->
    <section class="grid grid-cols-1 lg:grid-cols-3 gap-6">

      <!-- NOTIFICATION LIST -->
      <div class="lg:col-span-2 space-y-4">

        <div
          v-for="notification in filteredNotifications"
          :key="notification.id"
          :class="[
            'p-5 rounded-2xl border shadow-sm transition',
            notification.read
              ? 'bg-white border-slate-200'
              : getNotificationBackground(notification.type)
          ]"
        >

          <div class="flex items-start gap-4">

            <!-- ICON -->
            <div
              :class="[
                'h-12 w-12 rounded-full flex items-center justify-center shrink-0',
                getIconBackground(notification.type)
              ]"
            >
              <span
                v-html="getNotificationIcon(notification.type)"
                :class="[
                  'h-6 w-6',
                  getIconColor(notification.type)
                ]"
              ></span>
            </div>


            <!-- CONTENT -->
            <div class="flex-1 min-w-0">

              <div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-2">

                <div>
                  <div class="flex items-center gap-2 flex-wrap">

                    <h3 class="text-base font-bold text-slate-900">
                      {{ notification.title }}
                    </h3>

                    <span
                      v-if="!notification.read"
                      class="px-2 py-0.5 rounded-full bg-[#8B1E23]
                             text-white text-[10px] font-bold"
                    >
                      UNREAD
                    </span>

                    <span
                      v-else
                      class="px-2 py-0.5 rounded-full bg-slate-100
                             text-slate-500 text-[10px] font-bold"
                    >
                      READ
                    </span>

                  </div>
                </div>


                <!-- PRIORITY -->
                <span
                  :class="[
                    'px-2.5 py-1 rounded-full text-[10px] font-bold whitespace-nowrap',
                    getPriorityClass(notification.priority)
                  ]"
                >
                  {{ notification.priority }}
                </span>

              </div>


              <p class="text-sm text-slate-600 mt-2 leading-relaxed">
                {{ notification.message }}
              </p>


              <div class="flex flex-wrap items-center gap-2 mt-3">

                <span class="text-xs text-slate-400">
                  {{ notification.time }}
                </span>

                <span class="h-1 w-1 rounded-full bg-slate-300"></span>

                <span
                  class="text-xs font-medium"
                  :class="getTypeTextColor(notification.type)"
                >
                  {{ notification.type }}
                </span>

              </div>


              <!-- ACTIONS -->
              <div class="flex flex-wrap gap-2 mt-4">

                <button
                  @click="viewNotification(notification)"
                  class="px-3 py-2 rounded-lg border border-slate-300
                         text-xs font-semibold text-slate-700
                         hover:bg-slate-50 transition"
                >
                  View Details
                </button>

                <button
                  @click="toggleRead(notification)"
                  class="px-3 py-2 rounded-lg border border-slate-300
                         text-xs font-semibold text-slate-700
                         hover:bg-slate-50 transition"
                >
                  {{ notification.read ? 'Mark Unread' : 'Mark Read' }}
                </button>

                <button
                  @click="deleteNotification(notification.id)"
                  class="px-3 py-2 rounded-lg border border-red-200
                         text-xs font-semibold text-red-600
                         hover:bg-red-50 transition"
                >
                  Delete
                </button>

              </div>

            </div>


            <!-- UNREAD INDICATOR -->
            <span
              v-if="!notification.read"
              class="h-3 w-3 rounded-full bg-[#8B1E23] shrink-0"
            ></span>

          </div>
        </div>


        <!-- EMPTY STATE -->
        <div
          v-if="filteredNotifications.length === 0"
          class="bg-white border border-slate-200 rounded-2xl p-10 text-center"
        >
          <div class="h-14 w-14 mx-auto rounded-full bg-slate-100 flex items-center justify-center">
            <span
              v-html="ICONS.check"
              class="h-7 w-7 text-slate-400"
            ></span>
          </div>

          <h3 class="mt-4 text-lg font-bold text-slate-900">
            No notifications found
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            Try changing your search or filter settings.
          </p>
        </div>

      </div>


      <!-- RIGHT SIDEBAR -->
      <div class="space-y-6">

        <!-- SETTINGS -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <h3 class="text-lg font-bold text-slate-900">
            Notification Settings
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            Choose how you receive important alerts.
          </p>


          <div class="mt-5 space-y-5">

            <div
              v-for="setting in notificationSettings"
              :key="setting.key"
              class="flex items-center justify-between gap-4"
            >

              <div>
                <p class="text-sm font-semibold text-slate-800">
                  {{ setting.title }}
                </p>

                <p class="text-xs text-slate-500 mt-0.5">
                  {{ setting.description }}
                </p>
              </div>

              <button
                @click="setting.enabled = !setting.enabled"
                :aria-pressed="setting.enabled"
                :class="[
                  'relative w-11 h-6 rounded-full transition shrink-0',
                  setting.enabled
                    ? 'bg-[#8B1E23]'
                    : 'bg-slate-300'
                ]"
              >
                <span
                  :class="[
                    'absolute top-1 h-4 w-4 rounded-full bg-white shadow transition',
                    setting.enabled
                      ? 'left-6'
                      : 'left-1'
                  ]"
                ></span>
              </button>

            </div>

          </div>

        </div>


        <!-- UPCOMING DEADLINES -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <div class="flex items-center justify-between">
            <div>
              <h3 class="text-lg font-bold text-slate-900">
                Upcoming Deadlines
              </h3>

              <p class="text-xs text-slate-500 mt-1">
                Reports requiring attention
              </p>
            </div>

            <span
              class="px-2.5 py-1 rounded-full bg-red-50
                     text-[#8B1E23] text-xs font-bold"
            >
              {{ deadlines.length }}
            </span>
          </div>


          <div class="mt-4 space-y-3">

            <div
              v-for="deadline in deadlines"
              :key="deadline.id"
              :class="[
                'p-4 rounded-xl border',
                deadline.urgent
                  ? 'bg-red-50 border-red-100'
                  : 'bg-slate-50 border-slate-200'
              ]"
            >

              <div class="flex items-start justify-between gap-3">

                <div>
                  <p class="text-sm font-bold text-slate-900">
                    {{ deadline.title }}
                  </p>

                  <p
                    class="text-xs font-semibold mt-1"
                    :class="
                      deadline.urgent
                        ? 'text-red-600'
                        : 'text-slate-500'
                    "
                  >
                    {{ deadline.due }}
                  </p>
                </div>

                <span
                  v-if="deadline.urgent"
                  class="text-[10px] font-bold text-red-600"
                >
                  URGENT
                </span>

              </div>

            </div>

          </div>
        </div>


        <!-- QUICK SUMMARY -->
        <div class="bg-[#8B1E23] rounded-2xl shadow-sm p-6 text-white">

          <p class="text-sm text-red-100">
            Notification Summary
          </p>

          <p class="text-3xl font-bold mt-1">
            {{ notifications.length }}
          </p>

          <p class="text-sm text-red-100 mt-1">
            Total notifications
          </p>

          <div class="mt-5 pt-4 border-t border-white/20">

            <div class="flex items-center justify-between">
              <span class="text-sm text-red-100">
                Requiring attention
              </span>

              <span class="font-bold">
                {{ unreadCount }}
              </span>
            </div>

          </div>

        </div>

      </div>

    </section>


    <!-- VIEW DETAILS MODAL -->
    <div
      v-if="selectedNotification"
      class="fixed inset-0 z-50 bg-black/40 flex items-center justify-center p-4"
      @click.self="selectedNotification = null"
    >

      <div class="bg-white w-full max-w-lg rounded-2xl shadow-xl overflow-hidden">

        <div class="bg-[#8B1E23] px-6 py-5 text-white">

          <div class="flex items-center justify-between">

            <div>
              <p class="text-xs text-red-100 uppercase tracking-wide">
                Notification Details
              </p>

              <h3 class="text-xl font-bold mt-1">
                {{ selectedNotification.title }}
              </h3>
            </div>

            <button
              @click="selectedNotification = null"
              class="h-9 w-9 rounded-lg bg-white/10 hover:bg-white/20"
            >
              ✕
            </button>

          </div>

        </div>


        <div class="p-6 space-y-5">

          <div>
            <p class="text-xs font-semibold text-slate-500 uppercase">
              Message
            </p>

            <p class="text-sm text-slate-700 mt-1 leading-relaxed">
              {{ selectedNotification.message }}
            </p>
          </div>


          <div class="grid grid-cols-2 gap-4">

            <div class="bg-slate-50 rounded-xl p-4">
              <p class="text-xs text-slate-500">
                Type
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedNotification.type }}
              </p>
            </div>

            <div class="bg-slate-50 rounded-xl p-4">
              <p class="text-xs text-slate-500">
                Priority
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedNotification.priority }}
              </p>
            </div>

          </div>


          <div class="bg-slate-50 rounded-xl p-4">

            <p class="text-xs text-slate-500">
              Received
            </p>

            <p class="text-sm font-semibold text-slate-900 mt-1">
              {{ selectedNotification.time }}
            </p>

          </div>


          <div class="flex justify-end gap-3">

            <button
              @click="toggleRead(selectedNotification)"
              class="px-4 py-2.5 rounded-xl border border-slate-300
                     text-sm font-semibold hover:bg-slate-50"
            >
              {{ selectedNotification.read ? 'Mark Unread' : 'Mark Read' }}
            </button>

            <button
              @click="selectedNotification = null"
              class="px-4 py-2.5 rounded-xl bg-[#8B1E23]
                     text-white text-sm font-semibold hover:bg-[#72181D]"
            >
              Close
            </button>

          </div>

        </div>

      </div>

    </div>


    <!-- TOAST -->
    <transition name="toast">

      <div
        v-if="toastMessage"
        class="fixed bottom-6 right-6 z-[60] bg-slate-900
               text-white px-5 py-3 rounded-xl shadow-lg
               text-sm font-semibold"
      >
        {{ toastMessage }}
      </div>

    </transition>

  </div>
</template>


<script setup>
import { computed, ref } from 'vue'

const props = defineProps({
  ICONS: {
    type: Object,
    required: true
  }
})


/* =========================================================
   STATE
========================================================= */

const searchQuery = ref('')
const selectedType = ref('All')
const selectedStatus = ref('All')

const selectedNotification = ref(null)
const toastMessage = ref('')


/* =========================================================
   SAMPLE NOTIFICATIONS
   Frontend demo data.
   Later this can come from Django REST API.
========================================================= */

const notifications = ref([
  {
    id: 1,
    title: 'Report Deadline Reminder',
    message:
      'Your Fire Safety Inspection Report is due on September 12, 2026.',
    type: 'Report Alerts',
    priority: 'URGENT',
    time: '10 minutes ago',
    read: false
  },
  {
    id: 2,
    title: 'New Task Assigned',
    message:
      'You have been assigned to the Public Market Fire Safety Inspection.',
    type: 'Task Alerts',
    priority: 'HIGH',
    time: '1 hour ago',
    read: false
  },
  {
    id: 3,
    title: 'Report Accepted',
    message:
      'Your Routine Safety Patrol Report has been successfully recorded.',
    type: 'Report Alerts',
    priority: 'NORMAL',
    time: 'Yesterday',
    read: true
  },
  {
    id: 4,
    title: 'Activity Reminder',
    message:
      'Your scheduled Fire Safety Seminar will begin tomorrow at 9:00 AM.',
    type: 'Activity Reminders',
    priority: 'HIGH',
    time: 'Yesterday',
    read: false
  },
  {
    id: 5,
    title: 'System Update',
    message:
      'FireNotify notification services are operating normally.',
    type: 'System Alerts',
    priority: 'NORMAL',
    time: '2 days ago',
    read: true
  }
])


/* =========================================================
   NOTIFICATION SETTINGS
========================================================= */

const notificationSettings = ref([
  {
    key: 'tasks',
    title: 'Task Reminders',
    description: 'Alerts for assigned tasks',
    enabled: true
  },
  {
    key: 'reports',
    title: 'Report Deadlines',
    description: 'Reminders before deadlines',
    enabled: true
  },
  {
    key: 'activities',
    title: 'Activity Alerts',
    description: 'Upcoming activity reminders',
    enabled: true
  }
])


/* =========================================================
   DEADLINES
========================================================= */

const deadlines = ref([
  {
    id: 1,
    title: 'Fire Safety Inspection Report',
    due: 'Due Today',
    urgent: true
  },
  {
    id: 2,
    title: 'Monthly Operations Report',
    due: 'Due in 5 days',
    urgent: false
  },
  {
    id: 3,
    title: 'Activity Compliance Report',
    due: 'Due in 8 days',
    urgent: false
  }
])


/* =========================================================
   COMPUTED COUNTERS
========================================================= */

const unreadCount = computed(() => {
  return notifications.value.filter(item => !item.read).length
})

const taskAlertCount = computed(() => {
  return notifications.value.filter(
    item => item.type === 'Task Alerts'
  ).length
})

const reportAlertCount = computed(() => {
  return notifications.value.filter(
    item => item.type === 'Report Alerts'
  ).length
})

const systemAlertCount = computed(() => {
  return notifications.value.filter(
    item => item.type === 'System Alerts'
  ).length
})


/* =========================================================
   FILTERED NOTIFICATIONS
========================================================= */

const filteredNotifications = computed(() => {
  const query = searchQuery.value.toLowerCase().trim()

  return notifications.value.filter(notification => {

    const matchesSearch =
      !query ||
      notification.title.toLowerCase().includes(query) ||
      notification.message.toLowerCase().includes(query) ||
      notification.type.toLowerCase().includes(query)

    const matchesType =
      selectedType.value === 'All' ||
      notification.type === selectedType.value

    const matchesStatus =
      selectedStatus.value === 'All' ||
      (selectedStatus.value === 'Unread' && !notification.read) ||
      (selectedStatus.value === 'Read' && notification.read)

    return matchesSearch && matchesType && matchesStatus
  })
})


/* =========================================================
   ACTIONS
========================================================= */

const showToast = (message) => {
  toastMessage.value = message

  setTimeout(() => {
    toastMessage.value = ''
  }, 2500)
}


const markAllAsRead = () => {
  notifications.value.forEach(notification => {
    notification.read = true
  })

  showToast('All notifications marked as read.')
}


const toggleRead = (notification) => {
  notification.read = !notification.read

  showToast(
    notification.read
      ? 'Notification marked as read.'
      : 'Notification marked as unread.'
  )
}


const deleteNotification = (id) => {
  notifications.value = notifications.value.filter(
    notification => notification.id !== id
  )

  if (
    selectedNotification.value &&
    selectedNotification.value.id === id
  ) {
    selectedNotification.value = null
  }

  showToast('Notification deleted.')
}


const viewNotification = (notification) => {
  selectedNotification.value = notification

  if (!notification.read) {
    notification.read = true
  }
}


/* =========================================================
   ICON HELPERS
========================================================= */

const getNotificationIcon = (type) => {

  if (type === 'Task Alerts') {
    return props.ICONS.tasks
  }

  if (type === 'Report Alerts') {
    return props.ICONS.reports
  }

  if (type === 'System Alerts') {
    return props.ICONS.check
  }

  return props.ICONS.siren
}


const getIconBackground = (type) => {

  if (type === 'Task Alerts') {
    return 'bg-blue-100'
  }

  if (type === 'Report Alerts') {
    return 'bg-amber-100'
  }

  if (type === 'System Alerts') {
    return 'bg-green-100'
  }

  return 'bg-red-100'
}


const getIconColor = (type) => {

  if (type === 'Task Alerts') {
    return 'text-blue-600'
  }

  if (type === 'Report Alerts') {
    return 'text-amber-600'
  }

  if (type === 'System Alerts') {
    return 'text-green-600'
  }

  return 'text-[#8B1E23]'
}


const getNotificationBackground = (type) => {

  if (type === 'Task Alerts') {
    return 'bg-blue-50 border-blue-200'
  }

  if (type === 'Report Alerts') {
    return 'bg-amber-50 border-amber-200'
  }

  if (type === 'System Alerts') {
    return 'bg-green-50 border-green-200'
  }

  return 'bg-red-50 border-red-200'
}


const getTypeTextColor = (type) => {

  if (type === 'Task Alerts') {
    return 'text-blue-600'
  }

  if (type === 'Report Alerts') {
    return 'text-amber-600'
  }

  if (type === 'System Alerts') {
    return 'text-green-600'
  }

  return 'text-[#8B1E23]'
}


const getPriorityClass = (priority) => {

  if (priority === 'URGENT') {
    return 'bg-red-100 text-red-700'
  }

  if (priority === 'HIGH') {
    return 'bg-amber-100 text-amber-700'
  }

  return 'bg-slate-100 text-slate-600'
}
</script>


<style scoped>
.toast-enter-active,
.toast-leave-active {
  transition: all 0.25s ease;
}

.toast-enter-from,
.toast-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>