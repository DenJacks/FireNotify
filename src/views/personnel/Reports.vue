<template>
  <div class="w-full min-w-0 space-y-6">

    <!-- ========================================================= -->
    <!-- HEADER -->
    <!-- ========================================================= -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">

        <div>
          <p class="text-sm font-semibold text-[#8B1E23]">
            FIRENOTIFY PERSONNEL PORTAL
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            My Reports
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Create, submit, monitor, and review your operational reports.
          </p>
        </div>

        <button
          @click="openCreateModal"
          class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D] transition shadow-sm"
        >
          + Create Report
        </button>

      </div>

    </section>


    <!-- ========================================================= -->
    <!-- STATISTICS -->
    <!-- ========================================================= -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">

      <!-- TOTAL -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

        <div class="flex items-center justify-between">

          <div>
            <p class="text-sm text-slate-500">
              Total Reports
            </p>

            <p class="text-3xl font-bold text-slate-900 mt-1">
              {{ totalReports }}
            </p>

            <p class="text-xs text-slate-400 mt-1">
              Current records
            </p>
          </div>

          <div class="h-12 w-12 rounded-xl bg-blue-50 flex items-center justify-center">
            <span
              v-html="ICONS.reports"
              class="h-6 w-6 text-blue-600"
            ></span>
          </div>

        </div>

      </div>


      <!-- PENDING -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

        <div class="flex items-center justify-between">

          <div>
            <p class="text-sm text-slate-500">
              Pending
            </p>

            <p class="text-3xl font-bold text-yellow-600 mt-1">
              {{ pendingReports }}
            </p>

            <p class="text-xs text-slate-400 mt-1">
              Requires submission
            </p>
          </div>

          <div class="h-12 w-12 rounded-xl bg-yellow-50 flex items-center justify-center">
            <span
              v-html="ICONS.clock"
              class="h-6 w-6 text-yellow-600"
            ></span>
          </div>

        </div>

      </div>


      <!-- SUBMITTED -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

        <div class="flex items-center justify-between">

          <div>
            <p class="text-sm text-slate-500">
              Submitted
            </p>

            <p class="text-3xl font-bold text-green-600 mt-1">
              {{ submittedReports }}
            </p>

            <p class="text-xs text-slate-400 mt-1">
              Successfully submitted
            </p>
          </div>

          <div class="h-12 w-12 rounded-xl bg-green-50 flex items-center justify-center">
            <span
              v-html="ICONS.check"
              class="h-6 w-6 text-green-600"
            ></span>
          </div>

        </div>

      </div>


      <!-- RETURNED -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

        <div class="flex items-center justify-between">

          <div>
            <p class="text-sm text-slate-500">
              Returned
            </p>

            <p class="text-3xl font-bold text-[#8B1E23] mt-1">
              {{ returnedReports }}
            </p>

            <p class="text-xs text-slate-400 mt-1">
              Needs correction
            </p>
          </div>

          <div class="h-12 w-12 rounded-xl bg-red-50 flex items-center justify-center">
            <span
              v-html="ICONS.siren"
              class="h-6 w-6 text-[#8B1E23]"
            ></span>
          </div>

        </div>

      </div>

    </section>


    <!-- ========================================================= -->
    <!-- SEARCH + FILTER -->
    <!-- ========================================================= -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

      <div class="flex flex-col lg:flex-row lg:items-end gap-4">

        <div class="flex-1">

          <label class="block text-sm font-semibold text-slate-700 mb-2">
            Search Reports
          </label>

          <div class="relative">

            <input
              v-model="searchQuery"
              type="text"
              placeholder="Search report title, activity, location..."
              class="w-full px-4 py-3 pl-11 rounded-xl border border-slate-300 text-sm outline-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
            />

            <span class="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400">
              🔎
            </span>

          </div>

        </div>


        <div class="w-full lg:w-56">

          <label class="block text-sm font-semibold text-slate-700 mb-2">
            Status
          </label>

          <select
            v-model="statusFilter"
            class="w-full px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm text-slate-700 outline-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
          >
            <option value="All">All Status</option>
            <option value="Draft">Draft</option>
            <option value="Pending">Pending</option>
            <option value="Submitted">Submitted</option>
            <option value="Returned">Returned</option>
          </select>

        </div>


        <button
          @click="resetFilters"
          class="px-5 py-3 rounded-xl border border-slate-300 bg-white text-slate-700 text-sm font-bold hover:bg-slate-100 transition"
        >
          Reset
        </button>

      </div>

      <div class="mt-4 pt-4 border-t border-slate-100">

        <p class="text-sm text-slate-500">
          Showing
          <span class="font-bold text-slate-900">
            {{ filteredReports.length }}
          </span>
          of
          <span class="font-bold text-slate-900">
            {{ totalReports }}
          </span>
          reports
        </p>

      </div>

    </section>


    <!-- ========================================================= -->
    <!-- MAIN CONTENT -->
    <!-- ========================================================= -->
    <section class="grid grid-cols-1 lg:grid-cols-3 gap-6">

      <!-- ======================================================= -->
      <!-- REPORT LIST -->
      <!-- ======================================================= -->
      <div class="lg:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-4">

          <div>
            <h3 class="text-lg font-bold text-slate-900">
              Report List
            </h3>

            <p class="text-sm text-slate-500 mt-1">
              Your operational report records.
            </p>
          </div>

          <span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">
            {{ filteredReports.length }} Reports
          </span>

        </div>


        <!-- EMPTY -->
        <div
          v-if="filteredReports.length === 0"
          class="py-14 text-center"
        >

          <div class="h-14 w-14 mx-auto rounded-2xl bg-slate-100 flex items-center justify-center">
            📄
          </div>

          <h4 class="mt-4 font-bold text-slate-900">
            No reports found
          </h4>

          <p class="text-sm text-slate-500 mt-1">
            Try changing your search or status filter.
          </p>

        </div>


        <!-- LIST -->
        <div v-else class="mt-5 space-y-4">

          <article
            v-for="report in filteredReports"
            :key="report.id"
            class="p-5 rounded-xl border transition hover:shadow-sm"
            :class="reportCardClass(report.status)"
          >

            <div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4">

              <div class="flex gap-4">

                <div
                  class="h-11 w-11 rounded-xl flex items-center justify-center shrink-0"
                  :class="reportIconClass(report.status)"
                >
                  <span
                    v-html="reportIcon(report.status)"
                    class="h-5 w-5"
                  ></span>
                </div>


                <div>

                  <div class="flex flex-wrap items-center gap-2">

                    <p class="text-base font-bold text-slate-900">
                      {{ report.title }}
                    </p>

                    <span
                      class="px-2.5 py-1 rounded-full text-xs font-bold"
                      :class="statusClass(report.status)"
                    >
                      {{ report.status }}
                    </span>

                  </div>

                  <p class="text-sm text-slate-500 mt-1">
                    Activity: {{ report.activity }}
                  </p>

                  <p class="text-sm text-slate-500 mt-1">
                    Location: {{ report.location }}
                  </p>

                  <p
                    v-if="report.status === 'Pending'"
                    class="text-xs text-yellow-700 font-semibold mt-2"
                  >
                    Action required
                  </p>

                  <p
                    v-if="report.status === 'Submitted'"
                    class="text-xs text-green-700 font-semibold mt-2"
                  >
                    ✓ Successfully submitted
                  </p>

                  <p
                    v-if="report.status === 'Returned'"
                    class="text-xs text-[#8B1E23] font-semibold mt-2"
                  >
                    Correction required
                  </p>

                </div>

              </div>

            </div>


            <!-- REMARKS -->
            <div
              v-if="report.status === 'Returned' && report.remarks"
              class="mt-4 p-4 rounded-xl bg-white border border-red-200"
            >

              <p class="text-xs font-semibold text-slate-500 uppercase">
                Remarks
              </p>

              <p class="text-sm text-slate-700 mt-1">
                {{ report.remarks }}
              </p>

            </div>


            <!-- ACTIONS -->
            <div class="mt-4 flex flex-wrap gap-2">

              <button
                v-if="report.status === 'Pending'"
                @click="submitReport(report)"
                class="px-4 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-semibold hover:bg-[#72181D]"
              >
                Submit Report
              </button>


              <button
                v-if="report.status === 'Returned'"
                @click="reviseReport(report)"
                class="px-4 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-semibold hover:bg-[#72181D]"
              >
                Revise Report
              </button>


              <button
                v-if="report.status === 'Draft'"
                @click="editReport(report)"
                class="px-4 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-semibold hover:bg-[#72181D]"
              >
                Continue Draft
              </button>


              <button
                @click="viewReport(report)"
                class="px-4 py-2 rounded-lg border border-slate-300 bg-white text-slate-700 text-sm font-semibold hover:bg-slate-100"
              >
                View Report
              </button>


              <button
                v-if="report.status === 'Draft'"
                @click="deleteDraft(report)"
                class="px-4 py-2 rounded-lg border border-red-200 bg-red-50 text-[#8B1E23] text-sm font-semibold hover:bg-red-100"
              >
                Delete
              </button>

            </div>

          </article>

        </div>

      </div>


      <!-- ======================================================= -->
      <!-- RIGHT SIDE -->
      <!-- ======================================================= -->
      <div class="space-y-6">


        <!-- COMPLETION -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <h3 class="text-lg font-bold text-slate-900">
            Report Completion
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            Your report submission progress.
          </p>


          <div class="mt-5">

            <div class="flex items-end justify-between">

              <p class="text-3xl font-bold text-[#8B1E23]">
                {{ completionRate }}%
              </p>

              <span
                class="text-xs font-semibold"
                :class="completionRate >= 80 ? 'text-green-600' : 'text-yellow-600'"
              >
                {{ completionMessage }}
              </span>

            </div>


            <div class="mt-3 h-3 rounded-full bg-slate-200 overflow-hidden">

              <div
                class="h-full bg-[#8B1E23] rounded-full transition-all duration-500"
                :style="{ width: `${completionRate}%` }"
              ></div>

            </div>


            <div class="grid grid-cols-2 gap-4 mt-5">

              <div>
                <p class="text-xs text-slate-500">
                  Submitted
                </p>

                <p class="text-lg font-bold text-green-600">
                  {{ submittedReports }}
                </p>
              </div>

              <div>
                <p class="text-xs text-slate-500">
                  Pending
                </p>

                <p class="text-lg font-bold text-yellow-600">
                  {{ pendingReports }}
                </p>
              </div>

            </div>

          </div>

        </div>


        <!-- DEADLINES -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <h3 class="text-lg font-bold text-slate-900">
            Report Deadlines
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            Upcoming submission deadlines.
          </p>


          <div class="mt-5 space-y-3">

            <div
              v-for="deadline in deadlines"
              :key="deadline.title"
              class="p-4 rounded-xl border"
              :class="deadline.urgent ? 'bg-yellow-50 border-yellow-200' : 'bg-slate-50 border-slate-200'"
            >

              <div class="flex items-start justify-between gap-3">

                <div>

                  <p class="text-sm font-bold text-slate-900">
                    {{ deadline.title }}
                  </p>

                  <p class="text-xs text-slate-500 mt-1">
                    {{ deadline.date }}
                  </p>

                </div>

                <span
                  class="text-xs font-bold"
                  :class="deadline.urgent ? 'text-yellow-700' : 'text-slate-500'"
                >
                  {{ deadline.label }}
                </span>

              </div>

            </div>

          </div>

        </div>


        <!-- RECENT ACTIVITY -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <h3 class="text-lg font-bold text-slate-900">
            Recent Activity
          </h3>

          <div class="mt-5 space-y-4">

            <div
              v-for="activity in recentActivity"
              :key="activity.id"
              class="flex gap-3"
            >

              <div
                class="h-8 w-8 rounded-full flex items-center justify-center shrink-0"
                :class="activity.type === 'success'
                  ? 'bg-green-100 text-green-600'
                  : 'bg-red-100 text-[#8B1E23]'"
              >
                {{ activity.type === 'success' ? '✓' : '!' }}
              </div>

              <div>

                <p class="text-sm font-semibold text-slate-900">
                  {{ activity.title }}
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  {{ activity.report }}
                </p>

                <p class="text-xs text-slate-400 mt-1">
                  {{ activity.date }}
                </p>

              </div>

            </div>

          </div>

        </div>

      </div>

    </section>


    <!-- ========================================================= -->
    <!-- CREATE / EDIT REPORT MODAL -->
    <!-- ========================================================= -->
    <div
      v-if="showFormModal"
      class="fixed inset-0 z-50 bg-slate-900/50 flex items-center justify-center p-4"
      @click.self="closeFormModal"
    >

      <div class="w-full max-w-2xl bg-white rounded-2xl shadow-xl overflow-hidden">

        <div class="px-6 py-5 border-b border-slate-200 flex items-center justify-between">

          <div>

            <p class="text-xs font-bold text-[#8B1E23] uppercase">
              Report Management
            </p>

            <h3 class="text-xl font-bold text-slate-900 mt-1">
              {{ editingReport ? 'Edit Report' : 'Create Report' }}
            </h3>

          </div>

          <button
            @click="closeFormModal"
            class="h-10 w-10 rounded-xl hover:bg-slate-100 text-slate-500 text-xl"
          >
            ×
          </button>

        </div>


        <form
          @submit.prevent="saveReport"
          class="p-6 space-y-5"
        >

          <!-- TITLE -->
          <div>

            <label class="block text-sm font-semibold text-slate-700 mb-2">
              Report Title
            </label>

            <input
              v-model="form.title"
              type="text"
              placeholder="Enter report title"
              class="w-full px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/20"
            />

          </div>


          <!-- ACTIVITY -->
          <div>

            <label class="block text-sm font-semibold text-slate-700 mb-2">
              Activity
            </label>

            <select
              v-model="form.activity"
              class="w-full px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm outline-none focus:border-[#8B1E23]"
            >
              <option value="">
                Select activity
              </option>

              <option>
                Fire Safety Inspection
              </option>

              <option>
                Routine Safety Patrol
              </option>

              <option>
                Community Fire Safety Seminar
              </option>

              <option>
                Fire Drill Monitoring
              </option>

              <option>
                Emergency Response Drill
              </option>

            </select>

          </div>


          <!-- LOCATION -->
          <div>

            <label class="block text-sm font-semibold text-slate-700 mb-2">
              Location
            </label>

            <input
              v-model="form.location"
              type="text"
              placeholder="Enter activity location"
              class="w-full px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/20"
            />

          </div>


          <!-- REPORT CONTENT -->
          <div>

            <label class="block text-sm font-semibold text-slate-700 mb-2">
              Report Details
            </label>

            <textarea
              v-model="form.content"
              rows="5"
              placeholder="Enter accomplishment details, observations, findings, and actions taken..."
              class="w-full px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none resize-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/20"
            ></textarea>

          </div>


          <!-- FOOTER -->
          <div class="flex flex-col sm:flex-row justify-end gap-3 pt-2">

            <button
              type="button"
              @click="closeFormModal"
              class="px-5 py-2.5 rounded-xl border border-slate-300 bg-white text-slate-700 text-sm font-bold hover:bg-slate-100"
            >
              Cancel
            </button>

            <button
              type="button"
              @click="saveAsDraft"
              class="px-5 py-2.5 rounded-xl border border-[#8B1E23] text-[#8B1E23] text-sm font-bold hover:bg-red-50"
            >
              Save Draft
            </button>

            <button
              type="submit"
              class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]"
            >
              {{ editingReport ? 'Update Report' : 'Submit Report' }}
            </button>

          </div>

        </form>

      </div>

    </div>


    <!-- ========================================================= -->
    <!-- VIEW REPORT MODAL -->
    <!-- ========================================================= -->
    <div
      v-if="showViewModal && selectedReport"
      class="fixed inset-0 z-[60] bg-slate-900/50 flex items-center justify-center p-4"
      @click.self="closeViewModal"
    >

      <div class="w-full max-w-2xl bg-white rounded-2xl shadow-xl overflow-hidden">

        <div class="px-6 py-5 border-b border-slate-200 flex items-center justify-between">

          <div>

            <p class="text-xs font-bold text-[#8B1E23] uppercase">
              Report Details
            </p>

            <h3 class="text-xl font-bold text-slate-900 mt-1">
              {{ selectedReport.title }}
            </h3>

          </div>

          <button
            @click="closeViewModal"
            class="h-10 w-10 rounded-xl hover:bg-slate-100 text-slate-500 text-xl"
          >
            ×
          </button>

        </div>


        <div class="p-6 space-y-5">

          <div class="flex flex-wrap gap-2">

            <span
              class="px-3 py-1.5 rounded-full text-xs font-bold"
              :class="statusClass(selectedReport.status)"
            >
              {{ selectedReport.status }}
            </span>

          </div>


          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-400 uppercase font-semibold">
                Activity
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedReport.activity }}
              </p>
            </div>

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-400 uppercase font-semibold">
                Location
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedReport.location }}
              </p>
            </div>

          </div>


          <div>

            <p class="text-xs font-semibold text-slate-500 uppercase">
              Report Details
            </p>

            <div class="mt-2 p-4 rounded-xl bg-slate-50 border border-slate-200">

              <p class="text-sm text-slate-700 whitespace-pre-line leading-relaxed">
                {{ selectedReport.content || 'No report details provided.' }}
              </p>

            </div>

          </div>


          <div
            v-if="selectedReport.remarks"
            class="p-4 rounded-xl bg-red-50 border border-red-200"
          >

            <p class="text-xs font-semibold text-[#8B1E23] uppercase">
              Remarks
            </p>

            <p class="text-sm text-slate-700 mt-1">
              {{ selectedReport.remarks }}
            </p>

          </div>

        </div>


        <div class="px-6 py-4 bg-slate-50 border-t border-slate-200 flex justify-end">

          <button
            @click="closeViewModal"
            class="px-5 py-2.5 rounded-xl border border-slate-300 bg-white text-slate-700 text-sm font-bold hover:bg-slate-100"
          >
            Close
          </button>

        </div>

      </div>

    </div>


    <!-- ========================================================= -->
    <!-- TOAST -->
    <!-- ========================================================= -->
    <transition name="toast">

      <div
        v-if="toastMessage"
        class="fixed bottom-6 right-6 z-[80] bg-white border border-slate-200 shadow-xl rounded-xl px-5 py-4 flex items-center gap-3"
      >

        <div class="h-9 w-9 rounded-full bg-green-100 flex items-center justify-center text-green-600 font-bold">
          ✓
        </div>

        <div>

          <p class="text-sm font-bold text-slate-900">
            Action Successful
          </p>

          <p class="text-xs text-slate-500 mt-0.5">
            {{ toastMessage }}
          </p>

        </div>

      </div>

    </transition>

  </div>
</template>


<script setup>
import { computed, ref } from 'vue'


/* =========================================================
   PROPS
========================================================= */

const props = defineProps({
  currentUser: {
    type: Object,
    required: false,
    default: null
  },

  ICONS: {
    type: Object,
    required: true
  }
})

const ICONS = props.ICONS


/* =========================================================
   REPORT DATA
========================================================= */

const reports = ref([
  {
    id: 1,
    title: 'Fire Safety Inspection Report',
    activity: 'Fire Safety Inspection',
    location: 'Public Market Complex',
    status: 'Pending',
    date: 'September 12, 2026',
    content: '',
    remarks: ''
  },

  {
    id: 2,
    title: 'Routine Safety Patrol Report',
    activity: 'Routine Safety Patrol',
    location: 'Zone 2 Commercial Area',
    status: 'Submitted',
    date: 'September 7, 2026',
    content:
      'Routine safety patrol was conducted in the Zone 2 Commercial Area. No major fire safety violations were observed during the inspection.',
    remarks: ''
  },

  {
    id: 3,
    title: 'Fire Drill Monitoring Report',
    activity: 'Fire Drill Monitoring',
    location: 'Municipal Elementary School',
    status: 'Returned',
    date: 'September 8, 2026',
    content:
      'Fire drill monitoring was conducted at the Municipal Elementary School.',
    remarks:
      'Please attach the attendance sheet and update the inspection details.'
  },

  {
    id: 4,
    title: 'Community Fire Safety Seminar Report',
    activity: 'Community Fire Safety Seminar',
    location: 'Barangay San Isidro',
    status: 'Submitted',
    date: 'September 5, 2026',
    content:
      'Community fire safety seminar conducted for residents of Barangay San Isidro.',
    remarks: ''
  },

  {
    id: 5,
    title: 'Emergency Response Drill Report',
    activity: 'Emergency Response Drill',
    location: 'Balingasag Municipal Hall',
    status: 'Pending',
    date: 'September 15, 2026',
    content: '',
    remarks: ''
  }
])


/* =========================================================
   FILTERS
========================================================= */

const searchQuery = ref('')
const statusFilter = ref('All')


/* =========================================================
   MODAL STATE
========================================================= */

const showFormModal = ref(false)
const showViewModal = ref(false)

const selectedReport = ref(null)
const editingReport = ref(null)


/* =========================================================
   FORM
========================================================= */

const emptyForm = () => ({
  title: '',
  activity: '',
  location: '',
  content: ''
})

const form = ref(emptyForm())


/* =========================================================
   TOAST
========================================================= */

const toastMessage = ref('')

let toastTimer = null

const showToast = (message) => {

  toastMessage.value = message

  clearTimeout(toastTimer)

  toastTimer = setTimeout(() => {
    toastMessage.value = ''
  }, 3000)
}


/* =========================================================
   STATISTICS
========================================================= */

const totalReports = computed(() => {
  return reports.value.length
})

const pendingReports = computed(() => {
  return reports.value.filter(
    report => report.status === 'Pending'
  ).length
})

const submittedReports = computed(() => {
  return reports.value.filter(
    report => report.status === 'Submitted'
  ).length
})

const returnedReports = computed(() => {
  return reports.value.filter(
    report => report.status === 'Returned'
  ).length
})


/* =========================================================
   FILTERED REPORTS
========================================================= */

const filteredReports = computed(() => {

  const query = searchQuery.value.trim().toLowerCase()

  return reports.value.filter(report => {

    const matchesSearch =
      !query ||
      report.title.toLowerCase().includes(query) ||
      report.activity.toLowerCase().includes(query) ||
      report.location.toLowerCase().includes(query)

    const matchesStatus =
      statusFilter.value === 'All' ||
      report.status === statusFilter.value

    return matchesSearch && matchesStatus
  })
})


/* =========================================================
   COMPLETION
========================================================= */

const completionRate = computed(() => {

  if (!totalReports.value) {
    return 0
  }

  return Math.round(
    (submittedReports.value / totalReports.value) * 100
  )
})

const completionMessage = computed(() => {

  if (completionRate.value >= 90) {
    return 'Excellent'
  }

  if (completionRate.value >= 80) {
    return 'Good standing'
  }

  if (completionRate.value >= 60) {
    return 'Needs improvement'
  }

  return 'Attention required'
})


/* =========================================================
   DEADLINES
========================================================= */

const deadlines = ref([
  {
    title: 'Fire Safety Inspection',
    date: 'Due September 12, 2026',
    label: 'Today',
    urgent: true
  },

  {
    title: 'Community Fire Safety Seminar',
    date: 'Due September 13, 2026',
    label: 'Sep 13',
    urgent: false
  },

  {
    title: 'Emergency Response Drill',
    date: 'Due September 15, 2026',
    label: 'Sep 15',
    urgent: false
  }
])


/* =========================================================
   RECENT ACTIVITY
========================================================= */

const recentActivity = ref([
  {
    id: 1,
    title: 'Report submitted',
    report: 'Routine Safety Patrol Report',
    date: 'September 7, 2026 · 03:25 PM',
    type: 'success'
  },

  {
    id: 2,
    title: 'Report returned',
    report: 'Fire Drill Monitoring Report',
    date: 'September 8, 2026 · 10:15 AM',
    type: 'returned'
  }
])


/* =========================================================
   FILTER RESET
========================================================= */

const resetFilters = () => {

  searchQuery.value = ''
  statusFilter.value = 'All'
}


/* =========================================================
   CREATE REPORT
========================================================= */

const openCreateModal = () => {

  editingReport.value = null
  form.value = emptyForm()

  showFormModal.value = true
}


/* =========================================================
   EDIT / REVISE
========================================================= */

const editReport = (report) => {

  editingReport.value = report

  form.value = {
    title: report.title,
    activity: report.activity,
    location: report.location,
    content: report.content || ''
  }

  showFormModal.value = true
}

const reviseReport = (report) => {

  editReport(report)
}


/* =========================================================
   CLOSE FORM
========================================================= */

const closeFormModal = () => {

  showFormModal.value = false
  editingReport.value = null
  form.value = emptyForm()
}


/* =========================================================
   SAVE REPORT
========================================================= */

const validateForm = () => {

  if (!form.value.title.trim()) {
    showToast('Report title is required.')
    return false
  }

  if (!form.value.activity) {
    showToast('Please select an activity.')
    return false
  }

  if (!form.value.location.trim()) {
    showToast('Location is required.')
    return false
  }

  if (!form.value.content.trim()) {
    showToast('Please enter report details.')
    return false
  }

  return true
}


const saveReport = () => {

  if (!validateForm()) {
    return
  }

  if (editingReport.value) {

    editingReport.value.title = form.value.title
    editingReport.value.activity = form.value.activity
    editingReport.value.location = form.value.location
    editingReport.value.content = form.value.content
    editingReport.value.status = 'Submitted'
    editingReport.value.remarks = ''

    showToast('Report updated and submitted.')

  } else {

    reports.value.unshift({
      id: Date.now(),
      title: form.value.title,
      activity: form.value.activity,
      location: form.value.location,
      status: 'Submitted',
      date: new Date().toLocaleDateString('en-US', {
        month: 'long',
        day: 'numeric',
        year: 'numeric'
      }),
      content: form.value.content,
      remarks: ''
    })

    showToast('Report created and submitted.')
  }

  closeFormModal()
}


/* =========================================================
   SAVE DRAFT
========================================================= */

const saveAsDraft = () => {

  if (!form.value.title.trim()) {
    showToast('Enter a report title first.')
    return
  }

  if (editingReport.value) {

    editingReport.value.title = form.value.title
    editingReport.value.activity = form.value.activity
    editingReport.value.location = form.value.location
    editingReport.value.content = form.value.content
    editingReport.value.status = 'Draft'

    showToast('Report saved as draft.')

  } else {

    reports.value.unshift({
      id: Date.now(),
      title: form.value.title,
      activity: form.value.activity || 'No activity selected',
      location: form.value.location || 'No location',
      status: 'Draft',
      date: 'Draft',
      content: form.value.content,
      remarks: ''
    })

    showToast('Report saved as draft.')
  }

  closeFormModal()
}


/* =========================================================
   SUBMIT REPORT
========================================================= */

const submitReport = (report) => {

  report.status = 'Submitted'

  report.date = new Date().toLocaleDateString('en-US', {
    month: 'long',
    day: 'numeric',
    year: 'numeric'
  })

  showToast(`${report.title} submitted successfully.`)
}


/* =========================================================
   VIEW REPORT
========================================================= */

const viewReport = (report) => {

  selectedReport.value = report
  showViewModal.value = true
}

const closeViewModal = () => {

  showViewModal.value = false
  selectedReport.value = null
}


/* =========================================================
   DELETE DRAFT
========================================================= */

const deleteDraft = (report) => {

  if (report.status !== 'Draft') {
    return
  }

  const confirmed = window.confirm(
    `Delete "${report.title}"?`
  )

  if (!confirmed) {
    return
  }

  reports.value = reports.value.filter(
    item => item.id !== report.id
  )

  showToast('Draft deleted.')
}


/* =========================================================
   STATUS STYLING
========================================================= */

const statusClass = (status) => {

  const classes = {

    Draft:
      'bg-slate-100 text-slate-700',

    Pending:
      'bg-yellow-100 text-yellow-700',

    Submitted:
      'bg-green-100 text-green-700',

    Returned:
      'bg-red-100 text-[#8B1E23]'
  }

  return classes[status] || 'bg-slate-100 text-slate-700'
}


/* =========================================================
   CARD STYLING
========================================================= */

const reportCardClass = (status) => {

  const classes = {

    Draft:
      'border-slate-200 bg-slate-50',

    Pending:
      'border-yellow-200 bg-yellow-50',

    Submitted:
      'border-green-200 bg-green-50',

    Returned:
      'border-red-200 bg-red-50'
  }

  return classes[status] || 'border-slate-200 bg-slate-50'
}


/* =========================================================
   ICON STYLING
========================================================= */

const reportIconClass = (status) => {

  const classes = {

    Draft:
      'bg-slate-100 text-slate-600',

    Pending:
      'bg-yellow-100 text-yellow-700',

    Submitted:
      'bg-green-100 text-green-600',

    Returned:
      'bg-red-100 text-[#8B1E23]'
  }

  return classes[status] || 'bg-slate-100 text-slate-600'
}


const reportIcon = (status) => {

  if (status === 'Submitted') {
    return ICONS.check
  }

  if (status === 'Returned') {
    return ICONS.siren
  }

  if (status === 'Pending') {
    return ICONS.clock
  }

  return ICONS.reports
}
</script>


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