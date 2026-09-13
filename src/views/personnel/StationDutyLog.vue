<template>
  <div class="w-full min-w-0 space-y-6">
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">
        <div>
          <p class="text-sm font-semibold text-[#8B1E23]">FIRENOTIFY PERSONNEL PORTAL</p>
          <h2 class="text-2xl font-bold text-slate-900 mt-1">Station Duty Log</h2>
          <p class="text-sm text-slate-500 mt-1">Track duty assignments, shift attendance, and station activities.</p>
        </div>
        <button class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D] transition">+ Add Duty Entry</button>
      </div>
    </section>

    <section class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-5">
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><p class="text-sm text-slate-500">Duty Days This Month</p><p class="text-3xl font-bold text-slate-900 mt-2">22</p><p class="text-xs text-green-600 font-semibold mt-2">On schedule</p></div>
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><p class="text-sm text-slate-500">Hours Completed</p><p class="text-3xl font-bold text-blue-600 mt-2">168</p><p class="text-xs text-slate-400 mt-2">Of 176 scheduled hours</p></div>
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><p class="text-sm text-slate-500">Activities Logged</p><p class="text-3xl font-bold text-green-600 mt-2">18</p><p class="text-xs text-slate-400 mt-2">This month</p></div>
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><p class="text-sm text-slate-500">Pending Entries</p><p class="text-3xl font-bold text-[#8B1E23] mt-2">02</p><p class="text-xs text-red-600 font-semibold mt-2">Needs completion</p></div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">
      <div class="flex flex-col lg:flex-row lg:items-end gap-4">
        <div class="flex-1"><label class="text-sm font-semibold text-slate-700">Date Range</label><select class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm text-slate-700"><option>This Month</option><option>This Week</option><option>Last Month</option><option>Custom Range</option></select></div>
        <div class="flex-1"><label class="text-sm font-semibold text-slate-700">Duty Status</label><select class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm text-slate-700"><option>All Statuses</option><option>On Duty</option><option>Completed</option><option>Pending</option><option>Absent</option></select></div>
        <div class="flex-1"><label class="text-sm font-semibold text-slate-700">Search Entries</label><input type="text" placeholder="Search duty logs..." class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm outline-none focus:ring-2 focus:ring-[#8B1E23]/20" /></div>
      </div>
    </section>

    <section class="grid grid-cols-1 xl:grid-cols-3 gap-6">
      <div class="xl:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-4"><div><h3 class="text-lg font-bold text-slate-900">Duty Log Entries</h3><p class="text-sm text-slate-500 mt-1">Recent attendance and station duty records</p></div><span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">22 Records</span></div>
        <div class="mt-5 space-y-4">
          <div class="p-5 rounded-xl border border-green-200 bg-green-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"><div class="flex gap-4"><div class="h-11 w-11 rounded-xl bg-green-100 flex items-center justify-center shrink-0"><span v-html="ICONS.check" class="h-5 w-5 text-green-600"></span></div><div><p class="text-base font-bold text-slate-900">Regular Station Duty</p><p class="text-sm text-slate-500 mt-1">September 12, 2026 · Station 1</p><p class="text-sm text-slate-500 mt-1">Shift: 08:00 AM - 05:00 PM</p><p class="text-sm text-slate-500 mt-1">Activities: Briefing, equipment check, fire safety inspection</p></div></div><span class="w-fit px-3 py-1.5 rounded-full bg-green-100 text-green-700 text-xs font-bold">Completed</span></div></div>
          <div class="p-5 rounded-xl border border-blue-200 bg-blue-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"><div class="flex gap-4"><div class="h-11 w-11 rounded-xl bg-blue-100 flex items-center justify-center shrink-0"><span v-html="ICONS.clock" class="h-5 w-5 text-blue-600"></span></div><div><p class="text-base font-bold text-slate-900">Field Inspection Duty</p><p class="text-sm text-slate-500 mt-1">September 11, 2026 · Public Market Complex</p><p class="text-sm text-slate-500 mt-1">Shift: 09:00 AM - 04:30 PM</p><p class="text-sm text-slate-500 mt-1">Logged by FO3 Juan Dela Cruz</p></div></div><span class="w-fit px-3 py-1.5 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">Verified</span></div></div>
          <div class="p-5 rounded-xl border border-yellow-200 bg-yellow-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"><div class="flex gap-4"><div class="h-11 w-11 rounded-xl bg-yellow-100 flex items-center justify-center shrink-0"><span v-html="ICONS.clock" class="h-5 w-5 text-yellow-600"></span></div><div><p class="text-base font-bold text-slate-900">Station Support Duty</p><p class="text-sm text-slate-500 mt-1">September 10, 2026 · BFP Balingasag</p><p class="text-sm text-slate-500 mt-1">Shift: 08:00 AM - 05:00 PM</p><p class="text-sm text-slate-500 mt-1">Daily log requires supervisor review</p></div></div><span class="w-fit px-3 py-1.5 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">Pending Review</span></div></div>
          <div class="p-5 rounded-xl border border-slate-200 bg-slate-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"><div><p class="text-base font-bold text-slate-900">Emergency Response Drill</p><p class="text-sm text-slate-500 mt-1">September 9, 2026 · Municipal Training Ground</p><p class="text-sm text-slate-500 mt-1">Duration: 4 hours · Participants: 12 personnel</p></div><span class="w-fit px-3 py-1.5 rounded-full bg-slate-200 text-slate-700 text-xs font-bold">Archived</span></div></div>
        </div>
      </div>

      <div class="space-y-6">
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Current Shift</h3><div class="mt-5 p-5 rounded-xl bg-green-50 border border-green-100"><div class="flex items-center gap-3"><div class="h-3 w-3 rounded-full bg-green-500"></div><p class="font-bold text-green-700">Currently On Duty</p></div><p class="text-sm text-slate-500 mt-3">Station 1 · BFP Balingasag</p><p class="text-sm text-slate-500 mt-1">08:00 AM - 05:00 PM</p><p class="text-xs text-slate-400 mt-3">Started today at 08:00 AM</p></div></div>
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Attendance Summary</h3><div class="mt-5 space-y-4"><div><div class="flex justify-between text-sm"><span class="text-slate-500">Present</span><span class="font-bold text-green-600">20 days</span></div><div class="h-2 mt-2 rounded-full bg-slate-200"><div class="h-full w-[91%] rounded-full bg-green-500"></div></div></div><div><div class="flex justify-between text-sm"><span class="text-slate-500">Leave</span><span class="font-bold text-yellow-600">02 days</span></div><div class="h-2 mt-2 rounded-full bg-slate-200"><div class="h-full w-[9%] rounded-full bg-yellow-500"></div></div></div></div></div>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4"><div><h3 class="text-lg font-bold text-slate-900">Monthly Duty Performance</h3><p class="text-sm text-slate-500 mt-1">Your station attendance and duty completion rate</p></div><p class="text-3xl font-bold text-[#8B1E23]">95%</p></div><div class="mt-4 h-3 rounded-full bg-slate-200 overflow-hidden"><div class="h-full w-[95%] rounded-full bg-[#8B1E23]"></div></div><div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mt-5"><div><p class="text-xs text-slate-500">Scheduled Shifts</p><p class="text-xl font-bold text-slate-900 mt-1">22</p></div><div><p class="text-xs text-slate-500">Completed Shifts</p><p class="text-xl font-bold text-green-600 mt-1">20</p></div><div><p class="text-xs text-slate-500">Logs Pending Review</p><p class="text-xl font-bold text-yellow-600 mt-1">02</p></div></div></section>
  </div>
</template>

<script setup>
defineProps({
  ICONS: {
    type: Object,
    required: true
  }
})
</script>
