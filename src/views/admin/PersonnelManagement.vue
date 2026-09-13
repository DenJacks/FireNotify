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
          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">Personnel Management</p>
          <h2 class="text-2xl font-bold text-slate-900 mt-1">Station Personnel</h2>
          <p class="text-base text-slate-500 mt-1">Manage personnel records, ranks, assignments, and duty status.</p>
        </div>

        <button class="px-6 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition">
          + Add Personnel
        </button>
      </div>
    </section>

    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-slate-900">48</p>
        <p class="text-sm text-slate-500 mt-1">Total Personnel</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">41</p>
        <p class="text-sm text-slate-500 mt-1">On Duty</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">05</p>
        <p class="text-sm text-slate-500 mt-1">On Leave</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-slate-500">02</p>
        <p class="text-sm text-slate-500 mt-1">Off Duty</p>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">
      <div class="flex flex-col md:flex-row gap-4">
        <input type="text" placeholder="Search name, rank, or position..." class="flex-1 h-12 px-4 rounded-xl border border-slate-300 text-base focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]" />
        <select class="h-12 px-4 rounded-xl border border-slate-300 text-base">
          <option>All Duty Status</option>
          <option>On Duty</option>
          <option>Off Duty</option>
          <option>On Leave</option>
        </select>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="overflow-x-auto">
        <table class="w-full text-left">
          <thead>
            <tr class="border-b border-slate-200 text-xs font-bold uppercase tracking-wide text-slate-400">
              <th class="pb-4 pr-5">Personnel</th>
              <th class="pb-4 pr-5">Rank</th>
              <th class="pb-4 pr-5">Position</th>
              <th class="pb-4 pr-5">Shift</th>
              <th class="pb-4 text-right">Duty Status</th>
            </tr>
          </thead>

          <tbody class="divide-y divide-slate-100">
            <tr class="hover:bg-slate-50">
              <td class="py-5 pr-5">
                <div class="flex items-center gap-3">
                  <div class="h-11 w-11 rounded-full bg-[#8B1E23] text-white flex items-center justify-center text-xs font-bold">FO3</div>
                  <div>
                    <p class="font-bold text-slate-900">Juan Dela Cruz</p>
                    <p class="text-xs text-slate-500">Personnel ID: BFP-001</p>
                  </div>
                </div>
              </td>
              <td class="py-5 pr-5 text-sm text-slate-600">FO3</td>
              <td class="py-5 pr-5 text-sm text-slate-600">Fire Officer</td>
              <td class="py-5 pr-5 text-sm text-slate-600">Morning</td>
              <td class="py-5 text-right">
                <span class="px-3 py-1.5 rounded-full bg-green-50 text-green-700 text-xs font-bold">ON DUTY</span>
              </td>
            </tr>

            <tr class="hover:bg-slate-50">
              <td class="py-5 pr-5">
                <div class="flex items-center gap-3">
                  <div class="h-11 w-11 rounded-full bg-[#8B1E23] text-white flex items-center justify-center text-xs font-bold">SFO1</div>
                  <div>
                    <p class="font-bold text-slate-900">Maria Santos</p>
                    <p class="text-xs text-slate-500">Personnel ID: BFP-002</p>
                  </div>
                </div>
              </td>
              <td class="py-5 pr-5 text-sm text-slate-600">SFO1</td>
              <td class="py-5 pr-5 text-sm text-slate-600">Senior Fire Officer</td>
              <td class="py-5 pr-5 text-sm text-slate-600">Afternoon</td>
              <td class="py-5 text-right">
                <span class="px-3 py-1.5 rounded-full bg-green-50 text-green-700 text-xs font-bold">ON DUTY</span>
              </td>
            </tr>

            <tr class="hover:bg-slate-50">
              <td class="py-5 pr-5">
                <div class="flex items-center gap-3">
                  <div class="h-11 w-11 rounded-full bg-[#8B1E23] text-white flex items-center justify-center text-xs font-bold">FO2</div>
                  <div>
                    <p class="font-bold text-slate-900">Roberto Reyes</p>
                    <p class="text-xs text-slate-500">Personnel ID: BFP-003</p>
                  </div>
                </div>
              </td>
              <td class="py-5 pr-5 text-sm text-slate-600">FO2</td>
              <td class="py-5 pr-5 text-sm text-slate-600">Fire Officer</td>
              <td class="py-5 pr-5 text-sm text-slate-600">Night</td>
              <td class="py-5 text-right">
                <span class="px-3 py-1.5 rounded-full bg-yellow-50 text-yellow-700 text-xs font-bold">ON LEAVE</span>
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
            <h2 class="text-xl font-bold text-slate-900">Recent Assignments</h2>
            <p class="text-sm text-slate-500 mt-1">Latest assignments and role changes</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">Juan Dela Cruz</p>
                <p class="text-xs text-slate-500 mt-1">Assigned to Fire Safety Inspection Team</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">Assigned</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">Roberto Reyes</p>
                <p class="text-xs text-slate-500 mt-1">Transferred to Night Shift Dispatch Support</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-green-100 text-green-700 text-xs font-bold">Updated</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">Maria Santos</p>
                <p class="text-xs text-slate-500 mt-1">Promoted as Operations Lead for community drills</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">Promotion</span>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Team Availability</h2>
            <p class="text-sm text-slate-500 mt-1">Current staffing by shift</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Morning Shift</p>
                <p class="text-xs text-slate-500 mt-1">18 personnel assigned</p>
              </div>
              <span class="text-sm font-bold text-green-600">Fully Staffed</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Afternoon Shift</p>
                <p class="text-xs text-slate-500 mt-1">15 personnel assigned</p>
              </div>
              <span class="text-sm font-bold text-blue-600">On Schedule</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Night Shift</p>
                <p class="text-xs text-slate-500 mt-1">12 personnel assigned</p>
              </div>
              <span class="text-sm font-bold text-yellow-600">Low Coverage</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex items-center justify-between border-b border-slate-200 pb-5">
        <div>
          <h2 class="text-xl font-bold text-slate-900">Personnel Notes</h2>
          <p class="text-sm text-slate-500 mt-1">Admin reminders and coordination updates</p>
        </div>
      </div>

      <div class="mt-5 space-y-4">
        <div class="p-4 rounded-xl border border-emerald-200 bg-emerald-50">
          <p class="text-sm font-bold text-slate-900">Training Readiness</p>
          <p class="text-sm text-slate-600 mt-1">All new trainees have completed orientation and are scheduled for field drills next week.</p>
        </div>

        <div class="p-4 rounded-xl border border-orange-200 bg-orange-50">
          <p class="text-sm font-bold text-slate-900">Coverage Alert</p>
          <p class="text-sm text-slate-600 mt-1">Night shift requires two additional personnel for full emergency response coverage.</p>
        </div>

        <div class="p-4 rounded-xl border border-indigo-200 bg-indigo-50">
          <p class="text-sm font-bold text-slate-900">Leave Management</p>
          <p class="text-sm text-slate-600 mt-1">Two approved leave requests are scheduled this week and have been covered by backup assignments.</p>
        </div>
      </div>
    </section>
  </div>
</template>
