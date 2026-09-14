<script setup>
import { ref, computed, onMounted } from 'vue'

defineProps({
  currentUser: {
    type: Object,
    required: false,
    default: null
  }
})

const STORAGE_KEY = 'fireNotifyPdfExports'

const selectedTemplate = ref(null)
const selectedFormat = ref('Standard PDF')

const showExportModal = ref(false)
const showDetailsModal = ref(false)

const searchQuery = ref('')
const statusFilter = ref('All Status')

const toastMessage = ref('')
const showToast = ref(false)

const exportForm = ref({
  title: '',
  template: '',
  format: 'Standard PDF',
  dateFrom: '',
  dateTo: '',
  includeSummary: true,
  includeDetails: true,
  includeSignature: true
})

/* =========================================================
   EXPORT TEMPLATES
========================================================= */

const templates = [
  {
    id: 'TPL-001',
    name: 'Incident Summary Report',
    description: 'Standard BFP incident summary layout',
    category: 'Operations',
    pages: '2–4 pages'
  },
  {
    id: 'TPL-002',
    name: 'Personnel Roster',
    description: 'Structured staff roster for station operations',
    category: 'Personnel',
    pages: '1–2 pages'
  },
  {
    id: 'TPL-003',
    name: 'Compliance Audit Pack',
    description: 'Detailed compliance and escalation results',
    category: 'Compliance',
    pages: '4–8 pages'
  },
  {
    id: 'TPL-004',
    name: 'Station Duty Log',
    description: 'Daily and monthly station duty records',
    category: 'Operations',
    pages: '2–5 pages'
  },
  {
    id: 'TPL-005',
    name: 'Equipment Audit Report',
    description: 'Equipment condition and inspection summary',
    category: 'Equipment',
    pages: '2–4 pages'
  },
  {
    id: 'TPL-006',
    name: 'Weekly Compliance Summary',
    description: 'Weekly operational compliance overview',
    category: 'Compliance',
    pages: '3–5 pages'
  }
]

/* =========================================================
   DEFAULT EXPORT HISTORY
========================================================= */

const defaultExports = [
  {
    id: 'EXP-001',
    title: 'Weekly Compliance Summary',
    template: 'Weekly Compliance Summary',
    format: 'Standard PDF',
    status: 'Generated',
    date: '2026-08-18',
    generatedBy: 'Admin',
    pages: 4
  },
  {
    id: 'EXP-002',
    title: 'Station Duty Log',
    template: 'Station Duty Log',
    format: 'Print-Ready Layout',
    status: 'Generated',
    date: '2026-08-17',
    generatedBy: 'Admin',
    pages: 3
  },
  {
    id: 'EXP-003',
    title: 'Equipment Audit Report',
    template: 'Equipment Audit Report',
    format: 'Office Summary',
    status: 'Pending',
    date: '2026-08-16',
    generatedBy: 'Admin',
    pages: 2
  },
  {
    id: 'EXP-004',
    title: 'Personnel Roster',
    template: 'Personnel Roster',
    format: 'Standard PDF',
    status: 'Generated',
    date: '2026-08-14',
    generatedBy: 'Admin',
    pages: 2
  }
]

const exportHistory = ref([])

/* =========================================================
   LOAD / SAVE
========================================================= */

const loadExports = () => {
  const saved = localStorage.getItem(STORAGE_KEY)

  if (saved) {
    try {
      exportHistory.value = JSON.parse(saved)
      return
    } catch (error) {
      console.error('Failed to load export history:', error)
    }
  }

  exportHistory.value = defaultExports
  saveExports()
}

const saveExports = () => {
  localStorage.setItem(
    STORAGE_KEY,
    JSON.stringify(exportHistory.value)
  )
}

onMounted(() => {
  loadExports()
})

/* =========================================================
   COMPUTED STATS
========================================================= */

const availableTemplates = computed(() =>
  templates.length
)

const generatedCount = computed(() =>
  exportHistory.value.filter(
    item => item.status === 'Generated'
  ).length
)

const pendingCount = computed(() =>
  exportHistory.value.filter(
    item => item.status === 'Pending'
  ).length
)

const thisMonthCount = computed(() => {
  const now = new Date()

  return exportHistory.value.filter(item => {
    const date = new Date(`${item.date}T00:00:00`)

    return (
      date.getMonth() === now.getMonth() &&
      date.getFullYear() === now.getFullYear()
    )
  }).length
})

/* =========================================================
   FILTERED HISTORY
========================================================= */

const filteredHistory = computed(() => {
  const query = searchQuery.value
    .toLowerCase()
    .trim()

  return exportHistory.value
    .filter(item => {
      const matchesSearch =
        !query ||
        item.title.toLowerCase().includes(query) ||
        item.template.toLowerCase().includes(query) ||
        item.id.toLowerCase().includes(query)

      const matchesStatus =
        statusFilter.value === 'All Status' ||
        item.status === statusFilter.value

      return matchesSearch && matchesStatus
    })
    .sort(
      (a, b) =>
        new Date(b.date) - new Date(a.date)
    )
})

/* =========================================================
   CREATE EXPORT
========================================================= */

const openExportModal = template => {
  selectedTemplate.value = template || null

  exportForm.value = {
    title: template
      ? template.name
      : '',
    template: template
      ? template.name
      : '',
    format: selectedFormat.value,
    dateFrom: '',
    dateTo: '',
    includeSummary: true,
    includeDetails: true,
    includeSignature: true
  }

  showExportModal.value = true
}

const createExport = () => {
  if (
    !exportForm.value.title.trim() ||
    !exportForm.value.template
  ) {
    showNotification(
      'Please complete the export information.'
    )
    return
  }

  const newExport = {
    id: `EXP-${String(
      exportHistory.value.length + 1
    ).padStart(3, '0')}`,
    title: exportForm.value.title,
    template: exportForm.value.template,
    format: exportForm.value.format,
    status: 'Generated',
    date: new Date()
      .toISOString()
      .split('T')[0],
    generatedBy: 'Admin',
    pages: estimatePages(
      exportForm.value.template
    )
  }

  exportHistory.value.unshift(newExport)

  saveExports()

  showExportModal.value = false

  showNotification(
    `${newExport.title} generated successfully.`
  )
}

/* =========================================================
   QUICK EXPORT
========================================================= */

const quickExport = template => {
  selectedFormat.value = 'Standard PDF'
  openExportModal(template)
}

/* =========================================================
   VIEW DETAILS
========================================================= */

const viewExport = item => {
  selectedTemplate.value = item
  showDetailsModal.value = true
}

/* =========================================================
   PRINT
========================================================= */

const printExport = item => {
  const printWindow = window.open(
    '',
    '_blank',
    'width=900,height=700'
  )

  if (!printWindow) {
    showNotification(
      'Please allow pop-ups to print the report.'
    )
    return
  }

  printWindow.document.write(`
    <!DOCTYPE html>
    <html>
      <head>
        <title>${item.title}</title>

        <style>
          body {
            font-family: Arial, sans-serif;
            padding: 40px;
            color: #1e293b;
          }

          .header {
            border-bottom: 3px solid #8B1E23;
            padding-bottom: 15px;
            margin-bottom: 30px;
          }

          h1 {
            margin: 0;
            color: #8B1E23;
          }

          h2 {
            margin-top: 30px;
          }

          .meta {
            margin-top: 10px;
            color: #64748b;
          }

          .box {
            border: 1px solid #cbd5e1;
            padding: 15px;
            margin-top: 15px;
          }

          .signature {
            margin-top: 80px;
            display: flex;
            justify-content: space-between;
          }

          .line {
            width: 220px;
            border-top: 1px solid #334155;
            padding-top: 8px;
            text-align: center;
          }

          @media print {
            body {
              padding: 25px;
            }
          }
        </style>
      </head>

      <body>

        <div class="header">
          <h1>FIRENOTIFY</h1>
          <p>Station Operations & Compliance Monitoring System</p>
        </div>

        <h2>${item.title}</h2>

        <div class="meta">
          Report ID: ${item.id}<br>
          Template: ${item.template}<br>
          Format: ${item.format}<br>
          Generated: ${formatDate(item.date)}
        </div>

        <div class="box">
          <strong>Report Summary</strong>
          <p>
            This document contains the formatted administrative
            records generated through the FireNotify system.
          </p>
        </div>

        <div class="box">
          <strong>Station Information</strong>
          <p>
            Bureau of Fire Protection<br>
            BFP Balingasag
          </p>
        </div>

        <div class="box">
          <strong>Document Status</strong>
          <p>${item.status}</p>
        </div>

        <div class="signature">
          <div class="line">
            Prepared By
          </div>

          <div class="line">
            Station Chief
          </div>
        </div>

      </body>
    </html>
  `)

  printWindow.document.close()

  setTimeout(() => {
    printWindow.print()
  }, 300)

  showNotification(
    'Print-ready report opened.'
  )
}

/* =========================================================
   FORMAT SELECTION
========================================================= */

const selectFormat = format => {
  selectedFormat.value = format
  exportForm.value.format = format

  showNotification(
    `${format} selected.`
  )
}

/* =========================================================
   FILTER
========================================================= */

const clearFilters = () => {
  searchQuery.value = ''
  statusFilter.value = 'All Status'
}

/* =========================================================
   HELPERS
========================================================= */

const estimatePages = templateName => {
  const template = templates.find(
    item => item.name === templateName
  )

  if (!template) return 2

  if (template.pages.includes('8')) return 8
  if (template.pages.includes('5')) return 5
  if (template.pages.includes('4')) return 4

  return 2
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

const showNotification = message => {
  toastMessage.value = message
  showToast.value = true

  setTimeout(() => {
    showToast.value = false
  }, 2500)
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
            Administrative Tools
          </p>

          <h2
            class="text-2xl font-bold text-slate-900 mt-1"
          >
            Print &amp; Export PDF
          </h2>

          <p
            class="text-base text-slate-500 mt-1"
          >
            Generate formatted reports, share summaries,
            and export records for documentation.
          </p>

        </div>

        <button
          @click="openExportModal()"
          class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition"
        >
          Create PDF Export
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
        <p
          class="text-3xl font-bold text-[#8B1E23]"
        >
          {{ String(availableTemplates).padStart(2, '0') }}
        </p>

        <p
          class="text-sm text-slate-500 mt-1"
        >
          Available Templates
        </p>
      </div>

      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <p
          class="text-3xl font-bold text-blue-600"
        >
          {{ String(thisMonthCount).padStart(2, '0') }}
        </p>

        <p
          class="text-sm text-slate-500 mt-1"
        >
          This Month
        </p>
      </div>

      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <p
          class="text-3xl font-bold text-green-600"
        >
          {{ String(generatedCount).padStart(2, '0') }}
        </p>

        <p
          class="text-sm text-slate-500 mt-1"
        >
          Generated
        </p>
      </div>

      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <p
          class="text-3xl font-bold text-yellow-600"
        >
          {{ String(pendingCount).padStart(2, '0') }}
        </p>

        <p
          class="text-sm text-slate-500 mt-1"
        >
          Pending
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
          placeholder="Search exports, templates, or ID..."
          class="flex-1 px-4 py-3 border border-slate-200 rounded-xl outline-none focus:border-[#8B1E23]"
        />

        <select
          v-model="statusFilter"
          class="px-4 py-3 border border-slate-200 rounded-xl bg-white"
        >
          <option>All Status</option>
          <option>Generated</option>
          <option>Pending</option>
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
         TEMPLATES + RECENT EXPORTS
    ====================================================== -->

    <section
      class="grid grid-cols-1 xl:grid-cols-2 gap-6"
    >

      <!-- EXPORT TEMPLATES -->

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
              Export Templates
            </h2>

            <p
              class="text-sm text-slate-500 mt-1"
            >
              Quick formatting options for common reports
            </p>

          </div>

          <span
            class="text-xs font-bold text-slate-500"
          >
            {{ templates.length }} Templates
          </span>

        </div>

        <div
          class="mt-5 space-y-4"
        >

          <div
            v-for="template in templates"
            :key="template.id"
            class="p-4 rounded-xl border border-slate-200 bg-slate-50 hover:border-[#8B1E23] transition"
          >

            <div
              class="flex flex-col sm:flex-row sm:justify-between sm:items-center gap-3"
            >

              <div>

                <p
                  class="text-sm font-bold text-slate-900"
                >
                  {{ template.name }}
                </p>

                <p
                  class="text-xs text-slate-500 mt-1"
                >
                  {{ template.description }}
                </p>

                <div
                  class="flex gap-2 mt-2"
                >

                  <span
                    class="px-2 py-1 rounded-full bg-white border border-slate-200 text-[11px] font-bold text-slate-500"
                  >
                    {{ template.category }}
                  </span>

                  <span
                    class="px-2 py-1 rounded-full bg-white border border-slate-200 text-[11px] font-bold text-slate-500"
                  >
                    {{ template.pages }}
                  </span>

                </div>

              </div>

              <button
                @click="quickExport(template)"
                class="text-sm font-bold text-[#8B1E23] hover:text-[#72181D] whitespace-nowrap"
              >
                Export
              </button>

            </div>

          </div>

        </div>

      </div>

      <!-- RECENT EXPORTS -->

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
              Recent Exports
            </h2>

            <p
              class="text-sm text-slate-500 mt-1"
            >
              Latest generated PDFs and print requests
            </p>

          </div>

        </div>

        <div
          class="mt-5 space-y-4"
        >

          <div
            v-for="item in filteredHistory.slice(0, 4)"
            :key="item.id"
            class="p-4 rounded-xl border"
            :class="
              item.status === 'Generated'
                ? 'border-emerald-200 bg-emerald-50'
                : 'border-amber-200 bg-amber-50'
            "
          >

            <div
              class="flex justify-between gap-3"
            >

              <div>

                <p
                  class="text-sm font-bold text-slate-900"
                >
                  {{ item.title }}
                </p>

                <p
                  class="text-sm text-slate-600 mt-1"
                >
                  {{ item.template }}
                </p>

                <p
                  class="text-xs text-slate-500 mt-2"
                >
                  {{ formatDate(item.date) }}
                </p>

              </div>

              <span
                class="h-fit px-2.5 py-1 rounded-full text-xs font-bold"
                :class="
                  item.status === 'Generated'
                    ? 'bg-green-100 text-green-700'
                    : 'bg-yellow-100 text-yellow-700'
                "
              >
                {{ item.status }}
              </span>

            </div>

            <div
              class="flex gap-2 mt-3"
            >

              <button
                @click="viewExport(item)"
                class="px-3 py-2 rounded-lg bg-white border border-slate-200 text-xs font-bold text-slate-700"
              >
                View
              </button>

              <button
                @click="printExport(item)"
                class="px-3 py-2 rounded-lg bg-white border border-slate-200 text-xs font-bold text-[#8B1E23]"
              >
                Print
              </button>

            </div>

          </div>

        </div>

      </div>

    </section>

    <!-- =====================================================
         EXPORT HISTORY TABLE
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
            Export History
          </h2>

          <p
            class="text-sm text-slate-500 mt-1"
          >
            Track previously generated reports
          </p>

        </div>

        <span
          class="text-xs font-bold text-slate-500"
        >
          {{ filteredHistory.length }} records
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
                Export
              </th>

              <th class="pb-2 pr-4">
                Template
              </th>

              <th class="pb-2 pr-4">
                Date
              </th>

              <th class="pb-2 pr-4">
                Format
              </th>

              <th class="pb-2 pr-4">
                Status
              </th>

              <th class="pb-2 text-right">
                Actions
              </th>

            </tr>

          </thead>

          <tbody>

            <tr
              v-for="item in filteredHistory"
              :key="item.id"
              class="bg-slate-50"
            >

              <td
                class="py-4 pr-4 rounded-l-xl"
              >

                <p
                  class="font-semibold text-slate-900"
                >
                  {{ item.title }}
                </p>

                <p
                  class="text-xs text-slate-400 mt-1"
                >
                  {{ item.id }}
                </p>

              </td>

              <td
                class="py-4 pr-4 text-slate-600"
              >
                {{ item.template }}
              </td>

              <td
                class="py-4 pr-4 text-slate-600"
              >
                {{ formatDate(item.date) }}
              </td>

              <td
                class="py-4 pr-4 text-slate-600"
              >
                {{ item.format }}
              </td>

              <td
                class="py-4 pr-4"
              >

                <span
                  class="px-3 py-1 rounded-full text-xs font-bold"
                  :class="
                    item.status === 'Generated'
                      ? 'bg-green-100 text-green-700'
                      : 'bg-yellow-100 text-yellow-700'
                  "
                >
                  {{ item.status }}
                </span>

              </td>

              <td
                class="py-4 pr-4 rounded-r-xl"
              >

                <div
                  class="flex justify-end gap-2"
                >

                  <button
                    @click="viewExport(item)"
                    class="px-3 py-2 rounded-lg bg-white border border-slate-200 text-xs font-bold text-slate-700"
                  >
                    View
                  </button>

                  <button
                    @click="printExport(item)"
                    class="px-3 py-2 rounded-lg bg-[#8B1E23] text-white text-xs font-bold"
                  >
                    Print
                  </button>

                </div>

              </td>

            </tr>

          </tbody>

        </table>

        <div
          v-if="filteredHistory.length === 0"
          class="py-12 text-center"
        >

          <p class="text-3xl">
            📄
          </p>

          <p
            class="font-bold text-slate-700 mt-2"
          >
            No export records found
          </p>

        </div>

      </div>

    </section>

    <!-- =====================================================
         PRINT SETUP
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div
        class="flex items-center justify-between border-b border-slate-200 pb-5"
      >

        <div>

          <h2
            class="text-xl font-bold text-slate-900"
          >
            Print Setup
          </h2>

          <p
            class="text-sm text-slate-500 mt-1"
          >
            Choose output preferences for your next export
          </p>

        </div>

        <span
          class="text-xs font-bold text-[#8B1E23]"
        >
          {{ selectedFormat }}
        </span>

      </div>

      <div
        class="mt-5 grid grid-cols-1 md:grid-cols-3 gap-4"
      >

        <button
          @click="selectFormat('Standard PDF')"
          class="px-4 py-4 rounded-xl border text-left text-sm font-semibold transition"
          :class="
            selectedFormat === 'Standard PDF'
              ? 'border-[#8B1E23] bg-red-50 text-[#8B1E23]'
              : 'border-slate-200 bg-slate-50 text-slate-700 hover:bg-slate-100'
          "
        >
          <p class="font-bold">
            Standard PDF
          </p>

          <p
            class="text-xs text-slate-500 mt-1"
          >
            Normal document export
          </p>
        </button>

        <button
          @click="selectFormat('Print-Ready Layout')"
          class="px-4 py-4 rounded-xl border text-left text-sm font-semibold transition"
          :class="
            selectedFormat === 'Print-Ready Layout'
              ? 'border-[#8B1E23] bg-red-50 text-[#8B1E23]'
              : 'border-slate-200 bg-slate-50 text-slate-700 hover:bg-slate-100'
          "
        >
          <p class="font-bold">
            Print-Ready Layout
          </p>

          <p
            class="text-xs text-slate-500 mt-1"
          >
            Optimized for physical printing
          </p>
        </button>

        <button
          @click="selectFormat('Office Summary')"
          class="px-4 py-4 rounded-xl border text-left text-sm font-semibold transition"
          :class="
            selectedFormat === 'Office Summary'
              ? 'border-[#8B1E23] bg-red-50 text-[#8B1E23]'
              : 'border-slate-200 bg-slate-50 text-slate-700 hover:bg-slate-100'
          "
        >
          <p class="font-bold">
            Office Summary
          </p>

          <p
            class="text-xs text-slate-500 mt-1"
          >
            Short administrative summary
          </p>
        </button>

      </div>

    </section>

    <!-- =====================================================
         CREATE EXPORT MODAL
    ====================================================== -->

    <div
      v-if="showExportModal"
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
              Create PDF Export
            </h2>

            <p
              class="text-sm text-slate-500 mt-1"
            >
              Configure your administrative report.
            </p>

          </div>

          <button
            @click="showExportModal = false"
            class="text-2xl text-slate-400 hover:text-slate-700"
          >
            ×
          </button>

        </div>

        <div
          class="p-6 space-y-5"
        >

          <div>

            <label
              class="block text-sm font-bold text-slate-700 mb-2"
            >
              Report Title
            </label>

            <input
              v-model="exportForm.title"
              type="text"
              placeholder="Enter report title"
              class="w-full px-4 py-3 border border-slate-200 rounded-xl outline-none focus:border-[#8B1E23]"
            />

          </div>

          <div>

            <label
              class="block text-sm font-bold text-slate-700 mb-2"
            >
              Export Template
            </label>

            <select
              v-model="exportForm.template"
              class="w-full px-4 py-3 border border-slate-200 rounded-xl bg-white"
            >

              <option
                value=""
                disabled
              >
                Select template
              </option>

              <option
                v-for="template in templates"
                :key="template.id"
                :value="template.name"
              >
                {{ template.name }}
              </option>

            </select>

          </div>

          <div>

            <label
              class="block text-sm font-bold text-slate-700 mb-2"
            >
              Output Format
            </label>

            <select
              v-model="exportForm.format"
              class="w-full px-4 py-3 border border-slate-200 rounded-xl bg-white"
            >
              <option>Standard PDF</option>
              <option>Print-Ready Layout</option>
              <option>Office Summary</option>
            </select>

          </div>

          <div
            class="grid grid-cols-1 sm:grid-cols-2 gap-4"
          >

            <div>

              <label
                class="block text-sm font-bold text-slate-700 mb-2"
              >
                Date From
              </label>

              <input
                v-model="exportForm.dateFrom"
                type="date"
                class="w-full px-4 py-3 border border-slate-200 rounded-xl"
              />

            </div>

            <div>

              <label
                class="block text-sm font-bold text-slate-700 mb-2"
              >
                Date To
              </label>

              <input
                v-model="exportForm.dateTo"
                type="date"
                class="w-full px-4 py-3 border border-slate-200 rounded-xl"
              />

            </div>

          </div>

          <div
            class="border border-slate-200 rounded-xl p-4 space-y-3"
          >

            <p
              class="text-sm font-bold text-slate-800"
            >
              Include in Report
            </p>

            <label
              class="flex items-center gap-3 text-sm text-slate-700"
            >
              <input
                v-model="exportForm.includeSummary"
                type="checkbox"
                class="w-4 h-4"
              />
              Include summary
            </label>

            <label
              class="flex items-center gap-3 text-sm text-slate-700"
            >
              <input
                v-model="exportForm.includeDetails"
                type="checkbox"
                class="w-4 h-4"
              />
              Include detailed records
            </label>

            <label
              class="flex items-center gap-3 text-sm text-slate-700"
            >
              <input
                v-model="exportForm.includeSignature"
                type="checkbox"
                class="w-4 h-4"
              />
              Include signature section
            </label>

          </div>

        </div>

        <div
          class="p-6 border-t border-slate-200 flex justify-end gap-3"
        >

          <button
            @click="showExportModal = false"
            class="px-5 py-3 rounded-xl border border-slate-200 font-bold text-slate-700"
          >
            Cancel
          </button>

          <button
            @click="createExport"
            class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D]"
          >
            Create Export
          </button>

        </div>

      </div>
    </div>

    <!-- =====================================================
         DETAILS MODAL
    ====================================================== -->

    <div
      v-if="showDetailsModal && selectedTemplate"
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
              {{ selectedTemplate.id }}
            </p>

            <h2
              class="text-xl font-bold text-slate-900 mt-1"
            >
              {{ selectedTemplate.title }}
            </h2>

          </div>

          <button
            @click="showDetailsModal = false"
            class="text-2xl text-slate-400"
          >
            ×
          </button>

        </div>

        <div
          class="p-6 space-y-4"
        >

          <div
            class="grid grid-cols-2 gap-4"
          >

            <div
              class="bg-slate-50 rounded-xl p-4"
            >

              <p
                class="text-xs text-slate-400 font-bold uppercase"
              >
                Template
              </p>

              <p
                class="text-sm font-semibold text-slate-800 mt-1"
              >
                {{ selectedTemplate.template }}
              </p>

            </div>

            <div
              class="bg-slate-50 rounded-xl p-4"
            >

              <p
                class="text-xs text-slate-400 font-bold uppercase"
              >
                Format
              </p>

              <p
                class="text-sm font-semibold text-slate-800 mt-1"
              >
                {{ selectedTemplate.format }}
              </p>

            </div>

            <div
              class="bg-slate-50 rounded-xl p-4"
            >

              <p
                class="text-xs text-slate-400 font-bold uppercase"
              >
                Date
              </p>

              <p
                class="text-sm font-semibold text-slate-800 mt-1"
              >
                {{ formatDate(selectedTemplate.date) }}
              </p>

            </div>

            <div
              class="bg-slate-50 rounded-xl p-4"
            >

              <p
                class="text-xs text-slate-400 font-bold uppercase"
              >
                Pages
              </p>

              <p
                class="text-sm font-semibold text-slate-800 mt-1"
              >
                {{ selectedTemplate.pages }}
              </p>

            </div>

          </div>

        </div>

        <div
          class="p-6 border-t border-slate-200 flex justify-end gap-3"
        >

          <button
            @click="showDetailsModal = false"
            class="px-5 py-3 rounded-xl bg-slate-100 font-bold text-slate-700"
          >
            Close
          </button>

          <button
            @click="printExport(selectedTemplate)"
            class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold"
          >
            Print Report
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