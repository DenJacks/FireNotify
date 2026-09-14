<script setup>
import { ref, computed, onMounted } from 'vue'

const props = defineProps({
  currentUser: {
    type: Object,
    required: false,
    default: null
  }
})

const STORAGE_KEY = 'fireNotifyWeeklyMonthlyLogs'

const logs = ref([])

const searchQuery = ref('')
const typeFilter = ref('All')
const statusFilter = ref('All')

const showAddModal = ref(false)
const showEditModal = ref(false)
const showDetailsModal = ref(false)
const showDeleteModal = ref(false)

const selectedLog = ref(null)
const toastMessage = ref('')
const showToast = ref(false)

const form = ref({
  activity: '',
  personnel: '',
  type: 'Weekly',
  deadline: '',
  status: 'Pending',
  description: '',
  notes: ''
})

const defaultLogs = [
  {
    id: 'LOG-001',
    activity: 'After-Operation Fire Incident Report',
    personnel: 'SFO1 M. Santos',
    type: 'Weekly',
    deadline: '2026-09-14',
    status: 'Pending',
    description: 'Submission of after-operation report for a recent fire incident.',
    notes: 'For administrative review.'
  },
  {
    id: 'LOG-002',
    activity: 'Quarterly Establishment Inspection',
    personnel: 'FO3 J. Dela Cruz',
    type: 'Monthly',
    deadline: '2026-08-20',
    status: 'Completed',
    description: 'Quarterly inspection and documentation of covered establishments.',
    notes: 'Inspection completed and archived.'
  },
  {
    id: 'LOG-003',
    activity: 'Community Fire Safety Orientation',
    personnel: 'FO1 C. Garcia',
    type: 'Weekly',
    deadline: '2026-09-12',
    status: 'Completed',
    description: 'Fire prevention orientation for community members and responders.',
    notes: 'Five barangays covered.'
  },
  {
    id: 'LOG-004',
    activity: 'Equipment Readiness Summary',
    personnel: 'FO2 A. Villanueva',
    type: 'Monthly',
    deadline: '2026-09-10',
    status: 'Submitted',
    description: 'Monthly summary of equipment condition and readiness.',
    notes: 'All assigned rescue tools inspected.'
  },
  {
    id: 'LOG-005',
    activity: 'Station Activity Summary',
    personnel: 'FO2 M. Santos',
    type: 'Weekly',
    deadline: '2026-09-13',
    status: 'Pending',
    description: 'Weekly summary of station activities and operational duties.',
    notes: 'Waiting for final review.'
  },
  {
    id: 'LOG-006',
    activity: 'Monthly Compliance Report',
    personnel: 'Station Administration',
    type: 'Monthly',
    deadline: '2026-09-19',
    status: 'Pending',
    description: 'Monthly compliance summary covering station operations.',
    notes: 'Deadline monitoring enabled.'
  }
]

const loadLogs = () => {
  const saved = localStorage.getItem(STORAGE_KEY)

  if (saved) {
    try {
      logs.value = JSON.parse(saved)
      return
    } catch (error) {
      console.error('Failed to load logs:', error)
    }
  }

  logs.value = defaultLogs
  saveLogs()
}

const saveLogs = () => {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(logs.value))
}

onMounted(() => {
  loadLogs()
})

const filteredLogs = computed(() => {
  const query = searchQuery.value.toLowerCase().trim()

  return logs.value.filter(log => {
    const matchesSearch =
      !query ||
      log.activity.toLowerCase().includes(query) ||
      log.personnel.toLowerCase().includes(query) ||
      log.id.toLowerCase().includes(query)

    const matchesType =
      typeFilter.value === 'All' ||
      log.type === typeFilter.value

    const matchesStatus =
      statusFilter.value === 'All' ||
      log.status === statusFilter.value

    return matchesSearch && matchesType && matchesStatus
  })
})

const weeklyCount = computed(() =>
  logs.value.filter(log => log.type === 'Weekly').length
)

const monthlyCount = computed(() =>
  logs.value.filter(log => log.type === 'Monthly').length
)

const submittedCount = computed(() =>
  logs.value.filter(log =>
    log.status === 'Submitted' || log.status === 'Completed'
  ).length
)

const pendingCount = computed(() =>
  logs.value.filter(log => log.status === 'Pending').length
)

const completedCount = computed(() =>
  logs.value.filter(log => log.status === 'Completed').length
)

const totalCount = computed(() => logs.value.length)

const completionRate = computed(() => {
  if (!totalCount.value) return 0
  return Math.round((completedCount.value / totalCount.value) * 100)
})

const showNotification = message => {
  toastMessage.value = message
  showToast.value = true

  setTimeout(() => {
    showToast.value = false
  }, 2500)
}

const resetForm = () => {
  form.value = {
    activity: '',
    personnel: '',
    type: 'Weekly',
    deadline: '',
    status: 'Pending',
    description: '',
    notes: ''
  }
}

const openAddModal = () => {
  resetForm()
  showAddModal.value = true
}

const addLog = () => {
  if (
    !form.value.activity.trim() ||
    !form.value.personnel.trim() ||
    !form.value.deadline
  ) {
    showNotification('Please complete the required fields.')
    return
  }

  const newLog = {
    id: `LOG-${String(logs.value.length + 1).padStart(3, '0')}`,
    activity: form.value.activity,
    personnel: form.value.personnel,
    type: form.value.type,
    deadline: form.value.deadline,
    status: form.value.status,
    description: form.value.description,
    notes: form.value.notes
  }

  logs.value.unshift(newLog)

  saveLogs()
  showAddModal.value = false

  showNotification('Log entry added successfully.')
}

const openEditModal = log => {
  selectedLog.value = log

  form.value = {
    activity: log.activity,
    personnel: log.personnel,
    type: log.type,
    deadline: log.deadline,
    status: log.status,
    description: log.description || '',
    notes: log.notes || ''
  }

  showEditModal.value = true
}

const updateLog = () => {
  if (
    !form.value.activity.trim() ||
    !form.value.personnel.trim() ||
    !form.value.deadline
  ) {
    showNotification('Please complete the required fields.')
    return
  }

  const index = logs.value.findIndex(
    log => log.id === selectedLog.value.id
  )

  if (index !== -1) {
    logs.value[index] = {
      ...logs.value[index],
      activity: form.value.activity,
      personnel: form.value.personnel,
      type: form.value.type,
      deadline: form.value.deadline,
      status: form.value.status,
      description: form.value.description,
      notes: form.value.notes
    }
  }

  saveLogs()
  showEditModal.value = false

  showNotification('Log entry updated successfully.')
}

const openDetails = log => {
  selectedLog.value = log
  showDetailsModal.value = true
}

const openDeleteModal = log => {
  selectedLog.value = log
  showDeleteModal.value = true
}

const deleteLog = () => {
  logs.value = logs.value.filter(
    log => log.id !== selectedLog.value.id
  )

  saveLogs()
  showDeleteModal.value = false

  showNotification('Log entry deleted.')
}

const markSubmitted = log => {
  const item = logs.value.find(item => item.id === log.id)

  if (!item) return

  item.status = 'Submitted'

  saveLogs()

  showNotification('Log marked as submitted.')
}

const markCompleted = log => {
  const item = logs.value.find(item => item.id === log.id)

  if (!item) return

  item.status = 'Completed'

  saveLogs()

  showNotification('Log marked as completed.')
}

const clearFilters = () => {
  searchQuery.value = ''
  typeFilter.value = 'All'
  statusFilter.value = 'All'
}

const formatDate = date => {
  if (!date) return '-'

  const parsed = new Date(`${date}T00:00:00`)

  return parsed.toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric'
  })
}

const statusClass = status => {
  if (status === 'Completed') {
    return 'bg-green-100 text-green-700'
  }

  if (status === 'Submitted') {
    return 'bg-blue-100 text-blue-700'
  }

  if (status === 'Pending') {
    return 'bg-yellow-100 text-yellow-700'
  }

  return 'bg-slate-100 text-slate-700'
}

const typeClass = type => {
  return type === 'Weekly'
    ? 'bg-purple-100 text-purple-700'
    : 'bg-blue-100 text-blue-700'
}
</script>

<template>
  <div class="space-y-6">

    <!-- TOAST -->
    <transition name="fade">
      <div
        v-if="showToast"
        class="fixed top-6 right-6 z-[100] bg-slate-900 text-white px-5 py-3 rounded-xl shadow-lg text-sm font-semibold"
      >
        {{ toastMessage }}
      </div>
    </transition>

    <!-- HEADER -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

        <div>
          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">
            Record Archives
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Weekly / Monthly Logs
          </h2>

          <p class="text-base text-slate-500 mt-1">
            Review station summaries, recurring reports, and compliance records.
          </p>
        </div>

        <button
          @click="openAddModal"
          class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition shadow-sm"
        >
          + Add Log Entry
        </button>

      </div>
    </section>

    <!-- STATISTICS -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-5">

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">
          {{ totalCount }}
        </p>
        <p class="text-sm text-slate-500 mt-1">
          Total Logs
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-purple-600">
          {{ weeklyCount }}
        </p>
        <p class="text-sm text-slate-500 mt-1">
          Weekly Logs
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-blue-600">
          {{ monthlyCount }}
        </p>
        <p class="text-sm text-slate-500 mt-1">
          Monthly Reports
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">
          {{ submittedCount }}
        </p>
        <p class="text-sm text-slate-500 mt-1">
          Submitted
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">
          {{ pendingCount }}
        </p>
        <p class="text-sm text-slate-500 mt-1">
          Pending Review
        </p>
      </div>

    </section>

    <!-- SEARCH / FILTER -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

      <div class="flex flex-col lg:flex-row gap-4">

        <div class="flex-1 relative">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search activity, personnel, or log ID..."
            class="w-full px-4 py-3 border border-slate-200 rounded-xl outline-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
          />
        </div>

        <select
          v-model="typeFilter"
          class="px-4 py-3 border border-slate-200 rounded-xl bg-white outline-none focus:border-[#8B1E23]"
        >
          <option value="All">All Types</option>
          <option value="Weekly">Weekly</option>
          <option value="Monthly">Monthly</option>
        </select>

        <select
          v-model="statusFilter"
          class="px-4 py-3 border border-slate-200 rounded-xl bg-white outline-none focus:border-[#8B1E23]"
        >
          <option value="All">All Status</option>
          <option value="Pending">Pending</option>
          <option value="Submitted">Submitted</option>
          <option value="Completed">Completed</option>
        </select>

        <button
          @click="clearFilters"
          class="px-5 py-3 rounded-xl border border-slate-200 text-slate-700 font-semibold hover:bg-slate-50 transition"
        >
          Clear
        </button>

      </div>

      <div class="flex items-center justify-between mt-4 text-sm text-slate-500">
        <span>
          Showing <strong class="text-slate-900">{{ filteredLogs.length }}</strong>
          of <strong class="text-slate-900">{{ totalCount }}</strong> entries
        </span>

        <span>
          Completion Rate:
          <strong class="text-green-600">{{ completionRate }}%</strong>
        </span>
      </div>

    </section>

    <!-- HIGHLIGHTS -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- WEEKLY -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">

          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Weekly Highlights
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              This week's important operational notes
            </p>
          </div>

          <span class="px-3 py-1 rounded-full bg-purple-100 text-purple-700 text-xs font-bold">
            {{ weeklyCount }} Logs
          </span>

        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <p class="text-sm font-bold text-slate-900">
              Fire Safety Orientation
            </p>

            <p class="text-sm text-slate-600 mt-1">
              Covered 5 barangays with 98% attendance from local responders and volunteers.
            </p>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <p class="text-sm font-bold text-slate-900">
              Equipment Readiness
            </p>

            <p class="text-sm text-slate-600 mt-1">
              Assigned rescue tools were checked, cleaned, and tagged for dispatch readiness.
            </p>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <p class="text-sm font-bold text-slate-900">
              Dispatch Coordination
            </p>

            <p class="text-sm text-slate-600 mt-1">
              Dispatch teams coordinated with local emergency units for scheduled activities.
            </p>
          </div>

        </div>
      </div>

      <!-- MONTHLY -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">

          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Monthly Highlights
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              Station compliance and performance summary
            </p>
          </div>

          <span class="px-3 py-1 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">
            {{ monthlyCount }} Reports
          </span>

        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-emerald-200 bg-emerald-50">
            <p class="text-sm font-bold text-slate-900">
              Compliance Rate
            </p>

            <p class="text-sm text-slate-600 mt-1">
              Monthly compliance increased to 94.5%, surpassing the previous cycle by 4.2%.
            </p>
          </div>

          <div class="p-4 rounded-xl border border-blue-200 bg-blue-50">
            <p class="text-sm font-bold text-slate-900">
              Report Turnaround
            </p>

            <p class="text-sm text-slate-600 mt-1">
              Average report submission turnaround improved across operational activities.
            </p>
          </div>

          <div class="p-4 rounded-xl border border-amber-200 bg-amber-50">
            <p class="text-sm font-bold text-slate-900">
              Staff Performance
            </p>

            <p class="text-sm text-slate-600 mt-1">
              Operations staff maintained steady productivity while balancing drills, inspections, and training.
            </p>
          </div>

        </div>
      </div>

    </section>

    <!-- TABLE -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex items-center justify-between border-b border-slate-200 pb-5">

        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Recent Weekly / Monthly Entries
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Latest archived logs submitted by personnel
          </p>
        </div>

      </div>

      <div class="mt-5 overflow-x-auto">

        <table class="min-w-full">

          <thead>
            <tr class="border-b border-slate-200 text-left text-xs font-bold uppercase tracking-wide text-slate-500">

              <th class="px-4 py-4">Log ID</th>
              <th class="px-4 py-4">Activity</th>
              <th class="px-4 py-4">Personnel</th>
              <th class="px-4 py-4">Type</th>
              <th class="px-4 py-4">Deadline</th>
              <th class="px-4 py-4">Status</th>
              <th class="px-4 py-4 text-right">Actions</th>

            </tr>
          </thead>

          <tbody>

            <tr
              v-for="item in filteredLogs"
              :key="item.id"
              class="border-b border-slate-100 hover:bg-slate-50 transition"
            >

              <td class="px-4 py-4">
                <span class="font-bold text-[#8B1E23]">
                  {{ item.id }}
                </span>
              </td>

              <td class="px-4 py-4 min-w-[240px]">
                <p class="font-semibold text-slate-900">
                  {{ item.activity }}
                </p>

                <p class="text-xs text-slate-500 mt-1 max-w-[280px] truncate">
                  {{ item.description }}
                </p>
              </td>

              <td class="px-4 py-4 text-slate-600 whitespace-nowrap">
                {{ item.personnel }}
              </td>

              <td class="px-4 py-4">
                <span
                  class="px-3 py-1 rounded-full text-xs font-bold"
                  :class="typeClass(item.type)"
                >
                  {{ item.type }}
                </span>
              </td>

              <td class="px-4 py-4 text-slate-600 whitespace-nowrap">
                {{ formatDate(item.deadline) }}
              </td>

              <td class="px-4 py-4">
                <span
                  class="px-3 py-1 rounded-full text-xs font-bold"
                  :class="statusClass(item.status)"
                >
                  {{ item.status }}
                </span>
              </td>

              <td class="px-4 py-4">

                <div class="flex items-center justify-end gap-2">

                  <button
                    @click="openDetails(item)"
                    class="px-3 py-2 rounded-lg text-xs font-bold text-slate-700 bg-slate-100 hover:bg-slate-200"
                  >
                    View
                  </button>

                  <button
                    @click="openEditModal(item)"
                    class="px-3 py-2 rounded-lg text-xs font-bold text-blue-700 bg-blue-50 hover:bg-blue-100"
                  >
                    Edit
                  </button>

                  <button
                    v-if="item.status === 'Pending'"
                    @click="markSubmitted(item)"
                    class="px-3 py-2 rounded-lg text-xs font-bold text-green-700 bg-green-50 hover:bg-green-100"
                  >
                    Submit
                  </button>

                  <button
                    v-if="item.status === 'Submitted'"
                    @click="markCompleted(item)"
                    class="px-3 py-2 rounded-lg text-xs font-bold text-emerald-700 bg-emerald-50 hover:bg-emerald-100"
                  >
                    Complete
                  </button>

                  <button
                    @click="openDeleteModal(item)"
                    class="px-3 py-2 rounded-lg text-xs font-bold text-red-700 bg-red-50 hover:bg-red-100"
                  >
                    Delete
                  </button>

                </div>

              </td>

            </tr>

            <tr v-if="filteredLogs.length === 0">

              <td colspan="7" class="py-16 text-center">

                <div class="text-slate-400 text-4xl mb-3">
                  📋
                </div>

                <p class="font-bold text-slate-700">
                  No log entries found
                </p>

                <p class="text-sm text-slate-500 mt-1">
                  Try changing your search or filters.
                </p>

              </td>

            </tr>

          </tbody>

        </table>

      </div>
    </section>

    <!-- ADD / EDIT MODAL -->
    <div
      v-if="showAddModal || showEditModal"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div class="bg-white rounded-2xl shadow-2xl w-full max-w-2xl max-h-[90vh] overflow-y-auto">

        <div class="p-6 border-b border-slate-200 flex items-center justify-between">

          <div>
            <h2 class="text-xl font-bold text-slate-900">
              {{ showAddModal ? 'Add Log Entry' : 'Edit Log Entry' }}
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              {{ showAddModal
                ? 'Create a new weekly or monthly record.'
                : 'Update the selected record.'
              }}
            </p>
          </div>

          <button
            @click="showAddModal = false; showEditModal = false"
            class="text-slate-400 hover:text-slate-700 text-2xl"
          >
            ×
          </button>

        </div>

        <div class="p-6 space-y-5">

          <div>
            <label class="block text-sm font-bold text-slate-700 mb-2">
              Activity *
            </label>

            <input
              v-model="form.activity"
              type="text"
              placeholder="Enter activity or report title"
              class="w-full px-4 py-3 border border-slate-200 rounded-xl outline-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
            />
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-5">

            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">
                Personnel *
              </label>

              <input
                v-model="form.personnel"
                type="text"
                placeholder="e.g. FO3 J. Dela Cruz"
                class="w-full px-4 py-3 border border-slate-200 rounded-xl outline-none focus:border-[#8B1E23]"
              />
            </div>

            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">
                Deadline *
              </label>

              <input
                v-model="form.deadline"
                type="date"
                class="w-full px-4 py-3 border border-slate-200 rounded-xl outline-none focus:border-[#8B1E23]"
              />
            </div>

          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-5">

            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">
                Record Type
              </label>

              <select
                v-model="form.type"
                class="w-full px-4 py-3 border border-slate-200 rounded-xl bg-white outline-none focus:border-[#8B1E23]"
              >
                <option value="Weekly">Weekly</option>
                <option value="Monthly">Monthly</option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">
                Status
              </label>

              <select
                v-model="form.status"
                class="w-full px-4 py-3 border border-slate-200 rounded-xl bg-white outline-none focus:border-[#8B1E23]"
              >
                <option value="Pending">Pending</option>
                <option value="Submitted">Submitted</option>
                <option value="Completed">Completed</option>
              </select>
            </div>

          </div>

          <div>
            <label class="block text-sm font-bold text-slate-700 mb-2">
              Description
            </label>

            <textarea
              v-model="form.description"
              rows="3"
              placeholder="Brief description of the log entry..."
              class="w-full px-4 py-3 border border-slate-200 rounded-xl outline-none focus:border-[#8B1E23] resize-none"
            ></textarea>
          </div>

          <div>
            <label class="block text-sm font-bold text-slate-700 mb-2">
              Notes
            </label>

            <textarea
              v-model="form.notes"
              rows="3"
              placeholder="Additional notes..."
              class="w-full px-4 py-3 border border-slate-200 rounded-xl outline-none focus:border-[#8B1E23] resize-none"
            ></textarea>
          </div>

        </div>

        <div class="p-6 border-t border-slate-200 flex justify-end gap-3">

          <button
            @click="showAddModal = false; showEditModal = false"
            class="px-5 py-3 rounded-xl border border-slate-200 font-bold text-slate-700 hover:bg-slate-50"
          >
            Cancel
          </button>

          <button
            v-if="showAddModal"
            @click="addLog"
            class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D]"
          >
            Add Log
          </button>

          <button
            v-if="showEditModal"
            @click="updateLog"
            class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D]"
          >
            Save Changes
          </button>

        </div>

      </div>
    </div>

    <!-- DETAILS MODAL -->
    <div
      v-if="showDetailsModal && selectedLog"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div class="bg-white rounded-2xl shadow-2xl w-full max-w-xl">

        <div class="p-6 border-b border-slate-200 flex items-center justify-between">

          <div>
            <p class="text-xs font-bold text-[#8B1E23]">
              {{ selectedLog.id }}
            </p>

            <h2 class="text-xl font-bold text-slate-900 mt-1">
              Log Details
            </h2>
          </div>

          <button
            @click="showDetailsModal = false"
            class="text-slate-400 hover:text-slate-700 text-2xl"
          >
            ×
          </button>

        </div>

        <div class="p-6 space-y-5">

          <div>
            <p class="text-xs uppercase font-bold text-slate-400">
              Activity
            </p>

            <p class="font-bold text-slate-900 mt-1">
              {{ selectedLog.activity }}
            </p>
          </div>

          <div class="grid grid-cols-2 gap-5">

            <div>
              <p class="text-xs uppercase font-bold text-slate-400">
                Personnel
              </p>

              <p class="font-semibold text-slate-800 mt-1">
                {{ selectedLog.personnel }}
              </p>
            </div>

            <div>
              <p class="text-xs uppercase font-bold text-slate-400">
                Type
              </p>

              <span
                class="inline-block mt-1 px-3 py-1 rounded-full text-xs font-bold"
                :class="typeClass(selectedLog.type)"
              >
                {{ selectedLog.type }}
              </span>
            </div>

          </div>

          <div class="grid grid-cols-2 gap-5">

            <div>
              <p class="text-xs uppercase font-bold text-slate-400">
                Deadline
              </p>

              <p class="font-semibold text-slate-800 mt-1">
                {{ formatDate(selectedLog.deadline) }}
              </p>
            </div>

            <div>
              <p class="text-xs uppercase font-bold text-slate-400">
                Status
              </p>

              <span
                class="inline-block mt-1 px-3 py-1 rounded-full text-xs font-bold"
                :class="statusClass(selectedLog.status)"
              >
                {{ selectedLog.status }}
              </span>
            </div>

          </div>

          <div>
            <p class="text-xs uppercase font-bold text-slate-400">
              Description
            </p>

            <p class="text-sm text-slate-600 mt-1">
              {{ selectedLog.description || 'No description provided.' }}
            </p>
          </div>

          <div>
            <p class="text-xs uppercase font-bold text-slate-400">
              Notes
            </p>

            <p class="text-sm text-slate-600 mt-1">
              {{ selectedLog.notes || 'No additional notes.' }}
            </p>
          </div>

        </div>

        <div class="p-6 border-t border-slate-200 flex justify-end">

          <button
            @click="showDetailsModal = false"
            class="px-5 py-3 rounded-xl bg-slate-100 text-slate-700 font-bold hover:bg-slate-200"
          >
            Close
          </button>

        </div>

      </div>
    </div>

    <!-- DELETE MODAL -->
    <div
      v-if="showDeleteModal && selectedLog"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div class="bg-white rounded-2xl shadow-2xl w-full max-w-md p-6">

        <div class="w-12 h-12 rounded-full bg-red-100 text-red-600 flex items-center justify-center text-xl font-bold mb-4">
          !
        </div>

        <h2 class="text-xl font-bold text-slate-900">
          Delete Log Entry?
        </h2>

        <p class="text-sm text-slate-500 mt-2">
          Are you sure you want to delete
          <strong>{{ selectedLog.activity }}</strong>?
          This action cannot be undone.
        </p>

        <div class="flex justify-end gap-3 mt-6">

          <button
            @click="showDeleteModal = false"
            class="px-5 py-3 rounded-xl border border-slate-200 font-bold text-slate-700 hover:bg-slate-50"
          >
            Cancel
          </button>

          <button
            @click="deleteLog"
            class="px-5 py-3 rounded-xl bg-red-600 text-white font-bold hover:bg-red-700"
          >
            Delete
          </button>

        </div>

      </div>
    </div>

  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>