<script setup>
defineProps({
  currentUser: {
    type: Object,
    default: null
  }
})
</script>

<template>
  <div class="space-y-6">
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
        <div>
          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">Records Management</p>
          <h2 class="text-2xl font-bold text-slate-900 mt-1">Report Management</h2>
          <p class="text-base text-slate-500 mt-1">Review, monitor, approve, and manage submitted operational reports.</p>
        </div>

        <button class="px-6 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition">
          + Create Report
        </button>
      </div>
    </section>

    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-slate-900">50</p>
        <p class="text-sm text-slate-500 mt-1">Total Reports</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">12</p>
        <p class="text-sm text-slate-500 mt-1">For Review</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">34</p>
        <p class="text-sm text-slate-500 mt-1">Approved</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">04</p>
        <p class="text-sm text-slate-500 mt-1">Rejected</p>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <input type="text" placeholder="Search report..." class="h-12 px-4 rounded-xl border border-slate-300 text-base" />
        <select class="h-12 px-4 rounded-xl border border-slate-300 text-base">
          <option>All Report Types</option>
          <option>Incident Report</option>
          <option>Inspection Report</option>
          <option>Accomplishment Report</option>
          <option>Activity Report</option>
        </select>
        <select class="h-12 px-4 rounded-xl border border-slate-300 text-base">
          <option>All Status</option>
          <option>For Review</option>
          <option>Approved</option>
          <option>Rejected</option>
          <option>Returned</option>
        </select>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="space-y-4">
        <div class="p-5 rounded-xl border border-slate-200 hover:bg-slate-50">
          <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
            <div>
              <div class="flex items-center gap-3 flex-wrap">
                <h3 class="text-lg font-bold text-slate-900">Fire Safety Inspection Report</h3>
                <span class="px-3 py-1 rounded-full bg-yellow-50 text-yellow-700 text-xs font-bold">FOR REVIEW</span>
              </div>
              <p class="text-sm text-slate-500 mt-2">Submitted by FO3 Juan Dela Cruz</p>
              <p class="text-sm text-slate-400 mt-1">Submitted September 9, 2026 • Report ID: REP-001</p>
            </div>

            <div class="flex gap-2">
              <button class="px-4 py-2.5 rounded-lg border border-slate-300 text-sm font-bold hover:bg-slate-100">View</button>
              <button class="px-4 py-2.5 rounded-lg bg-green-600 text-white text-sm font-bold hover:bg-green-700">Approve</button>
            </div>
          </div>
        </div>

        <div class="p-5 rounded-xl border border-slate-200 hover:bg-slate-50">
          <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
            <div>
              <div class="flex items-center gap-3 flex-wrap">
                <h3 class="text-lg font-bold text-slate-900">Weekly Accomplishment Report</h3>
                <span class="px-3 py-1 rounded-full bg-green-50 text-green-700 text-xs font-bold">APPROVED</span>
              </div>
              <p class="text-sm text-slate-500 mt-2">Submitted by SFO1 Maria Santos</p>
              <p class="text-sm text-slate-400 mt-1">Approved September 8, 2026 • Report ID: REP-002</p>
            </div>
            <button class="px-4 py-2.5 rounded-lg border border-slate-300 text-sm font-bold hover:bg-slate-100">View Report</button>
          </div>
        </div>

        <div class="p-5 rounded-xl border border-red-200 bg-red-50">
          <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
            <div>
              <div class="flex items-center gap-3 flex-wrap">
                <h3 class="text-lg font-bold text-slate-900">Fire Incident Report</h3>
                <span class="px-3 py-1 rounded-full bg-red-100 text-[#8B1E23] text-xs font-bold">OVERDUE</span>
              </div>
              <p class="text-sm text-slate-600 mt-2">Assigned to FO2 Roberto Reyes</p>
              <p class="text-sm text-[#8B1E23] mt-1">Deadline: September 9, 2026 • 8:00 PM</p>
            </div>
            <button class="px-4 py-2.5 rounded-lg bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]">Send Reminder</button>
          </div>
        </div>
      </div>
    </section>

    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Report Analytics</h2>
            <p class="text-sm text-slate-500 mt-1">Submission efficiency this month</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>On-Time Submission</span>
              <span>86%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[86%] rounded-full bg-green-500"></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Approval Rate</span>
              <span>68%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[68%] rounded-full bg-blue-500"></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Corrections Needed</span>
              <span>24%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[24%] rounded-full bg-yellow-500"></div>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Recently Uploaded Files</h2>
            <p class="text-sm text-slate-500 mt-1">Latest attachments and documents</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div class="flex items-center justify-between p-3 rounded-xl border border-slate-200 bg-slate-50">
            <div>
              <p class="text-sm font-bold text-slate-900">InspectionChecklist_Sept9.pdf</p>
              <p class="text-xs text-slate-500 mt-1">Uploaded by FO3 Juan Dela Cruz</p>
            </div>
            <span class="text-xs font-bold text-slate-500">PDF</span>
          </div>

          <div class="flex items-center justify-between p-3 rounded-xl border border-slate-200 bg-slate-50">
            <div>
              <p class="text-sm font-bold text-slate-900">BarangayDrillSummary.xlsx</p>
              <p class="text-xs text-slate-500 mt-1">Uploaded by FO2 Roberto Reyes</p>
            </div>
            <span class="text-xs font-bold text-slate-500">XLSX</span>
          </div>

          <div class="flex items-center justify-between p-3 rounded-xl border border-slate-200 bg-slate-50">
            <div>
              <p class="text-sm font-bold text-slate-900">IncidentPhotos_Set2.jpg</p>
              <p class="text-xs text-slate-500 mt-1">Uploaded by SFO1 Maria Santos</p>
            </div>
            <span class="text-xs font-bold text-slate-500">IMG</span>
          </div>
        </div>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex items-center justify-between border-b border-slate-200 pb-5">
        <div>
          <h2 class="text-xl font-bold text-slate-900">Review Notes</h2>
          <p class="text-sm text-slate-500 mt-1">Notes for report coordinators and approvers</p>
        </div>
      </div>

      <div class="mt-5 space-y-4">
        <div class="p-4 rounded-xl border border-red-200 bg-red-50">
          <p class="text-sm font-bold text-slate-900">Priority Reminder</p>
          <p class="text-sm text-slate-600 mt-1">Fire incident reports submitted after deadline require immediate supervisor review and follow-up.</p>
        </div>

        <div class="p-4 rounded-xl border border-amber-200 bg-amber-50">
          <p class="text-sm font-bold text-slate-900">Correction Needed</p>
          <p class="text-sm text-slate-600 mt-1">A few inspection reports are missing photographs; request resubmission before approval.</p>
        </div>

        <div class="p-4 rounded-xl border border-blue-200 bg-blue-50">
          <p class="text-sm font-bold text-slate-900">Documentation</p>
          <p class="text-sm text-slate-600 mt-1">Ensure all attachments are properly named and linked to the corresponding report ID.</p>
        </div>
      </div>
    </section>
  </div>
</template>
