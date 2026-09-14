<script setup>
import { computed, ref } from 'vue'

defineProps({
  currentUser: {
    type: Object,
    default: null
  }
})

const searchQuery = ref('')
const selectedStatus = ref('All Status')
const selectedPriority = ref('All Priority')
const selectedRange = ref('All Deadlines')

const selectedDeadline = ref(null)
const selectedEscalation = ref(null)

const showDetailsModal = ref(false)
const showEscalationModal = ref(false)
const showResolveModal = ref(false)

const toastMessage = ref('')

const deadlines = ref([
  {
    id: 'DL-001',
    title: 'After-Operation Fire Incident Report',
    type: 'Incident Report',
    assignedTo: 'FO3 Juan Dela Cruz',
    station: 'BFP Balingasag',
    deadline: 'September 14, 2026',
    time: '08:00 AM',
    status: 'Overdue',
    priority: 'High',
    overdueBy: '2 hours',
    description:
      'Required after-operation report for the recent fire incident response.',
    escalationSent: false
  },
  {
    id: 'DL-002',
    title: 'Station Activity Report',
    type: 'Activity Report',
    assignedTo: 'FO2 Roberto Reyes',
    station: 'BFP Balingasag',
    deadline: 'September 14, 2026',
    time: '09:00 AM',
    status: 'Overdue',
    priority: 'High',
    overdueBy: '1 hour',
    description:
      'Daily station activity report covering completed and pending activities.',
    escalationSent: false
  },
  {
    id: 'DL-003',
    title: 'Weekly Accomplishment Report',
    type: 'Accomplishment Report',
    assignedTo: 'SFO1 Maria Santos',
    station: 'BFP Balingasag',
    deadline: 'September 15, 2026',
    time: '05:00 PM',
    status: 'Due Tomorrow',
    priority: 'Medium',
    overdueBy: null,
    description:
      'Weekly accomplishment report for station operations and personnel activities.',
    escalationSent: false
  },
  {
    id: 'DL-004',
    title: 'Monthly Compliance Report',
    type: 'Compliance Report',
    assignedTo: 'Station Administration',
    station: 'BFP Balingasag',
    deadline: 'September 19, 2026',
    time: '05:00 PM',
    status: 'Upcoming',
    priority: 'Medium',
    overdueBy: null,
    description:
      'Monthly compliance documentation for station operational requirements.',
    escalationSent: false
  },
  {
    id: 'DL-005',
    title: 'Barangay Fire Drill Summary',
    type: 'Activity Report',
    assignedTo: 'FO1 Carlo Garcia',
    station: 'BFP Balingasag',
    deadline: 'September 20, 2026',
    time: '04:00 PM',
    status: 'Upcoming',
    priority: 'Low',
    overdueBy: null,
    description:
      'Summary report for barangay fire drill attendance, observations, and results.',
    escalationSent: false
  },
  {
    id: 'DL-006',
    title: 'Equipment Inspection Report',
    type: 'Inspection Report',
    assignedTo: 'FO2 Mark Santos',
    station: 'BFP Balingasag',
    deadline: 'September 12, 2026',
    time: '03:00 PM',
    status: 'Completed',
    priority: 'Medium',
    overdueBy: null,
    description:
      'Inspection report for station firefighting equipment and safety resources.',
    escalationSent: false
  }
])

const escalations = ref([
  {
    id: 'ESC-001',
    title: 'After-Operation Fire Incident Report',
    description: 'Escalated to Station Operations Chief',
    priority: 'High',
    status: 'Pending',
    createdAt: 'September 14, 2026'
  },
  {
    id: 'ESC-002',
    title: 'Monthly Compliance Report',
    description: 'Pending review from Admin Office',
    priority: 'Medium',
    status: 'Pending',
    createdAt: 'September 13, 2026'
  },
  {
    id: 'ESC-003',
    title: 'Barangay Fire Drill Summary',
    description: 'Awaiting validation of attendance logs',
    priority: 'Low',
    status: 'Pending',
    createdAt: 'September 12, 2026'
  }
])

const filteredDeadlines = computed(() => {
  const query = searchQuery.value.toLowerCase().trim()

  return deadlines.value.filter(item => {
    const searchText = [
      item.title,
      item.type,
      item.assignedTo,
      item.station
    ]
      .join(' ')
      .toLowerCase()

    const matchesSearch =
      !query || searchText.includes(query)

    const matchesStatus =
      selectedStatus.value === 'All Status' ||
      item.status === selectedStatus.value

    const matchesPriority =
      selectedPriority.value === 'All Priority' ||
      item.priority === selectedPriority.value

    return matchesSearch && matchesStatus && matchesPriority
  })
})

const overdueCount = computed(() =>
  deadlines.value.filter(item => item.status === 'Overdue').length
)

const dueTodayCount = computed(() =>
  deadlines.value.filter(item => item.status === 'Due Today').length
)

const thisWeekCount = computed(() =>
  deadlines.value.filter(
    item =>
      ['Overdue', 'Due Today', 'Due Tomorrow', 'Upcoming'].includes(
        item.status
      )
  ).length
)

const completedCount = computed(() =>
  deadlines.value.filter(item => item.status === 'Completed').length
)

const pendingCount = computed(() =>
  deadlines.value.filter(
    item => item.status !== 'Completed'
  ).length
)

const escalationCount = computed(() =>
  escalations.value.filter(item => item.status === 'Pending').length
)

const onTimeRate = computed(() => {
  const completed = deadlines.value.filter(
    item => item.status === 'Completed'
  ).length

  if (!deadlines.value.length) return 0

  return Math.round(
    (completed / deadlines.value.length) * 100
  )
})

const resolvedBeforeDeadline = computed(() => {
  return Math.min(
    100,
    Math.max(0, onTimeRate.value + 8)
  )
})

const escalationRate = computed(() => {
  if (!deadlines.value.length) return 0

  return Math.round(
    (escalationCount.value / deadlines.value.length) * 100
  )
})

const hasFilters = computed(() =>
  searchQuery.value ||
  selectedStatus.value !== 'All Status' ||
  selectedPriority.value !== 'All Priority'
)

const clearFilters = () => {
  searchQuery.value = ''
  selectedStatus.value = 'All Status'
  selectedPriority.value = 'All Priority'
  selectedRange.value = 'All Deadlines'
}

const showToast = message => {
  toastMessage.value = message

  setTimeout(() => {
    toastMessage.value = ''
  }, 3000)
}

const viewDeadline = deadline => {
  selectedDeadline.value = deadline
  showDetailsModal.value = true
}

const sendEscalation = deadline => {
  selectedDeadline.value = deadline
  showEscalationModal.value = true
}

const confirmEscalation = () => {
  if (!selectedDeadline.value) return

  const deadline = deadlines.value.find(
    item => item.id === selectedDeadline.value.id
  )

  if (deadline) {
    deadline.escalationSent = true
  }

  const existing = escalations.value.find(
    item => item.title === selectedDeadline.value.title
  )

  if (!existing) {
    escalations.value.unshift({
      id: `ESC-${String(escalations.value.length + 1).padStart(3, '0')}`,
      title: selectedDeadline.value.title,
      description: 'Escalated to Station Operations Chief',
      priority: selectedDeadline.value.priority,
      status: 'Pending',
      createdAt: 'September 14, 2026'
    })
  }

  showEscalationModal.value = false

  showToast(
    `Escalation sent for "${selectedDeadline.value.title}".`
  )
}

const openResolve = deadline => {
  selectedDeadline.value = deadline
  showResolveModal.value = true
}

const resolveDeadline = () => {
  if (!selectedDeadline.value) return

  const deadline = deadlines.value.find(
    item => item.id === selectedDeadline.value.id
  )

  if (deadline) {
    deadline.status = 'Completed'
    deadline.overdueBy = null
  }

  showResolveModal.value = false

  showToast(
    `"${selectedDeadline.value.title}" marked as completed.`
  )
}

const sendReminder = deadline => {
  showToast(
    `Reminder sent to ${deadline.assignedTo}.`
  )
}

const viewEscalation = escalation => {
  selectedEscalation.value = escalation
}

const resolveEscalation = escalation => {
  escalation.status = 'Resolved'

  showToast(
    `Escalation for "${escalation.title}" resolved.`
  )
}

const getStatusClass = status => {
  const classes = {
    Overdue: 'bg-red-100 text-[#8B1E23]',
    'Due Today': 'bg-yellow-100 text-yellow-700',
    'Due Tomorrow': 'bg-amber-100 text-amber-700',
    Upcoming: 'bg-blue-100 text-blue-700',
    Completed: 'bg-green-100 text-green-700'
  }

  return classes[status] || 'bg-slate-100 text-slate-600'
}

const getPriorityClass = priority => {
  const classes = {
    High: 'bg-red-100 text-[#8B1E23]',
    Medium: 'bg-yellow-100 text-yellow-700',
    Low: 'bg-blue-100 text-blue-700'
  }

  return classes[priority] || 'bg-slate-100 text-slate-600'
}
</script>

<template>
  <div class="space-y-6">

    <!-- HEADER -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col xl:flex-row xl:items-center xl:justify-between gap-5">
        <div>
          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">
            Compliance Monitoring
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Deadline Monitor
          </h2>

          <p class="text-base text-slate-500 mt-1">
            Track upcoming, due, and overdue report deadlines.
          </p>
        </div>

        <div class="flex flex-wrap gap-3">
          <button
            @click="clearFilters"
            class="px-5 py-3 rounded-xl border border-slate-300 text-slate-700 font-bold hover:bg-slate-50 transition"
          >
            Reset Filters
          </button>

          <button
            @click="showToast('Deadline monitoring refreshed.')"
            class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition"
          >
            Refresh Monitor
          </button>
        </div>
      </div>
    </section>

    <!-- STATS -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-5">

      <div class="bg-white border border-red-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">
          {{ String(overdueCount).padStart(2, '0') }}
        </p>
        <p class="text-sm text-slate-500 mt-1">
          Overdue
        </p>
      </div>

      <div class="bg-white border border-yellow-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">
          {{ String(dueTodayCount).padStart(2, '0') }}
        </p>
        <p class="text-sm text-slate-500 mt-1">
          Due Today
        </p>
      </div>

      <div class="bg-white border border-blue-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-blue-600">
          {{ String(thisWeekCount).padStart(2, '0') }}
        </p>
        <p class="text-sm text-slate-500 mt-1">
          This Week
        </p>
      </div>

      <div class="bg-white border border-green-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">
          {{ String(completedCount).padStart(2, '0') }}
        </p>
        <p class="text-sm text-slate-500 mt-1">
          Completed
        </p>
      </div>

      <div class="bg-white border border-purple-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-purple-600">
          {{ String(escalationCount).padStart(2, '0') }}
        </p>
        <p class="text-sm text-slate-500 mt-1">
          Escalations
        </p>
      </div>

    </section>

    <!-- FILTERS -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">
      <div class="flex flex-col xl:flex-row gap-4">

        <div class="flex-1">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search deadline, report, personnel..."
            class="w-full h-12 px-4 rounded-xl border border-slate-300 text-base outline-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
          />
        </div>

        <select
          v-model="selectedStatus"
          class="h-12 px-4 rounded-xl border border-slate-300 text-base bg-white"
        >
          <option>All Status</option>
          <option>Overdue</option>
          <option>Due Today</option>
          <option>Due Tomorrow</option>
          <option>Upcoming</option>
          <option>Completed</option>
        </select>

        <select
          v-model="selectedPriority"
          class="h-12 px-4 rounded-xl border border-slate-300 text-base bg-white"
        >
          <option>All Priority</option>
          <option>High</option>
          <option>Medium</option>
          <option>Low</option>
        </select>

        <select
          v-model="selectedRange"
          class="h-12 px-4 rounded-xl border border-slate-300 text-base bg-white"
        >
          <option>All Deadlines</option>
          <option>Today</option>
          <option>This Week</option>
          <option>This Month</option>
        </select>

        <button
          v-if="hasFilters"
          @click="clearFilters"
          class="h-12 px-5 rounded-xl bg-slate-100 text-slate-700 font-bold hover:bg-slate-200"
        >
          Clear
        </button>

      </div>

      <div class="mt-4 flex justify-between items-center">
        <p class="text-sm text-slate-500">
          Showing
          <span class="font-bold text-slate-800">
            {{ filteredDeadlines.length }}
          </span>
          deadline records
        </p>

        <p class="text-sm font-semibold text-[#8B1E23]">
          {{ pendingCount }} pending
        </p>
      </div>
    </section>

    <!-- OVERDUE -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex items-center gap-3">
        <div class="h-11 w-11 rounded-xl bg-red-50 flex items-center justify-center text-xl">
          🚨
        </div>

        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Overdue Deadlines
          </h2>

          <p class="text-sm text-slate-500">
            Immediate administrative attention required
          </p>
        </div>
      </div>

      <div class="mt-5 space-y-3">

        <div
          v-for="deadline in filteredDeadlines.filter(item => item.status === 'Overdue')"
          :key="deadline.id"
          class="p-5 rounded-xl bg-red-50 border border-red-200"
        >
          <div class="flex flex-col xl:flex-row xl:items-center xl:justify-between gap-4">

            <div>
              <div class="flex flex-wrap items-center gap-2">
                <p class="font-bold text-slate-900">
                  {{ deadline.title }}
                </p>

                <span
                  :class="[
                    'px-2.5 py-1 rounded-full text-xs font-bold',
                    getPriorityClass(deadline.priority)
                  ]"
                >
                  {{ deadline.priority }}
                </span>
              </div>

              <p class="text-sm text-[#8B1E23] mt-1">
                Assigned to {{ deadline.assignedTo }}
              </p>

              <p class="text-sm text-[#8B1E23] mt-1 font-semibold">
                Overdue by {{ deadline.overdueBy }}
              </p>
            </div>

            <div class="flex flex-wrap gap-2">

              <button
                @click="viewDeadline(deadline)"
                class="px-4 py-2.5 rounded-lg bg-white border border-slate-300 text-sm font-bold hover:bg-slate-50"
              >
                View
              </button>

              <button
                @click="sendReminder(deadline)"
                class="px-4 py-2.5 rounded-lg border border-[#8B1E23] text-[#8B1E23] text-sm font-bold hover:bg-red-100"
              >
                Reminder
              </button>

              <button
                @click="sendEscalation(deadline)"
                class="px-5 py-2.5 rounded-lg bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]"
              >
                {{ deadline.escalationSent ? 'Escalated' : 'Send Escalation' }}
              </button>

              <button
                @click="openResolve(deadline)"
                class="px-4 py-2.5 rounded-lg bg-green-600 text-white text-sm font-bold hover:bg-green-700"
              >
                Resolve
              </button>

            </div>
          </div>
        </div>

        <div
          v-if="!filteredDeadlines.some(item => item.status === 'Overdue')"
          class="text-center py-10 text-slate-500"
        >
          <div class="text-4xl mb-2">✓</div>
          <p class="font-bold text-slate-700">
            No overdue deadlines
          </p>
          <p class="text-sm mt-1">
            All monitored deadlines are currently within schedule.
          </p>
        </div>

      </div>
    </section>

    <!-- UPCOMING -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Upcoming Deadlines
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Reports approaching their submission deadline
          </p>
        </div>

        <span class="text-sm font-bold text-slate-500">
          {{ filteredDeadlines.length }} records
        </span>
      </div>

      <div class="mt-5 space-y-3">

        <div
          v-for="deadline in filteredDeadlines.filter(item => item.status !== 'Overdue')"
          :key="deadline.id"
          class="flex flex-col xl:flex-row xl:items-center xl:justify-between gap-4 p-5 rounded-xl border border-slate-200 hover:bg-slate-50 transition"
        >

          <div class="flex-1">

            <div class="flex flex-wrap items-center gap-2">
              <p class="font-bold text-slate-900">
                {{ deadline.title }}
              </p>

              <span
                :class="[
                  'px-3 py-1 rounded-full text-xs font-bold',
                  getStatusClass(deadline.status)
                ]"
              >
                {{ deadline.status }}
              </span>
            </div>

            <p class="text-sm text-slate-500 mt-1">
              {{ deadline.type }} • {{ deadline.assignedTo }}
            </p>

            <p class="text-sm text-slate-400 mt-1">
              Deadline: {{ deadline.deadline }} • {{ deadline.time }}
            </p>

          </div>

          <div class="flex flex-wrap gap-2">

            <button
              @click="viewDeadline(deadline)"
              class="px-4 py-2.5 rounded-lg border border-slate-300 text-sm font-bold hover:bg-slate-100"
            >
              View
            </button>

            <button
              v-if="deadline.status !== 'Completed'"
              @click="sendReminder(deadline)"
              class="px-4 py-2.5 rounded-lg bg-yellow-500 text-white text-sm font-bold hover:bg-yellow-600"
            >
              Send Reminder
            </button>

          </div>

        </div>

      </div>
    </section>

    <!-- ANALYTICS + ESCALATION -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- TRENDS -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="border-b border-slate-200 pb-5">
          <h2 class="text-xl font-bold text-slate-900">
            Deadline Trends
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Current monitoring performance
          </p>
        </div>

        <div class="mt-5 space-y-5">

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>On-Time Rate</span>
              <span>{{ onTimeRate }}%</span>
            </div>

            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div
                class="h-full rounded-full bg-emerald-500 transition-all"
                :style="{ width: `${onTimeRate}%` }"
              ></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Escalation Rate</span>
              <span>{{ escalationRate }}%</span>
            </div>

            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div
                class="h-full rounded-full bg-red-500 transition-all"
                :style="{ width: `${escalationRate}%` }"
              ></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Resolved Before Deadline</span>
              <span>{{ resolvedBeforeDeadline }}%</span>
            </div>

            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div
                class="h-full rounded-full bg-blue-500 transition-all"
                :style="{ width: `${resolvedBeforeDeadline}%` }"
              ></div>
            </div>
          </div>

        </div>
      </div>

      <!-- ESCALATION -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="border-b border-slate-200 pb-5">
          <h2 class="text-xl font-bold text-slate-900">
            Escalation Queue
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Reports needing higher-level action
          </p>
        </div>

        <div class="mt-5 space-y-4">

          <div
            v-for="escalation in escalations"
            :key="escalation.id"
            class="p-4 rounded-xl border border-slate-200"
          >

            <div class="flex justify-between gap-3">

              <div>
                <p class="font-bold text-slate-900">
                  {{ escalation.title }}
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  {{ escalation.description }}
                </p>

                <p class="text-xs text-slate-400 mt-1">
                  {{ escalation.createdAt }}
                </p>
              </div>

              <span
                :class="[
                  'h-fit px-2.5 py-1 rounded-full text-xs font-bold',
                  getPriorityClass(escalation.priority)
                ]"
              >
                {{ escalation.priority }}
              </span>

            </div>

            <div class="flex gap-2 mt-3">

              <button
                @click="viewEscalation(escalation)"
                class="px-3 py-2 rounded-lg border border-slate-300 text-xs font-bold hover:bg-slate-50"
              >
                View
              </button>

              <button
                v-if="escalation.status === 'Pending'"
                @click="resolveEscalation(escalation)"
                class="px-3 py-2 rounded-lg bg-green-600 text-white text-xs font-bold hover:bg-green-700"
              >
                Mark Resolved
              </button>

              <span
                v-else
                class="px-3 py-2 rounded-lg bg-green-50 text-green-700 text-xs font-bold"
              >
                Resolved
              </span>

            </div>

          </div>

        </div>
      </div>

    </section>

    <!-- COMPLIANCE NOTES -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="border-b border-slate-200 pb-5">
        <h2 class="text-xl font-bold text-slate-900">
          Compliance Notes
        </h2>

        <p class="text-sm text-slate-500 mt-1">
          Operational reminders and monitoring details
        </p>
      </div>

      <div class="mt-5 grid grid-cols-1 lg:grid-cols-3 gap-4">

        <div class="p-4 rounded-xl border border-emerald-200 bg-emerald-50">
          <p class="text-sm font-bold text-slate-900">
            Monitoring Reminder
          </p>

          <p class="text-sm text-slate-600 mt-1">
            Review approaching deadlines daily to minimize late submissions.
          </p>
        </div>

        <div class="p-4 rounded-xl border border-orange-200 bg-orange-50">
          <p class="text-sm font-bold text-slate-900">
            Attention Required
          </p>

          <p class="text-sm text-slate-600 mt-1">
            {{ overdueCount }} overdue report(s) currently require administrative action.
          </p>
        </div>

        <div class="p-4 rounded-xl border border-indigo-200 bg-indigo-50">
          <p class="text-sm font-bold text-slate-900">
            Follow-Up
          </p>

          <p class="text-sm text-slate-600 mt-1">
            Confirm that escalated reports receive proper supervisor action and documentation.
          </p>
        </div>

      </div>
    </section>

    <!-- DETAILS MODAL -->
    <div
      v-if="showDetailsModal && selectedDeadline"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
      @click.self="showDetailsModal = false"
    >

      <div class="bg-white rounded-2xl shadow-xl w-full max-w-2xl">

        <div class="p-6 border-b border-slate-200 flex justify-between items-start">

          <div>
            <p class="text-xs font-bold uppercase text-[#8B1E23]">
              Deadline Details
            </p>

            <h3 class="text-xl font-bold text-slate-900 mt-1">
              {{ selectedDeadline.title }}
            </h3>
          </div>

          <button
            @click="showDetailsModal = false"
            class="text-slate-400 hover:text-slate-700 text-xl"
          >
            ✕
          </button>

        </div>

        <div class="p-6 space-y-4">

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-500">Report Type</p>
              <p class="font-bold text-slate-900 mt-1">
                {{ selectedDeadline.type }}
              </p>
            </div>

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-500">Assigned Personnel</p>
              <p class="font-bold text-slate-900 mt-1">
                {{ selectedDeadline.assignedTo }}
              </p>
            </div>

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-500">Deadline</p>
              <p class="font-bold text-slate-900 mt-1">
                {{ selectedDeadline.deadline }}
              </p>
            </div>

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-500">Time</p>
              <p class="font-bold text-slate-900 mt-1">
                {{ selectedDeadline.time }}
              </p>
            </div>

          </div>

          <div>
            <p class="text-sm font-bold text-slate-700">
              Description
            </p>

            <p class="text-sm text-slate-600 mt-1">
              {{ selectedDeadline.description }}
            </p>
          </div>

        </div>

        <div class="p-6 border-t border-slate-200 flex justify-end gap-3">

          <button
            @click="showDetailsModal = false"
            class="px-5 py-2.5 rounded-xl border border-slate-300 font-bold"
          >
            Close
          </button>

          <button
            v-if="selectedDeadline.status === 'Overdue'"
            @click="showDetailsModal = false; sendEscalation(selectedDeadline)"
            class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white font-bold"
          >
            Send Escalation
          </button>

        </div>

      </div>
    </div>

    <!-- ESCALATION MODAL -->
    <div
      v-if="showEscalationModal && selectedDeadline"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
      @click.self="showEscalationModal = false"
    >

      <div class="bg-white rounded-2xl shadow-xl w-full max-w-lg">

        <div class="p-6">
          <p class="text-xs font-bold uppercase text-[#8B1E23]">
            Escalation Confirmation
          </p>

          <h3 class="text-xl font-bold text-slate-900 mt-1">
            Send Escalation?
          </h3>

          <p class="text-sm text-slate-500 mt-2">
            This will create an escalation record for:
          </p>

          <div class="mt-4 p-4 rounded-xl bg-red-50 border border-red-200">
            <p class="font-bold text-slate-900">
              {{ selectedDeadline.title }}
            </p>

            <p class="text-sm text-[#8B1E23] mt-1">
              Assigned to {{ selectedDeadline.assignedTo }}
            </p>
          </div>
        </div>

        <div class="p-6 border-t border-slate-200 flex justify-end gap-3">

          <button
            @click="showEscalationModal = false"
            class="px-5 py-2.5 rounded-xl border border-slate-300 font-bold"
          >
            Cancel
          </button>

          <button
            @click="confirmEscalation"
            class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white font-bold"
          >
            Confirm Escalation
          </button>

        </div>

      </div>
    </div>

    <!-- RESOLVE MODAL -->
    <div
      v-if="showResolveModal && selectedDeadline"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
      @click.self="showResolveModal = false"
    >

      <div class="bg-white rounded-2xl shadow-xl w-full max-w-lg">

        <div class="p-6">

          <div class="h-12 w-12 rounded-full bg-green-100 text-green-700 flex items-center justify-center text-xl">
            ✓
          </div>

          <h3 class="text-xl font-bold text-slate-900 mt-4">
            Mark Deadline as Completed?
          </h3>

          <p class="text-sm text-slate-500 mt-2">
            Confirm that the required report has been submitted and reviewed.
          </p>

          <div class="mt-4 p-4 rounded-xl bg-slate-50">
            <p class="font-bold text-slate-900">
              {{ selectedDeadline.title }}
            </p>
          </div>

        </div>

        <div class="p-6 border-t border-slate-200 flex justify-end gap-3">

          <button
            @click="showResolveModal = false"
            class="px-5 py-2.5 rounded-xl border border-slate-300 font-bold"
          >
            Cancel
          </button>

          <button
            @click="resolveDeadline"
            class="px-5 py-2.5 rounded-xl bg-green-600 text-white font-bold hover:bg-green-700"
          >
            Confirm Complete
          </button>

        </div>

      </div>
    </div>

    <!-- ESCALATION DETAIL -->
    <div
      v-if="selectedEscalation"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
      @click.self="selectedEscalation = null"
    >

      <div class="bg-white rounded-2xl shadow-xl w-full max-w-lg">

        <div class="p-6">

          <p class="text-xs font-bold uppercase text-[#8B1E23]">
            Escalation Details
          </p>

          <h3 class="text-xl font-bold text-slate-900 mt-1">
            {{ selectedEscalation.title }}
          </h3>

          <div class="mt-5 space-y-3">

            <div>
              <p class="text-xs text-slate-500">
                Priority
              </p>

              <span
                :class="[
                  'inline-block mt-1 px-3 py-1 rounded-full text-xs font-bold',
                  getPriorityClass(selectedEscalation.priority)
                ]"
              >
                {{ selectedEscalation.priority }}
              </span>
            </div>

            <div>
              <p class="text-xs text-slate-500">
                Status
              </p>

              <p class="font-bold text-slate-900 mt-1">
                {{ selectedEscalation.status }}
              </p>
            </div>

            <div>
              <p class="text-xs text-slate-500">
                Details
              </p>

              <p class="text-sm text-slate-600 mt-1">
                {{ selectedEscalation.description }}
              </p>
            </div>

          </div>

        </div>

        <div class="p-6 border-t border-slate-200 flex justify-end gap-3">

          <button
            @click="selectedEscalation = null"
            class="px-5 py-2.5 rounded-xl border border-slate-300 font-bold"
          >
            Close
          </button>

        </div>

      </div>
    </div>

    <!-- TOAST -->
    <Transition
      enter-active-class="transition duration-200"
      enter-from-class="opacity-0 translate-y-2"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition duration-200"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="toastMessage"
        class="fixed bottom-6 right-6 z-[60] bg-slate-900 text-white px-5 py-3 rounded-xl shadow-lg font-semibold"
      >
        {{ toastMessage }}
      </div>
    </Transition>

  </div>
</template>