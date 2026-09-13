<template>
  <div class="w-full min-w-0 space-y-6">
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">
        <div><p class="text-sm font-semibold text-[#8B1E23]">FIRENOTIFY PERSONNEL PORTAL</p><h2 class="text-2xl font-bold text-slate-900 mt-1">Settings</h2><p class="text-sm text-slate-500 mt-1">Manage your account, notifications, security, and portal preferences.</p></div>
        <div class="h-14 w-14 rounded-2xl bg-[#8B1E23]/10 flex items-center justify-center"><span v-html="ICONS.settings" class="h-8 w-8 text-[#8B1E23]"></span></div>
      </div>
    </section>

    <section class="grid grid-cols-1 xl:grid-cols-3 gap-6">
      <div class="xl:col-span-2 space-y-6">
        <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><div class="border-b border-slate-200 pb-4"><h3 class="text-lg font-bold text-slate-900">Profile Information</h3><p class="text-sm text-slate-500 mt-1">Update the information shown on your personnel account.</p></div><div class="mt-5 grid grid-cols-1 sm:grid-cols-2 gap-4"><div><label class="text-sm font-semibold text-slate-700">First Name</label><input type="text" :value="currentUser?.firstName || 'Juan'" class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm" /></div><div><label class="text-sm font-semibold text-slate-700">Last Name</label><input type="text" :value="currentUser?.lastName || 'Dela Cruz'" class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm" /></div><div><label class="text-sm font-semibold text-slate-700">Rank</label><input type="text" :value="currentUser?.rank || 'FO3'" class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm" /></div><div><label class="text-sm font-semibold text-slate-700">Position</label><input type="text" value="Station Inspector" class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm" /></div><div class="sm:col-span-2"><label class="text-sm font-semibold text-slate-700">Station</label><input type="text" value="BFP Balingasag" class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm" /></div></div><button class="mt-5 px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]">Save Profile</button></section>

        <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><div class="border-b border-slate-200 pb-4"><h3 class="text-lg font-bold text-slate-900">Notification Preferences</h3><p class="text-sm text-slate-500 mt-1">Choose which alerts you receive in the portal.</p></div><div class="mt-5 space-y-5"><div class="flex items-center justify-between"><div><p class="text-sm font-semibold text-slate-800">Task reminders</p><p class="text-xs text-slate-500 mt-1">Receive alerts for assigned tasks and deadlines.</p></div><input type="checkbox" checked class="h-5 w-5 accent-[#8B1E23]" /></div><div class="flex items-center justify-between"><div><p class="text-sm font-semibold text-slate-800">Report notifications</p><p class="text-xs text-slate-500 mt-1">Be notified when reports are submitted or returned.</p></div><input type="checkbox" checked class="h-5 w-5 accent-[#8B1E23]" /></div><div class="flex items-center justify-between"><div><p class="text-sm font-semibold text-slate-800">Activity reminders</p><p class="text-xs text-slate-500 mt-1">Receive reminders for scheduled station activities.</p></div><input type="checkbox" checked class="h-5 w-5 accent-[#8B1E23]" /></div><div class="flex items-center justify-between"><div><p class="text-sm font-semibold text-slate-800">Email notifications</p><p class="text-xs text-slate-500 mt-1">Send important updates to your registered email.</p></div><input type="checkbox" class="h-5 w-5 accent-[#8B1E23]" /></div></div></section>

        <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><div class="border-b border-slate-200 pb-4"><h3 class="text-lg font-bold text-slate-900">Security</h3><p class="text-sm text-slate-500 mt-1">Keep your personnel account protected.</p></div><div class="mt-5 space-y-4"><div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 p-4 rounded-xl bg-slate-50 border border-slate-200"><div><p class="text-sm font-semibold text-slate-800">Password</p><p class="text-xs text-slate-500 mt-1">Last changed 30 days ago</p></div><button class="px-4 py-2 rounded-xl border border-slate-300 bg-white text-sm font-semibold text-slate-700 hover:bg-slate-100">Change Password</button></div><div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 p-4 rounded-xl bg-green-50 border border-green-100"><div><p class="text-sm font-semibold text-slate-800">Two-factor authentication</p><p class="text-xs text-green-700 mt-1">Your account is protected with 2FA.</p></div><span class="px-3 py-1.5 rounded-full bg-green-100 text-green-700 text-xs font-bold">Enabled</span></div></div></section>
      </div>

      <div class="space-y-6">
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Portal Preferences</h3><div class="mt-5 space-y-4"><div><label class="text-sm font-semibold text-slate-700">Language</label><select class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm"><option>English</option><option>Filipino</option></select></div><div><label class="text-sm font-semibold text-slate-700">Time Zone</label><select class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm"><option>Asia/Manila (UTC+8)</option><option>UTC</option></select></div><div><label class="text-sm font-semibold text-slate-700">Default Landing Page</label><select class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm"><option>Dashboard</option><option>Tasks</option><option>Activities</option></select></div></div></div>
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Display</h3><p class="text-sm text-slate-500 mt-1">Adjust how the portal looks on your device.</p><div class="mt-5 space-y-4"><div class="flex items-center justify-between"><div><p class="text-sm font-semibold text-slate-800">Compact sidebar</p><p class="text-xs text-slate-500 mt-1">Use a smaller navigation layout.</p></div><input type="checkbox" class="h-5 w-5 accent-[#8B1E23]" /></div><div class="flex items-center justify-between"><div><p class="text-sm font-semibold text-slate-800">Reduced motion</p><p class="text-xs text-slate-500 mt-1">Minimize interface transitions.</p></div><input type="checkbox" class="h-5 w-5 accent-[#8B1E23]" /></div></div></div>
      </div>
    </section>

    <section class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><div><h3 class="text-lg font-bold text-slate-900">Save your changes</h3><p class="text-sm text-slate-500 mt-1">Profile and preference updates apply to this account.</p></div><div class="flex gap-3"><button class="px-5 py-3 rounded-xl border border-slate-300 bg-white text-sm font-semibold text-slate-700 hover:bg-slate-100">Reset</button><button class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]">Save Changes</button></div></section>
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
