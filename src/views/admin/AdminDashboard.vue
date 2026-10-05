<template>
  <div
    class="flex h-screen w-full bg-slate-100 text-slate-800 font-sans overflow-hidden"
  >
    <!-- ===================================================== -->
    <!-- SIDEBAR -->
    <!-- ===================================================== -->

    <aside
      class="w-72 flex-shrink-0 bg-white border-r border-slate-200 flex flex-col justify-between shadow-sm z-20"
    >
      <!-- TOP RED LINE -->
      <div class="h-2 bg-[#8B1E23]"></div>

      <!-- SIDEBAR SCROLL AREA -->
      <div class="overflow-y-auto flex-1">

        <!-- ================================================= -->
        <!-- BRAND -->
        <!-- ================================================= -->

        <div
          class="flex items-center gap-4 px-6 py-6 border-b border-slate-200"
        >
          <div
            class="h-14 w-14 rounded-xl bg-[#8B1E23] flex items-center justify-center shadow-sm"
          >
            <svg
              viewBox="0 0 64 64"
              class="h-9 w-9"
              fill="none"
            >
              <path
                d="M32 4 L58 13 V29 C58 45 47 55 32 60 C17 55 6 45 6 29 V13 Z"
                stroke="#F4C542"
                stroke-width="3"
                fill="#8B1E23"
              />

              <path
                d="M32 20c-4.5 4.5-7 8.2-7 12.2 0 4.4 3.3 7.8 7.4 7.8 4.5 0 7.9-3.2 7.9-7.5 0-2.2-.9-3.9-2.3-5.6.1 1.7-.5 2.9-1.6 3.7.3-2.9-.7-6.4-4.4-10.6Z"
                fill="#F4C542"
              />
            </svg>
          </div>

          <div>
            <p class="text-sm font-semibold text-slate-500">
              Admin Portal
            </p>

            <h1
              class="text-xl font-extrabold tracking-wide text-slate-900"
            >
              FIRE<span class="text-[#8B1E23]">NOTIFY</span>
            </h1>

            <p class="text-xs text-slate-400 mt-0.5">
              BFP Operations System
            </p>
          </div>
        </div>


        <!-- ================================================= -->
        <!-- NAVIGATION -->
        <!-- ================================================= -->

        <div class="px-4 py-6 space-y-7">

          <!-- ================================================= -->
          <!-- MAIN NAVIGATION -->
          <!-- ================================================= -->

          <div>
            <p
              class="px-3 mb-3 text-xs font-bold uppercase tracking-wider text-slate-400"
            >
              Navigation
            </p>

            <nav class="space-y-2">

              <button
                v-for="item in menuBarItems"
                :key="item.name"
                @click="activeMenu = item.name"
                :class="[
                  'w-full flex items-center justify-between px-4 py-3.5 rounded-xl text-left transition-all duration-150',
                  activeMenu === item.name
                    ? 'bg-[#8B1E23] text-white shadow-md'
                    : 'text-slate-700 hover:bg-slate-100'
                ]"
              >

                <div class="flex items-center gap-4 min-w-0">

                  <!-- MODERN OUTLINE ICON -->
                  <span
                    v-html="ICONS[item.icon]"
                    class="w-6 h-6 shrink-0 flex items-center justify-center"
                    :class="
                      activeMenu === item.name
                        ? 'text-[#F4C542]'
                        : 'text-slate-500'
                    "
                  ></span>

                  <div class="min-w-0">
                    <span class="block text-base font-semibold truncate">
                      {{ item.name }}
                    </span>

                    <span
                      v-if="activeMenu !== item.name && item.context"
                      class="block text-xs text-slate-400 truncate"
                    >
                      {{ item.context }}
                    </span>
                  </div>

                </div>


                <!-- BADGE -->
                <span
                  v-if="item.badge > 0"
                  class="ml-2 px-2.5 py-1 rounded-full text-xs font-bold"
                  :class="
                    activeMenu === item.name
                      ? 'bg-white/20 text-white'
                      : 'bg-red-100 text-[#8B1E23]'
                  "
                >
                  {{ item.badge }}
                </span>

              </button>

            </nav>
          </div>


          <!-- ================================================= -->
          <!-- SYSTEM MANAGEMENT -->
          <!-- ================================================= -->

          <div>

            <p
              class="px-3 mb-3 text-xs font-bold uppercase tracking-wider text-slate-400"
            >
              System Management
            </p>

            <nav class="space-y-2">

              <button
                v-for="item in capstoneItems"
                :key="item.name"
                @click="activeMenu = item.name"
                :class="[
                  'w-full flex items-center gap-4 px-4 py-3.5 rounded-xl text-left transition-all duration-150',
                  activeMenu === item.name
                    ? 'bg-[#8B1E23] text-white shadow-md'
                    : 'text-slate-700 hover:bg-slate-100'
                ]"
              >

                <!-- MODERN OUTLINE ICON -->
                <span
                  v-html="ICONS[item.icon]"
                  class="w-6 h-6 shrink-0 flex items-center justify-center"
                  :class="
                    activeMenu === item.name
                      ? 'text-[#F4C542]'
                      : 'text-slate-500'
                  "
                ></span>

                <div class="min-w-0">
                  <span class="block text-base font-semibold truncate">
                    {{ item.name }}
                  </span>

                  <span
                    v-if="activeMenu !== item.name && item.context"
                    class="block text-xs text-slate-400 truncate"
                  >
                    {{ item.context }}
                  </span>
                </div>

              </button>

            </nav>

          </div>

        </div>
      </div>


      <!-- ===================================================== -->
      <!-- USER PROFILE + LOGOUT -->
      <!-- ===================================================== -->

      <div class="p-4 border-t border-slate-200 bg-slate-50">

        <div
          class="flex items-center gap-3 p-3 bg-white border border-slate-200 rounded-xl"
        >

          <div
            class="h-12 w-12 rounded-full bg-[#8B1E23] flex items-center justify-center text-white font-bold text-sm shrink-0"
          >
            {{ currentUser?.rank || 'ADMIN' }}
          </div>

          <div class="overflow-hidden">

            <p
              class="text-sm font-bold text-slate-900 truncate"
            >
              {{ currentUser?.name || 'User' }}
            </p>

            <p
              class="text-xs text-slate-500 truncate"
            >
              {{ currentUser?.role || 'System Administrator' }}
            </p>

          </div>

        </div>


        <!-- ================================================= -->
        <!-- LOGOUT -->
        <!-- ================================================= -->

        <button
          @click="showLogoutConfirm = true"
          class="w-full mt-3 flex items-center gap-3 px-4 py-3 rounded-xl text-base font-semibold text-slate-600 hover:bg-red-50 hover:text-[#8B1E23] transition"
        >

          <!-- MODERN LOGOUT ICON -->
          <span
            v-html="ICONS.logout"
            class="w-5 h-5 shrink-0 flex items-center justify-center"
          ></span>

          <span>
            Sign Out
          </span>

        </button>

      </div>
    </aside>


    <!-- ===================================================== -->
    <!-- MAIN CONTENT -->
    <!-- ===================================================== -->

    <div class="flex-1 flex flex-col overflow-y-auto">

      <!-- ================================================= -->
      <!-- HEADER -->
      <!-- ================================================= -->

      <header
        class="bg-white border-b border-slate-200 px-8 py-5 flex items-center justify-between sticky top-0 z-30 shadow-sm"
      >

        <div class="flex items-center gap-4">

          <!-- ACTIVE ICON -->
          <div
            class="h-11 w-11 rounded-xl bg-red-50 flex items-center justify-center"
          >

            <span
              v-html="ICONS[getActiveIcon()]"
              class="w-6 h-6 flex items-center justify-center text-[#8B1E23]"
            ></span>

          </div>


          <div>

            <p class="text-sm font-medium text-slate-500">
              FIRENOTIFY ADMIN
            </p>

            <h1 class="text-2xl font-bold text-slate-900">
              {{ activeMenu }}
            </h1>

          </div>

        </div>


        <!-- ================================================= -->
        <!-- HEADER RIGHT -->
        <!-- ================================================= -->

        <div class="flex items-center gap-4">

          <!-- SYSTEM ONLINE -->
          <div
            class="hidden md:flex items-center gap-2 px-4 py-2 rounded-full bg-green-50 border border-green-200"
          >

            <span class="h-3 w-3 rounded-full bg-green-500"></span>

            <span class="text-sm font-semibold text-green-700">
              System Online
            </span>

          </div>


          <!-- ================================================= -->
          <!-- NOTIFICATION BUTTON -->
          <!-- ================================================= -->

          <button
            @click="activeMenu = 'Notifications'"
            class="relative h-12 w-12 flex items-center justify-center rounded-xl border border-slate-200 hover:bg-slate-100 transition"
            title="Notifications"
          >

            <span
              v-html="ICONS.notifications"
              class="w-6 h-6 flex items-center justify-center text-slate-600"
            ></span>

            <span
              v-if="sidebarCounts.notifications > 0"
              class="absolute top-1 right-1 min-w-5 h-5 px-1 rounded-full bg-[#8B1E23] text-white text-[10px] font-bold flex items-center justify-center border-2 border-white"
            >
              {{ sidebarCounts.notifications }}
            </span>

          </button>

        </div>

      </header>


      <!-- ================================================= -->
      <!-- PAGE CONTENT -->
      <!-- ================================================= -->

      <main class="p-6 lg:p-8 space-y-7">

        <!-- DASHBOARD -->
        <Dashboard
          v-if="activeMenu === 'Dashboard'"
          :current-user="currentUser"
        />


        <!-- PERSONNEL ACTIVITY MANAGEMENT -->
        <PersonnelActivityManagement
          v-else-if="activeMenu === 'Personnel Activity Mgmt.'"
          :current-user="currentUser"
          :registered-users="registeredUsers"
        />


        <!-- PERSONNEL TASK MANAGEMENT -->
        <PersonnelTaskManagement
          v-else-if="activeMenu === 'Personnel Task Mgmt.'"
          :current-user="currentUser"
          :registered-users="registeredUsers"
          @delete-user="handleDeleteUser"
        />


        <!-- ACCOUNT APPROVALS -->
        <AccountApprovals
          v-else-if="activeMenu === 'Account Approvals'"
          :current-user="currentUser"
          @approval-updated="refreshNotificationBadge"
        />


        <!-- REPORT MANAGEMENT -->
        <ReportManagement
          v-else-if="activeMenu === 'Report Mgmt.'"
          :current-user="currentUser"
          :registered-users="registeredUsers"
          :ICONS="ICONS"
        />


        <!-- NOTIFICATIONS -->
        <Notifications
          v-else-if="activeMenu === 'Notifications'"
          :current-user="currentUser"
        />


        <!-- AUDIT & ESCALATIONS -->
        <AuditEscalations
          v-else-if="activeMenu === 'Audit & Escalations'"
          :current-user="currentUser"
          :registered-users="registeredUsers"
        />

      </main>

    </div>


    <!-- ===================================================== -->
    <!-- LOGOUT MODAL -->
    <!-- ===================================================== -->

    <div
      v-if="showLogoutConfirm"
      class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/40 px-4"
    >

      <div
        class="w-full max-w-md bg-white rounded-2xl shadow-2xl overflow-hidden"
      >

        <div class="h-2 bg-[#8B1E23]"></div>

        <div class="p-7">

          <div class="flex items-start gap-4">

            <div
              class="h-14 w-14 rounded-full bg-red-50 flex items-center justify-center shrink-0"
            >
              <span class="text-xl">
                🚨
              </span>
            </div>

            <div>

              <h3 class="text-xl font-bold text-slate-900">
                Confirm Sign Out
              </h3>

              <p class="text-base text-slate-500 mt-1">
                Are you sure you want to sign out of the Admin Portal?
              </p>

            </div>

          </div>


          <div
            class="mt-5 p-4 rounded-xl bg-yellow-50 border border-yellow-200"
          >

            <p
              class="text-sm text-slate-600 leading-relaxed"
            >
              Make sure all important administrative changes and reports
              have been saved before signing out.
            </p>

          </div>


          <div
            class="flex flex-col-reverse sm:flex-row justify-end gap-3 mt-7"
          >

            <button
              @click="showLogoutConfirm = false"
              class="w-full sm:w-auto px-6 py-3 rounded-xl border border-slate-300 bg-white text-slate-700 text-base font-semibold hover:bg-slate-100 transition"
            >
              Cancel
            </button>


            <button
              @click="confirmLogout"
              class="w-full sm:w-auto px-6 py-3 rounded-xl bg-[#8B1E23] text-white text-base font-semibold hover:bg-[#72181D] transition"
            >
              Sign Out
            </button>

          </div>

        </div>

      </div>

    </div>

  </div>
</template>


<script setup>

import { computed, onBeforeUnmount, onMounted, reactive, ref, watch } from 'vue'

import Dashboard from './Dashboard.vue'
import PersonnelActivityManagement from './PersonnelActivityManagement.vue'
import PersonnelTaskManagement from './PersonnelTaskManagement.vue'
import ReportManagement from './ReportManagement.vue'
import Notifications from './Notifications.vue'
import AuditEscalations from './AuditEscalations.vue'
import AccountApprovals from './AccountApprovals.vue'
import { getNotifications } from '../../utils/notificationApi.js'
import { getReportSubmissions } from '../../utils/reportApi.js'


// =====================================================
// PROPS
// =====================================================

const props = defineProps({

  currentUser: {
    type: Object,
    default: null
  },

  registeredUsers: {
    type: Array,
    default: () => []
  }

})


// =====================================================
// EMITS
// =====================================================

const emit = defineEmits([
  'logout',
  'delete-user'
])


// =====================================================
// ACTIVE MENU
// =====================================================

const ACTIVE_MENU_KEY = 'fireNotifyAdminActiveMenu'

const activeMenu = ref(
  localStorage.getItem(ACTIVE_MENU_KEY) || 'Dashboard'
)

const REFRESH_EVENTS = [
  'fireNotifyNotificationsUpdated',
  'fireNotifySupportTicketsUpdated',
  'fireNotifyUsersUpdated',
  'fireNotifyRegisteredUsersUpdated',
  'fireNotifyActivitiesUpdated',
  'fireNotifyTasksUpdated',
  'fireNotifyReportsUpdated'
]

const sidebarCounts = reactive({
  activities: 0,
  tasks: 0,
  reports: 0,
  notifications: 0,
  pendingApprovals: 0
})

const readArray = key => {
  try {
    const value = JSON.parse(localStorage.getItem(key) || '[]')
    return Array.isArray(value) ? value : []
  } catch {
    return []
  }
}

const statusKey = status => String(status || '').trim().toLowerCase()

const isPendingStatus = status => [
  'pending',
  'pending submission',
  'not submitted',
  'scheduled',
  'ongoing',
  'in_progress',
  'in progress',
  'assigned',
  'for review',
  'returned',
  'for_verification',
  'delayed',
  'overdue'
].includes(statusKey(status))

const refreshSidebarCounts = async () => {
  try {
    const [activityResponse, taskResponse, reportSubmissions, notifications, usersResponse] = await Promise.all([
      fetch('http://127.0.0.1:8000/api/activities/'),
      fetch('http://127.0.0.1:8000/api/tasks/'),
      getReportSubmissions(),
      getNotifications(props.currentUser),
      fetch('http://127.0.0.1:8000/api/users/')
    ])
    if (!activityResponse.ok || !taskResponse.ok || !usersResponse.ok) throw new Error('Dashboard count request failed.')
    const [activities, tasks, users] = await Promise.all([
      activityResponse.json(),
      taskResponse.json(),
      usersResponse.json()
    ])
    sidebarCounts.activities = activities.filter(item => isPendingStatus(item?.status)).length
    sidebarCounts.tasks = tasks.filter(item => isPendingStatus(item?.status)).length
    sidebarCounts.reports = reportSubmissions.filter(item => ['SUBMITTED', 'FOR_REVIEW'].includes(item.status)).length
    sidebarCounts.notifications = notifications.filter(item => !item.is_read).length
    sidebarCounts.pendingApprovals = Array.isArray(users)
      ? users.filter(user => String(user.role || '').toUpperCase() === 'PERSONNEL' && String(user.status || '').toUpperCase() === 'PENDING').length
      : 0
  } catch (error) {
    console.error('FireNotify: unable to refresh admin sidebar counts', error)
  }
}

// Keep the badge source centralized at the shell level so navigation does not reset it.
const refreshNotificationBadge = () => {
  refreshSidebarCounts()
}

// Save active menu
watch(activeMenu, (newMenu) => {
  localStorage.setItem(ACTIVE_MENU_KEY, newMenu)
})


// =====================================================
// LOGOUT STATE
// =====================================================

const showLogoutConfirm = ref(false)


// =====================================================
// MODERN SVG ICONS
// SAME STYLE AS PERSONNEL SIDEBAR
// =====================================================

const ICONS = {

  // ===================================================
  // DASHBOARD
  // ===================================================

  dashboard: `
    <svg
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <rect x="3" y="3" width="7" height="7" rx="1"/>
      <rect x="14" y="3" width="7" height="7" rx="1"/>
      <rect x="3" y="14" width="7" height="7" rx="1"/>
      <rect x="14" y="14" width="7" height="7" rx="1"/>
    </svg>
  `,


  // ===================================================
  // ACTIVITY
  // ===================================================

  activity: `
    <svg
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <circle cx="12" cy="12" r="9"/>
      <path d="M12 7v5l3 2"/>
    </svg>
  `,


  // ===================================================
  // TASKS / PERSONNEL
  // SAME ICON STYLE AS PERSONNEL
  // ===================================================

  personnel: `
    <svg
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <rect x="3" y="4" width="18" height="17" rx="2"/>
      <path d="M8 2v4M16 2v4M3 9h18"/>
      <path d="M8 13h2M13 13h3M8 17h6"/>
    </svg>
  `,


  // ===================================================
  // REPORTS
  // ===================================================

  report: `
    <svg
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path d="M6 3h9l5 5v13H6z"/>
      <path d="M14 3v6h6"/>
      <path d="M9 13h6M9 17h6"/>
    </svg>
  `,


  // ===================================================
  // NOTIFICATIONS
  // ===================================================

  notifications: `
    <svg
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path
        d="M18 8a6 6 0 0 0-12 0
           c0 7-3 7-3 9h18
           c0-2-3-2-3-9"
      />
      <path d="M10 21h4"/>
    </svg>
  `,


  // ===================================================
  // AUDIT & ESCALATIONS
  // ===================================================

  shield: `
    <svg
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path
        d="M12 3
           L20 6
           V11
           C20 16.5 16.5 20 12 21
           C7.5 20 4 16.5 4 11
           V6
           Z"
      />
      <path d="M9 12l2 2 4-4"/>
    </svg>
  `,


  // ===================================================
  // LOGOUT
  // ===================================================

  logout: `
    <svg
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/>
      <path d="m16 17 5-5-5-5"/>
      <path d="M21 12H9"/>
    </svg>
  `

}


// =====================================================
// MAIN NAVIGATION
// =====================================================

const menuBarItems = computed(() => [

  {
    name: 'Dashboard',
    icon: 'dashboard',
    context: 'Admin overview'
  },

  {
    name: 'Account Approvals',
    icon: 'personnel',
    context: 'Review personnel accounts',
    badge: sidebarCounts.pendingApprovals
  },

  {
    name: 'Personnel Activity Mgmt.',
    icon: 'activity',
    context: 'Manage station activities',
    badge: sidebarCounts.activities
  },

  {
    name: 'Personnel Task Mgmt.',
    icon: 'personnel',
    context: 'Assign and track tasks',
    badge: sidebarCounts.tasks
  },

  {
    name: 'Report Mgmt.',
    icon: 'report',
    context: 'Review submitted reports',
    badge: sidebarCounts.reports
  },

  {
    name: 'Notifications',
    icon: 'notifications',
    context: 'System alerts and updates',
    badge: sidebarCounts.notifications
  },

])


// =====================================================
// SYSTEM MANAGEMENT
// =====================================================

const capstoneItems = [

  {
    name: 'Audit & Escalations',
    icon: 'shield',
    context: 'Review system activity'
  }

]


// =====================================================
// LOGOUT FUNCTION
// =====================================================

const confirmLogout = () => {

  showLogoutConfirm.value = false

  // Reset Admin page to Dashboard
  localStorage.removeItem(ACTIVE_MENU_KEY)

  emit('logout')

}


// =====================================================
// ACTIVE ICON
// =====================================================

onMounted(() => {
  refreshNotificationBadge()

  window.addEventListener('storage', refreshNotificationBadge)
  window.addEventListener('focus', refreshNotificationBadge)
  REFRESH_EVENTS.forEach(eventName => {
    window.addEventListener(eventName, refreshNotificationBadge)
  })

})

onBeforeUnmount(() => {
  window.removeEventListener('storage', refreshNotificationBadge)
  window.removeEventListener('focus', refreshNotificationBadge)
  REFRESH_EVENTS.forEach(eventName => {
    window.removeEventListener(eventName, refreshNotificationBadge)
  })
})

const getActiveIcon = () => {

  const allItems = [
    ...menuBarItems.value,
    ...capstoneItems
  ]

  const found = allItems.find(
    item => item.name === activeMenu.value
  )

  return found
    ? found.icon
    : 'dashboard'

}


// =====================================================
// DELETE USER
// =====================================================

const handleDeleteUser = (userId) => {

  if (!userId) {
    return
  }

  emit('delete-user', userId)

}

</script>