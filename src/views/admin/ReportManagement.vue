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

const STORAGE_KEY = 'fireNotifyAdminReports'

const searchQuery = ref('')
const selectedType = ref('All Report Types')
const selectedStatus = ref('All Status')

const showReportModal = ref(false)
const showDetailsModal = ref(false)
const showDeleteModal = ref(false)
const showReviewModal = ref(false)

const editingReport = ref(null)
const selectedReport = ref(null)
const reportToDelete = ref(null)

const toastMessage = ref('')
const toastType = ref('success')

const reviewAction = ref('')
const reviewComment = ref('')

/* =========================================================
   REPORT FORM
========================================================= */

const emptyReport = () => ({
  id: '',
  title: '',
  type: 'Incident Report',
  submittedBy: '',
  rank: '',
  station: 'BFP Balingasag',
  submittedDate: '',
  deadline: '',
  status: 'For Review',
  description: '',
  attachment: ''
})

const reportForm = ref(emptyReport())

/* =========================================================
   SAMPLE REPORT DATA
========================================================= */

const defaultReports = [
  {
    id: 'REP-001',
    title: 'Fire Safety Inspection Report',
    type: 'Inspection Report',
    submittedBy: 'Juan Dela Cruz',
    rank: 'FO3',
    station: 'BFP Balingasag',
    submittedDate: 'September 9, 2026',
    deadline: 'September 10, 2026 • 5:00 PM',
    status: 'For Review',
    description:
      'Fire safety inspection conducted at Balingasag Public Market Complex.',
    attachment: 'InspectionChecklist_Sept9.pdf'
  },
  {
    id: 'REP-002',
    title: 'Weekly Accomplishment Report',
    type: 'Accomplishment Report',
    submittedBy: 'Maria Santos',
    rank: 'SFO1',
    station: 'BFP Balingasag',
    submittedDate: 'September 8, 2026',
    deadline: 'September 8, 2026 • 5:00 PM',
    status: 'Approved',
    description:
      'Weekly accomplishment report covering station activities and completed assignments.',
    attachment: 'WeeklyAccomplishment_Sept8.pdf'
  },
  {
    id: 'REP-003',
    title: 'Fire Incident Report',
    type: 'Incident Report',
    submittedBy: 'Roberto Reyes',
    rank: 'FO2',
    station: 'BFP Balingasag',
    submittedDate: 'Pending',
    deadline: 'September 9, 2026 • 8:00 PM',
    status: 'Overdue',
    description:
      'Incident report requiring immediate submission and supervisor follow-up.',
    attachment: ''
  },
  {
    id: 'REP-004',
    title: 'Community Fire Drill Report',
    type: 'Activity Report',
    submittedBy: 'Carlo Garcia',
    rank: 'FO1',
    station: 'BFP Balingasag',
    submittedDate: 'September 7, 2026',
    deadline: 'September 7, 2026 • 5:00 PM',
    status: 'Approved',
    description:
      'Report for the community fire drill conducted at the municipal elementary school.',
    attachment: 'BarangayDrillSummary.xlsx'
  },
  {
    id: 'REP-005',
    title: 'Equipment Inspection Report',
    type: 'Inspection Report',
    submittedBy: 'Ana Villanueva',
    rank: 'FO2',
    station: 'BFP Balingasag',
    submittedDate: 'September 6, 2026',
    deadline: 'September 7, 2026 • 5:00 PM',
    status: 'Returned',
    description:
      'Equipment inspection report returned because several inspection photos were missing.',
    attachment: 'EquipmentInspection.pdf'
  },
  {
    id: 'REP-006',
    title: 'Station Activity Report',
    type: 'Activity Report',
    submittedBy: 'Mark Santos',
    rank: 'FO2',
    station: 'BFP Balingasag',
    submittedDate: 'September 5, 2026',
    deadline: 'September 6, 2026 • 5:00 PM',
    status: 'Rejected',
    description:
      'Station activity report that did not meet the required documentation standards.',
    attachment: 'StationActivity.pdf'
  }
]

const savedReports = localStorage.getItem(STORAGE_KEY)

const reports = ref(
  savedReports
    ? JSON.parse(savedReports)
    : defaultReports
)

/* =========================================================
   FILE DATA
========================================================= */

const uploadedFiles = ref([
  {
    name: 'InspectionChecklist_Sept9.pdf',
    uploadedBy: 'FO3 Juan Dela Cruz',
    type: 'PDF'
  },
  {
    name: 'BarangayDrillSummary.xlsx',
    uploadedBy: 'FO2 Roberto Reyes',
    type: 'XLSX'
  },
  {
    name: 'IncidentPhotos_Set2.jpg',
    uploadedBy: 'SFO1 Maria Santos',
    type: 'IMG'
  },
  {
    name: 'EquipmentInspection.pdf',
    uploadedBy: 'FO2 Ana Villanueva',
    type: 'PDF'
  }
])

/* =========================================================
   COMPUTED STATISTICS
========================================================= */

const totalReports = computed(() => reports.value.length)

const forReviewCount = computed(() =>
  reports.value.filter(report => report.status === 'For Review').length
)

const approvedCount = computed(() =>
  reports.value.filter(report => report.status === 'Approved').length
)

const rejectedCount = computed(() =>
  reports.value.filter(report => report.status === 'Rejected').length
)

const returnedCount = computed(() =>
  reports.value.filter(report => report.status === 'Returned').length
)

const overdueCount = computed(() =>
  reports.value.filter(report => report.status === 'Overdue').length
)

/* =========================================================
   FILTERED REPORTS
========================================================= */

const filteredReports = computed(() => {
  const query = searchQuery.value.toLowerCase().trim()

  return reports.value.filter(report => {
    const searchableText = [
      report.id,
      report.title,
      report.type,
      report.submittedBy,
      report.rank,
      report.station,
      report.status
    ]
      .filter(Boolean)
      .join(' ')
      .toLowerCase()

    const matchesSearch =
      !query || searchableText.includes(query)

    const matchesType =
      selectedType.value === 'All Report Types' ||
      report.type === selectedType.value

    const matchesStatus =
      selectedStatus.value === 'All Status' ||
      report.status === selectedStatus.value

    return matchesSearch && matchesType && matchesStatus
  })
})

const hasFilters = computed(() =>
  searchQuery.value ||
  selectedType.value !== 'All Report Types' ||
  selectedStatus.value !== 'All Status'
)

/* =========================================================
   ANALYTICS
========================================================= */

const approvalRate = computed(() => {
  if (!totalReports.value) return 0

  return Math.round(
    (approvedCount.value / totalReports.value) * 100
  )
})

const reviewRate = computed(() => {
  if (!totalReports.value) return 0

  return Math.round(
    (forReviewCount.value / totalReports.value) * 100
  )
})

const correctionRate = computed(() => {
  if (!totalReports.value) return 0

  return Math.round(
    ((returnedCount.value + rejectedCount.value) /
      totalReports.value) *
      100
  )
})

const onTimeSubmission = computed(() => {
  if (!totalReports.value) return 0

  const late = reports.value.filter(
    report =>
      report.status === 'Overdue' ||
      report.status === 'Returned'
  ).length

  return Math.max(
    0,
    Math.round(((totalReports.value - late) / totalReports.value) * 100)
  )
})

/* =========================================================
   SAVE
========================================================= */

const saveReports = () => {
  localStorage.setItem(
    STORAGE_KEY,
    JSON.stringify(reports.value)
  )
}

/* =========================================================
   TOAST
========================================================= */

const showToast = (message, type = 'success') => {
  toastMessage.value = message
  toastType.value = type

  setTimeout(() => {
    toastMessage.value = ''
  }, 3000)
}

/* =========================================================
   FILTER ACTIONS
========================================================= */

const clearFilters = () => {
  searchQuery.value = ''
  selectedType.value = 'All Report Types'
  selectedStatus.value = 'All Status'
}

/* =========================================================
   CREATE REPORT
========================================================= */

const openCreateReport = () => {
  editingReport.value = null
  reportForm.value = emptyReport()

  reportForm.value.submittedBy =
    props.currentUser?.name ||
    'Admin User'

  reportForm.value.rank =
    props.currentUser?.rank ||
    'Admin'

  showReportModal.value = true
}

/* =========================================================
   EDIT REPORT
========================================================= */

const openEditReport = report => {
  editingReport.value = report

  reportForm.value = {
    ...report
  }

  showReportModal.value = true
}

/* =========================================================
   SAVE REPORT
========================================================= */

const saveReport = () => {
  if (
    !reportForm.value.title ||
    !reportForm.value.type ||
    !reportForm.value.submittedBy
  ) {
    showToast(
      'Please complete the required fields.',
      'error'
    )
    return
  }

  if (editingReport.value) {
    const index = reports.value.findIndex(
      report => report.id === editingReport.value.id
    )

    if (index !== -1) {
      reports.value[index] = {
        ...reportForm.value
      }
    }

    showToast('Report updated successfully.')
  } else {
    const newId =
      'REP-' +
      String(reports.value.length + 1).padStart(3, '0')

    reports.value.unshift({
      ...reportForm.value,
      id: newId,
      submittedDate:
        reportForm.value.submittedDate ||
        new Date().toLocaleDateString('en-US', {
          month: 'long',
          day: 'numeric',
          year: 'numeric'
        })
    })

    showToast('Report created successfully.')
  }

  saveReports()
  showReportModal.value = false
}

/* =========================================================
   VIEW REPORT
========================================================= */

const viewReport = report => {
  selectedReport.value = report
  showDetailsModal.value = true
}

/* =========================================================
   REVIEW REPORT
========================================================= */

const openReview = (report, action) => {
  selectedReport.value = report
  reviewAction.value = action
  reviewComment.value = ''

  showReviewModal.value = true
}

const submitReview = () => {
  if (!selectedReport.value) return

  const report = reports.value.find(
    item => item.id === selectedReport.value.id
  )

  if (!report) return

  if (
    reviewAction.value !== 'approve' &&
    !reviewComment.value.trim()
  ) {
    showToast(
      'Please provide a review comment.',
      'error'
    )
    return
  }

  if (reviewAction.value === 'approve') {
    report.status = 'Approved'
    showToast('Report approved successfully.')
  }

  if (reviewAction.value === 'reject') {
    report.status = 'Rejected'
    showToast('Report rejected.')
  }

  if (reviewAction.value === 'return') {
    report.status = 'Returned'
    showToast('Report returned for correction.')
  }

  saveReports()

  showReviewModal.value = false
}

/* =========================================================
   SEND REMINDER
========================================================= */

const sendReminder = report => {
  showToast(
    `Reminder sent to ${report.submittedBy}.`
  )
}

/* =========================================================
   DELETE REPORT
========================================================= */

const openDeleteReport = report => {
  reportToDelete.value = report
  showDeleteModal.value = true
}

const deleteReport = () => {
  if (!reportToDelete.value) return

  reports.value = reports.value.filter(
    report => report.id !== reportToDelete.value.id
  )

  saveReports()

  showDeleteModal.value = false

  showToast('Report deleted successfully.')

  reportToDelete.value = null
}

/* =========================================================
   STATUS STYLING
========================================================= */

const getStatusClass = status => {
  const classes = {
    'For Review':
      'bg-yellow-50 text-yellow-700 border-yellow-200',

    Approved:
      'bg-green-50 text-green-700 border-green-200',

    Rejected:
      'bg-red-50 text-red-700 border-red-200',

    Returned:
      'bg-blue-50 text-blue-700 border-blue-200',

    Overdue:
      'bg-red-100 text-[#8B1E23] border-red-200'
  }

  return classes[status] ||
    'bg-slate-100 text-slate-600 border-slate-200'
}

const getTypeClass = type => {
  const classes = {
    'Incident Report':
      'bg-red-50 text-red-700',

    'Inspection Report':
      'bg-blue-50 text-blue-700',

    'Accomplishment Report':
      'bg-green-50 text-green-700',

    'Activity Report':
      'bg-purple-50 text-purple-700'
  }

  return classes[type] ||
    'bg-slate-100 text-slate-600'
}

/* =========================================================
   INITIALS
========================================================= */

const getInitials = name => {
  if (!name) return 'U'

  return name
    .split(' ')
    .map(word => word[0])
    .join('')
    .slice(0, 2)
    .toUpperCase()
}

/* =========================================================
   FILE ACTION
========================================================= */

const viewFile = file => {
  showToast(`Opening ${file.name}...`)
}
</script>

<template>
  <div class="space-y-6">

    <!-- =====================================================
         HEADER
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >
      <div
        class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5"
      >
        <div>
          <p
            class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]"
          >
            Records Management
          </p>

          <h2
            class="text-2xl font-bold text-slate-900 mt-1"
          >
            Report Management
          </h2>

          <p class="text-base text-slate-500 mt-1">
            Review, monitor, approve, and manage submitted
            operational reports.
          </p>
        </div>

        <button
          @click="openCreateReport"
          class="px-6 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition shadow-sm"
        >
          + Create Report
        </button>
      </div>
    </section>

    <!-- =====================================================
         STATISTICS
    ====================================================== -->

    <section
      class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-5"
    >

      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-3xl font-bold text-slate-900">
          {{ totalReports }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Total Reports
        </p>
      </div>

      <div
        class="bg-white border border-yellow-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-3xl font-bold text-yellow-600">
          {{ forReviewCount }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          For Review
        </p>
      </div>

      <div
        class="bg-white border border-green-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-3xl font-bold text-green-600">
          {{ approvedCount }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Approved
        </p>
      </div>

      <div
        class="bg-white border border-red-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-3xl font-bold text-[#8B1E23]">
          {{ rejectedCount }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Rejected
        </p>
      </div>

      <div
        class="bg-white border border-red-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-3xl font-bold text-red-600">
          {{ overdueCount }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Overdue
        </p>
      </div>

    </section>

    <!-- =====================================================
         SEARCH / FILTERS
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5"
    >
      <div
        class="flex flex-col lg:flex-row gap-4"
      >

        <div class="flex-1 relative">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search report, ID, personnel..."
            class="w-full h-12 px-4 rounded-xl border border-slate-300 text-base focus:ring-2 focus:ring-[#8B1E23] focus:border-[#8B1E23] outline-none"
          />
        </div>

        <select
          v-model="selectedType"
          class="h-12 px-4 rounded-xl border border-slate-300 text-base lg:w-60 focus:ring-2 focus:ring-[#8B1E23] outline-none"
        >
          <option>All Report Types</option>
          <option>Incident Report</option>
          <option>Inspection Report</option>
          <option>Accomplishment Report</option>
          <option>Activity Report</option>
        </select>

        <select
          v-model="selectedStatus"
          class="h-12 px-4 rounded-xl border border-slate-300 text-base lg:w-52 focus:ring-2 focus:ring-[#8B1E23] outline-none"
        >
          <option>All Status</option>
          <option>For Review</option>
          <option>Approved</option>
          <option>Rejected</option>
          <option>Returned</option>
          <option>Overdue</option>
        </select>

        <button
          v-if="hasFilters"
          @click="clearFilters"
          class="h-12 px-5 rounded-xl border border-slate-300 text-slate-700 font-bold hover:bg-slate-100"
        >
          Clear
        </button>

      </div>
    </section>

    <!-- =====================================================
         REPORT LIST
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div
        class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 border-b border-slate-200 pb-5"
      >
        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Operational Reports
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            {{ filteredReports.length }} report(s) displayed
          </p>
        </div>

        <div
          class="text-sm font-semibold text-slate-500"
        >
          {{ forReviewCount }} awaiting review
        </div>
      </div>

      <div
        v-if="filteredReports.length"
        class="mt-5 space-y-4"
      >

        <div
          v-for="report in filteredReports"
          :key="report.id"
          class="p-5 rounded-xl border border-slate-200 hover:border-slate-300 hover:shadow-sm transition"
          :class="{
            'bg-red-50 border-red-200':
              report.status === 'Overdue'
          }"
        >

          <div
            class="flex flex-col xl:flex-row xl:items-center xl:justify-between gap-5"
          >

            <!-- REPORT INFO -->

            <div class="flex-1 min-w-0">

              <div
                class="flex items-center gap-3 flex-wrap"
              >

                <h3
                  class="text-lg font-bold text-slate-900"
                >
                  {{ report.title }}
                </h3>

                <span
                  class="px-3 py-1 rounded-full text-xs font-bold border"
                  :class="getStatusClass(report.status)"
                >
                  {{ report.status.toUpperCase() }}
                </span>

                <span
                  class="px-3 py-1 rounded-full text-xs font-bold"
                  :class="getTypeClass(report.type)"
                >
                  {{ report.type }}
                </span>

              </div>

              <div
                class="flex flex-wrap items-center gap-x-5 gap-y-2 mt-3 text-sm"
              >

                <span class="text-slate-600">
                  <strong>{{ report.rank }}</strong>
                  {{ report.submittedBy }}
                </span>

                <span class="text-slate-400">
                  {{ report.station }}
                </span>

                <span class="text-slate-400">
                  ID: {{ report.id }}
                </span>

              </div>

              <p
                v-if="report.status === 'Overdue'"
                class="text-sm text-[#8B1E23] font-semibold mt-2"
              >
                Deadline: {{ report.deadline }}
              </p>

              <p
                v-else
                class="text-sm text-slate-400 mt-2"
              >
                Submitted: {{ report.submittedDate }}
              </p>

            </div>

            <!-- ACTIONS -->

            <div
              class="flex flex-wrap gap-2"
            >

              <button
                @click="viewReport(report)"
                class="px-4 py-2.5 rounded-lg border border-slate-300 text-sm font-bold hover:bg-slate-100"
              >
                View
              </button>

              <button
                v-if="report.status === 'For Review'"
                @click="openReview(report, 'approve')"
                class="px-4 py-2.5 rounded-lg bg-green-600 text-white text-sm font-bold hover:bg-green-700"
              >
                Approve
              </button>

              <button
                v-if="
                  report.status === 'For Review' ||
                  report.status === 'Returned'
                "
                @click="openReview(report, 'return')"
                class="px-4 py-2.5 rounded-lg bg-blue-600 text-white text-sm font-bold hover:bg-blue-700"
              >
                Return
              </button>

              <button
                v-if="report.status === 'For Review'"
                @click="openReview(report, 'reject')"
                class="px-4 py-2.5 rounded-lg border border-red-300 text-red-700 text-sm font-bold hover:bg-red-50"
              >
                Reject
              </button>

              <button
                v-if="report.status === 'Overdue'"
                @click="sendReminder(report)"
                class="px-4 py-2.5 rounded-lg bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]"
              >
                Reminder
              </button>

              <button
                @click="openEditReport(report)"
                class="px-3 py-2.5 rounded-lg border border-slate-300 text-sm font-bold hover:bg-slate-100"
                title="Edit"
              >
                Edit
              </button>

              <button
                @click="openDeleteReport(report)"
                class="px-3 py-2.5 rounded-lg border border-red-200 text-red-600 text-sm font-bold hover:bg-red-50"
                title="Delete"
              >
                Delete
              </button>

            </div>

          </div>

        </div>

      </div>

      <!-- EMPTY STATE -->

      <div
        v-else
        class="py-16 text-center"
      >
        <div
          class="w-16 h-16 mx-auto rounded-full bg-slate-100 flex items-center justify-center text-2xl"
        >
          📄
        </div>

        <h3
          class="text-lg font-bold text-slate-900 mt-4"
        >
          No reports found
        </h3>

        <p
          class="text-sm text-slate-500 mt-1"
        >
          Try changing your search or filters.
        </p>

        <button
          @click="clearFilters"
          class="mt-4 px-5 py-2.5 rounded-lg bg-[#8B1E23] text-white font-bold"
        >
          Clear Filters
        </button>
      </div>

    </section>

    <!-- =====================================================
         ANALYTICS + FILES
    ====================================================== -->

    <section
      class="grid grid-cols-1 xl:grid-cols-2 gap-6"
    >

      <!-- ANALYTICS -->

      <div
        class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
      >

        <div
          class="border-b border-slate-200 pb-5"
        >
          <h2 class="text-xl font-bold text-slate-900">
            Report Analytics
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Current report processing performance
          </p>
        </div>

        <div class="mt-5 space-y-5">

          <div>
            <div
              class="flex justify-between text-sm font-semibold text-slate-700 mb-2"
            >
              <span>On-Time Submission</span>
              <span>{{ onTimeSubmission }}%</span>
            </div>

            <div
              class="h-2.5 rounded-full bg-slate-100 overflow-hidden"
            >
              <div
                class="h-full rounded-full bg-green-500 transition-all"
                :style="{ width: `${onTimeSubmission}%` }"
              ></div>
            </div>
          </div>

          <div>
            <div
              class="flex justify-between text-sm font-semibold text-slate-700 mb-2"
            >
              <span>Approval Rate</span>
              <span>{{ approvalRate }}%</span>
            </div>

            <div
              class="h-2.5 rounded-full bg-slate-100 overflow-hidden"
            >
              <div
                class="h-full rounded-full bg-blue-500 transition-all"
                :style="{ width: `${approvalRate}%` }"
              ></div>
            </div>
          </div>

          <div>
            <div
              class="flex justify-between text-sm font-semibold text-slate-700 mb-2"
            >
              <span>Correction / Rejection</span>
              <span>{{ correctionRate }}%</span>
            </div>

            <div
              class="h-2.5 rounded-full bg-slate-100 overflow-hidden"
            >
              <div
                class="h-full rounded-full bg-yellow-500 transition-all"
                :style="{ width: `${correctionRate}%` }"
              ></div>
            </div>
          </div>

          <div
            class="grid grid-cols-3 gap-3 pt-3"
          >

            <div
              class="p-3 rounded-xl bg-yellow-50 border border-yellow-100"
            >
              <p class="text-lg font-bold text-yellow-700">
                {{ forReviewCount }}
              </p>
              <p class="text-xs text-slate-500">
                Review
              </p>
            </div>

            <div
              class="p-3 rounded-xl bg-blue-50 border border-blue-100"
            >
              <p class="text-lg font-bold text-blue-700">
                {{ returnedCount }}
              </p>
              <p class="text-xs text-slate-500">
                Returned
              </p>
            </div>

            <div
              class="p-3 rounded-xl bg-red-50 border border-red-100"
            >
              <p class="text-lg font-bold text-red-700">
                {{ overdueCount }}
              </p>
              <p class="text-xs text-slate-500">
                Overdue
              </p>
            </div>

          </div>

        </div>

      </div>

      <!-- FILES -->

      <div
        class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
      >

        <div
          class="border-b border-slate-200 pb-5"
        >
          <h2 class="text-xl font-bold text-slate-900">
            Recently Uploaded Files
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Latest report attachments
          </p>
        </div>

        <div class="mt-5 space-y-3">

          <div
            v-for="file in uploadedFiles"
            :key="file.name"
            class="flex items-center justify-between gap-3 p-3 rounded-xl border border-slate-200 bg-slate-50 hover:bg-slate-100 transition"
          >

            <div class="flex items-center gap-3 min-w-0">

              <div
                class="w-10 h-10 rounded-lg bg-white border border-slate-200 flex items-center justify-center text-xs font-bold text-[#8B1E23]"
              >
                {{ file.type }}
              </div>

              <div class="min-w-0">

                <p
                  class="text-sm font-bold text-slate-900 truncate"
                >
                  {{ file.name }}
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  {{ file.uploadedBy }}
                </p>

              </div>

            </div>

            <button
              @click="viewFile(file)"
              class="text-sm font-bold text-[#8B1E23] hover:underline"
            >
              View
            </button>

          </div>

        </div>

      </div>

    </section>

    <!-- =====================================================
         REVIEW NOTES
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div
        class="border-b border-slate-200 pb-5"
      >
        <h2 class="text-xl font-bold text-slate-900">
          Review Notes
        </h2>

        <p class="text-sm text-slate-500 mt-1">
          Important reminders for report coordinators and approvers.
        </p>
      </div>

      <div class="mt-5 grid grid-cols-1 md:grid-cols-3 gap-4">

        <div
          class="p-4 rounded-xl border border-red-200 bg-red-50"
        >
          <p class="text-sm font-bold text-slate-900">
            Priority Reminder
          </p>

          <p class="text-sm text-slate-600 mt-1">
            Fire incident reports submitted after the deadline
            require immediate supervisor review and follow-up.
          </p>
        </div>

        <div
          class="p-4 rounded-xl border border-amber-200 bg-amber-50"
        >
          <p class="text-sm font-bold text-slate-900">
            Correction Needed
          </p>

          <p class="text-sm text-slate-600 mt-1">
            Check inspection reports for complete photographs
            and supporting documentation before approval.
          </p>
        </div>

        <div
          class="p-4 rounded-xl border border-blue-200 bg-blue-50"
        >
          <p class="text-sm font-bold text-slate-900">
            Documentation
          </p>

          <p class="text-sm text-slate-600 mt-1">
            Ensure all attachments are properly named and linked
            to the corresponding report ID.
          </p>
        </div>

      </div>

    </section>

    <!-- =====================================================
         CREATE / EDIT MODAL
    ====================================================== -->

    <div
      v-if="showReportModal"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div
        class="bg-white w-full max-w-2xl rounded-2xl shadow-xl max-h-[90vh] overflow-y-auto"
      >

        <div
          class="p-6 border-b border-slate-200 flex items-center justify-between"
        >
          <div>
            <h3
              class="text-xl font-bold text-slate-900"
            >
              {{ editingReport ? 'Edit Report' : 'Create Report' }}
            </h3>

            <p class="text-sm text-slate-500 mt-1">
              Manage operational report information.
            </p>
          </div>

          <button
            @click="showReportModal = false"
            class="text-slate-400 hover:text-slate-700 text-xl"
          >
            ✕
          </button>
        </div>

        <div class="p-6 space-y-5">

          <div>
            <label class="block text-sm font-bold text-slate-700 mb-2">
              Report Title *
            </label>

            <input
              v-model="reportForm.title"
              type="text"
              placeholder="Enter report title"
              class="w-full h-11 px-4 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#8B1E23] outline-none"
            />
          </div>

          <div
            class="grid grid-cols-1 md:grid-cols-2 gap-4"
          >

            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">
                Report Type *
              </label>

              <select
                v-model="reportForm.type"
                class="w-full h-11 px-4 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#8B1E23] outline-none"
              >
                <option>Incident Report</option>
                <option>Inspection Report</option>
                <option>Accomplishment Report</option>
                <option>Activity Report</option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">
                Status
              </label>

              <select
                v-model="reportForm.status"
                class="w-full h-11 px-4 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#8B1E23] outline-none"
              >
                <option>For Review</option>
                <option>Approved</option>
                <option>Rejected</option>
                <option>Returned</option>
                <option>Overdue</option>
              </select>
            </div>

          </div>

          <div
            class="grid grid-cols-1 md:grid-cols-2 gap-4"
          >

            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">
                Submitted By *
              </label>

              <input
                v-model="reportForm.submittedBy"
                type="text"
                class="w-full h-11 px-4 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#8B1E23] outline-none"
              />
            </div>

            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">
                Rank
              </label>

              <input
                v-model="reportForm.rank"
                type="text"
                placeholder="FO3"
                class="w-full h-11 px-4 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#8B1E23] outline-none"
              />
            </div>

          </div>

          <div
            class="grid grid-cols-1 md:grid-cols-2 gap-4"
          >

            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">
                Submission Date
              </label>

              <input
                v-model="reportForm.submittedDate"
                type="text"
                placeholder="September 14, 2026"
                class="w-full h-11 px-4 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#8B1E23] outline-none"
              />
            </div>

            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">
                Deadline
              </label>

              <input
                v-model="reportForm.deadline"
                type="text"
                placeholder="September 15, 2026 • 5:00 PM"
                class="w-full h-11 px-4 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#8B1E23] outline-none"
              />
            </div>

          </div>

          <div>
            <label class="block text-sm font-bold text-slate-700 mb-2">
              Attachment
            </label>

            <input
              v-model="reportForm.attachment"
              type="text"
              placeholder="filename.pdf"
              class="w-full h-11 px-4 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#8B1E23] outline-none"
            />
          </div>

          <div>
            <label class="block text-sm font-bold text-slate-700 mb-2">
              Description
            </label>

            <textarea
              v-model="reportForm.description"
              rows="4"
              placeholder="Enter report description..."
              class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#8B1E23] outline-none resize-none"
            ></textarea>
          </div>

        </div>

        <div
          class="p-6 border-t border-slate-200 flex justify-end gap-3"
        >

          <button
            @click="showReportModal = false"
            class="px-5 py-2.5 rounded-xl border border-slate-300 font-bold hover:bg-slate-100"
          >
            Cancel
          </button>

          <button
            @click="saveReport"
            class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D]"
          >
            {{ editingReport ? 'Save Changes' : 'Create Report' }}
          </button>

        </div>

      </div>
    </div>

    <!-- =====================================================
         DETAILS MODAL
    ====================================================== -->

    <div
      v-if="showDetailsModal && selectedReport"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div
        class="bg-white w-full max-w-2xl rounded-2xl shadow-xl"
      >

        <div
          class="p-6 border-b border-slate-200 flex items-center justify-between"
        >
          <div>
            <p
              class="text-xs font-bold text-[#8B1E23] uppercase tracking-wide"
            >
              {{ selectedReport.id }}
            </p>

            <h3
              class="text-xl font-bold text-slate-900 mt-1"
            >
              {{ selectedReport.title }}
            </h3>
          </div>

          <button
            @click="showDetailsModal = false"
            class="text-slate-400 hover:text-slate-700 text-xl"
          >
            ✕
          </button>
        </div>

        <div class="p-6 space-y-5">

          <div
            class="flex flex-wrap gap-2"
          >
            <span
              class="px-3 py-1 rounded-full text-xs font-bold border"
              :class="getStatusClass(selectedReport.status)"
            >
              {{ selectedReport.status }}
            </span>

            <span
              class="px-3 py-1 rounded-full text-xs font-bold"
              :class="getTypeClass(selectedReport.type)"
            >
              {{ selectedReport.type }}
            </span>
          </div>

          <div
            class="grid grid-cols-1 md:grid-cols-2 gap-4"
          >

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-500">
                Submitted By
              </p>

              <p class="font-bold text-slate-900 mt-1">
                {{ selectedReport.rank }}
                {{ selectedReport.submittedBy }}
              </p>
            </div>

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-500">
                Station
              </p>

              <p class="font-bold text-slate-900 mt-1">
                {{ selectedReport.station }}
              </p>
            </div>

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-500">
                Submitted Date
              </p>

              <p class="font-bold text-slate-900 mt-1">
                {{ selectedReport.submittedDate }}
              </p>
            </div>

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-500">
                Deadline
              </p>

              <p class="font-bold text-slate-900 mt-1">
                {{ selectedReport.deadline }}
              </p>
            </div>

          </div>

          <div>
            <p class="text-sm font-bold text-slate-700">
              Description
            </p>

            <p class="text-sm text-slate-600 mt-2 leading-6">
              {{ selectedReport.description || 'No description provided.' }}
            </p>
          </div>

          <div
            v-if="selectedReport.attachment"
            class="p-4 rounded-xl border border-slate-200 bg-slate-50"
          >

            <p class="text-xs text-slate-500">
              Attachment
            </p>

            <p class="text-sm font-bold text-[#8B1E23] mt-1">
              📎 {{ selectedReport.attachment }}
            </p>

          </div>

        </div>

        <div
          class="p-6 border-t border-slate-200 flex flex-wrap justify-end gap-2"
        >

          <button
            v-if="selectedReport.status === 'For Review'"
            @click="showDetailsModal = false; openReview(selectedReport, 'approve')"
            class="px-5 py-2.5 rounded-xl bg-green-600 text-white font-bold"
          >
            Approve
          </button>

          <button
            @click="showDetailsModal = false"
            class="px-5 py-2.5 rounded-xl border border-slate-300 font-bold hover:bg-slate-100"
          >
            Close
          </button>

        </div>

      </div>
    </div>

    <!-- =====================================================
         REVIEW MODAL
    ====================================================== -->

    <div
      v-if="showReviewModal && selectedReport"
      class="fixed inset-0 z-[60] bg-black/50 flex items-center justify-center p-4"
    >

      <div
        class="bg-white w-full max-w-lg rounded-2xl shadow-xl"
      >

        <div class="p-6 border-b border-slate-200">

          <h3
            class="text-xl font-bold text-slate-900"
          >
            {{
              reviewAction === 'approve'
                ? 'Approve Report'
                : reviewAction === 'reject'
                ? 'Reject Report'
                : 'Return Report'
            }}
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            {{ selectedReport.title }}
          </p>

        </div>

        <div class="p-6">

          <label
            class="block text-sm font-bold text-slate-700 mb-2"
          >
            Review Comment
            <span
              v-if="reviewAction !== 'approve'"
              class="text-red-500"
            >
              *
            </span>
          </label>

          <textarea
            v-model="reviewComment"
            rows="5"
            placeholder="Enter review notes or reason..."
            class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#8B1E23] outline-none resize-none"
          ></textarea>

        </div>

        <div
          class="p-6 border-t border-slate-200 flex justify-end gap-3"
        >

          <button
            @click="showReviewModal = false"
            class="px-5 py-2.5 rounded-xl border border-slate-300 font-bold"
          >
            Cancel
          </button>

          <button
            @click="submitReview"
            class="px-5 py-2.5 rounded-xl font-bold text-white"
            :class="
              reviewAction === 'approve'
                ? 'bg-green-600 hover:bg-green-700'
                : reviewAction === 'reject'
                ? 'bg-red-600 hover:bg-red-700'
                : 'bg-blue-600 hover:bg-blue-700'
            "
          >
            Confirm
          </button>

        </div>

      </div>
    </div>

    <!-- =====================================================
         DELETE MODAL
    ====================================================== -->

    <div
      v-if="showDeleteModal && reportToDelete"
      class="fixed inset-0 z-[70] bg-black/50 flex items-center justify-center p-4"
    >

      <div
        class="bg-white w-full max-w-md rounded-2xl shadow-xl p-6"
      >

        <div
          class="w-12 h-12 rounded-full bg-red-100 text-red-600 flex items-center justify-center text-xl"
        >
          !
        </div>

        <h3
          class="text-xl font-bold text-slate-900 mt-4"
        >
          Delete Report?
        </h3>

        <p
          class="text-sm text-slate-500 mt-2"
        >
          Are you sure you want to delete
          <strong>{{ reportToDelete.title }}</strong>?
          This action cannot be undone.
        </p>

        <div
          class="flex justify-end gap-3 mt-6"
        >

          <button
            @click="showDeleteModal = false"
            class="px-5 py-2.5 rounded-xl border border-slate-300 font-bold"
          >
            Cancel
          </button>

          <button
            @click="deleteReport"
            class="px-5 py-2.5 rounded-xl bg-red-600 text-white font-bold hover:bg-red-700"
          >
            Delete
          </button>

        </div>

      </div>
    </div>

    <!-- =====================================================
         TOAST
    ====================================================== -->

    <transition name="fade">

      <div
        v-if="toastMessage"
        class="fixed bottom-6 right-6 z-[100] px-5 py-4 rounded-xl shadow-lg text-white font-semibold"
        :class="
          toastType === 'error'
            ? 'bg-red-600'
            : 'bg-slate-900'
        "
      >
        {{ toastMessage }}
      </div>

    </transition>

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