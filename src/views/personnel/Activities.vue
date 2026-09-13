<template>
  <div class="w-full min-w-0 space-y-6">
    <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">
        <div>
          <p class="text-sm font-semibold text-[#8B1E23]">FIRENOTIFY PERSONNEL PORTAL</p>
          <h2 class="text-2xl font-bold text-slate-900 mt-1">Activities</h2>
          <p class="text-sm text-slate-500 mt-1">View and monitor activities assigned to your station.</p>
        </div>
        <div class="flex items-center gap-3">
          <div class="h-12 w-12 rounded-xl bg-[#8B1E23]/10 flex items-center justify-center">
            <span v-html="ICONS.tasks" class="h-6 w-6 text-[#8B1E23]"></span>
          </div>
          <div><p class="text-xs text-slate-500">Station</p><p class="text-base font-bold text-slate-900">BFP Balingasag</p></div>
        </div>
      </div>
    </div>

    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">Total Activities</p><p class="text-3xl font-bold text-slate-900 mt-1">12</p><p class="text-xs text-slate-400 mt-1">This month</p></div><div class="h-12 w-12 rounded-xl bg-blue-50 flex items-center justify-center"><span v-html="ICONS.tasks" class="h-6 w-6 text-blue-600"></span></div></div></div>
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">Scheduled</p><p class="text-3xl font-bold text-yellow-600 mt-1">05</p><p class="text-xs text-slate-400 mt-1">Upcoming activities</p></div><div class="h-12 w-12 rounded-xl bg-yellow-50 flex items-center justify-center"><span v-html="ICONS.clock" class="h-6 w-6 text-yellow-600"></span></div></div></div>
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">Completed</p><p class="text-3xl font-bold text-green-600 mt-1">06</p><p class="text-xs text-slate-400 mt-1">Successfully completed</p></div><div class="h-12 w-12 rounded-xl bg-green-50 flex items-center justify-center"><span v-html="ICONS.check" class="h-6 w-6 text-green-600"></span></div></div></div>
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">Overdue</p><p class="text-3xl font-bold text-[#8B1E23] mt-1">01</p><p class="text-xs text-slate-400 mt-1">Needs attention</p></div><div class="h-12 w-12 rounded-xl bg-red-50 flex items-center justify-center"><span v-html="ICONS.siren" class="h-6 w-6 text-[#8B1E23]"></span></div></div></div>
    </section>

    <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
        <div><h3 class="text-base font-bold text-slate-900">Activity List</h3><p class="text-sm text-slate-500">Review scheduled and completed station activities.</p></div>
        <div class="flex flex-col sm:flex-row gap-3"><select class="px-4 py-2.5 rounded-xl border border-slate-200 bg-white text-sm text-slate-700"><option>All Status</option><option>Scheduled</option><option>In Progress</option><option>Completed</option><option>Overdue</option></select><select class="px-4 py-2.5 rounded-xl border border-slate-200 bg-white text-sm text-slate-700"><option>All Activity Types</option><option>Inspection</option><option>Patrol</option><option>Training</option><option>Drill</option><option>Meeting</option></select></div>
      </div>
    </div>

    <section class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="lg:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-4"><div><h3 class="text-lg font-bold text-slate-900">Assigned Activities</h3><p class="text-sm text-slate-500 mt-1">Activities assigned to your station</p></div><span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">12 Activities</span></div>
        <div class="mt-5 space-y-4">
          <div class="p-5 rounded-xl border border-yellow-200 bg-yellow-50/50"><div class="flex flex-col sm:flex-row sm:items-start gap-4"><div class="h-12 w-12 rounded-xl bg-blue-50 flex items-center justify-center shrink-0"><span v-html="ICONS.tasks" class="h-6 w-6 text-blue-600"></span></div><div class="flex-1"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-2"><div><p class="text-base font-bold text-slate-900">Fire Safety Inspection</p><p class="text-sm text-slate-500 mt-1">Public Market Complex</p></div><span class="w-fit px-3 py-1.5 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">Scheduled</span></div><div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-4"><p class="text-sm text-slate-500">September 12, 2026</p><p class="text-sm text-slate-500">09:00 AM</p><p class="text-sm text-slate-500">Assigned: FO3 Juan Dela Cruz</p><p class="text-sm text-slate-500">Balingasag</p></div><div class="mt-4 flex flex-wrap gap-2"><button class="px-4 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-semibold hover:bg-[#72181D]">View Details</button><button class="px-4 py-2 rounded-lg border border-slate-200 bg-white text-slate-700 text-sm font-semibold hover:bg-slate-100">Update Status</button></div></div></div></div>
          <div class="p-5 rounded-xl border border-blue-200 bg-blue-50/40"><div class="flex flex-col sm:flex-row sm:items-start gap-4"><div class="h-12 w-12 rounded-xl bg-blue-100 flex items-center justify-center shrink-0"><span v-html="ICONS.tasks" class="h-6 w-6 text-blue-600"></span></div><div class="flex-1"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-2"><div><p class="text-base font-bold text-slate-900">Community Fire Safety Seminar</p><p class="text-sm text-slate-500 mt-1">Barangay San Isidro Covered Court</p></div><span class="w-fit px-3 py-1.5 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">In Progress</span></div><div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-4"><p class="text-sm text-slate-500">September 13, 2026</p><p class="text-sm text-slate-500">01:00 PM</p><p class="text-sm text-slate-500">Assigned: FO2 Mark Santos</p><p class="text-sm text-slate-500">Balingasag</p></div><div class="mt-4"><div class="flex justify-between text-xs mb-2"><span class="text-slate-500">Progress</span><span class="font-bold text-blue-600">60%</span></div><div class="h-2 rounded-full bg-slate-200 overflow-hidden"><div class="h-full w-[60%] bg-blue-600 rounded-full"></div></div></div></div></div></div>
          <div class="p-5 rounded-xl border border-green-200 bg-green-50"><div class="flex flex-col sm:flex-row sm:items-start gap-4"><div class="h-12 w-12 rounded-xl bg-green-100 flex items-center justify-center shrink-0"><span v-html="ICONS.check" class="h-6 w-6 text-green-600"></span></div><div class="flex-1"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-2"><div><p class="text-base font-bold text-slate-900">Routine Safety Patrol</p><p class="text-sm text-slate-500 mt-1">Zone 2 Commercial Area</p></div><span class="w-fit px-3 py-1.5 rounded-full bg-green-100 text-green-700 text-xs font-bold">Completed</span></div><div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-4"><p class="text-sm text-slate-500">September 10, 2026</p><p class="text-sm text-slate-500">08:00 AM</p><p class="text-sm text-slate-500">Completed by: FO3 Juan Dela Cruz</p><p class="text-sm text-slate-500">Balingasag</p></div><p class="mt-4 text-xs font-semibold text-green-700">Activity completed successfully</p></div></div></div>
          <div class="p-5 rounded-xl border border-red-200 bg-red-50"><div class="flex flex-col sm:flex-row sm:items-start gap-4"><div class="h-12 w-12 rounded-xl bg-red-100 flex items-center justify-center shrink-0"><span v-html="ICONS.siren" class="h-6 w-6 text-[#8B1E23]"></span></div><div class="flex-1"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-2"><div><p class="text-base font-bold text-slate-900">Fire Drill Monitoring</p><p class="text-sm text-slate-500 mt-1">Municipal Elementary School</p></div><span class="w-fit px-3 py-1.5 rounded-full bg-red-100 text-[#8B1E23] text-xs font-bold">Overdue</span></div><div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-4"><p class="text-sm text-slate-500">September 09, 2026</p><p class="text-sm text-slate-500">10:00 AM</p><p class="text-sm text-slate-500">Assigned: FO1 Carlo Reyes</p><p class="text-sm text-slate-500">Balingasag</p></div><button class="mt-4 px-4 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-semibold hover:bg-[#72181D]">Resolve Activity</button></div></div></div>
        </div>
      </div>

      <div class="space-y-6">
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><div class="flex items-center justify-between"><div><h3 class="text-lg font-bold text-slate-900">Today's Activities</h3><p class="text-sm text-slate-500 mt-1">September 12, 2026</p></div><div class="h-10 w-10 rounded-xl bg-[#8B1E23]/10 flex items-center justify-center"><span v-html="ICONS.clock" class="h-5 w-5 text-[#8B1E23]"></span></div></div><div class="mt-5 space-y-4"><div class="flex gap-3"><div class="w-1 rounded-full bg-[#8B1E23]"></div><div><p class="text-sm font-bold text-slate-900">Fire Safety Inspection</p><p class="text-xs text-slate-500 mt-1">09:00 AM · Public Market</p><span class="inline-block mt-2 text-xs font-semibold text-yellow-700">Scheduled</span></div></div><div class="flex gap-3"><div class="w-1 rounded-full bg-green-500"></div><div><p class="text-sm font-bold text-slate-900">Station Briefing</p><p class="text-xs text-slate-500 mt-1">04:00 PM · BFP Station</p><span class="inline-block mt-2 text-xs font-semibold text-green-700">Scheduled</span></div></div></div></div>
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Upcoming Activities</h3><p class="text-sm text-slate-500 mt-1">Next scheduled activities</p><div class="mt-5 space-y-4"><div class="p-4 rounded-xl bg-slate-50 border border-slate-200"><p class="text-sm font-bold text-slate-900">Fire Safety Seminar</p><p class="text-xs text-slate-500 mt-1">September 13 · 01:00 PM</p><p class="text-xs text-slate-500 mt-1">Barangay San Isidro</p></div><div class="p-4 rounded-xl bg-slate-50 border border-slate-200"><p class="text-sm font-bold text-slate-900">Emergency Response Drill</p><p class="text-xs text-slate-500 mt-1">September 15 · 08:30 AM</p><p class="text-xs text-slate-500 mt-1">Balingasag Municipal Hall</p></div><div class="p-4 rounded-xl bg-slate-50 border border-slate-200"><p class="text-sm font-bold text-slate-900">Personnel Training</p><p class="text-xs text-slate-500 mt-1">September 17 · 09:00 AM</p><p class="text-xs text-slate-500 mt-1">BFP Training Room</p></div></div></div>
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Activity Performance</h3><p class="text-sm text-slate-500 mt-1">Current station completion rate</p><div class="mt-5"><div class="flex items-end justify-between"><p class="text-3xl font-bold text-[#8B1E23]">91.7%</p><span class="text-xs font-semibold text-green-600">+4.2% this month</span></div><div class="mt-3 h-3 rounded-full bg-slate-200 overflow-hidden"><div class="h-full w-[91.7%] bg-[#8B1E23] rounded-full"></div></div><div class="grid grid-cols-2 gap-4 mt-5"><div><p class="text-xs text-slate-500">Completed</p><p class="text-lg font-bold text-green-600">06</p></div><div><p class="text-xs text-slate-500">Pending</p><p class="text-lg font-bold text-yellow-600">05</p></div></div></div></div>
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
