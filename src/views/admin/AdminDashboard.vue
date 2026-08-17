<template>
  <div class="flex h-screen w-full bg-[#120F0C] text-[#EDE6D6] font-sans overflow-hidden select-none">
    
    <!-- Sidebar -->
    <aside class="w-64 flex-shrink-0 border-r border-[#2D2620] bg-[#181410] flex flex-col justify-between z-20 relative">
      <!-- Top Hazard Accent Stripe -->
      <div class="h-1.5 w-full bg-[repeating-linear-gradient(45deg,#C1272D,#C1272D_10px,#181410_10px,#181410_20px)] border-b border-[#2D2620]"></div>

      <div class="overflow-y-auto flex-1">
        <!-- Logo Header -->
        <div class="flex items-center gap-3 px-5 py-4 border-b border-[#2D2620]">
          <div class="flex h-9 w-9 items-center justify-center rounded-lg bg-[#C1272D]/20 border border-[#C1272D]/50 text-[#C1272D] shadow-inner">
            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
              <path d="M12 23c-4.97 0-9-3.58-9-8 0-4.19 3.01-7.13 5.48-9.53C9.44 4.54 10.5 3.5 11 2c.4 1.5 1.5 2.54 2.52 3.47C16 7.87 19 10.81 19 15c0 4.42-4.03 8-9 8zm0-4c2.21 0 4-1.79 4-4 0-2.05-1.55-3.6-2.9-4.88-.67-.64-1.1-1.25-1.1-2.12-.47.8-1.07 1.4-1.72 2.03C8.95 11.4 7 13.06 7 15c0 2.21 2.24 4 5 4z"/>
            </svg>
          </div>
          <div>
            <span class="text-base font-black tracking-widest text-[#EDE6D6] block leading-none font-mono">FIRE<span class="text-[#C1272D]">NOTIFY</span></span>
            <span class="text-[9px] font-mono tracking-widest text-[#A89F91] uppercase">Station Operations</span>
          </div>
        </div>

        <!-- Navigation Menu -->
        <div class="px-3 py-4 space-y-6">
          
          <!-- Menu Bar Category -->
          <div>
            <p class="px-3 text-[9px] font-mono font-bold uppercase tracking-widest text-[#A89F91] mb-2 flex items-center gap-1.5">
              <span class="w-1.5 h-1.5 rounded-full bg-[#C1272D]"></span> Navigation
            </p>
            <nav class="space-y-1">
              <button 
                v-for="item in menuBarItems" 
                :key="item.name"
                @click="activeMenu = item.name"
                :class="[
                  'w-full flex items-center justify-between rounded-md px-3 py-2 text-xs font-mono tracking-wide transition-all duration-150',
                  activeMenu === item.name 
                    ? 'bg-[#C1272D]/15 text-[#EDE6D6] border-l-2 border-[#C1272D] font-bold' 
                    : 'text-[#A89F91] hover:bg-[#221B15] hover:text-[#EDE6D6]'
                ]"
              >
                <div class="flex items-center gap-2.5">
                  <svg class="w-4 h-4 fill-current opacity-80" viewBox="0 0 24 24" v-html="getSvgPath(item.icon)"></svg>
                  <span>{{ item.name }}</span>
                </div>
                <span v-if="item.badge" class="bg-[#C1272D] text-[#EDE6D6] text-[9px] font-mono font-bold px-1.5 py-0.2 rounded shadow">
                  {{ item.badge }}
                </span>
              </button>
            </nav>
          </div>

          <!-- Capstone Features Category -->
          <div>
            <p class="px-3 text-[9px] font-mono font-bold uppercase tracking-widest text-[#A89F91] mb-2 flex items-center gap-1.5">
              <span class="w-1.5 h-1.5 rounded-full bg-[#E8A33D]"></span> Capstone Core
            </p>
            <nav class="space-y-1">
              <button 
                v-for="item in capstoneItems" 
                :key="item.name"
                @click="activeMenu = item.name"
                :class="[
                  'w-full flex items-center gap-2.5 rounded-md px-3 py-2 text-xs font-mono tracking-wide transition-all duration-150',
                  activeMenu === item.name 
                    ? 'bg-[#E8A33D]/15 text-[#EDE6D6] border-l-2 border-[#E8A33D] font-bold' 
                    : 'text-[#A89F91] hover:bg-[#221B15] hover:text-[#EDE6D6]'
                ]"
              >
                <svg class="w-4 h-4 fill-current opacity-80" viewBox="0 0 24 24" v-html="getSvgPath(item.icon)"></svg>
                <span>{{ item.name }}</span>
              </button>
            </nav>
          </div>

        </div>
      </div>

      <!-- User Profile & Logout -->
      <div class="p-3 border-t border-[#2D2620] bg-[#120F0C] space-y-2">
        <div class="flex items-center gap-3 p-2 rounded bg-[#181410] border border-[#2D2620]">
          <div class="h-7 w-7 rounded bg-[#C1272D] flex items-center justify-center font-mono font-bold text-[#EDE6D6] text-[10px] shadow flex-shrink-0">
            {{ currentUser?.rank || 'FO3' }}
          </div>
          <div class="overflow-hidden">
            <p class="text-xs font-bold text-[#EDE6D6] truncate leading-tight">{{ currentUser?.name || 'Juan Dela Cruz' }}</p>
            <p class="text-[10px] font-mono text-[#A89F91] truncate">{{ currentUser?.role || 'Station Inspector' }}</p>
          </div>
        </div>

        <button 
          @click="showLogoutConfirm = true" 
          class="w-full flex items-center justify-between px-3 py-2 rounded text-xs font-mono text-[#A89F91] hover:text-[#C1272D] hover:bg-[#C1272D]/10 border border-transparent hover:border-[#C1272D]/30 transition group"
        >
          <div class="flex items-center gap-2">
            <svg class="w-4 h-4 fill-current group-hover:scale-110 transition-transform" viewBox="0 0 24 24">
              <path d="M17 7l-1.41 1.41L18.17 11H8v2h10.17l-2.58 2.58L17 17l5-5zM4 5h8V3H4c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h8v-2H4V5z"/>
            </svg>
            <span class="font-bold">Sign Out</span>
          </div>
          <span class="text-[9px] font-mono text-[#2D2620] group-hover:text-[#C1272D]">Exit</span>
        </button>
      </div>
    </aside>

    <!-- Main Content Area -->
    <div class="flex-1 flex flex-col overflow-y-auto bg-[#120F0C]">
      
      <!-- Top Navbar -->
      <header class="h-14 border-b border-[#2D2620] bg-[#181410] px-6 flex items-center justify-between sticky top-0 z-30">
        <div class="flex items-center gap-2.5">
          <svg class="w-4 h-4 fill-current text-[#C1272D]" viewBox="0 0 24 24" v-html="getSvgPath(getActiveIcon())"></svg>
          <h1 class="text-sm font-mono font-bold tracking-wider text-[#EDE6D6] uppercase">{{ activeMenu }}</h1>
        </div>

        <div class="flex items-center gap-4">
          <div class="flex items-center gap-2 rounded border border-emerald-500/30 bg-emerald-500/10 px-2.5 py-1 text-[11px] font-mono text-emerald-400">
            <span class="h-2 w-2 rounded-full bg-emerald-400 animate-pulse"></span>
            <span>ON DUTY • STATION 1</span>
          </div>
          <button @click="activeMenu = 'Notifications'" class="relative rounded p-1.5 text-[#A89F91] hover:bg-[#221B15] hover:text-[#EDE6D6] transition">
            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
              <path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z"/>
            </svg>
            <span class="absolute top-1 right-1 h-2 w-2 rounded-full bg-[#C1272D]"></span>
          </button>
        </div>
      </header>

      <!-- Dynamic Views Container -->
      <main class="p-6 space-y-6">
        
        <!-- PAGE 1: DASHBOARD -->
        <div v-if="activeMenu === 'Dashboard'" class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            <div class="rounded bg-[#181410] border border-[#2D2620] p-4 relative overflow-hidden">
              <div class="h-1 w-full bg-emerald-500 absolute top-0 left-0"></div>
              <p class="text-[10px] font-mono font-bold uppercase tracking-wider text-[#A89F91]">Active Personnel</p>
              <p class="mt-1 text-2xl font-mono font-bold text-[#EDE6D6]">48 Officers</p>
              <p class="mt-2 text-[10px] font-mono text-emerald-400">✓ Shifts fully covered</p>
            </div>
            
            <div class="rounded bg-[#181410] border border-[#2D2620] p-4 relative overflow-hidden">
              <div class="h-1 w-full bg-[#E8A33D] absolute top-0 left-0"></div>
              <p class="text-[10px] font-mono font-bold uppercase tracking-wider text-[#A89F91]">Pending Reports</p>
              <p class="mt-1 text-2xl font-mono font-bold text-[#E8A33D]">12 Files</p>
              <p class="mt-2 text-[10px] font-mono text-[#E8A33D]">⚠️ Action required within 24h</p>
            </div>

            <div class="rounded bg-[#181410] border border-[#2D2620] p-4 relative overflow-hidden">
              <div class="h-1 w-full bg-[#C1272D] absolute top-0 left-0"></div>
              <p class="text-[10px] font-mono font-bold uppercase tracking-wider text-[#A89F91]">Overdue Deadlines</p>
              <p class="mt-1 text-2xl font-mono font-bold text-[#C1272D]">2 Escalations</p>
              <p class="mt-2 text-[10px] font-mono text-[#C1272D]">Requires station chief audit</p>
            </div>

            <div class="rounded bg-[#181410] border border-[#2D2620] p-4 relative overflow-hidden">
              <div class="h-1 w-full bg-[#A89F91] absolute top-0 left-0"></div>
              <p class="text-[10px] font-mono font-bold uppercase tracking-wider text-[#A89F91]">Compliance Score</p>
              <p class="mt-1 text-2xl font-mono font-bold text-[#EDE6D6]">94.5%</p>
              <p class="mt-2 text-[10px] font-mono text-[#A89F91]">Monthly station metric</p>
            </div>
          </div>

          <div class="rounded bg-[#181410] border border-[#2D2620] p-5">
            <div class="flex items-center justify-between mb-4 border-b border-[#2D2620] pb-3">
              <h2 class="text-xs font-mono font-bold tracking-wider text-[#EDE6D6] uppercase flex items-center gap-2">
                <span class="w-2 h-2 bg-[#C1272D]"></span> Recent Operational Compliance Logs
              </h2>
              <button @click="activeMenu = 'Weekly/Monthly Logs'" class="text-[10px] font-mono font-bold text-[#C1272D] hover:underline">View All Logs →</button>
            </div>

            <div class="overflow-x-auto">
              <table class="w-full text-left font-mono text-xs">
                <thead>
                  <tr class="border-b border-[#2D2620] text-[#A89F91] text-[10px] uppercase tracking-wider">
                    <th class="pb-2 font-bold">Activity / Document</th>
                    <th class="pb-2 font-bold">Personnel Assigned</th>
                    <th class="pb-2 font-bold">Deadline</th>
                    <th class="pb-2 font-bold text-right">Status</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-[#2D2620]/60">
                  <tr v-for="log in logs" :key="log.activity" class="hover:bg-[#221B15] transition">
                    <td class="py-3 font-medium text-[#EDE6D6]">{{ log.activity }}</td>
                    <td class="py-3 text-[#A89F91]">{{ log.personnel }}</td>
                    <td class="py-3 text-[#A89F91]">{{ log.deadline }}</td>
                    <td class="py-3 text-right">
                      <span 
                        :class="[
                          'inline-block px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wider',
                          log.status === 'Pending' ? 'bg-[#E8A33D]/10 text-[#E8A33D] border border-[#E8A33D]/30' : 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/30'
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
          <div class="flex justify-between items-center bg-[#181410] p-5 rounded border border-[#2D2620]">
            <div>
              <h2 class="text-sm font-mono font-bold text-[#EDE6D6] uppercase">Station Activity Manager</h2>
              <p class="text-xs text-[#A89F91] mt-0.5">Schedule and monitor operational fire tasks and station drills.</p>
            </div>
            <button class="bg-[#C1272D] hover:bg-[#a31f24] text-[#EDE6D6] text-xs font-mono font-bold px-3.5 py-2 rounded border border-[#C1272D]/50 transition shadow">
              + Add New Activity
            </button>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div v-for="act in activityList" :key="act.title" class="bg-[#181410] border border-[#2D2620] p-4 rounded space-y-3">
              <div class="flex justify-between items-start">
                <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-[#221B15] text-[#E8A33D] border border-[#2D2620] uppercase">{{ act.type }}</span>
                <span class="text-[10px] font-mono text-[#C1272D] font-bold">{{ act.priority }} Priority</span>
              </div>
              <h3 class="font-bold text-[#EDE6D6] text-sm">{{ act.title }}</h3>
              <p class="text-xs text-[#A89F91]">Lead: {{ act.lead }}</p>
              <div class="pt-2 border-t border-[#2D2620] text-[10px] font-mono text-[#A89F91]">
                <span>📅 {{ act.date }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- PAGE 3: PERSONNEL MANAGEMENT -->
        <div v-else-if="activeMenu === 'Personnel Mgmt.'" class="space-y-6">
          <div class="flex justify-between items-center">
            <h2 class="text-sm font-mono font-bold text-[#EDE6D6] uppercase">Station Roster & Duty Details</h2>
            <input type="text" placeholder="Search officer..." class="bg-[#181410] border border-[#2D2620] rounded px-3 py-1.5 text-xs font-mono text-[#EDE6D6] focus:outline-none focus:border-[#C1272D] w-60" />
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            <div v-for="person in personnelList" :key="person.name" class="bg-[#181410] border border-[#2D2620] p-4 rounded flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="h-9 w-9 rounded bg-[#221B15] border border-[#2D2620] flex items-center justify-center font-mono font-bold text-[#C1272D] text-xs">
                  {{ person.rank }}
                </div>
                <div>
                  <h4 class="text-xs font-bold text-[#EDE6D6]">{{ person.name }}</h4>
                  <p class="text-[10px] font-mono text-[#A89F91]">{{ person.role }}</p>
                </div>
              </div>
              <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">
                {{ person.shift }} Shift
              </span>
            </div>
          </div>
        </div>

        <!-- PAGE 4: REPORT MANAGEMENT -->
        <div v-else-if="activeMenu === 'Report Mgmt.'" class="space-y-6">
          <div class="bg-[#181410] p-5 rounded border border-[#2D2620] space-y-4">
            <h2 class="text-sm font-mono font-bold text-[#EDE6D6] uppercase border-b border-[#2D2620] pb-2">Submit Official Compliance Report</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-[10px] font-mono uppercase text-[#A89F91] mb-1">Report Title</label>
                <input type="text" placeholder="e.g. Post-Fire Incident Assessment" class="w-full bg-[#120F0C] border border-[#2D2620] rounded px-3 py-2 text-xs font-mono text-[#EDE6D6] focus:outline-none focus:border-[#C1272D]" />
              </div>
              <div>
                <label class="block text-[10px] font-mono uppercase text-[#A89F91] mb-1">Assigned Inspector</label>
                <select class="w-full bg-[#120F0C] border border-[#2D2620] rounded px-3 py-2 text-xs font-mono text-[#EDE6D6] focus:outline-none focus:border-[#C1272D]">
                  <option>FO3 Juan Dela Cruz</option>
                  <option>SFO1 M. Santos</option>
                </select>
              </div>
            </div>
            <button class="bg-[#C1272D] hover:bg-[#a31f24] text-[#EDE6D6] text-xs font-mono font-bold px-4 py-2 rounded transition border border-[#C1272D]/50">
              Upload Document
            </button>
          </div>
        </div>

        <!-- PAGE 5: DEADLINE MONITOR -->
        <div v-else-if="activeMenu === 'Deadline Monitor'" class="space-y-4">
          <div class="bg-[#181410] p-5 rounded border border-[#2D2620]">
            <h2 class="text-sm font-mono font-bold text-[#EDE6D6] uppercase mb-4 border-b border-[#2D2620] pb-2">Critical Deadline Alerts</h2>
            <div class="space-y-3">
              <div class="flex items-center justify-between p-3 bg-[#C1272D]/10 border border-[#C1272D]/30 rounded">
                <div class="flex items-center gap-3">
                  <span class="text-base text-[#C1272D]">🚨</span>
                  <div>
                    <p class="font-bold text-xs text-[#EDE6D6]">After-Operation Fire Incident Report</p>
                    <p class="text-[#C1272D] text-[10px] font-mono">Overdue by 2 hours • High Escalation</p>
                  </div>
                </div>
                <button class="bg-[#C1272D] px-2.5 py-1 rounded text-[#EDE6D6] font-mono font-bold text-[10px]">Escalate</button>
              </div>
              <div class="flex items-center justify-between p-3 bg-[#E8A33D]/10 border border-[#E8A33D]/30 rounded">
                <div class="flex items-center gap-3">
                  <span class="text-base text-[#E8A33D]">⚠️</span>
                  <div>
                    <p class="font-bold text-xs text-[#EDE6D6]">Quarterly Station Equipment Inspection</p>
                    <p class="text-[#E8A33D] text-[10px] font-mono">Due in 18 Hours</p>
                  </div>
                </div>
                <button class="bg-[#E8A33D] text-[#120F0C] px-2.5 py-1 rounded font-mono font-bold text-[10px]">Notify</button>
              </div>
            </div>
          </div>
        </div>

        <!-- PAGE 6: NOTIFICATIONS -->
        <div v-else-if="activeMenu === 'Notifications'" class="space-y-4">
          <div class="bg-[#181410] p-5 rounded border border-[#2D2620]">
            <h2 class="text-sm font-mono font-bold text-[#EDE6D6] uppercase mb-4 border-b border-[#2D2620] pb-2">System Alerts</h2>
            <div class="space-y-2">
              <div v-for="n in 3" :key="n" class="p-3 bg-[#120F0C] rounded border border-[#2D2620] flex justify-between items-center text-xs">
                <div>
                  <p class="font-bold text-[#EDE6D6]">New Compliance Guidelines Published</p>
                  <p class="text-[10px] font-mono text-[#A89F91]">Regional Command • 10 mins ago</p>
                </div>
                <span class="text-[9px] font-mono font-bold text-[#C1272D] bg-[#C1272D]/10 px-2 py-0.5 rounded border border-[#C1272D]/30">UNREAD</span>
              </div>
            </div>
          </div>
        </div>

        <!-- FALLBACK SUB-PAGES -->
        <div v-else class="space-y-6">
          <div class="bg-[#181410] p-8 rounded border border-[#2D2620] text-center space-y-3">
            <svg class="w-8 h-8 fill-current text-[#C1272D] mx-auto" viewBox="0 0 24 24" v-html="getSvgPath(getActiveIcon())"></svg>
            <h2 class="text-sm font-mono font-bold text-[#EDE6D6] uppercase">{{ activeMenu }} Panel</h2>
            <p class="text-xs font-mono text-[#A89F91] max-w-md mx-auto">
              Module active. Configured for tactical operations and record tracking.
            </p>
          </div>
        </div>

      </main>
    </div>

    <!-- Log Out Confirmation Modal -->
    <div v-if="showLogoutConfirm" class="fixed inset-0 z-50 flex items-center justify-center bg-[#120F0C]/85 backdrop-blur-sm">
      <div class="w-full max-w-md rounded bg-[#181410] border border-[#2D2620] p-5 shadow-2xl space-y-4 relative overflow-hidden">
        <div class="h-1.5 w-full bg-[repeating-linear-gradient(45deg,#C1272D,#C1272D_10px,#181410_10px,#181410_20px)] absolute top-0 left-0"></div>
        
        <div class="flex items-center gap-3 pt-2">
          <div class="flex h-8 w-8 items-center justify-center rounded bg-[#C1272D]/20 border border-[#C1272D]/40 text-[#C1272D] text-sm">
            🚨
          </div>
          <div>
            <h3 class="text-sm font-mono font-bold text-[#EDE6D6] uppercase">Confirm Session Termination</h3>
            <p class="text-[10px] font-mono text-[#A89F91]">Disconnecting from station registry</p>
          </div>
        </div>
        
        <p class="text-xs text-[#A89F91] font-mono leading-relaxed bg-[#120F0C] p-3 rounded border border-[#2D2620]">
          You will be logged out of active station reporting. Unsaved report drafts will be cleared.
        </p>

        <div class="flex justify-end gap-2 pt-2">
          <button 
            @click="showLogoutConfirm = false" 
            class="rounded border border-[#2D2620] bg-[#221B15] px-3 py-1.5 text-xs font-mono text-[#A89F91] hover:text-[#EDE6D6] transition"
          >
            Cancel
          </button>
          <button 
            @click="confirmLogout" 
            class="rounded bg-[#C1272D] px-3 py-1.5 text-xs font-mono font-bold text-[#EDE6D6] hover:bg-[#a31f24] transition border border-[#C1272D]/50"
          >
            Confirm Exit
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

const ICONS = {
  dashboard: 'M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z',
  activity: 'M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11z',
  personnel: 'M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z',
  report: 'M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z',
  deadline: 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z',
  notifications: 'M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z',
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

const logs = ref([
  {
    activity: 'After-Operation Fire Incident Report',
    personnel: 'SFO1 M. Santos',
    deadline: 'Today, 17:00',
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

const getSvgPath = (key) => {
  return `<path d="${ICONS[key] || ICONS.default}"/>`
}

const getActiveIcon = () => {
  const allItems = [...menuBarItems, ...capstoneItems]
  const found = allItems.find(item => item.name === activeMenu.value)
  return found ? found.icon : 'default'
}
</script>