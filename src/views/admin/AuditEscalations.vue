<template>
  <div class="space-y-6">
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
        <div>
          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">Governance Overview</p>
          <h2 class="text-2xl font-bold text-slate-900 mt-1">Audit &amp; Escalations</h2>
          <p class="text-base text-slate-500 mt-1">Review compliance checks, investigate findings, and monitor escalated cases.</p>
        </div>

        <button class="px-5 py-3 rounded-xl border border-slate-300 bg-white text-slate-700 font-bold hover:bg-slate-100 transition">
          Export Audit Report
        </button>
      </div>
    </section>

    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">18</p>
        <p class="text-sm text-slate-500 mt-1">Open Findings</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">06</p>
        <p class="text-sm text-slate-500 mt-1">Escalated</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">92%</p>
        <p class="text-sm text-slate-500 mt-1">Resolution Rate</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-blue-600">04</p>
        <p class="text-sm text-slate-500 mt-1">Pending Reviews</p>
      </div>
    </section>

    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Escalation Queue</h2>
            <p class="text-sm text-slate-500 mt-1">Cases requiring higher-level attention</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div class="p-4 rounded-xl border border-red-200 bg-red-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">Late Fire Incident Report</p>
                <p class="text-xs text-slate-500 mt-1">Assigned to FO3 Juan Dela Cruz • 2 hours overdue</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-red-100 text-[#8B1E23] text-xs font-bold">High</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-yellow-200 bg-yellow-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">Monthly Compliance Report</p>
                <p class="text-xs text-slate-500 mt-1">Pending review from Admin Office • 3 documents incomplete</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">Medium</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-blue-200 bg-blue-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">Barangay Drill Attendance Review</p>
                <p class="text-xs text-slate-500 mt-1">Awaiting validation of attendance logs and signatures</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">Low</span>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Audit Findings</h2>
            <p class="text-sm text-slate-500 mt-1">Recent compliance and operational observations</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-start gap-4">
              <div>
                <p class="text-sm font-bold text-slate-900">Documentation Gap</p>
                <p class="text-xs text-slate-500 mt-1">Two submitted reports were missing attachment references.</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">Review</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-start gap-4">
              <div>
                <p class="text-sm font-bold text-slate-900">Equipment Check Delay</p>
                <p class="text-xs text-slate-500 mt-1">One station missed its scheduled maintenance verification window.</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">Action</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-start gap-4">
              <div>
                <p class="text-sm font-bold text-slate-900">Training Completion</p>
                <p class="text-xs text-slate-500 mt-1">All new personnel completed required orientation modules.</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-green-100 text-green-700 text-xs font-bold">Resolved</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Performance Metrics</h2>
            <p class="text-sm text-slate-500 mt-1">Current audit score trends</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
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

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Action Notes</h2>
            <p class="text-sm text-slate-500 mt-1">Follow-up reminders for administrators</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div class="p-4 rounded-xl border border-emerald-200 bg-emerald-50">
            <p class="text-sm font-bold text-slate-900">Reminder</p>
            <p class="text-sm text-slate-600 mt-1">Ensure all stations attach supporting evidence before submitting monthly compliance reports.</p>
          </div>

          <div class="p-4 rounded-xl border border-orange-200 bg-orange-50">
            <p class="text-sm font-bold text-slate-900">Attention</p>
            <p class="text-sm text-slate-600 mt-1">Two delayed incident reports need closure notes and supervisor approval before end of day.</p>
          </div>

          <div class="p-4 rounded-xl border border-indigo-200 bg-indigo-50">
            <p class="text-sm font-bold text-slate-900">Follow-Up</p>
            <p class="text-sm text-slate-600 mt-1">Schedule a review meeting with Station Chiefs to address recurring documentation inconsistencies.</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
