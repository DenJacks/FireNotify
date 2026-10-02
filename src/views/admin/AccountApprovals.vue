<template>
  <section class="space-y-6">
    <div class="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
      <div class="flex flex-col gap-3 md:flex-row md:items-center md:justify-between">
        <div>
          <p class="text-sm font-semibold uppercase tracking-[0.12em] text-[#8B1E23]">
            Personnel approvals
          </p>
          <h2 class="mt-1 text-2xl font-bold text-slate-900">
            Personnel accounts
          </h2>
        </div>

        <div class="inline-flex items-center gap-2 rounded-full bg-amber-50 px-3 py-2 text-sm font-semibold text-amber-800 border border-amber-200">
          <span class="h-2.5 w-2.5 rounded-full bg-amber-500"></span>
          {{ pendingCount }} awaiting review
        </div>
      </div>
    </div>

    <div v-if="loading" class="rounded-2xl border border-slate-200 bg-white p-8 text-slate-500 shadow-sm">
      Loading personnel accounts...
    </div>

    <div v-else-if="personnelUsers.length === 0" class="rounded-2xl border border-dashed border-slate-300 bg-white p-8 text-center text-slate-500 shadow-sm">
      No personnel accounts found.
    </div>

    <div v-else class="space-y-4">
      <div v-if="approvalConfirmation" class="rounded-xl border border-emerald-200 bg-emerald-50 px-4 py-3 text-sm font-medium text-emerald-800">
        ✓ You approved {{ approvalConfirmation }}
      </div>

      <div class="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-slate-200 text-left text-sm">
            <thead class="bg-slate-50 text-slate-600">
              <tr>
                <th class="px-5 py-3 font-semibold">Full Name</th>
                <th class="px-5 py-3 font-semibold">Badge Number</th>
                <th class="px-5 py-3 font-semibold">Rank</th>
                <th class="px-5 py-3 font-semibold">Email</th>
                <th class="px-5 py-3 font-semibold">Username</th>
                <th class="px-5 py-3 font-semibold">Status</th>
                <th class="px-5 py-3 font-semibold text-right">Action</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-200 bg-white">
              <tr v-for="user in personnelUsers" :key="user.id">
                <td class="px-5 py-4 font-semibold text-slate-900">
                  {{ fullName(user) }}
                </td>
                <td class="px-5 py-4 text-slate-700">{{ user.badge_number || '—' }}</td>
                <td class="px-5 py-4 text-slate-700">{{ user.rank || '—' }}</td>
                <td class="px-5 py-4 text-slate-700">{{ user.email || '—' }}</td>
                <td class="px-5 py-4 text-slate-700">{{ user.username || '—' }}</td>
                <td class="px-5 py-4">
                  <span class="inline-flex rounded-full border px-2.5 py-1 text-xs font-semibold uppercase tracking-wide" :class="statusClasses(user.status)">
                    {{ user.status || 'UNKNOWN' }}
                  </span>
                </td>
                <td class="px-5 py-4">
                  <div v-if="user.status === 'PENDING'" class="flex justify-end gap-2">
                    <button
                      type="button"
                      @click="handleAction(user, 'APPROVE')"
                      :disabled="actionInFlight === user.id"
                      class="rounded-lg bg-emerald-600 px-3 py-2 font-semibold text-white hover:bg-emerald-700 disabled:cursor-not-allowed disabled:opacity-60"
                    >
                      Approve
                    </button>
                    <button
                      type="button"
                      @click="handleAction(user, 'REJECT')"
                      :disabled="actionInFlight === user.id"
                      class="rounded-lg border border-red-200 bg-red-50 px-3 py-2 font-semibold text-red-700 hover:bg-red-100 disabled:cursor-not-allowed disabled:opacity-60"
                    >
                      Reject
                    </button>
                  </div>
                  <div v-else class="text-right text-xs text-slate-400">
                    No action
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'

const props = defineProps({
  currentUser: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['approval-updated'])

const personnelUsers = ref([])
const loading = ref(true)
const actionInFlight = ref(null)
const approvalConfirmation = ref('')

const API_URL = 'http://127.0.0.1:8000/api'

const pendingCount = computed(() => personnelUsers.value.filter(user => String(user.role || '').toUpperCase() === 'PERSONNEL' && String(user.status || '').toUpperCase() === 'PENDING').length)

const fullName = (user) => {
  const firstName = user.first_name || user.firstName || ''
  const lastName = user.last_name || user.lastName || ''

  if (firstName || lastName) {
    return `${firstName} ${lastName}`.trim()
  }

  return user.username || 'Unknown user'
}

const statusClasses = (status) => {
  const normalized = String(status || '').toUpperCase()

  if (normalized === 'PENDING') {
    return 'border-amber-200 bg-amber-50 text-amber-800'
  }

  if (normalized === 'APPROVED') {
    return 'border-emerald-200 bg-emerald-50 text-emerald-800'
  }

  if (normalized === 'REJECTED') {
    return 'border-red-200 bg-red-50 text-red-700'
  }

  if (normalized === 'SUSPENDED') {
    return 'border-slate-300 bg-slate-100 text-slate-700'
  }

  return 'border-slate-200 bg-slate-100 text-slate-600'
}

const loadPersonnelUsers = async () => {
  loading.value = true

  try {
    const response = await fetch(`${API_URL}/users/`)

    if (!response.ok) {
      throw new Error('Request failed')
    }

    const data = await response.json()
    personnelUsers.value = (Array.isArray(data) ? data : []).filter(user => String(user.role || '').toUpperCase() === 'PERSONNEL')
  } catch (error) {
    console.error('Unable to load personnel accounts:', error)
    personnelUsers.value = []
  } finally {
    loading.value = false
  }
}

const handleAction = async (user, action) => {
  if (!user || !user.id) {
    return
  }

  actionInFlight.value = user.id

  try {
    const response = await fetch(`${API_URL}/users/${user.id}/approval/`, {
      method: 'PATCH',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.cookie.split('; ').find(item => item.startsWith('csrftoken='))?.split('=')[1] || ''
      },
      body: JSON.stringify({
        action,
        admin_id: props.currentUser?.id || null,
        admin_email: props.currentUser?.email || null
      })
    })

    const data = await response.json().catch(() => ({}))

    if (!response.ok) {
      throw new Error(data.error || 'Approval update failed.')
    }

    if (action === 'APPROVE') {
      approvalConfirmation.value = fullName(user)
    } else {
      approvalConfirmation.value = ''
    }

    await loadPersonnelUsers()
    emit('approval-updated')
  } catch (error) {
    console.error('Approval action failed:', error)
    alert(error.message || 'Unable to update approval status.')
  } finally {
    actionInFlight.value = null
  }
}

onMounted(() => {
  loadPersonnelUsers()
})
</script>
