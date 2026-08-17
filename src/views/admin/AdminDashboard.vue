<template>
  <div class="flex h-screen w-full bg-[#070A12] text-slate-200 font-sans overflow-hidden select-none">
    
    <!-- Sidebar -->
    <aside class="w-64 flex-shrink-0 border-r border-slate-800/80 bg-[#0B0F19] flex flex-col justify-between z-20">
      <div class="overflow-y-auto">
        <!-- Logo -->
        <div class="flex items-center gap-3 px-6 py-5 border-b border-slate-800/60">
          <div class="flex h-9 w-9 items-center justify-center rounded-full bg-red-600/20 border border-red-500/30 text-red-500 shadow-md shadow-red-500/10">
            🔥
          </div>
          <span class="text-lg font-extrabold tracking-wider text-white">FIRE<span class="text-red-500">NOTIFY</span></span>
        </div>

        <!-- Navigation Menu -->
        <div class="px-4 py-4 space-y-6">
          
          <!-- Menu Bar Category -->
          <div>
            <p class="px-3 text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-2">Menu Bar</p>
            <nav class="space-y-1">
              <button 
                v-for="item in menuBarItems" 
                :key="item.name"
                @click="activeMenu = item.name"
                :class="[
                  'w-full flex items-center justify-between rounded-xl px-3 py-2.5 text-xs font-semibold transition-all duration-200',
                  activeMenu === item.name 
                    ? 'bg-gradient-to-r from-red-950/60 to-red-900/30 text-red-400 border border-red-800/40 shadow-sm' 
                    : 'text-slate-400 hover:bg-slate-800/40 hover:text-slate-200'
                ]"
              >
                <div class="flex items-center gap-3">
                  <span class="text-sm">{{ item.icon }}</span>
                  <span>{{ item.name }}</span>
                </div>
                <span v-if="item.badge" class="bg-red-600 text-white text-[10px] font-bold px-1.5 py-0.5 rounded-full shadow-sm">
                  {{ item.badge }}
                </span>
              </button>
            </nav>
          </div>

          <!-- Capstone Features Category -->
          <div>
            <p class="px-3 text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-2">Capstone Features</p>
            <nav class="space-y-1">
              <button 
                v-for="item in capstoneItems" 
                :key="item.name"
                @click="activeMenu = item.name"
                :class="[
                  'w-full flex items-center gap-3 rounded-xl px-3 py-2.5 text-xs font-semibold transition-all duration-200',
                  activeMenu === item.name 
                    ? 'bg-gradient-to-r from-red-950/60 to-red-900/30 text-red-400 border border-red-800/40 shadow-sm' 
                    : 'text-slate-400 hover:bg-slate-800/40 hover:text-slate-200'
                ]"
              >
                <span class="text-sm">{{ item.icon }}</span>
                <span>{{ item.name }}</span>
              </button>
            </nav>
          </div>

        </div>
      </div>

      <!-- User Profile & Redesigned Logout Section -->
      <div class="p-3 border-t border-slate-800/60 bg-[#080C14] space-y-2">
        <!-- User Info Card -->
        <div class="flex items-center gap-3 p-2 rounded-xl bg-slate-900/40 border border-slate-800/50">
          <div class="h-8 w-8 rounded-lg bg-red-600 flex items-center justify-center font-bold text-white text-xs shadow-md shadow-red-600/30 flex-shrink-0">
            {{ currentUser?.rank || 'FO3' }}
          </div>
          <div class="overflow-hidden">
            <p class="text-xs font-bold text-white truncate">{{ currentUser?.name || 'Juan Dela Cruz' }}</p>
            <p class="text-[10px] text-slate-500 truncate">{{ currentUser?.role || 'Station Inspector' }}</p>
          </div>
        </div>

        <!-- Logout Button with Icon & Label -->
        <button 
          @click="showLogoutConfirm = true" 
          class="w-full flex items-center justify-between px-3 py-2 rounded-xl text-xs font-medium text-slate-400 hover:text-red-400 hover:bg-red-500/10 border border-transparent hover:border-red-500/20 transition group"
        >
          <div class="flex items-center gap-2.5">
            <span class="text-sm group-hover:scale-110 transition-transform">🚪</span>
            <span class="font-semibold">Log Out</span>
          </div>
          <span class="text-[10px] text-slate-600 group-hover:text-red-400 transition-colors">Exit</span>
        </button>
      </div>
    </aside>

    <!-- Main Content Area -->
    <div class="flex-1 flex flex-col overflow-y-auto bg-[#070A12]">
      
      <!-- Top Navbar -->
      <header class="h-16 border-b border-slate-800/60 bg-[#0B0F19] px-8 flex items-center justify-between sticky top-0 z-30">
        <div class="flex items-center gap-2">
          <span class="text-slate-400 text-sm">{{ getActiveIcon() }}</span>
          <h1 class="text-base font-bold text-white">{{ activeMenu }}</h1>
        </div>

        <div class="flex items-center gap-4">
          <div class="flex items-center gap-2 rounded-full border border-emerald-500/20 bg-emerald-500/10 px-3 py-1 text-xs text-emerald-400">
            <span class="h-1.5 w-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
            <span>System Active • Station 1</span>
          </div>
          <button @click="activeMenu = 'Notifications'" class="relative rounded-lg p-2 text-slate-400 hover:bg-slate-800 hover:text-white transition">
            🔔
            <span class="absolute top-1 right-1 h-2 w-2 rounded-full bg-red-500"></span>
          </button>
        </div>
      </header>

      <!-- Dynamic Views Container -->
      <main class="p-8 space-y-6">
        
        <!-- PAGE 1: DASHBOARD -->
        <div v-if="activeMenu === 'Dashboard'" class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            <div class="rounded-2xl border border-slate-800/80 bg-[#0B101D] p-5 shadow-lg">
              <p class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Total Active Personnel</p>
              <p class="mt-2 text-2xl font-black text-white">48 Officers</p>
              <p class="mt-2 text-xs text-emerald-400 font-medium">✓ All shifts covered</p>
            </div>
            <div class="rounded-2xl border border-slate-800/80 bg-[#0B101D] p-5 shadow-lg">
              <p class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Pending Compliance Reports</p>
              <p class="mt-2 text-2xl font-black text-amber-500">12 Reports</p>
              <p class="mt-2 text-xs text-amber-400 font-medium">⚠️ Due in 24 hours</p>
            </div>
            <div class="rounded-2xl border border-slate-800/80 bg-[#0B101D] p-5 shadow-lg">
              <p class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Overdue Deadlines</p>
              <p class="mt-2 text-2xl font-black text-red-500">2 Alerts</p>
              <p class="mt-2 text-xs text-red-400 font-medium">Requires escalation</p>
            </div>
            <div class="rounded-2xl border border-slate-800/80 bg-[#0B101D] p-5 shadow-lg">
              <p class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Compliance Rating</p>
              <p class="mt-2 text-2xl font-black text-emerald-400">94.5%</p>
              <p class="mt-1 text-xs text-slate-500">Monthly Station Average</p>
            </div>
          </div>

          <div class="rounded-2xl border border-slate-800/80 bg-[#0B101D] p-6 shadow-xl">
            <div class="flex items-center justify-between mb-6">
              <h2 class="text-base font-bold text-white">Recent Operational Compliance Logs</h2>
              <button @click="activeMenu = 'Weekly/Monthly Logs'" class="text-xs font-semibold text-red-400 hover:text-red-300 transition">View All</button>
            </div>

            <div class="overflow-x-auto">
              <table class="w-full text-left text-xs">
                <thead>
                  <tr class="border-b border-slate-800/80 text-slate-400 uppercase tracking-wider">
                    <th class="pb-3 font-semibold">Activity / Document</th>
                    <th class="pb-3 font-semibold">Personnel Assigned</th>
                    <th class="pb-3 font-semibold">Deadline</th>
                    <th class="pb-3 font-semibold text-right">Status</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-800/40">
                  <tr v-for="log in logs" :key="log.activity" class="hover:bg-slate-900/40 transition">
                    <td class="py-4 font-semibold text-slate-200">{{ log.activity }}</td>
                    <td class="py-4 text-slate-400">{{ log.personnel }}</td>
                    <td class="py-4 text-slate-400">{{ log.deadline }}</td>
                    <td class="py-4 text-right">
                      <span 
                        :class="[
                          'inline-block px-3 py-1 rounded-full text-[11px] font-bold',
                          log.status === 'Pending' ? 'bg-amber-500/10 text-amber-500 border border-amber-500/20' : 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20'
                        ]"
                      >
                        {{ log.status }}
                      </span>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- PAGE 2: ACTIVITY MANAGEMENT -->
        <div v-else-if="activeMenu === 'Activity Mgmt.'" class="space-y-6">
          <div class="flex justify-between items-center bg-[#0B101D] p-6 rounded-2xl border border-slate-800/80">
            <div>
              <h2 class="text-lg font-bold text-white">Station Activity Manager</h2>
              <p class="text-xs text-slate-400 mt-1">Schedule and monitor operational fire tasks and station drills.</p>
            </div>
            <button class="bg-red-600 hover:bg-red-500 text-white text-xs font-bold px-4 py-2.5 rounded-xl transition shadow-lg shadow-red-600/20">
              + Add New Activity
            </button>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div v-for="act in activityList" :key="act.title" class="bg-[#0B101D] border border-slate-800/80 p-5 rounded-2xl space-y-3">
              <span class="text-xs font-bold px-2.5 py-1 rounded-full bg-slate-800 text-red-400 border border-slate-700/50">{{ act.type }}</span>
              <h3 class="font-bold text-white text-sm">{{ act.title }}</h3>
              <p class="text-xs text-slate-400">Assigned: {{ act.lead }}</p>
              <div class="pt-2 border-t border-slate-800/60 flex justify-between text-[11px] text-slate-500">
                <span>📅 {{ act.date }}</span>
                <span class="text-emerald-400 font-semibold">{{ act.priority }} Priority</span>
              </div>
            </div>
          </div>
        </div>

        <!-- PAGE 3: PERSONNEL MANAGEMENT -->
        <div v-else-if="activeMenu === 'Personnel Mgmt.'" class="space-y-6">
          <div class="flex justify-between items-center">
            <h2 class="text-lg font-bold text-white">Station Roster & Personnel Duty</h2>
            <input type="text" placeholder="Search officer..." class="bg-[#0B101D] border border-slate-800 rounded-xl px-4 py-2 text-xs text-slate-200 focus:outline-none focus:border-red-500 w-64" />
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            <div v-for="person in personnelList" :key="person.name" class="bg-[#0B101D] border border-slate-800/80 p-5 rounded-2xl flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="h-10 w-10 rounded-xl bg-slate-800 border border-slate-700 flex items-center justify-center font-bold text-red-400 text-xs">
                  {{ person.rank }}
                </div>
                <div>
                  <h4 class="text-xs font-bold text-white">{{ person.name }}</h4>
                  <p class="text-[10px] text-slate-500">{{ person.role }}</p>
                </div>
              </div>
              <span class="px-2.5 py-1 rounded-full text-[10px] font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                {{ person.shift }} Shift
              </span>
            </div>
          </div>
        </div>

        <!-- PAGE 4: REPORT MANAGEMENT -->
        <div v-else-if="activeMenu === 'Report Mgmt.'" class="space-y-6">
          <div class="bg-[#0B101D] p-6 rounded-2xl border border-slate-800/80 space-y-4">
            <h2 class="text-base font-bold text-white">Submit Official Compliance Report</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs text-slate-400 mb-2">Report Title</label>
                <input type="text" placeholder="e.g. Post-Fire Incident Assessment" class="w-full bg-[#070A12] border border-slate-800 rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-red-500" />
              </div>
              <div>
                <label class="block text-xs text-slate-400 mb-2">Assigned Lead Inspector</label>
                <select class="w-full bg-[#070A12] border border-slate-800 rounded-xl px-4 py-2.5 text-xs text-slate-300 focus:outline-none focus:border-red-500">
                  <option>FO3 Juan Dela Cruz</option>
                  <option>SFO1 M. Santos</option>
                </select>
              </div>
            </div>
            <button class="bg-red-600 hover:bg-red-500 text-white text-xs font-bold px-5 py-2.5 rounded-xl transition">
              Upload Report Document
            </button>
          </div>
        </div>

        <!-- PAGE 5: DEADLINE MONITOR -->
        <div v-else-if="activeMenu === 'Deadline Monitor'" class="space-y-4">
          <div class="bg-[#0B101D] p-6 rounded-2xl border border-slate-800/80">
            <h2 class="text-base font-bold text-white mb-4">Critical Deadline Alerts</h2>
            <div class="space-y-3">
              <div class="flex items-center justify-between p-4 bg-red-500/10 border border-red-500/20 rounded-xl text-xs">
                <div class="flex items-center gap-3">
                  <span class="text-lg">🚨</span>
                  <div>
                    <p class="font-bold text-red-200">After-Operation Fire Incident Report</p>
                    <p class="text-red-400/80 text-[10px]">Overdue by 2 hours • High Escalation</p>
                  </div>
                </div>
                <button class="bg-red-600 px-3 py-1.5 rounded-lg text-white font-bold text-[10px]">Escalate Now</button>
              </div>
              <div class="flex items-center justify-between p-4 bg-amber-500/10 border border-amber-500/20 rounded-xl text-xs">
                <div class="flex items-center gap-3">
                  <span class="text-lg">⚠️</span>
                  <div>
                    <p class="font-bold text-amber-200">Quarterly Station Equipment Inspection</p>
                    <p class="text-amber-400/80 text-[10px]">Due in 18 Hours</p>
                  </div>
                </div>
                <button class="bg-amber-600 px-3 py-1.5 rounded-lg text-white font-bold text-[10px]">Notify Officer</button>
              </div>
            </div>
          </div>
        </div>

        <!-- PAGE 6: NOTIFICATIONS -->
        <div v-else-if="activeMenu === 'Notifications'" class="space-y-4">
          <div class="bg-[#0B101D] p-6 rounded-2xl border border-slate-800/80">
            <h2 class="text-base font-bold text-white mb-4">System Alerts & Notifications</h2>
            <div class="space-y-2">
              <div v-for="n in 3" :key="n" class="p-3.5 bg-slate-900/60 rounded-xl border border-slate-800/60 flex justify-between items-center text-xs">
                <div>
                  <p class="font-semibold text-slate-200">New Compliance Guidelines Published</p>
                  <p class="text-[10px] text-slate-500">Regional Command • 10 mins ago</p>
                </div>
                <span class="text-[10px] text-red-400 font-bold bg-red-500/10 px-2 py-0.5 rounded border border-red-500/20">Unread</span>
              </div>
            </div>
          </div>
        </div>

        <!-- FALLBACK SUB-PAGES -->
        <div v-else class="space-y-6">
          <div class="bg-[#0B101D] p-8 rounded-2xl border border-slate-800/80 text-center space-y-3">
            <div class="text-4xl">{{ getActiveIcon() }}</div>
            <h2 class="text-lg font-bold text-white">{{ activeMenu }} Panel</h2>
            <p class="text-xs text-slate-400 max-w-md mx-auto">
              This panel is dynamically configured for {{ activeMenu }}. You can hook up specific FireNotify backend APIs or custom workflows here.
            </p>
            <div class="pt-4">
              <span class="inline-block px-4 py-2 rounded-xl bg-slate-800 text-slate-300 text-xs font-mono border border-slate-700">
                Module Status: Operational
              </span>
            </div>
          </div>
        </div>

      </main>
    </div>

    <!-- Log Out Confirmation Modal -->
    <div v-if="showLogoutConfirm" class="fixed inset-0 z-50 flex items-center justify-center bg-[#070A12]/80 backdrop-blur-md transition-opacity">
      <div class="w-full max-w-md rounded-2xl border border-slate-800 bg-[#0B101D] p-6 shadow-2xl space-y-4">
        <div class="flex items-center gap-3">
          <div class="flex h-10 w-10 items-center justify-center rounded-xl bg-red-500/10 border border-red-500/20 text-red-500 text-lg">
            🚨
          </div>
          <div>
            <h3 class="text-base font-bold text-white">Confirm Log Out</h3>
            <p class="text-xs text-slate-400">Are you sure you want to end your active session?</p>
          </div>
        </div>
        
        <p class="text-xs text-slate-400 leading-relaxed bg-[#070A12] p-3 rounded-xl border border-slate-800">
          You will be returned to the login screen. Any unsaved reports or draft forms will be discarded.
        </p>

        <div class="flex justify-end gap-3 pt-2">
          <button 
            @click="showLogoutConfirm = false" 
            class="rounded-xl border border-slate-700 bg-slate-800/80 px-4 py-2 text-xs font-medium text-slate-300 hover:bg-slate-700 transition"
          >
            Cancel
          </button>
          <button 
            @click="confirmLogout" 
            class="rounded-xl bg-red-600 px-4 py-2 text-xs font-semibold text-white shadow-lg shadow-red-600/30 hover:bg-red-500 transition"
          >
            Yes, Log Out
          </button>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  currentUser: {
    type: Object,
    required: false,
    default: null
  }
})

const emit = defineEmits(['logout'])

const activeMenu = ref('Dashboard')
const showLogoutConfirm = ref(false)

const menuBarItems = [
  { name: 'Dashboard', icon: '📊' },
  { name: 'Activity Mgmt.', icon: '📅' },
  { name: 'Personnel Mgmt.', icon: '🧑‍🚒' },
  { name: 'Report Mgmt.', icon: '📄' },
  { name: 'Deadline Monitor', icon: '🚨' },
  { name: 'Notifications', icon: '🔔', badge: '3' },
  { name: 'Weekly/Monthly Logs', icon: '📈' },
]

const capstoneItems = [
  { name: 'Audit & Escalations', icon: '🛡️' },
  { name: 'Compliance Health', icon: '🏆' },
  { name: 'Document Pipeline', icon: '📥' },
  { name: 'Print & Export PDF', icon: '🖨️' },
]

const logs = ref([
  {
    activity: 'After-Operation Fire Incident Report',
    personnel: 'SFO1 M. Santos',
    deadline: 'Today, 5:00 PM',
    status: 'Pending'
  },
  {
    activity: 'Quarterly Establishment Inspection',
    personnel: 'FO3 J. Dela Cruz',
    deadline: 'Aug 20, 2026',
    status: 'Completed'
  }
])

const activityList = ref([
  { title: 'Commercial Hydrant Inspection', lead: 'SFO1 M. Santos', type: 'Inspection', date: 'Today', priority: 'High' },
  { title: 'Barangay Safety Seminar', lead: 'FO3 J. Dela Cruz', type: 'Drill', date: 'Tomorrow', priority: 'Medium' },
  { title: 'Engine Maintenance Audit', lead: 'FO1 A. Reyes', type: 'Maintenance', date: 'Aug 19, 2026', priority: 'Low' }
])

const personnelList = ref([
  { name: 'Juan Dela Cruz', rank: 'FO3', role: 'Station Inspector', shift: 'Day' },
  { name: 'M. Santos', rank: 'SFO1', role: 'Operations Chief', shift: 'Day' },
  { name: 'A. Reyes', rank: 'FO1', role: 'Equipment Supervisor', shift: 'Night' }
])

const confirmLogout = () => {
  showLogoutConfirm.value = false
  emit('logout')
}

const getActiveIcon = () => {
  const allItems = [...menuBarItems, ...capstoneItems]
  const found = allItems.find(item => item.name === activeMenu.value)
  return found ? found.icon : '📌'
}
</script>