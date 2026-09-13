<template>
  <div class="flex h-screen w-full bg-slate-100 text-slate-800 font-sans overflow-hidden">

    <!-- ========================================================= -->
    <!-- ADMIN SIDEBAR -->
    <!-- ========================================================= -->
    <aside
      class="w-72 flex-shrink-0 bg-white border-r border-slate-200 flex flex-col justify-between shadow-sm z-20"
    >

      <!-- BFP MAROON ACCENT -->
      <div class="h-2 bg-[#8B1E23]"></div>

      <div class="overflow-y-auto flex-1">

        <!-- ===================================================== -->
        <!-- LOGO -->
        <!-- ===================================================== -->
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
              Admin Portal
            </p>

            <h1 class="text-xl font-extrabold tracking-wide text-slate-900">
              FIRE<span class="text-[#8B1E23]">NOTIFY</span>
            </h1>

            <p class="text-xs text-slate-400 mt-0.5">
              BFP Operations System
            </p>
          </div>

        </div>


        <!-- ===================================================== -->
        <!-- NAVIGATION -->
        <!-- ===================================================== -->
        <div class="px-4 py-6 space-y-7">


          <!-- =================================================== -->
          <!-- MAIN NAVIGATION -->
          <!-- =================================================== -->
          <div>

            <p
              class="px-3 mb-3 text-xs font-bold uppercase tracking-wider text-slate-400"
            >
              Navigation
            </p>

            <nav class="space-y-2">

              <button
                v-for="item in menuBarItems"
                :key="item.name"
                @click="activeMenu = item.name"
                :class="[
                  'w-full flex items-center justify-between px-4 py-3.5 rounded-xl text-left transition-all duration-150',
                  activeMenu === item.name
                    ? 'bg-[#8B1E23] text-white shadow-md'
                    : 'text-slate-700 hover:bg-slate-100'
                ]"
              >

                <div class="flex items-center gap-4 min-w-0">

                  <svg
                    class="w-6 h-6 fill-current shrink-0"
                    viewBox="0 0 24 24"
                    :class="
                      activeMenu === item.name
                        ? 'text-[#F4C542]'
                        : 'text-slate-500'
                    "
                    v-html="getSvgPath(item.icon)"
                  ></svg>

                  <span class="text-base font-semibold truncate">
                    {{ item.name }}
                  </span>

                </div>


                <span
                  v-if="item.badge"
                  class="ml-2 px-2.5 py-1 rounded-full text-xs font-bold"
                  :class="
                    activeMenu === item.name
                      ? 'bg-white/20 text-white'
                      : 'bg-red-100 text-[#8B1E23]'
                  "
                >
                  {{ item.badge }}
                </span>

              </button>

            </nav>

          </div>


          <!-- =================================================== -->
          <!-- CAPSTONE CORE -->
          <!-- =================================================== -->
          <div>

            <p
              class="px-3 mb-3 text-xs font-bold uppercase tracking-wider text-slate-400"
            >
              System Management
            </p>

            <nav class="space-y-2">

              <button
                v-for="item in capstoneItems"
                :key="item.name"
                @click="activeMenu = item.name"
                :class="[
                  'w-full flex items-center gap-4 px-4 py-3.5 rounded-xl text-left transition-all duration-150',
                  activeMenu === item.name
                    ? 'bg-[#8B1E23] text-white shadow-md'
                    : 'text-slate-700 hover:bg-slate-100'
                ]"
              >

                <svg
                  class="w-6 h-6 fill-current shrink-0"
                  viewBox="0 0 24 24"
                  :class="
                    activeMenu === item.name
                      ? 'text-[#F4C542]'
                      : 'text-slate-500'
                  "
                  v-html="getSvgPath(item.icon)"
                ></svg>

                <span class="text-base font-semibold truncate">
                  {{ item.name }}
                </span>

              </button>

            </nav>

          </div>

        </div>

      </div>


      <!-- ===================================================== -->
      <!-- ADMIN PROFILE -->
      <!-- ===================================================== -->
      <div class="p-4 border-t border-slate-200 bg-slate-50">

        <div
          class="flex items-center gap-3 p-3 bg-white border border-slate-200 rounded-xl"
        >

          <div
            class="h-12 w-12 rounded-full bg-[#8B1E23] flex items-center justify-center text-white font-bold text-sm shrink-0"
          >
            {{ currentUser?.rank || 'ADMIN' }}
          </div>

          <div class="overflow-hidden">

            <p class="text-sm font-bold text-slate-900 truncate">
              {{ currentUser?.name || 'Juan Dela Cruz' }}
            </p>

            <p class="text-xs text-slate-500 truncate">
              {{ currentUser?.role || 'System Administrator' }}
            </p>

          </div>

        </div>


        <!-- SIGN OUT -->
        <button
          @click="showLogoutConfirm = true"
          class="w-full mt-3 flex items-center gap-3 px-4 py-3 rounded-xl text-base font-semibold text-slate-600 hover:bg-red-50 hover:text-[#8B1E23] transition"
        >

          <svg
            class="w-5 h-5 fill-current"
            viewBox="0 0 24 24"
          >
            <path
              d="M17 7l-1.41 1.41L18.17 11H8v2h10.17l-2.58 2.58L17 17l5-5zM4 5h8V3H4c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h8v-2H4V5z"
            />
          </svg>

          <span>Sign Out</span>

        </button>

      </div>

    </aside>


    <!-- ========================================================= -->
    <!-- MAIN CONTENT -->
    <!-- ========================================================= -->
    <div class="flex-1 flex flex-col overflow-y-auto">


      <!-- ======================================================= -->
      <!-- TOP NAVBAR -->
      <!-- ======================================================= -->
      <header
        class="bg-white border-b border-slate-200 px-8 py-5 flex items-center justify-between sticky top-0 z-30 shadow-sm"
      >

        <div class="flex items-center gap-4">

          <div
            class="h-11 w-11 rounded-xl bg-red-50 flex items-center justify-center"
          >

            <svg
              class="w-6 h-6 fill-current text-[#8B1E23]"
              viewBox="0 0 24 24"
              v-html="getSvgPath(getActiveIcon())"
            ></svg>

          </div>

          <div>

            <p class="text-sm font-medium text-slate-500">
              FIRENOTIFY ADMIN
            </p>

            <h1 class="text-2xl font-bold text-slate-900">
              {{ activeMenu }}
            </h1>

          </div>

        </div>


        <div class="flex items-center gap-4">


          <!-- SYSTEM STATUS -->
          <div
            class="hidden md:flex items-center gap-2 px-4 py-2 rounded-full bg-green-50 border border-green-200"
          >

            <span class="h-3 w-3 rounded-full bg-green-500"></span>

            <span class="text-sm font-semibold text-green-700">
              System Online
            </span>

          </div>


          <!-- NOTIFICATIONS -->
          <button
            @click="activeMenu = 'Notifications'"
            class="relative h-12 w-12 flex items-center justify-center rounded-xl border border-slate-200 hover:bg-slate-100 transition"
            title="Notifications"
          >

            <svg
              class="w-6 h-6 fill-current text-slate-600"
              viewBox="0 0 24 24"
            >
              <path
                d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5S10.5 3.17 10.5 4v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z"
              />
            </svg>

            <span
              class="absolute top-2 right-2 h-3 w-3 rounded-full bg-[#8B1E23] border-2 border-white"
            ></span>

          </button>

        </div>

      </header>


     <!-- ========================================================= -->
<!-- MAIN PAGE -->
<!-- ========================================================= -->
<main class="p-6 lg:p-8 space-y-7">
  <Dashboard v-if="activeMenu === 'Dashboard'" :current-user="currentUser" />
  <ActivityManagement v-else-if="activeMenu === 'Activity Mgmt.'" :current-user="currentUser" />
  <PersonnelManagement v-else-if="activeMenu === 'Personnel Mgmt.'" :current-user="currentUser" />
  <ReportManagement v-else-if="activeMenu === 'Report Mgmt.'" :current-user="currentUser" />
  <DeadlineMonitor v-else-if="activeMenu === 'Deadline Monitor'" :current-user="currentUser" />
  <Notifications v-else-if="activeMenu === 'Notifications'" :current-user="currentUser" />
  <WeeklyMonthlyLogs v-else-if="activeMenu === 'Weekly/Monthly Logs'" :current-user="currentUser" />
  <AuditEscalations v-else-if="activeMenu === 'Audit & Escalations'" :current-user="currentUser" />
  <ComplianceHealth v-else-if="activeMenu === 'Compliance Health'" :current-user="currentUser" />
  <DocumentPipeline v-else-if="activeMenu === 'Document Pipeline'" :current-user="currentUser" />
  <PrintExportPDF v-else-if="activeMenu === 'Print & Export PDF'" :current-user="currentUser" />

  <!-- ===================================================== -->
  <!-- DASHBOARD -->
  <!-- ===================================================== -->
  <div
    v-if="false"
    class="space-y-7"
  >

    <!-- WELCOME -->
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


    <!-- ================================================= -->
    <!-- STATISTICS -->
    <!-- ================================================= -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">

      <!-- ACTIVE PERSONNEL -->
      <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm">

        <div class="flex items-center justify-between">

          <div class="h-12 w-12 rounded-xl bg-green-50 flex items-center justify-center">
            <svg
              class="w-6 h-6 fill-current text-green-600"
              viewBox="0 0 24 24"
            >
              <path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5s-3 1.34-3 3 1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5C15 14.17 10.33 13 8 13zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/>
            </svg>
          </div>

          <span class="px-3 py-1 rounded-full bg-green-50 text-green-700 text-xs font-bold">
            ACTIVE
          </span>

        </div>

        <p class="mt-5 text-4xl font-bold text-slate-900">
          48
        </p>

        <p class="mt-1 text-base text-slate-500">
          Active Personnel
        </p>

        <p class="mt-3 text-sm font-semibold text-green-600">
          All shifts covered
        </p>

      </div>


      <!-- PENDING REPORTS -->
      <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm">

        <div class="flex items-center justify-between">

          <div class="h-12 w-12 rounded-xl bg-yellow-50 flex items-center justify-center">
            <svg
              class="w-6 h-6 fill-current text-yellow-600"
              viewBox="0 0 24 24"
            >
              <path d="M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1 1.9 2 2 2h12c1.1 0 2-.9 2-2V8l-6-6zM15 9V3.5L18.5 9H15zM8 13h8v2H8v-2zm0 4h8v2H8v-2z"/>
            </svg>
          </div>

          <span class="px-3 py-1 rounded-full bg-yellow-50 text-yellow-700 text-xs font-bold">
            REVIEW
          </span>

        </div>

        <p class="mt-5 text-4xl font-bold text-slate-900">
          12
        </p>

        <p class="mt-1 text-base text-slate-500">
          Pending Reports
        </p>

        <p class="mt-3 text-sm font-semibold text-yellow-700">
          Requires review
        </p>

      </div>


      <!-- OVERDUE -->
      <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm">

        <div class="flex items-center justify-between">

          <div class="h-12 w-12 rounded-xl bg-red-50 flex items-center justify-center">
            <svg
              class="w-6 h-6 fill-current text-[#8B1E23]"
              viewBox="0 0 24 24"
            >
              <path d="M1 21h22L12 2 1 21zm12-3h-2v2h2v-2zm0-2h-2v-4h2v4z"/>
            </svg>
          </div>

          <span class="px-3 py-1 rounded-full bg-red-50 text-[#8B1E23] text-xs font-bold">
            ALERT
          </span>

        </div>

        <p class="mt-5 text-4xl font-bold text-[#8B1E23]">
          02
        </p>

        <p class="mt-1 text-base text-slate-500">
          Overdue Deadlines
        </p>

        <p class="mt-3 text-sm font-semibold text-[#8B1E23]">
          Immediate attention
        </p>

      </div>


      <!-- COMPLIANCE -->
      <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm">

        <div class="flex items-center justify-between">

          <div class="h-12 w-12 rounded-xl bg-blue-50 flex items-center justify-center">
            <svg
              class="w-6 h-6 fill-current text-blue-600"
              viewBox="0 0 24 24"
            >
              <path d="M12 2L4 5v6c0 5.55 3.84 10.74 8 12 4.16-1.26 8-6.45 8-12V5l-8-3zm-1.5 15l-3.5-3.5 1.41-1.41 2.09 2.08 5.59-5.59 1.41 1.41-7 7z"/>
            </svg>
          </div>

          <span class="px-3 py-1 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">
            MONTHLY
          </span>

        </div>

        <p class="mt-5 text-4xl font-bold text-slate-900">
          94.5%
        </p>

        <p class="mt-1 text-base text-slate-500">
          Compliance Score
        </p>

        <p class="mt-3 text-sm font-semibold text-blue-600">
          Station performance
        </p>

      </div>

    </section>


    <!-- ================================================= -->
    <!-- DASHBOARD LOWER CONTENT -->
    <!-- ================================================= -->
    <section class="grid grid-cols-1 xl:grid-cols-3 gap-6">

      <!-- RECENT ACTIVITIES -->
      <div class="xl:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">

          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Recent Operational Activities
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              Latest activities assigned to station personnel
            </p>
          </div>

          <button
            @click="activeMenu = 'Activity Mgmt.'"
            class="text-sm font-bold text-[#8B1E23] hover:underline"
          >
            View Activities →
          </button>

        </div>


        <div class="mt-5 space-y-3">

          <div class="p-4 rounded-xl border border-slate-200 hover:bg-slate-50">

            <div class="flex items-start justify-between gap-4">

              <div>
                <p class="font-bold text-slate-900">
                  Fire Safety Inspection
                </p>

                <p class="text-sm text-slate-500 mt-1">
                  Assigned to FO3 Juan Dela Cruz
                </p>

                <p class="text-sm text-slate-400 mt-1">
                  September 9, 2026 • 8:00 AM
                </p>
              </div>

              <span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">
                ONGOING
              </span>

            </div>

          </div>


          <div class="p-4 rounded-xl border border-slate-200 hover:bg-slate-50">

            <div class="flex items-start justify-between gap-4">

              <div>
                <p class="font-bold text-slate-900">
                  Community Fire Drill
                </p>

                <p class="text-sm text-slate-500 mt-1">
                  Assigned to SFO1 M. Santos
                </p>

                <p class="text-sm text-slate-400 mt-1">
                  September 10, 2026 • 1:00 PM
                </p>
              </div>

              <span class="px-3 py-1.5 rounded-full bg-yellow-50 text-yellow-700 text-xs font-bold">
                SCHEDULED
              </span>

            </div>

          </div>


          <div class="p-4 rounded-xl border border-slate-200 hover:bg-slate-50">

            <div class="flex items-start justify-between gap-4">

              <div>
                <p class="font-bold text-slate-900">
                  Station Equipment Inspection
                </p>

                <p class="text-sm text-slate-500 mt-1">
                  Assigned to FO2 R. Reyes
                </p>

                <p class="text-sm text-slate-400 mt-1">
                  September 11, 2026 • 3:00 PM
                </p>
              </div>

              <span class="px-3 py-1.5 rounded-full bg-green-50 text-green-700 text-xs font-bold">
                SCHEDULED
              </span>

            </div>

          </div>

        </div>

      </div>


      <!-- UPCOMING DEADLINES -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <h2 class="text-xl font-bold text-slate-900">
          Upcoming Deadlines
        </h2>

        <p class="text-sm text-slate-500 mt-1">
          Reports requiring attention
        </p>


        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl bg-red-50 border border-red-200">

            <div class="flex items-start gap-3">

              <span class="text-xl">
                🚨
              </span>

              <div>
                <p class="text-sm font-bold text-slate-900">
                  Fire Incident Report
                </p>

                <p class="text-xs text-[#8B1E23] mt-1">
                  Due today • 8:00 PM
                </p>

                <span class="inline-block mt-2 px-2.5 py-1 rounded-full bg-red-100 text-[#8B1E23] text-xs font-bold">
                  OVERDUE
                </span>
              </div>

            </div>

          </div>


          <div class="p-4 rounded-xl bg-yellow-50 border border-yellow-200">

            <div class="flex items-start gap-3">

              <span class="text-xl">
                ⚠️
              </span>

              <div>
                <p class="text-sm font-bold text-slate-900">
                  Weekly Accomplishment Report
                </p>

                <p class="text-xs text-yellow-700 mt-1">
                  Due tomorrow • 5:00 PM
                </p>

                <span class="inline-block mt-2 px-2.5 py-1 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">
                  UPCOMING
                </span>
              </div>

            </div>

          </div>


          <div class="p-4 rounded-xl bg-blue-50 border border-blue-200">

            <div class="flex items-start gap-3">

              <span class="text-xl">
                📋
              </span>

              <div>
                <p class="text-sm font-bold text-slate-900">
                  Monthly Compliance Report
                </p>

                <p class="text-xs text-blue-700 mt-1">
                  Due in 5 days
                </p>

                <span class="inline-block mt-2 px-2.5 py-1 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">
                  UPCOMING
                </span>
              </div>

            </div>

          </div>

        </div>

      </div>

    </section>


    <!-- RECENT SYSTEM ACTIVITY -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="border-b border-slate-200 pb-5">

        <h2 class="text-xl font-bold text-slate-900">
          Recent System Activity
        </h2>

        <p class="text-sm text-slate-500 mt-1">
          Latest actions performed in FireNotify
        </p>

      </div>


      <div class="mt-5 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">

        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
          <p class="text-sm font-semibold text-slate-900">
            ✓ Report Submitted
          </p>
          <p class="text-xs text-slate-500 mt-1">
            FO3 Juan Dela Cruz
          </p>
          <p class="text-xs text-slate-400 mt-2">
            10 minutes ago
          </p>
        </div>

        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
          <p class="text-sm font-semibold text-slate-900">
            ✓ Activity Completed
          </p>
          <p class="text-xs text-slate-500 mt-1">
            Station Equipment Check
          </p>
          <p class="text-xs text-slate-400 mt-2">
            25 minutes ago
          </p>
        </div>

        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
          <p class="text-sm font-semibold text-slate-900">
            ⚠ Deadline Reminder
          </p>
          <p class="text-xs text-slate-500 mt-1">
            Weekly Report
          </p>
          <p class="text-xs text-slate-400 mt-2">
            40 minutes ago
          </p>
        </div>

        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
          <p class="text-sm font-semibold text-slate-900">
            + New Activity
          </p>
          <p class="text-xs text-slate-500 mt-1">
            Community Fire Drill
          </p>
          <p class="text-xs text-slate-400 mt-2">
            1 hour ago
          </p>
        </div>

      </div>

    </section>


    <!-- ================================================= -->
    <!-- ADDITIONAL DASHBOARD CONTENT -->
    <!-- ================================================= -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- MISSION READINESS -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Mission Readiness
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Station preparedness summary
            </p>
          </div>

          <span class="px-3 py-1.5 rounded-full bg-green-50 text-green-700 text-xs font-bold">
            READY
          </span>
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


      <!-- PRIORITY ALERTS -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Priority Alerts
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Items requiring immediate attention
            </p>
          </div>

          <button
            @click="activeMenu = 'Notifications'"
            class="text-sm font-bold text-[#8B1E23] hover:underline"
          >
            View All
          </button>
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


    <!-- OPERATIONS TIMELINE -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex items-center justify-between border-b border-slate-200 pb-5">
        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Operations Timeline
          </h2>
          <p class="text-sm text-slate-500 mt-1">
            Key events and updates from today
          </p>
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


    <!-- REPORTS OVERVIEW -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex items-center justify-between border-b border-slate-200 pb-5">
        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Recent Reports
          </h2>
          <p class="text-sm text-slate-500 mt-1">
            Latest submissions and their current status
          </p>
        </div>

        <button
          @click="activeMenu = 'Report Mgmt.'"
          class="text-sm font-bold text-[#8B1E23] hover:underline"
        >
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


  <!-- ===================================================== -->
  <!-- ACTIVITY MANAGEMENT -->
  <!-- ===================================================== -->
  <div
    v-if="false"
    class="space-y-6"
  >

    <!-- HEADER -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

        <div>

          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">
            Operations Management
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Activity Management
          </h2>

          <p class="text-base text-slate-500 mt-1">
            Create, schedule, assign, and monitor station activities.
          </p>

        </div>

        <button
          class="px-6 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition"
        >
          + Create New Activity
        </button>

      </div>

    </section>


    <!-- ACTIVITY SUMMARY -->
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


    <!-- SEARCH AND FILTER -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">

        <input
          type="text"
          placeholder="Search activity..."
          class="h-12 px-4 rounded-xl border border-slate-300 text-base focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]"
        />

        <select
          class="h-12 px-4 rounded-xl border border-slate-300 text-base focus:outline-none focus:ring-2 focus:ring-red-200"
        >
          <option>All Activity Types</option>
          <option>Inspection</option>
          <option>Fire Drill</option>
          <option>Training</option>
          <option>Emergency Response</option>
        </select>

        <select
          class="h-12 px-4 rounded-xl border border-slate-300 text-base focus:outline-none focus:ring-2 focus:ring-red-200"
        >
          <option>All Status</option>
          <option>Scheduled</option>
          <option>Ongoing</option>
          <option>Completed</option>
          <option>Delayed</option>
        </select>

      </div>

    </section>


    <!-- ACTIVITY TABLE -->
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
                <p class="font-bold text-slate-900">
                  Fire Safety Inspection
                </p>
                <p class="text-xs text-slate-400 mt-1">
                  ACT-001
                </p>
              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                Inspection
              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                5 Personnel
              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                Sept. 9, 2026
              </td>

              <td class="py-5 pr-5">
                <span class="px-3 py-1.5 rounded-full bg-red-50 text-[#8B1E23] text-xs font-bold">
                  HIGH
                </span>
              </td>

              <td class="py-5 text-right">
                <span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">
                  ONGOING
                </span>
              </td>

            </tr>


            <tr class="hover:bg-slate-50">

              <td class="py-5 pr-5">
                <p class="font-bold text-slate-900">
                  Community Fire Drill
                </p>
                <p class="text-xs text-slate-400 mt-1">
                  ACT-002
                </p>
              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                Fire Drill
              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                8 Personnel
              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                Sept. 10, 2026
              </td>

              <td class="py-5 pr-5">
                <span class="px-3 py-1.5 rounded-full bg-yellow-50 text-yellow-700 text-xs font-bold">
                  MEDIUM
                </span>
              </td>

              <td class="py-5 text-right">
                <span class="px-3 py-1.5 rounded-full bg-yellow-50 text-yellow-700 text-xs font-bold">
                  SCHEDULED
                </span>
              </td>

            </tr>


            <tr class="hover:bg-slate-50">

              <td class="py-5 pr-5">
                <p class="font-bold text-slate-900">
                  Station Equipment Inspection
                </p>
                <p class="text-xs text-slate-400 mt-1">
                  ACT-003
                </p>
              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                Inspection
              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                4 Personnel
              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                Sept. 11, 2026
              </td>

              <td class="py-5 pr-5">
                <span class="px-3 py-1.5 rounded-full bg-green-50 text-green-700 text-xs font-bold">
                  LOW
                </span>
              </td>

              <td class="py-5 text-right">
                <span class="px-3 py-1.5 rounded-full bg-yellow-50 text-yellow-700 text-xs font-bold">
                  SCHEDULED
                </span>
              </td>

            </tr>

          </tbody>

        </table>

      </div>

    </section>


    <!-- ================================================= -->
    <!-- ACTIVITY MGMT. ADDITIONAL CONTENT -->
    <!-- ================================================= -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- PLANNED ACTIVITIES -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Planned Activities
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Upcoming schedule for the next 7 days
            </p>
          </div>

          <span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">
            06 ITEMS
          </span>
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


      <!-- WORKLOAD SUMMARY -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Workload Summary
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Personnel allocation by activity type
            </p>
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


    <!-- ACTIVITY NOTES -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex items-center justify-between border-b border-slate-200 pb-5">
        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Activity Notes
          </h2>
          <p class="text-sm text-slate-500 mt-1">
            Additional reminders for team coordination
          </p>
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


  <!-- ===================================================== -->
  <!-- PERSONNEL MANAGEMENT -->
  <!-- ===================================================== -->
  <div
    v-if="false"
    class="space-y-6"
  >

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

        <div>

          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">
            Personnel Management
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Station Personnel
          </h2>

          <p class="text-base text-slate-500 mt-1">
            Manage personnel records, ranks, assignments, and duty status.
          </p>

        </div>

        <button
          class="px-6 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition"
        >
          + Add Personnel
        </button>

      </div>

    </section>


    <!-- PERSONNEL STATISTICS -->
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


    <!-- SEARCH -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

      <div class="flex flex-col md:flex-row gap-4">

        <input
          type="text"
          placeholder="Search name, rank, or position..."
          class="flex-1 h-12 px-4 rounded-xl border border-slate-300 text-base focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]"
        />

        <select
          class="h-12 px-4 rounded-xl border border-slate-300 text-base"
        >
          <option>All Duty Status</option>
          <option>On Duty</option>
          <option>Off Duty</option>
          <option>On Leave</option>
        </select>

      </div>

    </section>


    <!-- PERSONNEL TABLE -->
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

                  <div class="h-11 w-11 rounded-full bg-[#8B1E23] text-white flex items-center justify-center text-xs font-bold">
                    FO3
                  </div>

                  <div>
                    <p class="font-bold text-slate-900">
                      Juan Dela Cruz
                    </p>
                    <p class="text-xs text-slate-500">
                      Personnel ID: BFP-001
                    </p>
                  </div>

                </div>
              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                FO3
              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                Fire Officer
              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                Morning
              </td>

              <td class="py-5 text-right">
                <span class="px-3 py-1.5 rounded-full bg-green-50 text-green-700 text-xs font-bold">
                  ON DUTY
                </span>
              </td>

            </tr>


            <tr class="hover:bg-slate-50">

              <td class="py-5 pr-5">
                <div class="flex items-center gap-3">

                  <div class="h-11 w-11 rounded-full bg-[#8B1E23] text-white flex items-center justify-center text-xs font-bold">
                    SFO1
                  </div>

                  <div>
                    <p class="font-bold text-slate-900">
                      Maria Santos
                    </p>
                    <p class="text-xs text-slate-500">
                      Personnel ID: BFP-002
                    </p>
                  </div>

                </div>
              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                SFO1
              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                Senior Fire Officer
              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                Afternoon
              </td>

              <td class="py-5 text-right">
                <span class="px-3 py-1.5 rounded-full bg-green-50 text-green-700 text-xs font-bold">
                  ON DUTY
                </span>
              </td>

            </tr>


            <tr class="hover:bg-slate-50">

              <td class="py-5 pr-5">
                <div class="flex items-center gap-3">

                  <div class="h-11 w-11 rounded-full bg-[#8B1E23] text-white flex items-center justify-center text-xs font-bold">
                    FO2
                  </div>

                  <div>
                    <p class="font-bold text-slate-900">
                      Roberto Reyes
                    </p>
                    <p class="text-xs text-slate-500">
                      Personnel ID: BFP-003
                    </p>
                  </div>

                </div>
              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                FO2
              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                Fire Officer
              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                Night
              </td>

              <td class="py-5 text-right">
                <span class="px-3 py-1.5 rounded-full bg-yellow-50 text-yellow-700 text-xs font-bold">
                  ON LEAVE
                </span>
              </td>

            </tr>

          </tbody>

        </table>

      </div>

    </section>


    <!-- ================================================= -->
    <!-- PERSONNEL MGMT. ADDITIONAL CONTENT -->
    <!-- ================================================= -->

    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- RECENT ASSIGNMENTS -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Recent Assignments
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Latest assignments and role changes
            </p>
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


      <!-- TEAM AVAILABILITY -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Team Availability
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Current staffing by shift
            </p>
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


    <!-- PERSONNEL NOTES -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex items-center justify-between border-b border-slate-200 pb-5">
        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Personnel Notes
          </h2>
          <p class="text-sm text-slate-500 mt-1">
            Admin reminders and coordination updates
          </p>
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


  <!-- ===================================================== -->
  <!-- REPORT MANAGEMENT -->
  <!-- ===================================================== -->
  <div
    v-if="false"
    class="space-y-6"
  >

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

        <div>

          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">
            Records Management
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Report Management
          </h2>

          <p class="text-base text-slate-500 mt-1">
            Review, monitor, approve, and manage submitted operational reports.
          </p>

        </div>

        <button
          class="px-6 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition"
        >
          + Create Report
        </button>

      </div>

    </section>


    <!-- REPORT SUMMARY -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-slate-900">50</p>
        <p class="text-sm text-slate-500 mt-1">Total Reports</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">12</p>
        <p class="text-sm text-slate-500 mt-1">For Review</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">34</p>
        <p class="text-sm text-slate-500 mt-1">Approved</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">04</p>
        <p class="text-sm text-slate-500 mt-1">Rejected</p>
      </div>

    </section>


    <!-- REPORT FILTERS -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">

        <input
          type="text"
          placeholder="Search report..."
          class="h-12 px-4 rounded-xl border border-slate-300 text-base"
        />

        <select
          class="h-12 px-4 rounded-xl border border-slate-300 text-base"
        >
          <option>All Report Types</option>
          <option>Incident Report</option>
          <option>Inspection Report</option>
          <option>Accomplishment Report</option>
          <option>Activity Report</option>
        </select>

        <select
          class="h-12 px-4 rounded-xl border border-slate-300 text-base"
        >
          <option>All Status</option>
          <option>For Review</option>
          <option>Approved</option>
          <option>Rejected</option>
          <option>Returned</option>
        </select>

      </div>

    </section>


    <!-- REPORT LIST -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="space-y-4">

        <!-- REPORT 1 -->
        <div class="p-5 rounded-xl border border-slate-200 hover:bg-slate-50">

          <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

            <div>

              <div class="flex items-center gap-3 flex-wrap">

                <h3 class="text-lg font-bold text-slate-900">
                  Fire Safety Inspection Report
                </h3>

                <span class="px-3 py-1 rounded-full bg-yellow-50 text-yellow-700 text-xs font-bold">
                  FOR REVIEW
                </span>

              </div>

              <p class="text-sm text-slate-500 mt-2">
                Submitted by FO3 Juan Dela Cruz
              </p>

              <p class="text-sm text-slate-400 mt-1">
                Submitted September 9, 2026 • Report ID: REP-001
              </p>

            </div>

            <div class="flex gap-2">

              <button
                class="px-4 py-2.5 rounded-lg border border-slate-300 text-sm font-bold hover:bg-slate-100"
              >
                View
              </button>

              <button
                class="px-4 py-2.5 rounded-lg bg-green-600 text-white text-sm font-bold hover:bg-green-700"
              >
                Approve
              </button>

            </div>

          </div>

        </div>


        <!-- REPORT 2 -->
        <div class="p-5 rounded-xl border border-slate-200 hover:bg-slate-50">

          <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

            <div>

              <div class="flex items-center gap-3 flex-wrap">

                <h3 class="text-lg font-bold text-slate-900">
                  Weekly Accomplishment Report
                </h3>

                <span class="px-3 py-1 rounded-full bg-green-50 text-green-700 text-xs font-bold">
                  APPROVED
                </span>

              </div>

              <p class="text-sm text-slate-500 mt-2">
                Submitted by SFO1 Maria Santos
              </p>

              <p class="text-sm text-slate-400 mt-1">
                Approved September 8, 2026 • Report ID: REP-002
              </p>

            </div>

            <button
              class="px-4 py-2.5 rounded-lg border border-slate-300 text-sm font-bold hover:bg-slate-100"
            >
              View Report
            </button>

          </div>

        </div>


        <!-- REPORT 3 -->
        <div class="p-5 rounded-xl border border-red-200 bg-red-50">

          <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

            <div>

              <div class="flex items-center gap-3 flex-wrap">

                <h3 class="text-lg font-bold text-slate-900">
                  Fire Incident Report
                </h3>

                <span class="px-3 py-1 rounded-full bg-red-100 text-[#8B1E23] text-xs font-bold">
                  OVERDUE
                </span>

              </div>

              <p class="text-sm text-slate-600 mt-2">
                Assigned to FO2 Roberto Reyes
              </p>

              <p class="text-sm text-[#8B1E23] mt-1">
                Deadline: September 9, 2026 • 8:00 PM
              </p>

            </div>

            <button
              class="px-4 py-2.5 rounded-lg bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]"
            >
              Send Reminder
            </button>

          </div>

        </div>

      </div>

    </section>


    <!-- ================================================= -->
    <!-- REPORT MGMT. ADDITIONAL CONTENT -->
    <!-- ================================================= -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- REPORT ANALYTICS -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Report Analytics
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Submission efficiency this month
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>On-Time Submission</span>
              <span>86%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[86%] rounded-full bg-green-500"></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Approval Rate</span>
              <span>68%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[68%] rounded-full bg-blue-500"></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Corrections Needed</span>
              <span>24%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[24%] rounded-full bg-yellow-500"></div>
            </div>
          </div>

        </div>

      </div>


      <!-- RECENTLY UPLOADED FILES -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Recently Uploaded Files
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Latest attachments and documents
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div class="flex items-center justify-between p-3 rounded-xl border border-slate-200 bg-slate-50">
            <div>
              <p class="text-sm font-bold text-slate-900">InspectionChecklist_Sept9.pdf</p>
              <p class="text-xs text-slate-500 mt-1">Uploaded by FO3 Juan Dela Cruz</p>
            </div>
            <span class="text-xs font-bold text-slate-500">PDF</span>
          </div>

          <div class="flex items-center justify-between p-3 rounded-xl border border-slate-200 bg-slate-50">
            <div>
              <p class="text-sm font-bold text-slate-900">BarangayDrillSummary.xlsx</p>
              <p class="text-xs text-slate-500 mt-1">Uploaded by FO2 Roberto Reyes</p>
            </div>
            <span class="text-xs font-bold text-slate-500">XLSX</span>
          </div>

          <div class="flex items-center justify-between p-3 rounded-xl border border-slate-200 bg-slate-50">
            <div>
              <p class="text-sm font-bold text-slate-900">IncidentPhotos_Set2.jpg</p>
              <p class="text-xs text-slate-500 mt-1">Uploaded by SFO1 Maria Santos</p>
            </div>
            <span class="text-xs font-bold text-slate-500">IMG</span>
          </div>

        </div>

      </div>

    </section>


    <!-- REPORT NOTES -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex items-center justify-between border-b border-slate-200 pb-5">
        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Review Notes
          </h2>
          <p class="text-sm text-slate-500 mt-1">
            Notes for report coordinators and approvers
          </p>
        </div>
      </div>

      <div class="mt-5 space-y-4">

        <div class="p-4 rounded-xl border border-red-200 bg-red-50">
          <p class="text-sm font-bold text-slate-900">Priority Reminder</p>
          <p class="text-sm text-slate-600 mt-1">Fire incident reports submitted after deadline require immediate supervisor review and follow-up.</p>
        </div>

        <div class="p-4 rounded-xl border border-amber-200 bg-amber-50">
          <p class="text-sm font-bold text-slate-900">Correction Needed</p>
          <p class="text-sm text-slate-600 mt-1">A few inspection reports are missing photographs; request resubmission before approval.</p>
        </div>

        <div class="p-4 rounded-xl border border-blue-200 bg-blue-50">
          <p class="text-sm font-bold text-slate-900">Documentation</p>
          <p class="text-sm text-slate-600 mt-1">Ensure all attachments are properly named and linked to the corresponding report ID.</p>
        </div>

      </div>

    </section>

  </div>


  <!-- ===================================================== -->
  <!-- DEADLINE MONITOR -->
  <!-- ===================================================== -->
  <div
    v-if="false"
    class="space-y-6"
  >

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">
        Compliance Monitoring
      </p>

      <h2 class="text-2xl font-bold text-slate-900 mt-1">
        Deadline Monitor
      </h2>

      <p class="text-base text-slate-500 mt-1">
        Track upcoming, due, and overdue report deadlines.
      </p>

    </section>


    <!-- DEADLINE SUMMARY -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">02</p>
        <p class="text-sm text-slate-500 mt-1">Overdue</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">03</p>
        <p class="text-sm text-slate-500 mt-1">Due Today</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-blue-600">07</p>
        <p class="text-sm text-slate-500 mt-1">This Week</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">24</p>
        <p class="text-sm text-slate-500 mt-1">Completed</p>
      </div>

    </section>


    <!-- OVERDUE -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex items-center gap-3">

        <div class="h-11 w-11 rounded-xl bg-red-50 flex items-center justify-center">
          🚨
        </div>

        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Overdue Deadlines
          </h2>

          <p class="text-sm text-slate-500">
            Immediate administrative attention required
          </p>
        </div>

      </div>


      <div class="mt-5 space-y-3">

        <div class="p-5 rounded-xl bg-red-50 border border-red-200">

          <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

            <div>

              <p class="font-bold text-slate-900">
                After-Operation Fire Incident Report
              </p>

              <p class="text-sm text-[#8B1E23] mt-1">
                Assigned to FO3 Juan Dela Cruz
              </p>

              <p class="text-sm text-[#8B1E23] mt-1">
                Overdue by 2 hours
              </p>

            </div>

            <button
              class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold"
            >
              Send Escalation
            </button>

          </div>

        </div>


        <div class="p-5 rounded-xl bg-red-50 border border-red-200">

          <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

            <div>

              <p class="font-bold text-slate-900">
                Station Activity Report
              </p>

              <p class="text-sm text-[#8B1E23] mt-1">
                Assigned to FO2 Roberto Reyes
              </p>

              <p class="text-sm text-[#8B1E23] mt-1">
                Overdue by 1 hour
              </p>

            </div>

            <button
              class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold"
            >
              Send Escalation
            </button>

          </div>

        </div>

      </div>

    </section>


    <!-- UPCOMING -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <h2 class="text-xl font-bold text-slate-900">
        Upcoming Deadlines
      </h2>

      <p class="text-sm text-slate-500 mt-1">
        Reports that are approaching their submission deadline
      </p>


      <div class="mt-5 space-y-3">

        <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4 p-5 rounded-xl border border-yellow-200 bg-yellow-50">

          <div>

            <p class="font-bold text-slate-900">
              Weekly Accomplishment Report
            </p>

            <p class="text-sm text-slate-500 mt-1">
              Assigned to SFO1 Maria Santos
            </p>

          </div>

          <span class="px-4 py-2 rounded-full bg-yellow-100 text-yellow-700 text-sm font-bold">
            Due Tomorrow • 5:00 PM
          </span>

        </div>


        <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4 p-5 rounded-xl border border-blue-200 bg-blue-50">

          <div>

            <p class="font-bold text-slate-900">
              Monthly Compliance Report
            </p>

            <p class="text-sm text-slate-500 mt-1">
              Station 1 Administration
            </p>

          </div>

          <span class="px-4 py-2 rounded-full bg-blue-100 text-blue-700 text-sm font-bold">
            Due in 5 Days
          </span>

        </div>

      </div>

    </section>


    <!-- ================================================= -->
    <!-- DEADLINE MONITOR ADDITIONAL CONTENT -->
    <!-- ================================================= -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- DEADLINE TRENDS -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Deadline Trends
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Weekly performance summary
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>On-Time Rate</span>
              <span>79%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[79%] rounded-full bg-emerald-500"></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Escalations Sent</span>
              <span>11</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[58%] rounded-full bg-red-500"></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Resolved Before Deadline</span>
              <span>67%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[67%] rounded-full bg-blue-500"></div>
            </div>
          </div>

        </div>

      </div>


      <!-- ESCALATION QUEUE -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Escalation Queue
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Reports needing action from higher units
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-red-200 bg-red-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">After-Operation Fire Incident Report</p>
                <p class="text-xs text-slate-500 mt-1">Escalated to Station Operations Chief</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-red-100 text-[#8B1E23] text-xs font-bold">High</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-yellow-200 bg-yellow-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">Monthly Compliance Report</p>
                <p class="text-xs text-slate-500 mt-1">Pending review from Admin Office</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">Medium</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-blue-200 bg-blue-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">Barangay Fire Drill Summary</p>
                <p class="text-xs text-slate-500 mt-1">Awaiting validation of attendance logs</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">Info</span>
            </div>
          </div>

        </div>

      </div>

    </section>


    <!-- DEADLINE NOTES -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex items-center justify-between border-b border-slate-200 pb-5">
        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Compliance Notes
          </h2>
          <p class="text-sm text-slate-500 mt-1">
            Operational reminders and monitoring details
          </p>
        </div>
      </div>

      <div class="mt-5 space-y-4">

        <div class="p-4 rounded-xl border border-emerald-200 bg-emerald-50">
          <p class="text-sm font-bold text-slate-900">Reminder</p>
          <p class="text-sm text-slate-600 mt-1">Late submissions should be resequenced immediately after review to avoid backlogs in the next cycle.</p>
        </div>

        <div class="p-4 rounded-xl border border-orange-200 bg-orange-50">
          <p class="text-sm font-bold text-slate-900">Attention</p>
          <p class="text-sm text-slate-600 mt-1">2 overdue reports require an escalation note to the operations head before the end of the day.</p>
        </div>

        <div class="p-4 rounded-xl border border-indigo-200 bg-indigo-50">
          <p class="text-sm font-bold text-slate-900">Follow-Up</p>
          <p class="text-sm text-slate-600 mt-1">Monitor the final status of all approved reports and ensure attachments are saved in the archive.</p>
        </div>

      </div>

    </section>

  </div>


  <!-- ===================================================== -->
  <!-- NOTIFICATIONS -->
  <!-- ===================================================== -->
  <div
    v-if="false"
    class="space-y-6"
  >

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

        <div>

          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">
            Communication Center
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Notifications
          </h2>

          <p class="text-base text-slate-500 mt-1">
            View system announcements, activity alerts, and deadline reminders.
          </p>

        </div>

        <button
          class="px-5 py-3 rounded-xl border border-slate-300 bg-white text-slate-700 font-bold hover:bg-slate-100"
        >
          Mark All as Read
        </button>

      </div>

    </section>


    <!-- NOTIFICATION SUMMARY -->
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


    <!-- NOTIFICATION LIST -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="space-y-3">

        <!-- NOTIFICATION 1 -->
        <div class="p-5 rounded-xl border border-red-200 bg-red-50">

          <div class="flex items-start gap-4">

            <div class="h-12 w-12 rounded-full bg-red-100 flex items-center justify-center shrink-0">
              🚨
            </div>

            <div class="flex-1">

              <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-2">

                <h3 class="font-bold text-slate-900">
                  Overdue Report Deadline
                </h3>

                <span class="px-3 py-1 rounded-full bg-red-100 text-[#8B1E23] text-xs font-bold">
                  UNREAD
                </span>

              </div>

              <p class="text-sm text-slate-600 mt-2">
                The After-Operation Fire Incident Report has passed its
                submission deadline.
              </p>

              <p class="text-xs text-slate-400 mt-2">
                10 minutes ago
              </p>

            </div>

          </div>

        </div>


        <!-- NOTIFICATION 2 -->
        <div class="p-5 rounded-xl border border-yellow-200 bg-yellow-50">

          <div class="flex items-start gap-4">

            <div class="h-12 w-12 rounded-full bg-yellow-100 flex items-center justify-center shrink-0">
              ⚠️
            </div>

            <div class="flex-1">

              <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-2">

                <h3 class="font-bold text-slate-900">
                  Upcoming Report Deadline
                </h3>

                <span class="px-3 py-1 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">
                  UNREAD
                </span>

              </div>

              <p class="text-sm text-slate-600 mt-2">
                Weekly Accomplishment Report is due tomorrow at 5:00 PM.
              </p>

              <p class="text-xs text-slate-400 mt-2">
                30 minutes ago
              </p>

            </div>

          </div>

        </div>


        <!-- NOTIFICATION 3 -->
        <div class="p-5 rounded-xl border border-blue-200 bg-blue-50">

          <div class="flex items-start gap-4">

            <div class="h-12 w-12 rounded-full bg-blue-100 flex items-center justify-center shrink-0">
              📋
            </div>

            <div class="flex-1">

              <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-2">

                <h3 class="font-bold text-slate-900">
                  New Activity Assigned
                </h3>

                <span class="px-3 py-1 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">
                  UNREAD
                </span>

              </div>

              <p class="text-sm text-slate-600 mt-2">
                Community Fire Drill has been scheduled for September 10,
                2026.
              </p>

              <p class="text-xs text-slate-400 mt-2">
                1 hour ago
              </p>

            </div>

          </div>

        </div>


        <!-- NOTIFICATION 4 -->
        <div class="p-5 rounded-xl border border-slate-200 bg-slate-50">

          <div class="flex items-start gap-4">

            <div class="h-12 w-12 rounded-full bg-green-100 flex items-center justify-center shrink-0">
              ✓
            </div>

            <div class="flex-1">

              <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-2">

                <h3 class="font-bold text-slate-900">
                  Report Approved
                </h3>

                <span class="px-3 py-1 rounded-full bg-green-100 text-green-700 text-xs font-bold">
                  READ
                </span>

              </div>

              <p class="text-sm text-slate-600 mt-2">
                Weekly Accomplishment Report submitted by SFO1 Maria Santos
                has been approved.
              </p>

              <p class="text-xs text-slate-400 mt-2">
                2 hours ago
              </p>

            </div>

          </div>

        </div>

      </div>

    </section>


    <!-- ================================================= -->
    <!-- NOTIFICATION ADDITIONAL CONTENT -->
    <!-- ================================================= -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- CHANNEL SUMMARY -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Channel Summary
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Message volume by source
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">System Alerts</p>
                <p class="text-xs text-slate-500 mt-1">12 messages today</p>
              </div>
              <span class="text-sm font-bold text-[#8B1E23]">42%</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Personnel Updates</p>
                <p class="text-xs text-slate-500 mt-1">9 messages today</p>
              </div>
              <span class="text-sm font-bold text-blue-600">31%</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Reports & Compliance</p>
                <p class="text-xs text-slate-500 mt-1">8 messages today</p>
              </div>
              <span class="text-sm font-bold text-green-600">27%</span>
            </div>
          </div>

        </div>

      </div>


      <!-- MESSAGE FILTERS -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Message Filters
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Quick sorting for incoming updates
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <button class="w-full text-left px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 hover:bg-slate-100 text-sm font-semibold text-slate-700">
            All Notifications
          </button>

          <button class="w-full text-left px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 hover:bg-slate-100 text-sm font-semibold text-slate-700">
            Deadline Alerts
          </button>

          <button class="w-full text-left px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 hover:bg-slate-100 text-sm font-semibold text-slate-700">
            Personnel Updates
          </button>

          <button class="w-full text-left px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 hover:bg-slate-100 text-sm font-semibold text-slate-700">
            System Announcements
          </button>

        </div>

      </div>

    </section>


    <!-- ANNOUNCEMENTS -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex items-center justify-between border-b border-slate-200 pb-5">
        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Announcements
          </h2>
          <p class="text-sm text-slate-500 mt-1">
            Administrative updates for all BFP units
          </p>
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


  <!-- ===================================================== -->
  <!-- WEEKLY / MONTHLY LOGS -->
  <!-- ===================================================== -->
  <div
    v-if="false"
    class="space-y-6"
  >

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

        <div>

          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">
            Record Archives
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Weekly / Monthly Logs
          </h2>

          <p class="text-base text-slate-500 mt-1">
            Review station summaries, recurring reports, and compliance records.
          </p>

        </div>

        <button
          class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition"
        >
          + Add Log Entry
        </button>

      </div>

    </section>


    <!-- LOG SUMMARY -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">12</p>
        <p class="text-sm text-slate-500 mt-1">Weekly Logs</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-blue-600">08</p>
        <p class="text-sm text-slate-500 mt-1">Monthly Reports</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">06</p>
        <p class="text-sm text-slate-500 mt-1">Submitted</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">02</p>
        <p class="text-sm text-slate-500 mt-1">Pending Review</p>
      </div>

    </section>


    <!-- WEEKLY / MONTHLY HIGHLIGHTS -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Weekly Highlights
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              This week’s important operational notes
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <p class="text-sm font-bold text-slate-900">Fire Safety Orientation</p>
            <p class="text-sm text-slate-600 mt-1">Covered 5 barangays with 98% attendance from local responders and volunteers.</p>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <p class="text-sm font-bold text-slate-900">Equipment Readiness</p>
            <p class="text-sm text-slate-600 mt-1">All assigned rescue tools were checked, cleaned, and tagged for dispatch readiness.</p>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <p class="text-sm font-bold text-slate-900">Dispatch Coordination</p>
            <p class="text-sm text-slate-600 mt-1">Dispatch teams coordinated with local emergency units for three scheduled activities.</p>
          </div>

        </div>

      </div>


      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Monthly Highlights
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Station compliance and performance summary
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-emerald-200 bg-emerald-50">
            <p class="text-sm font-bold text-slate-900">Compliance Rate</p>
            <p class="text-sm text-slate-600 mt-1">Monthly compliance increased to 94.5%, surpassing the previous cycle by 4.2%.</p>
          </div>

          <div class="p-4 rounded-xl border border-blue-200 bg-blue-50">
            <p class="text-sm font-bold text-slate-900">Report Turnaround</p>
            <p class="text-sm text-slate-600 mt-1">Average report submission turnaround improved to 2.3 days across all stations.</p>
          </div>

          <div class="p-4 rounded-xl border border-amber-200 bg-amber-50">
            <p class="text-sm font-bold text-slate-900">Staff Performance</p>
            <p class="text-sm text-slate-600 mt-1">Operations staff maintained steady productivity while balancing drills, inspections, and training.</p>
          </div>

        </div>

      </div>

    </section>


    <!-- LOG ENTRY TABLE -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex items-center justify-between border-b border-slate-200 pb-5">
        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Recent Weekly / Monthly Entries
          </h2>
          <p class="text-sm text-slate-500 mt-1">
            Latest archived logs submitted by personnel
          </p>
        </div>
      </div>

      <div class="mt-5 overflow-x-auto">
        <table class="min-w-full border-separate border-spacing-y-3">
          <thead>
            <tr class="text-left text-xs font-bold uppercase tracking-wide text-slate-500">
              <th class="pb-2 pr-4">Activity</th>
              <th class="pb-2 pr-4">Personnel</th>
              <th class="pb-2 pr-4">Deadline</th>
              <th class="pb-2">Status</th>
            </tr>
          </thead>

          <tbody>
            <tr
              v-for="item in logs"
              :key="item.activity"
              class="bg-slate-50 rounded-xl"
            >
              <td class="py-4 pr-4 font-semibold text-slate-900 rounded-l-xl">
                {{ item.activity }}
              </td>
              <td class="py-4 pr-4 text-slate-600">
                {{ item.personnel }}
              </td>
              <td class="py-4 pr-4 text-slate-600">
                {{ item.deadline }}
              </td>
              <td class="py-4 pr-4">
                <span
                  class="px-3 py-1 rounded-full text-xs font-bold"
                  :class="item.status === 'Completed'
                    ? 'bg-green-100 text-green-700'
                    : 'bg-yellow-100 text-yellow-700'"
                >
                  {{ item.status }}
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

    </section>

  </div>


  <!-- ===================================================== -->
  <!-- AUDIT & ESCALATIONS -->
  <!-- ===================================================== -->
  <div
    v-if="false"
    class="space-y-6"
  >

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

        <div>

          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">
            Governance Overview
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Audit & Escalations
          </h2>

          <p class="text-base text-slate-500 mt-1">
            Review compliance checks, investigate findings, and monitor escalated cases.
          </p>

        </div>

        <button
          class="px-5 py-3 rounded-xl border border-slate-300 bg-white text-slate-700 font-bold hover:bg-slate-100 transition"
        >
          Export Audit Report
        </button>

      </div>

    </section>


    <!-- AUDIT SUMMARY -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">18</p>
        <p class="text-sm text-slate-500 mt-1">Open Findings</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">06</p>
        <p class="text-sm text-slate-500 mt-1">Escalated</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">92%</p>
        <p class="text-sm text-slate-500 mt-1">Resolution Rate</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-blue-600">04</p>
        <p class="text-sm text-slate-500 mt-1">Pending Reviews</p>
      </div>

    </section>


    <!-- AUDIT OVERVIEW -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- ESCALATION QUEUE -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Escalation Queue
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Cases requiring higher-level attention
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-red-200 bg-red-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">Late Fire Incident Report</p>
                <p class="text-xs text-slate-500 mt-1">Assigned to FO3 Juan Dela Cruz • 2 hours overdue</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-red-100 text-[#8B1E23] text-xs font-bold">High</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-yellow-200 bg-yellow-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">Monthly Compliance Report</p>
                <p class="text-xs text-slate-500 mt-1">Pending review from Admin Office • 3 documents incomplete</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">Medium</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-blue-200 bg-blue-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">Barangay Drill Attendance Review</p>
                <p class="text-xs text-slate-500 mt-1">Awaiting validation of attendance logs and signatures</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">Low</span>
            </div>
          </div>

        </div>

      </div>


      <!-- AUDIT FINDINGS -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Audit Findings
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Recent compliance and operational observations
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-start gap-4">
              <div>
                <p class="text-sm font-bold text-slate-900">Documentation Gap</p>
                <p class="text-xs text-slate-500 mt-1">Two submitted reports were missing attachment references.</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">Review</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-start gap-4">
              <div>
                <p class="text-sm font-bold text-slate-900">Equipment Check Delay</p>
                <p class="text-xs text-slate-500 mt-1">One station missed its scheduled maintenance verification window.</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">Action</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-start gap-4">
              <div>
                <p class="text-sm font-bold text-slate-900">Training Completion</p>
                <p class="text-xs text-slate-500 mt-1">All new personnel completed required orientation modules.</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-green-100 text-green-700 text-xs font-bold">Resolved</span>
            </div>
          </div>

        </div>

      </div>

    </section>


    <!-- AUDIT TRACKER -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- PERFORMANCE METRICS -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Performance Metrics
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Current audit score trends
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Reporting Compliance</span>
              <span>96%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[96%] rounded-full bg-emerald-500"></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>On-Time Submission</span>
              <span>88%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[88%] rounded-full bg-blue-500"></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Attachment Completeness</span>
              <span>81%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[81%] rounded-full bg-yellow-500"></div>
            </div>
          </div>

        </div>

      </div>


      <!-- ACTION NOTES -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Action Notes
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Follow-up reminders for administrators
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-emerald-200 bg-emerald-50">
            <p class="text-sm font-bold text-slate-900">Reminder</p>
            <p class="text-sm text-slate-600 mt-1">Ensure all stations attach supporting evidence before submitting monthly compliance reports.</p>
          </div>

          <div class="p-4 rounded-xl border border-orange-200 bg-orange-50">
            <p class="text-sm font-bold text-slate-900">Attention</p>
            <p class="text-sm text-slate-600 mt-1">Two delayed incident reports need closure notes and supervisor approval before end of day.</p>
          </div>

          <div class="p-4 rounded-xl border border-indigo-200 bg-indigo-50">
            <p class="text-sm font-bold text-slate-900">Follow-Up</p>
            <p class="text-sm text-slate-600 mt-1">Schedule a review meeting with Station Chiefs to address recurring documentation inconsistencies.</p>
          </div>

        </div>

      </div>

    </section>

  </div>


  <!-- ===================================================== -->
  <!-- COMPLIANCE HEALTH -->
  <!-- ===================================================== -->
  <div
    v-if="false"
    class="space-y-6"
  >

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

        <div>

          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">
            Operational Health
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Compliance Health
          </h2>

          <p class="text-base text-slate-500 mt-1">
            Monitor station compliance, review health indicators, and track corrective actions.
          </p>

        </div>

        <button
          class="px-5 py-3 rounded-xl border border-slate-300 bg-white text-slate-700 font-bold hover:bg-slate-100 transition"
        >
          View Full Report
        </button>

      </div>

    </section>


    <!-- HEALTH SUMMARY -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">94.5%</p>
        <p class="text-sm text-slate-500 mt-1">Overall Health</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">07</p>
        <p class="text-sm text-slate-500 mt-1">Good Standing</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">02</p>
        <p class="text-sm text-slate-500 mt-1">Needs Attention</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-blue-600">89%</p>
        <p class="text-sm text-slate-500 mt-1">Deadline Adherence</p>
      </div>

    </section>


    <!-- COMPLIANCE OVERVIEW -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- STATION COMPLIANCE SNAPSHOT -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Station Compliance Snapshot
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Performance of each station and unit
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Station 1</p>
                <p class="text-xs text-slate-500 mt-1">Submission quality and adherence</p>
              </div>
              <span class="text-sm font-bold text-green-600">95%</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Station 2</p>
                <p class="text-xs text-slate-500 mt-1">Equipment checks and reporting</p>
              </div>
              <span class="text-sm font-bold text-yellow-600">82%</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Station 3</p>
                <p class="text-xs text-slate-500 mt-1">Documentation completeness</p>
              </div>
              <span class="text-sm font-bold text-green-600">91%</span>
            </div>
          </div>

        </div>

      </div>


      <!-- STANDARDS CHECK STATUS -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Standards Check Status
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Current compliance checklist progress
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Daily Logs</span>
              <span>98%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[98%] rounded-full bg-emerald-500"></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Equipment Verification</span>
              <span>87%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[87%] rounded-full bg-blue-500"></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Attachment Completeness</span>
              <span>84%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[84%] rounded-full bg-yellow-500"></div>
            </div>
          </div>

        </div>

      </div>

    </section>


    <!-- RISK AND ACTIONS -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- RISK AREAS -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Risk Areas
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Potential gaps affecting compliance
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-red-200 bg-red-50">
            <p class="text-sm font-bold text-slate-900">Delayed Report Submission</p>
            <p class="text-sm text-slate-600 mt-1">Two station reports remain unsubmitted beyond target deadlines.</p>
          </div>

          <div class="p-4 rounded-xl border border-yellow-200 bg-yellow-50">
            <p class="text-sm font-bold text-slate-900">Incomplete Attachments</p>
            <p class="text-sm text-slate-600 mt-1">Several reports lack required photos, signatures, or supporting documents.</p>
          </div>

          <div class="p-4 rounded-xl border border-blue-200 bg-blue-50">
            <p class="text-sm font-bold text-slate-900">Equipment Verification Window</p>
            <p class="text-sm text-slate-600 mt-1">One station missed a scheduled maintenance verification audit this cycle.</p>
          </div>

        </div>

      </div>


      <!-- REMEDIATION PLAN -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Remediation Plan
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Immediate steps to improve health scores
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-emerald-200 bg-emerald-50">
            <p class="text-sm font-bold text-slate-900">Priority 1</p>
            <p class="text-sm text-slate-600 mt-1">Complete all overdue reports and apply review notes before end of day.</p>
          </div>

          <div class="p-4 rounded-xl border border-orange-200 bg-orange-50">
            <p class="text-sm font-bold text-slate-900">Priority 2</p>
            <p class="text-sm text-slate-600 mt-1">Reconcile missing attachments and require station-level verification before submission.</p>
          </div>

          <div class="p-4 rounded-xl border border-indigo-200 bg-indigo-50">
            <p class="text-sm font-bold text-slate-900">Priority 3</p>
            <p class="text-sm text-slate-600 mt-1">Reschedule equipment verification for the affected station and document corrective action.</p>
          </div>

        </div>

      </div>

    </section>

  </div>


  <!-- ===================================================== -->
  <!-- DOCUMENT PIPELINE -->
  <!-- ===================================================== -->
  <div
    v-if="false"
    class="space-y-6"
  >

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

        <div>

          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">
            Records Workflow
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Document Pipeline
          </h2>

          <p class="text-base text-slate-500 mt-1">
            Track submitted documents, monitor approval stages, and manage the digital record flow.
          </p>

        </div>

        <button
          class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition"
        >
          + New Document
        </button>

      </div>

    </section>


    <!-- PIPELINE SUMMARY -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">146</p>
        <p class="text-sm text-slate-500 mt-1">Documents In Queue</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">98</p>
        <p class="text-sm text-slate-500 mt-1">Approved</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">24</p>
        <p class="text-sm text-slate-500 mt-1">Pending Review</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-blue-600">09</p>
        <p class="text-sm text-slate-500 mt-1">Archived Today</p>
      </div>

    </section>


    <!-- PIPELINE STAGES -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- DOCUMENT FLOW -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Document Flow
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Current status of submitted records
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Submission</p>
                <p class="text-xs text-slate-500 mt-1">42 new documents uploaded today</p>
              </div>
              <span class="text-sm font-bold text-[#8B1E23]">Active</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Validation</p>
                <p class="text-xs text-slate-500 mt-1">18 documents awaiting admin review</p>
              </div>
              <span class="text-sm font-bold text-blue-600">In Progress</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Approval</p>
                <p class="text-xs text-slate-500 mt-1">31 documents approved this cycle</p>
              </div>
              <span class="text-sm font-bold text-green-600">Ready</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Archive</p>
                <p class="text-xs text-slate-500 mt-1">12 records successfully filed</p>
              </div>
              <span class="text-sm font-bold text-emerald-600">Completed</span>
            </div>
          </div>

        </div>

      </div>


      <!-- PENDING APPROVALS -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Pending Approvals
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Documents waiting for final action
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-yellow-200 bg-yellow-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">Monthly Compliance Summary</p>
                <p class="text-xs text-slate-500 mt-1">Uploaded by Station 2 • 1 hour ago</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">Review</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-blue-200 bg-blue-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">Barangay Fire Drill Attendance</p>
                <p class="text-xs text-slate-500 mt-1">Uploaded by Admin Office • 3 hours ago</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">Validation</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-red-200 bg-red-50">
            <div class="flex justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">Incident Photo Documentation</p>
                <p class="text-xs text-slate-500 mt-1">Uploaded by FO3 Juan Dela Cruz • 5 hours ago</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-red-100 text-[#8B1E23] text-xs font-bold">Urgent</span>
            </div>
          </div>

        </div>

      </div>

    </section>


    <!-- PROCESS SUMMARY -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- DOCUMENT TYPES -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Document Types
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Most used record categories
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Incident Reports</p>
                <p class="text-xs text-slate-500 mt-1">64 files</p>
              </div>
              <span class="text-sm font-bold text-[#8B1E23]">44%</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Compliance Reports</p>
                <p class="text-xs text-slate-500 mt-1">39 files</p>
              </div>
              <span class="text-sm font-bold text-blue-600">27%</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Training & Activity Logs</p>
                <p class="text-xs text-slate-500 mt-1">25 files</p>
              </div>
              <span class="text-sm font-bold text-green-600">18%</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-bold text-slate-900">Other Records</p>
                <p class="text-xs text-slate-500 mt-1">18 files</p>
              </div>
              <span class="text-sm font-bold text-yellow-600">11%</span>
            </div>
          </div>

        </div>

      </div>


      <!-- RECENT ARCHIVE ACTIVITY -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Recent Archive Activity
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Latest filed documents and updates
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-emerald-200 bg-emerald-50">
            <p class="text-sm font-bold text-slate-900">Station 1 Weekly Summary</p>
            <p class="text-sm text-slate-600 mt-1">Filed successfully and synced to the archive this morning.</p>
          </div>

          <div class="p-4 rounded-xl border border-indigo-200 bg-indigo-50">
            <p class="text-sm font-bold text-slate-900">Barangay Safety Seminar Notes</p>
            <p class="text-sm text-slate-600 mt-1">Approved and stored under training records after final review.</p>
          </div>

          <div class="p-4 rounded-xl border border-amber-200 bg-amber-50">
            <p class="text-sm font-bold text-slate-900">Engine Maintenance Checklist</p>
            <p class="text-sm text-slate-600 mt-1">Auto-saved in the document archive pending audit verification.</p>
          </div>

        </div>

      </div>

    </section>

  </div>


  <!-- ===================================================== -->
  <!-- PRINT & EXPORT PDF -->
  <!-- ===================================================== -->
  <div
    v-if="false"
    class="space-y-6"
  >

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

        <div>

          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">
            Reporting Tools
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Print & Export PDF
          </h2>

          <p class="text-base text-slate-500 mt-1">
            Generate printable reports, export summaries, and prepare official documents for distribution.
          </p>

        </div>

        <button
          class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition"
        >
          Generate PDF
        </button>

      </div>

    </section>


    <!-- EXPORT SUMMARY -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">14</p>
        <p class="text-sm text-slate-500 mt-1">Reports Ready</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">07</p>
        <p class="text-sm text-slate-500 mt-1">Recently Exported</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">03</p>
        <p class="text-sm text-slate-500 mt-1">Queued</p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-blue-600">05</p>
        <p class="text-sm text-slate-500 mt-1">Templates</p>
      </div>

    </section>


    <!-- EXPORT OPTIONS -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- REPORT TEMPLATES -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Report Templates
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Standard document formats available
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-start gap-4">
              <div>
                <p class="text-sm font-bold text-slate-900">Monthly Compliance Report</p>
                <p class="text-xs text-slate-500 mt-1">Standard template for station summaries</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-green-100 text-green-700 text-xs font-bold">Ready</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-start gap-4">
              <div>
                <p class="text-sm font-bold text-slate-900">Incident Summary PDF</p>
                <p class="text-xs text-slate-500 mt-1">Used for formal incident documentation</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">Updated</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-start gap-4">
              <div>
                <p class="text-sm font-bold text-slate-900">Weekly Activity Log</p>
                <p class="text-xs text-slate-500 mt-1">Printable log for operational review</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-yellow-100 text-yellow-700 text-xs font-bold">Draft</span>
            </div>
          </div>

        </div>

      </div>


      <!-- EXPORT STATUS -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Export Status
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Current PDF generation progress
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Daily Summary</span>
              <span>96%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[96%] rounded-full bg-emerald-500"></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Incident Report Bundle</span>
              <span>78%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[78%] rounded-full bg-blue-500"></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Monthly Compliance Pack</span>
              <span>54%</span>
            </div>
            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[54%] rounded-full bg-yellow-500"></div>
            </div>
          </div>

        </div>

      </div>

    </section>


    <!-- EXPORT HISTORY -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- RECENT EXPORTS -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Recent Exports
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Most recent generated files
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-start gap-4">
              <div>
                <p class="text-sm font-bold text-slate-900">Weekly Accomplishment Report</p>
                <p class="text-xs text-slate-500 mt-1">Exported 10 minutes ago</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-green-100 text-green-700 text-xs font-bold">Success</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-start gap-4">
              <div>
                <p class="text-sm font-bold text-slate-900">Barangay Fire Drill Summary</p>
                <p class="text-xs text-slate-500 mt-1">Exported 1 hour ago</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-green-100 text-green-700 text-xs font-bold">Success</span>
            </div>
          </div>

          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
            <div class="flex justify-between items-start gap-4">
              <div>
                <p class="text-sm font-bold text-slate-900">Incident Photo Bundle</p>
                <p class="text-xs text-slate-500 mt-1">Exported yesterday</p>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-blue-100 text-blue-700 text-xs font-bold">Saved</span>
            </div>
          </div>

        </div>

      </div>


      <!-- PRINT SETTINGS -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Print Settings
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Preferred options for generated outputs
            </p>
          </div>
        </div>

        <div class="mt-5 space-y-4">

          <div class="p-4 rounded-xl border border-emerald-200 bg-emerald-50">
            <p class="text-sm font-bold text-slate-900">Paper Size</p>
            <p class="text-sm text-slate-600 mt-1">A4 default with margin optimization for official documentation.</p>
          </div>

          <div class="p-4 rounded-xl border border-indigo-200 bg-indigo-50">
            <p class="text-sm font-bold text-slate-900">Orientation</p>
            <p class="text-sm text-slate-600 mt-1">Portrait for summaries and landscape for multi-table reports.</p>
          </div>

          <div class="p-4 rounded-xl border border-amber-200 bg-amber-50">
            <p class="text-sm font-bold text-slate-900">Watermark</p>
            <p class="text-sm text-slate-600 mt-1">Official document watermark applied for printable compliance reports.</p>
          </div>

        </div>

      </div>

    </section>

  </div>


  <!-- ===================================================== -->
  <!-- FALLBACK -->
  <!-- ===================================================== -->
  <div
    v-if="false"
    class="bg-white border border-slate-200 rounded-2xl shadow-sm p-10 text-center"
  >

    <div
      class="mx-auto h-16 w-16 rounded-full bg-red-50 flex items-center justify-center"
    >

      <svg
        class="w-8 h-8 fill-current text-[#8B1E23]"
        viewBox="0 0 24 24"
        v-html="getSvgPath(getActiveIcon())"
      ></svg>

    </div>

    <h2 class="mt-5 text-2xl font-bold text-slate-900">
      {{ activeMenu }}
    </h2>

    <p class="mt-2 text-base text-slate-500 max-w-lg mx-auto">
      This module is ready for administrator use.
    </p>

  </div>

</main>

    </div>


    <!-- ========================================================= -->
    <!-- LOGOUT CONFIRMATION MODAL -->
    <!-- ========================================================= -->
    <div
      v-if="showLogoutConfirm"
      class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 backdrop-blur-sm px-4"
    >

      <div
        class="w-full max-w-md bg-white rounded-2xl shadow-2xl overflow-hidden"
      >

        <!-- MAROON TOP -->
        <div class="h-2 bg-[#8B1E23]"></div>


        <div class="p-7">

          <div class="flex items-start gap-4">

            <div
              class="h-14 w-14 rounded-full bg-red-50 flex items-center justify-center shrink-0"
            >

              <span class="text-xl">
                🚨
              </span>

            </div>


            <div>

              <h3 class="text-xl font-bold text-slate-900">
                Confirm Sign Out
              </h3>

              <p class="text-base text-slate-500 mt-1">
                Are you sure you want to sign out of the Admin Portal?
              </p>

            </div>

          </div>


          <div
            class="mt-5 p-4 rounded-xl bg-yellow-50 border border-yellow-200"
          >

            <p class="text-sm text-slate-600 leading-relaxed">
              Make sure all important administrative changes and reports
              have been saved before signing out.
            </p>

          </div>


          <div
            class="flex flex-col-reverse sm:flex-row justify-end gap-3 mt-7"
          >

            <button
              @click="showLogoutConfirm = false"
              class="w-full sm:w-auto px-6 py-3 rounded-xl border border-slate-300 bg-white text-slate-700 text-base font-semibold hover:bg-slate-100 transition"
            >
              Cancel
            </button>


            <button
              @click="confirmLogout"
              class="w-full sm:w-auto px-6 py-3 rounded-xl bg-[#8B1E23] text-white text-base font-semibold hover:bg-[#72181D] transition"
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
import Dashboard from './Dashboard.vue'
import ActivityManagement from './ActivityManagement.vue'
import PersonnelManagement from './PersonnelManagement.vue'
import ReportManagement from './ReportManagement.vue'
import DeadlineMonitor from './DeadlineMonitor.vue'
import Notifications from './Notifications.vue'
import WeeklyMonthlyLogs from './WeeklyMonthlyLogs.vue'
import AuditEscalations from './AuditEscalations.vue'
import ComplianceHealth from './ComplianceHealth.vue'
import DocumentPipeline from './DocumentPipeline.vue'
import PrintExportPDF from './PrintExportPDF.vue'

const props = defineProps({
  currentUser: {
    type: Object,
    required: false,
    default: null
  }
})

const emit = defineEmits(['logout'])

const activeMenu = ref('Dashboard')
const showLogoutConfirm = ref(false)

const ICONS = {
  dashboard: 'M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z',
  activity: 'M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11z',
  personnel: 'M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z',
  report: 'M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z',
  deadline: 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z',
  notifications: 'M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z',
  logs: 'M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z',
  shield: 'M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-5.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8s0 0 0 0z',
  default: 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z'
}

const menuBarItems = [
  { name: 'Dashboard', icon: 'dashboard' },
  { name: 'Activity Mgmt.', icon: 'activity' },
  { name: 'Personnel Mgmt.', icon: 'personnel' },
  { name: 'Report Mgmt.', icon: 'report' },
  { name: 'Deadline Monitor', icon: 'deadline' },
  { name: 'Notifications', icon: 'notifications', badge: '3' },
  { name: 'Weekly/Monthly Logs', icon: 'logs' },
]

const capstoneItems = [
  { name: 'Audit & Escalations', icon: 'shield' },
  { name: 'Compliance Health', icon: 'dashboard' },
  { name: 'Document Pipeline', icon: 'report' },
  { name: 'Print & Export PDF', icon: 'report' },
]

const logs = ref([
  {
    activity: 'After-Operation Fire Incident Report',
    personnel: 'SFO1 M. Santos',
    deadline: 'Today, 17:00',
    status: 'Pending'
  },
  {
    activity: 'Quarterly Establishment Inspection',
    personnel: 'FO3 J. Dela Cruz',
    deadline: 'Aug 20, 2026',
    status: 'Completed'
  }
])

const activityList = ref([
  { title: 'Commercial Hydrant Inspection', lead: 'SFO1 M. Santos', type: 'Inspection', date: 'Today', priority: 'High' },
  { title: 'Barangay Safety Seminar', lead: 'FO3 J. Dela Cruz', type: 'Drill', date: 'Tomorrow', priority: 'Medium' },
  { title: 'Engine Maintenance Audit', lead: 'FO1 A. Reyes', type: 'Maintenance', date: 'Aug 19, 2026', priority: 'Low' }
])

const personnelList = ref([
  { name: 'Juan Dela Cruz', rank: 'FO3', role: 'Station Inspector', shift: 'Day' },
  { name: 'M. Santos', rank: 'SFO1', role: 'Operations Chief', shift: 'Day' },
  { name: 'A. Reyes', rank: 'FO1', role: 'Equipment Supervisor', shift: 'Night' }
])

const confirmLogout = () => {
  showLogoutConfirm.value = false
  emit('logout')
}

const getSvgPath = (key) => {
  return `<path d="${ICONS[key] || ICONS.default}"/>`
}

const getActiveIcon = () => {
  const allItems = [...menuBarItems, ...capstoneItems]
  const found = allItems.find(item => item.name === activeMenu.value)
  return found ? found.icon : 'default'
}
</script>