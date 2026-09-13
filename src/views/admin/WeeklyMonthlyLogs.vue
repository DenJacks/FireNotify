<script setup>
const logs = [
  {
    activity: 'After-Operation Fire Incident Report',
    personnel: 'SFO1 M. Santos',
    deadline: 'Today, 17:00',
    status: 'Pending'
  },
  {
    activity: 'Quarterly Establishment Inspection',
    personnel: 'FO3 J. Dela Cruz',
    deadline: 'Aug 20, 2026',
    status: 'Completed'
  }
]
</script>

<template>
  <div class="space-y-6">
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
        <div>
          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">Record Archives</p>
          <h2 class="text-2xl font-bold text-slate-900 mt-1">Weekly / Monthly Logs</h2>
          <p class="text-base text-slate-500 mt-1">Review station summaries, recurring reports, and compliance records.</p>
        </div>

        <button class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition">
          + Add Log Entry
        </button>
      </div>
    </section>

    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">12</p>
        <p class="text-sm text-slate-500 mt-1">Weekly Logs</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-blue-600">08</p>
        <p class="text-sm text-slate-500 mt-1">Monthly Reports</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">06</p>
        <p class="text-sm text-slate-500 mt-1">Submitted</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">02</p>
        <p class="text-sm text-slate-500 mt-1">Pending Review</p>
      </div>
    </section>

    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Weekly Highlights</h2>
            <p class="text-sm text-slate-500 mt-1">This week’s important operational notes</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <p class="text-sm font-bold text-slate-900">Fire Safety Orientation</p>
            <p class="text-sm text-slate-600 mt-1">Covered 5 barangays with 98% attendance from local responders and volunteers.</p>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <p class="text-sm font-bold text-slate-900">Equipment Readiness</p>
            <p class="text-sm text-slate-600 mt-1">All assigned rescue tools were checked, cleaned, and tagged for dispatch readiness.</p>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <p class="text-sm font-bold text-slate-900">Dispatch Coordination</p>
            <p class="text-sm text-slate-600 mt-1">Dispatch teams coordinated with local emergency units for three scheduled activities.</p>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Monthly Highlights</h2>
            <p class="text-sm text-slate-500 mt-1">Station compliance and performance summary</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div class="p-4 rounded-xl border border-emerald-200 bg-emerald-50">
            <p class="text-sm font-bold text-slate-900">Compliance Rate</p>
            <p class="text-sm text-slate-600 mt-1">Monthly compliance increased to 94.5%, surpassing the previous cycle by 4.2%.</p>
          </div>

          <div class="p-4 rounded-xl border border-blue-200 bg-blue-50">
            <p class="text-sm font-bold text-slate-900">Report Turnaround</p>
            <p class="text-sm text-slate-600 mt-1">Average report submission turnaround improved to 2.3 days across all stations.</p>
          </div>

          <div class="p-4 rounded-xl border border-amber-200 bg-amber-50">
            <p class="text-sm font-bold text-slate-900">Staff Performance</p>
            <p class="text-sm text-slate-600 mt-1">Operations staff maintained steady productivity while balancing drills, inspections, and training.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex items-center justify-between border-b border-slate-200 pb-5">
        <div>
          <h2 class="text-xl font-bold text-slate-900">Recent Weekly / Monthly Entries</h2>
          <p class="text-sm text-slate-500 mt-1">Latest archived logs submitted by personnel</p>
        </div>
      </div>

      <div class="mt-5 overflow-x-auto">
        <table class="min-w-full border-separate border-spacing-y-3">
          <thead>
            <tr class="text-left text-xs font-bold uppercase tracking-wide text-slate-500">
              <th class="pb-2 pr-4">Activity</th>
              <th class="pb-2 pr-4">Personnel</th>
              <th class="pb-2 pr-4">Deadline</th>
              <th class="pb-2">Status</th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="item in logs" :key="item.activity" class="bg-slate-50 rounded-xl">
              <td class="py-4 pr-4 font-semibold text-slate-900 rounded-l-xl">{{ item.activity }}</td>
              <td class="py-4 pr-4 text-slate-600">{{ item.personnel }}</td>
              <td class="py-4 pr-4 text-slate-600">{{ item.deadline }}</td>
              <td class="py-4 pr-4">
                <span class="px-3 py-1 rounded-full text-xs font-bold" :class="item.status === 'Completed' ? 'bg-green-100 text-green-700' : 'bg-yellow-100 text-yellow-700'">
                  {{ item.status }}
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  </div>
</template>
