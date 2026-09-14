<template>
  <div class="flex h-screen w-full bg-slate-100 text-slate-800 font-sans overflow-hidden">
    <aside
      class="w-72 flex-shrink-0 bg-white border-r border-slate-200 flex flex-col justify-between shadow-sm z-20"
    >
      <div class="h-2 bg-[#8B1E23]"></div>

      <div class="overflow-y-auto flex-1">
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
                d="M32 20c-4.5 4.5-7 8.2-7 12.2 0 4.4 3.3 7.8 7.4 7.8 4.5 0 7.9-3.2 7.9-7.5 0-2.2-.9-3.9-2.3-5.6.1 1.7-.5 2.9-1.6 3.7.3-2.9-.7-6.4-4.4-10.6Z"
                fill="#F4C542"
              />
            </svg>
          </div>

          <div>
            <p class="text-sm font-semibold text-slate-500">Admin Portal</p>
            <h1 class="text-xl font-extrabold tracking-wide text-slate-900">
              FIRE<span class="text-[#8B1E23]">NOTIFY</span>
            </h1>
            <p class="text-xs text-slate-400 mt-0.5">BFP Operations System</p>
          </div>
        </div>

        <div class="px-4 py-6 space-y-7">
          <div>
            <p class="px-3 mb-3 text-xs font-bold uppercase tracking-wider text-slate-400">
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
                  <svg
                    class="w-6 h-6 fill-current shrink-0"
                    viewBox="0 0 24 24"
                    :class="activeMenu === item.name ? 'text-[#F4C542]' : 'text-slate-500'"
                    v-html="getSvgPath(item.icon)"
                  ></svg>

                  <span class="text-base font-semibold truncate">
                    {{ item.name }}
                  </span>
                </div>

                <span
                  v-if="item.badge"
                  class="ml-2 px-2.5 py-1 rounded-full text-xs font-bold"
                  :class="activeMenu === item.name ? 'bg-white/20 text-white' : 'bg-red-100 text-[#8B1E23]'"
                >
                  {{ item.badge }}
                </span>
              </button>
            </nav>
          </div>

          <div>
            <p class="px-3 mb-3 text-xs font-bold uppercase tracking-wider text-slate-400">
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
                <svg
                  class="w-6 h-6 fill-current shrink-0"
                  viewBox="0 0 24 24"
                  :class="activeMenu === item.name ? 'text-[#F4C542]' : 'text-slate-500'"
                  v-html="getSvgPath(item.icon)"
                ></svg>

                <span class="text-base font-semibold truncate">
                  {{ item.name }}
                </span>
              </button>
            </nav>
          </div>
        </div>
      </div>

      <div class="p-4 border-t border-slate-200 bg-slate-50">
        <div class="flex items-center gap-3 p-3 bg-white border border-slate-200 rounded-xl">
          <div
            class="h-12 w-12 rounded-full bg-[#8B1E23] flex items-center justify-center text-white font-bold text-sm shrink-0"
          >
            {{ currentUser?.rank || 'ADMIN' }}
          </div>

          <div class="overflow-hidden">
            <p class="text-sm font-bold text-slate-900 truncate">
              {{ currentUser?.name || 'Juan Dela Cruz' }}
            </p>
            <p class="text-xs text-slate-500 truncate">
              {{ currentUser?.role || 'System Administrator' }}
            </p>
          </div>
        </div>

        <button
          @click="showLogoutConfirm = true"
          class="w-full mt-3 flex items-center gap-3 px-4 py-3 rounded-xl text-base font-semibold text-slate-600 hover:bg-red-50 hover:text-[#8B1E23] transition"
        >
          <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
            <path
              d="M17 7l-1.41 1.41L18.17 11H8v2h10.17l-2.58 2.58L17 17l5-5zM4 5h8V3H4c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h8v-2H4V5z"
            />
          </svg>
          <span>Sign Out</span>
        </button>
      </div>
    </aside>

    <div class="flex-1 flex flex-col overflow-y-auto">
      <header
        class="bg-white border-b border-slate-200 px-8 py-5 flex items-center justify-between sticky top-0 z-30 shadow-sm"
      >
        <div class="flex items-center gap-4">
          <div class="h-11 w-11 rounded-xl bg-red-50 flex items-center justify-center">
            <svg
              class="w-6 h-6 fill-current text-[#8B1E23]"
              viewBox="0 0 24 24"
              v-html="getSvgPath(getActiveIcon())"
            ></svg>
          </div>

          <div>
            <p class="text-sm font-medium text-slate-500">FIRENOTIFY ADMIN</p>
            <h1 class="text-2xl font-bold text-slate-900">{{ activeMenu }}</h1>
          </div>
        </div>

        <div class="flex items-center gap-4">
          <div
            class="hidden md:flex items-center gap-2 px-4 py-2 rounded-full bg-green-50 border border-green-200"
          >
            <span class="h-3 w-3 rounded-full bg-green-500"></span>
            <span class="text-sm font-semibold text-green-700">System Online</span>
          </div>

          <button
            @click="activeMenu = 'Notifications'"
            class="relative h-12 w-12 flex items-center justify-center rounded-xl border border-slate-200 hover:bg-slate-100 transition"
            title="Notifications"
          >
            <svg class="w-6 h-6 fill-current text-slate-600" viewBox="0 0 24 24">
              <path
                d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5S10.5 3.17 10.5 4v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z"
              />
            </svg>
            <span
              class="absolute top-2 right-2 h-3 w-3 rounded-full bg-[#8B1E23] border-2 border-white"
            ></span>
          </button>
        </div>
      </header>

      <main class="p-6 lg:p-8 space-y-7">
        <Dashboard v-if="activeMenu === 'Dashboard'" :current-user="currentUser" />
        <ActivityManagement v-else-if="activeMenu === 'Activity Mgmt.'" :current-user="currentUser" />
        <PersonnelManagement v-else-if="activeMenu === 'Personnel Mgmt.'" :current-user="currentUser" />
        <ReportManagement v-else-if="activeMenu === 'Report Mgmt.'" :current-user="currentUser" />
        <DeadlineMonitor v-else-if="activeMenu === 'Deadline Monitor'" :current-user="currentUser" />
        <Notifications v-else-if="activeMenu === 'Notifications'" :current-user="currentUser" />
        <WeeklyMonthlyLogs v-else-if="activeMenu === 'Weekly/Monthly Logs'" :current-user="currentUser" />
        <AuditEscalations v-else-if="activeMenu === 'Audit & Escalations'" :current-user="currentUser" />
        <ComplianceHealth v-else-if="activeMenu === 'Compliance Health'" :current-user="currentUser" />
        <DocumentPipeline v-else-if="activeMenu === 'Document Pipeline'" :current-user="currentUser" />
        <PrintExportPDF v-else-if="activeMenu === 'Print & Export PDF'" :current-user="currentUser" />
      </main>
    </div>

    <div
      v-if="showLogoutConfirm"
      class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/40 px-4"
    >
      <div class="w-full max-w-md bg-white rounded-2xl shadow-2xl overflow-hidden">
        <div class="h-2 bg-[#8B1E23]"></div>

        <div class="p-7">
          <div class="flex items-start gap-4">
            <div
              class="h-14 w-14 rounded-full bg-red-50 flex items-center justify-center shrink-0"
            >
              <span class="text-xl">🚨</span>
            </div>

            <div>
              <h3 class="text-xl font-bold text-slate-900">Confirm Sign Out</h3>
              <p class="text-base text-slate-500 mt-1">
                Are you sure you want to sign out of the Admin Portal?
              </p>
            </div>
          </div>

          <div class="mt-5 p-4 rounded-xl bg-yellow-50 border border-yellow-200">
            <p class="text-sm text-slate-600 leading-relaxed">
              Make sure all important administrative changes and reports
              have been saved before signing out.
            </p>
          </div>

          <div class="flex flex-col-reverse sm:flex-row justify-end gap-3 mt-7">
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
import { ref, watch } from 'vue'
import Dashboard from './Dashboard.vue'
import ActivityManagement from './ActivityManagement.vue'
import PersonnelManagement from './PersonnelManagement.vue'
import ReportManagement from './ReportManagement.vue'
import DeadlineMonitor from './DeadlineMonitor.vue'
import Notifications from './Notifications.vue'
import WeeklyMonthlyLogs from './WeeklyMonthlyLogs.vue'
import AuditEscalations from './AuditEscalations.vue'
import ComplianceHealth from './ComplianceHealth.vue'
import DocumentPipeline from './DocumentPipeline.vue'
import PrintExportPDF from './PrintExportPDF.vue'

const props = defineProps({
  currentUser: {
    type: Object,
    required: false,
    default: null
  }
})

const emit = defineEmits(['logout'])


const ACTIVE_MENU_KEY = 'fireNotifyAdminActiveMenu'

const activeMenu = ref(
  localStorage.getItem(ACTIVE_MENU_KEY) || 'Dashboard'
)

watch(activeMenu, (newMenu) => {
  localStorage.setItem(ACTIVE_MENU_KEY, newMenu)
})



const showLogoutConfirm = ref(false)

const ICONS = {
  dashboard: 'M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z',
  activity: 'M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11z',
  personnel: 'M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z',
  report: 'M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z',
  deadline: 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z',
  notifications: 'M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5S10.5 3.17 10.5 4v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z',
  logs: 'M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z',
  shield: 'M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-5.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8s0 0 0 0z',
  default: 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z'
}

const menuBarItems = [
  { name: 'Dashboard', icon: 'dashboard' },
  { name: 'Activity Mgmt.', icon: 'activity' },
  { name: 'Personnel Mgmt.', icon: 'personnel' },
  { name: 'Report Mgmt.', icon: 'report' },
  { name: 'Deadline Monitor', icon: 'deadline' },
  { name: 'Notifications', icon: 'notifications', badge: '3' },
  { name: 'Weekly/Monthly Logs', icon: 'logs' },
]

const capstoneItems = [
  { name: 'Audit & Escalations', icon: 'shield' },
  { name: 'Compliance Health', icon: 'dashboard' },
  { name: 'Document Pipeline', icon: 'report' },
  { name: 'Print & Export PDF', icon: 'report' },
]

const confirmLogout = () => {
  showLogoutConfirm.value = false

  // Reset Admin page to Dashboard
  localStorage.removeItem(ACTIVE_MENU_KEY)

  emit('logout')
}


const getSvgPath = (key) => {
  return `<path d="${ICONS[key] || ICONS.default}"/>`
}

const getActiveIcon = () => {
  const allItems = [...menuBarItems, ...capstoneItems]
  const found = allItems.find(item => item.name === activeMenu.value)
  return found ? found.icon : 'default'
}
</script>
