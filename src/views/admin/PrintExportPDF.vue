<template>
  <div class="space-y-6">
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
        <div>
          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">Administrative Tools</p>
          <h2 class="text-2xl font-bold text-slate-900 mt-1">Print &amp; Export PDF</h2>
          <p class="text-base text-slate-500 mt-1">Generate formatted reports, share summaries, and export records for documentation.</p>
        </div>

        <button class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition">
          Create PDF Export
        </button>
      </div>
    </section>

    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">06</p>
        <p class="text-sm text-slate-500 mt-1">Available Templates</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-blue-600">12</p>
        <p class="text-sm text-slate-500 mt-1">This Month</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">08</p>
        <p class="text-sm text-slate-500 mt-1">Generated</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">04</p>
        <p class="text-sm text-slate-500 mt-1">Pending</p>
      </div>
    </section>

    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Export Templates</h2>
            <p class="text-sm text-slate-500 mt-1">Quick formatting options for common reports</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Incident Summary Report</p>
                <p class="text-xs text-slate-500 mt-1">Standard BFP incident summary layout</p>
              </div>
              <button class="text-sm font-bold text-[#8B1E23]">Export</button>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Personnel Roster</p>
                <p class="text-xs text-slate-500 mt-1">Structured staff roster for station operations</p>
              </div>
              <button class="text-sm font-bold text-[#8B1E23]">Export</button>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Compliance Audit Pack</p>
                <p class="text-xs text-slate-500 mt-1">Detailed compliance and escalation results</p>
              </div>
              <button class="text-sm font-bold text-[#8B1E23]">Export</button>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Recent Exports</h2>
            <p class="text-sm text-slate-500 mt-1">Latest generated PDFs and print requests</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div class="p-4 rounded-xl border border-emerald-200 bg-emerald-50">
            <p class="text-sm font-bold text-slate-900">Weekly Compliance Summary</p>
            <p class="text-sm text-slate-600 mt-1">Generated successfully on Aug 18, 2026.</p>
          </div>

          <div class="p-4 rounded-xl border border-blue-200 bg-blue-50">
            <p class="text-sm font-bold text-slate-900">Station Duty Log</p>
            <p class="text-sm text-slate-600 mt-1">Generated successfully on Aug 17, 2026.</p>
          </div>

          <div class="p-4 rounded-xl border border-amber-200 bg-amber-50">
            <p class="text-sm font-bold text-slate-900">Equipment Audit Report</p>
            <p class="text-sm text-slate-600 mt-1">Queued for deliverable approval.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex items-center justify-between border-b border-slate-200 pb-5">
        <div>
          <h2 class="text-xl font-bold text-slate-900">Print Setup</h2>
          <p class="text-sm text-slate-500 mt-1">Choose output preferences for your next export</p>
        </div>
      </div>

      <div class="mt-5 grid grid-cols-1 md:grid-cols-3 gap-4">
        <button class="px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 text-left hover:bg-slate-100 text-sm font-semibold text-slate-700">Standard PDF</button>
        <button class="px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 text-left hover:bg-slate-100 text-sm font-semibold text-slate-700">Print-Ready Layout</button>
        <button class="px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 text-left hover:bg-slate-100 text-sm font-semibold text-slate-700">Office Summary</button>
      </div>
    </section>
  </div>
</template>
