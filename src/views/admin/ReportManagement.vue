```vue
<script setup>
import { computed, onMounted, onBeforeUnmount, ref } from 'vue'

import {
  deleteReportFile,
  getReportFile
} from '../../utils/reportFileStorage.js'

const props = defineProps({
  currentUser: {
    type: Object,
    default: null
  },

  registeredUsers: {
    type: Array,
    default: () => []
  },

  ICONS: {
    type: Object,
    required: true
  }
})







/* =========================================================
   STORAGE
========================================================= */

const STORAGE_KEY = 'firenotify_reports'
const SYNC_EVENT = 'fireNotifyReportsUpdated'

/* =========================================================
   STATE
========================================================= */

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
   PERSONNEL ASSIGNMENT
========================================================= */

const selectedPersonnelIds = ref([])
const personnelSearch = ref('')

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

  status: 'Pending Submission',
  submissionStatus: 'Not Submitted',

  description: '',
  attachment: '',
  filename: '',
  fileType: '',
  fileSize: null,
  fileStored: false,

  assignedPersonnel: [],

  assignedToId: '',
  assignedToUsername: '',
  assignedToName: '',
  assignedToEmail: '',

  assignedBy: '',
  assignedById: '',

  startedAt: null,
  submittedAt: null,

  submissionNote: '',
  submittedByUser: null,

  createdAt: ''
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

    status: 'Submitted',

    description:
      'Fire safety inspection conducted at Balingasag Public Market Complex.',

    attachment: 'InspectionChecklist_Sept9.pdf',

    assignedPersonnel: [],

    assignedToId: '',
    assignedToUsername: '',
    assignedToName: '',
    assignedToEmail: '',

    assignedBy: 'Admin',
    assignedById: 'admin-default',

    startedAt: null,
    submittedAt: null,

    submissionNote: '',
    submittedByUser: null,

    createdAt: new Date().toISOString()
  }
]

/* =========================================================
   LOAD REPORTS
========================================================= */

const loadReports = () => {
  try {
    const savedReports = localStorage.getItem(STORAGE_KEY)

    if (savedReports) {
      reports.value = JSON.parse(savedReports)
    } else {
      reports.value = defaultReports
      saveReports()
    }
  } catch (error) {
    console.error('Failed to load reports:', error)
    reports.value = defaultReports
  }
}

const reports = ref([])

/* =========================================================
   PERSONNEL
========================================================= */

const personnel = computed(() => {
  return props.registeredUsers
    .filter(user => user.role !== 'admin')
    .map(user => ({
      ...user,

      id: user.id,

      username:
        user.username ||
        user.identifier ||
        '',

      firstName:
        user.firstName ||
        '',

      lastName:
        user.lastName ||
        '',

      name:
        user.name ||
        `${user.firstName || ''} ${user.lastName || ''}`.trim(),

      rank:
        user.rank ||
        'FO1',

      position:
        user.position ||
        'Fire Officer',

      email:
        user.email ||
        user.identifier ||
        '',

      status:
        user.status ||
        'Active'
    }))
})

const filteredPersonnel = computed(() => {
  const query = personnelSearch.value
    .toLowerCase()
    .trim()

  if (!query) {
    return personnel.value
  }

  return personnel.value.filter(person => {
    const text = [
      person.name,
      person.username,
      person.rank,
      person.position,
      person.email
    ]
      .filter(Boolean)
      .join(' ')
      .toLowerCase()

    return text.includes(query)
  })
})

const selectedPersonnel = computed(() => {
  return personnel.value.filter(person =>
    selectedPersonnelIds.value.includes(person.id)
  )
})

/* =========================================================
   PERSONNEL ASSIGNMENT ACTIONS
========================================================= */

const togglePersonnel = id => {
  if (selectedPersonnelIds.value.includes(id)) {
    selectedPersonnelIds.value =
      selectedPersonnelIds.value.filter(
        item => item !== id
      )
  } else {
    selectedPersonnelIds.value.push(id)
  }
}

const selectAllPersonnel = () => {
  selectedPersonnelIds.value =
    filteredPersonnel.value.map(person => person.id)
}

const clearSelectedPersonnel = () => {
  selectedPersonnelIds.value = []
}

const getFullName = person => {
  if (!person) return 'Unnamed Personnel'

  return (
    person.name ||
    `${person.firstName || ''} ${person.lastName || ''}`.trim() ||
    person.username ||
    'Unnamed Personnel'
  )
}

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
   STATISTICS
========================================================= */

const totalReports = computed(() =>
  reports.value.length
)

const pendingCount = computed(() =>
  reports.value.filter(
    report =>
      report.status === 'Pending' ||
      report.status === 'Pending Submission' ||
      report.status === 'Not Submitted'
  ).length
)

const inProgressCount = computed(() =>
  reports.value.filter(
    report => report.status === 'In Progress'
  ).length
)

const submittedCount = computed(() =>
  reports.value.filter(
    report => report.status === 'Submitted'
  ).length
)

const forReviewCount = computed(() =>
  reports.value.filter(
    report =>
      report.status === 'For Review'
  ).length
)

const approvedCount = computed(() =>
  reports.value.filter(
    report => report.status === 'Approved'
  ).length
)

const rejectedCount = computed(() =>
  reports.value.filter(
    report => report.status === 'Rejected'
  ).length
)

const returnedCount = computed(() =>
  reports.value.filter(
    report => report.status === 'Returned'
  ).length
)

const overdueCount = computed(() =>
  reports.value.filter(
    report => report.status === 'Overdue'
  ).length
)

/* =========================================================
   FILTERED REPORTS
========================================================= */

const filteredReports = computed(() => {
  const query =
    searchQuery.value
      .toLowerCase()
      .trim()

  return reports.value.filter(report => {
    const assignedNames =
      (report.assignedPersonnel || [])
        .map(person => person.name)
        .join(' ')

    const searchableText = [
      report.id,
      report.title,
      report.type,
      report.submittedBy,
      report.rank,
      report.station,
      report.status,
      report.assignedToName,
      assignedNames
    ]
      .filter(Boolean)
      .join(' ')
      .toLowerCase()

    const matchesSearch =
      !query ||
      searchableText.includes(query)

    const matchesType =
      selectedType.value === 'All Report Types' ||
      report.type === selectedType.value

    const matchesStatus =
      selectedStatus.value === 'All Status' ||
      report.status === selectedStatus.value

    return (
      matchesSearch &&
      matchesType &&
      matchesStatus
    )
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
    (approvedCount.value /
      totalReports.value) *
      100
  )
})

const reviewRate = computed(() => {
  if (!totalReports.value) return 0

  return Math.round(
    (
      (
        forReviewCount.value +
        submittedCount.value
      ) /
      totalReports.value
    ) *
      100
  )
})

const correctionRate = computed(() => {
  if (!totalReports.value) return 0

  return Math.round(
    (
      (
        returnedCount.value +
        rejectedCount.value
      ) /
      totalReports.value
    ) *
      100
  )
})

const onTimeSubmission = computed(() => {
  if (!totalReports.value) return 0

  const late =
    reports.value.filter(
      report =>
        report.status === 'Overdue'
    ).length

  return Math.max(
    0,
    Math.round(
      (
        (totalReports.value - late) /
        totalReports.value
      ) *
        100
    )
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

  window.dispatchEvent(
    new CustomEvent(SYNC_EVENT)
  )
}

/* =========================================================
   SYNC
========================================================= */

const handleStorage = event => {
  if (event.key === STORAGE_KEY) {
    loadReports()
  }
}

const handleReportSync = () => {
  loadReports()
}

/* =========================================================
   TOAST
========================================================= */

const showToast = (
  message,
  type = 'success'
) => {
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
  selectedType.value =
    'All Report Types'
  selectedStatus.value =
    'All Status'
}

/* =========================================================
   CREATE REPORT
========================================================= */

const openCreateReport = () => {
  editingReport.value = null

  reportForm.value =
    emptyReport()

  selectedPersonnelIds.value = []
  personnelSearch.value = ''

  reportForm.value.assignedBy =
    props.currentUser?.name ||
    'Admin User'

  reportForm.value.assignedById =
    props.currentUser?.id ||
    'admin-default'

  showReportModal.value = true
}

/* =========================================================
   EDIT REPORT
========================================================= */

const openEditReport = report => {
  editingReport.value = report

  reportForm.value = {
    ...emptyReport(),
    ...report
  }

  selectedPersonnelIds.value =
    (report.assignedPersonnel || [])
      .map(person => person.id)
      .filter(Boolean)

  /*
    Backward compatibility:
    old reports may only have assignedToId.
  */
  if (
    !selectedPersonnelIds.value.length &&
    report.assignedToId
  ) {
    selectedPersonnelIds.value = [
      report.assignedToId
    ]
  }

  personnelSearch.value = ''

  showReportModal.value = true
}

/* =========================================================
   SAVE REPORT
========================================================= */

const saveReport = () => {
  if (
    !reportForm.value.title ||
    !reportForm.value.type
  ) {
    showToast(
      'Please complete the required fields.',
      'error'
    )

    return
  }

  if (
    !selectedPersonnelIds.value.length
  ) {
    showToast(
      'Please assign this report to at least one personnel.',
      'error'
    )

    return
  }

  const assignedPeople =
    personnel.value
      .filter(person =>
        selectedPersonnelIds.value.includes(
          person.id
        )
      )
      .map(person => ({
        id: person.id,

        username:
          person.username || '',

        name:
          getFullName(person),

        rank:
          person.rank || 'FO1',

        position:
          person.position ||
          'Fire Officer',

        email:
          person.email || ''
      }))

  if (!assignedPeople.length) {
    showToast(
      'Selected personnel could not be found.',
      'error'
    )

    return
  }

  const firstPersonnel =
    assignedPeople[0]

  const baseReport = {
    ...reportForm.value,

    assignedPersonnel:
      assignedPeople,

    assignedToId:
      firstPersonnel.id,

    assignedToUsername:
      firstPersonnel.username,

    assignedToName:
      firstPersonnel.name,

    assignedToEmail:
      firstPersonnel.email,

    assignedBy:
      props.currentUser?.name ||
      reportForm.value.assignedBy ||
      'Admin User',

    assignedById:
      props.currentUser?.id ||
      reportForm.value.assignedById ||
      'admin-default'
  }

  /*
    Admin creates an assignment, not a personnel submission.
    The worker must explicitly upload a file later.
  */
  if (!editingReport.value) {
    baseReport.status = 'Pending Submission'
    baseReport.submissionStatus = 'Not Submitted'
    baseReport.createdAt =
      new Date().toISOString()
    baseReport.startedAt = null
    baseReport.submittedAt = null
    baseReport.submittedBy = null
    baseReport.filename = ''
    baseReport.fileType = ''
    baseReport.fileSize = null
    baseReport.fileStored = false
    baseReport.attachment = ''
    baseReport.submissionNote = ''
    baseReport.submittedByUser = null
  }

  if (editingReport.value) {
    const index =
      reports.value.findIndex(
        report =>
          report.id ===
          editingReport.value.id
      )

    if (index !== -1) {
      reports.value[index] = {
        ...reports.value[index],
        ...baseReport,
        id: editingReport.value.id
      }
    }

    showToast(
      'Report assignment updated successfully.'
    )
  } else {
    const newId =
      'REP-' +
      String(
        Date.now()
      ).slice(-6)

    reports.value.unshift({
      ...baseReport,
      id: newId
    })

    showToast(
      'Report assigned successfully.'
    )
  }

  saveReports()

  showReportModal.value = false

  selectedPersonnelIds.value = []
  personnelSearch.value = ''
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

const openReview = (
  report,
  action
) => {
  selectedReport.value = report

  reviewAction.value = action
  reviewComment.value = ''

  showReviewModal.value = true
}

const submitReview = () => {
  if (!selectedReport.value) return

  const report =
    reports.value.find(
      item =>
        item.id ===
        selectedReport.value.id
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

  if (
    reviewAction.value === 'approve'
  ) {
    report.status = 'Approved'
    report.submissionStatus = 'Approved'

    report.reviewComment =
      reviewComment.value

    report.reviewedBy =
      props.currentUser?.name ||
      'Admin User'

    report.reviewedAt =
      new Date().toISOString()

    showToast(
      'Report approved successfully.'
    )
  }

  if (
    reviewAction.value === 'reject'
  ) {
    report.status = 'Rejected'
    report.submissionStatus = 'Rejected'

    report.reviewComment =
      reviewComment.value

    report.reviewedBy =
      props.currentUser?.name ||
      'Admin User'

    report.reviewedAt =
      new Date().toISOString()

    showToast(
      'Report rejected.'
    )
  }

  if (
    reviewAction.value === 'return'
  ) {
    report.status = 'Returned'
    report.submissionStatus = 'Returned'

    report.reviewComment =
      reviewComment.value

    report.reviewedBy =
      props.currentUser?.name ||
      'Admin User'

    report.reviewedAt =
      new Date().toISOString()

    showToast(
      'Report returned for correction.'
    )
  }

  saveReports()

  showReviewModal.value = false
}

/* =========================================================
   SEND REMINDER
========================================================= */

const sendReminder = report => {
  showToast(
    `Reminder sent to ${
      report.assignedToName ||
      report.submittedBy ||
      'personnel'
    }.`
  )
}

/* =========================================================
   DELETE REPORT
========================================================= */

const openDeleteReport = report => {
  reportToDelete.value = report
  showDeleteModal.value = true
}

const deleteReport = async () => {
  if (!reportToDelete.value) return

  const targetReport = reportToDelete.value
  const reportId = targetReport.fileReferenceId || targetReport.id

  try {
    const fileDeleted = await deleteReportFile(reportId)

    if (!fileDeleted) {
      showToast('Unable to remove the stored file for this report.', 'error')
      return
    }
  } catch (error) {
    console.error('FireNotify: admin delete file failed', error)
    showToast('Unable to remove the stored file for this report.', 'error')
    return
  }

  reports.value =
    reports.value.filter(
      report =>
        report.id !==
        targetReport.id
    )

  saveReports()

  showDeleteModal.value = false
  reportToDelete.value = null

  showToast(
    'Report deleted successfully.'
  )
}

/* =========================================================
   STATUS STYLING
========================================================= */

const getStatusClass = status => {
  const classes = {
    Pending:
      'bg-yellow-50 text-yellow-700 border-yellow-200',

    'In Progress':
      'bg-blue-50 text-blue-700 border-blue-200',

    Submitted:
      'bg-purple-50 text-purple-700 border-purple-200',

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

  return (
    classes[status] ||
    'bg-slate-100 text-slate-600 border-slate-200'
  )
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

  return (
    classes[type] ||
    'bg-slate-100 text-slate-600'
  )
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

const viewFile = async file => {
  const report = file && file.reportId ? file : null
  const attachmentId = report?.reportId || report?.id || file?.id || file?.reportId
  const targetReport = report || selectedReport.value || file

  if (!targetReport) {
    showToast('No attachment available.', 'error')
    return
  }

  const reportId = targetReport.fileReferenceId || targetReport.id || attachmentId

  try {
    const fileRecord = await getReportFile(reportId)

    if (!fileRecord || !fileRecord.file) {
      showToast('This report has no uploaded file available.', 'error')
      return
    }

    const rawFile = fileRecord.file
    const mimeType = (fileRecord.mimeType || targetReport.fileType || 'application/pdf').toLowerCase()
    const displayName = fileRecord.filename || targetReport.filename || targetReport.attachment || 'report-file'

    let blob = rawFile

    if (rawFile instanceof Blob || rawFile instanceof File) {
      blob = rawFile
    } else if (rawFile instanceof ArrayBuffer) {
      blob = new Blob([rawFile], { type: mimeType })
    } else if (ArrayBuffer.isView(rawFile)) {
      const buffer = rawFile.buffer.slice(rawFile.byteOffset, rawFile.byteOffset + rawFile.byteLength)
      blob = new Blob([buffer], { type: mimeType })
    } else if (typeof rawFile === 'string') {
      blob = new Blob([rawFile], { type: mimeType })
    } else {
      blob = new Blob([String(rawFile || '')], { type: mimeType })
    }

    if (!blob || !(blob instanceof Blob) || blob.size === 0) {
      showToast('The attached file is empty or unreadable.', 'error')
      return
    }

    const objectUrl = URL.createObjectURL(blob)

    if (mimeType.includes('pdf')) {
      const previewWindow = window.open(objectUrl, '_blank')

      if (!previewWindow) {
        window.location.href = objectUrl
      }

      setTimeout(() => URL.revokeObjectURL(objectUrl), 15000)
      showToast(`Opening ${displayName}...`)
      return
    }

    const link = document.createElement('a')
    link.href = objectUrl
    link.download = displayName
    document.body.appendChild(link)
    link.click()
    link.remove()
    setTimeout(() => URL.revokeObjectURL(objectUrl), 15000)
    showToast(`Downloading ${displayName}...`)
  } catch (error) {
    console.error('FireNotify: unable to retrieve report file', error)
    showToast('Unable to retrieve the uploaded file for this report.', 'error')
  }
}

const downloadAttachment = report => {
  if (!report) return

  const reportId = report.fileReferenceId || report.id
  if (!reportId) {
    showToast('No attachment is available for download.', 'error')
    return
  }

  viewFile({ reportId, id: reportId })
}

/* =========================================================
   MOUNT
========================================================= */

onMounted(() => {
  loadReports()

  window.addEventListener(
    'storage',
    handleStorage
  )

  window.addEventListener(
    SYNC_EVENT,
    handleReportSync
  )
})

onBeforeUnmount(() => {
  window.removeEventListener(
    'storage',
    handleStorage
  )

  window.removeEventListener(
    SYNC_EVENT,
    handleReportSync
  )
})
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
          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">
            Records Management
          </p>

          <h2
            class="text-2xl font-bold text-slate-900 mt-1"
          >
            Report Management
          </h2>

          <p
            class="text-base text-slate-500 mt-1"
          >
            Create reports, assign them to personnel,
            monitor submissions, and review completed reports.
          </p>
        </div>

        <button
          @click="openCreateReport"
          class="px-6 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition shadow-sm"
        >
          + Assign Report
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
          {{ pendingCount }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Pending
        </p>
      </div>

      <div
        class="bg-white border border-blue-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-3xl font-bold text-blue-600">
          {{ inProgressCount }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          In Progress
        </p>
      </div>

      <div
        class="bg-white border border-purple-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-3xl font-bold text-purple-600">
          {{ submittedCount }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Submitted
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

    </section>

    <!-- =====================================================
         SEARCH / FILTER
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5"
    >
      <div
        class="flex flex-col lg:flex-row gap-4"
      >

        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search report, ID, personnel..."
          class="flex-1 h-12 px-4 rounded-xl border border-slate-300 text-base focus:ring-2 focus:ring-[#8B1E23] focus:border-[#8B1E23] outline-none"
        />

        <select
          v-model="selectedType"
          class="h-12 px-4 rounded-xl border border-slate-300 text-base lg:w-60 focus:ring-2 focus:ring-[#8B1E23] outline-none"
        >
          <option>
            All Report Types
          </option>

          <option>
            Incident Report
          </option>

          <option>
            Inspection Report
          </option>

          <option>
            Accomplishment Report
          </option>

          <option>
            Activity Report
          </option>
        </select>

        <select
          v-model="selectedStatus"
          class="h-12 px-4 rounded-xl border border-slate-300 text-base lg:w-52 focus:ring-2 focus:ring-[#8B1E23] outline-none"
        >
          <option>
            All Status
          </option>

          <option>Pending Submission</option>
          <option>Pending</option>
          <option>In Progress</option>
          <option>Submitted</option>
          <option>For Review</option>
          <option>Approved</option>
          <option>Returned</option>
          <option>Rejected</option>
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
          <h2
            class="text-xl font-bold text-slate-900"
          >
            Assigned Reports
          </h2>

          <p
            class="text-sm text-slate-500 mt-1"
          >
            {{ filteredReports.length }}
            report(s) displayed
          </p>
        </div>

        <div
          class="text-sm font-semibold text-slate-500"
        >
          {{ submittedCount }} submitted
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
                  {{ report.status }}
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

                <span
                  class="text-slate-600"
                >
                  <strong>
                    Assigned to:
                  </strong>

                  <span
                    v-if="report.assignedPersonnel?.length"
                  >
                    {{
                      report.assignedPersonnel
                        .map(person => person.name)
                        .join(', ')
                    }}
                  </span>

                  <span
                    v-else
                  >
                    No personnel assigned
                  </span>
                </span>

                <span
                  class="text-slate-400"
                >
                  ID: {{ report.id }}
                </span>

              </div>

              <p
                v-if="report.status === 'Overdue'"
                class="text-sm text-[#8B1E23] font-semibold mt-2"
              >
                Deadline:
                {{ report.deadline }}
              </p>

              <p
                v-else
                class="text-sm text-slate-400 mt-2"
              >
                Deadline:
                {{ report.deadline || 'No deadline' }}
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
                v-if="
                  report.status === 'Submitted' ||
                  report.status === 'For Review'
                "
                @click="openReview(report, 'approve')"
                class="px-4 py-2.5 rounded-lg bg-green-600 text-white text-sm font-bold hover:bg-green-700"
              >
                Approve
              </button>

              <button
                v-if="
                  report.status === 'Submitted' ||
                  report.status === 'For Review'
                "
                @click="openReview(report, 'return')"
                class="px-4 py-2.5 rounded-lg bg-blue-600 text-white text-sm font-bold hover:bg-blue-700"
              >
                Return
              </button>

              <button
                v-if="
                  report.status === 'Submitted' ||
                  report.status === 'For Review'
                "
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
              >
                Edit
              </button>

              <button
                @click="openDeleteReport(report)"
                class="px-3 py-2.5 rounded-lg border border-red-200 text-red-600 text-sm font-bold hover:bg-red-50"
              >
                Delete
              </button>

            </div>

          </div>

        </div>

      </div>

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
         ANALYTICS
    ====================================================== -->

    <section
      class="grid grid-cols-1 xl:grid-cols-2 gap-6"
    >

      <div
        class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
      >

        <div
          class="border-b border-slate-200 pb-5"
        >
          <h2
            class="text-xl font-bold text-slate-900"
          >
            Report Analytics
          </h2>

          <p
            class="text-sm text-slate-500 mt-1"
          >
            Current report processing performance
          </p>
        </div>

        <div
          class="mt-5 space-y-5"
        >

          <div>
            <div
              class="flex justify-between text-sm font-semibold text-slate-700 mb-2"
            >
              <span>
                On-Time Submission
              </span>

              <span>
                {{ onTimeSubmission }}%
              </span>
            </div>

            <div
              class="h-2.5 rounded-full bg-slate-100 overflow-hidden"
            >
              <div
                class="h-full rounded-full bg-green-500 transition-all"
                :style="{
                  width: `${onTimeSubmission}%`
                }"
              ></div>
            </div>
          </div>

          <div>
            <div
              class="flex justify-between text-sm font-semibold text-slate-700 mb-2"
            >
              <span>
                Approval Rate
              </span>

              <span>
                {{ approvalRate }}%
              </span>
            </div>

            <div
              class="h-2.5 rounded-full bg-slate-100 overflow-hidden"
            >
              <div
                class="h-full rounded-full bg-blue-500 transition-all"
                :style="{
                  width: `${approvalRate}%`
                }"
              ></div>
            </div>
          </div>

          <div>
            <div
              class="flex justify-between text-sm font-semibold text-slate-700 mb-2"
            >
              <span>
                Correction / Rejection
              </span>

              <span>
                {{ correctionRate }}%
              </span>
            </div>

            <div
              class="h-2.5 rounded-full bg-slate-100 overflow-hidden"
            >
              <div
                class="h-full rounded-full bg-yellow-500 transition-all"
                :style="{
                  width: `${correctionRate}%`
                }"
              ></div>
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
          <h2
            class="text-xl font-bold text-slate-900"
          >
            Recently Uploaded Files
          </h2>

          <p
            class="text-sm text-slate-500 mt-1"
          >
            Latest report attachments
          </p>
        </div>

        <div
          class="mt-5 space-y-3"
        >

          <div
            v-for="file in uploadedFiles"
            :key="file.name"
            class="flex items-center justify-between gap-3 p-3 rounded-xl border border-slate-200 bg-slate-50 hover:bg-slate-100 transition"
          >

            <div
              class="flex items-center gap-3 min-w-0"
            >

              <div
                class="w-10 h-10 rounded-lg bg-white border border-slate-200 flex items-center justify-center text-xs font-bold text-[#8B1E23]"
              >
                {{ file.type }}
              </div>

              <div
                class="min-w-0"
              >

                <p
                  class="text-sm font-bold text-slate-900 truncate"
                >
                  {{ file.name }}
                </p>

                <p
                  class="text-xs text-slate-500 mt-1"
                >
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
         CREATE / EDIT REPORT MODAL
    ====================================================== -->

    <div
      v-if="showReportModal"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div
        class="fn-modal-panel bg-white w-full max-w-3xl rounded-2xl shadow-xl"
      >

        <div
          class="p-6 border-b border-slate-200 flex items-center justify-between"
        >

          <div>

            <h3
              class="text-xl font-bold text-slate-900"
            >
              {{
                editingReport
                  ? 'Edit Report Assignment'
                  : 'Assign Report to Personnel'
              }}
            </h3>

            <p
              class="text-sm text-slate-500 mt-1"
            >
              Create a report and assign it directly to registered personnel.
            </p>

          </div>

          <button
            @click="showReportModal = false"
            class="text-slate-400 hover:text-slate-700 text-xl"
          >
            ✕
          </button>

        </div>

        <div
          class="p-6 space-y-5"
        >

          <!-- TITLE -->

          <div>

            <label
              class="block text-sm font-bold text-slate-700 mb-2"
            >
              Report Title *
            </label>

            <input
              v-model="reportForm.title"
              type="text"
              placeholder="Enter report title"
              class="w-full h-11 px-4 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#8B1E23] outline-none"
            />

          </div>

          <!-- TYPE -->

          <div
            class="grid grid-cols-1 md:grid-cols-2 gap-4"
          >

            <div>

              <label
                class="block text-sm font-bold text-slate-700 mb-2"
              >
                Report Type *
              </label>

              <select
                v-model="reportForm.type"
                class="w-full h-11 px-4 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#8B1E23] outline-none"
              >

                <option>
                  Incident Report
                </option>

                <option>
                  Inspection Report
                </option>

                <option>
                  Accomplishment Report
                </option>

                <option>
                  Activity Report
                </option>

              </select>

            </div>

          </div>

          <!-- ASSIGN PERSONNEL -->

          <div>

            <div
              class="flex items-center justify-between mb-2"
            >

              <label
                class="block text-sm font-bold text-slate-700"
              >
                Assign Personnel *
              </label>

              <span
                class="text-xs font-bold text-[#8B1E23]"
              >
                {{ selectedPersonnelIds.length }}
                selected
              </span>

            </div>

            <input
              v-model="personnelSearch"
              type="text"
              placeholder="Search registered personnel..."
              class="w-full h-11 px-4 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]"
            />

            <div
              class="flex items-center justify-between mt-3"
            >

              <button
                type="button"
                @click="selectAllPersonnel"
                class="text-xs font-bold text-[#8B1E23] hover:underline"
              >
                Select All
              </button>

              <button
                type="button"
                @click="clearSelectedPersonnel"
                class="text-xs font-bold text-slate-500 hover:text-slate-800"
              >
                Clear
              </button>

            </div>

            <div
              class="mt-3 border border-slate-200 rounded-xl overflow-hidden max-h-64 overflow-y-auto"
            >

              <label
                v-for="person in filteredPersonnel"
                :key="person.id"
                class="flex items-center gap-3 p-3 border-b border-slate-100 last:border-b-0 hover:bg-slate-50 cursor-pointer"
              >

                <input
                  type="checkbox"
                  :checked="
                    selectedPersonnelIds.includes(
                      person.id
                    )
                  "
                  @change="
                    togglePersonnel(person.id)
                  "
                  class="h-4 w-4 accent-[#8B1E23]"
                />

                <div
                  class="min-w-0 flex-1"
                >

                  <p
                    class="font-bold text-sm text-slate-800 truncate"
                  >
                    {{ getFullName(person) }}
                  </p>

                  <p
                    class="text-xs text-slate-500 truncate"
                  >
                    {{ person.rank }}
                    •
                    {{ person.position }}
                  </p>

                </div>

                <span
                  v-if="
                    selectedPersonnelIds.includes(
                      person.id
                    )
                  "
                  class="text-xs font-bold text-green-600"
                >
                  Assigned
                </span>

              </label>

              <div
                v-if="!filteredPersonnel.length"
                class="p-6 text-center"
              >

                <p
                  class="text-sm font-semibold text-slate-600"
                >
                  No registered personnel found.
                </p>

                <p
                  class="text-xs text-slate-400 mt-1"
                >
                  Register a personnel account first.
                </p>

              </div>

            </div>

          </div>

          <!-- DEADLINE -->

          <div>

              <label
                class="block text-sm font-bold text-slate-700 mb-2"
              >
                Deadline
              </label>

              <input
                v-model="reportForm.deadline"
                type="text"
                placeholder="September 25, 2026 • 5:00 PM"
                class="w-full h-11 px-4 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#8B1E23] outline-none"
              />

          </div>

          <!-- DESCRIPTION -->

          <div>

            <label
              class="block text-sm font-bold text-slate-700 mb-2"
            >
              Report Instructions / Description
            </label>

            <textarea
              v-model="reportForm.description"
              rows="5"
              placeholder="Describe what the assigned personnel needs to prepare..."
              class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#8B1E23] outline-none resize-none"
            ></textarea>

          </div>

          <!-- SELECTED PERSONNEL SUMMARY -->

          <div
            v-if="selectedPersonnel.length"
            class="p-4 rounded-xl bg-red-50 border border-red-100"
          >

            <p
              class="text-sm font-bold text-[#8B1E23]"
            >
              Assigned Personnel
            </p>

            <div
              class="flex flex-wrap gap-2 mt-3"
            >

              <span
                v-for="person in selectedPersonnel"
                :key="person.id"
                class="px-3 py-2 rounded-lg bg-white border border-red-100 text-sm font-semibold text-slate-700"
              >
                {{ getFullName(person) }}
              </span>

            </div>

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
            {{
              editingReport
                ? 'Save Changes'
                : 'Assign Report'
            }}
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
        class="bg-white w-full max-w-2xl rounded-2xl shadow-xl max-h-[90vh] overflow-y-auto"
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

        <div
          class="p-6 space-y-5"
        >

          <div
            class="flex flex-wrap gap-2"
          >

            <span
              class="px-3 py-1 rounded-full text-xs font-bold border"
              :class="
                getStatusClass(
                  selectedReport.status
                )
              "
            >
              {{ selectedReport.status }}
            </span>

            <span
              class="px-3 py-1 rounded-full text-xs font-bold"
              :class="
                getTypeClass(
                  selectedReport.type
                )
              "
            >
              {{ selectedReport.type }}
            </span>

          </div>

          <!-- ASSIGNED PERSONNEL -->

          <div
            class="p-4 rounded-xl bg-red-50 border border-red-100"
          >

            <p
              class="text-xs font-bold text-[#8B1E23] uppercase"
            >
              Assigned Personnel
            </p>

            <div
              v-if="
                selectedReport.assignedPersonnel?.length
              "
              class="flex flex-wrap gap-2 mt-3"
            >

              <span
                v-for="person in selectedReport.assignedPersonnel"
                :key="person.id"
                class="px-3 py-2 rounded-lg bg-white border border-red-100 text-sm font-semibold text-slate-700"
              >
                {{ person.name }}
              </span>

            </div>

            <p
              v-else
              class="text-sm text-slate-500 mt-2"
            >
              No personnel assigned.
            </p>

          </div>

          <!-- INFORMATION -->

          <div
            class="grid grid-cols-1 md:grid-cols-2 gap-4"
          >

            <div
              class="p-4 rounded-xl bg-slate-50"
            >

              <p
                class="text-xs text-slate-500"
              >
                Deadline
              </p>

              <p
                class="font-bold text-slate-900 mt-1"
              >
                {{
                  selectedReport.deadline ||
                  'No deadline'
                }}
              </p>

            </div>

            <div
              class="p-4 rounded-xl bg-slate-50"
            >

              <p
                class="text-xs text-slate-500"
              >
                Assigned By
              </p>

              <p
                class="font-bold text-slate-900 mt-1"
              >
                {{
                  selectedReport.assignedBy ||
                  'Admin'
                }}
              </p>

            </div>

            <div
              class="p-4 rounded-xl bg-slate-50"
            >

              <p
                class="text-xs text-slate-500"
              >
                Submitted Date
              </p>

              <p
                class="font-bold text-slate-900 mt-1"
              >
                {{
                  selectedReport.submittedDate ||
                  'Pending'
                }}
              </p>

            </div>

            <div
              class="p-4 rounded-xl bg-slate-50"
            >

              <p
                class="text-xs text-slate-500"
              >
                Submitted At
              </p>

              <p
                class="font-bold text-slate-900 mt-1"
              >
                {{
                  selectedReport.submittedAt ||
                  'Not submitted'
                }}
              </p>

            </div>

          </div>

          <!-- DESCRIPTION -->

          <div>

            <p
              class="text-sm font-bold text-slate-700"
            >
              Report Instructions
            </p>

            <p
              class="text-sm text-slate-600 mt-2 leading-6"
            >
              {{
                selectedReport.description ||
                'No instructions provided.'
              }}
            </p>

          </div>

          <!-- SUBMISSION NOTE -->

          <div
            v-if="
              selectedReport.submissionNote
            "
            class="p-4 rounded-xl bg-purple-50 border border-purple-100"
          >

            <p
              class="text-xs font-bold text-purple-700 uppercase"
            >
              Personnel Submission Note
            </p>

            <p
              class="text-sm text-slate-700 mt-2"
            >
              {{ selectedReport.submissionNote }}
            </p>

          </div>

          <!-- REVIEW COMMENT -->

          <div
            v-if="
              selectedReport.reviewComment
            "
            class="p-4 rounded-xl bg-blue-50 border border-blue-100"
          >

            <p
              class="text-xs font-bold text-blue-700 uppercase"
            >
              Admin Review
            </p>

            <p
              class="text-sm text-slate-700 mt-2"
            >
              {{ selectedReport.reviewComment }}
            </p>

            <p
              class="text-xs text-slate-500 mt-2"
            >
              Reviewed by:
              {{
                selectedReport.reviewedBy ||
                'Admin'
              }}
            </p>

          </div>

          <!-- ATTACHMENT -->

          <div
            v-if="selectedReport.attachment || selectedReport.filename"
            class="p-4 rounded-xl border border-slate-200 bg-slate-50"
          >

            <p
              class="text-xs text-slate-500"
            >
              Attachment
            </p>

            <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 mt-2">
              <p class="text-sm font-bold text-[#8B1E23]">
                📎
                {{ selectedReport.attachment || selectedReport.filename }}
              </p>

              <div class="flex gap-2">
                <button
                  @click="viewFile({ id: selectedReport.fileReferenceId || selectedReport.id, reportId: selectedReport.fileReferenceId || selectedReport.id })"
                  class="px-3 py-2 rounded-lg border border-slate-300 bg-white text-slate-700 text-sm font-bold hover:bg-slate-100"
                >
                  View
                </button>

                <button
                  @click="downloadAttachment(selectedReport)"
                  class="px-3 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]"
                >
                  Download
                </button>
              </div>
            </div>

          </div>

          <div v-else class="p-4 rounded-xl border border-dashed border-slate-200 bg-slate-50 text-sm text-slate-500">
            No attachment
          </div>

        </div>

        <div
          class="p-6 border-t border-slate-200 flex flex-wrap justify-end gap-2"
        >

          <button
            v-if="
              selectedReport.status === 'Submitted' ||
              selectedReport.status === 'For Review'
            "
            @click="
              showDetailsModal = false;
              openReview(
                selectedReport,
                'approve'
              )
            "
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
      v-if="
        showReviewModal &&
        selectedReport
      "
      class="fixed inset-0 z-[60] bg-black/50 flex items-center justify-center p-4"
    >

      <div
        class="bg-white w-full max-w-lg rounded-2xl shadow-xl"
      >

        <div
          class="p-6 border-b border-slate-200"
        >

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

          <p
            class="text-sm text-slate-500 mt-1"
          >
            {{ selectedReport.title }}
          </p>

        </div>

        <div class="p-6">

          <label
            class="block text-sm font-bold text-slate-700 mb-2"
          >
            Review Comment

            <span
              v-if="
                reviewAction !== 'approve'
              "
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
            @click="
              showReviewModal = false
            "
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
      v-if="
        showDeleteModal &&
        reportToDelete
      "
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
          <strong>
            {{ reportToDelete.title }}
          </strong>?
          This action cannot be undone.
        </p>

        <div
          class="flex justify-end gap-3 mt-6"
        >

          <button
            @click="
              showDeleteModal = false
            "
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
```

### 2. AdminDashboard.vue

Sa imong `AdminDashboard.vue`, make sure **Report Management** receives `registeredUsers`, exactly like Activity Management:

```vue
<ReportManagement
  v-else-if="activeMenu === 'Report Mgmt.'"
  :current-user="currentUser"
  :registered-users="registeredUsers"
/>
