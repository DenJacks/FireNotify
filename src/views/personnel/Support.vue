<template>
  <div class="w-full min-w-0 space-y-6">
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">
        <div>
          <p class="text-sm font-semibold text-[#8B1E23]">FIRENOTIFY PERSONNEL PORTAL</p>
          <h2 class="text-2xl font-bold text-slate-900 mt-1">Support Center</h2>
          <p class="text-sm text-slate-500 mt-1">Get help with tasks, reports, activities, equipment, and your personnel account.</p>
        </div>
        <div class="h-14 w-14 rounded-2xl bg-[#8B1E23]/10 flex items-center justify-center"><span v-html="ICONS.support" class="h-8 w-8 text-[#8B1E23]"></span></div>
      </div>
    </section>

    <section class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-5">
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><div class="flex items-center gap-3"><div class="h-11 w-11 rounded-xl bg-blue-50 flex items-center justify-center"><span v-html="ICONS.tasks" class="h-5 w-5 text-blue-600"></span></div><div><p class="text-sm font-bold text-slate-900">Task Help</p><p class="text-xs text-slate-500 mt-1">Assignments and status updates</p></div></div></div>
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><div class="flex items-center gap-3"><div class="h-11 w-11 rounded-xl bg-green-50 flex items-center justify-center"><span v-html="ICONS.reports" class="h-5 w-5 text-green-600"></span></div><div><p class="text-sm font-bold text-slate-900">Report Help</p><p class="text-xs text-slate-500 mt-1">Submission and corrections</p></div></div></div>
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><div class="flex items-center gap-3"><div class="h-11 w-11 rounded-xl bg-yellow-50 flex items-center justify-center"><span v-html="ICONS.clock" class="h-5 w-5 text-yellow-600"></span></div><div><p class="text-sm font-bold text-slate-900">Activity Help</p><p class="text-xs text-slate-500 mt-1">Schedules and duty activities</p></div></div></div>
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><div class="flex items-center gap-3"><div class="h-11 w-11 rounded-xl bg-red-50 flex items-center justify-center"><span v-html="ICONS.siren" class="h-5 w-5 text-[#8B1E23]"></span></div><div><p class="text-sm font-bold text-slate-900">Urgent Support</p><p class="text-xs text-slate-500 mt-1">Immediate station assistance</p></div></div></div>
    </section>

    <section class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="lg:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="border-b border-slate-200 pb-4"><h3 class="text-lg font-bold text-slate-900">Frequently Asked Questions</h3><p class="text-sm text-slate-500 mt-1">Quick answers for common portal tasks</p></div>
        <div class="mt-5 space-y-3">
          <details class="p-4 rounded-xl border border-slate-200 bg-slate-50"><summary class="font-semibold text-slate-900 cursor-pointer">How do I update a task status?</summary><p class="text-sm text-slate-500 mt-3">Open Tasks from the sidebar, select the assignment, and use Update Status after completing the required duty.</p></details>
          <details class="p-4 rounded-xl border border-slate-200 bg-slate-50"><summary class="font-semibold text-slate-900 cursor-pointer">How do I submit a report?</summary><p class="text-sm text-slate-500 mt-3">Open Reports, choose the pending report, and select Submit Report. Attach the required documentation before sending it.</p></details>
          <details class="p-4 rounded-xl border border-slate-200 bg-slate-50"><summary class="font-semibold text-slate-900 cursor-pointer">What should I do when equipment is damaged?</summary><p class="text-sm text-slate-500 mt-3">Open Equipment Audit and record the item condition, issue details, and required maintenance or replacement action.</p></details>
          <details class="p-4 rounded-xl border border-slate-200 bg-slate-50"><summary class="font-semibold text-slate-900 cursor-pointer">Where can I view station duty records?</summary><p class="text-sm text-slate-500 mt-3">Open Station Duty Log to review shifts, attendance, logged activities, and pending entries.</p></details>
        </div>
      </div>

      <div class="space-y-6">
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Contact Support</h3><p class="text-sm text-slate-500 mt-1">Our station support team can assist with portal issues.</p><div class="mt-5 space-y-4"><div><p class="text-xs text-slate-500">Support Officer</p><p class="font-semibold text-slate-900 mt-1">BFP Balingasag Station Office</p></div><div><p class="text-xs text-slate-500">Office Hours</p><p class="font-semibold text-slate-900 mt-1">Monday - Friday · 08:00 AM - 05:00 PM</p></div><div><p class="text-xs text-slate-500">Response Time</p><p class="font-semibold text-green-600 mt-1">Usually within one business day</p></div></div></div>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><div class="border-b border-slate-200 pb-4"><h3 class="text-lg font-bold text-slate-900">Submit a Support Request</h3><p class="text-sm text-slate-500 mt-1">Describe the issue so the support team can assist you.</p></div><div class="mt-5 grid grid-cols-1 lg:grid-cols-2 gap-4"><div><label class="text-sm font-semibold text-slate-700">Issue Type</label><select class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm text-slate-700"><option>Select issue type</option><option>Account Access</option><option>Task or Activity</option><option>Report Submission</option><option>Equipment Record</option><option>Other</option></select></div><div><label class="text-sm font-semibold text-slate-700">Priority</label><select class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm text-slate-700"><option>Normal</option><option>High</option><option>Urgent</option></select></div><div class="lg:col-span-2"><label class="text-sm font-semibold text-slate-700">Message</label><textarea rows="4" placeholder="Describe your concern..." class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm outline-none focus:ring-2 focus:ring-[#8B1E23]/20"></textarea></div></div><button class="mt-5 px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]">Send Support Request</button></section>
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
