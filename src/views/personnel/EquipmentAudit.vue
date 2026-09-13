<template>
  <div class="w-full min-w-0 space-y-6">
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">
        <div>
          <p class="text-sm font-semibold text-[#8B1E23]">FIRENOTIFY PERSONNEL PORTAL</p>
          <h2 class="text-2xl font-bold text-slate-900 mt-1">Equipment Audit</h2>
          <p class="text-sm text-slate-500 mt-1">Monitor equipment availability, condition, assignment, and maintenance records.</p>
        </div>
        <button class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D] transition">+ Add Equipment</button>
      </div>
    </section>

    <section class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-5">
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><p class="text-sm text-slate-500">Total Equipment</p><p class="text-3xl font-bold text-slate-900 mt-2">48</p><p class="text-xs text-slate-400 mt-2">Station inventory</p></div>
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><p class="text-sm text-slate-500">Serviceable</p><p class="text-3xl font-bold text-green-600 mt-2">41</p><p class="text-xs text-green-600 font-semibold mt-2">85% operational</p></div>
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><p class="text-sm text-slate-500">For Maintenance</p><p class="text-3xl font-bold text-yellow-600 mt-2">05</p><p class="text-xs text-slate-400 mt-2">Needs inspection or repair</p></div>
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><p class="text-sm text-slate-500">Missing / Damaged</p><p class="text-3xl font-bold text-[#8B1E23] mt-2">02</p><p class="text-xs text-red-600 font-semibold mt-2">Immediate attention</p></div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">
      <div class="flex flex-col lg:flex-row lg:items-end gap-4">
        <div class="flex-1"><label class="text-sm font-semibold text-slate-700">Equipment Category</label><select class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm text-slate-700"><option>All Categories</option><option>Firefighting Tools</option><option>Protective Equipment</option><option>Communication</option><option>Medical Supplies</option></select></div>
        <div class="flex-1"><label class="text-sm font-semibold text-slate-700">Condition</label><select class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm text-slate-700"><option>All Conditions</option><option>Serviceable</option><option>For Maintenance</option><option>Damaged</option><option>Missing</option></select></div>
        <div class="flex-1"><label class="text-sm font-semibold text-slate-700">Search Inventory</label><input type="text" placeholder="Search equipment..." class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm outline-none focus:ring-2 focus:ring-[#8B1E23]/20" /></div>
      </div>
    </section>

    <section class="grid grid-cols-1 xl:grid-cols-3 gap-6">
      <div class="xl:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-4"><div><h3 class="text-lg font-bold text-slate-900">Equipment Inventory</h3><p class="text-sm text-slate-500 mt-1">Current station equipment records</p></div><span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">48 Items</span></div>
        <div class="mt-5 space-y-4">
          <div class="p-5 rounded-xl border border-green-200 bg-green-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"><div class="flex gap-4"><div class="h-11 w-11 rounded-xl bg-green-100 flex items-center justify-center shrink-0"><span v-html="ICONS.check" class="h-5 w-5 text-green-600"></span></div><div><p class="text-base font-bold text-slate-900">Fire Hose Reel - FH-001</p><p class="text-sm text-slate-500 mt-1">Firefighting Tools · Station 1</p><p class="text-sm text-slate-500 mt-1">Assigned to: Engine 01 · Last inspected: September 5, 2026</p><p class="text-sm text-slate-500 mt-1">Next inspection: October 5, 2026</p></div></div><span class="w-fit px-3 py-1.5 rounded-full bg-green-100 text-green-700 text-xs font-bold">Serviceable</span></div></div>
          <div class="p-5 rounded-xl border border-green-200 bg-green-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"><div class="flex gap-4"><div class="h-11 w-11 rounded-xl bg-green-100 flex items-center justify-center shrink-0"><span v-html="ICONS.check" class="h-5 w-5 text-green-600"></span></div><div><p class="text-base font-bold text-slate-900">SCBA Set - SCBA-014</p><p class="text-sm text-slate-500 mt-1">Protective Equipment · Locker A-04</p><p class="text-sm text-slate-500 mt-1">Assigned to: FO3 Juan Dela Cruz · Last inspected: September 1, 2026</p><p class="text-sm text-slate-500 mt-1">Cylinder pressure: 3,000 PSI</p></div></div><span class="w-fit px-3 py-1.5 rounded-full bg-green-100 text-green-700 text-xs font-bold">Serviceable</span></div></div>
          <div class="p-5 rounded-xl border border-yellow-200 bg-yellow-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"><div class="flex gap-4"><div class="h-11 w-11 rounded-xl bg-yellow-100 flex items-center justify-center shrink-0"><span v-html="ICONS.clock" class="h-5 w-5 text-yellow-600"></span></div><div><p class="text-base font-bold text-slate-900">Portable Radio - RAD-008</p><p class="text-sm text-slate-500 mt-1">Communication · Control Room</p><p class="text-sm text-slate-500 mt-1">Assigned to: Station Communications · Battery replacement required</p><p class="text-sm text-slate-500 mt-1">Maintenance due: September 15, 2026</p></div></div><span class="w-fit px-3 py-1.5 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">For Maintenance</span></div></div>
          <div class="p-5 rounded-xl border border-red-200 bg-red-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"><div class="flex gap-4"><div class="h-11 w-11 rounded-xl bg-red-100 flex items-center justify-center shrink-0"><span v-html="ICONS.siren" class="h-5 w-5 text-[#8B1E23]"></span></div><div><p class="text-base font-bold text-slate-900">Hydraulic Cutter - HYD-003</p><p class="text-sm text-slate-500 mt-1">Rescue Tools · Equipment Bay</p><p class="text-sm text-slate-500 mt-1">Reported by: FO1 Carlo Reyes · Reported: September 9, 2026</p><p class="text-sm text-slate-500 mt-1">Issue: Hydraulic leak detected</p></div></div><span class="w-fit px-3 py-1.5 rounded-full bg-red-100 text-[#8B1E23] text-xs font-bold">Damaged</span></div></div>
          <div class="p-5 rounded-xl border border-slate-200 bg-slate-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"><div><p class="text-base font-bold text-slate-900">First Aid Kit - MED-006</p><p class="text-sm text-slate-500 mt-1">Medical Supplies · Response Vehicle 02</p><p class="text-sm text-slate-500 mt-1">Inventory count incomplete · Last checked: August 30, 2026</p></div><span class="w-fit px-3 py-1.5 rounded-full bg-slate-200 text-slate-700 text-xs font-bold">Audit Required</span></div></div>
        </div>
      </div>

      <div class="space-y-6">
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Audit Progress</h3><p class="text-sm text-slate-500 mt-1">Monthly inventory verification</p><div class="mt-5"><div class="flex items-end justify-between"><p class="text-3xl font-bold text-[#8B1E23]">85%</p><span class="text-xs font-semibold text-green-600">41 of 48 checked</span></div><div class="mt-3 h-3 rounded-full bg-slate-200 overflow-hidden"><div class="h-full w-[85%] bg-[#8B1E23] rounded-full"></div></div><p class="text-xs text-slate-500 mt-3">7 items still require inspection or verification.</p></div></div>
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Upcoming Maintenance</h3><div class="mt-5 space-y-4"><div class="p-4 rounded-xl bg-yellow-50 border border-yellow-200"><p class="text-sm font-bold text-slate-900">Portable Radio - RAD-008</p><p class="text-xs text-yellow-700 font-semibold mt-1">Due September 15, 2026</p></div><div class="p-4 rounded-xl bg-slate-50 border border-slate-200"><p class="text-sm font-bold text-slate-900">SCBA Cylinder Inspection</p><p class="text-xs text-slate-500 mt-1">Due September 20, 2026</p></div><div class="p-4 rounded-xl bg-slate-50 border border-slate-200"><p class="text-sm font-bold text-slate-900">Vehicle Pump Test</p><p class="text-xs text-slate-500 mt-1">Due September 25, 2026</p></div></div></div>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4"><div><h3 class="text-lg font-bold text-slate-900">Equipment Compliance</h3><p class="text-sm text-slate-500 mt-1">Station equipment readiness and audit completion</p></div><p class="text-3xl font-bold text-green-600">85%</p></div><div class="mt-4 h-3 rounded-full bg-slate-200 overflow-hidden"><div class="h-full w-[85%] rounded-full bg-green-500"></div></div><div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mt-5"><div><p class="text-xs text-slate-500">Serviceable</p><p class="text-xl font-bold text-green-600 mt-1">41</p></div><div><p class="text-xs text-slate-500">Maintenance</p><p class="text-xl font-bold text-yellow-600 mt-1">05</p></div><div><p class="text-xs text-slate-500">Unresolved Issues</p><p class="text-xl font-bold text-[#8B1E23] mt-1">02</p></div></div></section>
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
