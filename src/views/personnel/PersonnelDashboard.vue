<template>
  <div class="personnel-portal flex h-screen w-full bg-slate-100 text-slate-800 font-sans overflow-hidden">

    <!-- ========================================================= -->
    <!-- SIDEBAR -->
    <!-- ========================================================= -->

    <aside
      class="w-72 flex-shrink-0 bg-white border-r border-slate-200
             flex flex-col justify-between shadow-sm z-20"
    >

      <!-- SIDEBAR SCROLL AREA -->
      <div class="overflow-y-auto flex-1">

        <!-- TOP ACCENT -->
        <div class="h-2 bg-[#8B1E23]"></div>

        <!-- BRAND -->
        <div class="flex items-center gap-4 px-6 py-6 border-b border-slate-200">

          <div
            class="h-14 w-14 rounded-xl bg-[#8B1E23]
                   flex items-center justify-center shadow-sm"
          >
            <svg
              viewBox="0 0 64 64"
              class="h-9 w-9"
              fill="none"
            >
              <path
                d="M32 4 L58 13 V29
                   C58 45 47 55 32 60
                   C17 55 6 45 6 29 V13 Z"
                stroke="#F4C542"
                stroke-width="3"
                fill="#8B1E23"
              />

              <path
                d="M32 20
                   c-4.5 4.5-7 8.2-7 12.2
                   0 4.4 3.3 7.8 7.4 7.8
                   4.5 0 7.9-3.2 7.9-7.5
                   0-2.2-.9-3.9-2.3-5.6
                   .1 1.7-.5 2.9-1.6 3.7
                   .3-2.9-.7-6.4-4.4-10.6Z"
                fill="#F4C542"
              />
            </svg>
          </div>

          <div>
            <p class="text-sm font-semibold text-slate-500">
              Personnel Portal
            </p>

            <h1 class="text-xl font-extrabold tracking-wide text-slate-900">
              FIRE<span class="text-[#8B1E23]">NOTIFY</span>
            </h1>

            <p class="text-xs text-slate-400 mt-0.5">
              BFP Operations System
            </p>
          </div>

        </div>


        <!-- ===================================================== -->
        <!-- NAVIGATION -->
        <!-- ===================================================== -->

        <div class="px-4 py-6 space-y-7">

          <!-- FIELD DUTY -->
          <div>

            <p
              class="px-3 mb-3 text-xs font-bold uppercase
                     tracking-wider text-slate-400"
            >
              Field Duty
            </p>

            <nav class="space-y-2">

              <button
                v-for="item in fieldItems"
                :key="item.name"
                @click="activeTab = item.name"
                :class="[
                  'w-full flex items-center justify-between px-4 py-3.5 rounded-xl text-left transition-all',
                  activeTab === item.name
                    ? 'bg-[#8B1E23] text-white shadow-md'
                    : 'text-slate-700 hover:bg-slate-100'
                ]"
              >

                <div class="flex items-center gap-4 min-w-0">

                  <!-- SVG ICON -->
                  <span
                    v-html="ICONS[item.icon]"
                    class="h-5 w-5 shrink-0 text-current"
                  ></span>

                  <div class="min-w-0">

                    <span
                      class="block text-base font-semibold truncate"
                    >
                      {{ item.name }}
                    </span>

                    <span
                      v-if="activeTab !== item.name"
                      class="block text-xs text-slate-400 truncate"
                    >
                      {{ item.context }}
                    </span>

                  </div>
                </div>


                <!-- BADGE -->
                <span
                  v-if="item.badge > 0"
                  class="ml-2 px-2 py-1 rounded-full text-xs font-bold"
                  :class="
                    activeTab === item.name
                      ? 'bg-white/20 text-white'
                      : 'bg-red-100 text-[#8B1E23]'
                  "
                >
                  {{ item.badge }}
                </span>

              </button>

            </nav>
          </div>


          <!-- MANAGEMENT -->
          <div>

            <p
              class="px-3 mb-3 text-xs font-bold uppercase
                     tracking-wider text-slate-400"
            >
            </p>

            <nav class="space-y-2">

              <button
                v-for="item in managementItems"
                :key="item.name"
                @click="activeTab = item.name"
                :class="[
                  'w-full flex items-center gap-4 px-4 py-3.5 rounded-xl text-left transition-all',
                  activeTab === item.name
                    ? 'bg-[#8B1E23] text-white shadow-md'
                    : 'text-slate-700 hover:bg-slate-100'
                ]"
              >

                <span
                  v-html="ICONS[item.icon]"
                  class="h-5 w-5 shrink-0 text-current"
                ></span>

                <span class="text-base font-semibold truncate">
                  {{ item.name }}
                </span>

              </button>

            </nav>
          </div>


          <!-- TOOLS -->
          <div>

            <p
              class="px-3 mb-3 text-xs font-bold uppercase
                     tracking-wider text-slate-400"
            >
              Personnel Tools
            </p>

            <nav class="space-y-2">

              <button
                v-for="item in toolItems"
                :key="item.name"
                @click="activeTab = item.name"
                :class="[
                  'w-full flex items-center gap-4 px-4 py-3.5 rounded-xl text-left transition-all',
                  activeTab === item.name
                    ? 'bg-[#8B1E23] text-white shadow-md'
                    : 'text-slate-700 hover:bg-slate-100'
                ]"
              >

                <span
                  v-html="ICONS[item.icon]"
                  class="h-5 w-5 shrink-0 text-current"
                ></span>

                <span class="text-base font-semibold truncate">
                  {{ item.name }}
                </span>

              </button>

            </nav>
          </div>

        </div>
      </div>


      <!-- ======================================================= -->
      <!-- USER / LOGOUT -->
      <!-- ======================================================= -->

      <div class="p-4 border-t border-slate-200 bg-slate-50">

        <div
          class="flex items-center gap-3 p-3 bg-white
                 border border-slate-200 rounded-xl"
        >

          <div
            class="h-12 w-12 rounded-full bg-[#8B1E23]
                   flex items-center justify-center
                   text-white font-bold text-sm shrink-0"
          >
            {{ currentUser?.rank || 'FO3' }}
          </div>

          <div class="overflow-hidden">

            <p class="text-sm font-bold text-slate-900 truncate">
  {{ currentUser?.name || 'User' }}
</p>
            <p class="text-xs text-slate-500 truncate">
              {{ currentUser?.role || 'Fire Officer' }}
            </p>

          </div>

        </div>


        <!-- SIGN OUT -->
        <button
          @click="showLogoutConfirm = true"
          class="w-full mt-3 flex items-center gap-3 px-4 py-3
                 rounded-xl text-base font-semibold text-slate-600
                 hover:bg-red-50 hover:text-[#8B1E23] transition"
        >

          <span
            v-html="ICONS.logout"
            class="h-5 w-5 shrink-0"
          ></span>

          <span>Log Out</span>

        </button>

      </div>

    </aside>


    <!-- ========================================================= -->
    <!-- MAIN CONTENT -->
    <!-- ========================================================= -->

    <div class="flex-1 flex flex-col min-w-0 overflow-hidden">

      <!-- HEADER -->
      <header
        class="bg-white border-b border-slate-200
               px-6 lg:px-8 py-5
               flex items-center justify-between shadow-sm"
      >

        <div>

          <p class="text-sm font-medium text-slate-500">
            FIRENOTIFY PERSONNEL
          </p>

          <h1 class="text-2xl font-bold text-slate-900">
            {{ activeTab }}
          </h1>

        </div>


        <div class="flex items-center gap-4">

          <!-- SYSTEM ONLINE -->
          <div
            class="hidden md:flex items-center gap-2
                   px-4 py-2 rounded-full
                   bg-green-50 border border-green-200"
          >

            <span
              class="h-3 w-3 rounded-full bg-green-500"
            ></span>

            <span class="text-sm font-semibold text-green-700">
              System Online
            </span>

          </div>


          <!-- NOTIFICATION BUTTON -->
          <button
            @click="activeTab = 'Notifications'"
            class="relative h-12 w-12 flex items-center justify-center
                   rounded-xl border border-slate-200
                   hover:bg-slate-100 transition"
            title="Notifications"
          >

            <span
              v-html="ICONS.notifications"
              class="h-5 w-5 text-slate-600"
            ></span>

            <span
              v-if="sidebarCounts.notifications > 0"
              class="absolute top-1 right-1 min-w-5 h-5 px-1
                     rounded-full bg-[#8B1E23] text-white text-[10px]
                     font-bold flex items-center justify-center
                     border-2 border-white"
            >
              {{ sidebarCounts.notifications }}
            </span>

          </button>

        </div>

      </header>


      <!-- ======================================================= -->
      <!-- PAGE COMPONENT -->
      <!-- ======================================================= -->

      <main
        class="flex-1 min-h-0 overflow-y-auto p-6 lg:p-8"
      >

       <component
  :is="pageComponents[activeTab]"
  :current-user="currentUser"
  :registered-users="registeredUsers"
  :ICONS="ICONS"
  @update-user="handleUserUpdate"
  @open-support="activeTab = 'Support'"
/>

      </main>

    </div>


    <!-- ========================================================= -->
    <!-- LOGOUT MODAL -->
    <!-- ========================================================= -->

    <div
      v-if="showLogoutConfirm"
      class="fixed inset-0 z-50 flex items-center
             justify-center bg-slate-900/40 px-4"
    >

      <div
        class="w-full max-w-md bg-white
               rounded-2xl shadow-2xl overflow-hidden"
      >

        <div class="h-2 bg-[#8B1E23]"></div>

        <div class="p-7">

          <h3 class="text-xl font-bold text-slate-900">
            Confirm Sign Out
          </h3>

          <p class="text-base text-slate-500 mt-2">
            Are you sure you want to sign out?
          </p>

          <div class="flex justify-end gap-3 mt-7">

            <button
              @click="showLogoutConfirm = false"
              class="px-6 py-3 rounded-xl
                     border border-slate-300
                     bg-white text-slate-700
                     font-semibold hover:bg-slate-100 transition"
            >
              Cancel
            </button>

            <button
              @click="confirmLogout"
              class="px-6 py-3 rounded-xl
                     bg-[#8B1E23] text-white
                     font-semibold hover:bg-[#72181D] transition"
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
import Tasks from './Tasks.vue'
import Activities from './Activities.vue'
import Reports from './Reports.vue'
import Notifications from './Notifications.vue'
import Support from './Support.vue'
import Settings from './Settings.vue'
import {
  applyPersonnelSettings,
  getPersonnelSettings,
  initializePersonnelSettings,
  SETTINGS_UPDATED_EVENT
} from '../../utils/personnelSettings.js'
import {
  getUnreadPersonnelCount,
  mergeDerivedPersonnelNotifications
} from '../../utils/notificationService.js'


/* =========================================================
   PROPS / EMITS
   ========================================================= */

   
const props = defineProps({
  currentUser: {
    type: Object,
    required: false,
    default: null
  },

  registeredUsers: {
    type: Array,
    default: () => []
  }
})

const emit = defineEmits(['logout', 'update-user'])

/* =========================================================
   SHARED SHELL STATE
   ========================================================= */

const ACTIVE_TAB_KEY = 'fireNotifyPersonnelActiveTab'

const activeTab = ref(
  localStorage.getItem(ACTIVE_TAB_KEY) || 'Dashboard'
)

watch(activeTab, (newTab) => {
  localStorage.setItem(ACTIVE_TAB_KEY, newTab)
})

const showLogoutConfirm = ref(false)

const STORAGE_KEYS = {
  tasks: 'firenotify_tasks',
  reports: 'firenotify_reports'
}

const UPDATE_EVENTS = [
  'fireNotifyUsersUpdated',
  'fireNotifySupportTicketsUpdated',
  'fireNotifyRegisteredUsersUpdated',
  'fireNotifyActivitiesUpdated',
  'fireNotifyTasksUpdated',
  'fireNotifyReportsUpdated',
  'fireNotifyNotificationsUpdated'
]

const sidebarCounts = reactive({
  tasks: 0,
  reports: 0,
  notifications: 0
})

let sidebarRefreshTimer = null
const applySettingsEvent = event => {
  applyPersonnelSettings(event.detail || getPersonnelSettings())
}

const readArray = key => {
  try {
    const value = JSON.parse(localStorage.getItem(key) || '[]')
    return Array.isArray(value) ? value : []
  } catch {
    return []
  }
}

const normalize = value => String(value || '').trim().toLowerCase()

const getCurrentUser = () => {
  if (props.currentUser) return props.currentUser

  try {
    return JSON.parse(localStorage.getItem('fireNotifyCurrentUser') || 'null') || null
  } catch {
    return null
  }
}

const identityValues = user => [
  user?.id,
  user?.userId,
  user?.identifier,
  user?.email,
  user?.username,
  user?.name,
  `${user?.firstName || ''} ${user?.lastName || ''}`.trim()
].map(normalize).filter(Boolean)

const recordBelongsToCurrentUser = record => {
  const identities = identityValues(getCurrentUser())
  if (!identities.length) return false

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

  for (const person of record?.assignedPersonnel || []) {
    values.push(person?.id, person?.userId, person?.username, person?.identifier, person?.email, person?.name)
  }

  return values.map(normalize).some(value => value && identities.includes(value))
}

const isPending = status => [
  'pending',
  'pending submission',
  'not submitted',
  'scheduled',
  'in progress',
  'assigned',
  'for review',
  'returned'
].includes(normalize(status))

const isCompleted = status => [
  'completed',
  'complete',
  'done',
  'finished',
  'approved',
  'reviewed',
  'submitted',
  'closed',
  'resolved'
].includes(normalize(status))

const refreshSidebarCounts = () => {
  const currentUser = getCurrentUser()
  mergeDerivedPersonnelNotifications(currentUser)
  const tasks = readArray(STORAGE_KEYS.tasks)
  const reports = readArray(STORAGE_KEYS.reports)

  sidebarCounts.tasks = tasks.filter(task => {
    return recordBelongsToCurrentUser(task) && isPending(task?.status)
  }).length

  sidebarCounts.reports = reports.filter(report => {
    return recordBelongsToCurrentUser(report) && !isCompleted(report?.status || report?.submissionStatus)
  }).length

  sidebarCounts.notifications = getUnreadPersonnelCount(currentUser)
}


/* =========================================================
   PAGE COMPONENTS
   ========================================================= */

const pageComponents = {
  Dashboard,
  Tasks,
  Activities,
  Reports,
  Notifications,
  
  Support,
  Settings
}


/* =========================================================
   SIDEBAR ITEMS
   ========================================================= */

const fieldItems = computed(() => [
  {
    name: 'Dashboard',
    icon: 'dashboard',
    context: 'Operations overview'
  },
  {
    name: 'Tasks',
    icon: 'tasks',
    context: 'Assigned activities',
    badge: sidebarCounts.tasks
  },
  {
    name: 'Activities',
    icon: 'activities',
    context: 'View station activities'
  },
  {
    name: 'Reports',
    icon: 'reports',
    context: 'Submit accomplishment reports',
    badge: sidebarCounts.reports
  },
  {
    name: 'Notifications',
    icon: 'notifications',
    context: 'Deadlines & station alerts',
    badge: sidebarCounts.notifications
  }
])


const managementItems = [
 
  
 
]


const toolItems = [
  {
    name: 'Support',
    icon: 'support',
    context: 'Get system assistance'
  },
  {
    name: 'Settings',
    icon: 'settings',
    context: 'Account & preferences'
  }
]

onMounted(() => {
  initializePersonnelSettings()
  refreshSidebarCounts()

  window.addEventListener('storage', refreshSidebarCounts)
  window.addEventListener('focus', refreshSidebarCounts)
  window.addEventListener(SETTINGS_UPDATED_EVENT, applySettingsEvent)
  UPDATE_EVENTS.forEach(eventName => {
    window.addEventListener(eventName, refreshSidebarCounts)
  })

  sidebarRefreshTimer = setInterval(refreshSidebarCounts, 800)
})

onBeforeUnmount(() => {
  window.removeEventListener('storage', refreshSidebarCounts)
  window.removeEventListener('focus', refreshSidebarCounts)
  window.removeEventListener(SETTINGS_UPDATED_EVENT, applySettingsEvent)
  UPDATE_EVENTS.forEach(eventName => {
    window.removeEventListener(eventName, refreshSidebarCounts)
  })

  if (sidebarRefreshTimer) {
    clearInterval(sidebarRefreshTimer)
  }
})


/* =========================================================
   SHARED SVG ICONS
   ========================================================= */

const ICONS = {

  /* DASHBOARD */
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


  /* TASKS */
  tasks: `
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


  /* ACTIVITIES */
  activities: `
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


  /* REPORTS */
  reports: `
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


  /* NOTIFICATIONS */
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


 


  /* DUTY LOG */
  duty: `
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
      <path d="M8 13h8M8 17h5"/>
    </svg>
  `,


  /* EQUIPMENT */
  equipment: `
    <svg
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path
        d="M14.7 6.3a4 4 0 0 0-5.4 5.4
           L3 18v3h3l6.3-6.3
           a4 4 0 0 0 5.4-5.4
           l-2.2 2.2-3-3z"
      />
      <path d="M19 3l2 2"/>
    </svg>
  `,


  /* SUPPORT */
  support: `
    <svg
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <circle cx="12" cy="12" r="9"/>
      <path
        d="M9.5 9
           a2.5 2.5 0 1 1 4.2 1.8
           c-1 .8-1.7 1.2-1.7 2.7"
      />
      <path d="M12 17h.01"/>
    </svg>
  `,


  /* SETTINGS */
  settings: `
    <svg
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <circle cx="12" cy="12" r="3"/>
      <path
        d="M19.4 15
           a1.7 1.7 0 0 0 .3 1.9
           l.1.1-1.5 1.5-.1-.1
           a1.7 1.7 0 0 0-1.9-.3
           a1.7 1.7 0 0 0-1 1.5V20h-2v-.2
           a1.7 1.7 0 0 0-1-1.5
           a1.7 1.7 0 0 0-1.9.3
           l-.1.1-1.5-1.5.1-.1
           a1.7 1.7 0 0 0 .3-1.9
           a1.7 1.7 0 0 0-1.5-1H6v-2h.2
           a1.7 1.7 0 0 0 1.5-1
           a1.7 1.7 0 0 0-.3-1.9
           l-.1-.1 1.5-1.5.1.1
           a1.7 1.7 0 0 0 1.9.3
           a1.7 1.7 0 0 0 1-1.5V6h2v.2
           a1.7 1.7 0 0 0 1 1.5
           a1.7 1.7 0 0 0 1.9-.3
           l.1-.1 1.5 1.5-.1.1
           a1.7 1.7 0 0 0-.3 1.9
           a1.7 1.7 0 0 0 1.5 1h.2v2h-.2
           a1.7 1.7 0 0 0-1.5 1z"
      />
    </svg>
  `,


  /* LOGOUT */
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


/* =========================================================
   LOGOUT
   ========================================================= */

const confirmLogout = () => {
  showLogoutConfirm.value = false
  emit('logout')
}




const handleUserUpdate = (updatedUser) => {
  emit('update-user', updatedUser)
}


</script>