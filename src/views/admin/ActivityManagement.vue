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
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
        <div>
          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">Operations Management</p>
          <h2 class="text-2xl font-bold text-slate-900 mt-1">Activity Management</h2>
          <p class="text-base text-slate-500 mt-1">Create, schedule, assign, and monitor station activities.</p>
        </div>

        <button class="px-6 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition">
          + Create New Activity
        </button>
      </div>
    </section>

    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-slate-900">08</p>
        <p class="text-sm text-slate-500 mt-1">Today's Activities</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-blue-600">05</p>
        <p class="text-sm text-slate-500 mt-1">Scheduled</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">18</p>
        <p class="text-sm text-slate-500 mt-1">Completed</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">02</p>
        <p class="text-sm text-slate-500 mt-1">Delayed</p>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <input type="text" placeholder="Search activity..." class="h-12 px-4 rounded-xl border border-slate-300 text-base focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]" />
        <select class="h-12 px-4 rounded-xl border border-slate-300 text-base focus:outline-none focus:ring-2 focus:ring-red-200">
          <option>All Activity Types</option>
          <option>Inspection</option>
          <option>Fire Drill</option>
          <option>Training</option>
          <option>Emergency Response</option>
        </select>
        <select class="h-12 px-4 rounded-xl border border-slate-300 text-base focus:outline-none focus:ring-2 focus:ring-red-200">
          <option>All Status</option>
          <option>Scheduled</option>
          <option>Ongoing</option>
          <option>Completed</option>
          <option>Delayed</option>
        </select>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="overflow-x-auto">
        <table class="w-full text-left">
          <thead>
            <tr class="border-b border-slate-200 text-xs font-bold uppercase tracking-wide text-slate-400">
              <th class="pb-4 pr-5">Activity</th>
              <th class="pb-4 pr-5">Type</th>
              <th class="pb-4 pr-5">Assigned Personnel</th>
              <th class="pb-4 pr-5">Schedule</th>
              <th class="pb-4 pr-5">Priority</th>
              <th class="pb-4 text-right">Status</th>
            </tr>
          </thead>

          <tbody class="divide-y divide-slate-100">
            <tr class="hover:bg-slate-50">
              <td class="py-5 pr-5">
                <p class="font-bold text-slate-900">Fire Safety Inspection</p>
                <p class="text-xs text-slate-400 mt-1">ACT-001</p>
              </td>
              <td class="py-5 pr-5 text-sm text-slate-600">Inspection</td>
              <td class="py-5 pr-5 text-sm text-slate-600">5 Personnel</td>
              <td class="py-5 pr-5 text-sm text-slate-600">Sept. 9, 2026</td>
              <td class="py-5 pr-5">
                <span class="px-3 py-1.5 rounded-full bg-red-50 text-[#8B1E23] text-xs font-bold">HIGH</span>
              </td>
              <td class="py-5 text-right">
                <span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">ONGOING</span>
              </td>
            </tr>

            <tr class="hover:bg-slate-50">
              <td class="py-5 pr-5">
                <p class="font-bold text-slate-900">Community Fire Drill</p>
                <p class="text-xs text-slate-400 mt-1">ACT-002</p>
              </td>
              <td class="py-5 pr-5 text-sm text-slate-600">Fire Drill</td>
              <td class="py-5 pr-5 text-sm text-slate-600">8 Personnel</td>
              <td class="py-5 pr-5 text-sm text-slate-600">Sept. 10, 2026</td>
              <td class="py-5 pr-5">
                <span class="px-3 py-1.5 rounded-full bg-yellow-50 text-yellow-700 text-xs font-bold">MEDIUM</span>
              </td>
              <td class="py-5 text-right">
                <span class="px-3 py-1.5 rounded-full bg-yellow-50 text-yellow-700 text-xs font-bold">SCHEDULED</span>
              </td>
            </tr>

            <tr class="hover:bg-slate-50">
              <td class="py-5 pr-5">
                <p class="font-bold text-slate-900">Station Equipment Inspection</p>
                <p class="text-xs text-slate-400 mt-1">ACT-003</p>
              </td>
              <td class="py-5 pr-5 text-sm text-slate-600">Inspection</td>
              <td class="py-5 pr-5 text-sm text-slate-600">4 Personnel</td>
              <td class="py-5 pr-5 text-sm text-slate-600">Sept. 11, 2026</td>
              <td class="py-5 pr-5">
                <span class="px-3 py-1.5 rounded-full bg-green-50 text-green-700 text-xs font-bold">LOW</span>
              </td>
              <td class="py-5 text-right">
                <span class="px-3 py-1.5 rounded-full bg-yellow-50 text-yellow-700 text-xs font-bold">SCHEDULED</span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Planned Activities</h2>
            <p class="text-sm text-slate-500 mt-1">Upcoming schedule for the next 7 days</p>
          </div>
          <span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">06 ITEMS</span>
        </div>

        <div class="mt-5 space-y-4">
          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">Vehicle Maintenance Check</p>
                <p class="text-xs text-slate-500 mt-1">Sept. 14 • 9:00 AM</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">Planned</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">Barangay Rescue Coordination Drill</p>
                <p class="text-xs text-slate-500 mt-1">Sept. 15 • 1:30 PM</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">Prepared</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">High-rise Building Inspection</p>
                <p class="text-xs text-slate-500 mt-1">Sept. 16 • 8:00 AM</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-green-100 text-green-700 text-xs font-bold">Confirmed</span>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Workload Summary</h2>
            <p class="text-sm text-slate-500 mt-1">Personnel allocation by activity type</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Inspections</span>
              <span>48%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[48%] rounded-full bg-[#8B1E23]"></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Drills</span>
              <span>29%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[29%] rounded-full bg-blue-500"></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Training</span>
              <span>17%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[17%] rounded-full bg-green-500"></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Response Ops</span>
              <span>06%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[6%] rounded-full bg-yellow-500"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex items-center justify-between border-b border-slate-200 pb-5">
        <div>
          <h2 class="text-xl font-bold text-slate-900">Activity Notes</h2>
          <p class="text-sm text-slate-500 mt-1">Additional reminders for team coordination</p>
        </div>
      </div>

      <div class="mt-5 space-y-4">
        <div class="p-4 rounded-xl border border-lime-200 bg-lime-50">
          <p class="text-sm font-bold text-slate-900">Reminder</p>
          <p class="text-sm text-slate-600 mt-1">All inspection teams must bring updated checklist forms before deployment.</p>
        </div>

        <div class="p-4 rounded-xl border border-amber-200 bg-amber-50">
          <p class="text-sm font-bold text-slate-900">Coordination</p>
          <p class="text-sm text-slate-600 mt-1">Coordinate with the barangay office for drill participation and crowd control support.</p>
        </div>

        <div class="p-4 rounded-xl border border-sky-200 bg-sky-50">
          <p class="text-sm font-bold text-slate-900">Escalation</p>
          <p class="text-sm text-slate-600 mt-1">Any delay in scheduled drills must be logged and escalated to the operations section chief.</p>
        </div>
      </div>
    </section>
  </div>
</template>
