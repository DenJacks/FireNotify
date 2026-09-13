<script setup>
defineProps({
  currentUser: {
    type: Object,
    default: null
  }
})
</script>

<template>
  <div class="space-y-7">
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-7">
      <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">
        Administrator Dashboard
      </p>

      <h2 class="text-3xl font-bold text-slate-900 mt-2">
        Good day, {{ currentUser?.name || 'Administrator' }}!
      </h2>

      <p class="text-base text-slate-500 mt-2">
        Monitor personnel, activities, reports, deadlines, and station
        compliance from one place.
      </p>
    </section>

    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
      <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm">
        <div class="flex items-center justify-between">
          <div class="h-12 w-12 rounded-xl bg-green-50 flex items-center justify-center">
            <svg class="w-6 h-6 fill-current text-green-600" viewBox="0 0 24 24">
              <path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5s-3 1.34-3 3 1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5C15 14.17 10.33 13 8 13zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/>
            </svg>
          </div>
          <span class="px-3 py-1 rounded-full bg-green-50 text-green-700 text-xs font-bold">ACTIVE</span>
        </div>
        <p class="mt-5 text-4xl font-bold text-slate-900">48</p>
        <p class="mt-1 text-base text-slate-500">Active Personnel</p>
        <p class="mt-3 text-sm font-semibold text-green-600">All shifts covered</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm">
        <div class="flex items-center justify-between">
          <div class="h-12 w-12 rounded-xl bg-yellow-50 flex items-center justify-center">
            <svg class="w-6 h-6 fill-current text-yellow-600" viewBox="0 0 24 24">
              <path d="M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1 1.9 2 2 2h12c1.1 0 2-.9 2-2V8l-6-6zM15 9V3.5L18.5 9H15zM8 13h8v2H8v-2zm0 4h8v2H8v-2z"/>
            </svg>
          </div>
          <span class="px-3 py-1 rounded-full bg-yellow-50 text-yellow-700 text-xs font-bold">REVIEW</span>
        </div>
        <p class="mt-5 text-4xl font-bold text-slate-900">12</p>
        <p class="mt-1 text-base text-slate-500">Pending Reports</p>
        <p class="mt-3 text-sm font-semibold text-yellow-700">Requires review</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm">
        <div class="flex items-center justify-between">
          <div class="h-12 w-12 rounded-xl bg-red-50 flex items-center justify-center">
            <svg class="w-6 h-6 fill-current text-[#8B1E23]" viewBox="0 0 24 24">
              <path d="M1 21h22L12 2 1 21zm12-3h-2v2h2v-2zm0-2h-2v-4h2v4z"/>
            </svg>
          </div>
          <span class="px-3 py-1 rounded-full bg-red-50 text-[#8B1E23] text-xs font-bold">ALERT</span>
        </div>
        <p class="mt-5 text-4xl font-bold text-[#8B1E23]">02</p>
        <p class="mt-1 text-base text-slate-500">Overdue Deadlines</p>
        <p class="mt-3 text-sm font-semibold text-[#8B1E23]">Immediate attention</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm">
        <div class="flex items-center justify-between">
          <div class="h-12 w-12 rounded-xl bg-blue-50 flex items-center justify-center">
            <svg class="w-6 h-6 fill-current text-blue-600" viewBox="0 0 24 24">
              <path d="M12 2L4 5v6c0 5.55 3.84 10.74 8 12 4.16-1.26 8-6.45 8-12V5l-8-3zm-1.5 15l-3.5-3.5 1.41-1.41 2.09 2.08 5.59-5.59 1.41 1.41-7 7z"/>
            </svg>
          </div>
          <span class="px-3 py-1 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">MONTHLY</span>
        </div>
        <p class="mt-5 text-4xl font-bold text-slate-900">94.5%</p>
        <p class="mt-1 text-base text-slate-500">Compliance Score</p>
        <p class="mt-3 text-sm font-semibold text-blue-600">Station performance</p>
      </div>
    </section>

    <section class="grid grid-cols-1 xl:grid-cols-3 gap-6">
      <div class="xl:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Recent Operational Activities</h2>
            <p class="text-sm text-slate-500 mt-1">Latest activities assigned to station personnel</p>
          </div>

          <button class="text-sm font-bold text-[#8B1E23] hover:underline">
            View Activities →
          </button>
        </div>

        <div class="mt-5 space-y-3">
          <div class="p-4 rounded-xl border border-slate-200 hover:bg-slate-50">
            <div class="flex items-start justify-between gap-4">
              <div>
                <p class="font-bold text-slate-900">Fire Safety Inspection</p>
                <p class="text-sm text-slate-500 mt-1">Assigned to FO3 Juan Dela Cruz</p>
                <p class="text-sm text-slate-400 mt-1">September 9, 2026 • 8:00 AM</p>
              </div>
              <span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">ONGOING</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 hover:bg-slate-50">
            <div class="flex items-start justify-between gap-4">
              <div>
                <p class="font-bold text-slate-900">Community Fire Drill</p>
                <p class="text-sm text-slate-500 mt-1">Assigned to SFO1 M. Santos</p>
                <p class="text-sm text-slate-400 mt-1">September 10, 2026 • 1:00 PM</p>
              </div>
              <span class="px-3 py-1.5 rounded-full bg-yellow-50 text-yellow-700 text-xs font-bold">SCHEDULED</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 hover:bg-slate-50">
            <div class="flex items-start justify-between gap-4">
              <div>
                <p class="font-bold text-slate-900">Station Equipment Inspection</p>
                <p class="text-sm text-slate-500 mt-1">Assigned to FO2 R. Reyes</p>
                <p class="text-sm text-slate-400 mt-1">September 11, 2026 • 3:00 PM</p>
              </div>
              <span class="px-3 py-1.5 rounded-full bg-green-50 text-green-700 text-xs font-bold">SCHEDULED</span>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <h2 class="text-xl font-bold text-slate-900">Upcoming Deadlines</h2>
        <p class="text-sm text-slate-500 mt-1">Reports requiring attention</p>

        <div class="mt-5 space-y-4">
          <div class="p-4 rounded-xl bg-red-50 border border-red-200">
            <div class="flex items-start gap-3">
              <span class="text-xl">🚨</span>
              <div>
                <p class="text-sm font-bold text-slate-900">Fire Incident Report</p>
                <p class="text-xs text-[#8B1E23] mt-1">Due today • 8:00 PM</p>
                <span class="inline-block mt-2 px-2.5 py-1 rounded-full bg-red-100 text-[#8B1E23] text-xs font-bold">OVERDUE</span>
              </div>
            </div>
          </div>

          <div class="p-4 rounded-xl bg-yellow-50 border border-yellow-200">
            <div class="flex items-start gap-3">
              <span class="text-xl">⚠️</span>
              <div>
                <p class="text-sm font-bold text-slate-900">Weekly Accomplishment Report</p>
                <p class="text-xs text-yellow-700 mt-1">Due tomorrow • 5:00 PM</p>
                <span class="inline-block mt-2 px-2.5 py-1 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">UPCOMING</span>
              </div>
            </div>
          </div>

          <div class="p-4 rounded-xl bg-blue-50 border border-blue-200">
            <div class="flex items-start gap-3">
              <span class="text-xl">📋</span>
              <div>
                <p class="text-sm font-bold text-slate-900">Monthly Compliance Report</p>
                <p class="text-xs text-blue-700 mt-1">Due in 5 days</p>
                <span class="inline-block mt-2 px-2.5 py-1 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">UPCOMING</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="border-b border-slate-200 pb-5">
        <h2 class="text-xl font-bold text-slate-900">Recent System Activity</h2>
        <p class="text-sm text-slate-500 mt-1">Latest actions performed in FireNotify</p>
      </div>

      <div class="mt-5 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
          <p class="text-sm font-semibold text-slate-900">✓ Report Submitted</p>
          <p class="text-xs text-slate-500 mt-1">FO3 Juan Dela Cruz</p>
          <p class="text-xs text-slate-400 mt-2">10 minutes ago</p>
        </div>

        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
          <p class="text-sm font-semibold text-slate-900">✓ Activity Completed</p>
          <p class="text-xs text-slate-500 mt-1">Station Equipment Check</p>
          <p class="text-xs text-slate-400 mt-2">25 minutes ago</p>
        </div>

        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
          <p class="text-sm font-semibold text-slate-900">⚠ Deadline Reminder</p>
          <p class="text-xs text-slate-500 mt-1">Weekly Report</p>
          <p class="text-xs text-slate-400 mt-2">40 minutes ago</p>
        </div>

        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
          <p class="text-sm font-semibold text-slate-900">+ New Activity</p>
          <p class="text-xs text-slate-500 mt-1">Community Fire Drill</p>
          <p class="text-xs text-slate-400 mt-2">1 hour ago</p>
        </div>
      </div>
    </section>

    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Mission Readiness</h2>
            <p class="text-sm text-slate-500 mt-1">Station preparedness summary</p>
          </div>
          <span class="px-3 py-1.5 rounded-full bg-green-50 text-green-700 text-xs font-bold">READY</span>
        </div>

        <div class="mt-5 space-y-4">
          <div class="flex items-center justify-between p-3 rounded-xl bg-slate-50 border border-slate-200">
            <div>
              <p class="text-sm font-bold text-slate-900">Engine Availability</p>
              <p class="text-xs text-slate-500 mt-1">4 of 5 engines operational</p>
            </div>
            <span class="text-sm font-bold text-green-600">80%</span>
          </div>

          <div class="flex items-center justify-between p-3 rounded-xl bg-slate-50 border border-slate-200">
            <div>
              <p class="text-sm font-bold text-slate-900">Comm. Systems</p>
              <p class="text-xs text-slate-500 mt-1">Radios and dispatch links stable</p>
            </div>
            <span class="text-sm font-bold text-blue-600">Stable</span>
          </div>

          <div class="flex items-center justify-between p-3 rounded-xl bg-slate-50 border border-slate-200">
            <div>
              <p class="text-sm font-bold text-slate-900">Medical Kits</p>
              <p class="text-xs text-slate-500 mt-1">Fully stocked across all units</p>
            </div>
            <span class="text-sm font-bold text-emerald-600">100%</span>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Priority Alerts</h2>
            <p class="text-sm text-slate-500 mt-1">Items requiring immediate attention</p>
          </div>
          <button class="text-sm font-bold text-[#8B1E23] hover:underline">View All</button>
        </div>

        <div class="mt-5 space-y-4">
          <div class="p-4 rounded-xl bg-red-50 border border-red-200">
            <div class="flex justify-between items-start gap-3">
              <div>
                <p class="text-sm font-bold text-slate-900">Unresolved Fire Investigation</p>
                <p class="text-xs text-slate-500 mt-1">Case #FI-2048 • Barangay San Roque</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-red-100 text-[#8B1E23] text-xs font-bold">High</span>
            </div>
          </div>

          <div class="p-4 rounded-xl bg-yellow-50 border border-yellow-200">
            <div class="flex justify-between items-start gap-3">
              <div>
                <p class="text-sm font-bold text-slate-900">Equipment Calibration Due</p>
                <p class="text-xs text-slate-500 mt-1">Portable pump unit • due tomorrow</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">Medium</span>
            </div>
          </div>

          <div class="p-4 rounded-xl bg-blue-50 border border-blue-200">
            <div class="flex justify-between items-start gap-3">
              <div>
                <p class="text-sm font-bold text-slate-900">Training Attendance Update</p>
                <p class="text-xs text-slate-500 mt-1">2 personnel still pending attendance</p>
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
          <h2 class="text-xl font-bold text-slate-900">Operations Timeline</h2>
          <p class="text-sm text-slate-500 mt-1">Key events and updates from today</p>
        </div>
      </div>

      <div class="mt-5 space-y-4">
        <div class="flex gap-4 p-4 rounded-xl border border-slate-200 hover:bg-slate-50">
          <div class="flex flex-col items-center">
            <span class="h-3 w-3 rounded-full bg-[#8B1E23]"></span>
            <span class="w-px h-full bg-slate-200 mt-2"></span>
          </div>
          <div class="flex-1">
            <p class="text-sm font-bold text-slate-900">08:00 AM • Morning Briefing</p>
            <p class="text-sm text-slate-500 mt-1">All station personnel attended the daily operations briefing and reviewed updated response protocols.</p>
          </div>
        </div>

        <div class="flex gap-4 p-4 rounded-xl border border-slate-200 hover:bg-slate-50">
          <div class="flex flex-col items-center">
            <span class="h-3 w-3 rounded-full bg-blue-500"></span>
            <span class="w-px h-full bg-slate-200 mt-2"></span>
          </div>
          <div class="flex-1">
            <p class="text-sm font-bold text-slate-900">10:30 AM • Fire Safety Inspection</p>
            <p class="text-sm text-slate-500 mt-1">Inspection status reported for three commercial establishments in the central district.</p>
          </div>
        </div>

        <div class="flex gap-4 p-4 rounded-xl border border-slate-200 hover:bg-slate-50">
          <div class="flex flex-col items-center">
            <span class="h-3 w-3 rounded-full bg-green-500"></span>
          </div>
          <div class="flex-1">
            <p class="text-sm font-bold text-slate-900">01:00 PM • Community Drill</p>
            <p class="text-sm text-slate-500 mt-1">Final logistics approved for the barangay evacuation drill scheduled this afternoon.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex items-center justify-between border-b border-slate-200 pb-5">
        <div>
          <h2 class="text-xl font-bold text-slate-900">Recent Reports</h2>
          <p class="text-sm text-slate-500 mt-1">Latest submissions and their current status</p>
        </div>

        <button class="text-sm font-bold text-[#8B1E23] hover:underline">
          Open Reports →
        </button>
      </div>

      <div class="mt-5 overflow-x-auto">
        <table class="w-full text-left">
          <thead>
            <tr class="border-b border-slate-200 text-xs font-bold uppercase tracking-wide text-slate-400">
              <th class="pb-3 pr-4">Report</th>
              <th class="pb-3 pr-4">Submitted By</th>
              <th class="pb-3 pr-4">Date</th>
              <th class="pb-3 text-right">Status</th>
            </tr>
          </thead>

          <tbody class="divide-y divide-slate-100">
            <tr class="hover:bg-slate-50">
              <td class="py-4 pr-4 font-semibold text-slate-900">After-Operation Incident Report</td>
              <td class="py-4 pr-4 text-sm text-slate-600">FO3 Juan Dela Cruz</td>
              <td class="py-4 pr-4 text-sm text-slate-600">Sept. 9, 2026</td>
              <td class="py-4 text-right">
                <span class="px-3 py-1.5 rounded-full bg-yellow-50 text-yellow-700 text-xs font-bold">Pending</span>
              </td>
            </tr>

            <tr class="hover:bg-slate-50">
              <td class="py-4 pr-4 font-semibold text-slate-900">Monthly Compliance Summary</td>
              <td class="py-4 pr-4 text-sm text-slate-600">SFO1 Maria Santos</td>
              <td class="py-4 pr-4 text-sm text-slate-600">Sept. 8, 2026</td>
              <td class="py-4 text-right">
                <span class="px-3 py-1.5 rounded-full bg-green-50 text-green-700 text-xs font-bold">Approved</span>
              </td>
            </tr>

            <tr class="hover:bg-slate-50">
              <td class="py-4 pr-4 font-semibold text-slate-900">Barangay Fire Drill Summary</td>
              <td class="py-4 pr-4 text-sm text-slate-600">FO2 R. Reyes</td>
              <td class="py-4 pr-4 text-sm text-slate-600">Sept. 7, 2026</td>
              <td class="py-4 text-right">
                <span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">Reviewed</span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  </div>
</template>
