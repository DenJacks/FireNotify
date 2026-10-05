```vue
<script setup>
import { computed, onMounted, onBeforeUnmount, ref } from 'vue'

import {
  createReport,
  deleteReport as deleteReportFromApi,
  getReportArchiveIds,
  getReports,
  setReportArchive,
  updateReport,
  updateReportSubmission
} from '../../utils/reportApi.js'
import '../../styles/operations.css'
import { formatOperationDate, formatOperationTime } from '../../utils/operationsFormat.js'

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

const getUserDisplayName = user => {
  if (!user) return 'Admin'
  const fullName = `${user.first_name || user.firstName || ''} ${user.last_name || user.lastName || ''}`.trim()
  return fullName || user.name || user.username || user.email || 'Admin'
}

const getAssignedByName = report => {
  if (report.assigned_by_name || report.assignedByName) {
    return report.assigned_by_name || report.assignedByName
  }

  const creator = report.assigned_by ?? report.assignedBy ?? report.created_by ?? report.createdBy
  if (creator && typeof creator === 'object') return getUserDisplayName(creator)

  const creatorId = creator
  const matchedCreator = props.registeredUsers.find(user => String(user.id) === String(creatorId))
  if (matchedCreator) return getUserDisplayName(matchedCreator)

  return report.assigned_by_username || report.assignedByUsername ||
    report.assigned_by_email || report.assignedByEmail || 'Admin'
}







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
const selectedPersonnelId = ref('All Personnel')
const selectedPeriod = ref('All Time')
const reportView = ref('active')
const archivedReportIds = ref(new Set())
const REPORT_TYPES_KEY = 'fireNotifyReportTypes'
const reportTypes = ref([
  'Incident Report',
  'Inspection Report',
  'Accomplishment Report',
  'Activity Report'
])
const showNewReportType = ref(false)
const newReportTypeName = ref('')

const mergeReportTypes = values => {
  const types = [...reportTypes.value, ...values]
    .map(value => String(value || '').trim())
    .filter(Boolean)
  const uniqueTypes = [...new Map(types.map(type => [type.toLowerCase(), type])).values()]
  reportTypes.value = uniqueTypes
  localStorage.setItem(REPORT_TYPES_KEY, JSON.stringify(uniqueTypes))
}

const loadSavedReportTypes = () => {
  try {
    const saved = JSON.parse(localStorage.getItem(REPORT_TYPES_KEY) || '[]')
    if (Array.isArray(saved)) mergeReportTypes(saved)
  } catch (error) {
    console.warn('FireNotify: unable to load saved report types', error)
  }
}

const createReportType = () => {
  const name = newReportTypeName.value.trim()
  if (!name) return
  const existing = reportTypes.value.find(type => type.toLowerCase() === name.toLowerCase())
  if (!existing) mergeReportTypes([name])
  reportForm.value.type = existing || name
  newReportTypeName.value = ''
  showNewReportType.value = false
}

const showReportModal = ref(false)
const showDetailsModal = ref(false)
const showDeleteModal = ref(false)
const showReviewModal = ref(false)

const editingReport = ref(null)
const selectedReport = ref(null)
const hasTimeValue = value => /(?:T|\s)\d{1,2}:\d{2}/.test(String(value || ''))
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

/* =========================================================
   LOAD REPORTS
========================================================= */

const loadReports = async () => {
  try {
    const reportRecords = await getReports()
    mergeReportTypes(reportRecords.map(report => report.report_type || report.type))
    archivedReportIds.value = new Set()
    const userId = props.currentUser?.id
    if (userId !== null && userId !== undefined) {
      try {
        archivedReportIds.value = new Set(await getReportArchiveIds(userId))
      } catch (error) {
        console.error('FireNotify: unable to load Admin report archives', error)
      }
    }
    const peopleById = new Map(props.registeredUsers.map(person => [String(person.id), person]))
    const statusLabels = {
      PENDING: 'Pending',
      IN_PROGRESS: 'In Progress',
      SUBMITTED: 'Submitted',
      FOR_REVIEW: 'For Review',
      APPROVED: 'Approved',
      RETURNED: 'Returned',
      REJECTED: 'Rejected'
    }

    reports.value = reportRecords.flatMap(report => {
      const assignedPeople = (report.assigned_personnel_ids || [])
        .map(id => peopleById.get(String(id)))
        .filter(Boolean)
        .map(person => ({
          ...person,
          name: person.name || `${person.firstName || person.first_name || ''} ${person.lastName || person.last_name || ''}`.trim() || person.username || person.email
        }))

      const assignments = report.assignments || []
      if (!assignments.length) {
        return [{
          id: report.id,
          rowId: `report-${report.id}-unassigned`,
          reportId: report.id,
          title: report.title,
          type: report.report_type,
          description: report.description,
          submittedBy: '',
          assignedPersonnel: [],
          assignedById: report.assigned_by ?? report.created_by,
          assignedBy: getAssignedByName(report),
          assignedByName: getAssignedByName(report),
          deadline: report.deadline,
          submittedDate: '',
          status: 'Unassigned',
          submissionStatus: 'UNASSIGNED',
          accomplishment: '',
          remarks: '',
          reviewComment: '',
          reviewedBy: '',
          reviewedAt: '',
          attachment: '',
          filename: '',
          hasEvidence: false,
          isActiveAssignment: false,
          isPrimaryAssignment: true,
          createdAt: report.created_at
        }]
      }

      return assignments.map((assignment, assignmentIndex) => {
        const person = peopleById.get(String(assignment.personnel))
        const name = person?.name || `${person?.firstName || person?.first_name || ''} ${person?.lastName || person?.last_name || ''}`.trim() || assignment.personnel_name || person?.username || person?.email || 'Personnel'
        const status = statusLabels[assignment.status] || 'Pending'
        const date = report.deadline ? new Date(report.deadline) : null
        const overdue = date && !Number.isNaN(date.getTime()) && date < new Date() && ['Pending', 'In Progress', 'Returned'].includes(status)

        return {
          id: report.id,
          rowId: assignment.id,
          reportId: report.id,
          submissionId: assignment.id,
          title: report.title,
          type: report.report_type,
          description: report.description,
          submittedBy: name,
          submittedById: assignment.personnel,
          assignedToId: assignment.personnel,
          assignedPersonnel: assignedPeople,
          assignedById: report.assigned_by ?? report.created_by,
          assignedBy: getAssignedByName(report),
          assignedByName: getAssignedByName(report),
          deadline: report.deadline,
          submittedDate: assignment.submitted_at || '',
          status: overdue ? 'Overdue' : status,
          submissionStatus: assignment.status,
          accomplishment: assignment.content || '',
          remarks: assignment.review_comment || '',
          reviewComment: assignment.review_comment || '',
          reviewedBy: assignment.reviewer ? peopleById.get(String(assignment.reviewer))?.name || 'Admin' : '',
          reviewedAt: assignment.reviewed_at || '',
          attachment: assignment.attachment || '',
          filename: assignment.attachment?.split('/').pop() || '',
          hasEvidence: Boolean(assignment.attachment),
          isActiveAssignment: assignment.is_active,
          isPrimaryAssignment: assignmentIndex === 0,
          createdAt: report.created_at
        }
      })
    })
  } catch (error) {
    console.error('Failed to load reports:', error)
    showToast('Unable to load reports from Django.', 'error')
  }
}

const reports = ref([])

/* =========================================================
   PERSONNEL
========================================================= */

const personnel = computed(() => {
  return props.registeredUsers
    .filter(user => String(user?.role || '').trim().toUpperCase() === 'PERSONNEL')
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

    const matchesPersonnel = selectedPersonnelId.value === 'All Personnel' ||
      String(report.assignedToId || report.submittedById) === String(selectedPersonnelId.value)
    const reportDate = new Date(report.submittedDate || report.deadline)
    const validReportDate = !Number.isNaN(reportDate.getTime())
    const now = new Date()
    const matchesPeriod = selectedPeriod.value === 'All Time' ||
      (validReportDate && selectedPeriod.value === 'Weekly' && reportDate >= new Date(now.getTime() - 7 * 86400000)) ||
      (validReportDate && selectedPeriod.value === 'Monthly' && reportDate.getMonth() === now.getMonth() && reportDate.getFullYear() === now.getFullYear())
    const isArchived = archivedReportIds.value.has(String(report.reportId || report.id))
    const matchesArchiveView = reportView.value === 'archived' ? isArchived : !isArchived

    return (
      matchesSearch &&
      matchesType &&
      matchesStatus &&
      matchesPersonnel &&
      matchesPeriod &&
      matchesArchiveView
    )
  })
})

const activeReportCount = computed(() =>
  new Set(reports.value.filter(report => !archivedReportIds.value.has(String(report.reportId || report.id))).map(report => String(report.reportId || report.id))).size
)

const archivedReportCount = computed(() =>
  new Set(reports.value.filter(report => archivedReportIds.value.has(String(report.reportId || report.id))).map(report => String(report.reportId || report.id))).size
)

const hasFilters = computed(() =>
  searchQuery.value ||
  selectedType.value !== 'All Report Types' ||
  selectedStatus.value !== 'All Status' ||
  selectedPersonnelId.value !== 'All Personnel' ||
  selectedPeriod.value !== 'All Time'
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
  window.dispatchEvent(new CustomEvent(SYNC_EVENT))
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
  selectedPersonnelId.value = 'All Personnel'
  selectedPeriod.value = 'All Time'
}

const printReports = () => window.print()

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

const saveReport = async () => {
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

  const payload = {
    title: reportForm.value.title.trim(),
    report_type: reportForm.value.type,
    description: reportForm.value.description || '',
    deadline: reportForm.value.deadline || '',
    assigned_personnel: assignedPeople.map(person => person.id)
  }

  try {
    if (editingReport.value) {
      await updateReport(editingReport.value.reportId || editingReport.value.id, payload)
      showToast('Report assignment updated successfully.')
    } else {
      payload.assigned_by = props.currentUser?.id || null
      await createReport(payload)
      showToast('Report assigned successfully.')
    }
    await loadReports()
    showReportModal.value = false
    selectedPersonnelIds.value = []
    personnelSearch.value = ''
  } catch (error) {
    console.error('FireNotify: report save failed', error)
    showToast(error.message || 'Unable to save report.', 'error')
  }
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

const submitReview = async () => {
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

  if (!report.submissionId) {
    showToast('This activity has no submission to review.', 'error')
    return
  }

  const nextStatus = {
    approve: 'APPROVED',
    return: 'RETURNED',
    reject: 'REJECTED'
  }[reviewAction.value]
  try {
    await updateReportSubmission(report.submissionId, {
      status: nextStatus,
      review_comment: reviewComment.value.trim(),
      reviewer: props.currentUser?.id || null
    })

    await loadReports()
    showToast({
      approve: 'Report approved successfully.',
      return: 'Report returned for correction.',
      reject: 'Report rejected.'
    }[reviewAction.value])
    showReviewModal.value = false
  } catch (error) {
    console.error('FireNotify: report review failed', error)
    showToast('Unable to save the report review.', 'error')
  }
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

const archiveReport = async report => {
  const userId = props.currentUser?.id
  if (userId === null || userId === undefined) {
    showToast('Unable to identify the current Admin.', 'error')
    return
  }

  const reportId = report.reportId || report.id
  try {
    await setReportArchive(reportId, userId, true)
    archivedReportIds.value = new Set([...archivedReportIds.value, String(reportId)])
    showToast('Report archived for Admin.')
  } catch (error) {
    showToast(error.message || 'Unable to archive report.', 'error')
  }
}

const restoreReport = async report => {
  const userId = props.currentUser?.id
  if (userId === null || userId === undefined) {
    showToast('Unable to identify the current Admin.', 'error')
    return
  }

  const reportId = report.reportId || report.id
  try {
    await setReportArchive(reportId, userId, false)
    const archivedIds = new Set(archivedReportIds.value)
    archivedIds.delete(String(reportId))
    archivedReportIds.value = archivedIds
    showToast('Report restored to Admin active reports.')
  } catch (error) {
    showToast(error.message || 'Unable to restore report.', 'error')
  }
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
  const reportId = targetReport.reportId || targetReport.id

  if (reportView.value === 'active') {
    const userId = props.currentUser?.id
    if (userId === null || userId === undefined) {
      showToast('Unable to identify the current Admin.', 'error')
      return
    }
    try {
      await setReportArchive(reportId, userId, true)
      archivedReportIds.value = new Set([...archivedReportIds.value, String(reportId)])
    } catch (error) {
      showToast(error.message || 'Unable to archive report.', 'error')
      return
    }

    showDeleteModal.value = false
    reportToDelete.value = null
    showToast('Report moved to Admin archive.')
    return
  }

  try {
    await deleteReportFromApi(reportId)
    await loadReports()
  } catch (error) {
    console.error('FireNotify: admin report delete failed', error)
    showToast(error.message || 'Unable to delete report.', 'error')
    return
  }

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
  const targetReport = file?.attachment ? file : selectedReport.value || file
  if (!targetReport) {
    showToast('No attachment available.', 'error')
    return
  }

  if (!targetReport.attachment) {
    showToast('This report has no uploaded file available.', 'error')
    return
  }
  const fileUrl = targetReport.attachment.startsWith('http')
    ? targetReport.attachment
    : `http://127.0.0.1:8000${targetReport.attachment}`
  window.open(fileUrl, '_blank', 'noopener')
}

const downloadAttachment = report => {
  if (!report) return

  if (!report.attachment) {
    showToast('No attachment is available for download.', 'error')
    return
  }
  const fileUrl = report.attachment.startsWith('http')
    ? report.attachment
    : `http://127.0.0.1:8000${report.attachment}`
  const link = document.createElement('a')
  link.href = fileUrl
  link.download = report.filename || 'report-attachment'
  document.body.appendChild(link)
  link.click()
  link.remove()
}

/* =========================================================
   MOUNT
========================================================= */

onMounted(() => {
  loadSavedReportTypes()
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
  <div class="space-y-4">

    <!-- =====================================================
         HEADER
    ====================================================== -->

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
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
            Activity records and personnel submissions from Django.
          </p>
        </div>

        <div class="flex flex-wrap gap-3">
          <button
            @click="openCreateReport"
            class="px-6 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition shadow-sm"
          >
            + Assign Report
          </button>
          <button
            @click="printReports"
            class="px-6 py-3 rounded-xl border border-slate-300 bg-white text-slate-700 font-bold hover:bg-slate-50 transition"
          >
            Print PDF
          </button>
        </div>
      </div>
    </section>

    <!-- =====================================================
         STATISTICS
    ====================================================== -->

    <section
      class="fn-operations-summary fn-operations-summary--five"
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

          <option v-for="type in reportTypes" :key="type" :value="type">
            {{ type }}
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

        <select
          v-model="selectedPersonnelId"
          class="h-12 px-4 rounded-xl border border-slate-300 text-base lg:w-56 focus:ring-2 focus:ring-[#8B1E23] outline-none"
        >
          <option value="All Personnel">All Personnel</option>
          <option v-for="person in personnel" :key="person.id" :value="person.id">
            {{ person.name || `${person.firstName || ''} ${person.lastName || ''}`.trim() || person.username }}
          </option>
        </select>

        <select
          v-model="selectedPeriod"
          class="h-12 px-4 rounded-xl border border-slate-300 text-base lg:w-40 focus:ring-2 focus:ring-[#8B1E23] outline-none"
        >
          <option>All Time</option>
          <option>Weekly</option>
          <option>Monthly</option>
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
        class="fn-operations-heading"
      >
        <div>
          <h2
            class="text-base font-bold text-slate-900"
          >
            Assigned Reports
          </h2>

          <p
            class="text-sm text-slate-500 mt-1"
          >
            {{ filteredReports.length }} {{ filteredReports.length === 1 ? 'report' : 'reports' }} displayed
          </p>
        </div>

        <div class="text-xs font-semibold text-slate-600">
          {{ submittedCount }} submitted
        </div>
      </div>

      <div class="flex gap-2 border-b border-slate-200 px-5 pt-4">
        <button type="button" @click="reportView = 'active'" class="border-b-2 px-4 py-3 text-sm font-bold" :class="reportView === 'active' ? 'border-[#8B1E23] text-[#8B1E23]' : 'border-transparent text-slate-500'">
          Active Reports <span class="ml-1 text-xs">{{ activeReportCount }}</span>
        </button>
        <button type="button" @click="reportView = 'archived'" class="border-b-2 px-4 py-3 text-sm font-bold" :class="reportView === 'archived' ? 'border-[#8B1E23] text-[#8B1E23]' : 'border-transparent text-slate-500'">
          Archived Reports <span class="ml-1 text-xs">{{ archivedReportCount }}</span>
        </button>
      </div>

      <div class="fn-operations-table-wrap">
        <table class="fn-operations-table">
          <thead>
            <tr><th>Report</th><th>Assigned Personnel</th><th>Deadline</th><th>Status</th><th>Submission</th><th class="text-right">Actions</th></tr>
          </thead>
          <tbody>
            <tr v-for="report in filteredReports" :key="report.rowId">
              <td data-label="Report" class="min-w-0">
                <div class="flex min-w-0 flex-col gap-1.5 whitespace-normal">
                  <p class="break-words text-sm font-semibold leading-5 text-slate-900">{{ report.title }}</p>
                  <p class="break-words text-xs leading-5 text-slate-600"><span class="font-semibold">Report Type:</span> {{ report.type || 'Report' }}</p>
                  <p v-if="report.location" class="break-words text-xs leading-5 text-slate-600"><span class="font-semibold">Location:</span> {{ report.location }}</p>
                  <p v-if="report.description" class="break-words whitespace-pre-wrap text-xs leading-5 text-slate-600"><span class="font-semibold">Description/Details:</span> {{ report.description }}</p>
                  <p v-if="report.accomplishment" class="break-words whitespace-pre-wrap text-xs leading-5 text-slate-600"><span class="font-semibold">Submission:</span> {{ report.accomplishment }}</p>
                  <p v-if="report.reviewComment" class="break-words whitespace-pre-wrap text-xs leading-5 text-amber-800"><span class="font-semibold">Review/Remarks:</span> {{ report.reviewComment }}</p>
                </div>
              </td>
              <td data-label="Assigned Personnel"><span class="block min-w-0 break-words leading-5">{{ report.assignedPersonnel?.length ? report.assignedPersonnel.map(person => person.name).join(', ') : 'No personnel assigned' }}</span></td>
              <td data-label="Deadline">
                <div class="flex flex-col gap-0.5">
                  <span class="leading-5">{{ formatOperationDate(report.deadline) }}</span>
                  <span v-if="hasTimeValue(report.deadline)" class="text-xs leading-5 text-slate-500">{{ formatOperationTime(report.deadline) }}</span>
                </div>
              </td>
              <td data-label="Status"><span class="fn-operations-badge" :class="getStatusClass(report.status)">{{ report.status }}</span></td>
              <td data-label="Submission">
                <div class="flex flex-col gap-0.5">
                  <span class="leading-5">{{ report.submittedDate ? formatOperationDate(report.submittedDate) : 'Not submitted' }}</span>
                  <span v-if="hasTimeValue(report.submittedDate)" class="text-xs leading-5 text-slate-500">{{ formatOperationTime(report.submittedDate) }}</span>
                </div>
              </td>
              <td data-label="Actions">
                <div class="flex flex-wrap gap-1.5 sm:justify-end">
                  <template v-if="reportView === 'archived'">
                    <button @click="viewReport(report)" class="fn-operations-action">View Report</button>
                    <button v-if="report.isPrimaryAssignment" @click="restoreReport(report)" class="fn-operations-action">Restore</button>
                    <button v-if="report.isPrimaryAssignment" @click="openDeleteReport(report)" class="fn-operations-action fn-operations-action--danger">Delete Permanently</button>
                  </template>
                  <template v-else>
                    <button @click="viewReport(report)" class="fn-operations-action">View Report</button>
                    <button v-if="report.isPrimaryAssignment" @click="archiveReport(report)" class="fn-operations-action">Archive</button>
                    <button v-if="report.isPrimaryAssignment" @click="openDeleteReport(report)" class="fn-operations-action fn-operations-action--danger">Delete</button>
                  </template>
                </div>
              </td>
            </tr>
            <tr v-if="!filteredReports.length">
              <td colspan="6" class="py-10 text-center">
                <p class="font-bold text-slate-700">No reports found</p>
                <p class="mt-1 text-sm text-slate-500">Try changing your search or filters.</p>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

    </section>

   


    <!-- =====================================================
         CREATE / EDIT REPORT MODAL
    ====================================================== -->

    <div
      v-if="showReportModal"
      class="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-sm flex items-center justify-center p-4"
    >

      <div
        class="fn-modal-panel w-full max-w-3xl bg-white rounded-2xl shadow-2xl overflow-hidden"
      >

        <div
          class="fn-modal-header bg-[#8B1E23] p-6 text-white"
        >

          <div class="flex items-start justify-between gap-4">
            <div>
              <p class="fn-modal-header-label text-xs uppercase tracking-wider font-bold text-white/70">
                Report Details
              </p>

              <h3 class="text-2xl font-bold mt-1 text-white">
                {{ editingReport ? 'Edit Report Assignment' : 'Assign Report to Personnel' }}
              </h3>

              <p class="fn-modal-header-description text-sm text-white/80 mt-1">
                Create a report and assign it directly to registered personnel.
              </p>
            </div>

            <button
              type="button"
              @click="showReportModal = false"
              class="h-9 w-9 rounded-lg bg-white/10 hover:bg-white/20 text-white"
              aria-label="Close report form"
            >
              ✕
            </button>
          </div>
        </div>

        <div
          class="p-6 space-y-5 max-h-[70vh] overflow-y-auto"
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
                <option v-for="type in reportTypes" :key="type" :value="type">
                  {{ type }}
                </option>

              </select>

              <button
                v-if="!showNewReportType"
                type="button"
                @click="showNewReportType = true"
                class="mt-2 text-sm font-bold text-[#8B1E23] hover:underline"
              >
                + Create New Report Type
              </button>

              <div v-else class="mt-3 flex flex-wrap items-center gap-2">
                <input
                  v-model="newReportTypeName"
                  type="text"
                  placeholder="New Report Type"
                  class="min-w-0 flex-1 h-10 px-3 rounded-lg border border-slate-300"
                  @keyup.enter="createReportType"
                />
                <button type="button" @click="createReportType" class="px-3 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-bold">
                  Create Type
                </button>
                <button type="button" @click="showNewReportType = false; newReportTypeName = ''" class="px-3 py-2 rounded-lg border border-slate-300 text-sm font-semibold">
                  Cancel
                </button>
              </div>

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
          class="px-6 py-5 bg-slate-50 border-t border-slate-200 flex justify-end gap-3"
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

            <h3
              class="mt-1 break-words text-xl font-bold leading-6 text-slate-900"
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
                  selectedReport.deadline ? formatOperationDate(selectedReport.deadline) : 'No deadline'
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

              <p class="mt-1 flex flex-col gap-0.5 font-bold leading-5 text-slate-900">
                <span>{{ selectedReport.submittedDate ? formatOperationDate(selectedReport.submittedDate) : 'Pending' }}</span>
                <span v-if="hasTimeValue(selectedReport.submittedDate)" class="text-xs font-normal text-slate-500">{{ formatOperationTime(selectedReport.submittedDate) }}</span>
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

              <p class="mt-1 flex flex-col gap-0.5 font-bold leading-5 text-slate-900">
                <span>{{ selectedReport.submittedAt ? formatOperationDate(selectedReport.submittedAt) : 'Not submitted' }}</span>
                <span v-if="hasTimeValue(selectedReport.submittedAt)" class="text-xs font-normal text-slate-500">{{ formatOperationTime(selectedReport.submittedAt) }}</span>
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
              class="mt-2 break-words whitespace-pre-wrap text-sm leading-6 text-slate-600"
            >
              {{
                selectedReport.description ||
                'No instructions provided.'
              }}
            </p>

          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-500">Accomplishment</p>
              <p class="mt-2 break-words whitespace-pre-wrap text-sm leading-6 text-slate-700">{{ selectedReport.accomplishment || 'No submission yet.' }}</p>
            </div>
            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-500">Remarks</p>
              <p class="mt-2 break-words whitespace-pre-wrap text-sm leading-6 text-slate-700">{{ selectedReport.remarks || 'No remarks.' }}</p>
            </div>
            <div v-if="selectedReport.revisionNote" class="p-4 rounded-xl bg-amber-50 border border-amber-100 md:col-span-2">
              <p class="text-xs font-bold text-amber-700">Revision Information</p>
              <p class="mt-2 break-words whitespace-pre-wrap text-sm leading-6 text-slate-700">{{ selectedReport.revisionNote }}</p>
            </div>
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
              class="mt-2 break-words whitespace-pre-wrap text-sm leading-6 text-slate-700"
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
              class="mt-2 break-words whitespace-pre-wrap text-sm leading-6 text-slate-700"
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
            v-if="['Submitted', 'For Review'].includes(selectedReport.status)"
            @click="showDetailsModal = false; openReview(selectedReport, 'return')"
            class="px-5 py-2.5 rounded-xl bg-amber-600 text-white font-bold"
          >
            Return
          </button>

          <button
            v-if="['Submitted', 'For Review'].includes(selectedReport.status)"
            @click="showDetailsModal = false; openReview(selectedReport, 'reject')"
            class="px-5 py-2.5 rounded-xl bg-red-600 text-white font-bold"
          >
            Reject
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
          {{ reportView === 'active' ? 'Move Report to Archive?' : 'Delete Report Permanently?' }}
        </h3>

        <p class="text-sm text-slate-500 mt-2">
          <template v-if="reportView === 'active'">
            Move <strong>{{ reportToDelete.title }}</strong> to Admin Archived Reports? You can restore it later.
          </template>
          <template v-else>
            Permanently delete <strong>{{ reportToDelete.title }}</strong> and its submission records and attachments? This cannot be undone.
          </template>
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
            {{ reportView === 'active' ? 'Move to Archive' : 'Delete Permanently' }}
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
