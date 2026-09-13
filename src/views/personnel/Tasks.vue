<template>
  <div class="w-full min-w-0 space-y-6">
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">
        <div>
          <p class="text-sm font-bold text-[#8B1E23]">FIRENOTIFY PERSONNEL PORTAL</p>
          <h2 class="text-2xl font-bold text-slate-900 mt-1">Assigned Tasks</h2>
          <p class="text-sm text-slate-500 mt-1">Monitor and manage your assigned duties and activities.</p>
        </div>

        <button class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]">+ View All Tasks</button>
      </div>
    </section>

    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-slate-500">Total Tasks</p>
            <p class="text-3xl font-bold text-slate-900 mt-1">09</p>
          </div>
          <div class="h-12 w-12 rounded-xl bg-blue-50 flex items-center justify-center">
            <span v-html="ICONS.tasks" class="h-6 w-6 text-blue-600"></span>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-slate-500">Pending</p>
            <p class="text-3xl font-bold text-amber-600 mt-1">04</p>
          </div>
          <div class="h-12 w-12 rounded-xl bg-amber-50 flex items-center justify-center">
            <span class="text-xl">⏳</span>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-slate-500">Completed</p>
            <p class="text-3xl font-bold text-green-600 mt-1">05</p>
          </div>
          <div class="h-12 w-12 rounded-xl bg-green-50 flex items-center justify-center">
            <span class="text-xl">✓</span>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-slate-500">Overdue</p>
            <p class="text-3xl font-bold text-red-600 mt-1">02</p>
          </div>
          <div class="h-12 w-12 rounded-xl bg-red-50 flex items-center justify-center">
            <span class="text-xl">!</span>
          </div>
        </div>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">
      <div class="flex flex-col lg:flex-row gap-4 lg:items-center lg:justify-between">
        <div>
          <h3 class="font-bold text-slate-900">Task List</h3>
          <p class="text-sm text-slate-500">Review your current assignments.</p>
        </div>

        <div class="flex flex-col sm:flex-row gap-3">
          <select class="px-4 py-3 rounded-xl border border-slate-300 text-sm font-medium bg-white">
            <option>All Tasks</option>
            <option>Pending</option>
            <option>Completed</option>
            <option>Overdue</option>
          </select>

          <select class="px-4 py-3 rounded-xl border border-slate-300 text-sm font-medium bg-white">
            <option>All Priorities</option>
            <option>High Priority</option>
            <option>Medium Priority</option>
            <option>Low Priority</option>
          </select>
        </div>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex items-center justify-between border-b border-slate-200 pb-5">
        <div>
          <h3 class="text-xl font-bold text-slate-900">Current Assignments</h3>
          <p class="text-sm text-slate-500 mt-1">Tasks assigned to your personnel account.</p>
        </div>

        <span class="px-4 py-2 rounded-full bg-blue-50 text-blue-700 text-sm font-bold">09 Total</span>
      </div>

      <div class="mt-5 space-y-4">
        <div v-for="task in taskList" :key="task.title" class="p-5 rounded-xl border border-slate-200 bg-slate-50 hover:border-[#8B1E23] transition">
          <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">
            <div class="flex items-start gap-4">
              <div class="h-12 w-12 rounded-xl bg-blue-100 flex items-center justify-center shrink-0">
                <span v-html="ICONS.tasks" class="h-6 w-6 text-blue-600"></span>
              </div>

              <div>
                <div class="flex flex-wrap items-center gap-2">
                  <p class="text-base font-bold text-slate-900">{{ task.title }}</p>
                  <span class="px-2.5 py-1 rounded-full bg-amber-100 text-amber-700 text-xs font-bold">Pending</span>
                </div>

                <p class="text-sm text-slate-500 mt-1">Due: {{ task.due }}</p>
                <p class="text-sm text-slate-500 mt-1">Assigned to BFP Balingasag Station</p>
              </div>
            </div>

            <div class="flex flex-col sm:flex-row gap-3">
              <button class="px-4 py-3 rounded-xl border border-slate-300 bg-white text-slate-700 text-sm font-bold hover:bg-slate-100">View Details</button>
              <button class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]">Update Status</button>
            </div>
          </div>

          <div class="mt-5">
            <div class="flex justify-between mb-2">
              <span class="text-xs font-semibold text-slate-500">Task Progress</span>
              <span class="text-xs font-bold text-slate-700">60%</span>
            </div>

            <div class="w-full h-2.5 bg-slate-200 rounded-full overflow-hidden">
              <div class="h-full bg-[#8B1E23] rounded-full" style="width: 60%"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <h3 class="text-lg font-bold text-slate-900">Today's Priority</h3>
        <p class="text-sm text-slate-500 mt-1">Tasks that require immediate attention.</p>

        <div class="mt-5 space-y-4">
          <div class="p-4 rounded-xl bg-red-50 border border-red-100">
            <div class="flex items-start gap-3">
              <span class="text-red-600 font-bold text-lg">!</span>
              <div>
                <p class="font-bold text-slate-900">Fire Safety Inspection</p>
                <p class="text-sm text-slate-500 mt-1">Public Market Complex</p>
                <p class="text-xs text-red-600 font-bold mt-2">Due Today • 09:00 AM</p>
              </div>
            </div>
          </div>

          <div class="p-4 rounded-xl bg-amber-50 border border-amber-100">
            <div class="flex items-start gap-3">
              <span class="text-amber-600 font-bold text-lg">!</span>
              <div>
                <p class="font-bold text-slate-900">Monthly Activity Report</p>
                <p class="text-sm text-slate-500 mt-1">Submit station activity report</p>
                <p class="text-xs text-amber-600 font-bold mt-2">Due Tomorrow</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <h3 class="text-lg font-bold text-slate-900">Recently Completed</h3>
        <p class="text-sm text-slate-500 mt-1">Your latest completed assignments.</p>

        <div class="mt-5 space-y-4">
          <div class="flex items-center gap-4 p-4 rounded-xl bg-green-50">
            <div class="h-10 w-10 rounded-full bg-green-100 flex items-center justify-center">
              <span class="text-green-600 font-bold">✓</span>
            </div>
            <div>
              <p class="font-bold text-slate-900">Fire Drill Evaluation</p>
              <p class="text-xs text-slate-500 mt-1">Completed today</p>
            </div>
          </div>

          <div class="flex items-center gap-4 p-4 rounded-xl bg-green-50">
            <div class="h-10 w-10 rounded-full bg-green-100 flex items-center justify-center">
              <span class="text-green-600 font-bold">✓</span>
            </div>
            <div>
              <p class="font-bold text-slate-900">Equipment Inspection</p>
              <p class="text-xs text-slate-500 mt-1">Completed yesterday</p>
            </div>
          </div>
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
  },
  taskList: {
    type: Array,
    required: false,
    default: () => []
  }
})
</script>
