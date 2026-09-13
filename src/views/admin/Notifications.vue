<script setup>
const notifications = [
  {
    icon: '🚨',
    title: 'Overdue Report Deadline',
    detail: 'The After-Operation Fire Incident Report has passed its submission deadline.',
    time: '10 minutes ago',
    tone: 'red',
    badge: 'UNREAD'
  },
  {
    icon: '⚠️',
    title: 'Upcoming Report Deadline',
    detail: 'Weekly Accomplishment Report is due tomorrow at 5:00 PM.',
    time: '30 minutes ago',
    tone: 'yellow',
    badge: 'UNREAD'
  },
  {
    icon: '📋',
    title: 'New Activity Assigned',
    detail: 'Community Fire Drill has been scheduled for September 10, 2026.',
    time: '1 hour ago',
    tone: 'blue',
    badge: 'UNREAD'
  },
  {
    icon: '✓',
    title: 'Report Approved',
    detail: 'Weekly Accomplishment Report submitted by SFO1 Maria Santos has been approved.',
    time: '2 hours ago',
    tone: 'slate',
    badge: 'READ'
  }
]

const channelSummary = [
  { label: 'System Alerts', count: '12 messages today', value: '42%', color: 'text-[#8B1E23]' },
  { label: 'Personnel Updates', count: '9 messages today', value: '31%', color: 'text-blue-600' },
  { label: 'Reports & Compliance', count: '8 messages today', value: '27%', color: 'text-green-600' }
]
</script>

<template>
  <div class="space-y-6">
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
        <div>
          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">Communication Center</p>
          <h2 class="text-2xl font-bold text-slate-900 mt-1">Notifications</h2>
          <p class="text-base text-slate-500 mt-1">View system announcements, activity alerts, and deadline reminders.</p>
        </div>

        <button class="px-5 py-3 rounded-xl border border-slate-300 bg-white text-slate-700 font-bold hover:bg-slate-100">
          Mark All as Read
        </button>
      </div>
    </section>

    <section class="grid grid-cols-1 sm:grid-cols-3 gap-5">
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">05</p>
        <p class="text-sm text-slate-500 mt-1">Unread</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">03</p>
        <p class="text-sm text-slate-500 mt-1">Deadline Alerts</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-blue-600">08</p>
        <p class="text-sm text-slate-500 mt-1">Activity Updates</p>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="space-y-3">
        <div v-for="item in notifications" :key="item.title" :class="[
          'p-5 rounded-xl border',
          item.tone === 'red' ? 'border-red-200 bg-red-50' : '',
          item.tone === 'yellow' ? 'border-yellow-200 bg-yellow-50' : '',
          item.tone === 'blue' ? 'border-blue-200 bg-blue-50' : '',
          item.tone === 'slate' ? 'border-slate-200 bg-slate-50' : ''
        ]">
          <div class="flex items-start gap-4">
            <div :class="[
              'h-12 w-12 rounded-full flex items-center justify-center shrink-0',
              item.tone === 'red' ? 'bg-red-100' : '',
              item.tone === 'yellow' ? 'bg-yellow-100' : '',
              item.tone === 'blue' ? 'bg-blue-100' : '',
              item.tone === 'slate' ? 'bg-green-100' : ''
            ]">
              {{ item.icon }}
            </div>

            <div class="flex-1">
              <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-2">
                <h3 class="font-bold text-slate-900">{{ item.title }}</h3>
                <span :class="[
                  'px-3 py-1 rounded-full text-xs font-bold',
                  item.badge === 'UNREAD' && item.tone === 'red' ? 'bg-red-100 text-[#8B1E23]' : '',
                  item.badge === 'UNREAD' && item.tone === 'yellow' ? 'bg-yellow-100 text-yellow-700' : '',
                  item.badge === 'UNREAD' && item.tone === 'blue' ? 'bg-blue-100 text-blue-700' : '',
                  item.badge === 'READ' ? 'bg-green-100 text-green-700' : ''
                ]">{{ item.badge }}</span>
              </div>

              <p class="text-sm text-slate-600 mt-2">{{ item.detail }}</p>
              <p class="text-xs text-slate-400 mt-2">{{ item.time }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Channel Summary</h2>
            <p class="text-sm text-slate-500 mt-1">Message volume by source</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <div v-for="item in channelSummary" :key="item.label" class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">{{ item.label }}</p>
                <p class="text-xs text-slate-500 mt-1">{{ item.count }}</p>
              </div>
              <span :class="['text-sm font-bold', item.color]">{{ item.value }}</span>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Message Filters</h2>
            <p class="text-sm text-slate-500 mt-1">Quick sorting for incoming updates</p>
          </div>
        </div>

        <div class="mt-5 space-y-4">
          <button class="w-full text-left px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 hover:bg-slate-100 text-sm font-semibold text-slate-700">All Notifications</button>
          <button class="w-full text-left px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 hover:bg-slate-100 text-sm font-semibold text-slate-700">Deadline Alerts</button>
          <button class="w-full text-left px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 hover:bg-slate-100 text-sm font-semibold text-slate-700">Personnel Updates</button>
          <button class="w-full text-left px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 hover:bg-slate-100 text-sm font-semibold text-slate-700">System Announcements</button>
        </div>
      </div>
    </section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex items-center justify-between border-b border-slate-200 pb-5">
        <div>
          <h2 class="text-xl font-bold text-slate-900">Announcements</h2>
          <p class="text-sm text-slate-500 mt-1">Administrative updates for all BFP units</p>
        </div>
      </div>

      <div class="mt-5 space-y-4">
        <div class="p-4 rounded-xl border border-emerald-200 bg-emerald-50">
          <p class="text-sm font-bold text-slate-900">Operations Update</p>
          <p class="text-sm text-slate-600 mt-1">All station units are reminded to check radio signal stability before the next dispatch cycle.</p>
        </div>

        <div class="p-4 rounded-xl border border-indigo-200 bg-indigo-50">
          <p class="text-sm font-bold text-slate-900">Training Notice</p>
          <p class="text-sm text-slate-600 mt-1">Community fire drill briefing will be held tomorrow at 7:30 AM at the barangay hall.</p>
        </div>

        <div class="p-4 rounded-xl border border-amber-200 bg-amber-50">
          <p class="text-sm font-bold text-slate-900">Compliance Advisory</p>
          <p class="text-sm text-slate-600 mt-1">All approved reports must be archived within 24 hours to maintain digital records compliance.</p>
        </div>
      </div>
    </section>
  </div>
</template>
