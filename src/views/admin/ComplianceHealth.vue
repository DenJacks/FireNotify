<template>
  <div class="space-y-6">
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
        <div>
          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">Operational Health</p>
          <h2 class="text-2xl font-bold text-slate-900 mt-1">Compliance Health</h2>
          <p class="text-base text-slate-500 mt-1">Monitor station compliance, review health indicators, and track corrective actions.</p>
        </div>

        <button class="px-5 py-3 rounded-xl border border-slate-300 bg-white text-slate-700 font-bold hover:bg-slate-100 transition">
          View Full Report
        </button>
      </div>
    </section>

    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">94.5%</p>
        <p class="text-sm text-slate-500 mt-1">Overall Health</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">07</p>
        <p class="text-sm text-slate-500 mt-1">Good Standing</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">02</p>
        <p class="text-sm text-slate-500 mt-1">Needs Attention</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-blue-600">89%</p>
        <p class="text-sm text-slate-500 mt-1">Deadline Adherence</p>
      </div>
    </section>

    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Station Compliance Snapshot</h2>
            <p class="text-sm text-slate-500 mt-1">Performance of each station and unit</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Station 1</p>
                <p class="text-xs text-slate-500 mt-1">Submission quality and adherence</p>
              </div>
              <span class="text-sm font-bold text-green-600">95%</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Station 2</p>
                <p class="text-xs text-slate-500 mt-1">Equipment checks and reporting</p>
              </div>
              <span class="text-sm font-bold text-yellow-600">82%</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Station 3</p>
                <p class="text-xs text-slate-500 mt-1">Documentation completeness</p>
              </div>
              <span class="text-sm font-bold text-green-600">91%</span>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Standards Check Status</h2>
            <p class="text-sm text-slate-500 mt-1">Current compliance checklist progress</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Daily Logs</span>
              <span>98%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[98%] rounded-full bg-emerald-500"></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Equipment Verification</span>
              <span>87%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[87%] rounded-full bg-blue-500"></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Attachment Completeness</span>
              <span>84%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[84%] rounded-full bg-yellow-500"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Risk Areas</h2>
            <p class="text-sm text-slate-500 mt-1">Potential gaps affecting compliance</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div class="p-4 rounded-xl border border-red-200 bg-red-50">
            <p class="text-sm font-bold text-slate-900">Delayed Report Submission</p>
            <p class="text-sm text-slate-600 mt-1">Two station reports remain unsubmitted beyond target deadlines.</p>
          </div>

          <div class="p-4 rounded-xl border border-yellow-200 bg-yellow-50">
            <p class="text-sm font-bold text-slate-900">Incomplete Attachments</p>
            <p class="text-sm text-slate-600 mt-1">Several reports lack required photos, signatures, or supporting documents.</p>
          </div>

          <div class="p-4 rounded-xl border border-blue-200 bg-blue-50">
            <p class="text-sm font-bold text-slate-900">Equipment Verification Window</p>
            <p class="text-sm text-slate-600 mt-1">One station missed a scheduled maintenance verification audit this cycle.</p>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Remediation Plan</h2>
            <p class="text-sm text-slate-500 mt-1">Immediate steps to improve health scores</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div class="p-4 rounded-xl border border-emerald-200 bg-emerald-50">
            <p class="text-sm font-bold text-slate-900">Priority 1</p>
            <p class="text-sm text-slate-600 mt-1">Complete all overdue reports and apply review notes before end of day.</p>
          </div>

          <div class="p-4 rounded-xl border border-orange-200 bg-orange-50">
            <p class="text-sm font-bold text-slate-900">Priority 2</p>
            <p class="text-sm text-slate-600 mt-1">Reconcile missing attachments and require station-level verification before submission.</p>
          </div>

          <div class="p-4 rounded-xl border border-indigo-200 bg-indigo-50">
            <p class="text-sm font-bold text-slate-900">Priority 3</p>
            <p class="text-sm text-slate-600 mt-1">Reschedule equipment verification for the affected station and document corrective action.</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
