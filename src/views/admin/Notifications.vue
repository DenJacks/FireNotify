<script setup>
import { computed, ref } from 'vue'

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

const notifications = ref([
  {
    id: 1,
    icon: '🚨',
    title: 'Overdue Report Deadline',
    detail:
      'The After-Operation Fire Incident Report has passed its submission deadline.',
    time: '10 minutes ago',
    tone: 'red',
    type: 'Deadline Alerts',
    read: false
  },
  {
    id: 2,
    icon: '⚠️',
    title: 'Upcoming Report Deadline',
    detail:
      'Weekly Accomplishment Report is due tomorrow at 5:00 PM.',
    time: '30 minutes ago',
    tone: 'yellow',
    type: 'Deadline Alerts',
    read: false
  },
  {
    id: 3,
    icon: '📋',
    title: 'New Activity Assigned',
    detail:
      'Community Fire Drill has been scheduled for September 10, 2026.',
    time: '1 hour ago',
    tone: 'blue',
    type: 'Personnel Updates',
    read: false
  },
  {
    id: 4,
    icon: '✓',
    title: 'Report Approved',
    detail:
      'Weekly Accomplishment Report submitted by SFO1 Maria Santos has been approved.',
    time: '2 hours ago',
    tone: 'green',
    type: 'Reports & Compliance',
    read: true
  },
  {
    id: 5,
    icon: '📢',
    title: 'Operations Announcement',
    detail:
      'All station units are reminded to check radio signal stability before the next dispatch cycle.',
    time: '3 hours ago',
    tone: 'purple',
    type: 'System Announcements',
    read: true
  },
  {
    id: 6,
    icon: '📝',
    title: 'Report Returned',
    detail:
      'Equipment Inspection Report requires additional information before approval.',
    time: '4 hours ago',
    tone: 'orange',
    type: 'Reports & Compliance',
    read: false
  },
  {
    id: 7,
    icon: '👤',
    title: 'Personnel Assignment Updated',
    detail:
      'FO2 Mark Santos has been assigned to the September 15 emergency response drill.',
    time: '5 hours ago',
    tone: 'blue',
    type: 'Personnel Updates',
    read: true
  },
  {
    id: 8,
    icon: '🔔',
    title: 'Compliance Reminder',
    detail:
      'Approved reports must be archived within 24 hours to maintain digital records compliance.',
    time: 'Yesterday',
    tone: 'yellow',
    type: 'System Announcements',
    read: true
  }
])

const announcements = ref([
  {
    id: 1,
    title: 'Operations Update',
    detail:
      'All station units are reminded to check radio signal stability before the next dispatch cycle.',
    tone: 'green',
    date: 'Today'
  },
  {
    id: 2,
    title: 'Training Notice',
    detail:
      'Community fire drill briefing will be held tomorrow at 7:30 AM at the barangay hall.',
    tone: 'blue',
    date: 'Today'
  },
  {
    id: 3,
    title: 'Compliance Advisory',
    detail:
      'All approved reports must be archived within 24 hours to maintain digital records compliance.',
    tone: 'yellow',
    date: 'Yesterday'
  }
])

const channelSummary = computed(() => [
  {
    label: 'System Alerts',
    count: notifications.value.filter(
      item => item.type === 'System Announcements'
    ).length,
    color: 'text-[#8B1E23]'
  },
  {
    label: 'Personnel Updates',
    count: notifications.value.filter(
      item => item.type === 'Personnel Updates'
    ).length,
    color: 'text-blue-600'
  },
  {
    label: 'Reports & Compliance',
    count: notifications.value.filter(
      item => item.type === 'Reports & Compliance'
    ).length,
    color: 'text-green-600'
  },
  {
    label: 'Deadline Alerts',
    count: notifications.value.filter(
      item => item.type === 'Deadline Alerts'
    ).length,
    color: 'text-yellow-600'
  }
])

const unreadCount = computed(() =>
  notifications.value.filter(item => !item.read).length
)

const deadlineCount = computed(() =>
  notifications.value.filter(
    item => item.type === 'Deadline Alerts'
  ).length
)

const activityCount = computed(() =>
  notifications.value.filter(
    item => item.type === 'Personnel Updates'
  ).length
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
      (selectedStatus.value === 'Unread' && !item.read) ||
      (selectedStatus.value === 'Read' && item.read)

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

const markAllAsRead = () => {
  notifications.value.forEach(item => {
    item.read = true
  })

  showToast('All notifications marked as read.')
}

const toggleRead = notification => {
  notification.read = !notification.read

  showToast(
    notification.read
      ? 'Notification marked as read.'
      : 'Notification marked as unread.'
  )
}

const deleteNotification = notification => {
  const index = notifications.value.findIndex(
    item => item.id === notification.id
  )

  if (index !== -1) {
    notifications.value.splice(index, 1)
  }

  showToast('Notification deleted.')
}

const viewNotification = notification => {
  selectedNotification.value = notification

  if (!notification.read) {
    notification.read = true
  }

  showDetailsModal.value = true
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
    orange: 'border-orange-200 bg-orange-50'
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
    orange: 'bg-orange-100'
  }

  return classes[tone] || 'bg-slate-100'
}

const getBadgeClass = notification => {
  if (notification.read) {
    return 'bg-green-100 text-green-700'
  }

  const classes = {
    red: 'bg-red-100 text-[#8B1E23]',
    yellow: 'bg-yellow-100 text-yellow-700',
    blue: 'bg-blue-100 text-blue-700',
    green: 'bg-green-100 text-green-700',
    purple: 'bg-purple-100 text-purple-700',
    orange: 'bg-orange-100 text-orange-700'
  }

  return classes[notification.tone] || 'bg-slate-100 text-slate-700'
}
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
          <option>System Announcements</option>
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
            No notifications found
          </p>

          <p class="text-sm text-slate-500 mt-1">
            Try changing your search or filters.
          </p>

          <button
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

      <!-- CHANNEL SUMMARY -->
      <div
        class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
      >

        <div class="border-b border-slate-200 pb-5">

          <h2 class="text-xl font-bold text-slate-900">
            Channel Summary
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Current message volume by source
          </p>

        </div>

        <div class="mt-5 space-y-3">

          <div
            v-for="item in channelSummary"
            :key="item.label"
            class="p-4 rounded-xl border border-slate-200 bg-slate-50"
          >

            <div class="flex justify-between items-center">

              <div>
                <p class="text-sm font-bold text-slate-900">
                  {{ item.label }}
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  {{ item.count }} message(s)
                </p>
              </div>

              <span
                :class="['text-sm font-bold', item.color]"
              >
                {{ item.count }}
              </span>

            </div>

          </div>

        </div>
      </div>

      <!-- QUICK FILTERS -->
      <div
        class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
      >

        <div class="border-b border-slate-200 pb-5">

          <h2 class="text-xl font-bold text-slate-900">
            Message Filters
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Quickly sort incoming updates
          </p>

        </div>

        <div class="mt-5 space-y-3">

          <button
            @click="selectFilter('All Notifications')"
            :class="[
              'w-full text-left px-4 py-3 rounded-xl border text-sm font-semibold transition',
              selectedFilter === 'All Notifications'
                ? 'bg-[#8B1E23] text-white border-[#8B1E23]'
                : 'border-slate-200 bg-slate-50 text-slate-700 hover:bg-slate-100'
            ]"
          >
            All Notifications
          </button>

          <button
            @click="selectFilter('Deadline Alerts')"
            :class="[
              'w-full text-left px-4 py-3 rounded-xl border text-sm font-semibold transition',
              selectedFilter === 'Deadline Alerts'
                ? 'bg-[#8B1E23] text-white border-[#8B1E23]'
                : 'border-slate-200 bg-slate-50 text-slate-700 hover:bg-slate-100'
            ]"
          >
            Deadline Alerts
          </button>

          <button
            @click="selectFilter('Personnel Updates')"
            :class="[
              'w-full text-left px-4 py-3 rounded-xl border text-sm font-semibold transition',
              selectedFilter === 'Personnel Updates'
                ? 'bg-[#8B1E23] text-white border-[#8B1E23]'
                : 'border-slate-200 bg-slate-50 text-slate-700 hover:bg-slate-100'
            ]"
          >
            Personnel Updates
          </button>

          <button
            @click="selectFilter('Reports & Compliance')"
            :class="[
              'w-full text-left px-4 py-3 rounded-xl border text-sm font-semibold transition',
              selectedFilter === 'Reports & Compliance'
                ? 'bg-[#8B1E23] text-white border-[#8B1E23]'
                : 'border-slate-200 bg-slate-50 text-slate-700 hover:bg-slate-100'
            ]"
          >
            Reports & Compliance
          </button>

          <button
            @click="selectFilter('System Announcements')"
            :class="[
              'w-full text-left px-4 py-3 rounded-xl border text-sm font-semibold transition',
              selectedFilter === 'System Announcements'
                ? 'bg-[#8B1E23] text-white border-[#8B1E23]'
                : 'border-slate-200 bg-slate-50 text-slate-700 hover:bg-slate-100'
            ]"
          >
            System Announcements
          </button>

        </div>
      </div>

    </section>

    <!-- ANNOUNCEMENTS -->
    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div class="flex items-center justify-between border-b border-slate-200 pb-5">

        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Announcements
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Administrative updates for all BFP units
          </p>
        </div>

        <span
          class="px-3 py-1 rounded-full bg-slate-100 text-slate-600 text-xs font-bold"
        >
          {{ announcements.length }} Active
        </span>

      </div>

      <div class="mt-5 grid grid-cols-1 lg:grid-cols-3 gap-4">

        <div
          v-for="announcement in announcements"
          :key="announcement.id"
          :class="[
            'p-5 rounded-xl border',
            announcement.tone === 'green'
              ? 'border-emerald-200 bg-emerald-50'
              : '',
            announcement.tone === 'blue'
              ? 'border-indigo-200 bg-indigo-50'
              : '',
            announcement.tone === 'yellow'
              ? 'border-amber-200 bg-amber-50'
              : ''
          ]"
        >

          <div class="flex justify-between gap-3">

            <p class="text-sm font-bold text-slate-900">
              {{ announcement.title }}
            </p>

            <span class="text-xs text-slate-400">
              {{ announcement.date }}
            </span>

          </div>

          <p class="text-sm text-slate-600 mt-2">
            {{ announcement.detail }}
          </p>

        </div>

      </div>
    </section>

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