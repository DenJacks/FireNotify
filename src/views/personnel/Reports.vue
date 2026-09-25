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
            View and submit reports assigned to you by the administrator.
          </p>
        </div>

        <div class="px-4 py-2 rounded-xl border border-slate-200 bg-slate-50 text-sm font-semibold text-slate-600">
          Assigned reports only
        </div>

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
              Assigned reports
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
              Waiting for review
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
            <option value="All">
              All Status
            </option>

            <option value="Draft">
              Draft
            </option>

            <option value="Pending">
              Pending
            </option>

            <option value="Pending Submission">
              Pending Submission
            </option>

            <option value="In Progress">
              In Progress
            </option>

            <option value="Submitted">
              Submitted
            </option>

            <option value="Returned">
              Returned
            </option>

            <option value="Approved">
              Approved
            </option>

            <option value="Rejected">
              Rejected
            </option>
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
              Assigned Reports
            </h3>

            <p class="text-sm text-slate-500 mt-1">
              Reports assigned to your account.
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
            No assigned reports
          </h4>

          <p class="text-sm text-slate-500 mt-1">
            Reports assigned to your account will appear here.
          </p>

        </div>


        <!-- LIST -->
        <div
          v-else
          class="mt-5 space-y-4"
        >

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


                <div class="min-w-0">

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
                    Activity:
                    <span class="font-semibold text-slate-700">
                      {{ report.activity || 'No activity specified' }}
                    </span>
                  </p>


                  <p class="text-sm text-slate-500 mt-1">
                    Location:
                    <span class="font-semibold text-slate-700">
                      {{ report.location || 'No location specified' }}
                    </span>
                  </p>


                  <p
                    v-if="report.assignedBy"
                    class="text-xs text-slate-400 mt-2"
                  >
                    Assigned by:
                    <span class="font-semibold text-slate-600">
                      {{ assignedPersonnelName(report.assignedBy) }}
                    </span>
                  </p>


                  <p
                    v-if="report.deadline"
                    class="text-xs text-slate-500 mt-2"
                  >
                    Deadline:
                    <span class="font-semibold">
                      {{ formatDate(report.deadline) }}
                    </span>
                  </p>


                  <p
                    v-if="
                      report.status === 'Pending' ||
                      report.status === 'Pending Submission' ||
                      report.status === 'Not Submitted'
                    "
                    class="text-xs text-yellow-700 font-semibold mt-2"
                  >
                    Action required — attach the completed report and submit it.
                  </p>


                  <p
                    v-if="report.status === 'In Progress'"
                    class="text-xs text-blue-700 font-semibold mt-2"
                  >
                    Report is currently in progress.
                  </p>


                  <p
                    v-if="report.status === 'Submitted'"
                    class="text-xs text-green-700 font-semibold mt-2"
                  >
                    ✓ Successfully submitted — waiting for administrator review.
                  </p>


                  <p
                    v-if="report.status === 'Returned'"
                    class="text-xs text-[#8B1E23] font-semibold mt-2"
                  >
                    Correction required — please revise the report.
                  </p>


                  <p
                    v-if="report.status === 'Approved'"
                    class="text-xs text-green-700 font-semibold mt-2"
                  >
                    ✓ Report approved by administrator.
                  </p>


                  <p
                    v-if="report.status === 'Rejected'"
                    class="text-xs text-red-700 font-semibold mt-2"
                  >
                    Report was rejected. Please review the remarks.
                  </p>

                </div>

              </div>

            </div>


            <!-- REMARKS -->
            <div
              v-if="report.remarks"
              class="mt-4 p-4 rounded-xl bg-white border border-red-200"
            >

              <p class="text-xs font-semibold text-slate-500 uppercase">
                Administrator Remarks
              </p>

              <p class="text-sm text-slate-700 mt-1">
                {{ report.remarks }}
              </p>

            </div>


            <!-- ACTIONS -->
            <div class="mt-4 flex flex-wrap gap-2">

              <!-- START LEGACY PERSONNEL REPORT -->
              <button
                v-if="
                  (report.status === 'Pending' && !report.assignedById)
                "
                @click="startReport(report)"
                class="px-4 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-semibold hover:bg-[#72181D]"
              >
                {{ report.status === 'Returned' ? 'Revise Report' : 'Start Report' }}
              </button>


              <!-- SUBMIT ASSIGNED REPORT -->
              <button
                v-if="
                  report.status === 'Pending' ||
                  report.status === 'Pending Submission' ||
                  report.status === 'Not Submitted' ||
                  report.status === 'In Progress' ||
                  report.status === 'Returned'
                "
                @click="submitReport(report)"
                class="px-4 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-semibold hover:bg-[#72181D]"
              >
                {{ report.status === 'Returned' ? 'Resubmit Report' : 'Submit Report' }}
              </button>


              <!-- DRAFT -->
              <button
                v-if="report.status === 'Draft'"
                @click="editReport(report)"
                class="px-4 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-semibold hover:bg-[#72181D]"
              >
                Continue Draft
              </button>


              <!-- VIEW -->
              <button
                v-if="
                  report.status === 'Submitted' ||
                  report.status === 'For Review' ||
                  report.status === 'Approved' ||
                  report.status === 'Rejected'
                "
                @click="viewReport(report)"
                class="px-4 py-2 rounded-lg border border-slate-300 bg-white text-slate-700 text-sm font-semibold hover:bg-slate-100"
              >
                View Report
              </button>


              <!-- DELETE DRAFT -->
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
                :class="
                  completionRate >= 80
                    ? 'text-green-600'
                    : 'text-yellow-600'
                "
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
              :key="deadline.id"
              class="p-4 rounded-xl border"
              :class="
                deadline.urgent
                  ? 'bg-yellow-50 border-yellow-200'
                  : 'bg-slate-50 border-slate-200'
              "
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
                  :class="
                    deadline.urgent
                      ? 'text-yellow-700'
                      : 'text-slate-500'
                  "
                >
                  {{ deadline.label }}
                </span>

              </div>

            </div>

          </div>

        </div>


        <!-- CURRENT USER -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <h3 class="text-lg font-bold text-slate-900">
            Current Account
          </h3>

          <div class="mt-5 p-4 rounded-xl bg-slate-50 border border-slate-200">

            <p class="text-sm font-bold text-slate-900">
              {{ currentUserName }}
            </p>

            <p class="text-xs text-slate-500 mt-1">
              {{ currentUserRole }}
            </p>

          </div>

        </div>

      </div>

    </section>


    <!-- ========================================================= -->
    <!-- CREATE / EDIT MODAL -->
    <!-- ========================================================= -->
    <div
      v-if="showFormModal"
      class="fixed inset-0 z-50 bg-slate-900/50 flex items-center justify-center p-4"
      @click.self="closeFormModal"
    >

      <div class="fn-modal-panel w-full max-w-2xl bg-white rounded-2xl shadow-xl overflow-hidden">

        <div class="px-6 py-5 border-b border-slate-200 flex items-center justify-between">

          <div>

            <p class="text-xs font-bold text-[#8B1E23] uppercase">
              Personnel Report
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
              <span class="text-[#8B1E23]">*</span>
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
              <span class="text-[#8B1E23]">*</span>
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
              <span class="text-[#8B1E23]">*</span>
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
              <span class="text-[#8B1E23]">*</span>
            </label>

            <textarea
              v-model="form.content"
              rows="5"
              placeholder="Enter accomplishment details, observations, findings, and actions taken..."
              class="w-full px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none resize-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/20"
            ></textarea>

          </div>

          <div>
            <label class="block text-sm font-semibold text-slate-700 mb-2">
              Attachment
            </label>

            <input
              type="file"
              accept=".pdf,.doc,.docx,.ppt,.pptx,application/pdf,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.ms-powerpoint,application/vnd.openxmlformats-officedocument.presentationml.presentation"
              @change="handleFileSelection"
              class="block w-full text-sm text-slate-600 file:mr-4 file:py-2.5 file:px-4 file:rounded-xl file:border-0 file:bg-[#8B1E23] file:text-white file:font-semibold file:hover:bg-[#72181D]"
            />

            <p class="text-xs text-slate-500 mt-2">
              Supported: PDF, DOC, DOCX, PPT, PPTX • Max 25MB
            </p>

            <div v-if="form.attachmentName" class="mt-3 flex items-center gap-3 rounded-xl border border-slate-200 bg-slate-50 px-3 py-2 text-sm text-slate-700">
              <span>📎</span>
              <span class="font-semibold truncate">{{ form.attachmentName }}</span>
            </div>
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
    <!-- VIEW MODAL -->
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
                {{ selectedReport.activity || 'No activity specified' }}
              </p>

            </div>


            <div class="p-4 rounded-xl bg-slate-50">

              <p class="text-xs text-slate-400 uppercase font-semibold">
                Location
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedReport.location || 'No location specified' }}
              </p>

            </div>

          </div>


          <div
            v-if="selectedReport.deadline"
            class="p-4 rounded-xl bg-yellow-50 border border-yellow-200"
          >

            <p class="text-xs text-yellow-700 uppercase font-semibold">
              Deadline
            </p>

            <p class="text-sm font-bold text-slate-900 mt-1">
              {{ formatDate(selectedReport.deadline) }}
            </p>

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
              Administrator Remarks
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
    <!-- REPORT SUBMISSION MODAL -->
    <!-- ========================================================= -->
    <div
      v-if="showSubmissionModal && submissionReport"
      class="fixed inset-0 z-[70] bg-slate-900/50 flex items-center justify-center p-4"
      @click.self="closeSubmitReportModal"
    >
      <div class="w-full max-w-lg bg-white rounded-2xl shadow-xl overflow-hidden">
        <div class="px-6 py-5 border-b border-slate-200 flex items-center justify-between">
          <div>
            <p class="text-xs font-bold text-[#8B1E23] uppercase">Report Submission</p>
            <h3 class="text-xl font-bold text-slate-900 mt-1">Submit Report</h3>
            <p class="text-sm text-slate-500 mt-1">{{ submissionReport.title }}</p>
          </div>
          <button
            @click="closeSubmitReportModal"
            class="h-10 w-10 rounded-xl hover:bg-slate-100 text-slate-500 text-xl"
          >
            ×
          </button>
        </div>

        <div class="p-6 space-y-5">
          <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
            <p class="text-sm text-slate-600">This action updates the existing assigned report and attaches the final file.</p>
          </div>

          <div>
            <label class="block text-sm font-semibold text-slate-700 mb-2">Supporting Document</label>
            <input
              type="file"
              accept=".pdf,.doc,.docx,.ppt,.pptx,application/pdf,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.ms-powerpoint,application/vnd.openxmlformats-officedocument.presentationml.presentation"
              @change="handleSubmissionFileSelection"
              class="block w-full text-sm text-slate-600 file:mr-4 file:py-2.5 file:px-4 file:rounded-xl file:border-0 file:bg-[#8B1E23] file:text-white file:font-semibold file:hover:bg-[#72181D]"
            />

            <div v-if="submissionFileName" class="mt-3 flex items-center gap-3 rounded-xl border border-slate-200 bg-slate-50 px-3 py-2 text-sm text-slate-700">
              <span>📎</span>
              <span class="font-semibold truncate">{{ submissionFileName }}</span>
            </div>
          </div>

          <div class="flex flex-col sm:flex-row justify-end gap-3 pt-2">
            <button
              type="button"
              @click="closeSubmitReportModal"
              class="px-5 py-2.5 rounded-xl border border-slate-300 bg-white text-slate-700 text-sm font-bold hover:bg-slate-100"
            >
              Cancel
            </button>

            <button
              type="button"
              @click="submitAssignedReport"
              :disabled="!selectedSubmissionFile"
              class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D] disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Submit Report
            </button>
          </div>
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
import {
  computed,
  ref,
  onMounted,
  onUnmounted
} from 'vue'
import {
  saveReportFile,
  getReportFile,
  deleteReportFile
} from '../../utils/reportFileStorage.js'
import { resolvePersonnelName } from '../../utils/personnelName.js'


/* =========================================================
   PROPS
========================================================= */

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


const ICONS = props.ICONS

const assignedPersonnelName = value => resolvePersonnelName(
  value,
  props.registeredUsers,
  typeof value === 'string' && ['admin', 'administrator'].includes(value.trim().toLowerCase())
    ? value
    : 'Personnel unavailable'
)


/* =========================================================
   STORAGE
========================================================= */

const REPORT_STORAGE_KEY = 'firenotify_reports'
const MAX_FILE_SIZE = 25 * 1024 * 1024
const SUPPORTED_FILE_TYPES = [
  'application/pdf',
  'application/msword',
  'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  'application/vnd.ms-powerpoint',
  'application/vnd.openxmlformats-officedocument.presentationml.presentation'
]
const SUPPORTED_EXTENSIONS = ['pdf', 'doc', 'docx', 'ppt', 'pptx']

/* =========================================================
   CURRENT USER
========================================================= */

const getCurrentUser = () => {

  if (props.currentUser) {
    return props.currentUser
  }

  try {

    return JSON.parse(
      localStorage.getItem('currentUser') || 'null'
    )

  } catch {

    return null

  }
}


const currentUserName = computed(() => {

  const user = getCurrentUser()

  if (!user) {
    return 'Personnel'
  }

  return (
    user.name ||
    `${user.firstName || ''} ${user.lastName || ''}`.trim() ||
    user.username ||
    user.identifier ||
    'Personnel'
  )
})


const currentUserRole = computed(() => {

  const user = getCurrentUser()

  return (
    user?.position ||
    user?.rank ||
    'Fire Personnel'
  )
})


/* =========================================================
   REPORT DATA
========================================================= */

const reports = ref([])


/* =========================================================
   LOAD REPORTS
========================================================= */

const loadReports = () => {

  const user = getCurrentUser()

  if (!user) {

    reports.value = []

    return

  }


  let storedReports = []

  try {

    storedReports = JSON.parse(
      localStorage.getItem(REPORT_STORAGE_KEY) || '[]'
    )

  } catch {

    storedReports = []

  }


  const currentUserId = String(
    user.id || ''
  )


  const currentUsername =
    user.username ||
    user.identifier ||
    ''


  const currentEmail =
    user.email ||
    user.identifier ||
    ''


  reports.value = storedReports.filter(report => {

    const assignedId =
      String(report.assignedToId || '')

    const assignedUsername =
      report.assignedToUsername || ''

    const assignedEmail =
      report.assignedToEmail || ''


    return (

      (
        currentUserId &&
        assignedId &&
        assignedId === currentUserId
      )

      ||

      (
        currentUsername &&
        assignedUsername &&
        assignedUsername === currentUsername
      )

      ||

      (
        currentEmail &&
        assignedEmail &&
        assignedEmail === currentEmail
      )

    )

  })

}


/* =========================================================
   SYNC
========================================================= */

onMounted(() => {

  loadReports()


  window.addEventListener(
    'storage',
    loadReports
  )


  window.addEventListener(
    'fireNotifyReportsUpdated',
    loadReports
  )


  window.addEventListener(
    'focus',
    loadReports
  )

})


onUnmounted(() => {

  window.removeEventListener(
    'storage',
    loadReports
  )


  window.removeEventListener(
    'fireNotifyReportsUpdated',
    loadReports
  )


  window.removeEventListener(
    'focus',
    loadReports
  )

})


/* =========================================================
   FILTERS
========================================================= */

const searchQuery = ref('')

const statusFilter = ref('All')


/* =========================================================
   MODAL STATE
========================================================= */

const showFormModal = ref(false)
const showSubmissionModal = ref(false)

const showViewModal = ref(false)

const selectedReport = ref(null)
const submissionReport = ref(null)
const selectedSubmissionFile = ref(null)
const submissionFileName = ref('')

const editingReport = ref(null)


/* =========================================================
   FORM
========================================================= */

const emptyForm = () => ({
  title: '',
  activity: '',
  location: '',
  content: '',
  attachmentFile: null,
  attachmentName: ''
})


const form = ref(emptyForm())
const selectedReportFile = ref(null)


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
   SAVE STORAGE
========================================================= */

const saveReports = () => {

  localStorage.setItem(
    REPORT_STORAGE_KEY,
    JSON.stringify(reports.value)
  )

  window.dispatchEvent(
    new Event('fireNotifyReportsUpdated')
  )

}


/* =========================================================
   STATISTICS
========================================================= */

const totalReports = computed(() => {

  return reports.value.length

})


const pendingReports = computed(() => {

  return reports.value.filter(
    report =>
      report.status === 'Pending' ||
      report.status === 'Pending Submission' ||
      report.status === 'Not Submitted' ||
      report.status === 'Draft'
  ).length

})


const submittedReports = computed(() => {

  return reports.value.filter(
    report =>
      report.status === 'Submitted' ||
      report.status === 'Approved'
  ).length

})


const returnedReports = computed(() => {

  return reports.value.filter(
    report =>
      report.status === 'Returned'
  ).length

})


/* =========================================================
   FILTERED REPORTS
========================================================= */

const filteredReports = computed(() => {

  const query =
    searchQuery.value.trim().toLowerCase()


  return reports.value.filter(report => {

    const title =
      String(report.title || '').toLowerCase()

    const activity =
      String(report.activity || '').toLowerCase()

    const location =
      String(report.location || '').toLowerCase()


    const matchesSearch =
      !query ||
      title.includes(query) ||
      activity.includes(query) ||
      location.includes(query)


    const matchesStatus =
      statusFilter.value === 'All' ||
      report.status === statusFilter.value


    return (
      matchesSearch &&
      matchesStatus
    )

  })

})


/* =========================================================
   COMPLETION
========================================================= */

const completionRate = computed(() => {

  if (!totalReports.value) {
    return 0
  }


  const completed =
    reports.value.filter(
      report =>
        report.status === 'Submitted' ||
        report.status === 'Approved'
    ).length


  return Math.round(
    (completed / totalReports.value) * 100
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

const deadlines = computed(() => {

  return reports.value

    .filter(report => {

      return (
        report.deadline &&
        report.status !== 'Approved'
      )

    })

    .sort((a, b) => {

      return new Date(a.deadline) -
        new Date(b.deadline)

    })

    .slice(0, 5)

    .map(report => {

      const deadline =
        new Date(report.deadline)

      const now =
        new Date()

      const difference =
        Math.ceil(
          (
            deadline - now
          ) /
          (
            1000 *
            60 *
            60 *
            24
          )
        )


      return {

        id: report.id,

        title: report.title,

        date:
          `Due ${formatDate(report.deadline)}`,

        label:
          difference <= 0
            ? 'Overdue'
            : difference === 1
              ? 'Tomorrow'
              : `${difference} days`,

        urgent:
          difference <= 2

      }

    })

})


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
  showToast('Assigned reports are submitted from the report card itself.')
}


/* =========================================================
   EDIT REPORT
========================================================= */

const editReport = (report) => {

  editingReport.value = report

  form.value = {

    title:
      report.title || '',

    activity:
      report.activity || '',

    location:
      report.location || '',

    content:
      report.content || ''

  }


  showFormModal.value = true

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
   VALIDATE
========================================================= */

const getFileExtension = fileName => {
  const value = String(fileName || '').split('.').pop()?.toLowerCase() || ''
  return value
}

const isSupportedAttachment = file => {
  if (!file) return { valid: false, message: 'Please select a file.' }

  const name = String(file.name || '')
  const extension = getFileExtension(name)
  const mimeType = String(file.type || '').toLowerCase()
  const hasSupportedExtension = SUPPORTED_EXTENSIONS.includes(extension)
  const hasSupportedMime = SUPPORTED_FILE_TYPES.includes(mimeType)

  if (!hasSupportedExtension && !hasSupportedMime) {
    return {
      valid: false,
      message: 'Unsupported file type. Please attach a PDF, Word, or PowerPoint file.'
    }
  }

  if (file.size > MAX_FILE_SIZE) {
    return {
      valid: false,
      message: 'File is too large. Maximum supported size is 25MB.'
    }
  }

  return { valid: true }
}

const handleFileSelection = event => {
  const file = event?.target?.files?.[0]

  if (!file) {
    selectedReportFile.value = null
    form.value.attachmentFile = null
    form.value.attachmentName = ''
    return
  }

  const validation = isSupportedAttachment(file)

  if (!validation.valid) {
    showToast(validation.message)
    event.target.value = ''
    selectedReportFile.value = null
    form.value.attachmentFile = null
    form.value.attachmentName = ''
    return
  }

  selectedReportFile.value = file
  form.value.attachmentFile = file
  form.value.attachmentName = file.name
}

const addReportNotification = (report) => {
  try {
    const notificationKey = 'firenotify_notifications'
    const current = JSON.parse(localStorage.getItem(notificationKey) || '[]')
    const payload = {
      id: `notif-${Date.now()}`,
      title: 'New report submitted',
      detail: `${report.submittedBy || currentUserName.value} submitted a new report: ${report.title}`,
      type: 'Reports & Compliance',
      tone: 'blue',
      status: 'unread',
      read: false,
      createdAt: new Date().toISOString(),
      assignedToId: report.assignedById || 'admin-default',
      assignedToName: 'Administrator',
      personnelName: report.submittedBy || currentUserName.value
    }

    const next = [payload, ...Array.isArray(current) ? current : []]
    localStorage.setItem(notificationKey, JSON.stringify(next))
    window.dispatchEvent(new CustomEvent('fireNotifyNotificationsUpdated'))
  } catch (error) {
    console.warn('FireNotify: unable to save report notification', error)
  }
}

const persistReportAttachment = async report => {
  if (!form.value.attachmentFile) {
    return report
  }

  const validation = isSupportedAttachment(form.value.attachmentFile)
  if (!validation.valid) {
    throw new Error(validation.message)
  }

  const savedFile = await saveReportFile({
    reportId: report.id,
    id: report.id,
    file: form.value.attachmentFile,
    filename: form.value.attachmentFile.name,
    mimeType: form.value.attachmentFile.type || 'application/octet-stream',
    size: form.value.attachmentFile.size,
    createdAt: new Date().toISOString()
  })

  if (savedFile) {
    report.fileStored = true
    report.fileReferenceId = report.id
    report.filename = form.value.attachmentFile.name
    report.fileType = form.value.attachmentFile.type || 'application/octet-stream'
    report.fileSize = form.value.attachmentFile.size
    report.attachment = form.value.attachmentFile.name
    report.attachmentStored = true
  }

  return report
}

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

  if (form.value.attachmentFile) {
    const validation = isSupportedAttachment(form.value.attachmentFile)
    if (!validation.valid) {
      showToast(validation.message)
      return false
    }
  }

  return true
}

const openSubmitReport = report => {
  selectedSubmissionFile.value = null
  submissionFileName.value = ''
  submissionReport.value = report
  showSubmissionModal.value = true
}

const closeSubmitReportModal = () => {
  showSubmissionModal.value = false
  submissionReport.value = null
  selectedSubmissionFile.value = null
  submissionFileName.value = ''
}

const handleSubmissionFileSelection = event => {
  const file = event?.target?.files?.[0]
  if (!file) {
    selectedSubmissionFile.value = null
    submissionFileName.value = ''
    return
  }

  const validation = isSupportedAttachment(file)
  if (!validation.valid) {
    showToast(validation.message)
    event.target.value = ''
    selectedSubmissionFile.value = null
    submissionFileName.value = ''
    return
  }

  selectedSubmissionFile.value = file
  submissionFileName.value = file.name
}


/* =========================================================
   SAVE REPORT
========================================================= */

const finalizeReportSubmission = async () => {
  if (!submissionReport.value) {
    return
  }

  if (!selectedSubmissionFile.value) {
    showToast('Please choose a file before submitting.')
    return
  }

  const validation = isSupportedAttachment(selectedSubmissionFile.value)
  if (!validation.valid) {
    showToast(validation.message)
    return
  }

  const user = getCurrentUser()
  if (!user) {
    showToast('No active personnel account was found.', 'error')
    return
  }

  const index = reports.value.findIndex(item => item.id === submissionReport.value.id)
  if (index === -1) {
    showToast('The selected assigned report could not be found.', 'error')
    return
  }

  const report = reports.value[index]

  try {
    const savedFile = await saveReportFile({
      reportId: report.id,
      id: report.id,
      file: selectedSubmissionFile.value,
      filename: selectedSubmissionFile.value.name,
      mimeType: selectedSubmissionFile.value.type || 'application/octet-stream',
      size: selectedSubmissionFile.value.size,
      createdAt: new Date().toISOString()
    })

    if (!savedFile) {
      showToast('Unable to save the selected file in this browser.', 'error')
      return
    }
  } catch (error) {
    console.error('FireNotify: report upload failed', error)
    showToast('Unable to save the selected file in this browser.', 'error')
    return
  }

  reports.value[index] = {
    ...report,
    status: 'Submitted',
    submissionStatus: 'Submitted',
    submittedAt: new Date().toISOString(),
    submittedDate: new Date().toLocaleDateString('en-US', {
      month: 'long',
      day: 'numeric',
      year: 'numeric'
    }),
    submittedBy: currentUserName.value,
    submittedById: user.id || user.identifier || '',
    filename: selectedSubmissionFile.value.name,
    fileType: selectedSubmissionFile.value.type || 'application/octet-stream',
    fileSize: selectedSubmissionFile.value.size,
    fileStored: true,
    fileReferenceId: report.id,
    attachment: selectedSubmissionFile.value.name,
    attachmentStored: true
  }

  saveReports()
  addReportNotification(reports.value[index])
  closeSubmitReportModal()
  showToast('Report submitted successfully.')
}

const saveReport = () => {

  if (!validateForm()) {
    return
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

        title:
          form.value.title,

        activity:
          form.value.activity,

        location:
          form.value.location,

        content:
          form.value.content,

        status:
          'Submitted',

        submittedAt:
          new Date().toISOString(),

        submittedDate:
          new Date().toLocaleDateString(
            'en-US',
            {
              month: 'long',
              day: 'numeric',
              year: 'numeric'
            }
          )

      }

    }


    saveReports()

    showToast(
      'Report updated and submitted.'
    )

  } else {

    const user =
      getCurrentUser()


    const newReport = {

      id:
        `REP-${Date.now()}-${Math.random()
          .toString(36)
          .slice(2, 7)}`,

      title:
        form.value.title,

      activity:
        form.value.activity,

      location:
        form.value.location,

      content:
        form.value.content,

      assignedToId:
        user?.id || '',

      assignedToUsername:
        user?.username ||
        user?.identifier ||
        '',

      assignedToName:
        currentUserName.value,

      assignedToEmail:
        user?.email ||
        user?.identifier ||
        '',

      assignedById:
        'personnel-self',

      assignedBy:
        currentUserName.value,

      status:
        'Submitted',

      date:
        new Date().toLocaleDateString(
          'en-US',
          {
            month: 'long',
            day: 'numeric',
            year: 'numeric'
          }
        ),

      submittedAt:
        new Date().toISOString(),

      submittedBy:
        currentUserName.value,

      remarks:
        '',

      createdAt:
        new Date().toISOString()

    }


    reports.value.unshift(
      newReport
    )


    saveReports()


    showToast(
      'Report created and submitted.'
    )

  }


  closeFormModal()

}


/* =========================================================
   SAVE DRAFT
========================================================= */

const saveAsDraft = async () => {

  if (!form.value.title.trim()) {

    showToast(
      'Enter a report title first.'
    )

    return

  }


  const user =
    getCurrentUser()


  if (editingReport.value) {

    const index =
      reports.value.findIndex(
        report =>
          report.id ===
          editingReport.value.id
      )


    if (index !== -1) {
      const nextReport = {
        ...reports.value[index],
        title: form.value.title,
        activity: form.value.activity,
        location: form.value.location,
        content: form.value.content,
        status: 'Draft'
      }

      if (form.value.attachmentFile) {
        try {
          await persistReportAttachment(nextReport)
        } catch (error) {
          showToast(error.message || 'Unable to attach file.')
          return
        }
      }

      reports.value[index] = nextReport
    }


    saveReports()

    showToast(
      'Report saved as draft.'
    )

  } else {

    const draftReport = {
      id: `REP-${Date.now()}-${Math.random().toString(36).slice(2, 7)}`,
      title: form.value.title,
      activity: form.value.activity || 'No activity selected',
      location: form.value.location || 'No location',
      content: form.value.content,
      assignedToId: user?.id || '',
      assignedToUsername: user?.username || user?.identifier || '',
      assignedToName: currentUserName.value,
      assignedToEmail: user?.email || user?.identifier || '',
      assignedBy: currentUserName.value,
      status: 'Draft',
      date: 'Draft',
      remarks: '',
      createdAt: new Date().toISOString()
    }

    try {
      await persistReportAttachment(draftReport)
    } catch (error) {
      showToast(error.message || 'Unable to attach file.')
      return
    }

    reports.value.unshift(draftReport)

    saveReports()

    showToast(
      'Report saved as draft.'
    )

  }


  closeFormModal()

}


/* =========================================================
   START REPORT
========================================================= */

const startReport = (report) => {

  const index =
    reports.value.findIndex(
      item =>
        item.id === report.id
    )


  if (index === -1) {
    return
  }


  reports.value[index] = {

    ...reports.value[index],

    status:
      'In Progress',

    progress:
      10,

    startedAt:
      new Date().toISOString(),

    remarks:
      ''

  }


  saveReports()


  showToast(
    `${report.title} started.`
  )

}


/* =========================================================
   SUBMIT REPORT
========================================================= */

const submitReport = (report) => {

  openSubmitReport(report)
}


/* =========================================================
   SUBMISSION MODAL
========================================================= */

const submitAssignedReport = async () => {
  await finalizeReportSubmission()
}


/* =========================================================
   VIEW REPORT
========================================================= */

const viewReport = (report) => {

  selectedReport.value =
    report

  showViewModal.value =
    true

}


const closeViewModal = () => {

  showViewModal.value =
    false

  selectedReport.value =
    null

}


/* =========================================================
   DELETE DRAFT
========================================================= */

const deleteDraft = (report) => {

  if (report.status !== 'Draft') {
    return
  }


  const confirmed =
    window.confirm(
      `Delete "${report.title}"?`
    )


  if (!confirmed) {
    return
  }


  reports.value =
    reports.value.filter(
      item =>
        item.id !== report.id
    )


  saveReports()


  showToast(
    'Draft deleted.'
  )

}


/* =========================================================
   DATE FORMAT
========================================================= */

const formatDate = (date) => {

  if (!date) {
    return 'No deadline'
  }


  const parsed =
    new Date(date)


  if (Number.isNaN(parsed.getTime())) {
    return date
  }


  return parsed.toLocaleDateString(
    'en-US',
    {
      month: 'long',
      day: 'numeric',
      year: 'numeric'
    }
  )

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

    'Pending Submission':
      'bg-yellow-100 text-yellow-700',

    'Not Submitted':
      'bg-yellow-100 text-yellow-700',

    'In Progress':
      'bg-blue-100 text-blue-700',

    Submitted:
      'bg-green-100 text-green-700',

    Returned:
      'bg-red-100 text-[#8B1E23]',

    Approved:
      'bg-green-100 text-green-700',

    Rejected:
      'bg-red-100 text-red-700'

  }


  return (
    classes[status] ||
    'bg-slate-100 text-slate-700'
  )

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

    'In Progress':
      'border-blue-200 bg-blue-50',

    Submitted:
      'border-green-200 bg-green-50',

    Returned:
      'border-red-200 bg-red-50',

    Approved:
      'border-green-200 bg-green-50',

    Rejected:
      'border-red-200 bg-red-50'

  }


  return (
    classes[status] ||
    'border-slate-200 bg-slate-50'
  )

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

    'In Progress':
      'bg-blue-100 text-blue-700',

    Submitted:
      'bg-green-100 text-green-600',

    Returned:
      'bg-red-100 text-[#8B1E23]',

    Approved:
      'bg-green-100 text-green-600',

    Rejected:
      'bg-red-100 text-red-600'

  }


  return (
    classes[status] ||
    'bg-slate-100 text-slate-600'
  )

}


const reportIcon = (status) => {

  if (
    status === 'Submitted' ||
    status === 'Approved'
  ) {

    return ICONS.check

  }


  if (
    status === 'Returned' ||
    status === 'Rejected'
  ) {

    return ICONS.siren

  }


  if (
    status === 'Pending'
  ) {

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