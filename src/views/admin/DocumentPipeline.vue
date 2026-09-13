<template>
  <div class="space-y-6">
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
        <div>
          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">Document Flow</p>
          <h2 class="text-2xl font-bold text-slate-900 mt-1">Document Pipeline</h2>
          <p class="text-base text-slate-500 mt-1">Track paperwork from submission to approval, archiving, and retrieval.</p>
        </div>

        <button class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition">
          + New Document
        </button>
      </div>
    </section>

    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">142</p>
        <p class="text-sm text-slate-500 mt-1">Total Docs</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-blue-600">48</p>
        <p class="text-sm text-slate-500 mt-1">In Review</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">71</p>
        <p class="text-sm text-slate-500 mt-1">Approved</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">23</p>
        <p class="text-sm text-slate-500 mt-1">Needs Action</p>
      </div>
    </section>

    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Pipeline Stages</h2>
            <p class="text-sm text-slate-500 mt-1">Current volume across document states</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Submitted</p>
                <p class="text-xs text-slate-500 mt-1">Ready for administrative review</p>
              </div>
              <span class="text-sm font-bold text-slate-700">34</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">In Review</p>
                <p class="text-xs text-slate-500 mt-1">Evaluated by the admin office</p>
              </div>
              <span class="text-sm font-bold text-blue-600">48</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Approved</p>
                <p class="text-xs text-slate-500 mt-1">Archived and available for retrieval</p>
              </div>
              <span class="text-sm font-bold text-green-600">71</span>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Recent Activity</h2>
            <p class="text-sm text-slate-500 mt-1">Latest updates in the document pipeline</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div class="p-4 rounded-xl border border-emerald-200 bg-emerald-50">
            <p class="text-sm font-bold text-slate-900">Report Approved</p>
            <p class="text-sm text-slate-600 mt-1">After-Operation Fire Incident Report was approved and archived.</p>
          </div>

          <div class="p-4 rounded-xl border border-blue-200 bg-blue-50">
            <p class="text-sm font-bold text-slate-900">Revision Requested</p>
            <p class="text-sm text-slate-600 mt-1">Quarterly Establishment Inspection needs updated attachments.</p>
          </div>

          <div class="p-4 rounded-xl border border-amber-200 bg-amber-50">
            <p class="text-sm font-bold text-slate-900">Awaiting Signature</p>
            <p class="text-sm text-slate-600 mt-1">Barangay Drill Attendance Sheet is pending final signature from the station chief.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex items-center justify-between border-b border-slate-200 pb-5">
        <div>
          <h2 class="text-xl font-bold text-slate-900">Document Queue</h2>
          <p class="text-sm text-slate-500 mt-1">Pending and recently updated documents</p>
        </div>
      </div>

      <div class="mt-5 overflow-x-auto">
        <table class="min-w-full border-separate border-spacing-y-3">
          <thead>
            <tr class="text-left text-xs font-bold uppercase tracking-wide text-slate-500">
              <th class="pb-2 pr-4">Document</th>
              <th class="pb-2 pr-4">Submitted By</th>
              <th class="pb-2 pr-4">Date</th>
              <th class="pb-2">Stage</th>
            </tr>
          </thead>

          <tbody>
            <tr class="bg-slate-50 rounded-xl">
              <td class="py-4 pr-4 font-semibold text-slate-900 rounded-l-xl">After-Operation Fire Incident Report</td>
              <td class="py-4 pr-4 text-slate-600">SFO1 M. Santos</td>
              <td class="py-4 pr-4 text-slate-600">Aug 12, 2026</td>
              <td class="py-4 pr-4"><span class="px-3 py-1 rounded-full bg-green-100 text-green-700 text-xs font-bold">Approved</span></td>
            </tr>

            <tr class="bg-slate-50 rounded-xl">
              <td class="py-4 pr-4 font-semibold text-slate-900 rounded-l-xl">Quarterly Establishment Inspection</td>
              <td class="py-4 pr-4 text-slate-600">FO3 J. Dela Cruz</td>
              <td class="py-4 pr-4 text-slate-600">Aug 15, 2026</td>
              <td class="py-4 pr-4"><span class="px-3 py-1 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">Revision</span></td>
            </tr>

            <tr class="bg-slate-50 rounded-xl">
              <td class="py-4 pr-4 font-semibold text-slate-900 rounded-l-xl">Barangay Drill Attendance Sheet</td>
              <td class="py-4 pr-4 text-slate-600">SFO2 R. Garcia</td>
              <td class="py-4 pr-4 text-slate-600">Aug 18, 2026</td>
              <td class="py-4 pr-4"><span class="px-3 py-1 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">In Review</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  </div>
</template>
