<script setup>
import { ref, computed, onMounted } from 'vue'

defineProps({
  currentUser: {
    type: Object,
    required: false,
    default: null
  }
})

const STORAGE_KEY = 'fireNotifyDocumentPipeline'

const documents = ref([])

const searchQuery = ref('')
const stageFilter = ref('All Stages')

const showDocumentModal = ref(false)
const showDetailsModal = ref(false)
const showDeleteModal = ref(false)

const selectedDocument = ref(null)

const isEditing = ref(false)

const toastMessage = ref('')
const showToast = ref(false)

const documentForm = ref({
  name: '',
  submittedBy: '',
  date: '',
  stage: 'Submitted',
  description: '',
  fileName: ''
})

/* =========================================================
   DEFAULT DOCUMENTS
========================================================= */

const defaultDocuments = [
  {
    id: 'DOC-001',
    name: 'After-Operation Fire Incident Report',
    submittedBy: 'SFO1 M. Santos',
    date: '2026-08-12',
    stage: 'Approved',
    description: 'After-operation report submitted for administrative review and archival.',
    fileName: 'FireIncidentReport_Aug12.pdf'
  },
  {
    id: 'DOC-002',
    name: 'Quarterly Establishment Inspection',
    submittedBy: 'FO3 J. Dela Cruz',
    date: '2026-08-15',
    stage: 'Revision',
    description: 'Inspection report requires updated attachments before final approval.',
    fileName: 'QuarterlyInspection_Aug15.pdf'
  },
  {
    id: 'DOC-003',
    name: 'Barangay Drill Attendance Sheet',
    submittedBy: 'SFO2 R. Garcia',
    date: '2026-08-18',
    stage: 'In Review',
    description: 'Attendance sheet is currently being evaluated by the administrative office.',
    fileName: 'BarangayDrillAttendance.xlsx'
  },
  {
    id: 'DOC-004',
    name: 'Weekly Accomplishment Report',
    submittedBy: 'FO2 M. Santos',
    date: '2026-09-08',
    stage: 'Submitted',
    description: 'Weekly accomplishment report waiting for administrative review.',
    fileName: 'WeeklyAccomplishment_Sept8.pdf'
  },
  {
    id: 'DOC-005',
    name: 'Equipment Inspection Report',
    submittedBy: 'FO2 A. Villanueva',
    date: '2026-09-10',
    stage: 'Revision',
    description: 'Equipment inspection document returned for additional supporting evidence.',
    fileName: 'EquipmentInspection.pdf'
  },
  {
    id: 'DOC-006',
    name: 'Monthly Compliance Report',
    submittedBy: 'Station Administration',
    date: '2026-09-19',
    stage: 'Submitted',
    description: 'Monthly compliance report prepared for station-level submission.',
    fileName: 'MonthlyComplianceReport.pdf'
  }
]

/* =========================================================
   LOAD / SAVE
========================================================= */

const loadDocuments = () => {
  const saved = localStorage.getItem(STORAGE_KEY)

  if (saved) {
    try {
      documents.value = JSON.parse(saved)
      return
    } catch (error) {
      console.error('Failed to load document pipeline:', error)
    }
  }

  documents.value = defaultDocuments
  saveDocuments()
}

const saveDocuments = () => {
  localStorage.setItem(
    STORAGE_KEY,
    JSON.stringify(documents.value)
  )
}

onMounted(() => {
  loadDocuments()
})

/* =========================================================
   COMPUTED STATS
========================================================= */

const totalDocuments = computed(() =>
  documents.value.length
)

const submittedCount = computed(() =>
  documents.value.filter(
    document => document.stage === 'Submitted'
  ).length
)

const inReviewCount = computed(() =>
  documents.value.filter(
    document => document.stage === 'In Review'
  ).length
)

const approvedCount = computed(() =>
  documents.value.filter(
    document => document.stage === 'Approved'
  ).length
)

const revisionCount = computed(() =>
  documents.value.filter(
    document => document.stage === 'Revision'
  ).length
)

const needsActionCount = computed(() =>
  documents.value.filter(
    document =>
      document.stage === 'Revision' ||
      document.stage === 'Submitted'
  ).length
)

const archivedCount = computed(() =>
  documents.value.filter(
    document => document.stage === 'Approved'
  ).length
)

/* =========================================================
   FILTERED DOCUMENTS
========================================================= */

const filteredDocuments = computed(() => {
  const query = searchQuery.value
    .toLowerCase()
    .trim()

  return documents.value
    .filter(document => {
      const matchesSearch =
        !query ||
        document.name.toLowerCase().includes(query) ||
        document.submittedBy.toLowerCase().includes(query) ||
        document.id.toLowerCase().includes(query)

      const matchesStage =
        stageFilter.value === 'All Stages' ||
        document.stage === stageFilter.value

      return matchesSearch && matchesStage
    })
    .sort(
      (a, b) =>
        new Date(b.date) - new Date(a.date)
    )
})

/* =========================================================
   RECENT ACTIVITY
========================================================= */

const recentActivities = computed(() => {
  return [...documents.value]
    .sort(
      (a, b) =>
        new Date(b.date) - new Date(a.date)
    )
    .slice(0, 3)
})

/* =========================================================
   MODALS
========================================================= */

const openNewDocument = () => {
  selectedDocument.value = null
  isEditing.value = false

  documentForm.value = {
    name: '',
    submittedBy: '',
    date: new Date().toISOString().split('T')[0],
    stage: 'Submitted',
    description: '',
    fileName: ''
  }

  showDocumentModal.value = true
}

const openEditDocument = document => {
  selectedDocument.value = document
  isEditing.value = true

  documentForm.value = {
    name: document.name,
    submittedBy: document.submittedBy,
    date: document.date,
    stage: document.stage,
    description: document.description,
    fileName: document.fileName
  }

  showDocumentModal.value = true
}

const openDetails = document => {
  selectedDocument.value = document
  showDetailsModal.value = true
}

const confirmDelete = document => {
  selectedDocument.value = document
  showDeleteModal.value = true
}

/* =========================================================
   SAVE DOCUMENT
========================================================= */

const saveDocument = () => {
  if (
    !documentForm.value.name.trim() ||
    !documentForm.value.submittedBy.trim()
  ) {
    showNotification(
      'Document name and submitter are required.'
    )
    return
  }

  if (isEditing.value && selectedDocument.value) {
    const index = documents.value.findIndex(
      document =>
        document.id === selectedDocument.value.id
    )

    if (index !== -1) {
      documents.value[index] = {
        ...documents.value[index],
        ...documentForm.value
      }
    }

    showNotification('Document updated successfully.')
  } else {
    const newDocument = {
      id: `DOC-${String(
        documents.value.length + 1
      ).padStart(3, '0')}`,
      ...documentForm.value
    }

    documents.value.unshift(newDocument)

    showNotification('New document added.')
  }

  saveDocuments()

  showDocumentModal.value = false
}

/* =========================================================
   DELETE
========================================================= */

const deleteDocument = () => {
  if (!selectedDocument.value) return

  documents.value = documents.value.filter(
    document =>
      document.id !== selectedDocument.value.id
  )

  saveDocuments()

  showDeleteModal.value = false
  selectedDocument.value = null

  showNotification('Document deleted.')
}

/* =========================================================
   STAGE ACTIONS
========================================================= */

const updateStage = (document, stage) => {
  const item = documents.value.find(
    record => record.id === document.id
  )

  if (!item) return

  item.stage = stage

  saveDocuments()

  showNotification(
    `${document.name} moved to ${stage}.`
  )
}

const approveDocument = document => {
  updateStage(document, 'Approved')
}

const requestRevision = document => {
  updateStage(document, 'Revision')
}

const startReview = document => {
  updateStage(document, 'In Review')
}

/* =========================================================
   FILTERS
========================================================= */

const clearFilters = () => {
  searchQuery.value = ''
  stageFilter.value = 'All Stages'
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

const formatDate = date => {
  if (!date) return '—'

  return new Date(
    `${date}T00:00:00`
  ).toLocaleDateString(
    'en-US',
    {
      month: 'short',
      day: 'numeric',
      year: 'numeric'
    }
  )
}

const stageClass = stage => {
  if (stage === 'Approved') {
    return 'bg-green-100 text-green-700'
  }

  if (stage === 'In Review') {
    return 'bg-blue-100 text-blue-700'
  }

  if (stage === 'Revision') {
    return 'bg-yellow-100 text-yellow-700'
  }

  return 'bg-slate-100 text-slate-700'
}

const activityClass = stage => {
  if (stage === 'Approved') {
    return 'border-emerald-200 bg-emerald-50'
  }

  if (stage === 'Revision') {
    return 'border-blue-200 bg-blue-50'
  }

  return 'border-amber-200 bg-amber-50'
}

const activityTitle = stage => {
  if (stage === 'Approved') return 'Document Approved'
  if (stage === 'Revision') return 'Revision Requested'
  if (stage === 'In Review') return 'Document Under Review'

  return 'Document Submitted'
}
</script>

<template>
  <div class="space-y-6">

    <!-- =====================================================
         TOAST
    ====================================================== -->

    <transition name="fade">
      <div
        v-if="showToast"
        class="fixed top-6 right-6 z-[100] bg-slate-900 text-white px-5 py-3 rounded-xl shadow-xl text-sm font-semibold"
      >
        {{ toastMessage }}
      </div>
    </transition>

    <!-- =====================================================
         HEADER
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div
        class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4"
      >

        <div>

          <p
            class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]"
          >
            Document Flow
          </p>

          <h2
            class="text-2xl font-bold text-slate-900 mt-1"
          >
            Document Pipeline
          </h2>

          <p class="text-base text-slate-500 mt-1">
            Track paperwork from submission to approval,
            archiving, and retrieval.
          </p>

        </div>

        <button
          @click="openNewDocument"
          class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition"
        >
          + New Document
        </button>

      </div>
    </section>

    <!-- =====================================================
         STATS
    ====================================================== -->

    <section
      class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5"
    >

      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-3xl font-bold text-[#8B1E23]">
          {{ totalDocuments }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Total Docs
        </p>
      </div>

      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-3xl font-bold text-blue-600">
          {{ inReviewCount }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          In Review
        </p>
      </div>

      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-3xl font-bold text-green-600">
          {{ approvedCount }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Approved
        </p>
      </div>

      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-3xl font-bold text-yellow-600">
          {{ needsActionCount }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Needs Action
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
          placeholder="Search document, submitter, or ID..."
          class="flex-1 px-4 py-3 border border-slate-200 rounded-xl outline-none focus:border-[#8B1E23]"
        />

        <select
          v-model="stageFilter"
          class="px-4 py-3 border border-slate-200 rounded-xl bg-white"
        >
          <option>All Stages</option>
          <option>Submitted</option>
          <option>In Review</option>
          <option>Approved</option>
          <option>Revision</option>
        </select>

        <button
          @click="clearFilters"
          class="px-5 py-3 rounded-xl border border-slate-200 font-bold text-slate-700 hover:bg-slate-50"
        >
          Clear
        </button>

      </div>

    </section>

    <!-- =====================================================
         PIPELINE + RECENT ACTIVITY
    ====================================================== -->

    <section
      class="grid grid-cols-1 xl:grid-cols-2 gap-6"
    >

      <!-- PIPELINE STAGES -->

      <div
        class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
      >

        <div
          class="flex items-center justify-between border-b border-slate-200 pb-5"
        >

          <div>

            <h2
              class="text-xl font-bold text-slate-900"
            >
              Pipeline Stages
            </h2>

            <p
              class="text-sm text-slate-500 mt-1"
            >
              Current volume across document states
            </p>

          </div>

          <span
            class="text-xs font-bold text-slate-500"
          >
            {{ totalDocuments }} Documents
          </span>

        </div>

        <div class="mt-5 space-y-4">

          <div
            class="p-4 rounded-xl border border-slate-200 bg-slate-50"
          >

            <div
              class="flex justify-between items-center"
            >

              <div>

                <p
                  class="text-sm font-bold text-slate-900"
                >
                  Submitted
                </p>

                <p
                  class="text-xs text-slate-500 mt-1"
                >
                  Ready for administrative review
                </p>

              </div>

              <span
                class="text-sm font-bold text-slate-700"
              >
                {{ submittedCount }}
              </span>

            </div>

          </div>

          <div
            class="p-4 rounded-xl border border-blue-200 bg-blue-50"
          >

            <div
              class="flex justify-between items-center"
            >

              <div>

                <p
                  class="text-sm font-bold text-slate-900"
                >
                  In Review
                </p>

                <p
                  class="text-xs text-slate-500 mt-1"
                >
                  Evaluated by the admin office
                </p>

              </div>

              <span
                class="text-sm font-bold text-blue-600"
              >
                {{ inReviewCount }}
              </span>

            </div>

          </div>

          <div
            class="p-4 rounded-xl border border-green-200 bg-green-50"
          >

            <div
              class="flex justify-between items-center"
            >

              <div>

                <p
                  class="text-sm font-bold text-slate-900"
                >
                  Approved
                </p>

                <p
                  class="text-xs text-slate-500 mt-1"
                >
                  Archived and available for retrieval
                </p>

              </div>

              <span
                class="text-sm font-bold text-green-600"
              >
                {{ approvedCount }}
              </span>

            </div>

          </div>

          <div
            class="p-4 rounded-xl border border-yellow-200 bg-yellow-50"
          >

            <div
              class="flex justify-between items-center"
            >

              <div>

                <p
                  class="text-sm font-bold text-slate-900"
                >
                  Revision
                </p>

                <p
                  class="text-xs text-slate-500 mt-1"
                >
                  Requires correction or additional documents
                </p>

              </div>

              <span
                class="text-sm font-bold text-yellow-600"
              >
                {{ revisionCount }}
              </span>

            </div>

          </div>

        </div>
      </div>

      <!-- RECENT ACTIVITY -->

      <div
        class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
      >

        <div
          class="flex items-center justify-between border-b border-slate-200 pb-5"
        >

          <div>

            <h2
              class="text-xl font-bold text-slate-900"
            >
              Recent Activity
            </h2>

            <p
              class="text-sm text-slate-500 mt-1"
            >
              Latest updates in the document pipeline
            </p>

          </div>

        </div>

        <div class="mt-5 space-y-4">

          <div
            v-for="document in recentActivities"
            :key="document.id"
            class="p-4 rounded-xl border"
            :class="activityClass(document.stage)"
          >

            <div
              class="flex justify-between gap-3"
            >

              <div>

                <p
                  class="text-sm font-bold text-slate-900"
                >
                  {{ activityTitle(document.stage) }}
                </p>

                <p
                  class="text-sm text-slate-600 mt-1"
                >
                  {{ document.name }}
                </p>

                <p
                  class="text-xs text-slate-400 mt-2"
                >
                  {{ formatDate(document.date) }}
                </p>

              </div>

              <span
                class="h-fit px-2.5 py-1 rounded-full text-xs font-bold"
                :class="stageClass(document.stage)"
              >
                {{ document.stage }}
              </span>

            </div>

          </div>

        </div>
      </div>

    </section>

    <!-- =====================================================
         DOCUMENT QUEUE
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
            Document Queue
          </h2>

          <p
            class="text-sm text-slate-500 mt-1"
          >
            Pending and recently updated documents
          </p>

        </div>

        <span
          class="text-xs font-bold text-slate-500"
        >
          Showing {{ filteredDocuments.length }} documents
        </span>

      </div>

      <div
        class="mt-5 overflow-x-auto"
      >

        <table
          class="min-w-full border-separate border-spacing-y-3"
        >

          <thead>

            <tr
              class="text-left text-xs font-bold uppercase tracking-wide text-slate-500"
            >

              <th class="pb-2 pr-4">
                Document
              </th>

              <th class="pb-2 pr-4">
                Submitted By
              </th>

              <th class="pb-2 pr-4">
                Date
              </th>

              <th class="pb-2 pr-4">
                Stage
              </th>

              <th class="pb-2 text-right">
                Actions
              </th>

            </tr>

          </thead>

          <tbody>

            <tr
              v-for="document in filteredDocuments"
              :key="document.id"
              class="bg-slate-50"
            >

              <td
                class="py-4 pr-4 rounded-l-xl"
              >

                <p
                  class="font-semibold text-slate-900"
                >
                  {{ document.name }}
                </p>

                <p
                  class="text-xs text-slate-400 mt-1"
                >
                  {{ document.id }}
                </p>

              </td>

              <td
                class="py-4 pr-4 text-slate-600"
              >
                {{ document.submittedBy }}
              </td>

              <td
                class="py-4 pr-4 text-slate-600"
              >
                {{ formatDate(document.date) }}
              </td>

              <td
                class="py-4 pr-4"
              >

                <span
                  class="px-3 py-1 rounded-full text-xs font-bold"
                  :class="stageClass(document.stage)"
                >
                  {{ document.stage }}
                </span>

              </td>

              <td
                class="py-4 pr-4 rounded-r-xl"
              >

                <div
                  class="flex justify-end gap-2"
                >

                  <button
                    @click="openDetails(document)"
                    class="px-3 py-2 rounded-lg bg-white border border-slate-200 text-xs font-bold text-slate-700 hover:bg-slate-100"
                  >
                    View
                  </button>

                  <button
                    @click="openEditDocument(document)"
                    class="px-3 py-2 rounded-lg bg-blue-50 text-blue-700 text-xs font-bold hover:bg-blue-100"
                  >
                    Edit
                  </button>

                  <button
                    @click="confirmDelete(document)"
                    class="px-3 py-2 rounded-lg bg-red-50 text-red-700 text-xs font-bold hover:bg-red-100"
                  >
                    Delete
                  </button>

                </div>

              </td>

            </tr>

          </tbody>

        </table>

        <div
          v-if="filteredDocuments.length === 0"
          class="py-12 text-center"
        >

          <p class="text-3xl">
            📄
          </p>

          <p
            class="font-bold text-slate-700 mt-2"
          >
            No documents found
          </p>

          <p
            class="text-sm text-slate-400 mt-1"
          >
            Try changing your search or filter.
          </p>

        </div>

      </div>

    </section>

    <!-- =====================================================
         NEW / EDIT DOCUMENT MODAL
    ====================================================== -->

    <div
      v-if="showDocumentModal"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div
        class="bg-white rounded-2xl shadow-2xl w-full max-w-xl max-h-[90vh] overflow-y-auto"
      >

        <div
          class="p-6 border-b border-slate-200 flex justify-between"
        >

          <div>

            <h2
              class="text-xl font-bold text-slate-900"
            >
              {{
                isEditing
                  ? 'Edit Document'
                  : 'New Document'
              }}
            </h2>

            <p
              class="text-sm text-slate-500 mt-1"
            >
              Manage document pipeline information.
            </p>

          </div>

          <button
            @click="showDocumentModal = false"
            class="text-2xl text-slate-400 hover:text-slate-700"
          >
            ×
          </button>

        </div>

        <div class="p-6 space-y-5">

          <div>

            <label
              class="block text-sm font-bold text-slate-700 mb-2"
            >
              Document Name
            </label>

            <input
              v-model="documentForm.name"
              type="text"
              placeholder="Enter document name"
              class="w-full px-4 py-3 border border-slate-200 rounded-xl outline-none focus:border-[#8B1E23]"
            />

          </div>

          <div>

            <label
              class="block text-sm font-bold text-slate-700 mb-2"
            >
              Submitted By
            </label>

            <input
              v-model="documentForm.submittedBy"
              type="text"
              placeholder="e.g. FO3 J. Dela Cruz"
              class="w-full px-4 py-3 border border-slate-200 rounded-xl outline-none focus:border-[#8B1E23]"
            />

          </div>

          <div
            class="grid grid-cols-1 sm:grid-cols-2 gap-4"
          >

            <div>

              <label
                class="block text-sm font-bold text-slate-700 mb-2"
              >
                Date
              </label>

              <input
                v-model="documentForm.date"
                type="date"
                class="w-full px-4 py-3 border border-slate-200 rounded-xl"
              />

            </div>

            <div>

              <label
                class="block text-sm font-bold text-slate-700 mb-2"
              >
                Stage
              </label>

              <select
                v-model="documentForm.stage"
                class="w-full px-4 py-3 border border-slate-200 rounded-xl bg-white"
              >
                <option>Submitted</option>
                <option>In Review</option>
                <option>Approved</option>
                <option>Revision</option>
              </select>

            </div>

          </div>

          <div>

            <label
              class="block text-sm font-bold text-slate-700 mb-2"
            >
              File Name
            </label>

            <input
              v-model="documentForm.fileName"
              type="text"
              placeholder="e.g. MonthlyReport.pdf"
              class="w-full px-4 py-3 border border-slate-200 rounded-xl"
            />

          </div>

          <div>

            <label
              class="block text-sm font-bold text-slate-700 mb-2"
            >
              Description
            </label>

            <textarea
              v-model="documentForm.description"
              rows="4"
              placeholder="Document description..."
              class="w-full px-4 py-3 border border-slate-200 rounded-xl resize-none"
            ></textarea>

          </div>

        </div>

        <div
          class="p-6 border-t border-slate-200 flex justify-end gap-3"
        >

          <button
            @click="showDocumentModal = false"
            class="px-5 py-3 rounded-xl border border-slate-200 font-bold text-slate-700"
          >
            Cancel
          </button>

          <button
            @click="saveDocument"
            class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D]"
          >
            {{
              isEditing
                ? 'Save Changes'
                : 'Add Document'
            }}
          </button>

        </div>

      </div>
    </div>

    <!-- =====================================================
         DETAILS MODAL
    ====================================================== -->

    <div
      v-if="showDetailsModal && selectedDocument"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div
        class="bg-white rounded-2xl shadow-2xl w-full max-w-lg"
      >

        <div
          class="p-6 border-b border-slate-200 flex justify-between"
        >

          <div>

            <p
              class="text-xs font-bold text-[#8B1E23]"
            >
              {{ selectedDocument.id }}
            </p>

            <h2
              class="text-xl font-bold text-slate-900 mt-1"
            >
              {{ selectedDocument.name }}
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

          <div
            class="flex justify-between items-center"
          >

            <span
              class="px-3 py-1 rounded-full text-xs font-bold"
              :class="stageClass(selectedDocument.stage)"
            >
              {{ selectedDocument.stage }}
            </span>

            <span
              class="text-sm text-slate-500"
            >
              {{ formatDate(selectedDocument.date) }}
            </span>

          </div>

          <div>

            <p
              class="text-xs uppercase font-bold text-slate-400"
            >
              Submitted By
            </p>

            <p
              class="font-semibold text-slate-800 mt-1"
            >
              {{ selectedDocument.submittedBy }}
            </p>

          </div>

          <div>

            <p
              class="text-xs uppercase font-bold text-slate-400"
            >
              File
            </p>

            <p
              class="font-semibold text-slate-800 mt-1"
            >
              {{ selectedDocument.fileName || 'No file attached' }}
            </p>

          </div>

          <div>

            <p
              class="text-xs uppercase font-bold text-slate-400"
            >
              Description
            </p>

            <p
              class="text-sm text-slate-600 mt-1"
            >
              {{ selectedDocument.description || 'No description provided.' }}
            </p>

          </div>

          <div
            v-if="selectedDocument.stage !== 'Approved'"
            class="pt-4 border-t border-slate-200"
          >

            <p
              class="text-sm font-bold text-slate-700 mb-3"
            >
              Quick Stage Action
            </p>

            <div class="flex flex-wrap gap-2">

              <button
                v-if="selectedDocument.stage === 'Submitted'"
                @click="startReview(selectedDocument)"
                class="px-3 py-2 rounded-lg bg-blue-50 text-blue-700 text-xs font-bold"
              >
                Start Review
              </button>

              <button
                v-if="selectedDocument.stage !== 'Approved'"
                @click="approveDocument(selectedDocument)"
                class="px-3 py-2 rounded-lg bg-green-50 text-green-700 text-xs font-bold"
              >
                Approve
              </button>

              <button
                v-if="selectedDocument.stage !== 'Revision'"
                @click="requestRevision(selectedDocument)"
                class="px-3 py-2 rounded-lg bg-yellow-50 text-yellow-700 text-xs font-bold"
              >
                Request Revision
              </button>

            </div>

          </div>

        </div>

        <div
          class="p-6 border-t border-slate-200 flex justify-end"
        >

          <button
            @click="showDetailsModal = false"
            class="px-5 py-3 rounded-xl bg-slate-100 font-bold text-slate-700"
          >
            Close
          </button>

        </div>

      </div>
    </div>

    <!-- =====================================================
         DELETE MODAL
    ====================================================== -->

    <div
      v-if="showDeleteModal && selectedDocument"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div
        class="bg-white rounded-2xl shadow-2xl w-full max-w-md p-6"
      >

        <div
          class="w-12 h-12 rounded-full bg-red-100 text-red-600 flex items-center justify-center text-xl"
        >
          !
        </div>

        <h2
          class="text-xl font-bold text-slate-900 mt-4"
        >
          Delete Document?
        </h2>

        <p
          class="text-sm text-slate-500 mt-2"
        >
          Are you sure you want to delete
          <strong>{{ selectedDocument.name }}</strong>?
          This action cannot be undone.
        </p>

        <div
          class="flex justify-end gap-3 mt-6"
        >

          <button
            @click="showDeleteModal = false"
            class="px-5 py-3 rounded-xl border border-slate-200 font-bold text-slate-700"
          >
            Cancel
          </button>

          <button
            @click="deleteDocument"
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