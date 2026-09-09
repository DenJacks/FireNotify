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
      <main class="p-6 lg:p-8 space-y-7">


        <!-- ===================================================== -->
        <!-- WELCOME -->
        <!-- ===================================================== -->
        <section
          class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6"
        >

          <div
            class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5"
          >

            <div>

              <p class="text-sm font-medium text-[#8B1E23] mb-1">
                FIRENOTIFY PERSONNEL PORTAL
              </p>

              <h2 class="text-2xl lg:text-3xl font-bold text-slate-900">
                Welcome back,
                {{ currentUser?.firstName || 'Juan' }}!
              </h2>

              <p class="mt-2 text-base text-slate-500">
                Monitor your assigned tasks, reports, and station activities.
              </p>

            </div>


            <div
              class="flex items-center gap-3 px-5 py-4 rounded-xl bg-[#8B1E23] text-white"
            >

              <div
                class="h-11 w-11 rounded-full bg-white/10 flex items-center justify-center"
              >
                <span
                  v-html="ICONS.siren"
                  class="h-6 w-6 text-[#F4C542]"
                ></span>
              </div>

              <div>

                <p class="text-xs text-white/70">
                  Current Status
                </p>

                <p class="text-base font-bold">
                  On Duty
                </p>

              </div>

            </div>

          </div>

        </section>


        <!-- ===================================================== -->
        <!-- SUMMARY CARDS -->
        <!-- ===================================================== -->
        <section>


         


    


          
        </section>


        <!-- ===================================================== -->
<!-- MAIN GRID -->
<!-- ===================================================== -->
<section class="grid grid-cols-1 lg:grid-cols-3 gap-6">

  <!-- =================================================== -->
  <!-- LEFT CONTENT -->
  <!-- =================================================== -->
  <div class="lg:col-span-2 space-y-6">

    <!-- ================================================= -->
    <!-- DASHBOARD -->
    <!-- ================================================= -->
    <div
      v-if="activeTab === 'Dashboard'"
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
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
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 border-b border-slate-200 pb-5">

        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Assigned Tasks
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Activities and duties assigned to you
          </p>
        </div>

        <span class="px-4 py-2 rounded-full bg-blue-50 text-blue-700 text-sm font-bold">
          09 Total Tasks
        </span>

      </div>

      <div class="mt-5 space-y-4">

        <div
          v-for="task in taskList"
          :key="task.title"
          class="p-5 rounded-xl border border-slate-200 bg-slate-50"
        >

          <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">

            <div class="flex items-start gap-4">

              <div class="h-11 w-11 rounded-full bg-blue-100 flex items-center justify-center shrink-0">
                <span
                  v-html="ICONS.tasks"
                  class="h-5 w-5 text-blue-600"
                ></span>
              </div>

              <div>
                <p class="text-base font-bold text-slate-900">
                  {{ task.title }}
                </p>

                <p class="text-sm text-slate-500 mt-1">
                  Due: {{ task.due }}
                </p>

                <p class="text-sm text-slate-500 mt-1">
                  Assigned to your station
                </p>
              </div>

            </div>

            <button
              class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]"
            >
              Update Status
            </button>

          </div>

        </div>

      </div>

    </div>


    <!-- ================================================= -->
    <!-- REPORTS -->
    <!-- ================================================= -->
    <div
      v-else-if="activeTab === 'Reports'"
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div class="border-b border-slate-200 pb-5">

        <h2 class="text-xl font-bold text-slate-900">
          My Reports
        </h2>

        <p class="text-sm text-slate-500 mt-1">
          Submit and monitor your operational reports
        </p>

      </div>

      <!-- REPORT SUMMARY -->
      <div class="mt-5 grid grid-cols-1 sm:grid-cols-3 gap-4">

        <div class="p-4 rounded-xl bg-yellow-50 border border-yellow-200">
          <p class="text-sm font-semibold text-yellow-700">
            Pending
          </p>
          <p class="text-2xl font-bold text-slate-900 mt-1">
            03
          </p>
        </div>

        <div class="p-4 rounded-xl bg-green-50 border border-green-200">
          <p class="text-sm font-semibold text-green-700">
            Submitted
          </p>
          <p class="text-2xl font-bold text-slate-900 mt-1">
            12
          </p>
        </div>

        <div class="p-4 rounded-xl bg-red-50 border border-red-200">
          <p class="text-sm font-semibold text-[#8B1E23]">
            Returned
          </p>
          <p class="text-2xl font-bold text-slate-900 mt-1">
            01
          </p>
        </div>

      </div>

      <!-- REPORT LIST -->
      <div class="mt-6 space-y-3">

        <div class="p-5 rounded-xl border border-yellow-200 bg-yellow-50">

          <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">

            <div>
              <p class="text-base font-bold text-slate-900">
                Fire Safety Inspection Report
              </p>

              <p class="text-sm text-slate-500 mt-1">
                Due: September 12, 2026
              </p>
            </div>

            <button
              class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold"
            >
              Submit Report
            </button>

          </div>

        </div>

        <div class="p-5 rounded-xl border border-green-200 bg-green-50">

          <div class="flex items-center justify-between gap-4">

            <div>
              <p class="text-base font-bold text-slate-900">
                Routine Safety Patrol Report
              </p>

              <p class="text-sm text-slate-500 mt-1">
                Submitted September 7, 2026
              </p>
            </div>

            <span class="px-4 py-2 rounded-full bg-green-100 text-green-700 text-sm font-bold">
              Submitted
            </span>

          </div>

        </div>

      </div>

    </div>


    <!-- ================================================= -->
    <!-- PERSONNEL ROSTER -->
    <!-- ================================================= -->
    <div
      v-else-if="activeTab === 'Personnel Roster'"
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div class="border-b border-slate-200 pb-5">

        <h2 class="text-xl font-bold text-slate-900">
          Personnel Roster
        </h2>

        <p class="text-sm text-slate-500 mt-1">
          View personnel currently assigned to your station
        </p>

      </div>

      <div class="mt-5 grid grid-cols-1 md:grid-cols-2 gap-4">

        <div
          v-for="person in roster"
          :key="person.name"
          class="p-5 bg-slate-50 border border-slate-200 rounded-xl"
        >

          <div class="flex items-center gap-4">

            <div
              class="h-14 w-14 rounded-full bg-[#8B1E23] flex items-center justify-center text-white font-bold text-xs shrink-0"
            >
              {{ person.rank }}
            </div>

            <div class="flex-1 min-w-0">

              <p class="text-base font-bold text-slate-900 truncate">
                {{ person.name }}
              </p>

              <p class="text-sm text-slate-600 mt-1">
                {{ person.role }}
              </p>

              <p class="text-sm text-slate-400 mt-1">
                {{ person.shift }}
              </p>

            </div>

            <span class="px-3 py-1.5 rounded-full bg-green-100 text-green-700 text-xs font-bold">
              Active
            </span>

          </div>

        </div>

      </div>

    </div>


    <!-- ================================================= -->
    <!-- ACTIVITY MANAGEMENT -->
    <!-- ================================================= -->
    <div
      v-else-if="activeTab === 'Activity Management'"
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 border-b border-slate-200 pb-5">

        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Activity Management
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            View activities assigned to your station
          </p>
        </div>

        <span class="px-4 py-2 rounded-full bg-blue-50 text-blue-700 text-sm font-bold">
          Station Activities
        </span>

      </div>

      <div class="mt-5 space-y-4">

        <div class="p-5 rounded-xl border border-slate-200 bg-slate-50">

          <div class="flex items-start gap-4">

            <div class="h-12 w-12 rounded-xl bg-blue-50 flex items-center justify-center shrink-0">
              <span
                v-html="ICONS.tasks"
                class="h-6 w-6 text-blue-600"
              ></span>
            </div>

            <div class="flex-1">

              <p class="text-base font-bold text-slate-900">
                Fire Safety Inspection
              </p>

              <p class="text-sm text-slate-500 mt-1">
                September 12, 2026 · 09:00 AM
              </p>

              <p class="text-sm text-slate-500 mt-1">
                Public Market Complex
              </p>

            </div>

            <span class="px-3 py-1.5 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">
              Scheduled
            </span>

          </div>

        </div>

        <div class="p-5 rounded-xl border border-green-200 bg-green-50">

          <div class="flex items-start gap-4">

            <div class="h-12 w-12 rounded-xl bg-green-100 flex items-center justify-center shrink-0">
              <span
                v-html="ICONS.check"
                class="h-6 w-6 text-green-600"
              ></span>
            </div>

            <div class="flex-1">

              <p class="text-base font-bold text-slate-900">
                Routine Safety Patrol
              </p>

              <p class="text-sm text-slate-500 mt-1">
                Zone 2 Commercial Area
              </p>

            </div>

            <span class="px-3 py-1.5 rounded-full bg-green-100 text-green-700 text-xs font-bold">
              Completed
            </span>

          </div>

        </div>

      </div>

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
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div class="border-b border-slate-200 pb-5">

        <h2 class="text-xl font-bold text-slate-900">
          Notifications
        </h2>

        <p class="text-sm text-slate-500 mt-1">
          Important announcements, reminders, and system alerts
        </p>

      </div>

      <div class="mt-5 space-y-4">

        <!-- NOTIFICATION 1 -->
        <div class="p-5 rounded-xl border border-red-200 bg-red-50">

          <div class="flex items-start gap-4">

            <div class="h-11 w-11 rounded-full bg-red-100 flex items-center justify-center shrink-0">

              <span
                v-html="ICONS.siren"
                class="h-5 w-5 text-[#8B1E23]"
              ></span>

            </div>

            <div class="flex-1">

              <p class="text-base font-bold text-slate-900">
                Report Deadline Reminder
              </p>

              <p class="text-sm text-slate-600 mt-1">
                Your Fire Safety Inspection Report is due on September 12, 2026.
              </p>

              <p class="text-xs text-slate-400 mt-2">
                10 minutes ago
              </p>

            </div>

            <span class="h-3 w-3 rounded-full bg-[#8B1E23] shrink-0"></span>

          </div>

        </div>


        <!-- NOTIFICATION 2 -->
        <div class="p-5 rounded-xl border border-blue-200 bg-blue-50">

          <div class="flex items-start gap-4">

            <div class="h-11 w-11 rounded-full bg-blue-100 flex items-center justify-center shrink-0">

              <span
                v-html="ICONS.tasks"
                class="h-5 w-5 text-blue-600"
              ></span>

            </div>

            <div class="flex-1">

              <p class="text-base font-bold text-slate-900">
                New Task Assigned
              </p>

              <p class="text-sm text-slate-600 mt-1">
                You have been assigned to the Public Market Fire Safety Inspection.
              </p>

              <p class="text-xs text-slate-400 mt-2">
                1 hour ago
              </p>

            </div>

          </div>

        </div>


        <!-- NOTIFICATION 3 -->
        <div class="p-5 rounded-xl border border-green-200 bg-green-50">

          <div class="flex items-start gap-4">

            <div class="h-11 w-11 rounded-full bg-green-100 flex items-center justify-center shrink-0">

              <span
                v-html="ICONS.check"
                class="h-5 w-5 text-green-600"
              ></span>

            </div>

            <div class="flex-1">

              <p class="text-base font-bold text-slate-900">
                Report Accepted
              </p>

              <p class="text-sm text-slate-600 mt-1">
                Your Routine Safety Patrol Report has been successfully recorded.
              </p>

              <p class="text-xs text-slate-400 mt-2">
                Yesterday
              </p>

            </div>

          </div>

        </div>

      </div>

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
  <div class="space-y-6">

    <!-- ================================================= -->
    <!-- QUICK ACTIONS -->
    <!-- ================================================= -->
    <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <h3 class="text-xl font-bold text-slate-900">
        Quick Actions
      </h3>

      <p class="text-sm text-slate-500 mt-1">
        Frequently used personnel actions
      </p>

      <div class="mt-5 space-y-3">

        <button
          @click="activeTab = 'Tasks'"
          class="w-full flex items-center gap-3 p-4 rounded-xl bg-blue-50 hover:bg-blue-100 text-left transition"
        >

          <span
            v-html="ICONS.tasks"
            class="h-6 w-6 text-blue-600"
          ></span>

          <div>
            <p class="text-sm font-bold text-slate-900">
              View My Tasks
            </p>

            <p class="text-xs text-slate-500">
              Check assigned duties
            </p>
          </div>

        </button>


        <button
          @click="activeTab = 'Reports'"
          class="w-full flex items-center gap-3 p-4 rounded-xl bg-yellow-50 hover:bg-yellow-100 text-left transition"
        >

          <span
            v-html="ICONS.reports"
            class="h-6 w-6 text-yellow-600"
          ></span>

          <div>
            <p class="text-sm font-bold text-slate-900">
              My Reports
            </p>

            <p class="text-xs text-slate-500">
              Submit pending reports
            </p>
          </div>

        </button>


        <button
          @click="activeTab = 'Deadline Monitor'"
          class="w-full flex items-center gap-3 p-4 rounded-xl bg-red-50 hover:bg-red-100 text-left transition"
        >

          <span
            v-html="ICONS.siren"
            class="h-6 w-6 text-[#8B1E23]"
          ></span>

          <div>
            <p class="text-sm font-bold text-slate-900">
              Check Deadlines
            </p>

            <p class="text-xs text-slate-500">
              View urgent deadlines
            </p>
          </div>

        </button>

      </div>

    </div>


    <!-- ================================================= -->
    <!-- STATION UPDATES -->
    <!-- ================================================= -->
    <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex items-center justify-between border-b border-slate-200 pb-5">

        <div>
          <h3 class="text-xl font-bold text-slate-900">
            Station Updates
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            Recent station information
          </p>
        </div>

        <span class="h-3 w-3 rounded-full bg-green-500"></span>

      </div>


      <div class="mt-5 space-y-4">

        <div class="p-4 rounded-xl border border-yellow-200 bg-yellow-50">

          <p class="text-sm font-bold text-yellow-800">
            Morning Briefing
          </p>

          <p class="text-sm text-slate-600 mt-1">
            Station shift change and equipment check completed at 08:00 AM.
          </p>

        </div>


        <div class="p-4 rounded-xl border border-red-200 bg-red-50">

          <p class="text-sm font-bold text-[#8B1E23]">
            Important Reminder
          </p>

          <p class="text-sm text-slate-600 mt-1">
            Personnel are reminded to submit pending operational reports.
          </p>

        </div>


        <div class="p-4 rounded-xl border border-green-200 bg-green-50">

          <p class="text-sm font-bold text-green-700">
            Safety Clearance
          </p>

          <p class="text-sm text-slate-600 mt-1">
            Quarterly safety seminar training has been verified.
          </p>

        </div>

      </div>

    </div>

  </div>

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