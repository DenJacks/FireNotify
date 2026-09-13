<template>
  <div class="flex h-screen w-full bg-slate-100 text-slate-800 font-sans overflow-hidden">

    <!-- ========================================================= -->
    <!-- SIDEBAR -->
    <!-- ========================================================= -->
    <aside
      class="w-72 flex-shrink-0 bg-white border-r border-slate-200 flex flex-col justify-between shadow-sm z-20"
    >

      <!-- TOP SIDEBAR -->
      <div class="overflow-y-auto">

        <!-- BFP COLOR ACCENT -->
        <div class="h-2 bg-[#8B1E23]"></div>

        <!-- LOGO -->
        <div class="flex items-center gap-4 px-6 py-6 border-b border-slate-200">

          <div
            class="h-14 w-14 rounded-xl bg-[#8B1E23] flex items-center justify-center shadow-sm"
          >
            <svg
              viewBox="0 0 64 64"
              class="h-9 w-9"
              fill="none"
            >
              <path
                d="M32 4 L58 13 V29 C58 45 47 55 32 60 C17 55 6 45 6 29 V13 Z"
                stroke="#F4C542"
                stroke-width="3"
                fill="#8B1E23"
              />

              <path
                d="M32 20c-4.5 4.5-7 8.2-7 12.2 0 4.4 3.3 7.8 7.4 7.8 4.5 0 7.9-3.2 7.9-7.5 0-2.2-.9-3.9-2.3-5.6.1 1.7-.5 2.9-1.6 3.7.3-2.9-.7-6.4-4.4-10.6Z"
                fill="#F4C542"
              />
            </svg>
          </div>

          <div>
            <p class="text-sm font-semibold text-slate-500">
              Personnel Portal
            </p>

            <h1 class="text-xl font-extrabold tracking-wide text-slate-900">
              FIRE<span class="text-[#8B1E23]">NOTIFY</span>
            </h1>
          </div>

        </div>


        <!-- ===================================================== -->
        <!-- NAVIGATION -->
        <!-- ===================================================== -->
        <div class="px-4 py-6 space-y-7">

          <!-- FIELD DUTY -->
          <div>
            <p
              class="px-3 mb-3 text-xs font-bold uppercase tracking-wider text-slate-400"
            >
              Field Duty
            </p>

            <nav class="space-y-2">

              <button
                v-for="item in fieldItems"
                :key="item.name"
                @click="activeTab = item.name"
                :title="item.context"
                :class="[
                  'w-full flex items-center gap-4 px-4 py-3.5 rounded-xl text-left transition-all duration-150',
                  activeTab === item.name
                    ? 'bg-[#8B1E23] text-white shadow-md'
                    : 'text-slate-700 hover:bg-slate-100'
                ]"
              >

                <span
                  v-html="ICONS[item.icon]"
                  :class="[
                    'h-6 w-6 shrink-0',
                    activeTab === item.name
                      ? 'text-[#F4C542]'
                      : 'text-slate-500'
                  ]"
                ></span>

                <div class="min-w-0 flex-1">

                  <span class="block text-base font-semibold truncate">
                    {{ item.name }}
                  </span>

                  <span
                    :class="[
                      'block text-xs mt-0.5 truncate',
                      activeTab === item.name
                        ? 'text-white/75'
                        : 'text-slate-400'
                    ]"
                  >
                    {{ item.context }}
                  </span>

                </div>

                <span
                  v-if="item.badge"
                  class="rounded-full bg-red-100 text-red-700 px-2.5 py-1 text-xs font-bold"
                >
                  {{ item.badge }}
                </span>

              </button>

            </nav>
          </div>


          <!-- MANAGEMENT -->
          <div>
            <p
              class="px-3 mb-3 text-xs font-bold uppercase tracking-wider text-slate-400"
            >
              Management & Records
            </p>

            <nav class="space-y-2">

              <button
                v-for="item in managementItems"
                :key="item.name"
                @click="activeTab = item.name"
                :title="item.context"
                :class="[
                  'w-full flex items-center gap-4 px-4 py-3.5 rounded-xl text-left transition-all duration-150',
                  activeTab === item.name
                    ? 'bg-[#8B1E23] text-white shadow-md'
                    : 'text-slate-700 hover:bg-slate-100'
                ]"
              >

                <span
                  v-html="ICONS[item.icon]"
                  :class="[
                    'h-6 w-6 shrink-0',
                    activeTab === item.name
                      ? 'text-[#F4C542]'
                      : 'text-slate-500'
                  ]"
                ></span>

                <div class="min-w-0">

                  <span class="block text-base font-semibold truncate">
                    {{ item.name }}
                  </span>

                  <span
                    :class="[
                      'block text-xs mt-0.5 truncate',
                      activeTab === item.name
                        ? 'text-white/75'
                        : 'text-slate-400'
                    ]"
                  >
                    {{ item.context }}
                  </span>

                </div>

              </button>

            </nav>
          </div>


          <!-- PERSONNEL TOOLS -->
          <div>
            <p
              class="px-3 mb-3 text-xs font-bold uppercase tracking-wider text-slate-400"
            >
              Personnel Tools
            </p>

            <nav class="space-y-2">

              <button
                v-for="item in toolItems"
                :key="item.name"
                @click="activeTab = item.name"
                :title="item.context"
                :class="[
                  'w-full flex items-center gap-4 px-4 py-3.5 rounded-xl text-left transition-all duration-150',
                  activeTab === item.name
                    ? 'bg-[#8B1E23] text-white shadow-md'
                    : 'text-slate-700 hover:bg-slate-100'
                ]"
              >

                <span
                  v-html="ICONS[item.icon]"
                  :class="[
                    'h-6 w-6 shrink-0',
                    activeTab === item.name
                      ? 'text-[#F4C542]'
                      : 'text-slate-500'
                  ]"
                ></span>

                <div class="min-w-0">

                  <span class="block text-base font-semibold truncate">
                    {{ item.name }}
                  </span>

                  <span
                    :class="[
                      'block text-xs mt-0.5 truncate',
                      activeTab === item.name
                        ? 'text-white/75'
                        : 'text-slate-400'
                    ]"
                  >
                    {{ item.context }}
                  </span>

                </div>

              </button>

            </nav>
          </div>

        </div>
      </div>


      <!-- ===================================================== -->
      <!-- USER PROFILE -->
      <!-- ===================================================== -->
      <div class="p-4 border-t border-slate-200 bg-slate-50">

        <div
          class="flex items-center gap-3 p-3 bg-white border border-slate-200 rounded-xl"
        >

          <div
            class="h-12 w-12 rounded-full bg-[#8B1E23] flex items-center justify-center text-white font-bold text-sm"
          >
            {{ currentUser?.rank || 'FO3' }}
          </div>

          <div class="overflow-hidden">

            <p class="text-sm font-bold text-slate-900 truncate">
              {{ currentUser?.firstName || 'Juan' }}
              {{ currentUser?.lastName || 'Dela Cruz' }}
            </p>

            <p class="text-xs text-slate-500 truncate">
              Station Inspector
            </p>

          </div>

        </div>


        <!-- SIGN OUT -->
        <button
          @click="showLogoutConfirm = true"
          class="w-full mt-3 flex items-center gap-3 px-4 py-3 rounded-xl text-base font-semibold text-slate-600 hover:bg-red-50 hover:text-[#8B1E23] transition"
        >

          <span
            v-html="ICONS.logout"
            class="h-5 w-5"
          ></span>

          <span>Sign Out</span>

        </button>

      </div>

    </aside>


    <!-- ========================================================= -->
    <!-- MAIN CONTENT -->
    <!-- ========================================================= -->
    <div class="flex-1 flex flex-col overflow-y-auto">

      <!-- ======================================================= -->
      <!-- HEADER -->
      <!-- ======================================================= -->
      <header
        class="bg-white border-b border-slate-200 px-8 py-5 flex items-center justify-between sticky top-0 z-30 shadow-sm"
      >

        <div>

          <p class="text-sm font-medium text-slate-500">
            Personnel Portal
          </p>

          <h1 class="text-2xl font-bold text-slate-900">
            {{ activeTab }}
          </h1>

        </div>


        <div class="flex items-center gap-4">

          <!-- DUTY STATUS -->
          <div
            class="hidden sm:flex items-center gap-2 px-4 py-2 rounded-full bg-green-50 border border-green-200"
          >

            <span class="h-3 w-3 rounded-full bg-green-500"></span>

            <span class="text-sm font-semibold text-green-700">
              On Duty · Station 1
            </span>

          </div>


          <!-- NOTIFICATIONS -->
          <button
            @click="activeTab = 'Notifications'"
            class="relative h-12 w-12 flex items-center justify-center rounded-xl border border-slate-200 bg-white hover:bg-slate-100 transition"
            title="Notifications"
          >

            <span
              v-html="ICONS.bell"
              class="h-6 w-6 text-slate-600"
            ></span>

            <span
              class="absolute top-2 right-2 h-3 w-3 rounded-full bg-[#8B1E23] border-2 border-white"
            ></span>

          </button>

        </div>

      </header>


      <!-- ======================================================= -->
      <!-- PAGE -->
      <!-- ======================================================= -->
      <main class="flex-1 min-w-0 min-h-0 overflow-y-auto p-6 lg:p-8">
<div 
  v-if="activeTab === 'Dashboard'" 
  class="flex-1 min-w-0 min-h-0 overflow-y-auto p-6 space-y-7"
>

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
                    <button @click="activeTab = 'Tasks'" class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]">View Task</button>
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
                <div class="mt-5 grid grid-cols-2 gap-3"><button @click="activeTab = 'Tasks'" class="p-4 rounded-xl border border-slate-200 hover:bg-slate-50 text-left"><p class="text-sm font-bold text-slate-900">View Tasks</p><p class="text-xs text-slate-500 mt-1">Check assignments</p></button><button @click="activeTab = 'Reports'" class="p-4 rounded-xl border border-slate-200 hover:bg-slate-50 text-left"><p class="text-sm font-bold text-slate-900">Submit Report</p><p class="text-xs text-slate-500 mt-1">Upload report</p></button><button @click="activeTab = 'Activities'" class="p-4 rounded-xl border border-slate-200 hover:bg-slate-50 text-left"><p class="text-sm font-bold text-slate-900">Activities</p><p class="text-xs text-slate-500 mt-1">View schedule</p></button><button @click="activeTab = 'Notifications'" class="p-4 rounded-xl border border-slate-200 hover:bg-slate-50 text-left"><p class="text-sm font-bold text-slate-900">Notifications</p><p class="text-xs text-slate-500 mt-1">View alerts</p></button></div>
              </div>
            </div>
          </section>
        </div>


        <!-- ===================================================== -->
        <!-- WELCOME -->
        <!-- ===================================================== -->
       
         


    


          


        <!-- ===================================================== -->
<!-- MAIN GRID -->
<!-- ===================================================== -->
<section v-if="activeTab !== 'Dashboard'" class="grid grid-cols-1 lg:grid-cols-3 gap-6 h-full min-h-0">

  <!-- =================================================== -->
  <!-- LEFT CONTENT -->
  <!-- =================================================== -->
  <div
    :class="[
      activeTab === 'Tasks' || activeTab === 'Reports' || activeTab === 'Notifications' || activeTab === 'Personnel Roster' || activeTab === 'Station Duty Log' || activeTab === 'Equipment Audit' || activeTab === 'Support' || activeTab === 'Settings'
        ? 'lg:col-span-3 w-full min-w-0'
        : 'lg:col-span-2',
      'space-y-6'
    ]"
  >

    <!-- ================================================= -->
    <!-- DASHBOARD -->
    <!-- ================================================= -->
    <div 
  v-if="activeTab === 'Dashboard'" 
  class="w-full min-w-0 space-y-7"
>

      <div class="border-b border-slate-200 pb-5">
        <h2 class="text-xl font-bold text-slate-900">
          Personnel Dashboard
        </h2>

        <p class="text-sm text-slate-500 mt-1">
          Overview of your current duties, reports, and station activities
        </p>
      </div>

      <div class="mt-5 grid grid-cols-1 md:grid-cols-2 gap-4">

        <div class="p-5 rounded-xl bg-blue-50 border border-blue-100">
          <p class="text-sm font-semibold text-blue-700">
            Today's Assignment
          </p>

          <p class="mt-2 text-lg font-bold text-slate-900">
            Fire Safety Inspection
          </p>

          <p class="text-sm text-slate-500 mt-1">
            Public Market Complex · 09:00 AM
          </p>
        </div>

        <div class="p-5 rounded-xl bg-green-50 border border-green-100">
          <p class="text-sm font-semibold text-green-700">
            Completed Tasks
          </p>

          <p class="mt-2 text-3xl font-bold text-slate-900">
            06
          </p>

          <p class="text-sm text-slate-500 mt-1">
            Tasks completed this week
          </p>
        </div>

        <div class="p-5 rounded-xl bg-yellow-50 border border-yellow-100">
          <p class="text-sm font-semibold text-yellow-700">
            Reports To Submit
          </p>

          <p class="mt-2 text-3xl font-bold text-slate-900">
            03
          </p>

          <p class="text-sm text-slate-500 mt-1">
            Reports awaiting submission
          </p>
        </div>

        <div class="p-5 rounded-xl bg-red-50 border border-red-100">
          <p class="text-sm font-semibold text-[#8B1E23]">
            Urgent Attention
          </p>

          <p class="mt-2 text-3xl font-bold text-slate-900">
            02
          </p>

          <p class="text-sm text-slate-500 mt-1">
            Tasks require immediate action
          </p>
        </div>

      </div>

    </div>


   <!-- ================================================= -->
<!-- TASKS -->
<!-- ================================================= -->
<div 
  v-else-if="activeTab === 'Tasks'" 
  class="w-full min-w-0 space-y-6"
>

  <!-- TASK HEADER -->
  <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

    <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">

      <div>
        <p class="text-sm font-bold text-[#8B1E23]">
          FIRENOTIFY PERSONNEL PORTAL
        </p>

        <h2 class="text-2xl font-bold text-slate-900 mt-1">
          Assigned Tasks
        </h2>

        <p class="text-sm text-slate-500 mt-1">
          Monitor and manage your assigned duties and activities.
        </p>
      </div>

      <button
        class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]"
      >
        + View All Tasks
      </button>

    </div>

  </section>


  <!-- ================================================= -->
  <!-- TASK SUMMARY -->
  <!-- ================================================= -->
  <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">

    <!-- TOTAL -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-sm text-slate-500">Total Tasks</p>
          <p class="text-3xl font-bold text-slate-900 mt-1">09</p>
        </div>

        <div class="h-12 w-12 rounded-xl bg-blue-50 flex items-center justify-center">
          <span
            v-html="ICONS.tasks"
            class="h-6 w-6 text-blue-600"
          ></span>
        </div>
      </div>
    </div>


    <!-- PENDING -->
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


    <!-- COMPLETED -->
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


    <!-- OVERDUE -->
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


  <!-- ================================================= -->
  <!-- TASK FILTER -->
  <!-- ================================================= -->
  <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

    <div class="flex flex-col lg:flex-row gap-4 lg:items-center lg:justify-between">

      <div>
        <h3 class="font-bold text-slate-900">
          Task List
        </h3>

        <p class="text-sm text-slate-500">
          Review your current assignments.
        </p>
      </div>

      <div class="flex flex-col sm:flex-row gap-3">

        <select
          class="px-4 py-3 rounded-xl border border-slate-300 text-sm font-medium bg-white"
        >
          <option>All Tasks</option>
          <option>Pending</option>
          <option>Completed</option>
          <option>Overdue</option>
        </select>

        <select
          class="px-4 py-3 rounded-xl border border-slate-300 text-sm font-medium bg-white"
        >
          <option>All Priorities</option>
          <option>High Priority</option>
          <option>Medium Priority</option>
          <option>Low Priority</option>
        </select>

      </div>

    </div>

  </section>


  <!-- ================================================= -->
  <!-- ASSIGNED TASKS -->
  <!-- ================================================= -->
  <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

    <div class="flex items-center justify-between border-b border-slate-200 pb-5">

      <div>
        <h3 class="text-xl font-bold text-slate-900">
          Current Assignments
        </h3>

        <p class="text-sm text-slate-500 mt-1">
          Tasks assigned to your personnel account.
        </p>
      </div>

      <span class="px-4 py-2 rounded-full bg-blue-50 text-blue-700 text-sm font-bold">
        09 Total
      </span>

    </div>


    <div class="mt-5 space-y-4">

      <div
        v-for="task in taskList"
        :key="task.title"
        class="p-5 rounded-xl border border-slate-200 bg-slate-50 hover:border-[#8B1E23] transition"
      >

        <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">

          <!-- TASK INFORMATION -->
          <div class="flex items-start gap-4">

            <div
              class="h-12 w-12 rounded-xl bg-blue-100 flex items-center justify-center shrink-0"
            >
              <span
                v-html="ICONS.tasks"
                class="h-6 w-6 text-blue-600"
              ></span>
            </div>

            <div>

              <div class="flex flex-wrap items-center gap-2">

                <p class="text-base font-bold text-slate-900">
                  {{ task.title }}
                </p>

                <span class="px-2.5 py-1 rounded-full bg-amber-100 text-amber-700 text-xs font-bold">
                  Pending
                </span>

              </div>

              <p class="text-sm text-slate-500 mt-1">
                Due: {{ task.due }}
              </p>

              <p class="text-sm text-slate-500 mt-1">
                Assigned to BFP Balingasag Station
              </p>

            </div>

          </div>


          <!-- TASK ACTION -->
          <div class="flex flex-col sm:flex-row gap-3">

            <button
              class="px-4 py-3 rounded-xl border border-slate-300 bg-white text-slate-700 text-sm font-bold hover:bg-slate-100"
            >
              View Details
            </button>

            <button
              class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]"
            >
              Update Status
            </button>

          </div>

        </div>


        <!-- PROGRESS -->
        <div class="mt-5">

          <div class="flex justify-between mb-2">

            <span class="text-xs font-semibold text-slate-500">
              Task Progress
            </span>

            <span class="text-xs font-bold text-slate-700">
              60%
            </span>

          </div>

          <div class="w-full h-2.5 bg-slate-200 rounded-full overflow-hidden">

            <div
              class="h-full bg-[#8B1E23] rounded-full"
              style="width: 60%"
            ></div>

          </div>

        </div>

      </div>

    </div>

  </section>


  <!-- ================================================= -->
  <!-- TASK DETAILS + PRIORITY -->
  <!-- ================================================= -->
  <section class="grid grid-cols-1 lg:grid-cols-2 gap-6">

    <!-- TODAY -->
    <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <h3 class="text-lg font-bold text-slate-900">
        Today's Priority
      </h3>

      <p class="text-sm text-slate-500 mt-1">
        Tasks that require immediate attention.
      </p>

      <div class="mt-5 space-y-4">

        <div class="p-4 rounded-xl bg-red-50 border border-red-100">

          <div class="flex items-start gap-3">

            <span class="text-red-600 font-bold text-lg">
              !
            </span>

            <div>
              <p class="font-bold text-slate-900">
                Fire Safety Inspection
              </p>

              <p class="text-sm text-slate-500 mt-1">
                Public Market Complex
              </p>

              <p class="text-xs text-red-600 font-bold mt-2">
                Due Today • 09:00 AM
              </p>
            </div>

          </div>

        </div>


        <div class="p-4 rounded-xl bg-amber-50 border border-amber-100">

          <div class="flex items-start gap-3">

            <span class="text-amber-600 font-bold text-lg">
              !
            </span>

            <div>
              <p class="font-bold text-slate-900">
                Monthly Activity Report
              </p>

              <p class="text-sm text-slate-500 mt-1">
                Submit station activity report
              </p>

              <p class="text-xs text-amber-600 font-bold mt-2">
                Due Tomorrow
              </p>
            </div>

          </div>

        </div>

      </div>

    </div>


    <!-- RECENTLY COMPLETED -->
    <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <h3 class="text-lg font-bold text-slate-900">
        Recently Completed
      </h3>

      <p class="text-sm text-slate-500 mt-1">
        Your latest completed assignments.
      </p>

      <div class="mt-5 space-y-4">

        <div class="flex items-center gap-4 p-4 rounded-xl bg-green-50">

          <div class="h-10 w-10 rounded-full bg-green-100 flex items-center justify-center">
            <span class="text-green-600 font-bold">
              ✓
            </span>
          </div>

          <div>
            <p class="font-bold text-slate-900">
              Fire Drill Evaluation
            </p>

            <p class="text-xs text-slate-500 mt-1">
              Completed today
            </p>
          </div>

        </div>


        <div class="flex items-center gap-4 p-4 rounded-xl bg-green-50">

          <div class="h-10 w-10 rounded-full bg-green-100 flex items-center justify-center">
            <span class="text-green-600 font-bold">
              ✓
            </span>
          </div>

          <div>
            <p class="font-bold text-slate-900">
              Equipment Inspection
            </p>

            <p class="text-xs text-slate-500 mt-1">
              Completed yesterday
            </p>
          </div>

        </div>

      </div>

    </div>

  </section>


  <!-- ================================================= -->
  <!-- TASK INSTRUCTIONS -->
  <!-- ================================================= -->
  

</div>


    <!-- ================================================= -->
    <!-- REPORTS -->
    <!-- ================================================= -->
    <div
      v-else-if="activeTab === 'Reports'"
      class="w-full min-w-0 space-y-6"
    >

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">
          <div>
            <p class="text-sm font-semibold text-[#8B1E23]">FIRENOTIFY PERSONNEL PORTAL</p>
            <h2 class="text-2xl font-bold text-slate-900 mt-1">My Reports</h2>
            <p class="text-sm text-slate-500 mt-1">Submit, monitor, and review your operational reports.</p>
          </div>
          <button class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D] transition">+ Create Report</button>
        </div>
      </div>

      <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">Total Reports</p><p class="text-3xl font-bold text-slate-900 mt-1">16</p><p class="text-xs text-slate-400 mt-1">This month</p></div><div class="h-12 w-12 rounded-xl bg-blue-50 flex items-center justify-center"><span v-html="ICONS.reports" class="h-6 w-6 text-blue-600"></span></div></div></div>
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">Pending</p><p class="text-3xl font-bold text-yellow-600 mt-1">03</p><p class="text-xs text-slate-400 mt-1">Requires submission</p></div><div class="h-12 w-12 rounded-xl bg-yellow-50 flex items-center justify-center"><span v-html="ICONS.clock" class="h-6 w-6 text-yellow-600"></span></div></div></div>
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">Submitted</p><p class="text-3xl font-bold text-green-600 mt-1">12</p><p class="text-xs text-slate-400 mt-1">Successfully submitted</p></div><div class="h-12 w-12 rounded-xl bg-green-50 flex items-center justify-center"><span v-html="ICONS.check" class="h-6 w-6 text-green-600"></span></div></div></div>
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">Returned</p><p class="text-3xl font-bold text-[#8B1E23] mt-1">01</p><p class="text-xs text-slate-400 mt-1">Needs correction</p></div><div class="h-12 w-12 rounded-xl bg-red-50 flex items-center justify-center"><span v-html="ICONS.siren" class="h-6 w-6 text-[#8B1E23]"></span></div></div></div>
      </section>

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">
        <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
          <div><h3 class="text-lg font-bold text-slate-900">Report Records</h3><p class="text-sm text-slate-500 mt-1">Search and filter your submitted reports.</p></div>
          <div class="flex flex-col sm:flex-row gap-3"><input type="text" placeholder="Search reports..." class="px-4 py-2.5 rounded-xl border border-slate-200 bg-white text-sm outline-none focus:ring-2 focus:ring-[#8B1E23]/20" /><select class="px-4 py-2.5 rounded-xl border border-slate-200 bg-white text-sm text-slate-700"><option>All Status</option><option>Pending</option><option>Submitted</option><option>Returned</option></select></div>
        </div>
      </div>

      <section class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div class="lg:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
          <div class="flex items-center justify-between border-b border-slate-200 pb-4"><div><h3 class="text-lg font-bold text-slate-900">Report List</h3><p class="text-sm text-slate-500 mt-1">Your latest operational reports</p></div><span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">16 Reports</span></div>
          <div class="mt-5 space-y-4">
            <div class="p-5 rounded-xl border border-yellow-200 bg-yellow-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"><div class="flex gap-4"><div class="h-11 w-11 rounded-xl bg-yellow-100 flex items-center justify-center shrink-0"><span v-html="ICONS.reports" class="h-5 w-5 text-yellow-700"></span></div><div><p class="text-base font-bold text-slate-900">Fire Safety Inspection Report</p><p class="text-sm text-slate-500 mt-1">Activity: Fire Safety Inspection</p><p class="text-sm text-slate-500 mt-1">Due: September 12, 2026</p><p class="text-xs text-yellow-700 font-semibold mt-2">Action required</p></div></div><span class="w-fit px-3 py-1.5 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">Pending</span></div><div class="mt-4 flex flex-wrap gap-2"><button class="px-4 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-semibold hover:bg-[#72181D]">Submit Report</button><button @click="activeTab = 'Activities'" class="px-4 py-2 rounded-lg border border-slate-200 bg-white text-slate-700 text-sm font-semibold hover:bg-slate-100">View Activity</button></div></div>
            <div class="p-5 rounded-xl border border-green-200 bg-green-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"><div class="flex gap-4"><div class="h-11 w-11 rounded-xl bg-green-100 flex items-center justify-center shrink-0"><span v-html="ICONS.check" class="h-5 w-5 text-green-600"></span></div><div><p class="text-base font-bold text-slate-900">Routine Safety Patrol Report</p><p class="text-sm text-slate-500 mt-1">Activity: Routine Safety Patrol</p><p class="text-sm text-slate-500 mt-1">Submitted: September 7, 2026</p><p class="text-xs text-green-700 font-semibold mt-2">Successfully submitted</p></div></div><span class="w-fit px-3 py-1.5 rounded-full bg-green-100 text-green-700 text-xs font-bold">Submitted</span></div><div class="mt-4"><button class="px-4 py-2 rounded-lg border border-slate-200 bg-white text-slate-700 text-sm font-semibold hover:bg-slate-100">View Report</button></div></div>
            <div class="p-5 rounded-xl border border-red-200 bg-red-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"><div class="flex gap-4"><div class="h-11 w-11 rounded-xl bg-red-100 flex items-center justify-center shrink-0"><span v-html="ICONS.siren" class="h-5 w-5 text-[#8B1E23]"></span></div><div><p class="text-base font-bold text-slate-900">Fire Drill Monitoring Report</p><p class="text-sm text-slate-500 mt-1">Activity: Fire Drill Monitoring</p><p class="text-sm text-slate-500 mt-1">Returned: September 8, 2026</p><p class="text-xs text-[#8B1E23] font-semibold mt-2">Correction required</p></div></div><span class="w-fit px-3 py-1.5 rounded-full bg-red-100 text-[#8B1E23] text-xs font-bold">Returned</span></div><div class="mt-4 p-4 rounded-xl bg-white border border-red-200"><p class="text-xs font-semibold text-slate-500 uppercase">Remarks</p><p class="text-sm text-slate-700 mt-1">Please attach the attendance sheet and update the inspection details.</p></div><button class="mt-4 px-4 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-semibold hover:bg-[#72181D]">Revise Report</button></div>
            <div class="p-5 rounded-xl border border-slate-200 bg-slate-50"><div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4"><div><p class="text-base font-bold text-slate-900">Community Fire Safety Seminar Report</p><p class="text-sm text-slate-500 mt-1">Submitted September 5, 2026</p><p class="text-sm text-slate-500 mt-1">Barangay San Isidro</p></div><div class="flex items-center gap-2"><span class="px-3 py-1.5 rounded-full bg-green-100 text-green-700 text-xs font-bold">Submitted</span><button class="px-3 py-1.5 rounded-lg border border-slate-200 bg-white text-slate-700 text-xs font-semibold">View</button></div></div></div>
          </div>
        </div>

        <div class="space-y-6">
          <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Report Completion</h3><p class="text-sm text-slate-500 mt-1">Your report submission progress</p><div class="mt-5"><div class="flex items-end justify-between"><p class="text-3xl font-bold text-[#8B1E23]">80%</p><span class="text-xs font-semibold text-green-600">Good standing</span></div><div class="mt-3 h-3 rounded-full bg-slate-200 overflow-hidden"><div class="h-full w-[80%] bg-[#8B1E23] rounded-full"></div></div><div class="grid grid-cols-2 gap-4 mt-5"><div><p class="text-xs text-slate-500">Submitted</p><p class="text-lg font-bold text-green-600">12</p></div><div><p class="text-xs text-slate-500">Pending</p><p class="text-lg font-bold text-yellow-600">03</p></div></div></div></div>
          <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Report Deadlines</h3><p class="text-sm text-slate-500 mt-1">Upcoming submission deadlines</p><div class="mt-5 space-y-4"><div class="p-4 rounded-xl bg-yellow-50 border border-yellow-200"><div class="flex justify-between gap-3"><div><p class="text-sm font-bold text-slate-900">Fire Safety Inspection</p><p class="text-xs text-slate-500 mt-1">Due today</p></div><span class="text-xs font-bold text-yellow-700">Today</span></div></div><div class="p-4 rounded-xl bg-slate-50 border border-slate-200"><p class="text-sm font-bold text-slate-900">Community Seminar</p><p class="text-xs text-slate-500 mt-1">Due September 13, 2026</p></div><div class="p-4 rounded-xl bg-slate-50 border border-slate-200"><p class="text-sm font-bold text-slate-900">Emergency Drill</p><p class="text-xs text-slate-500 mt-1">Due September 15, 2026</p></div></div></div>
          <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Recent Activity</h3><div class="mt-5 space-y-4"><div class="flex gap-3"><div class="h-8 w-8 rounded-full bg-green-100 flex items-center justify-center shrink-0"><span v-html="ICONS.check" class="h-4 w-4 text-green-600"></span></div><div><p class="text-sm font-semibold text-slate-900">Report submitted</p><p class="text-xs text-slate-500 mt-1">Routine Safety Patrol Report</p><p class="text-xs text-slate-400 mt-1">September 7, 2026 · 03:25 PM</p></div></div><div class="flex gap-3"><div class="h-8 w-8 rounded-full bg-red-100 flex items-center justify-center shrink-0"><span v-html="ICONS.siren" class="h-4 w-4 text-[#8B1E23]"></span></div><div><p class="text-sm font-semibold text-slate-900">Report returned</p><p class="text-xs text-slate-500 mt-1">Fire Drill Monitoring Report</p><p class="text-xs text-slate-400 mt-1">September 8, 2026 · 10:15 AM</p></div></div></div></div>
        </div>
      </section>


    </div>


    <!-- ================================================= -->
<!-- PERSONNEL ROSTER -->
<!-- ================================================= -->
<div
  v-else-if="activeTab === 'Personnel Roster'"
  class="space-y-6"
>

  <!-- PAGE HEADER -->
  <section
    class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
  >
    <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

      <div>
        <p class="text-sm font-semibold text-[#8B1E23]">
          PERSONNEL MANAGEMENT
        </p>

        <h2 class="text-2xl font-bold text-slate-900 mt-1">
          Personnel Roster
        </h2>

        <p class="text-sm text-slate-500 mt-1">
          View personnel currently assigned to your station
        </p>
      </div>

      <div class="flex items-center gap-3">
        <div
          class="h-12 w-12 rounded-xl bg-[#8B1E23] flex items-center justify-center text-white"
        >
          <span v-html="ICONS.users || ICONS.check"></span>
        </div>

        <div>
          <p class="text-xs text-slate-400">
            Station Personnel
          </p>
          <p class="text-lg font-bold text-slate-900">
            {{ roster.length }} Personnel
          </p>
        </div>
      </div>

    </div>
  </section>


  <!-- SUMMARY CARDS -->
  <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">

    <!-- TOTAL -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-sm text-slate-500">
            Total Personnel
          </p>

          <p class="text-2xl font-bold text-slate-900 mt-1">
            {{ roster.length }}
          </p>
        </div>

        <div class="h-11 w-11 rounded-xl bg-slate-100 flex items-center justify-center">
          <span v-html="ICONS.users || ICONS.check"></span>
        </div>
      </div>
    </div>


    <!-- ACTIVE -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-sm text-slate-500">
            Active
          </p>

          <p class="text-2xl font-bold text-green-600 mt-1">
            09
          </p>
        </div>

        <div class="h-11 w-11 rounded-xl bg-green-100 flex items-center justify-center">
          <span class="text-green-600 font-bold">
            ✓
          </span>
        </div>
      </div>
    </div>


    <!-- ON DUTY -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-sm text-slate-500">
            On Duty
          </p>

          <p class="text-2xl font-bold text-[#8B1E23] mt-1">
            06
          </p>
        </div>

        <div class="h-11 w-11 rounded-xl bg-red-50 flex items-center justify-center">
          <span class="text-[#8B1E23] font-bold">
            ●
          </span>
        </div>
      </div>
    </div>


    <!-- OFF DUTY -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-sm text-slate-500">
            Off Duty
          </p>

          <p class="text-2xl font-bold text-amber-600 mt-1">
            03
          </p>
        </div>

        <div class="h-11 w-11 rounded-xl bg-amber-100 flex items-center justify-center">
          <span class="text-amber-600 font-bold">
            ◷
          </span>
        </div>
      </div>
    </div>

  </section>


  <!-- SEARCH AND FILTER -->
  <section
    class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5"
  >

    <div class="flex flex-col lg:flex-row gap-4">

      <!-- SEARCH -->
      <div class="flex-1">
        <label class="block text-sm font-semibold text-slate-700 mb-2">
          Search Personnel
        </label>

        <input
          type="text"
          placeholder="Search by name, rank, or role..."
          class="w-full px-4 py-3 rounded-xl border border-slate-300
                 focus:outline-none focus:ring-2 focus:ring-[#8B1E23]
                 focus:border-[#8B1E23]"
        />
      </div>


      <!-- STATUS -->
      <div class="w-full lg:w-52">
        <label class="block text-sm font-semibold text-slate-700 mb-2">
          Duty Status
        </label>

        <select
          class="w-full px-4 py-3 rounded-xl border border-slate-300
                 focus:outline-none focus:ring-2 focus:ring-[#8B1E23]"
        >
          <option>All Status</option>
          <option>On Duty</option>
          <option>Off Duty</option>
          <option>Leave</option>
        </select>
      </div>


      <!-- RANK -->
      <div class="w-full lg:w-52">
        <label class="block text-sm font-semibold text-slate-700 mb-2">
          Rank
        </label>

        <select
          class="w-full px-4 py-3 rounded-xl border border-slate-300
                 focus:outline-none focus:ring-2 focus:ring-[#8B1E23]"
        >
          <option>All Ranks</option>
          <option>Officer</option>
          <option>Fire Officer</option>
          <option>Senior Fire Officer</option>
        </select>
      </div>

    </div>

  </section>


  <!-- MAIN ROSTER -->
  <section class="grid grid-cols-1 lg:grid-cols-3 gap-6">

    <!-- PERSONNEL LIST -->
    <div
      class="lg:col-span-2 bg-white border border-slate-200
             rounded-2xl shadow-sm p-6"
    >

      <div class="flex items-center justify-between border-b border-slate-200 pb-4">

        <div>
          <h3 class="text-lg font-bold text-slate-900">
            Station Personnel
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            Current personnel assigned to this station
          </p>
        </div>

        <span
          class="px-3 py-1.5 rounded-full bg-slate-100
                 text-slate-700 text-xs font-bold"
        >
          {{ roster.length }} Members
        </span>

      </div>


      <!-- PERSONNEL CARDS -->
      <div class="mt-5 grid grid-cols-1 md:grid-cols-2 gap-4">

        <div
          v-for="person in roster"
          :key="person.name"
          class="p-5 bg-slate-50 border border-slate-200
                 rounded-xl hover:border-[#8B1E23]
                 hover:shadow-sm transition"
        >

          <!-- TOP -->
          <div class="flex items-start gap-4">

            <!-- AVATAR -->
            <div
              class="h-14 w-14 rounded-full bg-[#8B1E23]
                     flex items-center justify-center text-white
                     font-bold text-xs shrink-0"
            >
              {{ person.rank }}
            </div>


            <!-- INFO -->
            <div class="flex-1 min-w-0">

              <p class="text-base font-bold text-slate-900 truncate">
                {{ person.name }}
              </p>

              <p class="text-sm text-[#8B1E23] font-semibold mt-1">
                {{ person.role }}
              </p>

              <p class="text-sm text-slate-500 mt-1">
                {{ person.shift }}
              </p>

            </div>

            <!-- STATUS -->
            <span
              class="px-3 py-1.5 rounded-full
                     bg-green-100 text-green-700
                     text-xs font-bold"
            >
              Active
            </span>

          </div>


          <!-- DETAILS -->
          <div
            class="mt-4 pt-4 border-t border-slate-200
                   grid grid-cols-2 gap-3"
          >

            <div>
              <p class="text-xs text-slate-400">
                Assignment
              </p>

              <p class="text-sm font-semibold text-slate-700 mt-1">
                Station Duty
              </p>
            </div>

            <div>
              <p class="text-xs text-slate-400">
                Availability
              </p>

              <p class="text-sm font-semibold text-green-600 mt-1">
                Available
              </p>
            </div>

          </div>


          <!-- ACTION -->
          <button
            class="w-full mt-4 px-4 py-2.5 rounded-lg
                   border border-slate-300 bg-white
                   text-sm font-semibold text-slate-700
                   hover:bg-[#8B1E23] hover:text-white
                   hover:border-[#8B1E23] transition"
          >
            View Personnel Details
          </button>

        </div>

      </div>

    </div>


    <!-- RIGHT SIDE -->
    <div class="space-y-6">

      <!-- DUTY OVERVIEW -->
      <div
        class="bg-white border border-slate-200
               rounded-2xl shadow-sm p-6"
      >

        <h3 class="text-lg font-bold text-slate-900">
          Duty Overview
        </h3>

        <p class="text-sm text-slate-500 mt-1">
          Personnel availability today
        </p>


        <div class="mt-5 space-y-4">

          <!-- ON DUTY -->
          <div>
            <div class="flex justify-between text-sm mb-2">
              <span class="font-medium text-slate-600">
                On Duty
              </span>

              <span class="font-bold text-slate-900">
                06 / 09
              </span>
            </div>

            <div class="h-2 bg-slate-100 rounded-full overflow-hidden">
              <div
                class="h-full bg-[#8B1E23] rounded-full"
                style="width: 67%"
              ></div>
            </div>
          </div>


          <!-- OFF DUTY -->
          <div>
            <div class="flex justify-between text-sm mb-2">
              <span class="font-medium text-slate-600">
                Off Duty
              </span>

              <span class="font-bold text-slate-900">
                03 / 09
              </span>
            </div>

            <div class="h-2 bg-slate-100 rounded-full overflow-hidden">
              <div
                class="h-full bg-amber-400 rounded-full"
                style="width: 33%"
              ></div>
            </div>
          </div>

        </div>

      </div>


      <!-- SHIFT INFORMATION -->
      <div
        class="bg-white border border-slate-200
               rounded-2xl shadow-sm p-6"
      >

        <h3 class="text-lg font-bold text-slate-900">
          Shift Information
        </h3>

        <div class="mt-5 space-y-4">

          <div class="flex justify-between items-center">
            <span class="text-sm text-slate-500">
              Current Shift
            </span>

            <span class="text-sm font-bold text-slate-900">
              Day Shift
            </span>
          </div>

          <div class="flex justify-between items-center">
            <span class="text-sm text-slate-500">
              Time
            </span>

            <span class="text-sm font-bold text-slate-900">
              08:00 AM – 05:00 PM
            </span>
          </div>

          <div class="flex justify-between items-center">
            <span class="text-sm text-slate-500">
              Duty Officer
            </span>

            <span class="text-sm font-bold text-[#8B1E23]">
              Station Inspector
            </span>
          </div>

        </div>

      </div>


      <!-- ROSTER REMINDER -->
      <div
        
      >

        



      </div>

    </div>

  </section>

</div>


    <!-- ================================================= -->
    <!-- ACTIVITIES -->
    <!-- ================================================= -->
    <div
      v-else-if="activeTab === 'Activities'"
      class="space-y-6"
    >

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">
          <div>
            <p class="text-sm font-semibold text-[#8B1E23]">FIRENOTIFY PERSONNEL PORTAL</p>
            <h2 class="text-2xl font-bold text-slate-900 mt-1">Activities</h2>
            <p class="text-sm text-slate-500 mt-1">View and monitor activities assigned to your station.</p>
          </div>
          <div class="flex items-center gap-3">
            <div class="h-12 w-12 rounded-xl bg-[#8B1E23]/10 flex items-center justify-center">
              <span v-html="ICONS.tasks" class="h-6 w-6 text-[#8B1E23]"></span>
            </div>
            <div><p class="text-xs text-slate-500">Station</p><p class="text-base font-bold text-slate-900">BFP Balingasag</p></div>
          </div>
        </div>
      </div>

      <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">Total Activities</p><p class="text-3xl font-bold text-slate-900 mt-1">12</p><p class="text-xs text-slate-400 mt-1">This month</p></div><div class="h-12 w-12 rounded-xl bg-blue-50 flex items-center justify-center"><span v-html="ICONS.tasks" class="h-6 w-6 text-blue-600"></span></div></div></div>
        <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">Scheduled</p><p class="text-3xl font-bold text-yellow-600 mt-1">05</p><p class="text-xs text-slate-400 mt-1">Upcoming activities</p></div><div class="h-12 w-12 rounded-xl bg-yellow-50 flex items-center justify-center"><span v-html="ICONS.clock" class="h-6 w-6 text-yellow-600"></span></div></div></div>
        <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">Completed</p><p class="text-3xl font-bold text-green-600 mt-1">06</p><p class="text-xs text-slate-400 mt-1">Successfully completed</p></div><div class="h-12 w-12 rounded-xl bg-green-50 flex items-center justify-center"><span v-html="ICONS.check" class="h-6 w-6 text-green-600"></span></div></div></div>
        <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">Overdue</p><p class="text-3xl font-bold text-[#8B1E23] mt-1">01</p><p class="text-xs text-slate-400 mt-1">Needs attention</p></div><div class="h-12 w-12 rounded-xl bg-red-50 flex items-center justify-center"><span v-html="ICONS.siren" class="h-6 w-6 text-[#8B1E23]"></span></div></div></div>
      </section>

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">
        <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
          <div><h3 class="text-base font-bold text-slate-900">Activity List</h3><p class="text-sm text-slate-500">Review scheduled and completed station activities.</p></div>
          <div class="flex flex-col sm:flex-row gap-3"><select class="px-4 py-2.5 rounded-xl border border-slate-200 bg-white text-sm text-slate-700"><option>All Status</option><option>Scheduled</option><option>In Progress</option><option>Completed</option><option>Overdue</option></select><select class="px-4 py-2.5 rounded-xl border border-slate-200 bg-white text-sm text-slate-700"><option>All Activity Types</option><option>Inspection</option><option>Patrol</option><option>Training</option><option>Drill</option><option>Meeting</option></select></div>
        </div>
      </div>

      <section class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div class="lg:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
          <div class="flex items-center justify-between border-b border-slate-200 pb-4"><div><h3 class="text-lg font-bold text-slate-900">Assigned Activities</h3><p class="text-sm text-slate-500 mt-1">Activities assigned to your station</p></div><span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">12 Activities</span></div>
          <div class="mt-5 space-y-4">
            <div class="p-5 rounded-xl border border-yellow-200 bg-yellow-50/50"><div class="flex flex-col sm:flex-row sm:items-start gap-4"><div class="h-12 w-12 rounded-xl bg-blue-50 flex items-center justify-center shrink-0"><span v-html="ICONS.tasks" class="h-6 w-6 text-blue-600"></span></div><div class="flex-1"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-2"><div><p class="text-base font-bold text-slate-900">Fire Safety Inspection</p><p class="text-sm text-slate-500 mt-1">Public Market Complex</p></div><span class="w-fit px-3 py-1.5 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">Scheduled</span></div><div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-4"><p class="text-sm text-slate-500">September 12, 2026</p><p class="text-sm text-slate-500">09:00 AM</p><p class="text-sm text-slate-500">Assigned: FO3 Juan Dela Cruz</p><p class="text-sm text-slate-500">Balingasag</p></div><div class="mt-4 flex flex-wrap gap-2"><button class="px-4 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-semibold hover:bg-[#72181D]">View Details</button><button class="px-4 py-2 rounded-lg border border-slate-200 bg-white text-slate-700 text-sm font-semibold hover:bg-slate-100">Update Status</button></div></div></div></div>
            <div class="p-5 rounded-xl border border-blue-200 bg-blue-50/40"><div class="flex flex-col sm:flex-row sm:items-start gap-4"><div class="h-12 w-12 rounded-xl bg-blue-100 flex items-center justify-center shrink-0"><span v-html="ICONS.tasks" class="h-6 w-6 text-blue-600"></span></div><div class="flex-1"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-2"><div><p class="text-base font-bold text-slate-900">Community Fire Safety Seminar</p><p class="text-sm text-slate-500 mt-1">Barangay San Isidro Covered Court</p></div><span class="w-fit px-3 py-1.5 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">In Progress</span></div><div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-4"><p class="text-sm text-slate-500">September 13, 2026</p><p class="text-sm text-slate-500">01:00 PM</p><p class="text-sm text-slate-500">Assigned: FO2 Mark Santos</p><p class="text-sm text-slate-500">Balingasag</p></div><div class="mt-4"><div class="flex justify-between text-xs mb-2"><span class="text-slate-500">Progress</span><span class="font-bold text-blue-600">60%</span></div><div class="h-2 rounded-full bg-slate-200 overflow-hidden"><div class="h-full w-[60%] bg-blue-600 rounded-full"></div></div></div></div></div></div>
            <div class="p-5 rounded-xl border border-green-200 bg-green-50"><div class="flex flex-col sm:flex-row sm:items-start gap-4"><div class="h-12 w-12 rounded-xl bg-green-100 flex items-center justify-center shrink-0"><span v-html="ICONS.check" class="h-6 w-6 text-green-600"></span></div><div class="flex-1"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-2"><div><p class="text-base font-bold text-slate-900">Routine Safety Patrol</p><p class="text-sm text-slate-500 mt-1">Zone 2 Commercial Area</p></div><span class="w-fit px-3 py-1.5 rounded-full bg-green-100 text-green-700 text-xs font-bold">Completed</span></div><div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-4"><p class="text-sm text-slate-500">September 10, 2026</p><p class="text-sm text-slate-500">08:00 AM</p><p class="text-sm text-slate-500">Completed by: FO3 Juan Dela Cruz</p><p class="text-sm text-slate-500">Balingasag</p></div><p class="mt-4 text-xs font-semibold text-green-700">Activity completed successfully</p></div></div></div>
            <div class="p-5 rounded-xl border border-red-200 bg-red-50"><div class="flex flex-col sm:flex-row sm:items-start gap-4"><div class="h-12 w-12 rounded-xl bg-red-100 flex items-center justify-center shrink-0"><span v-html="ICONS.siren" class="h-6 w-6 text-[#8B1E23]"></span></div><div class="flex-1"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-2"><div><p class="text-base font-bold text-slate-900">Fire Drill Monitoring</p><p class="text-sm text-slate-500 mt-1">Municipal Elementary School</p></div><span class="w-fit px-3 py-1.5 rounded-full bg-red-100 text-[#8B1E23] text-xs font-bold">Overdue</span></div><div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-4"><p class="text-sm text-slate-500">September 09, 2026</p><p class="text-sm text-slate-500">10:00 AM</p><p class="text-sm text-slate-500">Assigned: FO1 Carlo Reyes</p><p class="text-sm text-slate-500">Balingasag</p></div><button class="mt-4 px-4 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-semibold hover:bg-[#72181D]">Resolve Activity</button></div></div></div>
          </div>
        </div>

        <div class="space-y-6">
          <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><div class="flex items-center justify-between"><div><h3 class="text-lg font-bold text-slate-900">Today's Activities</h3><p class="text-sm text-slate-500 mt-1">September 12, 2026</p></div><div class="h-10 w-10 rounded-xl bg-[#8B1E23]/10 flex items-center justify-center"><span v-html="ICONS.clock" class="h-5 w-5 text-[#8B1E23]"></span></div></div><div class="mt-5 space-y-4"><div class="flex gap-3"><div class="w-1 rounded-full bg-[#8B1E23]"></div><div><p class="text-sm font-bold text-slate-900">Fire Safety Inspection</p><p class="text-xs text-slate-500 mt-1">09:00 AM · Public Market</p><span class="inline-block mt-2 text-xs font-semibold text-yellow-700">Scheduled</span></div></div><div class="flex gap-3"><div class="w-1 rounded-full bg-green-500"></div><div><p class="text-sm font-bold text-slate-900">Station Briefing</p><p class="text-xs text-slate-500 mt-1">04:00 PM · BFP Station</p><span class="inline-block mt-2 text-xs font-semibold text-green-700">Scheduled</span></div></div></div></div>
          <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Upcoming Activities</h3><p class="text-sm text-slate-500 mt-1">Next scheduled activities</p><div class="mt-5 space-y-4"><div class="p-4 rounded-xl bg-slate-50 border border-slate-200"><p class="text-sm font-bold text-slate-900">Fire Safety Seminar</p><p class="text-xs text-slate-500 mt-1">September 13 · 01:00 PM</p><p class="text-xs text-slate-500 mt-1">Barangay San Isidro</p></div><div class="p-4 rounded-xl bg-slate-50 border border-slate-200"><p class="text-sm font-bold text-slate-900">Emergency Response Drill</p><p class="text-xs text-slate-500 mt-1">September 15 · 08:30 AM</p><p class="text-xs text-slate-500 mt-1">Balingasag Municipal Hall</p></div><div class="p-4 rounded-xl bg-slate-50 border border-slate-200"><p class="text-sm font-bold text-slate-900">Personnel Training</p><p class="text-xs text-slate-500 mt-1">September 17 · 09:00 AM</p><p class="text-xs text-slate-500 mt-1">BFP Training Room</p></div></div></div>
          <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Activity Performance</h3><p class="text-sm text-slate-500 mt-1">Current station completion rate</p><div class="mt-5"><div class="flex items-end justify-between"><p class="text-3xl font-bold text-[#8B1E23]">91.7%</p><span class="text-xs font-semibold text-green-600">+4.2% this month</span></div><div class="mt-3 h-3 rounded-full bg-slate-200 overflow-hidden"><div class="h-full w-[91.7%] bg-[#8B1E23] rounded-full"></div></div><div class="grid grid-cols-2 gap-4 mt-5"><div><p class="text-xs text-slate-500">Completed</p><p class="text-lg font-bold text-green-600">06</p></div><div><p class="text-xs text-slate-500">Pending</p><p class="text-lg font-bold text-yellow-600">05</p></div></div></div></div>
        </div>
      </section>

      

    </div>


    <!-- ================================================= -->
    <!-- STATION DUTY LOG -->
    <!-- ================================================= -->
    <div
      v-else-if="activeTab === 'Station Duty Log'"
      class="space-y-6"
    >
      <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">
          <div>
            <p class="text-sm font-semibold text-[#8B1E23]">FIRENOTIFY PERSONNEL PORTAL</p>
            <h2 class="text-2xl font-bold text-slate-900 mt-1">Station Duty Log</h2>
            <p class="text-sm text-slate-500 mt-1">Track duty assignments, shift attendance, and station activities.</p>
          </div>
          <button class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D] transition">+ Add Duty Entry</button>
        </div>
      </section>

      <section class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-5">
        <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><p class="text-sm text-slate-500">Duty Days This Month</p><p class="text-3xl font-bold text-slate-900 mt-2">22</p><p class="text-xs text-green-600 font-semibold mt-2">On schedule</p></div>
        <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><p class="text-sm text-slate-500">Hours Completed</p><p class="text-3xl font-bold text-blue-600 mt-2">168</p><p class="text-xs text-slate-400 mt-2">Of 176 scheduled hours</p></div>
        <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><p class="text-sm text-slate-500">Activities Logged</p><p class="text-3xl font-bold text-green-600 mt-2">18</p><p class="text-xs text-slate-400 mt-2">This month</p></div>
        <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><p class="text-sm text-slate-500">Pending Entries</p><p class="text-3xl font-bold text-[#8B1E23] mt-2">02</p><p class="text-xs text-red-600 font-semibold mt-2">Needs completion</p></div>
      </section>

      <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">
        <div class="flex flex-col lg:flex-row lg:items-end gap-4">
          <div class="flex-1"><label class="text-sm font-semibold text-slate-700">Date Range</label><select class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm text-slate-700"><option>This Month</option><option>This Week</option><option>Last Month</option><option>Custom Range</option></select></div>
          <div class="flex-1"><label class="text-sm font-semibold text-slate-700">Duty Status</label><select class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm text-slate-700"><option>All Statuses</option><option>On Duty</option><option>Completed</option><option>Pending</option><option>Absent</option></select></div>
          <div class="flex-1"><label class="text-sm font-semibold text-slate-700">Search Entries</label><input type="text" placeholder="Search duty logs..." class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm outline-none focus:ring-2 focus:ring-[#8B1E23]/20" /></div>
        </div>
      </section>

      <section class="grid grid-cols-1 xl:grid-cols-3 gap-6">
        <div class="xl:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
          <div class="flex items-center justify-between border-b border-slate-200 pb-4"><div><h3 class="text-lg font-bold text-slate-900">Duty Log Entries</h3><p class="text-sm text-slate-500 mt-1">Recent attendance and station duty records</p></div><span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">22 Records</span></div>
          <div class="mt-5 space-y-4">
            <div class="p-5 rounded-xl border border-green-200 bg-green-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"><div class="flex gap-4"><div class="h-11 w-11 rounded-xl bg-green-100 flex items-center justify-center shrink-0"><span v-html="ICONS.check" class="h-5 w-5 text-green-600"></span></div><div><p class="text-base font-bold text-slate-900">Regular Station Duty</p><p class="text-sm text-slate-500 mt-1">September 12, 2026 · Station 1</p><p class="text-sm text-slate-500 mt-1">Shift: 08:00 AM - 05:00 PM</p><p class="text-sm text-slate-500 mt-1">Activities: Briefing, equipment check, fire safety inspection</p></div></div><span class="w-fit px-3 py-1.5 rounded-full bg-green-100 text-green-700 text-xs font-bold">Completed</span></div></div>
            <div class="p-5 rounded-xl border border-blue-200 bg-blue-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"><div class="flex gap-4"><div class="h-11 w-11 rounded-xl bg-blue-100 flex items-center justify-center shrink-0"><span v-html="ICONS.clock" class="h-5 w-5 text-blue-600"></span></div><div><p class="text-base font-bold text-slate-900">Field Inspection Duty</p><p class="text-sm text-slate-500 mt-1">September 11, 2026 · Public Market Complex</p><p class="text-sm text-slate-500 mt-1">Shift: 09:00 AM - 04:30 PM</p><p class="text-sm text-slate-500 mt-1">Logged by FO3 Juan Dela Cruz</p></div></div><span class="w-fit px-3 py-1.5 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">Verified</span></div></div>
            <div class="p-5 rounded-xl border border-yellow-200 bg-yellow-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"><div class="flex gap-4"><div class="h-11 w-11 rounded-xl bg-yellow-100 flex items-center justify-center shrink-0"><span v-html="ICONS.clock" class="h-5 w-5 text-yellow-600"></span></div><div><p class="text-base font-bold text-slate-900">Station Support Duty</p><p class="text-sm text-slate-500 mt-1">September 10, 2026 · BFP Balingasag</p><p class="text-sm text-slate-500 mt-1">Shift: 08:00 AM - 05:00 PM</p><p class="text-sm text-slate-500 mt-1">Daily log requires supervisor review</p></div></div><span class="w-fit px-3 py-1.5 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">Pending Review</span></div></div>
            <div class="p-5 rounded-xl border border-slate-200 bg-slate-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"><div><p class="text-base font-bold text-slate-900">Emergency Response Drill</p><p class="text-sm text-slate-500 mt-1">September 9, 2026 · Municipal Training Ground</p><p class="text-sm text-slate-500 mt-1">Duration: 4 hours · Participants: 12 personnel</p></div><span class="w-fit px-3 py-1.5 rounded-full bg-slate-200 text-slate-700 text-xs font-bold">Archived</span></div></div>
          </div>
        </div>

        <div class="space-y-6">
          <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Current Shift</h3><div class="mt-5 p-5 rounded-xl bg-green-50 border border-green-100"><div class="flex items-center gap-3"><div class="h-3 w-3 rounded-full bg-green-500"></div><p class="font-bold text-green-700">Currently On Duty</p></div><p class="text-sm text-slate-500 mt-3">Station 1 · BFP Balingasag</p><p class="text-sm text-slate-500 mt-1">08:00 AM - 05:00 PM</p><p class="text-xs text-slate-400 mt-3">Started today at 08:00 AM</p></div></div>
          <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Attendance Summary</h3><div class="mt-5 space-y-4"><div><div class="flex justify-between text-sm"><span class="text-slate-500">Present</span><span class="font-bold text-green-600">20 days</span></div><div class="h-2 mt-2 rounded-full bg-slate-200"><div class="h-full w-[91%] rounded-full bg-green-500"></div></div></div><div><div class="flex justify-between text-sm"><span class="text-slate-500">Leave</span><span class="font-bold text-yellow-600">02 days</span></div><div class="h-2 mt-2 rounded-full bg-slate-200"><div class="h-full w-[9%] rounded-full bg-yellow-500"></div></div></div></div></div>
        </div>
      </section>

      <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4"><div><h3 class="text-lg font-bold text-slate-900">Monthly Duty Performance</h3><p class="text-sm text-slate-500 mt-1">Your station attendance and duty completion rate</p></div><p class="text-3xl font-bold text-[#8B1E23]">95%</p></div><div class="mt-4 h-3 rounded-full bg-slate-200 overflow-hidden"><div class="h-full w-[95%] rounded-full bg-[#8B1E23]"></div></div><div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mt-5"><div><p class="text-xs text-slate-500">Scheduled Shifts</p><p class="text-xl font-bold text-slate-900 mt-1">22</p></div><div><p class="text-xs text-slate-500">Completed Shifts</p><p class="text-xl font-bold text-green-600 mt-1">20</p></div><div><p class="text-xs text-slate-500">Logs Pending Review</p><p class="text-xl font-bold text-yellow-600 mt-1">02</p></div></div></section>
    </div>

    <!-- ================================================= -->
    <!-- EQUIPMENT AUDIT -->
    <!-- ================================================= -->
    <div
      v-else-if="activeTab === 'Equipment Audit'"
      class="space-y-6"
    >
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

    <!-- ================================================= -->
    <!-- DEADLINE MONITOR -->
    <!-- ================================================= -->
    <div
      v-else-if="activeTab === 'Deadline Monitor'"
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div class="border-b border-slate-200 pb-5">

        <h2 class="text-xl font-bold text-slate-900">
          Deadline Monitor
        </h2>

        <p class="text-sm text-slate-500 mt-1">
          Monitor upcoming and overdue report deadlines
        </p>

      </div>

      <!-- DEADLINE SUMMARY -->
      <div class="mt-5 grid grid-cols-1 sm:grid-cols-3 gap-4">

        <div class="p-5 rounded-xl bg-red-50 border border-red-200">
          <p class="text-sm font-semibold text-[#8B1E23]">
            Overdue
          </p>

          <p class="text-3xl font-bold text-slate-900 mt-1">
            02
          </p>
        </div>

        <div class="p-5 rounded-xl bg-yellow-50 border border-yellow-200">
          <p class="text-sm font-semibold text-yellow-700">
            Due Today
          </p>

          <p class="text-3xl font-bold text-slate-900 mt-1">
            03
          </p>
        </div>

        <div class="p-5 rounded-xl bg-blue-50 border border-blue-200">
          <p class="text-sm font-semibold text-blue-700">
            This Week
          </p>

          <p class="text-3xl font-bold text-slate-900 mt-1">
            06
          </p>
        </div>

      </div>

      <!-- DEADLINE LIST -->
      <div class="mt-6 space-y-4">

        <div class="p-5 rounded-xl border border-red-200 bg-red-50">

          <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">

            <div>
              <p class="text-base font-bold text-slate-900">
                Incident Report
              </p>

              <p class="text-sm text-slate-500 mt-1">
                Deadline: September 8, 2026
              </p>
            </div>

            <span class="px-4 py-2 rounded-full bg-[#8B1E23] text-white text-sm font-bold">
              OVERDUE
            </span>

          </div>

        </div>

        <div class="p-5 rounded-xl border border-yellow-200 bg-yellow-50">

          <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">

            <div>
              <p class="text-base font-bold text-slate-900">
                Fire Safety Inspection Report
              </p>

              <p class="text-sm text-slate-500 mt-1">
                Deadline: September 12, 2026
              </p>
            </div>

            <span class="px-4 py-2 rounded-full bg-yellow-100 text-yellow-700 text-sm font-bold">
              3 DAYS LEFT
            </span>

          </div>

        </div>

      </div>

    </div>


    <!-- ================================================= -->
    <!-- NOTIFICATIONS -->
    <!-- ================================================= -->
    <div
      v-else-if="activeTab === 'Notifications'"
      class="space-y-6"
    >

      <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
          <div><h2 class="text-2xl font-bold text-slate-900">Notifications</h2><p class="text-sm text-slate-500 mt-1">Important announcements, reminders, and system alerts</p></div>
          <button class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-semibold hover:bg-[#72181D] transition">Mark All as Read</button>
        </div>
      </section>

      <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">Unread</p><p class="text-3xl font-bold text-[#8B1E23] mt-1">03</p></div><div class="h-11 w-11 rounded-full bg-red-100 flex items-center justify-center"><span v-html="ICONS.siren" class="h-5 w-5 text-[#8B1E23]"></span></div></div></div>
        <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">Task Alerts</p><p class="text-3xl font-bold text-slate-900 mt-1">02</p></div><div class="h-11 w-11 rounded-full bg-blue-100 flex items-center justify-center"><span v-html="ICONS.tasks" class="h-5 w-5 text-blue-600"></span></div></div></div>
        <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">Report Alerts</p><p class="text-3xl font-bold text-slate-900 mt-1">04</p></div><div class="h-11 w-11 rounded-full bg-amber-100 flex items-center justify-center"><span v-html="ICONS.reports" class="h-5 w-5 text-amber-600"></span></div></div></div>
        <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><div class="flex items-center justify-between"><div><p class="text-sm text-slate-500">System Alerts</p><p class="text-3xl font-bold text-slate-900 mt-1">01</p></div><div class="h-11 w-11 rounded-full bg-green-100 flex items-center justify-center"><span v-html="ICONS.check" class="h-5 w-5 text-green-600"></span></div></div></div>
      </section>

      <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">
        <div class="flex flex-col lg:flex-row gap-4"><div class="flex-1"><label class="text-sm font-semibold text-slate-700">Notification Type</label><select class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-slate-700 focus:outline-none focus:ring-2 focus:ring-[#8B1E23]"><option>All Notifications</option><option>Task Alerts</option><option>Report Alerts</option><option>Activity Reminders</option><option>System Alerts</option></select></div><div class="flex-1"><label class="text-sm font-semibold text-slate-700">Status</label><select class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-slate-700 focus:outline-none focus:ring-2 focus:ring-[#8B1E23]"><option>All</option><option>Unread</option><option>Read</option></select></div></div>
      </section>

      <section class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div class="lg:col-span-2 space-y-4">
          <div class="p-5 rounded-2xl border border-red-200 bg-red-50 shadow-sm"><div class="flex items-start gap-4"><div class="h-12 w-12 rounded-full bg-red-100 flex items-center justify-center shrink-0"><span v-html="ICONS.siren" class="h-6 w-6 text-[#8B1E23]"></span></div><div class="flex-1"><div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2"><p class="text-base font-bold text-slate-900">Report Deadline Reminder</p><span class="text-xs font-semibold text-[#8B1E23]">UNREAD</span></div><p class="text-sm text-slate-600 mt-1">Your Fire Safety Inspection Report is due on September 12, 2026.</p><div class="flex items-center gap-2 mt-3"><span class="text-xs text-slate-400">10 minutes ago</span><span class="h-1 w-1 rounded-full bg-slate-300"></span><span class="text-xs font-medium text-red-600">Urgent</span></div></div><span class="h-3 w-3 rounded-full bg-[#8B1E23] shrink-0"></span></div></div>
          <div class="p-5 rounded-2xl border border-blue-200 bg-blue-50 shadow-sm"><div class="flex items-start gap-4"><div class="h-12 w-12 rounded-full bg-blue-100 flex items-center justify-center shrink-0"><span v-html="ICONS.tasks" class="h-6 w-6 text-blue-600"></span></div><div class="flex-1"><div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2"><p class="text-base font-bold text-slate-900">New Task Assigned</p><span class="text-xs font-semibold text-blue-600">UNREAD</span></div><p class="text-sm text-slate-600 mt-1">You have been assigned to the Public Market Fire Safety Inspection.</p><div class="flex items-center gap-2 mt-3"><span class="text-xs text-slate-400">1 hour ago</span><span class="h-1 w-1 rounded-full bg-slate-300"></span><span class="text-xs font-medium text-blue-600">Task Assignment</span></div></div></div></div>
          <div class="p-5 rounded-2xl border border-green-200 bg-green-50 shadow-sm"><div class="flex items-start gap-4"><div class="h-12 w-12 rounded-full bg-green-100 flex items-center justify-center shrink-0"><span v-html="ICONS.check" class="h-6 w-6 text-green-600"></span></div><div class="flex-1"><div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2"><p class="text-base font-bold text-slate-900">Report Accepted</p><span class="text-xs font-semibold text-green-600">READ</span></div><p class="text-sm text-slate-600 mt-1">Your Routine Safety Patrol Report has been successfully recorded.</p><div class="flex items-center gap-2 mt-3"><span class="text-xs text-slate-400">Yesterday</span><span class="h-1 w-1 rounded-full bg-slate-300"></span><span class="text-xs font-medium text-green-600">Report Update</span></div></div></div></div>
          <div class="p-5 rounded-2xl border border-amber-200 bg-amber-50 shadow-sm"><div class="flex items-start gap-4"><div class="h-12 w-12 rounded-full bg-amber-100 flex items-center justify-center shrink-0"><span v-html="ICONS.siren" class="h-6 w-6 text-amber-600"></span></div><div class="flex-1"><p class="text-base font-bold text-slate-900">Activity Reminder</p><p class="text-sm text-slate-600 mt-1">Your scheduled Fire Safety Seminar will begin tomorrow at 9:00 AM.</p><p class="text-xs text-slate-400 mt-3">Yesterday</p></div></div></div>
          <div class="p-5 rounded-2xl border border-slate-200 bg-white shadow-sm"><div class="flex items-start gap-4"><div class="h-12 w-12 rounded-full bg-slate-100 flex items-center justify-center shrink-0"><span v-html="ICONS.check" class="h-6 w-6 text-slate-600"></span></div><div class="flex-1"><p class="text-base font-bold text-slate-900">System Update</p><p class="text-sm text-slate-600 mt-1">FireNotify notification services are operating normally.</p><p class="text-xs text-slate-400 mt-3">2 days ago</p></div></div></div>
        </div>

        <div class="space-y-6">
          <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Notification Settings</h3><p class="text-sm text-slate-500 mt-1">Choose how you receive important alerts.</p><div class="mt-5 space-y-4"><div class="flex items-center justify-between"><div><p class="text-sm font-semibold text-slate-800">Task Reminders</p><p class="text-xs text-slate-500">Alerts for assigned tasks</p></div><input type="checkbox" checked class="h-5 w-5 accent-[#8B1E23]" /></div><div class="flex items-center justify-between"><div><p class="text-sm font-semibold text-slate-800">Report Deadlines</p><p class="text-xs text-slate-500">Reminders before deadlines</p></div><input type="checkbox" checked class="h-5 w-5 accent-[#8B1E23]" /></div><div class="flex items-center justify-between"><div><p class="text-sm font-semibold text-slate-800">Activity Alerts</p><p class="text-xs text-slate-500">Upcoming activity reminders</p></div><input type="checkbox" checked class="h-5 w-5 accent-[#8B1E23]" /></div></div></div>
          <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Upcoming Deadlines</h3><div class="mt-4 space-y-4"><div class="p-4 rounded-xl bg-red-50 border border-red-100"><p class="text-sm font-bold text-slate-900">Fire Safety Inspection Report</p><p class="text-xs text-red-600 font-semibold mt-1">Due Today</p></div><div class="p-4 rounded-xl bg-amber-50 border border-amber-100"><p class="text-sm font-bold text-slate-900">Monthly Operations Report</p><p class="text-xs text-amber-600 font-semibold mt-1">Due in 5 days</p></div><div class="p-4 rounded-xl bg-slate-50 border border-slate-200"><p class="text-sm font-bold text-slate-900">Activity Compliance Report</p><p class="text-xs text-slate-500 font-semibold mt-1">Due in 8 days</p></div></div></div>
        </div>
      </section>


    </div>


    <!-- ================================================= -->
    <!-- SUPPORT -->
    <!-- ================================================= -->
    <div
      v-else-if="activeTab === 'Support'"
      class="space-y-6"
    >
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

    <!-- ================================================= -->
    <!-- SETTINGS -->
    <!-- ================================================= -->
    <div
      v-else-if="activeTab === 'Settings'"
      class="space-y-6"
    >
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

    <!-- ================================================= -->
    <!-- OTHER -->
    <!-- ================================================= -->
    <div
      v-else
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-10 text-center"
    >

      <div class="mx-auto h-16 w-16 rounded-full bg-red-50 flex items-center justify-center">

        <span
          v-html="ICONS[getActiveIcon()]"
          class="h-8 w-8 text-[#8B1E23]"
        ></span>

      </div>

      <h2 class="mt-5 text-2xl font-bold text-slate-900">
        {{ activeTab }}
      </h2>

      <p class="mt-2 text-base text-slate-500 max-w-lg mx-auto">
        This section contains personnel information and operational
        controls related to {{ activeTab }}.
      </p>

    </div>

  </div>


  <!-- =================================================== -->
  <!-- RIGHT SIDEBAR -->
  <!-- =================================================== -->
  

</section>

      </main>

    </div>


    <!-- ========================================================= -->
    <!-- SIGN OUT MODAL -->
    <!-- ========================================================= -->
    <div
      v-if="showLogoutConfirm"
      class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 backdrop-blur-sm px-4"
    >

      <div
        class="w-full max-w-md bg-white rounded-2xl shadow-2xl overflow-hidden"
      >

        <!-- TOP ACCENT -->
        <div class="h-2 bg-[#8B1E23]"></div>


        <div class="p-7">

          <div class="flex items-start gap-4">

            <div
              class="h-14 w-14 rounded-full bg-red-50 flex items-center justify-center shrink-0"
            >

              <span
                v-html="ICONS.siren"
                class="h-7 w-7 text-[#8B1E23]"
              ></span>

            </div>

            <div>

              <h3 class="text-xl font-bold text-slate-900">
                Confirm Sign Out
              </h3>

              <p class="text-base text-slate-500 mt-1">
                Are you sure you want to exit the Personnel Portal?
              </p>

            </div>

          </div>


          <div
            class="mt-5 p-4 rounded-xl bg-yellow-50 border border-yellow-200"
          >

            <p class="text-sm text-slate-600 leading-relaxed">
              Any unsaved changes in active forms or field logs may be lost
              when you sign out.
            </p>

          </div>


          <div class="flex flex-col-reverse sm:flex-row justify-end gap-3 mt-7">

            <button
              @click="showLogoutConfirm = false"
              class="w-full sm:w-auto px-6 py-3 rounded-xl border border-slate-300 bg-white text-slate-700 text-base font-semibold hover:bg-slate-100 transition"
            >
              Cancel
            </button>

            <button
              @click="confirmLogout"
              class="w-full sm:w-auto px-6 py-3 rounded-xl bg-[#8B1E23] text-white text-base font-semibold hover:bg-[#72181D] transition shadow-sm"
            >
              Sign Out
            </button>

          </div>

        </div>
        
      </div>

    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  currentUser: {
    type: Object,
    required: false,
    default: null
  }
})

const emit = defineEmits(['logout'])

const activeTab = ref('Dashboard')
const showLogoutConfirm = ref(false)

const ICONS = {
  dashboard: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/></svg>',
  tasks: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 2.5h6a1 1 0 011 1V5H8V3.5a1 1 0 011-1z"/><path d="M9 11h6M9 15h6"/></svg>',
  reports: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><path d="M14 2v6h6"/><path d="M9 13h6M9 17h6"/></svg>',
  notifications: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M18 8a6 6 0 10-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 01-3.46 0"/></svg>',
  bell: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M18 8a6 6 0 10-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 01-3.46 0"/></svg>',
  roster: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>',
  dutylog: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>',
  equipment: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg>',
  support: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M3 18v-6a9 9 0 0118 0v6"/><path d="M21 19a2 2 0 01-2 2h-1a2 2 0 01-2-2v-3a2 2 0 012-2h3zM3 19a2 2 0 002 2h1a2 2 0 002-2v-3a2 2 0 00-2-2H3z"/></svg>',
  settings: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 11-2.83 2.83l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-4 0v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 11-2.83-2.83l.06-.06a1.65 1.65 0 00.33-1.82 1.65 1.65 0 00-1.51-1H3a2 2 0 010-4h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 112.83-2.83l.06.06a1.65 1.65 0 001.82.33H9a1.65 1.65 0 001-1.51V3a2 2 0 014 0v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 112.83 2.83l-.06.06a1.65 1.65 0 00-.33 1.82V9a1.65 1.65 0 001.51 1H21a2 2 0 010 4h-.09a1.65 1.65 0 00-1.51 1z"/></svg>',
  logout: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M9 21H5a2 2 0 01-2-2V5a2 2 0 012-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/></svg>',
  siren: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
  check: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
  clock: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
  pin: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M12 21s7-6.8 7-12a7 7 0 10-14 0c0 5.2 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>'
}

const fieldItems = [
  { name: 'Dashboard', icon: 'dashboard', context: 'Operations overview', badge: null },
  { name: 'Tasks', icon: 'tasks', context: 'Assigned activities', badge: '4' },
  { name: 'Activities', icon: 'clock', context: 'View station activities' },
  { name: 'Reports', icon: 'reports', context: 'Submit accomplishment reports', badge: '3' },
  { name: 'Notifications', icon: 'notifications', context: 'Deadlines & station alerts', badge: '3' }
]

const managementItems = [
  { name: 'Personnel Roster', icon: 'roster', context: 'View station personnel' },
  { name: 'Station Duty Log', icon: 'dutylog', context: 'Track duty & shift records' },
  { name: 'Equipment Audit', icon: 'equipment', context: 'Monitor equipment status' }
]

const toolItems = [
  { name: 'Support', icon: 'support', context: 'Get system assistance' },
  { name: 'Settings', icon: 'settings', context: 'Account & preferences' }
]

const taskList = ref([
  { title: 'Check hydrant systems in Sector 1', due: 'Today, 5:00 PM' },
  { title: 'Submit incident log for Station 2', due: 'Tomorrow, 10:00 AM' },
  { title: 'Conduct Fire Safety Inspection', due: 'Aug 22, 2026' }
])

const roster = ref([
  { name: 'Juan Dela Cruz', rank: 'FO3', role: 'Inspector', shift: 'Day' },
  { name: 'Mark Santos', rank: 'SFO1', role: 'Chief', shift: 'Day' },
  { name: 'Alan Reyes', rank: 'FO1', role: 'Equipment', shift: 'Night' }
])

const confirmLogout = () => {
  showLogoutConfirm.value = false
  emit('logout')
}

const getActiveIcon = () => {
  const allItems = [...fieldItems, ...managementItems, ...toolItems]
  const found = allItems.find(item => item.name === activeTab.value)
  return found ? found.icon : 'pin'
}
</script>

<style scoped>
.font-display { font-family: 'Oswald', 'Arial Narrow', sans-serif; }
.font-body { font-family: 'IBM Plex Sans', 'Helvetica Neue', sans-serif; }
.font-mono { font-family: 'IBM Plex Mono', 'SFMono-Regular', monospace; }

/* Custom Scrollbar */
.custom-scrollbar::-webkit-scrollbar {
  width: 5px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: #15120F;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #3A3530;
  border-radius: 2px;
}
.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: #E8A33D;
}
</style>