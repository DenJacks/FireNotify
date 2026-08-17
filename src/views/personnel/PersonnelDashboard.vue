<template>
  <div class="flex h-screen w-full bg-[#070A12] text-slate-200 font-sans overflow-hidden select-none">
    
    <!-- Background Glow Accents -->
    <div class="pointer-events-none absolute top-0 left-1/4 h-96 w-96 -translate-y-1/2 rounded-full bg-red-600/10 blur-[120px]"></div>
    <div class="pointer-events-none absolute top-1/3 right-10 h-96 w-96 rounded-full bg-amber-600/10 blur-[140px]"></div>

    <!-- Enhanced Sidebar -->
    <aside class="w-64 flex-shrink-0 border-r border-slate-800/80 bg-[#0B0F19] flex flex-col justify-between z-20">
      <div class="overflow-y-auto">
        
        <!-- Logo -->
        <div class="flex items-center gap-3 px-6 py-5 border-b border-slate-800/60">
          <div class="flex h-9 w-9 items-center justify-center rounded-full bg-red-600/20 border border-red-500/30 text-red-500 shadow-md shadow-red-500/10">
            🔥
          </div>
          <div>
            <span class="text-[10px] font-bold uppercase tracking-widest text-red-500 block -mb-1">Personnel Portal</span>
            <span class="text-lg font-extrabold tracking-wider text-white">FIRE<span class="text-red-500">NOTIFY</span></span>
          </div>
        </div>

        <!-- Navigation Categories -->
        <div class="px-4 py-4 space-y-5">
          
          <!-- Category 1: Field Operations -->
          <div>
            <p class="px-3 text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-2">Field Duty</p>
            <nav class="space-y-1">
              <button 
                v-for="item in fieldItems" 
                :key="item.name"
                @click="activeTab = item.name"
                :class="[
                  'w-full flex items-center justify-between rounded-xl px-3 py-2 text-xs font-semibold transition-all duration-200',
                  activeTab === item.name 
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

          <!-- Category 2: Station Management & Records -->
          <div>
            <p class="px-3 text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-2">Management & Records</p>
            <nav class="space-y-1">
              <button 
                v-for="item in managementItems" 
                :key="item.name"
                @click="activeTab = item.name"
                :class="[
                  'w-full flex items-center gap-3 rounded-xl px-3 py-2 text-xs font-semibold transition-all duration-200',
                  activeTab === item.name 
                    ? 'bg-gradient-to-r from-red-950/60 to-red-900/30 text-red-400 border border-red-800/40 shadow-sm' 
                    : 'text-slate-400 hover:bg-slate-800/40 hover:text-slate-200'
                ]"
              >
                <span class="text-sm">{{ item.icon }}</span>
                <span>{{ item.name }}</span>
              </button>
            </nav>
          </div>

          <!-- Category 3: Personnel Tools -->
          <div>
            <p class="px-3 text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-2">Personnel Tools</p>
            <nav class="space-y-1">
              <button 
                v-for="item in toolItems" 
                :key="item.name"
                @click="activeTab = item.name"
                :class="[
                  'w-full flex items-center gap-3 rounded-xl px-3 py-2 text-xs font-semibold transition-all duration-200',
                  activeTab === item.name 
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

      <!-- User Profile & Redesigned Bottom Bar -->
      <div class="p-3 border-t border-slate-800/60 bg-[#080C14] space-y-2">
        <!-- Profile Box -->
        <div class="flex items-center gap-3 p-2 rounded-xl bg-slate-900/40 border border-slate-800/50">
          <div class="h-8 w-8 rounded-lg bg-red-600 flex items-center justify-center font-bold text-white text-xs shadow-md shadow-red-600/30 flex-shrink-0">
            {{ currentUser?.rank || 'FO3' }}
          </div>
          <div class="overflow-hidden">
            <p class="text-xs font-bold text-white truncate">{{ currentUser?.firstName || 'Juan' }} {{ currentUser?.lastName || 'Dela Cruz' }}</p>
            <p class="text-[10px] text-slate-500 truncate">Station Inspector</p>
          </div>
        </div>

        <!-- Full Logout Action Button -->
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
    <div class="flex-1 flex flex-col overflow-y-auto bg-[#070A12] z-10">
      
      <!-- Top Navbar -->
      <header class="h-16 border-b border-slate-800/60 bg-[#0B0F19]/90 backdrop-blur-md px-8 flex items-center justify-between sticky top-0 z-30">
        <div class="flex items-center gap-2">
          <span class="text-slate-400 text-sm">{{ getActiveIcon() }}</span>
          <h1 class="text-base font-bold text-white">{{ activeTab }}</h1>
        </div>

        <div class="flex items-center gap-4">
          <div class="flex items-center gap-2 rounded-full border border-emerald-500/20 bg-emerald-500/10 px-3 py-1 text-xs text-emerald-400">
            <span class="h-1.5 w-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
            <span>On Duty • Station 1</span>
          </div>
          <button @click="activeTab = 'Notifications'" class="relative rounded-lg p-2 text-slate-400 hover:bg-slate-800 hover:text-white transition">
            🔔
            <span class="absolute top-1 right-1 h-2 w-2 rounded-full bg-red-500"></span>
          </button>
        </div>
      </header>

      <!-- Dashboard Body -->
      <main class="p-8 space-y-6">
        
        <!-- Top Stats Cards -->
        <section class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div class="rounded-2xl border border-slate-800/80 bg-[#0B101D] p-5 shadow-lg">
            <div class="flex justify-between items-center">
              <p class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Assigned Tasks</p>
              <span class="text-lg">📋</span>
            </div>
            <p class="mt-2 text-3xl font-black text-white">9</p>
            <p class="mt-2 text-xs text-emerald-400 font-medium">4 Urgent pending</p>
          </div>

          <div class="rounded-2xl border border-slate-800/80 bg-[#0B101D] p-5 shadow-lg">
            <div class="flex justify-between items-center">
              <p class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Pending Reports</p>
              <span class="text-lg">📄</span>
            </div>
            <p class="mt-2 text-3xl font-black text-amber-500">3</p>
            <p class="mt-2 text-xs text-amber-400 font-medium">⚠️ Submission needed</p>
          </div>

          <div class="rounded-2xl border border-slate-800/80 bg-[#0B101D] p-5 shadow-lg">
            <div class="flex justify-between items-center">
              <p class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Station Alerts</p>
              <span class="text-lg">🚨</span>
            </div>
            <p class="mt-2 text-3xl font-black text-red-500">2</p>
            <p class="mt-2 text-xs text-red-400 font-medium">Requires immediate response</p>
          </div>
        </section>

        <!-- Dynamic Main Views -->
        <section class="grid grid-cols-1 lg:grid-cols-3 gap-6">
          
          <div class="lg:col-span-2 space-y-6">
            
            <!-- VIEW: DASHBOARD -->
            <div v-if="activeTab === 'Dashboard'" class="rounded-2xl border border-slate-800/80 bg-[#0B101D] p-6 shadow-xl space-y-4">
              <div class="flex items-center justify-between border-b border-slate-800/80 pb-4">
                <h2 class="text-base font-bold text-white">Active Operational Workflows</h2>
                <button @click="activeTab = 'Tasks'" class="text-xs font-semibold text-red-400 hover:text-red-300 transition">View All Tasks</button>
              </div>

              <div class="space-y-3">
                <div class="flex items-center justify-between rounded-xl border border-slate-800 bg-[#070A12] p-4 text-xs">
                  <div class="flex items-center gap-3">
                    <span class="text-emerald-400 text-lg">✓</span>
                    <div>
                      <p class="font-bold text-slate-200">Routine Safety Patrol</p>
                      <p class="text-[10px] text-slate-500">Zone 2 Commercial Area</p>
                    </div>
                  </div>
                  <span class="px-2.5 py-1 rounded-full text-[10px] font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Completed</span>
                </div>

                <div class="flex items-center justify-between rounded-xl border border-slate-800 bg-[#070A12] p-4 text-xs">
                  <div class="flex items-center gap-3">
                    <span class="text-amber-400 text-lg">⏳</span>
                    <div>
                      <p class="font-bold text-slate-200">Fire Hazard Inspection</p>
                      <p class="text-[10px] text-slate-500">Public Market Complex</p>
                    </div>
                  </div>
                  <span class="px-2.5 py-1 rounded-full text-[10px] font-bold bg-amber-500/10 text-amber-400 border border-amber-500/20">In Progress</span>
                </div>

                <div class="flex items-center justify-between rounded-xl border border-slate-800 bg-[#070A12] p-4 text-xs">
                  <div class="flex items-center gap-3">
                    <span class="text-red-400 text-lg">🚨</span>
                    <div>
                      <p class="font-bold text-slate-200">Post-Operation Incident Assessment</p>
                      <p class="text-[10px] text-slate-500">Subdivision Sector 4</p>
                    </div>
                  </div>
                  <span class="px-2.5 py-1 rounded-full text-[10px] font-bold bg-red-500/10 text-red-400 border border-red-500/20">Urgent</span>
                </div>
              </div>
            </div>

            <!-- VIEW: TASKS -->
            <div v-else-if="activeTab === 'Tasks'" class="rounded-2xl border border-slate-800/80 bg-[#0B101D] p-6 shadow-xl space-y-4">
              <h2 class="text-base font-bold text-white border-b border-slate-800/80 pb-4">Assigned Personnel Tasks</h2>
              <div class="space-y-3">
                <div v-for="task in taskList" :key="task.title" class="flex items-center justify-between rounded-xl border border-slate-800 bg-[#070A12] p-4 text-xs">
                  <div>
                    <p class="font-bold text-slate-200">{{ task.title }}</p>
                    <p class="text-[10px] text-slate-500">Due: {{ task.due }}</p>
                  </div>
                  <button class="bg-slate-800 hover:bg-slate-700 text-slate-200 text-[10px] font-bold px-3 py-1.5 rounded-lg border border-slate-700 transition">
                    Update Status
                  </button>
                </div>
              </div>
            </div>

            <!-- VIEW: REPORTS -->
            <div v-else-if="activeTab === 'Reports'" class="rounded-2xl border border-slate-800/80 bg-[#0B101D] p-6 shadow-xl space-y-4">
              <h2 class="text-base font-bold text-white border-b border-slate-800/80 pb-4">Incident & Operational Submissions</h2>
              <div class="space-y-3">
                <div class="flex items-center justify-between rounded-xl border border-slate-800 bg-[#070A12] p-4 text-xs">
                  <div>
                    <p class="font-bold text-slate-200">Incident Report #1047</p>
                    <p class="text-[10px] text-slate-500">Submitted by: FO3 J. Dela Cruz</p>
                  </div>
                  <span class="px-2.5 py-1 rounded-full text-[10px] font-bold bg-red-500/10 text-red-400 border border-red-500/20">Pending Review</span>
                </div>
              </div>
            </div>

            <!-- VIEW: PERSONNEL ROSTER -->
            <div v-else-if="activeTab === 'Personnel Roster'" class="rounded-2xl border border-slate-800/80 bg-[#0B101D] p-6 shadow-xl space-y-4">
              <h2 class="text-base font-bold text-white border-b border-slate-800/80 pb-4">Active Station Roster</h2>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <div v-for="person in roster" :key="person.name" class="p-3 bg-[#070A12] border border-slate-800 rounded-xl flex items-center gap-3">
                  <div class="h-9 w-9 rounded-lg bg-slate-800 border border-slate-700 flex items-center justify-center font-bold text-red-400 text-xs">
                    {{ person.rank }}
                  </div>
                  <div>
                    <p class="text-xs font-bold text-white">{{ person.name }}</p>
                    <p class="text-[10px] text-slate-500">{{ person.role }} • {{ person.shift }}</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- FALLBACK SUB-PANEL -->
            <div v-else class="rounded-2xl border border-slate-800/80 bg-[#0B101D] p-8 shadow-xl text-center space-y-3">
              <div class="text-4xl">{{ getActiveIcon() }}</div>
              <h2 class="text-lg font-bold text-white">{{ activeTab }} View</h2>
              <p class="text-xs text-slate-400 max-w-md mx-auto">
                This section is dynamically loaded for field operations. Custom tools for {{ activeTab }} can be linked here.
              </p>
            </div>

          </div>

          <!-- Right Panel: Live Feeds -->
          <div class="rounded-2xl border border-slate-800/80 bg-[#0B101D] p-6 shadow-xl space-y-4">
            <div class="flex items-center justify-between">
              <h3 class="text-sm font-bold text-white">Live Station Feeds</h3>
              <span class="text-[10px] text-slate-500">Real-time</span>
            </div>

            <div class="space-y-3 text-xs">
              <div class="rounded-xl border border-amber-500/20 bg-amber-500/10 p-3.5 text-amber-200">
                <p class="font-bold text-[11px]">📢 Morning Briefing</p>
                <p class="text-[10px] text-amber-300/80 mt-1">Station shift change and equipment check at 08:00 AM.</p>
              </div>

              <div class="rounded-xl border border-red-500/20 bg-red-500/10 p-3.5 text-red-200">
                <p class="font-bold text-[11px]">🚨 Escalation Warning</p>
                <p class="text-[10px] text-red-300/80 mt-1">Maintenance request #202 waiting for inspector approval.</p>
              </div>

              <div class="rounded-xl border border-emerald-500/20 bg-emerald-500/10 p-3.5 text-emerald-200">
                <p class="font-bold text-[11px]">✅ Safety Clearance</p>
                <p class="text-[10px] text-emerald-300/80 mt-1">Quarterly safety seminar training verified and logged.</p>
              </div>
            </div>
          </div>

        </section>

      </main>
    </div>

    <!-- Sign Out Confirmation Modal -->
    <div v-if="showLogoutConfirm" class="fixed inset-0 z-50 flex items-center justify-center bg-[#070A12]/80 backdrop-blur-md transition-opacity">
      <div class="w-full max-w-md rounded-2xl border border-slate-800 bg-[#0B101D] p-6 shadow-2xl space-y-4">
        <div class="flex items-center gap-3">
          <div class="flex h-10 w-10 items-center justify-center rounded-xl bg-red-500/10 border border-red-500/20 text-red-500 text-lg">
            🚨
          </div>
          <div>
            <h3 class="text-base font-bold text-white">Confirm Sign Out</h3>
            <p class="text-xs text-slate-400">Are you sure you want to log out from the Personnel Portal?</p>
          </div>
        </div>
        
        <p class="text-xs text-slate-400 leading-relaxed bg-[#070A12] p-3 rounded-xl border border-slate-800">
          Unsaved changes in active forms or field logs may be lost upon logging out.
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
            Sign Out
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

const activeTab = ref('Dashboard')
const showLogoutConfirm = ref(false)

const fieldItems = [
  { name: 'Dashboard', icon: '📊' },
  { name: 'Tasks', icon: '📋' },
  { name: 'Reports', icon: '📄' },
  { name: 'Notifications', icon: '🔔', badge: '3' }
]

const managementItems = [
  { name: 'Personnel Roster', icon: '🧑‍🚒' },
  { name: 'Station Duty Log', icon: '📑' },
  { name: 'Equipment Audit', icon: '🛠️' }
]

const toolItems = [
  { name: 'Support', icon: '🎧' },
  { name: 'Settings', icon: '⚙️' }
]

const taskList = ref([
  { title: 'Check hydrant systems in Sector 1', due: 'Today, 5:00 PM' },
  { title: 'Submit incident log for Station 2', due: 'Tomorrow, 10:00 AM' },
  { title: 'Conduct Fire Safety Inspection', due: 'Aug 22, 2026' }
])

const roster = ref([
  { name: 'Juan Dela Cruz', rank: 'FO3', role: 'Inspector', shift: 'Day' },
  { name: 'Mark Santos', rank: 'SFO1', role: 'Chief', shift: 'Day' },
  { name: 'Alan Reyes', rank: 'FO1', role: 'Equipment', shift: 'Night' }
])

const confirmLogout = () => {
  showLogoutConfirm.value = false
  emit('logout')
}

const getActiveIcon = () => {
  const allItems = [...fieldItems, ...managementItems, ...toolItems]
  const found = allItems.find(item => item.name === activeTab.value)
  return found ? found.icon : '📌'
}
</script>