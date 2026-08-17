<template>
  <div class="min-h-screen bg-slate-950 text-slate-100">
    <div class="mx-auto max-w-7xl px-4 py-6">
      <header class="mb-6 flex items-center justify-between rounded-2xl border border-slate-800 bg-slate-900/80 p-4 shadow-2xl">
        <div>
          <p class="text-[10px] uppercase tracking-[0.35em] text-slate-500">Personnel Portal</p>
          <h1 class="mt-2 text-2xl font-bold text-white">Welcome, {{ currentUser?.firstName || 'Officer' }}</h1>
        </div>
        <button @click="showLogoutConfirm = true" class="rounded-xl border border-red-500/30 bg-red-500/10 px-3 py-2 text-sm text-red-200">Logout</button>
      </header>

      <div class="grid gap-6 xl:grid-cols-[260px_1fr]">
        <aside class="rounded-2xl border border-slate-800 bg-slate-900/80 p-4 shadow-2xl">
          <p class="mb-3 text-[10px] uppercase tracking-[0.25em] text-slate-500">Navigation</p>
          <nav class="space-y-2">
            <button v-for="item in navItems" :key="item" @click="activeTab = item" :class="['w-full rounded-xl px-3 py-2 text-left text-sm transition', activeTab === item ? 'bg-red-600 text-white' : 'text-slate-300 hover:bg-slate-800']">
              {{ item }}
            </button>
          </nav>
        </aside>

        <main class="space-y-6">
          <section class="grid gap-4 md:grid-cols-3">
            <div class="rounded-2xl border border-slate-800 bg-slate-900/80 p-4">
              <p class="text-sm text-slate-400">Assigned Tasks</p>
              <p class="mt-2 text-3xl font-bold text-white">9</p>
            </div>
            <div class="rounded-2xl border border-slate-800 bg-slate-900/80 p-4">
              <p class="text-sm text-slate-400">Pending Reports</p>
              <p class="mt-2 text-3xl font-bold text-white">3</p>
            </div>
            <div class="rounded-2xl border border-slate-800 bg-slate-900/80 p-4">
              <p class="text-sm text-slate-400">Alerts</p>
              <p class="mt-2 text-3xl font-bold text-white">2</p>
            </div>
          </section>

          <section class="grid gap-6 xl:grid-cols-[1.5fr_1fr]">
            <div class="rounded-2xl border border-slate-800 bg-slate-900/80 p-5">
              <h2 class="mb-4 text-xl font-bold text-white">{{ activeTab }}</h2>

              <div v-if="activeTab === 'Dashboard'" class="space-y-3">
                <div class="rounded-xl border border-slate-800 bg-slate-950 p-3">
                  <div class="flex justify-between text-sm">
                    <span class="text-slate-300">Routine patrol</span>
                    <span class="text-emerald-300">Completed</span>
                  </div>
                </div>
                <div class="rounded-xl border border-slate-800 bg-slate-950 p-3">
                  <div class="flex justify-between text-sm">
                    <span class="text-slate-300">Fire hazard inspection</span>
                    <span class="text-amber-300">In progress</span>
                  </div>
                </div>
              </div>

              <div v-else-if="activeTab === 'Tasks'" class="space-y-3">
                <div class="rounded-xl border border-slate-800 bg-slate-950 p-3">
                  <div class="flex justify-between text-sm">
                    <span class="text-slate-300">Check hydrant systems</span>
                    <span class="text-slate-400">Today</span>
                  </div>
                </div>
                <div class="rounded-xl border border-slate-800 bg-slate-950 p-3">
                  <div class="flex justify-between text-sm">
                    <span class="text-slate-300">Submit incident log</span>
                    <span class="text-slate-400">Tomorrow</span>
                  </div>
                </div>
              </div>

              <div v-else-if="activeTab === 'Reports'" class="space-y-3">
                <div class="rounded-xl border border-slate-800 bg-slate-950 p-3">
                  <div class="flex justify-between text-sm">
                    <span class="text-slate-300">Incident report #1047</span>
                    <span class="text-red-300">Pending</span>
                  </div>
                </div>
              </div>

              <div v-else class="rounded-xl border border-slate-800 bg-slate-950 p-3 text-sm text-slate-300">
                No item selected yet.
              </div>
            </div>

            <div class="rounded-2xl border border-slate-800 bg-slate-900/80 p-5">
              <h3 class="text-lg font-semibold text-white">Notifications</h3>
              <div class="mt-4 space-y-3 text-sm">
                <div class="rounded-xl border border-amber-500/30 bg-amber-500/10 p-3 text-amber-200">Station briefing at 08:00 AM.</div>
                <div class="rounded-xl border border-red-500/30 bg-red-500/10 p-3 text-red-200">Maintenance request waiting approval.</div>
                <div class="rounded-xl border border-emerald-500/30 bg-emerald-500/10 p-3 text-emerald-200">Safety training completed.</div>
              </div>
            </div>
          </section>
        </main>
      </div>
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

const navItems = ['Dashboard', 'Tasks', 'Reports', 'Notifications', 'Support']
const activeTab = ref('Dashboard')
const showLogoutConfirm = ref(false)

const confirmLogout = () => {
  showLogoutConfirm.value = false
  emit('logout')
}
</script>
