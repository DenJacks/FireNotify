<template>
  <div class="w-full min-w-0 space-y-7">
    <section class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">
        <div>
          <p class="text-sm font-medium text-[#8B1E23] mb-1">FIRENOTIFY PERSONNEL PORTAL</p>
          <h2 class="text-2xl lg:text-3xl font-bold text-slate-900">
            Welcome back, {{ currentUser?.firstName || 'Juan' }}!
          </h2>
          <p class="mt-2 text-base text-slate-500">Monitor your assigned tasks, reports, and station activities.</p>
        </div>

        <div class="flex items-center gap-3 px-5 py-4 rounded-xl bg-[#8B1E23] text-white">
          <div class="h-11 w-11 rounded-full bg-white/10 flex items-center justify-center">
            <span v-html="ICONS.siren" class="h-6 w-6 text-[#F4C542]"></span>
          </div>
          <div>
            <p class="text-xs text-white/70">Current Status</p>
            <p class="text-base font-bold">On Duty</p>
          </div>
        </div>
      </div>
    </section>

    <section class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-5">
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-slate-500">Today's Tasks</p>
            <p class="text-3xl font-bold text-slate-900 mt-2">04</p>
            <p class="text-xs text-blue-600 font-semibold mt-2">2 pending</p>
          </div>
          <div class="h-12 w-12 rounded-xl bg-blue-50 flex items-center justify-center">
            <span v-html="ICONS.tasks" class="h-6 w-6 text-blue-600"></span>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-slate-500">Completed</p>
            <p class="text-3xl font-bold text-slate-900 mt-2">06</p>
            <p class="text-xs text-green-600 font-semibold mt-2">This week</p>
          </div>
          <div class="h-12 w-12 rounded-xl bg-green-50 flex items-center justify-center">
            <span class="text-xl text-green-600">&#10003;</span>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-slate-500">Reports To Submit</p>
            <p class="text-3xl font-bold text-slate-900 mt-2">03</p>
            <p class="text-xs text-yellow-600 font-semibold mt-2">Needs attention</p>
          </div>
          <div class="h-12 w-12 rounded-xl bg-yellow-50 flex items-center justify-center">
            <span v-html="ICONS.reports" class="h-6 w-6 text-yellow-600"></span>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-slate-500">Urgent</p>
            <p class="text-3xl font-bold text-slate-900 mt-2">02</p>
            <p class="text-xs text-red-600 font-semibold mt-2">Immediate action</p>
          </div>
          <div class="h-12 w-12 rounded-xl bg-red-50 flex items-center justify-center">
            <span class="text-xl text-red-600">!</span>
          </div>
        </div>
      </div>
    </section>

    <section class="grid grid-cols-1 xl:grid-cols-3 gap-6">
      <div class="xl:col-span-2 space-y-6">
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
          <div class="flex items-center justify-between border-b border-slate-200 pb-5">
            <div>
              <h2 class="text-xl font-bold text-slate-900">Today's Assignment</h2>
              <p class="text-sm text-slate-500 mt-1">Your scheduled duty for today</p>
            </div>
            <span class="px-3 py-1 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">09:00 AM</span>
          </div>
          <div class="mt-5 p-5 rounded-xl bg-blue-50 border border-blue-100">
            <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
              <div>
                <p class="text-sm font-semibold text-blue-700">FIRE SAFETY INSPECTION</p>
                <h3 class="text-lg font-bold text-slate-900 mt-1">Public Market Complex</h3>
                <p class="text-sm text-slate-500 mt-2">Scheduled inspection and fire safety compliance checking.</p>
              </div>
              <button class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]">View Task</button>
            </div>
          </div>
        </div>

        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
          <div class="border-b border-slate-200 pb-5">
            <h2 class="text-xl font-bold text-slate-900">Upcoming Activities</h2>
            <p class="text-sm text-slate-500 mt-1">Your next scheduled station activities</p>
          </div>
          <div class="mt-5 space-y-4">
            <div class="flex items-center gap-4 p-4 rounded-xl border border-slate-200">
              <div class="h-12 w-12 rounded-xl bg-red-50 flex items-center justify-center shrink-0"><span v-html="ICONS.clock" class="h-6 w-6 text-[#8B1E23]"></span></div>
              <div class="flex-1"><p class="font-bold text-slate-900">Fire Drill Evaluation</p><p class="text-sm text-slate-500 mt-1">Tomorrow · 08:30 AM</p></div>
              <span class="px-3 py-1 rounded-full bg-yellow-50 text-yellow-700 text-xs font-bold">Upcoming</span>
            </div>
            <div class="flex items-center gap-4 p-4 rounded-xl border border-slate-200">
              <div class="h-12 w-12 rounded-xl bg-green-50 flex items-center justify-center shrink-0"><span v-html="ICONS.reports" class="h-6 w-6 text-green-600"></span></div>
              <div class="flex-1"><p class="font-bold text-slate-900">Monthly Station Report</p><p class="text-sm text-slate-500 mt-1">September 15 · 04:00 PM</p></div>
              <span class="px-3 py-1 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">Scheduled</span>
            </div>
            <div class="flex items-center gap-4 p-4 rounded-xl border border-slate-200">
              <div class="h-12 w-12 rounded-xl bg-purple-50 flex items-center justify-center shrink-0"><span v-html="ICONS.roster" class="h-6 w-6 text-purple-600"></span></div>
              <div class="flex-1"><p class="font-bold text-slate-900">Personnel Training</p><p class="text-sm text-slate-500 mt-1">September 18 · 09:00 AM</p></div>
              <span class="px-3 py-1 rounded-full bg-purple-50 text-purple-700 text-xs font-bold">Training</span>
            </div>
          </div>
        </div>

        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
          <div class="border-b border-slate-200 pb-5">
            <h2 class="text-xl font-bold text-slate-900">Recent Task Activity</h2>
            <p class="text-sm text-slate-500 mt-1">Recent updates on your assigned duties</p>
          </div>
          <div class="mt-5 space-y-4">
            <div class="flex items-start gap-4"><div class="h-10 w-10 rounded-full bg-green-100 flex items-center justify-center"><span class="text-green-600 font-bold">&#10003;</span></div><div><p class="text-sm font-semibold text-slate-900">Fire Safety Inspection completed</p><p class="text-xs text-slate-500 mt-1">Today · 10:42 AM</p></div></div>
            <div class="flex items-start gap-4"><div class="h-10 w-10 rounded-full bg-blue-100 flex items-center justify-center"><span class="text-blue-600 font-bold">&#8635;</span></div><div><p class="text-sm font-semibold text-slate-900">Emergency Response Drill updated</p><p class="text-xs text-slate-500 mt-1">Yesterday · 03:20 PM</p></div></div>
            <div class="flex items-start gap-4"><div class="h-10 w-10 rounded-full bg-yellow-100 flex items-center justify-center"><span class="text-yellow-600 font-bold">!</span></div><div><p class="text-sm font-semibold text-slate-900">Monthly report requires submission</p><p class="text-xs text-slate-500 mt-1">Yesterday · 01:15 PM</p></div></div>
          </div>
        </div>
      </div>

      <div class="space-y-6">
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
          <h2 class="text-lg font-bold text-slate-900">Duty Status</h2>
          <div class="mt-5 p-5 rounded-xl bg-green-50 border border-green-100">
            <div class="flex items-center gap-3"><div class="h-3 w-3 rounded-full bg-green-500"></div><p class="font-bold text-green-700">Currently On Duty</p></div>
            <p class="text-sm text-slate-500 mt-3">Station 1 · BFP Balingasag</p><p class="text-sm text-slate-500 mt-1">Shift: 08:00 AM – 05:00 PM</p>
          </div>
        </div>

        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
          <h2 class="text-lg font-bold text-slate-900">Weekly Progress</h2><p class="text-sm text-slate-500 mt-1">Task completion this week</p>
          <div class="mt-5"><div class="flex items-center justify-between text-sm mb-2"><span class="font-medium text-slate-600">Completed Tasks</span><span class="font-bold text-slate-900">75%</span></div><div class="h-3 bg-slate-100 rounded-full overflow-hidden"><div class="h-full bg-[#8B1E23] rounded-full" style="width: 75%"></div></div><p class="text-xs text-slate-500 mt-3">6 of 8 assigned tasks completed</p></div>
        </div>

        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
          <h2 class="text-lg font-bold text-slate-900">Station Information</h2>
          <div class="mt-5 space-y-4"><div><p class="text-xs text-slate-500">Station</p><p class="font-semibold text-slate-900 mt-1">BFP Balingasag</p></div><div><p class="text-xs text-slate-500">Personnel Position</p><p class="font-semibold text-slate-900 mt-1">Fire Officer</p></div><div><p class="text-xs text-slate-500">Station Contact</p><p class="font-semibold text-slate-900 mt-1">BFP Station Office</p></div></div>
        </div>

        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
          <div class="flex items-center justify-between"><h2 class="text-lg font-bold text-slate-900">Notifications</h2><span class="px-2 py-1 rounded-full bg-red-50 text-red-700 text-xs font-bold">3 New</span></div>
          <div class="mt-5 space-y-4"><div class="p-3 rounded-xl bg-red-50"><p class="text-sm font-semibold text-slate-900">Task deadline approaching</p><p class="text-xs text-slate-500 mt-1">Monthly report is due tomorrow.</p></div><div class="p-3 rounded-xl bg-blue-50"><p class="text-sm font-semibold text-slate-900">New task assigned</p><p class="text-xs text-slate-500 mt-1">Fire drill evaluation has been assigned.</p></div><div class="p-3 rounded-xl bg-yellow-50"><p class="text-sm font-semibold text-slate-900">Reminder</p><p class="text-xs text-slate-500 mt-1">Personnel training is scheduled this week.</p></div></div>
        </div>

        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
          <h2 class="text-lg font-bold text-slate-900">Quick Actions</h2>
          <div class="mt-5 grid grid-cols-2 gap-3"><button class="p-4 rounded-xl border border-slate-200 hover:bg-slate-50 text-left"><p class="text-sm font-bold text-slate-900">View Tasks</p><p class="text-xs text-slate-500 mt-1">Check assignments</p></button><button class="p-4 rounded-xl border border-slate-200 hover:bg-slate-50 text-left"><p class="text-sm font-bold text-slate-900">Submit Report</p><p class="text-xs text-slate-500 mt-1">Upload report</p></button><button class="p-4 rounded-xl border border-slate-200 hover:bg-slate-50 text-left"><p class="text-sm font-bold text-slate-900">Activities</p><p class="text-xs text-slate-500 mt-1">View schedule</p></button><button class="p-4 rounded-xl border border-slate-200 hover:bg-slate-50 text-left"><p class="text-sm font-bold text-slate-900">Notifications</p><p class="text-xs text-slate-500 mt-1">View alerts</p></button></div>
        </div>
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
