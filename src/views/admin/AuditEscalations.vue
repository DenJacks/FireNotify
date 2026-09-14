<script setup>
import { ref, computed, onMounted } from 'vue'

const props = defineProps({
  currentUser: {
    type: Object,
    required: false,
    default: null
  }
})

const STORAGE_KEY = 'fireNotifyAuditEscalations'

const findings = ref([])
const escalations = ref([])

const searchQuery = ref('')
const findingStatusFilter = ref('All')
const priorityFilter = ref('All')

const showAddModal = ref(false)
const showEditModal = ref(false)
const showDetailsModal = ref(false)
const showDeleteModal = ref(false)
const showEscalateModal = ref(false)

const selectedFinding = ref(null)

const toastMessage = ref('')
const showToast = ref(false)

const form = ref({
  title: '',
  category: 'Documentation',
  description: '',
  personnel: '',
  priority: 'Medium',
  status: 'Open',
  dueDate: '',
  notes: ''
})

const defaultFindings = [
  {
    id: 'AUD-001',
    title: 'Documentation Gap',
    category: 'Documentation',
    description: 'Two submitted reports were missing attachment references.',
    personnel: 'Station Administration',
    priority: 'Medium',
    status: 'Open',
    dueDate: '2026-09-15',
    notes: 'Review supporting documents before final approval.'
  },
  {
    id: 'AUD-002',
    title: 'Equipment Check Delay',
    category: 'Equipment',
    description: 'One station missed its scheduled maintenance verification window.',
    personnel: 'FO2 A. Villanueva',
    priority: 'Low',
    status: 'Open',
    dueDate: '2026-09-16',
    notes: 'Coordinate with equipment custodian.'
  },
  {
    id: 'AUD-003',
    title: 'Training Completion',
    category: 'Training',
    description: 'All new personnel completed required orientation modules.',
    personnel: 'Personnel Division',
    priority: 'Low',
    status: 'Resolved',
    dueDate: '2026-09-10',
    notes: 'Training requirement successfully completed.'
  },
  {
    id: 'AUD-004',
    title: 'Late Fire Incident Report',
    category: 'Reporting',
    description: 'Fire incident report was not submitted within the required reporting period.',
    personnel: 'FO3 Juan Dela Cruz',
    priority: 'High',
    status: 'Escalated',
    dueDate: '2026-09-14',
    notes: 'Supervisor review required.'
  },
  {
    id: 'AUD-005',
    title: 'Incomplete Compliance Documents',
    category: 'Compliance',
    description: 'Three required documents are still incomplete for the monthly compliance review.',
    personnel: 'Admin Office',
    priority: 'Medium',
    status: 'Escalated',
    dueDate: '2026-09-17',
    notes: 'Follow up with responsible personnel.'
  },
  {
    id: 'AUD-006',
    title: 'Missing Attendance Validation',
    category: 'Activity',
    description: 'Barangay drill attendance logs are awaiting validation and signatures.',
    personnel: 'FO1 Carlo Garcia',
    priority: 'Low',
    status: 'Open',
    dueDate: '2026-09-18',
    notes: 'Validate attendance records.'
  }
]

const defaultEscalations = [
  {
    id: 'ESC-001',
    findingId: 'AUD-004',
    title: 'Late Fire Incident Report',
    description: 'Assigned to FO3 Juan Dela Cruz • 2 hours overdue',
    priority: 'High',
    status: 'Pending',
    assignedTo: 'Station Supervisor'
  },
  {
    id: 'ESC-002',
    findingId: 'AUD-005',
    title: 'Monthly Compliance Report',
    description: 'Pending review from Admin Office • 3 documents incomplete',
    priority: 'Medium',
    status: 'Pending',
    assignedTo: 'Admin Officer'
  },
  {
    id: 'ESC-003',
    findingId: 'AUD-006',
    title: 'Barangay Drill Attendance Review',
    description: 'Awaiting validation of attendance logs and signatures',
    priority: 'Low',
    status: 'Pending',
    assignedTo: 'Operations Officer'
  }
]

const loadData = () => {
  const saved = localStorage.getItem(STORAGE_KEY)

  if (saved) {
    try {
      const data = JSON.parse(saved)

      findings.value = data.findings || defaultFindings
      escalations.value = data.escalations || defaultEscalations

      return
    } catch (error) {
      console.error('Failed to load audit data:', error)
    }
  }

  findings.value = defaultFindings
  escalations.value = defaultEscalations

  saveData()
}

const saveData = () => {
  localStorage.setItem(
    STORAGE_KEY,
    JSON.stringify({
      findings: findings.value,
      escalations: escalations.value
    })
  )
}

onMounted(() => {
  loadData()
})

/* =========================================================
   COMPUTED DATA
========================================================= */

const filteredFindings = computed(() => {
  const query = searchQuery.value.toLowerCase().trim()

  return findings.value.filter(item => {
    const matchesSearch =
      !query ||
      item.title.toLowerCase().includes(query) ||
      item.description.toLowerCase().includes(query) ||
      item.personnel.toLowerCase().includes(query) ||
      item.category.toLowerCase().includes(query)

    const matchesStatus =
      findingStatusFilter.value === 'All' ||
      item.status === findingStatusFilter.value

    const matchesPriority =
      priorityFilter.value === 'All' ||
      item.priority === priorityFilter.value

    return matchesSearch && matchesStatus && matchesPriority
  })
})

const openFindings = computed(() =>
  findings.value.filter(item =>
    item.status === 'Open' || item.status === 'Escalated'
  ).length
)

const escalatedCount = computed(() =>
  findings.value.filter(item => item.status === 'Escalated').length
)

const resolvedCount = computed(() =>
  findings.value.filter(item => item.status === 'Resolved').length
)

const pendingReviews = computed(() =>
  findings.value.filter(item => item.status === 'Open').length
)

const resolutionRate = computed(() => {
  if (!findings.value.length) return 0

  return Math.round(
    (resolvedCount.value / findings.value.length) * 100
  )
})

const pendingEscalations = computed(() =>
  escalations.value.filter(item => item.status === 'Pending')
)

const highPriorityCount = computed(() =>
  findings.value.filter(item => item.priority === 'High').length
)

/* =========================================================
   FORM
========================================================= */

const resetForm = () => {
  form.value = {
    title: '',
    category: 'Documentation',
    description: '',
    personnel: '',
    priority: 'Medium',
    status: 'Open',
    dueDate: '',
    notes: ''
  }
}

const openAddModal = () => {
  resetForm()
  showAddModal.value = true
}

const addFinding = () => {
  if (
    !form.value.title.trim() ||
    !form.value.description.trim() ||
    !form.value.personnel.trim()
  ) {
    showNotification('Please complete the required fields.')
    return
  }

  const newFinding = {
    id: `AUD-${String(findings.value.length + 1).padStart(3, '0')}`,
    title: form.value.title,
    category: form.value.category,
    description: form.value.description,
    personnel: form.value.personnel,
    priority: form.value.priority,
    status: form.value.status,
    dueDate: form.value.dueDate,
    notes: form.value.notes
  }

  findings.value.unshift(newFinding)

  saveData()

  showAddModal.value = false

  showNotification('Audit finding added successfully.')
}

const openEditModal = finding => {
  selectedFinding.value = finding

  form.value = {
    title: finding.title,
    category: finding.category,
    description: finding.description,
    personnel: finding.personnel,
    priority: finding.priority,
    status: finding.status,
    dueDate: finding.dueDate || '',
    notes: finding.notes || ''
  }

  showEditModal.value = true
}

const updateFinding = () => {
  if (
    !form.value.title.trim() ||
    !form.value.description.trim() ||
    !form.value.personnel.trim()
  ) {
    showNotification('Please complete the required fields.')
    return
  }

  const index = findings.value.findIndex(
    item => item.id === selectedFinding.value.id
  )

  if (index !== -1) {
    findings.value[index] = {
      ...findings.value[index],
      title: form.value.title,
      category: form.value.category,
      description: form.value.description,
      personnel: form.value.personnel,
      priority: form.value.priority,
      status: form.value.status,
      dueDate: form.value.dueDate,
      notes: form.value.notes
    }
  }

  saveData()

  showEditModal.value = false

  showNotification('Audit finding updated.')
}

/* =========================================================
   DETAILS
========================================================= */

const openDetails = finding => {
  selectedFinding.value = finding
  showDetailsModal.value = true
}

/* =========================================================
   DELETE
========================================================= */

const openDeleteModal = finding => {
  selectedFinding.value = finding
  showDeleteModal.value = true
}

const deleteFinding = () => {
  const id = selectedFinding.value.id

  findings.value = findings.value.filter(
    item => item.id !== id
  )

  escalations.value = escalations.value.filter(
    item => item.findingId !== id
  )

  saveData()

  showDeleteModal.value = false

  showNotification('Audit finding deleted.')
}

/* =========================================================
   STATUS
========================================================= */

const resolveFinding = finding => {
  const item = findings.value.find(
    record => record.id === finding.id
  )

  if (!item) return

  item.status = 'Resolved'

  const escalation = escalations.value.find(
    record => record.findingId === finding.id
  )

  if (escalation) {
    escalation.status = 'Resolved'
  }

  saveData()

  showNotification('Finding marked as resolved.')
}

/* =========================================================
   ESCALATION
========================================================= */

const openEscalateModal = finding => {
  selectedFinding.value = finding
  showEscalateModal.value = true
}

const confirmEscalation = () => {
  if (!selectedFinding.value) return

  const finding = findings.value.find(
    item => item.id === selectedFinding.value.id
  )

  if (!finding) return

  finding.status = 'Escalated'

  const existingEscalation = escalations.value.find(
    item => item.findingId === finding.id &&
      item.status === 'Pending'
  )

  if (!existingEscalation) {
    escalations.value.unshift({
      id: `ESC-${String(escalations.value.length + 1).padStart(3, '0')}`,
      findingId: finding.id,
      title: finding.title,
      description: `${finding.personnel} • Requires higher-level attention`,
      priority: finding.priority,
      status: 'Pending',
      assignedTo: 'Station Supervisor'
    })
  }

  saveData()

  showEscalateModal.value = false

  showNotification('Finding escalated successfully.')
}

const resolveEscalation = escalation => {
  const item = escalations.value.find(
    record => record.id === escalation.id
  )

  if (!item) return

  item.status = 'Resolved'

  const finding = findings.value.find(
    record => record.id === escalation.findingId
  )

  if (finding) {
    finding.status = 'Resolved'
  }

  saveData()

  showNotification('Escalation resolved.')
}

/* =========================================================
   UTILITIES
========================================================= */

const showNotification = message => {
  toastMessage.value = message
  showToast.value = true

  setTimeout(() => {
    showToast.value = false
  }, 2500)
}

const clearFilters = () => {
  searchQuery.value = ''
  findingStatusFilter.value = 'All'
  priorityFilter.value = 'All'
}

const formatDate = date => {
  if (!date) return 'No deadline'

  return new Date(`${date}T00:00:00`).toLocaleDateString(
    'en-US',
    {
      month: 'short',
      day: 'numeric',
      year: 'numeric'
    }
  )
}

const priorityClass = priority => {
  if (priority === 'High') {
    return 'bg-red-100 text-red-700'
  }

  if (priority === 'Medium') {
    return 'bg-yellow-100 text-yellow-700'
  }

  return 'bg-blue-100 text-blue-700'
}

const statusClass = status => {
  if (status === 'Resolved') {
    return 'bg-green-100 text-green-700'
  }

  if (status === 'Escalated') {
    return 'bg-red-100 text-red-700'
  }

  return 'bg-yellow-100 text-yellow-700'
}

const categoryClass = category => {
  const classes = {
    Documentation: 'bg-purple-100 text-purple-700',
    Equipment: 'bg-blue-100 text-blue-700',
    Training: 'bg-green-100 text-green-700',
    Reporting: 'bg-red-100 text-red-700',
    Compliance: 'bg-orange-100 text-orange-700',
    Activity: 'bg-indigo-100 text-indigo-700'
  }

  return classes[category] || 'bg-slate-100 text-slate-700'
}

const exportAuditReport = () => {
  const rows = findings.value.map(item => ({
    ID: item.id,
    Finding: item.title,
    Category: item.category,
    Personnel: item.personnel,
    Priority: item.priority,
    Status: item.status,
    Deadline: item.dueDate
  }))

  const header = Object.keys(rows[0] || {
    ID: '',
    Finding: '',
    Category: '',
    Personnel: '',
    Priority: '',
    Status: '',
    Deadline: ''
  })

  const csv = [
    header.join(','),
    ...rows.map(row =>
      header
        .map(key => `"${String(row[key] ?? '').replace(/"/g, '""')}"`)
        .join(',')
    )
  ].join('\n')

  const blob = new Blob([csv], {
    type: 'text/csv;charset=utf-8;'
  })

  const url = URL.createObjectURL(blob)

  const link = document.createElement('a')
  link.href = url
  link.download = 'FireNotify-Audit-Report.csv'
  link.click()

  URL.revokeObjectURL(url)

  showNotification('Audit report exported.')
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
            Governance Overview
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Audit & Escalations
          </h2>

          <p class="text-base text-slate-500 mt-1">
            Review compliance checks, investigate findings, and monitor escalated cases.
          </p>
        </div>

        <div class="flex gap-3">

          <button
            @click="exportAuditReport"
            class="px-5 py-3 rounded-xl border border-slate-300 bg-white text-slate-700 font-bold hover:bg-slate-100 transition"
          >
            Export Audit Report
          </button>

          <button
            @click="openAddModal"
            class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition"
          >
            + Add Finding
          </button>

        </div>

      </div>
    </section>

    <!-- STATS -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">
          {{ openFindings }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Open Findings
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">
          {{ escalatedCount }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Escalated
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">
          {{ resolutionRate }}%
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Resolution Rate
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-blue-600">
          {{ pendingReviews }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Pending Reviews
        </p>
      </div>

    </section>

    <!-- SEARCH / FILTER -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

      <div class="flex flex-col lg:flex-row gap-4">

        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search findings, personnel, category..."
          class="flex-1 px-4 py-3 border border-slate-200 rounded-xl outline-none focus:border-[#8B1E23]"
        />

        <select
          v-model="findingStatusFilter"
          class="px-4 py-3 border border-slate-200 rounded-xl bg-white outline-none"
        >
          <option value="All">All Status</option>
          <option value="Open">Open</option>
          <option value="Escalated">Escalated</option>
          <option value="Resolved">Resolved</option>
        </select>

        <select
          v-model="priorityFilter"
          class="px-4 py-3 border border-slate-200 rounded-xl bg-white outline-none"
        >
          <option value="All">All Priority</option>
          <option value="High">High</option>
          <option value="Medium">Medium</option>
          <option value="Low">Low</option>
        </select>

        <button
          @click="clearFilters"
          class="px-5 py-3 rounded-xl border border-slate-200 font-bold text-slate-700 hover:bg-slate-50"
        >
          Clear
        </button>

      </div>

      <div class="flex flex-wrap justify-between gap-3 mt-4 text-sm text-slate-500">

        <span>
          Showing
          <strong class="text-slate-900">
            {{ filteredFindings.length }}
          </strong>
          findings
        </span>

        <span>
          High Priority:
          <strong class="text-red-600">
            {{ highPriorityCount }}
          </strong>
        </span>

      </div>

    </section>

    <!-- ESCALATION + FINDINGS -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- ESCALATION QUEUE -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">

          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Escalation Queue
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              Cases requiring higher-level attention
            </p>
          </div>

          <span class="px-3 py-1 rounded-full bg-red-100 text-red-700 text-xs font-bold">
            {{ pendingEscalations.length }} Pending
          </span>

        </div>

        <div class="mt-5 space-y-4">

          <div
            v-for="item in pendingEscalations"
            :key="item.id"
            class="p-4 rounded-xl border"
            :class="
              item.priority === 'High'
                ? 'border-red-200 bg-red-50'
                : item.priority === 'Medium'
                  ? 'border-yellow-200 bg-yellow-50'
                  : 'border-blue-200 bg-blue-50'
            "
          >

            <div class="flex justify-between gap-3">

              <div>
                <p class="font-bold text-slate-900">
                  {{ item.title }}
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  {{ item.description }}
                </p>

                <p class="text-xs text-slate-400 mt-2">
                  Assigned to: {{ item.assignedTo }}
                </p>
              </div>

              <span
                class="h-fit px-2.5 py-1 rounded-full text-xs font-bold"
                :class="priorityClass(item.priority)"
              >
                {{ item.priority }}
              </span>

            </div>

            <div class="flex justify-end mt-3">

              <button
                @click="resolveEscalation(item)"
                class="px-3 py-2 rounded-lg bg-green-100 text-green-700 text-xs font-bold hover:bg-green-200"
              >
                Resolve
              </button>

            </div>

          </div>

          <div
            v-if="pendingEscalations.length === 0"
            class="py-10 text-center"
          >
            <p class="text-3xl">
              ✓
            </p>

            <p class="font-bold text-slate-700 mt-2">
              No pending escalations
            </p>

            <p class="text-sm text-slate-500 mt-1">
              All escalated cases have been resolved.
            </p>
          </div>

        </div>
      </div>

      <!-- FINDINGS -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">

          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Audit Findings
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              Recent compliance and operational observations
            </p>
          </div>

        </div>

        <div class="mt-5 space-y-4">

          <div
            v-for="finding in filteredFindings.slice(0, 5)"
            :key="finding.id"
            class="p-4 rounded-xl border border-slate-200 bg-slate-50"
          >

            <div class="flex justify-between items-start gap-4">

              <div class="min-w-0">

                <div class="flex flex-wrap gap-2 mb-2">

                  <span
                    class="px-2.5 py-1 rounded-full text-xs font-bold"
                    :class="categoryClass(finding.category)"
                  >
                    {{ finding.category }}
                  </span>

                  <span
                    class="px-2.5 py-1 rounded-full text-xs font-bold"
                    :class="priorityClass(finding.priority)"
                  >
                    {{ finding.priority }}
                  </span>

                </div>

                <p class="text-sm font-bold text-slate-900">
                  {{ finding.title }}
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  {{ finding.description }}
                </p>

              </div>

              <span
                class="shrink-0 px-2.5 py-1 rounded-full text-xs font-bold"
                :class="statusClass(finding.status)"
              >
                {{ finding.status }}
              </span>

            </div>

            <div class="flex flex-wrap justify-end gap-2 mt-4">

              <button
                @click="openDetails(finding)"
                class="px-3 py-2 rounded-lg bg-white border border-slate-200 text-xs font-bold text-slate-700 hover:bg-slate-100"
              >
                View
              </button>

              <button
                @click="openEditModal(finding)"
                class="px-3 py-2 rounded-lg bg-blue-50 text-blue-700 text-xs font-bold hover:bg-blue-100"
              >
                Edit
              </button>

              <button
                v-if="finding.status === 'Open'"
                @click="openEscalateModal(finding)"
                class="px-3 py-2 rounded-lg bg-red-50 text-red-700 text-xs font-bold hover:bg-red-100"
              >
                Escalate
              </button>

              <button
                v-if="finding.status !== 'Resolved'"
                @click="resolveFinding(finding)"
                class="px-3 py-2 rounded-lg bg-green-50 text-green-700 text-xs font-bold hover:bg-green-100"
              >
                Resolve
              </button>

              <button
                @click="openDeleteModal(finding)"
                class="px-3 py-2 rounded-lg bg-red-50 text-red-700 text-xs font-bold hover:bg-red-100"
              >
                Delete
              </button>

            </div>

          </div>

          <div
            v-if="filteredFindings.length === 0"
            class="py-10 text-center"
          >
            <p class="text-3xl">
              🔎
            </p>

            <p class="font-bold text-slate-700 mt-2">
              No findings found
            </p>
          </div>

        </div>
      </div>

    </section>

    <!-- METRICS -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="border-b border-slate-200 pb-5">

          <h2 class="text-xl font-bold text-slate-900">
            Performance Metrics
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Current audit score trends
          </p>

        </div>

        <div class="mt-5 space-y-5">

          <div>

            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Reporting Compliance</span>
              <span>96%</span>
            </div>

            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[96%] rounded-full bg-emerald-500"></div>
            </div>

          </div>

          <div>

            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>On-Time Submission</span>
              <span>88%</span>
            </div>

            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[88%] rounded-full bg-blue-500"></div>
            </div>

          </div>

          <div>

            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Attachment Completeness</span>
              <span>81%</span>
            </div>

            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[81%] rounded-full bg-yellow-500"></div>
            </div>

          </div>

        </div>
      </div>

      <!-- ACTION NOTES -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="border-b border-slate-200 pb-5">

          <h2 class="text-xl font-bold text-slate-900">
            Action Notes
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Follow-up reminders for administrators
          </p>

        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-emerald-200 bg-emerald-50">
            <p class="text-sm font-bold text-slate-900">
              Reminder
            </p>

            <p class="text-sm text-slate-600 mt-1">
              Ensure all stations attach supporting evidence before submitting monthly compliance reports.
            </p>
          </div>

          <div class="p-4 rounded-xl border border-orange-200 bg-orange-50">
            <p class="text-sm font-bold text-slate-900">
              Attention
            </p>

            <p class="text-sm text-slate-600 mt-1">
              Two delayed incident reports need closure notes and supervisor approval before end of day.
            </p>
          </div>

          <div class="p-4 rounded-xl border border-indigo-200 bg-indigo-50">
            <p class="text-sm font-bold text-slate-900">
              Follow-Up
            </p>

            <p class="text-sm text-slate-600 mt-1">
              Schedule a review meeting with Station Chiefs to address recurring documentation inconsistencies.
            </p>
          </div>

        </div>
      </div>

    </section>

    <!-- ADD / EDIT MODAL -->
    <div
      v-if="showAddModal || showEditModal"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div class="bg-white rounded-2xl shadow-2xl w-full max-w-2xl max-h-[90vh] overflow-y-auto">

        <div class="p-6 border-b border-slate-200 flex justify-between">

          <div>
            <h2 class="text-xl font-bold text-slate-900">
              {{ showAddModal ? 'Add Audit Finding' : 'Edit Audit Finding' }}
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              Record compliance or operational observations.
            </p>
          </div>

          <button
            @click="showAddModal = false; showEditModal = false"
            class="text-2xl text-slate-400 hover:text-slate-700"
          >
            ×
          </button>

        </div>

        <div class="p-6 space-y-5">

          <div>
            <label class="block text-sm font-bold text-slate-700 mb-2">
              Finding Title *
            </label>

            <input
              v-model="form.title"
              type="text"
              placeholder="e.g. Documentation Gap"
              class="w-full px-4 py-3 border border-slate-200 rounded-xl outline-none focus:border-[#8B1E23]"
            />
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-5">

            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">
                Category
              </label>

              <select
                v-model="form.category"
                class="w-full px-4 py-3 border border-slate-200 rounded-xl bg-white"
              >
                <option>Documentation</option>
                <option>Equipment</option>
                <option>Training</option>
                <option>Reporting</option>
                <option>Compliance</option>
                <option>Activity</option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">
                Priority
              </label>

              <select
                v-model="form.priority"
                class="w-full px-4 py-3 border border-slate-200 rounded-xl bg-white"
              >
                <option>High</option>
                <option>Medium</option>
                <option>Low</option>
              </select>
            </div>

          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-5">

            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">
                Personnel / Office *
              </label>

              <input
                v-model="form.personnel"
                type="text"
                placeholder="Responsible personnel"
                class="w-full px-4 py-3 border border-slate-200 rounded-xl outline-none focus:border-[#8B1E23]"
              />
            </div>

            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">
                Due Date
              </label>

              <input
                v-model="form.dueDate"
                type="date"
                class="w-full px-4 py-3 border border-slate-200 rounded-xl outline-none focus:border-[#8B1E23]"
              />
            </div>

          </div>

          <div>
            <label class="block text-sm font-bold text-slate-700 mb-2">
              Description *
            </label>

            <textarea
              v-model="form.description"
              rows="4"
              placeholder="Describe the audit finding..."
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
              placeholder="Additional action or review notes..."
              class="w-full px-4 py-3 border border-slate-200 rounded-xl outline-none focus:border-[#8B1E23] resize-none"
            ></textarea>
          </div>

        </div>

        <div class="p-6 border-t border-slate-200 flex justify-end gap-3">

          <button
            @click="showAddModal = false; showEditModal = false"
            class="px-5 py-3 rounded-xl border border-slate-200 font-bold text-slate-700"
          >
            Cancel
          </button>

          <button
            v-if="showAddModal"
            @click="addFinding"
            class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D]"
          >
            Add Finding
          </button>

          <button
            v-else
            @click="updateFinding"
            class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D]"
          >
            Save Changes
          </button>

        </div>

      </div>
    </div>

    <!-- DETAILS MODAL -->
    <div
      v-if="showDetailsModal && selectedFinding"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div class="bg-white rounded-2xl shadow-2xl w-full max-w-xl">

        <div class="p-6 border-b border-slate-200 flex justify-between">

          <div>
            <p class="text-xs font-bold text-[#8B1E23]">
              {{ selectedFinding.id }}
            </p>

            <h2 class="text-xl font-bold text-slate-900 mt-1">
              {{ selectedFinding.title }}
            </h2>
          </div>

          <button
            @click="showDetailsModal = false"
            class="text-2xl text-slate-400"
          >
            ×
          </button>

        </div>

        <div class="p-6 space-y-5">

          <div class="flex flex-wrap gap-2">

            <span
              class="px-3 py-1 rounded-full text-xs font-bold"
              :class="categoryClass(selectedFinding.category)"
            >
              {{ selectedFinding.category }}
            </span>

            <span
              class="px-3 py-1 rounded-full text-xs font-bold"
              :class="priorityClass(selectedFinding.priority)"
            >
              {{ selectedFinding.priority }}
            </span>

            <span
              class="px-3 py-1 rounded-full text-xs font-bold"
              :class="statusClass(selectedFinding.status)"
            >
              {{ selectedFinding.status }}
            </span>

          </div>

          <div>
            <p class="text-xs uppercase font-bold text-slate-400">
              Description
            </p>

            <p class="text-sm text-slate-600 mt-1">
              {{ selectedFinding.description }}
            </p>
          </div>

          <div class="grid grid-cols-2 gap-5">

            <div>
              <p class="text-xs uppercase font-bold text-slate-400">
                Responsible
              </p>

              <p class="font-semibold text-slate-800 mt-1">
                {{ selectedFinding.personnel }}
              </p>
            </div>

            <div>
              <p class="text-xs uppercase font-bold text-slate-400">
                Due Date
              </p>

              <p class="font-semibold text-slate-800 mt-1">
                {{ formatDate(selectedFinding.dueDate) }}
              </p>
            </div>

          </div>

          <div>
            <p class="text-xs uppercase font-bold text-slate-400">
              Notes
            </p>

            <p class="text-sm text-slate-600 mt-1">
              {{ selectedFinding.notes || 'No notes provided.' }}
            </p>
          </div>

        </div>

        <div class="p-6 border-t border-slate-200 flex justify-end">

          <button
            @click="showDetailsModal = false"
            class="px-5 py-3 rounded-xl bg-slate-100 font-bold text-slate-700"
          >
            Close
          </button>

        </div>

      </div>
    </div>

    <!-- ESCALATE MODAL -->
    <div
      v-if="showEscalateModal && selectedFinding"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div class="bg-white rounded-2xl shadow-2xl w-full max-w-md p-6">

        <div class="w-12 h-12 rounded-full bg-red-100 text-red-600 flex items-center justify-center text-xl font-bold">
          !
        </div>

        <h2 class="text-xl font-bold text-slate-900 mt-4">
          Escalate Finding?
        </h2>

        <p class="text-sm text-slate-500 mt-2">
          This will move
          <strong>{{ selectedFinding.title }}</strong>
          to the escalation queue for higher-level attention.
        </p>

        <div class="flex justify-end gap-3 mt-6">

          <button
            @click="showEscalateModal = false"
            class="px-5 py-3 rounded-xl border border-slate-200 font-bold"
          >
            Cancel
          </button>

          <button
            @click="confirmEscalation"
            class="px-5 py-3 rounded-xl bg-red-600 text-white font-bold hover:bg-red-700"
          >
            Escalate
          </button>

        </div>

      </div>
    </div>

    <!-- DELETE MODAL -->
    <div
      v-if="showDeleteModal && selectedFinding"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div class="bg-white rounded-2xl shadow-2xl w-full max-w-md p-6">

        <div class="w-12 h-12 rounded-full bg-red-100 text-red-600 flex items-center justify-center text-xl font-bold">
          !
        </div>

        <h2 class="text-xl font-bold text-slate-900 mt-4">
          Delete Finding?
        </h2>

        <p class="text-sm text-slate-500 mt-2">
          Are you sure you want to delete
          <strong>{{ selectedFinding.title }}</strong>?
          This will also remove its escalation record.
        </p>

        <div class="flex justify-end gap-3 mt-6">

          <button
            @click="showDeleteModal = false"
            class="px-5 py-3 rounded-xl border border-slate-200 font-bold"
          >
            Cancel
          </button>

          <button
            @click="deleteFinding"
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