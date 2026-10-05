<script setup>
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'

import {
  deleteNotification as deleteNotificationInApi,
  getNotifications,
  markAllNotificationsRead,
  setNotificationRead
} from '../../utils/notificationApi.js'

const NOTIFICATION_EVENTS = ['fireNotifyNotificationsUpdated']
const isNotificationRead = notification => Boolean(notification?.is_read ?? notification?.read ?? String(notification?.status || '').toLowerCase() === 'read')

const props = defineProps({
  currentUser: {
    type: Object,
    default: null
  },
  ICONS: {
    type: Object,
    default: () => ({})
  }
})

const searchQuery = ref('')
const selectedFilter = ref('All Notifications')
const selectedStatus = ref('All')
const selectedNotification = ref(null)
const showDetailsModal = ref(false)
const toastMessage = ref('')
const notifications = ref([])
const showDeleteAllModal = ref(false)
let notificationRefreshTimer = null

const normalizeNotification = (item, index = 0) => {
  const id = item?.id ?? item?.notificationId ?? item?._id ??
    `${item?.sourceType || item?.type || 'notification'}-${item?.sourceId || item?.recordId || index}`
  const status = String(item?.status || '').trim()
  const read = isNotificationRead(item)

  const title =
    item?.title ||
    item?.subject ||
    item?.message ||
    item?.name ||
    'Notification'

  const detail =
    item?.detail ||
    item?.message ||
    item?.description ||
    item?.body ||
    'No additional details available.'

  const tone =
    item?.tone ||
    item?.color ||
    (
      String(item?.type || '').includes('Deadline')
        ? 'red'
        : String(item?.type || '').includes('Personnel')
          ? 'blue'
          : String(item?.type || '').includes('Report')
            ? 'green'
            : String(item?.type || '').includes('System')
              ? 'purple'
              : 'slate'
    )

  const type =
    item?.type ||
    item?.category ||
    item?.kind ||
    'System Announcements'

  const icon =
    item?.icon ||
    (
      tone === 'red'
        ? '🚨'
        : tone === 'yellow'
          ? '⚠️'
          : tone === 'blue'
            ? '📋'
            : tone === 'green'
              ? '✓'
              : tone === 'purple'
                ? '📢'
                : '🔔'
    )

  const rawTime = item?.time || item?.createdAt || item?.timestamp || item?.date
  const parsedTime = rawTime ? new Date(String(rawTime).replace(/•/g, ' ').trim()) : null
  const time = parsedTime && !Number.isNaN(parsedTime.getTime()) && parsedTime.getFullYear() >= 1970
    ? parsedTime.toLocaleString('en-US', { dateStyle: 'medium', timeStyle: 'short' })
    : 'Recently'

  return {
    ...item,
    id,
    title,
    detail,
    type,
    tone,
    icon,
    time,
    read,
    status
  }
}

const refreshNotifications = async () => {
  try {
    notifications.value = (await getNotifications(props.currentUser))
      .map((item, index) => normalizeNotification(item, index))
  } catch (error) {
    console.error('FireNotify: unable to load notifications from Django', error)
    notifications.value = []
  }
}

const markAllAsRead = async () => {
  await markAllNotificationsRead(props.currentUser)
  await refreshNotifications()
  showToast('All notifications marked as read.')
}

const toggleRead = async notification => {
  await setNotificationRead(notification, props.currentUser, !isNotificationRead(notification))
  await refreshNotifications()
  showToast(
    isNotificationRead(notification)
      ? 'Notification marked as unread.'
      : 'Notification marked as read.'
  )
}

const deleteNotification = async notification => {
  await deleteNotificationInApi(notification, props.currentUser)
  await refreshNotifications()
  showToast('Notification deleted.')
}

const deleteAll = async () => {
  await Promise.all(notifications.value.map(notification => deleteNotificationInApi(notification, props.currentUser)))
  await refreshNotifications()
  showDeleteAllModal.value = false
  showToast('All notifications deleted.')
}

const viewNotification = async notification => {
  selectedNotification.value = notification

  if (!isNotificationRead(notification)) {
    await setNotificationRead(notification, props.currentUser, true)
    await refreshNotifications()
  }

  showDetailsModal.value = true
}

const channelSummary = computed(() => [
  {
    label: 'System Alerts',
    count: notifications.value.filter(item => item.type === 'System Announcements').length,
    color: 'text-[#8B1E23]'
  },
  {
    label: 'Personnel Updates',
    count: notifications.value.filter(item => item.type === 'Personnel Updates').length,
    color: 'text-blue-600'
  },
  {
    label: 'Reports & Compliance',
    count: notifications.value.filter(item => item.type === 'Reports & Compliance').length,
    color: 'text-green-600'
  },
  {
    label: 'Deadline Alerts',
    count: notifications.value.filter(item => item.type === 'Deadline Alerts').length,
    color: 'text-yellow-600'
  }
])

const unreadCount = computed(() =>
  notifications.value.filter(item => !isNotificationRead(item)).length
)

const deadlineCount = computed(() =>
  notifications.value.filter(item => item.type === 'Deadline Alerts').length
)

const activityCount = computed(() =>
  notifications.value.filter(item => item.type === 'Personnel Updates').length
)

const filteredNotifications = computed(() => {
  const query = searchQuery.value.toLowerCase().trim()

  return notifications.value.filter(item => {
    const matchesSearch =
      !query ||
      `${item.title} ${item.detail} ${item.type}`
        .toLowerCase()
        .includes(query)

    const matchesFilter =
      selectedFilter.value === 'All Notifications' ||
      item.type === selectedFilter.value

    const matchesStatus =
      selectedStatus.value === 'All' ||
      (selectedStatus.value === 'Unread' && !isNotificationRead(item)) ||
      (selectedStatus.value === 'Read' && isNotificationRead(item))

    return matchesSearch && matchesFilter && matchesStatus
  })
})

const hasFilters = computed(() =>
  searchQuery.value ||
  selectedFilter.value !== 'All Notifications' ||
  selectedStatus.value !== 'All'
)

const showToast = message => {
  toastMessage.value = message

  setTimeout(() => {
    toastMessage.value = ''
  }, 3000)
}

const clearFilters = () => {
  searchQuery.value = ''
  selectedFilter.value = 'All Notifications'
  selectedStatus.value = 'All'
}

const selectFilter = filter => {
  selectedFilter.value = filter
}

const getToneClass = tone => {
  const classes = {
    red: 'border-red-200 bg-red-50',
    yellow: 'border-yellow-200 bg-yellow-50',
    blue: 'border-blue-200 bg-blue-50',
    green: 'border-green-200 bg-green-50',
    purple: 'border-purple-200 bg-purple-50',
    orange: 'border-orange-200 bg-orange-50',
    slate: 'border-slate-200 bg-slate-50'
  }

  return classes[tone] || 'border-slate-200 bg-slate-50'
}

const getIconClass = tone => {
  const classes = {
    red: 'bg-red-100',
    yellow: 'bg-yellow-100',
    blue: 'bg-blue-100',
    green: 'bg-green-100',
    purple: 'bg-purple-100',
    orange: 'bg-orange-100',
    slate: 'bg-slate-100'
  }

  return classes[tone] || 'bg-slate-100'
}

const getBadgeClass = notification => {
  if (isNotificationRead(notification)) {
    return 'bg-green-100 text-green-700'
  }

  const classes = {
    red: 'bg-red-100 text-[#8B1E23]',
    yellow: 'bg-yellow-100 text-yellow-700',
    blue: 'bg-blue-100 text-blue-700',
    green: 'bg-green-100 text-green-700',
    purple: 'bg-purple-100 text-purple-700',
    orange: 'bg-orange-100 text-orange-700',
    slate: 'bg-slate-100 text-slate-700'
  }

  return classes[notification.tone] || 'bg-slate-100 text-slate-700'
}

onMounted(() => {
  refreshNotifications()

  window.addEventListener('storage', refreshNotifications)
  window.addEventListener('focus', refreshNotifications)
  NOTIFICATION_EVENTS.forEach(eventName => {
    window.addEventListener(eventName, refreshNotifications)
  })

  notificationRefreshTimer = setInterval(refreshNotifications, 30000)
})

onBeforeUnmount(() => {
  window.removeEventListener('storage', refreshNotifications)
  window.removeEventListener('focus', refreshNotifications)
  NOTIFICATION_EVENTS.forEach(eventName => {
    window.removeEventListener(eventName, refreshNotifications)
  })

  if (notificationRefreshTimer) {
    clearInterval(notificationRefreshTimer)
  }
})
</script>

<template>
  <div class="space-y-6">

    <!-- HEADER -->
    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >
      <div
        class="flex flex-col xl:flex-row xl:items-center xl:justify-between gap-5"
      >

        <div>
          <p
            class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]"
          >
            Communication Center
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Notifications
          </h2>

          <p class="text-base text-slate-500 mt-1">
            View system announcements, activity alerts, and deadline reminders.
          </p>
        </div>

        <div class="flex flex-wrap gap-3">

          <button
            @click="clearFilters"
            class="px-5 py-3 rounded-xl border border-slate-300 bg-white text-slate-700 font-bold hover:bg-slate-100 transition"
          >
            Reset Filters
          </button>

          <button
            @click="markAllAsRead"
            class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition"
          >
            Mark All as Read
          </button>

          <button
            @click="showDeleteAllModal = true"
            :disabled="notifications.length === 0"
            class="px-5 py-3 rounded-xl border border-red-200 text-[#8B1E23] font-bold hover:bg-red-50 transition disabled:opacity-40 disabled:cursor-not-allowed"
          >
            Delete All
          </button>

        </div>
      </div>
    </section>

    <!-- STATS -->
    <section class="grid grid-cols-1 sm:grid-cols-3 gap-5">

      <div
        class="bg-white border border-red-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-3xl font-bold text-[#8B1E23]">
          {{ String(unreadCount).padStart(2, '0') }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Unread
        </p>
      </div>

      <div
        class="bg-white border border-yellow-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-3xl font-bold text-yellow-600">
          {{ String(deadlineCount).padStart(2, '0') }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Deadline Alerts
        </p>
      </div>

      <div
        class="bg-white border border-blue-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-3xl font-bold text-blue-600">
          {{ String(activityCount).padStart(2, '0') }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Personnel Updates
        </p>
      </div>

    </section>

    <!-- SEARCH + FILTERS -->
    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5"
    >

      <div class="flex flex-col xl:flex-row gap-4">

        <div class="flex-1">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search notifications..."
            class="w-full h-12 px-4 rounded-xl border border-slate-300 outline-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
          />
        </div>

        <select
          v-model="selectedFilter"
          class="h-12 px-4 rounded-xl border border-slate-300 bg-white"
        >
          <option>All Notifications</option>
          <option>Deadline Alerts</option>
          <option>Personnel Updates</option>
          <option>Reports & Compliance</option>
        </select>

        <select
          v-model="selectedStatus"
          class="h-12 px-4 rounded-xl border border-slate-300 bg-white"
        >
          <option>All</option>
          <option>Unread</option>
          <option>Read</option>
        </select>

        <button
          v-if="hasFilters"
          @click="clearFilters"
          class="h-12 px-5 rounded-xl bg-slate-100 text-slate-700 font-bold hover:bg-slate-200"
        >
          Clear
        </button>

      </div>

      <div class="mt-4 flex justify-between items-center">

        <p class="text-sm text-slate-500">
          Showing
          <span class="font-bold text-slate-800">
            {{ filteredNotifications.length }}
          </span>
          notifications
        </p>

        <p class="text-sm font-bold text-[#8B1E23]">
          {{ unreadCount }} unread
        </p>

      </div>
    </section>

    <!-- NOTIFICATION LIST -->
    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div class="flex items-center justify-between border-b border-slate-200 pb-5">

        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Notification Inbox
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Latest system and operational updates
          </p>
        </div>

      </div>

      <div class="mt-5 space-y-3">

        <div
          v-for="item in filteredNotifications"
          :key="item.id"
          :class="[
            'p-5 rounded-xl border transition hover:shadow-sm',
            getToneClass(item.tone),
            !item.read ? 'ring-1 ring-[#8B1E23]/10' : ''
          ]"
        >

          <div class="flex items-start gap-4">

            <div
              :class="[
                'h-12 w-12 rounded-full flex items-center justify-center shrink-0 text-lg',
                getIconClass(item.tone)
              ]"
            >
              {{ item.icon }}
            </div>

            <div class="flex-1 min-w-0">

              <div
                class="flex flex-col xl:flex-row xl:items-center xl:justify-between gap-2"
              >

                <div class="flex flex-wrap items-center gap-2">

                  <h3 class="font-bold text-slate-900">
                    {{ item.title }}
                  </h3>

                  <span
                    v-if="!item.read"
                    class="h-2 w-2 rounded-full bg-[#8B1E23]"
                  ></span>

                </div>

                <span
                  :class="[
                    'px-3 py-1 rounded-full text-xs font-bold w-fit',
                    getBadgeClass(item)
                  ]"
                >
                  {{ item.read ? 'READ' : 'UNREAD' }}
                </span>

              </div>

              <p class="text-sm text-slate-600 mt-2">
                {{ item.detail }}
              </p>

              <div
                class="flex flex-wrap items-center gap-3 mt-3"
              >

                <p class="text-xs text-slate-400">
                  {{ item.time }}
                </p>

                <span class="text-slate-300">•</span>

                <span class="text-xs font-semibold text-slate-500">
                  {{ item.type }}
                </span>

              </div>

              <!-- ACTIONS -->
              <div class="flex flex-wrap gap-2 mt-4">

                <button
                  @click="viewNotification(item)"
                  class="px-3 py-2 rounded-lg bg-white border border-slate-300 text-xs font-bold text-slate-700 hover:bg-slate-100"
                >
                  View Details
                </button>

                <button
                  @click="toggleRead(item)"
                  class="px-3 py-2 rounded-lg bg-white border border-slate-300 text-xs font-bold text-slate-700 hover:bg-slate-100"
                >
                  {{ item.read ? 'Mark Unread' : 'Mark Read' }}
                </button>

                <button
                  @click="deleteNotification(item)"
                  class="px-3 py-2 rounded-lg bg-white border border-red-200 text-xs font-bold text-[#8B1E23] hover:bg-red-50"
                >
                  Delete
                </button>

              </div>

            </div>
          </div>
        </div>

        <!-- EMPTY -->
        <div
          v-if="!filteredNotifications.length"
          class="text-center py-12"
        >
          <div class="text-4xl mb-3">
            🔔
          </div>

          <p class="font-bold text-slate-800">
            {{ notifications.length ? 'No notifications found' : 'No notifications yet' }}
          </p>

          <p class="text-sm text-slate-500 mt-1">
            {{ notifications.length ? 'Try changing your search or filters.' : "You're all caught up." }}
          </p>

          <button
            v-if="notifications.length"
            @click="clearFilters"
            class="mt-4 px-4 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-bold"
          >
            Clear Filters
          </button>
        </div>

      </div>
    </section>

    <!-- CHANNEL SUMMARY + FILTERS -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      

    </section>

    <!-- DELETE ALL MODAL -->
    <div
      v-if="showDeleteAllModal"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
      @click.self="showDeleteAllModal = false"
    >
      <div class="bg-white rounded-2xl shadow-xl w-full max-w-md p-6">
        <h3 class="text-xl font-bold text-slate-900">Delete all notifications?</h3>
        <p class="text-sm text-slate-500 mt-2">
          All notifications for your admin account will be permanently removed.
        </p>
        <div class="flex justify-end gap-3 mt-6">
          <button
            @click="showDeleteAllModal = false"
            class="px-4 py-2.5 rounded-xl border border-slate-300 text-slate-700 font-semibold"
          >
            Cancel
          </button>
          <button
            @click="deleteAll"
            class="px-4 py-2.5 rounded-xl bg-[#8B1E23] text-white font-semibold"
          >
            Delete All
          </button>
        </div>
      </div>
    </div>

    <!-- DETAILS MODAL -->
    <div
      v-if="showDetailsModal && selectedNotification"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
      @click.self="showDetailsModal = false"
    >

      <div class="bg-white rounded-2xl shadow-xl w-full max-w-xl">

        <div
          class="p-6 border-b border-slate-200 flex justify-between items-start"
        >

          <div class="flex items-start gap-3">

            <div
              :class="[
                'h-12 w-12 rounded-full flex items-center justify-center text-lg',
                getIconClass(selectedNotification.tone)
              ]"
            >
              {{ selectedNotification.icon }}
            </div>

            <div>

              <p class="text-xs font-bold uppercase text-[#8B1E23]">
                Notification Details
              </p>

              <h3 class="text-xl font-bold text-slate-900 mt-1">
                {{ selectedNotification.title }}
              </h3>

            </div>

          </div>

          <button
            @click="showDetailsModal = false"
            class="text-slate-400 hover:text-slate-700 text-xl"
          >
            ✕
          </button>

        </div>

        <div class="p-6 space-y-4">

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-500">
                Category
              </p>

              <p class="font-bold text-slate-900 mt-1">
                {{ selectedNotification.type }}
              </p>
            </div>

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-500">
                Status
              </p>

              <p class="font-bold text-slate-900 mt-1">
                {{ selectedNotification.read ? 'Read' : 'Unread' }}
              </p>
            </div>

          </div>

          <div>
            <p class="text-sm font-bold text-slate-700">
              Message
            </p>

            <p class="text-sm text-slate-600 mt-1">
              {{ selectedNotification.detail }}
            </p>
          </div>

          <div>
            <p class="text-sm font-bold text-slate-700">
              Received
            </p>

            <p class="text-sm text-slate-500 mt-1">
              {{ selectedNotification.time }}
            </p>
          </div>

        </div>

        <div
          class="p-6 border-t border-slate-200 flex justify-end"
        >

          <button
            @click="showDetailsModal = false"
            class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D]"
          >
            Close
          </button>

        </div>

      </div>
    </div>

    <!-- TOAST -->
    <Transition
      enter-active-class="transition duration-200"
      enter-from-class="opacity-0 translate-y-2"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition duration-200"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="toastMessage"
        class="fixed bottom-6 right-6 z-[60] bg-slate-900 text-white px-5 py-3 rounded-xl shadow-lg font-semibold"
      >
        {{ toastMessage }}
      </div>
    </Transition>

  </div>
</template>