<template>
  <div class="relative flex h-screen w-full bg-[#15120F] text-[#D8CFC3] font-body overflow-hidden select-none bg-[radial-gradient(#3A3530_1px,transparent_1px)] [background-size:24px_24px]">

    <!-- Ambient Glow FX -->
    <div class="pointer-events-none absolute top-0 left-1/4 h-96 w-96 -translate-y-1/2 rounded-full bg-[#C1272D]/[0.08] blur-[140px]"></div>
    <div class="pointer-events-none absolute top-1/3 right-10 h-96 w-96 rounded-full bg-[#E8A33D]/[0.06] blur-[150px]"></div>

    <!-- Sidebar -->
    <aside class="w-64 flex-shrink-0 border-r border-[#3A3530] bg-[#181410] flex flex-col justify-between z-20 shadow-2xl">
      <div class="overflow-y-auto custom-scrollbar">

        <!-- Hazard Stripe Top Accent -->
        <div class="h-[5px] w-full" style="background-image: repeating-linear-gradient(135deg, #E8A33D 0 12px, #15120F 12px 24px);"></div>

        <!-- Logo Header -->
        <div class="flex items-center gap-3 px-6 py-5 border-b border-[#3A3530]/70 bg-[#141110]">
          <div class="relative flex items-center justify-center h-10 w-10 bg-[#100D0B] border border-[#C9A227]/40 rounded-sm">
            <svg viewBox="0 0 64 64" class="h-7 w-7 shrink-0" fill="none">
              <path d="M32 4 L58 13 V29 C58 45 47 55 32 60 C17 55 6 45 6 29 V13 Z" stroke="#C9A227" stroke-width="2.5" fill="#100D0B"/>
              <path d="M32 20c-4.5 4.5-7 8.2-7 12.2 0 4.4 3.3 7.8 7.4 7.8 4.5 0 7.9-3.2 7.9-7.5 0-2.2-.9-3.9-2.3-5.6.1 1.7-.5 2.9-1.6 3.7.3-2.9-.7-6.4-4.4-10.6Z" fill="#C9A227"/>
            </svg>
          </div>
          <div>
            <span class="block -mb-1 font-mono text-[9px] font-bold uppercase tracking-[0.25em] text-[#E8A33D]">Personnel Portal</span>
            <span class="font-display text-lg font-bold tracking-[0.08em] text-[#EDE6D6]">FIRE<span class="text-[#C1272D]">NOTIFY</span></span>
          </div>
        </div>

        <!-- Navigation Sections -->
        <div class="px-3 py-4 space-y-6">

          <!-- Section 1 -->
          <div>
            <p class="px-3 mb-2 font-mono text-[9px] font-bold uppercase tracking-[0.28em] text-[#6E645A]">Field Duty</p>
            <nav class="space-y-1">
              <button
                v-for="item in fieldItems"
                :key="item.name"
                @click="activeTab = item.name"
                :title="item.context"
                :class="[
                  'group relative w-full flex items-center justify-between rounded-sm pl-3 pr-3 py-2.5 text-xs font-medium transition-all duration-150 border-l-2',
                  activeTab === item.name
                    ? 'bg-[#211B16] text-[#EDE6D6] border-[#C1272D] shadow-inner'
                    : 'text-[#9A9086] border-transparent hover:bg-[#1D1814] hover:text-[#D8CFC3]'
                ]"
              >
                <div class="flex items-center gap-3 min-w-0">
                  <span
                    v-html="ICONS[item.icon]"
                    :class="['h-4 w-4 shrink-0 transition-colors', activeTab === item.name ? 'text-[#E8A33D]' : 'text-[#7A6F63] group-hover:text-[#9A9086]']"
                  ></span>
                  <div class="text-left min-w-0">
                    <span class="block truncate font-semibold">{{ item.name }}</span>
                    <span class="block truncate font-mono text-[9px] text-[#5A5148]">{{ item.context }}</span>
                  </div>
                </div>
                <span
                  v-if="item.badge"
                  class="ml-2 shrink-0 rounded-xs border border-[#C1272D]/40 bg-[#C1272D]/10 px-1.5 py-0.5 font-mono text-[9px] font-bold text-[#E4595E]"
                >{{ item.badge }}</span>
              </button>
            </nav>
          </div>

          <!-- Section 2 -->
          <div>
            <p class="px-3 mb-2 font-mono text-[9px] font-bold uppercase tracking-[0.28em] text-[#6E645A]">Management & Records</p>
            <nav class="space-y-1">
              <button
                v-for="item in managementItems"
                :key="item.name"
                @click="activeTab = item.name"
                :title="item.context"
                :class="[
                  'group relative w-full flex items-center gap-3 rounded-sm pl-3 pr-3 py-2.5 text-xs font-medium transition-all duration-150 border-l-2',
                  activeTab === item.name
                    ? 'bg-[#211B16] text-[#EDE6D6] border-[#C1272D] shadow-inner'
                    : 'text-[#9A9086] border-transparent hover:bg-[#1D1814] hover:text-[#D8CFC3]'
                ]"
              >
                <span
                  v-html="ICONS[item.icon]"
                  :class="['h-4 w-4 shrink-0 transition-colors', activeTab === item.name ? 'text-[#E8A33D]' : 'text-[#7A6F63] group-hover:text-[#9A9086]']"
                ></span>
                <div class="text-left min-w-0">
                  <span class="block truncate font-semibold">{{ item.name }}</span>
                  <span class="block truncate font-mono text-[9px] text-[#5A5148]">{{ item.context }}</span>
                </div>
              </button>
            </nav>
          </div>

          <!-- Section 3 -->
          <div>
            <p class="px-3 mb-2 font-mono text-[9px] font-bold uppercase tracking-[0.28em] text-[#6E645A]">Personnel Tools</p>
            <nav class="space-y-1">
              <button
                v-for="item in toolItems"
                :key="item.name"
                @click="activeTab = item.name"
                :title="item.context"
                :class="[
                  'group relative w-full flex items-center gap-3 rounded-sm pl-3 pr-3 py-2.5 text-xs font-medium transition-all duration-150 border-l-2',
                  activeTab === item.name
                    ? 'bg-[#211B16] text-[#EDE6D6] border-[#C1272D] shadow-inner'
                    : 'text-[#9A9086] border-transparent hover:bg-[#1D1814] hover:text-[#D8CFC3]'
                ]"
              >
                <span
                  v-html="ICONS[item.icon]"
                  :class="['h-4 w-4 shrink-0 transition-colors', activeTab === item.name ? 'text-[#E8A33D]' : 'text-[#7A6F63] group-hover:text-[#9A9086]']"
                ></span>
                <div class="text-left min-w-0">
                  <span class="block truncate font-semibold">{{ item.name }}</span>
                  <span class="block truncate font-mono text-[9px] text-[#5A5148]">{{ item.context }}</span>
                </div>
              </button>
            </nav>
          </div>

        </div>
      </div>

      <!-- Profile & Sign Out Footer -->
      <div class="p-3 border-t border-[#3A3530] bg-[#141110] space-y-2">
        <div class="flex items-center gap-3 p-2 rounded-sm bg-[#1D1814] border border-[#3A3530]">
          <div class="h-8 w-8 rounded-xs bg-[#C1272D] flex items-center justify-center font-mono font-bold text-[#EDE6D6] text-[10px] shrink-0 border border-[#E4595E]/30">
            {{ currentUser?.rank || 'FO3' }}
          </div>
          <div class="overflow-hidden">
            <p class="text-xs font-semibold text-[#EDE6D6] truncate">{{ currentUser?.firstName || 'Juan' }} {{ currentUser?.lastName || 'Dela Cruz' }}</p>
            <p class="font-mono text-[9px] uppercase tracking-wider text-[#6E645A] truncate">Station Inspector</p>
          </div>
        </div>

        <button
          @click="showLogoutConfirm = true"
          class="w-full flex items-center justify-between px-3 py-2 rounded-sm text-xs font-semibold text-[#9A9086] hover:text-[#E4595E] hover:bg-[#C1272D]/[0.12] border border-transparent hover:border-[#C1272D]/30 transition-all duration-150 group"
        >
          <div class="flex items-center gap-2.5">
            <span v-html="ICONS.logout" class="h-3.5 w-3.5 text-[#7A6F63] group-hover:text-[#E4595E]"></span>
            <span>Sign Out</span>
          </div>
          <span class="font-mono text-[9px] uppercase tracking-widest text-[#5A5148] group-hover:text-[#E4595E]">Exit</span>
        </button>
      </div>
    </aside>

    <!-- Main Workspace -->
    <div class="flex-1 flex flex-col overflow-y-auto z-10 custom-scrollbar">

      <!-- Top Header -->
      <header class="h-16 border-b border-[#3A3530] bg-[#181410]/95 backdrop-blur-md px-8 flex items-center justify-between sticky top-0 z-30">
        <div>
          <p class="font-mono text-[9px] uppercase tracking-[0.25em] text-[#6E645A]">Operations Control</p>
          <h1 class="font-display text-lg font-bold tracking-wide text-[#EDE6D6] uppercase">{{ activeTab }}</h1>
        </div>

        <div class="flex items-center gap-4">
          <div class="flex items-center gap-2 rounded-xs border border-[#7BA88A]/30 bg-[#7BA88A]/[0.08] px-3 py-1.5">
            <span class="relative flex h-2 w-2">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#7BA88A]/60"></span>
              <span class="relative inline-flex rounded-full h-2 w-2 bg-[#7BA88A]"></span>
            </span>
            <span class="font-mono text-[10px] font-semibold uppercase tracking-[0.15em] text-[#9BC1A6]">On Duty · Station 1</span>
          </div>

          <button @click="activeTab = 'Notifications'" class="relative rounded-sm p-2 text-[#9A9086] hover:bg-[#211B16] hover:text-[#EDE6D6] border border-transparent hover:border-[#3A3530] transition-all">
            <span v-html="ICONS.bell" class="block h-4 w-4"></span>
            <span class="absolute top-1.5 right-1.5 h-1.5 w-1.5 rounded-full bg-[#C1272D]"></span>
          </button>
        </div>
      </header>

      <!-- Dashboard Viewport -->
      <main class="p-8 space-y-6">

        <!-- Tactical Metric Cards -->
        <section class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div class="relative rounded-sm border border-[#3A3530] bg-[#181410] p-5 border-t-2 border-t-[#E8A33D] shadow-lg">
            <div class="flex justify-between items-start">
              <p class="font-mono text-[10px] font-bold uppercase tracking-[0.2em] text-[#7A6F63]">Assigned Tasks</p>
              <span v-html="ICONS.tasks" class="h-4 w-4 text-[#7A6F63]"></span>
            </div>
            <p class="mt-3 font-display text-4xl font-bold text-[#EDE6D6]">09</p>
            <p class="mt-1 font-mono text-[10px] font-semibold text-[#7BA88A]">4 urgent pending</p>
          </div>

          <div class="relative rounded-sm border border-[#3A3530] bg-[#181410] p-5 border-t-2 border-t-[#E8A33D] shadow-lg">
            <div class="flex justify-between items-start">
              <p class="font-mono text-[10px] font-bold uppercase tracking-[0.2em] text-[#7A6F63]">Pending Reports</p>
              <span v-html="ICONS.reports" class="h-4 w-4 text-[#7A6F63]"></span>
            </div>
            <p class="mt-3 font-display text-4xl font-bold text-[#E8A33D]">03</p>
            <p class="mt-1 font-mono text-[10px] font-semibold text-[#E8A33D]/90">Submission needed</p>
          </div>

          <div class="relative rounded-sm border border-[#3A3530] bg-[#181410] p-5 border-t-2 border-t-[#C1272D] shadow-lg">
            <div class="flex justify-between items-start">
              <p class="font-mono text-[10px] font-bold uppercase tracking-[0.2em] text-[#7A6F63]">Station Alerts</p>
              <span v-html="ICONS.siren" class="h-4 w-4 text-[#C1272D]"></span>
            </div>
            <p class="mt-3 font-display text-4xl font-bold text-[#E4595E]">02</p>
            <p class="mt-1 font-mono text-[10px] font-semibold text-[#E4595E]/90">Requires immediate response</p>
          </div>
        </section>

        <!-- Dynamic Main Section -->
        <section class="grid grid-cols-1 lg:grid-cols-3 gap-6">

          <div class="lg:col-span-2 space-y-6">

            <!-- Tab: Dashboard -->
            <div v-if="activeTab === 'Dashboard'" class="rounded-sm border border-[#3A3530] bg-[#181410] p-6 space-y-4 shadow-xl">
              <div class="flex items-center justify-between border-b border-[#3A3530] pb-4">
                <h2 class="font-display text-base font-bold text-[#EDE6D6] uppercase tracking-wide">Active Operational Workflows</h2>
                <button @click="activeTab = 'Tasks'" class="font-mono text-[10px] uppercase tracking-wider font-bold text-[#E8A33D] hover:text-[#f0b45c] transition-colors">View All →</button>
              </div>

              <div class="space-y-2.5">
                <div class="flex items-center justify-between rounded-sm border border-[#3A3530] bg-[#100D0B] p-4 text-xs">
                  <div class="flex items-center gap-3">
                    <span v-html="ICONS.check" class="h-4 w-4 text-[#7BA88A] shrink-0"></span>
                    <div>
                      <p class="font-semibold text-[#D8CFC3]">Routine Safety Patrol</p>
                      <p class="font-mono text-[9px] text-[#6E645A] mt-0.5">Zone 2 Commercial Area</p>
                    </div>
                  </div>
                  <span class="px-2 py-1 rounded-xs font-mono text-[9px] font-bold uppercase tracking-wider bg-[#7BA88A]/10 text-[#7BA88A] border border-[#7BA88A]/30">Completed</span>
                </div>

                <div class="flex items-center justify-between rounded-sm border border-[#3A3530] bg-[#100D0B] p-4 text-xs">
                  <div class="flex items-center gap-3">
                    <span v-html="ICONS.clock" class="h-4 w-4 text-[#E8A33D] shrink-0"></span>
                    <div>
                      <p class="font-semibold text-[#D8CFC3]">Fire Hazard Inspection</p>
                      <p class="font-mono text-[9px] text-[#6E645A] mt-0.5">Public Market Complex</p>
                    </div>
                  </div>
                  <span class="px-2 py-1 rounded-xs font-mono text-[9px] font-bold uppercase tracking-wider bg-[#E8A33D]/10 text-[#E8A33D] border border-[#E8A33D]/30">In Progress</span>
                </div>

                <div class="flex items-center justify-between rounded-sm border border-[#C1272D]/30 bg-[#100D0B] p-4 text-xs">
                  <div class="flex items-center gap-3">
                    <span v-html="ICONS.siren" class="h-4 w-4 text-[#E4595E] shrink-0"></span>
                    <div>
                      <p class="font-semibold text-[#D8CFC3]">Post-Operation Incident Assessment</p>
                      <p class="font-mono text-[9px] text-[#6E645A] mt-0.5">Subdivision Sector 4</p>
                    </div>
                  </div>
                  <span class="px-2 py-1 rounded-xs font-mono text-[9px] font-bold uppercase tracking-wider bg-[#C1272D]/10 text-[#E4595E] border border-[#C1272D]/30">Urgent</span>
                </div>
              </div>
            </div>

            <!-- Tab: Tasks -->
            <div v-else-if="activeTab === 'Tasks'" class="rounded-sm border border-[#3A3530] bg-[#181410] p-6 space-y-4 shadow-xl">
              <h2 class="font-display text-base font-bold text-[#EDE6D6] uppercase tracking-wide border-b border-[#3A3530] pb-4">Assigned Personnel Tasks</h2>
              <div class="space-y-2.5">
                <div v-for="task in taskList" :key="task.title" class="flex items-center justify-between rounded-sm border border-[#3A3530] bg-[#100D0B] p-4 text-xs">
                  <div>
                    <p class="font-semibold text-[#D8CFC3]">{{ task.title }}</p>
                    <p class="font-mono text-[9px] text-[#6E645A] mt-0.5">Due: {{ task.due }}</p>
                  </div>
                  <button class="bg-[#211B16] hover:bg-[#2A231D] text-[#D8CFC3] font-mono text-[9px] font-bold uppercase tracking-wider px-3 py-1.5 rounded-xs border border-[#3A3530] transition-colors">
                    Update Status
                  </button>
                </div>
              </div>
            </div>

            <!-- Tab: Reports -->
            <div v-else-if="activeTab === 'Reports'" class="rounded-sm border border-[#3A3530] bg-[#181410] p-6 space-y-4 shadow-xl">
              <h2 class="font-display text-base font-bold text-[#EDE6D6] uppercase tracking-wide border-b border-[#3A3530] pb-4">Incident & Operational Submissions</h2>
              <div class="space-y-2.5">
                <div class="flex items-center justify-between rounded-sm border border-[#C1272D]/30 bg-[#100D0B] p-4 text-xs">
                  <div>
                    <p class="font-semibold text-[#D8CFC3]">Incident Report #1047</p>
                    <p class="font-mono text-[9px] text-[#6E645A] mt-0.5">Submitted by: FO3 J. Dela Cruz</p>
                  </div>
                  <span class="px-2 py-1 rounded-xs font-mono text-[9px] font-bold uppercase tracking-wider bg-[#C1272D]/10 text-[#E4595E] border border-[#C1272D]/30">Pending Review</span>
                </div>
              </div>
            </div>

            <!-- Tab: Personnel Roster -->
            <div v-else-if="activeTab === 'Personnel Roster'" class="rounded-sm border border-[#3A3530] bg-[#181410] p-6 space-y-4 shadow-xl">
              <h2 class="font-display text-base font-bold text-[#EDE6D6] uppercase tracking-wide border-b border-[#3A3530] pb-4">Active Station Roster</h2>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                <div v-for="person in roster" :key="person.name" class="p-3 bg-[#100D0B] border border-[#3A3530] rounded-sm flex items-center gap-3">
                  <div class="h-9 w-9 rounded-xs bg-[#211B16] border border-[#3A3530] flex items-center justify-center font-mono font-bold text-[#E8A33D] text-[10px] shrink-0">
                    {{ person.rank }}
                  </div>
                  <div>
                    <p class="text-xs font-semibold text-[#EDE6D6]">{{ person.name }}</p>
                    <p class="font-mono text-[9px] text-[#6E645A] mt-0.5">{{ person.role }} · {{ person.shift }}</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Fallback Blank View -->
            <div v-else class="rounded-sm border border-[#3A3530] bg-[#181410] p-12 text-center space-y-3 shadow-xl">
              <span v-html="ICONS[getActiveIcon()]" class="mx-auto block h-10 w-10 text-[#7A6F63]"></span>
              <h2 class="font-display text-xl font-bold text-[#EDE6D6] uppercase tracking-wider">{{ activeTab }}</h2>
              <p class="text-xs text-[#9A9086] max-w-md mx-auto leading-relaxed">
                Module active for station personnel. Real-time controls for <span class="text-[#E8A33D] font-mono">{{ activeTab }}</span> are currently synced with dispatch.
              </p>
            </div>

          </div>

          <!-- Live Feeds Sidebar -->
          <div class="rounded-sm border border-[#3A3530] bg-[#181410] p-6 space-y-4 shadow-xl">
            <div class="flex items-center justify-between border-b border-[#3A3530] pb-3">
              <h3 class="font-display text-sm font-bold text-[#EDE6D6] uppercase tracking-wide">Live Station Feeds</h3>
              <span class="font-mono text-[9px] uppercase tracking-wider text-[#6E645A]">Real-time</span>
            </div>

            <div class="space-y-2.5 text-xs">
              <div class="rounded-sm border border-[#3A3530] border-l-2 border-l-[#E8A33D] bg-[#100D0B] p-3.5">
                <p class="font-semibold text-[11px] text-[#E8A33D]">Morning Briefing</p>
                <p class="text-[10px] text-[#9A9086] mt-1 leading-relaxed">Station shift change and equipment check completed at 08:00 AM.</p>
              </div>

              <div class="rounded-sm border border-[#3A3530] border-l-2 border-l-[#C1272D] bg-[#100D0B] p-3.5">
                <p class="font-semibold text-[11px] text-[#E4595E]">Escalation Warning</p>
                <p class="text-[10px] text-[#9A9086] mt-1 leading-relaxed">Maintenance request #202 waiting for inspector approval.</p>
              </div>

              <div class="rounded-sm border border-[#3A3530] border-l-2 border-l-[#7BA88A] bg-[#100D0B] p-3.5">
                <p class="font-semibold text-[11px] text-[#7BA88A]">Safety Clearance</p>
                <p class="text-[10px] text-[#9A9086] mt-1 leading-relaxed">Quarterly safety seminar training verified and logged in system.</p>
              </div>
            </div>
          </div>

        </section>

      </main>
    </div>

    <!-- Sign Out Tactical Modal -->
    <div v-if="showLogoutConfirm" class="fixed inset-0 z-50 flex items-center justify-center bg-[#0A0806]/85 backdrop-blur-md transition-opacity">
      <div class="w-full max-w-md overflow-hidden rounded-sm border border-[#3A3530] bg-[#181410] shadow-2xl">
        <div class="h-[5px] w-full" style="background-image: repeating-linear-gradient(135deg, #E8A33D 0 12px, #15120F 12px 24px);"></div>
        <div class="p-6 space-y-4">
          <div class="flex items-center gap-3">
            <div class="flex h-10 w-10 items-center justify-center rounded-xs bg-[#C1272D]/10 border border-[#C1272D]/30 shrink-0">
              <span v-html="ICONS.siren" class="h-5 w-5 text-[#E4595E]"></span>
            </div>
            <div>
              <h3 class="font-display text-lg font-bold text-[#EDE6D6] uppercase tracking-wide">Confirm Sign Out</h3>
              <p class="text-xs text-[#9A9086] mt-0.5">Are you sure you want to exit the Personnel Portal?</p>
            </div>
          </div>

          <p class="text-xs text-[#9A9086] leading-relaxed bg-[#100D0B] p-3 rounded-xs border border-[#3A3530]">
            Unsaved changes in active forms or field logs may be lost upon signing out.
          </p>

          <div class="flex justify-end gap-3 pt-2">
            <button
              @click="showLogoutConfirm = false"
              class="rounded-xs border border-[#3A3530] bg-[#211B16] px-4 py-2 text-xs font-bold uppercase tracking-wider text-[#D8CFC3] hover:bg-[#2A231D] transition-colors"
            >
              Cancel
            </button>
            <button
              @click="confirmLogout"
              class="rounded-xs bg-[#C1272D] px-4 py-2 text-xs font-bold uppercase tracking-wider text-[#EDE6D6] hover:bg-[#A82126] transition-colors shadow-md"
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

const ICONS = {
  dashboard: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/></svg>',
  tasks: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 2.5h6a1 1 0 011 1V5H8V3.5a1 1 0 011-1z"/><path d="M9 11h6M9 15h6"/></svg>',
  reports: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><path d="M14 2v6h6"/><path d="M9 13h6M9 17h6"/></svg>',
  notifications: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M18 8a6 6 0 10-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 01-3.46 0"/></svg>',
  bell: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M18 8a6 6 0 10-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 01-3.46 0"/></svg>',
  roster: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>',
  dutylog: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>',
  equipment: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg>',
  support: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M3 18v-6a9 9 0 0118 0v6"/><path d="M21 19a2 2 0 01-2 2h-1a2 2 0 01-2-2v-3a2 2 0 012-2h3zM3 19a2 2 0 002 2h1a2 2 0 002-2v-3a2 2 0 00-2-2H3z"/></svg>',
  settings: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 11-2.83 2.83l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-4 0v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 11-2.83-2.83l.06-.06a1.65 1.65 0 00.33-1.82 1.65 1.65 0 00-1.51-1H3a2 2 0 010-4h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 112.83-2.83l.06.06a1.65 1.65 0 001.82.33H9a1.65 1.65 0 001-1.51V3a2 2 0 014 0v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 112.83 2.83l-.06.06a1.65 1.65 0 00-.33 1.82V9a1.65 1.65 0 001.51 1H21a2 2 0 010 4h-.09a1.65 1.65 0 00-1.51 1z"/></svg>',
  logout: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M9 21H5a2 2 0 01-2-2V5a2 2 0 012-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/></svg>',
  siren: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
  check: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
  clock: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
  pin: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M12 21s7-6.8 7-12a7 7 0 10-14 0c0 5.2 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>'
}

const fieldItems = [
  { name: 'Dashboard', icon: 'dashboard', context: 'Operations overview', badge: null },
  { name: 'Tasks', icon: 'tasks', context: 'Assigned activities', badge: '4' },
  { name: 'Reports', icon: 'reports', context: 'Submit accomplishment reports', badge: '3' },
  { name: 'Notifications', icon: 'notifications', context: 'Deadlines & station alerts', badge: '3' }
]

const managementItems = [
  { name: 'Personnel Roster', icon: 'roster', context: 'View station personnel' },
  { name: 'Station Duty Log', icon: 'dutylog', context: 'Track duty & shift records' },
  { name: 'Equipment Audit', icon: 'equipment', context: 'Monitor equipment status' }
]

const toolItems = [
  { name: 'Support', icon: 'support', context: 'Get system assistance' },
  { name: 'Settings', icon: 'settings', context: 'Account & preferences' }
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
  return found ? found.icon : 'pin'
}
</script>

<style scoped>
.font-display { font-family: 'Oswald', 'Arial Narrow', sans-serif; }
.font-body { font-family: 'IBM Plex Sans', 'Helvetica Neue', sans-serif; }
.font-mono { font-family: 'IBM Plex Mono', 'SFMono-Regular', monospace; }

/* Custom Scrollbar */
.custom-scrollbar::-webkit-scrollbar {
  width: 5px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: #15120F;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #3A3530;
  border-radius: 2px;
}
.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: #E8A33D;
}
</style>