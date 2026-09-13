<template>
  <div class="w-full min-w-0 space-y-6">
    <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">
        <div>
          <p class="text-sm font-semibold text-[#8B1E23]">FIRENOTIFY PERSONNEL PORTAL</p>
          <h2 class="text-2xl font-bold text-slate-900 mt-1">My Reports</h2>
          <p class="text-sm text-slate-500 mt-1">Submit, monitor, and review your operational reports.</p>
        </div>
        <button class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D] transition">+ Create Report</button>
      </div>
    </div>

    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">Total Reports</p><p class="text-3xl font-bold text-slate-900 mt-1">16</p><p class="text-xs text-slate-400 mt-1">This month</p></div><div class="h-12 w-12 rounded-xl bg-blue-50 flex items-center justify-center"><span v-html="ICONS.reports" class="h-6 w-6 text-blue-600"></span></div></div></div>
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">Pending</p><p class="text-3xl font-bold text-yellow-600 mt-1">03</p><p class="text-xs text-slate-400 mt-1">Requires submission</p></div><div class="h-12 w-12 rounded-xl bg-yellow-50 flex items-center justify-center"><span v-html="ICONS.clock" class="h-6 w-6 text-yellow-600"></span></div></div></div>
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">Submitted</p><p class="text-3xl font-bold text-green-600 mt-1">12</p><p class="text-xs text-slate-400 mt-1">Successfully submitted</p></div><div class="h-12 w-12 rounded-xl bg-green-50 flex items-center justify-center"><span v-html="ICONS.check" class="h-6 w-6 text-green-600"></span></div></div></div>
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">Returned</p><p class="text-3xl font-bold text-[#8B1E23] mt-1">01</p><p class="text-xs text-slate-400 mt-1">Needs correction</p></div><div class="h-12 w-12 rounded-xl bg-red-50 flex items-center justify-center"><span v-html="ICONS.siren" class="h-6 w-6 text-[#8B1E23]"></span></div></div></div>
    </section>

    <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
        <div><h3 class="text-lg font-bold text-slate-900">Report Records</h3><p class="text-sm text-slate-500 mt-1">Search and filter your submitted reports.</p></div>
        <div class="flex flex-col sm:flex-row gap-3"><input type="text" placeholder="Search reports..." class="px-4 py-2.5 rounded-xl border border-slate-200 bg-white text-sm outline-none focus:ring-2 focus:ring-[#8B1E23]/20" /><select class="px-4 py-2.5 rounded-xl border border-slate-200 bg-white text-sm text-slate-700"><option>All Status</option><option>Pending</option><option>Submitted</option><option>Returned</option></select></div>
      </div>
    </div>

    <section class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="lg:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-4"><div><h3 class="text-lg font-bold text-slate-900">Report List</h3><p class="text-sm text-slate-500 mt-1">Your latest operational reports</p></div><span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">16 Reports</span></div>
        <div class="mt-5 space-y-4">
          <div class="p-5 rounded-xl border border-yellow-200 bg-yellow-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"><div class="flex gap-4"><div class="h-11 w-11 rounded-xl bg-yellow-100 flex items-center justify-center shrink-0"><span v-html="ICONS.reports" class="h-5 w-5 text-yellow-700"></span></div><div><p class="text-base font-bold text-slate-900">Fire Safety Inspection Report</p><p class="text-sm text-slate-500 mt-1">Activity: Fire Safety Inspection</p><p class="text-sm text-slate-500 mt-1">Due: September 12, 2026</p><p class="text-xs text-yellow-700 font-semibold mt-2">Action required</p></div></div><span class="w-fit px-3 py-1.5 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">Pending</span></div><div class="mt-4 flex flex-wrap gap-2"><button class="px-4 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-semibold hover:bg-[#72181D]">Submit Report</button><button class="px-4 py-2 rounded-lg border border-slate-200 bg-white text-slate-700 text-sm font-semibold hover:bg-slate-100">View Activity</button></div></div>
          <div class="p-5 rounded-xl border border-green-200 bg-green-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"><div class="flex gap-4"><div class="h-11 w-11 rounded-xl bg-green-100 flex items-center justify-center shrink-0"><span v-html="ICONS.check" class="h-5 w-5 text-green-600"></span></div><div><p class="text-base font-bold text-slate-900">Routine Safety Patrol Report</p><p class="text-sm text-slate-500 mt-1">Activity: Routine Safety Patrol</p><p class="text-sm text-slate-500 mt-1">Submitted: September 7, 2026</p><p class="text-xs text-green-700 font-semibold mt-2">Successfully submitted</p></div></div><span class="w-fit px-3 py-1.5 rounded-full bg-green-100 text-green-700 text-xs font-bold">Submitted</span></div><div class="mt-4"><button class="px-4 py-2 rounded-lg border border-slate-200 bg-white text-slate-700 text-sm font-semibold hover:bg-slate-100">View Report</button></div></div>
          <div class="p-5 rounded-xl border border-red-200 bg-red-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"><div class="flex gap-4"><div class="h-11 w-11 rounded-xl bg-red-100 flex items-center justify-center shrink-0"><span v-html="ICONS.siren" class="h-5 w-5 text-[#8B1E23]"></span></div><div><p class="text-base font-bold text-slate-900">Fire Drill Monitoring Report</p><p class="text-sm text-slate-500 mt-1">Activity: Fire Drill Monitoring</p><p class="text-sm text-slate-500 mt-1">Returned: September 8, 2026</p><p class="text-xs text-[#8B1E23] font-semibold mt-2">Correction required</p></div></div><span class="w-fit px-3 py-1.5 rounded-full bg-red-100 text-[#8B1E23] text-xs font-bold">Returned</span></div><div class="mt-4 p-4 rounded-xl bg-white border border-red-200"><p class="text-xs font-semibold text-slate-500 uppercase">Remarks</p><p class="text-sm text-slate-700 mt-1">Please attach the attendance sheet and update the inspection details.</p></div><button class="mt-4 px-4 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-semibold hover:bg-[#72181D]">Revise Report</button></div>
          <div class="p-5 rounded-xl border border-slate-200 bg-slate-50"><div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4"><div><p class="text-base font-bold text-slate-900">Community Fire Safety Seminar Report</p><p class="text-sm text-slate-500 mt-1">Submitted September 5, 2026</p><p class="text-sm text-slate-500 mt-1">Barangay San Isidro</p></div><div class="flex items-center gap-2"><span class="px-3 py-1.5 rounded-full bg-green-100 text-green-700 text-xs font-bold">Submitted</span><button class="px-3 py-1.5 rounded-lg border border-slate-200 bg-white text-slate-700 text-xs font-semibold">View</button></div></div></div>
        </div>
      </div>

      <div class="space-y-6">
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Report Completion</h3><p class="text-sm text-slate-500 mt-1">Your report submission progress</p><div class="mt-5"><div class="flex items-end justify-between"><p class="text-3xl font-bold text-[#8B1E23]">80%</p><span class="text-xs font-semibold text-green-600">Good standing</span></div><div class="mt-3 h-3 rounded-full bg-slate-200 overflow-hidden"><div class="h-full w-[80%] bg-[#8B1E23] rounded-full"></div></div><div class="grid grid-cols-2 gap-4 mt-5"><div><p class="text-xs text-slate-500">Submitted</p><p class="text-lg font-bold text-green-600">12</p></div><div><p class="text-xs text-slate-500">Pending</p><p class="text-lg font-bold text-yellow-600">03</p></div></div></div></div>
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Report Deadlines</h3><p class="text-sm text-slate-500 mt-1">Upcoming submission deadlines</p><div class="mt-5 space-y-4"><div class="p-4 rounded-xl bg-yellow-50 border border-yellow-200"><div class="flex justify-between gap-3"><div><p class="text-sm font-bold text-slate-900">Fire Safety Inspection</p><p class="text-xs text-slate-500 mt-1">Due today</p></div><span class="text-xs font-bold text-yellow-700">Today</span></div></div><div class="p-4 rounded-xl bg-slate-50 border border-slate-200"><p class="text-sm font-bold text-slate-900">Community Seminar</p><p class="text-xs text-slate-500 mt-1">Due September 13, 2026</p></div><div class="p-4 rounded-xl bg-slate-50 border border-slate-200"><p class="text-sm font-bold text-slate-900">Emergency Drill</p><p class="text-xs text-slate-500 mt-1">Due September 15, 2026</p></div></div></div>
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Recent Activity</h3><div class="mt-5 space-y-4"><div class="flex gap-3"><div class="h-8 w-8 rounded-full bg-green-100 flex items-center justify-center shrink-0"><span v-html="ICONS.check" class="h-4 w-4 text-green-600"></span></div><div><p class="text-sm font-semibold text-slate-900">Report submitted</p><p class="text-xs text-slate-500 mt-1">Routine Safety Patrol Report</p><p class="text-xs text-slate-400 mt-1">September 7, 2026 · 03:25 PM</p></div></div><div class="flex gap-3"><div class="h-8 w-8 rounded-full bg-red-100 flex items-center justify-center shrink-0"><span v-html="ICONS.siren" class="h-4 w-4 text-[#8B1E23]"></span></div><div><p class="text-sm font-semibold text-slate-900">Report returned</p><p class="text-xs text-slate-500 mt-1">Fire Drill Monitoring Report</p><p class="text-xs text-slate-400 mt-1">September 8, 2026 · 10:15 AM</p></div></div></div></div>
      </div>
    </section>
  </div>
</template>

<script setup>
defineProps({
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
</script>
