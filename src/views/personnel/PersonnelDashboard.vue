<template>
  <div class="flex h-screen w-full bg-slate-100 text-slate-800 font-sans overflow-hidden">

    <!-- ========================================================= -->
    <!-- SIDEBAR -->
    <!-- ========================================================= -->
    <aside
      class="w-72 flex-shrink-0 bg-white border-r border-slate-200 flex flex-col justify-between shadow-sm z-20"
    >
      <!-- BRAND -->
      <div class="overflow-y-auto flex-1">

        <div class="h-2 bg-[#8B1E23]"></div>

        <div class="flex items-center gap-4 px-6 py-6 border-b border-slate-200">
          <div
            class="h-14 w-14 rounded-xl bg-[#8B1E23] flex items-center justify-center shadow-sm"
          >
            <svg viewBox="0 0 64 64" class="h-9 w-9" fill="none">
              <path
                d="M32 4 L58 13 V29 C58 45 47 55 32 60 C17 55 6 45 6 29 V13 Z"
                stroke="#F4C542"
                stroke-width="3"
                fill="#8B1E23"
              />
              <path
                d="M32 20c-4.5 4.5-7 8.2-7 12.2 0 4.4 3.3 7.8 7.4 7.8
                4.5 0 7.9-3.2 7.9-7.5 0-2.2-.9-3.9-2.3-5.6
                .1 1.7-.5 2.9-1.6 3.7.3-2.9-.7-6.4-4.4-10.6Z"
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

        <!-- NAVIGATION -->
        <div class="px-4 py-6 space-y-7">

          <!-- FIELD DUTY -->
          <div>
            <p class="px-3 mb-3 text-xs font-bold uppercase tracking-wider text-slate-400">
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
                  <span class="text-xl shrink-0">
                    {{ item.icon }}
                  </span>

                  <div class="min-w-0">
                    <span class="block text-base font-semibold truncate">
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

                <span
                  v-if="item.badge"
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
            <p class="px-3 mb-3 text-xs font-bold uppercase tracking-wider text-slate-400">
              Management & Records
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
                <span class="text-xl shrink-0">
                  {{ item.icon }}
                </span>

                <span class="text-base font-semibold truncate">
                  {{ item.name }}
                </span>
              </button>
            </nav>
          </div>

          <!-- TOOLS -->
          <div>
            <p class="px-3 mb-3 text-xs font-bold uppercase tracking-wider text-slate-400">
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
                <span class="text-xl shrink-0">
                  {{ item.icon }}
                </span>

                <span class="text-base font-semibold truncate">
                  {{ item.name }}
                </span>
              </button>
            </nav>
          </div>

        </div>
      </div>

      <!-- USER / LOGOUT -->
      <div class="p-4 border-t border-slate-200 bg-slate-50">

        <div
          class="flex items-center gap-3 p-3 bg-white border border-slate-200 rounded-xl"
        >
          <div
            class="h-12 w-12 rounded-full bg-[#8B1E23] flex items-center justify-center text-white font-bold text-sm shrink-0"
          >
            {{ currentUser?.rank || 'FO3' }}
          </div>

          <div class="overflow-hidden">
            <p class="text-sm font-bold text-slate-900 truncate">
              {{ currentUser?.name || 'Juan Dela Cruz' }}
            </p>

            <p class="text-xs text-slate-500 truncate">
              {{ currentUser?.role || 'Fire Officer' }}
            </p>
          </div>
        </div>

        <button
          @click="showLogoutConfirm = true"
          class="w-full mt-3 flex items-center gap-3 px-4 py-3 rounded-xl
                 text-base font-semibold text-slate-600
                 hover:bg-red-50 hover:text-[#8B1E23] transition"
        >
          <span>🚪</span>
          <span>Sign Out</span>
        </button>

      </div>
    </aside>

    <!-- ========================================================= -->
    <!-- MAIN CONTENT -->
    <!-- ========================================================= -->
    <div class="flex-1 flex flex-col min-w-0 overflow-hidden">

      <!-- HEADER -->
      <header
        class="bg-white border-b border-slate-200 px-6 lg:px-8 py-5
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

          <div
            class="hidden md:flex items-center gap-2 px-4 py-2
                   rounded-full bg-green-50 border border-green-200"
          >
            <span class="h-3 w-3 rounded-full bg-green-500"></span>

            <span class="text-sm font-semibold text-green-700">
              System Online
            </span>
          </div>

          <button
            @click="activeTab = 'Notifications'"
            class="relative h-12 w-12 flex items-center justify-center
                   rounded-xl border border-slate-200
                   hover:bg-slate-100 transition"
            title="Notifications"
          >
            🔔

            <span
              class="absolute top-2 right-2 h-3 w-3 rounded-full
                     bg-[#8B1E23] border-2 border-white"
            ></span>
          </button>

        </div>
      </header>

      <!-- ======================================================= -->
      <!-- PAGE COMPONENT -->
      <!-- ======================================================= -->
      <main class="flex-1 min-h-0 overflow-y-auto p-6 lg:p-8">

        <component
          :is="pageComponents[activeTab]"
          :current-user="currentUser"
          :ICONS="ICONS"
        />

      </main>
    </div>

    <!-- ========================================================= -->
    <!-- LOGOUT MODAL -->
    <!-- ========================================================= -->
    <div
      v-if="showLogoutConfirm"
      class="fixed inset-0 z-50 flex items-center justify-center
             bg-slate-900/40 px-4"
    >
      <div class="w-full max-w-md bg-white rounded-2xl shadow-2xl overflow-hidden">

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
              class="px-6 py-3 rounded-xl border border-slate-300
                     bg-white text-slate-700 font-semibold
                     hover:bg-slate-100 transition"
            >
              Cancel
            </button>

            <button
              @click="confirmLogout"
              class="px-6 py-3 rounded-xl bg-[#8B1E23]
                     text-white font-semibold hover:bg-[#72181D] transition"
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
import { ref, watch } from 'vue'

import Dashboard from './Dashboard.vue'
import Tasks from './Tasks.vue'
import Activities from './Activities.vue'
import Reports from './Reports.vue'
import Notifications from './Notifications.vue'
import PersonnelRoster from './PersonnelRoster.vue'
import StationDutyLog from './StationDutyLog.vue'
import EquipmentAudit from './EquipmentAudit.vue'
import Support from './Support.vue'
import Settings from './Settings.vue'


/* =========================================================
   PROPS / EMITS
   ========================================================= */

   

const props = defineProps({
  currentUser: {
    type: Object,
    required: false,
    default: null
  }
})

const emit = defineEmits(['logout'])


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


/* =========================================================
   PAGE COMPONENTS
   ========================================================= */

const pageComponents = {
  Dashboard,
  Tasks,
  Activities,
  Reports,
  Notifications,
  'Personnel Roster': PersonnelRoster,
  'Station Duty Log': StationDutyLog,
  'Equipment Audit': EquipmentAudit,
  Support,
  Settings
}


/* =========================================================
   SIDEBAR ITEMS
   ========================================================= */

const fieldItems = [
  {
    name: 'Dashboard',
    icon: '📊',
    context: 'Operations overview'
  },
  {
    name: 'Tasks',
    icon: '📋',
    context: 'Assigned activities',
    badge: '4'
  },
  {
    name: 'Activities',
    icon: '🕒',
    context: 'View station activities'
  },
  {
    name: 'Reports',
    icon: '📄',
    context: 'Submit accomplishment reports',
    badge: '3'
  },
  {
    name: 'Notifications',
    icon: '🔔',
    context: 'Deadlines & station alerts',
    badge: '3'
  }
]

const managementItems = [
  {
    name: 'Personnel Roster',
    icon: '👥',
    context: 'View station personnel'
  },
  {
    name: 'Station Duty Log',
    icon: '📝',
    context: 'Track duty & shift records'
  },
  {
    name: 'Equipment Audit',
    icon: '🧰',
    context: 'Monitor equipment status'
  }
]

const toolItems = [
  {
    name: 'Support',
    icon: '❓',
    context: 'Get system assistance'
  },
  {
    name: 'Settings',
    icon: '⚙️',
    context: 'Account & preferences'
  }
]


/* =========================================================
   SHARED ICONS
   ========================================================= */

const ICONS = {}


/* =========================================================
   LOGOUT
   ========================================================= */

const confirmLogout = () => {
  showLogoutConfirm.value = false
  emit('logout')
}
</script>