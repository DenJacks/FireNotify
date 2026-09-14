<script setup>
import { computed, ref } from 'vue'

const props = defineProps({
  currentUser: {
    type: Object,
    default: null
  }
})

/* =========================================================
   STATE
========================================================= */

const searchQuery = ref('')
const selectedType = ref('All Activity Types')
const selectedStatus = ref('All Status')
const selectedPriority = ref('All Priorities')

const showActivityModal = ref(false)
const showDetailsModal = ref(false)
const showDeleteModal = ref(false)

const editingActivity = ref(null)
const selectedActivity = ref(null)

const toastMessage = ref('')
const toastType = ref('success')

const activityForm = ref({
  name: '',
  type: 'Inspection',
  personnel: 1,
  schedule: '',
  time: '',
  priority: 'Medium',
  status: 'Scheduled',
  location: '',
  description: ''
})

/* =========================================================
   DEMO DATA
   Replace with Django API later
========================================================= */

const activities = ref([
  {
    id: 'ACT-001',
    name: 'Fire Safety Inspection',
    type: 'Inspection',
    personnel: 5,
    schedule: '2026-09-09',
    time: '09:00',
    priority: 'High',
    status: 'Ongoing',
    location: 'Public Market Complex',
    description: 'Conduct fire safety inspection and verify compliance requirements.'
  },
  {
    id: 'ACT-002',
    name: 'Community Fire Drill',
    type: 'Fire Drill',
    personnel: 8,
    schedule: '2026-09-10',
    time: '13:30',
    priority: 'Medium',
    status: 'Scheduled',
    location: 'Barangay San Isidro',
    description: 'Community fire drill and emergency response coordination.'
  },
  {
    id: 'ACT-003',
    name: 'Station Equipment Inspection',
    type: 'Inspection',
    personnel: 4,
    schedule: '2026-09-11',
    time: '08:30',
    priority: 'Low',
    status: 'Scheduled',
    location: 'BFP Balingasag Station',
    description: 'Inspect fire equipment and verify serviceability.'
  },
  {
    id: 'ACT-004',
    name: 'Emergency Response Training',
    type: 'Training',
    personnel: 10,
    schedule: '2026-09-14',
    time: '09:00',
    priority: 'High',
    status: 'Scheduled',
    location: 'BFP Training Room',
    description: 'Emergency response and incident management training.'
  },
  {
    id: 'ACT-005',
    name: 'Vehicle Maintenance Check',
    type: 'Inspection',
    personnel: 3,
    schedule: '2026-09-14',
    time: '14:00',
    priority: 'Medium',
    status: 'Scheduled',
    location: 'BFP Motor Pool',
    description: 'Routine inspection and maintenance check of response vehicles.'
  },
  {
    id: 'ACT-006',
    name: 'Barangay Rescue Coordination Drill',
    type: 'Emergency Response',
    personnel: 7,
    schedule: '2026-09-15',
    time: '13:30',
    priority: 'High',
    status: 'Scheduled',
    location: 'Barangay Coordination Center',
    description: 'Coordinate rescue response procedures with barangay personnel.'
  },
  {
    id: 'ACT-007',
    name: 'High-rise Building Inspection',
    type: 'Inspection',
    personnel: 6,
    schedule: '2026-09-16',
    time: '08:00',
    priority: 'High',
    status: 'Scheduled',
    location: 'Municipal Commercial Building',
    description: 'Conduct inspection of fire exits, alarms and emergency equipment.'
  },
  {
    id: 'ACT-008',
    name: 'Station Briefing',
    type: 'Training',
    personnel: 12,
    schedule: '2026-09-12',
    time: '16:00',
    priority: 'Low',
    status: 'Completed',
    location: 'BFP Balingasag Station',
    description: 'Weekly station operations briefing.'
  },
  {
    id: 'ACT-009',
    name: 'Routine Safety Patrol',
    type: 'Emergency Response',
    personnel: 4,
    schedule: '2026-09-13',
    time: '10:00',
    priority: 'Medium',
    status: 'Delayed',
    location: 'Zone 2 Commercial Area',
    description: 'Routine safety patrol and fire hazard monitoring.'
  }
])

/* =========================================================
   COMPUTED FILTERS
========================================================= */

const filteredActivities = computed(() => {
  const query = searchQuery.value.toLowerCase().trim()

  return activities.value.filter(activity => {
    const searchText = [
      activity.name,
      activity.id,
      activity.type,
      activity.location
    ]
      .join(' ')
      .toLowerCase()

    const matchesSearch =
      !query || searchText.includes(query)

    const matchesType =
      selectedType.value === 'All Activity Types' ||
      activity.type === selectedType.value

    const matchesStatus =
      selectedStatus.value === 'All Status' ||
      activity.status === selectedStatus.value

    const matchesPriority =
      selectedPriority.value === 'All Priorities' ||
      activity.priority === selectedPriority.value

    return (
      matchesSearch &&
      matchesType &&
      matchesStatus &&
      matchesPriority
    )
  })
})

/* =========================================================
   STATISTICS
========================================================= */

const today = '2026-09-14'

const todaysActivities = computed(() =>
  activities.value.filter(
    activity => activity.schedule === today
  ).length
)

const scheduledCount = computed(() =>
  activities.value.filter(
    activity => activity.status === 'Scheduled'
  ).length
)

const completedCount = computed(() =>
  activities.value.filter(
    activity => activity.status === 'Completed'
  ).length
)

const delayedCount = computed(() =>
  activities.value.filter(
    activity => activity.status === 'Delayed'
  ).length
)

const ongoingCount = computed(() =>
  activities.value.filter(
    activity => activity.status === 'Ongoing'
  ).length
)

const completionRate = computed(() => {
  if (!activities.value.length) return 0

  return Math.round(
    (completedCount.value / activities.value.length) * 100
  )
})

/* =========================================================
   WORKLOAD
========================================================= */

const workload = computed(() => {
  const total = activities.value.length || 1

  const types = [
    'Inspection',
    'Fire Drill',
    'Training',
    'Emergency Response'
  ]

  return types.map(type => {
    const count = activities.value.filter(
      activity => activity.type === type
    ).length

    return {
      type,
      count,
      percentage: Math.round((count / total) * 100)
    }
  })
})

/* =========================================================
   UPCOMING ACTIVITIES
========================================================= */

const plannedActivities = computed(() =>
  activities.value
    .filter(activity =>
      ['Scheduled', 'Ongoing'].includes(activity.status)
    )
    .sort((a, b) =>
      a.schedule.localeCompare(b.schedule)
    )
    .slice(0, 5)
)

/* =========================================================
   MODALS
========================================================= */

const openCreateModal = () => {
  editingActivity.value = null

  activityForm.value = {
    name: '',
    type: 'Inspection',
    personnel: 1,
    schedule: '',
    time: '',
    priority: 'Medium',
    status: 'Scheduled',
    location: '',
    description: ''
  }

  showActivityModal.value = true
}

const openEditModal = activity => {
  editingActivity.value = activity

  activityForm.value = {
    name: activity.name,
    type: activity.type,
    personnel: activity.personnel,
    schedule: activity.schedule,
    time: activity.time,
    priority: activity.priority,
    status: activity.status,
    location: activity.location,
    description: activity.description
  }

  showActivityModal.value = true
}

const viewActivity = activity => {
  selectedActivity.value = activity
  showDetailsModal.value = true
}

const openDeleteModal = activity => {
  selectedActivity.value = activity
  showDeleteModal.value = true
}

/* =========================================================
   CRUD
========================================================= */

const saveActivity = () => {
  if (
    !activityForm.value.name ||
    !activityForm.value.schedule ||
    !activityForm.value.time ||
    !activityForm.value.location
  ) {
    showToast('Please complete all required fields.', 'error')
    return
  }

  if (editingActivity.value) {
    Object.assign(
      editingActivity.value,
      activityForm.value
    )

    showToast('Activity updated successfully.')
  } else {
    const newActivity = {
      id: `ACT-${String(
        activities.value.length + 1
      ).padStart(3, '0')}`,
      ...activityForm.value
    }

    activities.value.unshift(newActivity)

    showToast('New activity created successfully.')
  }

  showActivityModal.value = false
}

const deleteActivity = () => {
  if (!selectedActivity.value) return

  activities.value = activities.value.filter(
    activity =>
      activity.id !== selectedActivity.value.id
  )

  showDeleteModal.value = false
  selectedActivity.value = null

  showToast('Activity deleted successfully.')
}

const updateStatus = (activity, status) => {
  activity.status = status

  showToast(
    `Activity marked as ${status}.`
  )
}

/* =========================================================
   HELPERS
========================================================= */

const clearFilters = () => {
  searchQuery.value = ''
  selectedType.value = 'All Activity Types'
  selectedStatus.value = 'All Status'
  selectedPriority.value = 'All Priorities'
}

const hasActiveFilters = computed(() =>
  searchQuery.value ||
  selectedType.value !== 'All Activity Types' ||
  selectedStatus.value !== 'All Status' ||
  selectedPriority.value !== 'All Priorities'
)

const showToast = (message, type = 'success') => {
  toastMessage.value = message
  toastType.value = type

  setTimeout(() => {
    toastMessage.value = ''
  }, 3000)
}

const formatDate = date => {
  if (!date) return '—'

  return new Date(`${date}T00:00:00`).toLocaleDateString(
    'en-US',
    {
      month: 'short',
      day: 'numeric',
      year: 'numeric'
    }
  )
}

const formatTime = time => {
  if (!time) return '—'

  const [hours, minutes] = time.split(':')
  const date = new Date()

  date.setHours(Number(hours))
  date.setMinutes(Number(minutes))

  return date.toLocaleTimeString(
    'en-US',
    {
      hour: 'numeric',
      minute: '2-digit'
    }
  )
}

const getPriorityClass = priority => {
  const classes = {
    High: 'bg-red-50 text-[#8B1E23]',
    Medium: 'bg-yellow-50 text-yellow-700',
    Low: 'bg-green-50 text-green-700'
  }

  return classes[priority] || 'bg-slate-100 text-slate-600'
}

const getStatusClass = status => {
  const classes = {
    Scheduled: 'bg-yellow-50 text-yellow-700',
    Ongoing: 'bg-blue-50 text-blue-700',
    Completed: 'bg-green-50 text-green-700',
    Delayed: 'bg-red-50 text-[#8B1E23]'
  }

  return classes[status] || 'bg-slate-100 text-slate-600'
}

const getTypeClass = type => {
  const classes = {
    Inspection: 'bg-purple-50 text-purple-700',
    'Fire Drill': 'bg-orange-50 text-orange-700',
    Training: 'bg-green-50 text-green-700',
    'Emergency Response': 'bg-blue-50 text-blue-700'
  }

  return classes[type] || 'bg-slate-100 text-slate-600'
}
</script>

<template>
  <div class="space-y-6">

    <!-- =====================================================
         HEADER
    ====================================================== -->

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">

        <div>
          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">
            Operations Management
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Activity Management
          </h2>

          <p class="text-base text-slate-500 mt-1">
            Create, schedule, assign, and monitor station activities.
          </p>
        </div>

        <button
          @click="openCreateModal"
          class="px-6 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition shadow-sm"
        >
          + Create New Activity
        </button>

      </div>

    </section>


    <!-- =====================================================
         STATISTICS
    ====================================================== -->

    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-5">

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-slate-900">
          {{ String(todaysActivities).padStart(2, '0') }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Today's Activities
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-blue-600">
          {{ String(scheduledCount).padStart(2, '0') }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Scheduled
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">
          {{ String(completedCount).padStart(2, '0') }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Completed
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">
          {{ String(delayedCount).padStart(2, '0') }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Delayed
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-emerald-600">
          {{ completionRate }}%
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Completion Rate
        </p>
      </div>

    </section>


    <!-- =====================================================
         SEARCH & FILTERS
    ====================================================== -->

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

      <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4">

        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search activity..."
          class="h-12 px-4 rounded-xl border border-slate-300 text-base focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]"
        />

        <select
          v-model="selectedType"
          class="h-12 px-4 rounded-xl border border-slate-300 text-base focus:outline-none focus:ring-2 focus:ring-red-200"
        >
          <option>All Activity Types</option>
          <option>Inspection</option>
          <option>Fire Drill</option>
          <option>Training</option>
          <option>Emergency Response</option>
        </select>

        <select
          v-model="selectedStatus"
          class="h-12 px-4 rounded-xl border border-slate-300 text-base focus:outline-none focus:ring-2 focus:ring-red-200"
        >
          <option>All Status</option>
          <option>Scheduled</option>
          <option>Ongoing</option>
          <option>Completed</option>
          <option>Delayed</option>
        </select>

        <select
          v-model="selectedPriority"
          class="h-12 px-4 rounded-xl border border-slate-300 text-base focus:outline-none focus:ring-2 focus:ring-red-200"
        >
          <option>All Priorities</option>
          <option>High</option>
          <option>Medium</option>
          <option>Low</option>
        </select>

      </div>

      <div
        v-if="hasActiveFilters"
        class="mt-4 flex justify-end"
      >
        <button
          @click="clearFilters"
          class="text-sm font-bold text-[#8B1E23] hover:underline"
        >
          Clear Filters
        </button>
      </div>

    </section>


    <!-- =====================================================
         ACTIVITY TABLE
    ====================================================== -->

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex items-center justify-between mb-5">

        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Station Activities
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            {{ filteredActivities.length }} activities found
          </p>
        </div>

      </div>

      <div class="overflow-x-auto">

        <table class="w-full text-left">

          <thead>
            <tr class="border-b border-slate-200 text-xs font-bold uppercase tracking-wide text-slate-400">

              <th class="pb-4 pr-5">
                Activity
              </th>

              <th class="pb-4 pr-5">
                Type
              </th>

              <th class="pb-4 pr-5">
                Personnel
              </th>

              <th class="pb-4 pr-5">
                Schedule
              </th>

              <th class="pb-4 pr-5">
                Priority
              </th>

              <th class="pb-4 pr-5">
                Status
              </th>

              <th class="pb-4 text-right">
                Actions
              </th>

            </tr>
          </thead>

          <tbody class="divide-y divide-slate-100">

            <tr
              v-for="activity in filteredActivities"
              :key="activity.id"
              class="hover:bg-slate-50 transition"
            >

              <td class="py-5 pr-5">

                <p class="font-bold text-slate-900">
                  {{ activity.name }}
                </p>

                <p class="text-xs text-slate-400 mt-1">
                  {{ activity.id }}
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  {{ activity.location }}
                </p>

              </td>

              <td class="py-5 pr-5">

                <span
                  :class="getTypeClass(activity.type)"
                  class="px-3 py-1.5 rounded-full text-xs font-bold"
                >
                  {{ activity.type }}
                </span>

              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                {{ activity.personnel }} Personnel
              </td>

              <td class="py-5 pr-5">

                <p class="text-sm font-semibold text-slate-700">
                  {{ formatDate(activity.schedule) }}
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  {{ formatTime(activity.time) }}
                </p>

              </td>

              <td class="py-5 pr-5">

                <span
                  :class="getPriorityClass(activity.priority)"
                  class="px-3 py-1.5 rounded-full text-xs font-bold"
                >
                  {{ activity.priority.toUpperCase() }}
                </span>

              </td>

              <td class="py-5 pr-5">

                <span
                  :class="getStatusClass(activity.status)"
                  class="px-3 py-1.5 rounded-full text-xs font-bold"
                >
                  {{ activity.status.toUpperCase() }}
                </span>

              </td>

              <td class="py-5 text-right">

                <div class="flex justify-end gap-2">

                  <button
                    @click="viewActivity(activity)"
                    class="px-3 py-2 rounded-lg bg-slate-100 text-slate-700 text-xs font-bold hover:bg-slate-200"
                  >
                    View
                  </button>

                  <button
                    @click="openEditModal(activity)"
                    class="px-3 py-2 rounded-lg bg-blue-50 text-blue-700 text-xs font-bold hover:bg-blue-100"
                  >
                    Edit
                  </button>

                  <button
                    @click="openDeleteModal(activity)"
                    class="px-3 py-2 rounded-lg bg-red-50 text-[#8B1E23] text-xs font-bold hover:bg-red-100"
                  >
                    Delete
                  </button>

                </div>

              </td>

            </tr>

            <tr v-if="!filteredActivities.length">

              <td
                colspan="7"
                class="py-12 text-center"
              >

                <p class="font-bold text-slate-700">
                  No activities found
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


    <!-- =====================================================
         PLANNED ACTIVITIES + WORKLOAD
    ====================================================== -->

    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- Planned -->

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">

          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Planned Activities
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              Upcoming station schedule
            </p>
          </div>

          <span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">
            {{ plannedActivities.length }} ITEMS
          </span>

        </div>

        <div class="mt-5 space-y-4">

          <div
            v-for="activity in plannedActivities"
            :key="activity.id"
            class="p-4 rounded-xl border border-slate-200 bg-slate-50 hover:bg-white transition"
          >

            <div class="flex justify-between gap-4">

              <div>

                <p class="font-bold text-slate-900">
                  {{ activity.name }}
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  {{ formatDate(activity.schedule) }}
                  •
                  {{ formatTime(activity.time) }}
                </p>

                <p class="text-xs text-slate-400 mt-1">
                  {{ activity.location }}
                </p>

              </div>

              <span
                :class="getStatusClass(activity.status)"
                class="h-fit px-2.5 py-1 rounded-full text-xs font-bold whitespace-nowrap"
              >
                {{ activity.status }}
              </span>

            </div>

          </div>

        </div>

      </div>


      <!-- Workload -->

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="border-b border-slate-200 pb-5">

          <h2 class="text-xl font-bold text-slate-900">
            Workload Summary
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Activity allocation by type
          </p>

        </div>

        <div class="mt-5 space-y-5">

          <div
            v-for="item in workload"
            :key="item.type"
          >

            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">

              <span>
                {{ item.type }}
              </span>

              <span>
                {{ item.percentage }}%
              </span>

            </div>

            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">

              <div
                class="h-full rounded-full bg-[#8B1E23] transition-all duration-500"
                :style="{ width: `${item.percentage}%` }"
              ></div>

            </div>

          </div>

        </div>

      </div>

    </section>


    <!-- =====================================================
         QUICK STATUS
    ====================================================== -->

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="border-b border-slate-200 pb-5">

        <h2 class="text-xl font-bold text-slate-900">
          Activity Status Overview
        </h2>

        <p class="text-sm text-slate-500 mt-1">
          Current operational activity distribution
        </p>

      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-5">

        <div class="p-4 rounded-xl bg-blue-50 border border-blue-100">
          <p class="text-2xl font-bold text-blue-700">
            {{ scheduledCount }}
          </p>

          <p class="text-sm text-blue-700 mt-1 font-semibold">
            Scheduled Activities
          </p>
        </div>

        <div class="p-4 rounded-xl bg-indigo-50 border border-indigo-100">
          <p class="text-2xl font-bold text-indigo-700">
            {{ ongoingCount }}
          </p>

          <p class="text-sm text-indigo-700 mt-1 font-semibold">
            Ongoing Activities
          </p>
        </div>

        <div class="p-4 rounded-xl bg-green-50 border border-green-100">
          <p class="text-2xl font-bold text-green-700">
            {{ completedCount }}
          </p>

          <p class="text-sm text-green-700 mt-1 font-semibold">
            Completed Activities
          </p>
        </div>

        <div class="p-4 rounded-xl bg-red-50 border border-red-100">
          <p class="text-2xl font-bold text-[#8B1E23]">
            {{ delayedCount }}
          </p>

          <p class="text-sm text-[#8B1E23] mt-1 font-semibold">
            Delayed Activities
          </p>
        </div>

      </div>

    </section>


    <!-- =====================================================
         ACTIVITY NOTES
    ====================================================== -->

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="border-b border-slate-200 pb-5">

        <h2 class="text-xl font-bold text-slate-900">
          Activity Notes
        </h2>

        <p class="text-sm text-slate-500 mt-1">
          Important operational reminders
        </p>

      </div>

      <div class="mt-5 space-y-4">

        <div class="p-4 rounded-xl border border-lime-200 bg-lime-50">

          <p class="text-sm font-bold text-slate-900">
            Reminder
          </p>

          <p class="text-sm text-slate-600 mt-1">
            All inspection teams must bring updated checklist forms before deployment.
          </p>

        </div>

        <div class="p-4 rounded-xl border border-amber-200 bg-amber-50">

          <p class="text-sm font-bold text-slate-900">
            Coordination
          </p>

          <p class="text-sm text-slate-600 mt-1">
            Coordinate with the barangay office for drill participation and crowd control support.
          </p>

        </div>

        <div class="p-4 rounded-xl border border-sky-200 bg-sky-50">

          <p class="text-sm font-bold text-slate-900">
            Escalation
          </p>

          <p class="text-sm text-slate-600 mt-1">
            Any delay in scheduled drills must be logged and escalated to the operations section chief.
          </p>

        </div>

      </div>

    </section>


    <!-- =====================================================
         CREATE / EDIT MODAL
    ====================================================== -->

    <div
      v-if="showActivityModal"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div class="bg-white w-full max-w-2xl rounded-2xl shadow-xl max-h-[90vh] overflow-y-auto">

        <div class="p-6 border-b border-slate-200">

          <h2 class="text-xl font-bold text-slate-900">
            {{ editingActivity ? 'Edit Activity' : 'Create New Activity' }}
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Enter the activity details below.
          </p>

        </div>

        <div class="p-6 space-y-5">

          <div>

            <label class="block text-sm font-bold text-slate-700 mb-2">
              Activity Name *
            </label>

            <input
              v-model="activityForm.name"
              type="text"
              placeholder="e.g. Fire Safety Inspection"
              class="w-full h-12 px-4 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]"
            />

          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

            <div>

              <label class="block text-sm font-bold text-slate-700 mb-2">
                Activity Type
              </label>

              <select
                v-model="activityForm.type"
                class="w-full h-12 px-4 rounded-xl border border-slate-300"
              >
                <option>Inspection</option>
                <option>Fire Drill</option>
                <option>Training</option>
                <option>Emergency Response</option>
              </select>

            </div>

            <div>

              <label class="block text-sm font-bold text-slate-700 mb-2">
                Assigned Personnel
              </label>

              <input
                v-model.number="activityForm.personnel"
                type="number"
                min="1"
                class="w-full h-12 px-4 rounded-xl border border-slate-300"
              />

            </div>

          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

            <div>

              <label class="block text-sm font-bold text-slate-700 mb-2">
                Schedule *
              </label>

              <input
                v-model="activityForm.schedule"
                type="date"
                class="w-full h-12 px-4 rounded-xl border border-slate-300"
              />

            </div>

            <div>

              <label class="block text-sm font-bold text-slate-700 mb-2">
                Time *
              </label>

              <input
                v-model="activityForm.time"
                type="time"
                class="w-full h-12 px-4 rounded-xl border border-slate-300"
              />

            </div>

          </div>

          <div>

            <label class="block text-sm font-bold text-slate-700 mb-2">
              Location *
            </label>

            <input
              v-model="activityForm.location"
              type="text"
              placeholder="Activity location"
              class="w-full h-12 px-4 rounded-xl border border-slate-300"
            />

          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

            <div>

              <label class="block text-sm font-bold text-slate-700 mb-2">
                Priority
              </label>

              <select
                v-model="activityForm.priority"
                class="w-full h-12 px-4 rounded-xl border border-slate-300"
              >
                <option>High</option>
                <option>Medium</option>
                <option>Low</option>
              </select>

            </div>

            <div>

              <label class="block text-sm font-bold text-slate-700 mb-2">
                Status
              </label>

              <select
                v-model="activityForm.status"
                class="w-full h-12 px-4 rounded-xl border border-slate-300"
              >
                <option>Scheduled</option>
                <option>Ongoing</option>
                <option>Completed</option>
                <option>Delayed</option>
              </select>

            </div>

          </div>

          <div>

            <label class="block text-sm font-bold text-slate-700 mb-2">
              Description
            </label>

            <textarea
              v-model="activityForm.description"
              rows="4"
              placeholder="Activity description or instructions..."
              class="w-full px-4 py-3 rounded-xl border border-slate-300 resize-none focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]"
            ></textarea>

          </div>

        </div>

        <div class="p-6 border-t border-slate-200 flex justify-end gap-3">

          <button
            @click="showActivityModal = false"
            class="px-5 py-2.5 rounded-xl border border-slate-300 text-slate-700 font-bold hover:bg-slate-50"
          >
            Cancel
          </button>

          <button
            @click="saveActivity"
            class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D]"
          >
            {{ editingActivity ? 'Save Changes' : 'Create Activity' }}
          </button>

        </div>

      </div>

    </div>


    <!-- =====================================================
         DETAILS MODAL
    ====================================================== -->

    <div
      v-if="showDetailsModal && selectedActivity"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div class="bg-white w-full max-w-xl rounded-2xl shadow-xl">

        <div class="p-6 border-b border-slate-200 flex justify-between">

          <div>

            <p class="text-xs font-bold text-[#8B1E23]">
              {{ selectedActivity.id }}
            </p>

            <h2 class="text-xl font-bold text-slate-900 mt-1">
              {{ selectedActivity.name }}
            </h2>

          </div>

          <button
            @click="showDetailsModal = false"
            class="text-slate-400 hover:text-slate-700 text-xl"
          >
            ×
          </button>

        </div>

        <div class="p-6 space-y-5">

          <div class="grid grid-cols-2 gap-4">

            <div>
              <p class="text-xs text-slate-400 uppercase font-bold">
                Type
              </p>

              <p class="font-semibold text-slate-800 mt-1">
                {{ selectedActivity.type }}
              </p>
            </div>

            <div>
              <p class="text-xs text-slate-400 uppercase font-bold">
                Personnel
              </p>

              <p class="font-semibold text-slate-800 mt-1">
                {{ selectedActivity.personnel }}
              </p>
            </div>

            <div>
              <p class="text-xs text-slate-400 uppercase font-bold">
                Schedule
              </p>

              <p class="font-semibold text-slate-800 mt-1">
                {{ formatDate(selectedActivity.schedule) }}
              </p>
            </div>

            <div>
              <p class="text-xs text-slate-400 uppercase font-bold">
                Time
              </p>

              <p class="font-semibold text-slate-800 mt-1">
                {{ formatTime(selectedActivity.time) }}
              </p>
            </div>

            <div>
              <p class="text-xs text-slate-400 uppercase font-bold">
                Priority
              </p>

              <span
                :class="getPriorityClass(selectedActivity.priority)"
                class="inline-block px-3 py-1 rounded-full text-xs font-bold mt-1"
              >
                {{ selectedActivity.priority }}
              </span>
            </div>

            <div>
              <p class="text-xs text-slate-400 uppercase font-bold">
                Status
              </p>

              <span
                :class="getStatusClass(selectedActivity.status)"
                class="inline-block px-3 py-1 rounded-full text-xs font-bold mt-1"
              >
                {{ selectedActivity.status }}
              </span>
            </div>

          </div>

          <div>

            <p class="text-xs text-slate-400 uppercase font-bold">
              Location
            </p>

            <p class="font-semibold text-slate-800 mt-1">
              {{ selectedActivity.location }}
            </p>

          </div>

          <div>

            <p class="text-xs text-slate-400 uppercase font-bold">
              Description
            </p>

            <p class="text-sm text-slate-600 mt-1">
              {{ selectedActivity.description || 'No description provided.' }}
            </p>

          </div>

          <div class="flex flex-wrap gap-2 pt-2">

            <button
              v-if="selectedActivity.status !== 'Ongoing'"
              @click="updateStatus(selectedActivity, 'Ongoing'); showDetailsModal = false"
              class="px-4 py-2 rounded-lg bg-blue-50 text-blue-700 text-sm font-bold"
            >
              Mark Ongoing
            </button>

            <button
              v-if="selectedActivity.status !== 'Completed'"
              @click="updateStatus(selectedActivity, 'Completed'); showDetailsModal = false"
              class="px-4 py-2 rounded-lg bg-green-50 text-green-700 text-sm font-bold"
            >
              Mark Completed
            </button>

          </div>

        </div>

      </div>

    </div>


    <!-- =====================================================
         DELETE MODAL
    ====================================================== -->

    <div
      v-if="showDeleteModal && selectedActivity"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div class="bg-white w-full max-w-md rounded-2xl shadow-xl p-6">

        <div class="w-12 h-12 rounded-full bg-red-50 text-[#8B1E23] flex items-center justify-center text-xl font-bold">
          !
        </div>

        <h2 class="text-xl font-bold text-slate-900 mt-4">
          Delete Activity?
        </h2>

        <p class="text-sm text-slate-500 mt-2">
          Are you sure you want to delete
          <strong>{{ selectedActivity.name }}</strong>?
          This action cannot be undone.
        </p>

        <div class="flex justify-end gap-3 mt-6">

          <button
            @click="showDeleteModal = false"
            class="px-5 py-2.5 rounded-xl border border-slate-300 font-bold text-slate-700"
          >
            Cancel
          </button>

          <button
            @click="deleteActivity"
            class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D]"
          >
            Delete Activity
          </button>

        </div>

      </div>

    </div>


    <!-- =====================================================
         TOAST
    ====================================================== -->

    <transition name="toast">

      <div
        v-if="toastMessage"
        class="fixed bottom-6 right-6 z-[60] bg-slate-900 text-white px-5 py-4 rounded-xl shadow-xl flex items-center gap-3"
      >

        <div
          :class="toastType === 'error'
            ? 'bg-red-500'
            : 'bg-green-500'"
          class="w-2 h-2 rounded-full"
        ></div>

        <p class="text-sm font-semibold">
          {{ toastMessage }}
        </p>

      </div>

    </transition>

  </div>
</template>

<style scoped>
.toast-enter-active,
.toast-leave-active {
  transition: all 0.25s ease;
}

.toast-enter-from,
.toast-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>