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

  <!-- ===================================================== -->
  <!-- DASHBOARD -->
  <!-- ===================================================== -->
  <div
    v-if="activeMenu === 'Dashboard'"
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

  </div>


  <!-- ===================================================== -->
  <!-- ACTIVITY MANAGEMENT -->
  <!-- ===================================================== -->
  <div
    v-else-if="activeMenu === 'Activity Mgmt.'"
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

  </div>


  <!-- ===================================================== -->
  <!-- PERSONNEL MANAGEMENT -->
  <!-- ===================================================== -->
  <div
    v-else-if="activeMenu === 'Personnel Mgmt.'"
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

  </div>


  <!-- ===================================================== -->
  <!-- REPORT MANAGEMENT -->
  <!-- ===================================================== -->
  <div
    v-else-if="activeMenu === 'Report Mgmt.'"
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

  </div>


  <!-- ===================================================== -->
  <!-- DEADLINE MONITOR -->
  <!-- ===================================================== -->
  <div
    v-else-if="activeMenu === 'Deadline Monitor'"
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

  </div>


  <!-- ===================================================== -->
  <!-- NOTIFICATIONS -->
  <!-- ===================================================== -->
  <div
    v-else-if="activeMenu === 'Notifications'"
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

  </div>


  <!-- ===================================================== -->
  <!-- FALLBACK -->
  <!-- ===================================================== -->
  <div
    v-else
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