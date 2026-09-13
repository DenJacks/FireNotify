<template>
  <div class="w-full min-w-0 space-y-6">
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
        <div>
          <p class="text-sm font-semibold text-[#8B1E23]">PERSONNEL MANAGEMENT</p>
          <h2 class="text-2xl font-bold text-slate-900 mt-1">Personnel Roster</h2>
          <p class="text-sm text-slate-500 mt-1">View personnel currently assigned to your station</p>
        </div>

        <div class="flex items-center gap-3">
          <div class="h-12 w-12 rounded-xl bg-[#8B1E23] flex items-center justify-center text-white">
            <span v-html="ICONS.users || ICONS.check"></span>
          </div>

          <div>
            <p class="text-xs text-slate-400">Station Personnel</p>
            <p class="text-lg font-bold text-slate-900">{{ roster.length }} Personnel</p>
          </div>
        </div>
      </div>
    </section>

    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-slate-500">Total Personnel</p>
            <p class="text-2xl font-bold text-slate-900 mt-1">{{ roster.length }}</p>
          </div>
          <div class="h-11 w-11 rounded-xl bg-slate-100 flex items-center justify-center">
            <span v-html="ICONS.users || ICONS.check"></span>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-slate-500">Active</p>
            <p class="text-2xl font-bold text-green-600 mt-1">09</p>
          </div>
          <div class="h-11 w-11 rounded-xl bg-green-100 flex items-center justify-center">
            <span class="text-green-600 font-bold">✓</span>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-slate-500">On Duty</p>
            <p class="text-2xl font-bold text-[#8B1E23] mt-1">06</p>
          </div>
          <div class="h-11 w-11 rounded-xl bg-red-50 flex items-center justify-center">
            <span class="text-[#8B1E23] font-bold">●</span>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-slate-500">Off Duty</p>
            <p class="text-2xl font-bold text-amber-600 mt-1">03</p>
          </div>
          <div class="h-11 w-11 rounded-xl bg-amber-100 flex items-center justify-center">
            <span class="text-amber-600 font-bold">◷</span>
          </div>
        </div>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">
      <div class="flex flex-col lg:flex-row gap-4">
        <div class="flex-1">
          <label class="block text-sm font-semibold text-slate-700 mb-2">Search Personnel</label>
          <input type="text" placeholder="Search by name, rank, or role..." class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-[#8B1E23] focus:border-[#8B1E23]" />
        </div>

        <div class="w-full lg:w-52">
          <label class="block text-sm font-semibold text-slate-700 mb-2">Duty Status</label>
          <select class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-[#8B1E23]">
            <option>All Status</option>
            <option>On Duty</option>
            <option>Off Duty</option>
            <option>Leave</option>
          </select>
        </div>

        <div class="w-full lg:w-52">
          <label class="block text-sm font-semibold text-slate-700 mb-2">Rank</label>
          <select class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-[#8B1E23]">
            <option>All Ranks</option>
            <option>Officer</option>
            <option>Fire Officer</option>
            <option>Senior Fire Officer</option>
          </select>
        </div>
      </div>
    </section>

    <section class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="lg:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-4">
          <div>
            <h3 class="text-lg font-bold text-slate-900">Station Personnel</h3>
            <p class="text-sm text-slate-500 mt-1">Current personnel assigned to this station</p>
          </div>
          <span class="px-3 py-1.5 rounded-full bg-slate-100 text-slate-700 text-xs font-bold">{{ roster.length }} Members</span>
        </div>

        <div class="mt-5 grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="person in roster" :key="person.name" class="p-5 bg-slate-50 border border-slate-200 rounded-xl hover:border-[#8B1E23] hover:shadow-sm transition">
            <div class="flex items-start gap-4">
              <div class="h-14 w-14 rounded-full bg-[#8B1E23] flex items-center justify-center text-white font-bold text-xs shrink-0">
                {{ person.rank }}
              </div>

              <div class="flex-1 min-w-0">
                <p class="text-base font-bold text-slate-900 truncate">{{ person.name }}</p>
                <p class="text-sm text-[#8B1E23] font-semibold mt-1">{{ person.role }}</p>
                <p class="text-sm text-slate-500 mt-1">{{ person.shift }}</p>
              </div>

              <span class="px-3 py-1.5 rounded-full bg-green-100 text-green-700 text-xs font-bold">Active</span>
            </div>

            <div class="mt-4 pt-4 border-t border-slate-200 grid grid-cols-2 gap-3">
              <div>
                <p class="text-xs text-slate-400">Assignment</p>
                <p class="text-sm font-semibold text-slate-700 mt-1">Station Duty</p>
              </div>
              <div>
                <p class="text-xs text-slate-400">Availability</p>
                <p class="text-sm font-semibold text-green-600 mt-1">Available</p>
              </div>
            </div>

            <button class="w-full mt-4 px-4 py-2.5 rounded-lg border border-slate-300 bg-white text-sm font-semibold text-slate-700 hover:bg-[#8B1E23] hover:text-white hover:border-[#8B1E23] transition">View Personnel Details</button>
          </div>
        </div>
      </div>

      <div class="space-y-6">
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
          <h3 class="text-lg font-bold text-slate-900">Duty Overview</h3>
          <p class="text-sm text-slate-500 mt-1">Personnel availability today</p>

          <div class="mt-5 space-y-4">
            <div>
              <div class="flex justify-between text-sm mb-2">
                <span class="font-medium text-slate-600">On Duty</span>
                <span class="font-bold text-slate-900">06 / 09</span>
              </div>
              <div class="h-2 bg-slate-100 rounded-full overflow-hidden">
                <div class="h-full bg-[#8B1E23] rounded-full" style="width: 67%"></div>
              </div>
            </div>

            <div>
              <div class="flex justify-between text-sm mb-2">
                <span class="font-medium text-slate-600">Off Duty</span>
                <span class="font-bold text-slate-900">03 / 09</span>
              </div>
              <div class="h-2 bg-slate-100 rounded-full overflow-hidden">
                <div class="h-full bg-amber-400 rounded-full" style="width: 33%"></div>
              </div>
            </div>
          </div>
        </div>

        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
          <h3 class="text-lg font-bold text-slate-900">Shift Information</h3>
          <div class="mt-5 space-y-4">
            <div class="flex justify-between items-center">
              <span class="text-sm text-slate-500">Current Shift</span>
              <span class="text-sm font-bold text-slate-900">Day Shift</span>
            </div>
            <div class="flex justify-between items-center">
              <span class="text-sm text-slate-500">Time</span>
              <span class="text-sm font-bold text-slate-900">08:00 AM – 05:00 PM</span>
            </div>
            <div class="flex justify-between items-center">
              <span class="text-sm text-slate-500">Duty Officer</span>
              <span class="text-sm font-bold text-[#8B1E23]">Station Inspector</span>
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
  roster: {
    type: Array,
    required: false,
    default: () => []
  }
})
</script>
