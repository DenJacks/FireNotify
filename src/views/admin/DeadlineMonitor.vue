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
      <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">Compliance Monitoring</p>
      <h2 class="text-2xl font-bold text-slate-900 mt-1">Deadline Monitor</h2>
      <p class="text-base text-slate-500 mt-1">Track upcoming, due, and overdue report deadlines.</p>
    </section>

    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">02</p>
        <p class="text-sm text-slate-500 mt-1">Overdue</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">03</p>
        <p class="text-sm text-slate-500 mt-1">Due Today</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-blue-600">07</p>
        <p class="text-sm text-slate-500 mt-1">This Week</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">24</p>
        <p class="text-sm text-slate-500 mt-1">Completed</p>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex items-center gap-3">
        <div class="h-11 w-11 rounded-xl bg-red-50 flex items-center justify-center">🚨</div>
        <div>
          <h2 class="text-xl font-bold text-slate-900">Overdue Deadlines</h2>
          <p class="text-sm text-slate-500">Immediate administrative attention required</p>
        </div>
      </div>

      <div class="mt-5 space-y-3">
        <div class="p-5 rounded-xl bg-red-50 border border-red-200">
          <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
            <div>
              <p class="font-bold text-slate-900">After-Operation Fire Incident Report</p>
              <p class="text-sm text-[#8B1E23] mt-1">Assigned to FO3 Juan Dela Cruz</p>
              <p class="text-sm text-[#8B1E23] mt-1">Overdue by 2 hours</p>
            </div>
            <button class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold">Send Escalation</button>
          </div>
        </div>

        <div class="p-5 rounded-xl bg-red-50 border border-red-200">
          <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
            <div>
              <p class="font-bold text-slate-900">Station Activity Report</p>
              <p class="text-sm text-[#8B1E23] mt-1">Assigned to FO2 Roberto Reyes</p>
              <p class="text-sm text-[#8B1E23] mt-1">Overdue by 1 hour</p>
            </div>
            <button class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold">Send Escalation</button>
          </div>
        </div>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <h2 class="text-xl font-bold text-slate-900">Upcoming Deadlines</h2>
      <p class="text-sm text-slate-500 mt-1">Reports that are approaching their submission deadline</p>

      <div class="mt-5 space-y-3">
        <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4 p-5 rounded-xl border border-yellow-200 bg-yellow-50">
          <div>
            <p class="font-bold text-slate-900">Weekly Accomplishment Report</p>
            <p class="text-sm text-slate-500 mt-1">Assigned to SFO1 Maria Santos</p>
          </div>
          <span class="px-4 py-2 rounded-full bg-yellow-100 text-yellow-700 text-sm font-bold">Due Tomorrow • 5:00 PM</span>
        </div>

        <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4 p-5 rounded-xl border border-blue-200 bg-blue-50">
          <div>
            <p class="font-bold text-slate-900">Monthly Compliance Report</p>
            <p class="text-sm text-slate-500 mt-1">Station 1 Administration</p>
          </div>
          <span class="px-4 py-2 rounded-full bg-blue-100 text-blue-700 text-sm font-bold">Due in 5 Days</span>
        </div>
      </div>
    </section>

    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Deadline Trends</h2>
            <p class="text-sm text-slate-500 mt-1">Weekly performance summary</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>On-Time Rate</span>
              <span>79%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[79%] rounded-full bg-emerald-500"></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Escalations Sent</span>
              <span>11</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[58%] rounded-full bg-red-500"></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Resolved Before Deadline</span>
              <span>67%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[67%] rounded-full bg-blue-500"></div>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Escalation Queue</h2>
            <p class="text-sm text-slate-500 mt-1">Reports needing action from higher units</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div class="p-4 rounded-xl border border-red-200 bg-red-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">After-Operation Fire Incident Report</p>
                <p class="text-xs text-slate-500 mt-1">Escalated to Station Operations Chief</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-red-100 text-[#8B1E23] text-xs font-bold">High</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-yellow-200 bg-yellow-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">Monthly Compliance Report</p>
                <p class="text-xs text-slate-500 mt-1">Pending review from Admin Office</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">Medium</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-blue-200 bg-blue-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">Barangay Fire Drill Summary</p>
                <p class="text-xs text-slate-500 mt-1">Awaiting validation of attendance logs</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">Info</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex items-center justify-between border-b border-slate-200 pb-5">
        <div>
          <h2 class="text-xl font-bold text-slate-900">Compliance Notes</h2>
          <p class="text-sm text-slate-500 mt-1">Operational reminders and monitoring details</p>
        </div>
      </div>

      <div class="mt-5 space-y-4">
        <div class="p-4 rounded-xl border border-emerald-200 bg-emerald-50">
          <p class="text-sm font-bold text-slate-900">Reminder</p>
          <p class="text-sm text-slate-600 mt-1">Late submissions should be resequenced immediately after review to avoid backlogs in the next cycle.</p>
        </div>

        <div class="p-4 rounded-xl border border-orange-200 bg-orange-50">
          <p class="text-sm font-bold text-slate-900">Attention</p>
          <p class="text-sm text-slate-600 mt-1">2 overdue reports require an escalation note to the operations head before the end of the day.</p>
        </div>

        <div class="p-4 rounded-xl border border-indigo-200 bg-indigo-50">
          <p class="text-sm font-bold text-slate-900">Follow-Up</p>
          <p class="text-sm text-slate-600 mt-1">Monitor the final status of all approved reports and ensure attachments are saved in the archive.</p>
        </div>
      </div>
    </section>
  </div>
</template>
