<template>
  <div class="min-h-screen bg-slate-950 text-slate-100">
    <div class="mx-auto flex max-w-7xl gap-6 px-4 py-6">
      <aside class="w-72 shrink-0 rounded-2xl border border-slate-800 bg-slate-900/80 p-4 shadow-2xl">
        <div class="mb-6 flex items-center justify-between">
          <div>
            <div class="text-[10px] uppercase tracking-[0.35em] text-slate-500">System</div>
            <h1 class="mt-2 text-xl font-bold">FireNotify</h1>
          </div>
          <button @click="showLogoutConfirm = true" class="rounded-lg border border-red-500/30 bg-red-500/10 px-2 py-1 text-xs text-red-300">Logout</button>
        </div>

        <div class="space-y-5">
          <div>
            <p class="mb-2 text-[10px] uppercase tracking-[0.25em] text-slate-500">Overview</p>
            <nav class="space-y-1">
              <button v-for="item in overviewItems" :key="item.label" @click="activeTab = item.label" :class="['w-full rounded-xl px-3 py-2 text-left text-sm transition', activeTab === item.label ? 'bg-red-600 text-white' : 'text-slate-300 hover:bg-slate-800']">
                {{ item.label }}
              </button>
            </nav>
          </div>

          <div>
            <p class="mb-2 text-[10px] uppercase tracking-[0.25em] text-slate-500">Operations</p>
            <nav class="space-y-1">
              <button v-for="item in operationsItems" :key="item.label" @click="activeTab = item.label" :class="['w-full rounded-xl px-3 py-2 text-left text-sm transition', activeTab === item.label ? 'bg-red-600 text-white' : 'text-slate-300 hover:bg-slate-800']">
                {{ item.label }}
              </button>
            </nav>
          </div>

          <div>
            <p class="mb-2 text-[10px] uppercase tracking-[0.25em] text-slate-500">Administration</p>
            <nav class="space-y-1">
              <button v-for="item in adminItems" :key="item.label" @click="activeTab = item.label" :class="['w-full rounded-xl px-3 py-2 text-left text-sm transition', activeTab === item.label ? 'bg-red-600 text-white' : 'text-slate-300 hover:bg-slate-800']">
                {{ item.label }}
              </button>
            </nav>
          </div>
        </div>
      </aside>

      <main class="flex-1 rounded-2xl border border-slate-800 bg-slate-900/80 p-6 shadow-2xl">
        <header class="mb-6 flex items-center justify-between border-b border-slate-800 pb-4">
          <div>
            <p class="text-[10px] uppercase tracking-[0.35em] text-slate-500">Admin</p>
            <h2 class="text-2xl font-bold text-white">{{ activeTab }}</h2>
          </div>
          <div class="rounded-full border border-slate-700 bg-slate-950/80 px-3 py-1 text-sm text-slate-200">
            {{ currentUser?.firstName || 'Admin' }} {{ currentUser?.lastName || '' }}
          </div>
        </header>

        <div class="grid gap-4 md:grid-cols-3">
          <div class="rounded-2xl border border-slate-800 bg-slate-950/80 p-4">
            <p class="text-sm text-slate-400">Active Incidents</p>
            <p class="mt-2 text-3xl font-bold text-white">24</p>
          </div>
          <div class="rounded-2xl border border-slate-800 bg-slate-950/80 p-4">
            <p class="text-sm text-slate-400">Report Compliance</p>
            <p class="mt-2 text-3xl font-bold text-white">96%</p>
          </div>
          <div class="rounded-2xl border border-slate-800 bg-slate-950/80 p-4">
            <p class="text-sm text-slate-400">Response Time</p>
            <p class="mt-2 text-3xl font-bold text-white">14m</p>
          </div>
        </div>

        <div class="mt-6 grid gap-6 xl:grid-cols-[2fr_1fr]">
          <div class="rounded-2xl border border-slate-800 bg-slate-950/80 p-5">
            <div class="mb-3 flex items-center justify-between">
              <h3 class="text-lg font-semibold text-white">Operations Summary</h3>
              <span class="text-xs uppercase tracking-[0.2em] text-emerald-300">Live</span>
            </div>
            <div class="space-y-3">
              <div class="rounded-xl border border-slate-800 bg-slate-900 p-3">
                <div class="flex justify-between text-sm">
                  <span class="text-slate-300">Fire Safety Checks</span>
                  <span class="text-white font-semibold">82% complete</span>
                </div>
              </div>
              <div class="rounded-xl border border-slate-800 bg-slate-900 p-3">
                <div class="flex justify-between text-sm">
                  <span class="text-slate-300">Personnel Availability</span>
                  <span class="text-white font-semibold">91% ready</span>
                </div>
              </div>
              <div class="rounded-xl border border-slate-800 bg-slate-900 p-3">
                <div class="flex justify-between text-sm">
                  <span class="text-slate-300">Inspection Backlog</span>
                  <span class="text-white font-semibold">7 pending</span>
                </div>
              </div>
            </div>
          </div>

          <div class="rounded-2xl border border-slate-800 bg-slate-950/80 p-5">
            <h3 class="text-lg font-semibold text-white">Alerts</h3>
            <div class="mt-4 space-y-3">
              <div class="rounded-xl border border-amber-500/30 bg-amber-500/10 p-3 text-sm text-amber-200">High priority inspection needed in Sector 4.</div>
              <div class="rounded-xl border border-red-500/30 bg-red-500/10 p-3 text-sm text-red-200">Equipment maintenance overdue in Station 2.</div>
              <div class="rounded-xl border border-emerald-500/30 bg-emerald-500/10 p-3 text-sm text-emerald-200">Two units are now fully deployed and operational.</div>
            </div>
          </div>
        </div>
      </main>
    </div>

    <div v-if="showLogoutConfirm" class="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/80 backdrop-blur-sm">
      <div class="w-full max-w-md rounded-2xl border border-slate-700 bg-slate-900 p-6 shadow-2xl">
        <h3 class="text-xl font-bold text-white">Are you sure you want to log out?</h3>
        <p class="mt-2 text-sm text-slate-400">Your current session will end and you will be returned to the login screen.</p>
        <div class="mt-6 flex justify-end gap-3">
          <button @click="showLogoutConfirm = false" class="rounded-xl border border-slate-700 bg-slate-800 px-4 py-2 text-sm text-slate-200">No</button>
          <button @click="confirmLogout" class="rounded-xl bg-red-600 px-4 py-2 text-sm font-semibold text-white">Yes</button>
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

const overviewItems = ['Overview', 'Dashboard', 'Reports']
const operationsItems = ['Incidents', 'Units', 'Inspections', 'Dispatch']
const adminItems = ['Users', 'Audit Logs', 'Settings', 'Permissions']

const activeTab = ref('Overview')
const showLogoutConfirm = ref(false)

const confirmLogout = () => {
  showLogoutConfirm.value = false
  emit('logout')
}
</script>
