<template>
  <div class="w-full min-w-0 space-y-6">

    <!-- ========================================================= -->
    <!-- PAGE HEADER -->
    <!-- ========================================================= -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex flex-col xl:flex-row xl:items-center xl:justify-between gap-5">

        <div>
          <p class="text-sm font-bold text-[#8B1E23] tracking-wide">
            FIRENOTIFY PERSONNEL PORTAL
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Activities
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            View, monitor, and manage activities assigned to your station.
          </p>
        </div>

        <div class="flex items-center gap-3">

          <div
            class="h-12 w-12 rounded-xl bg-[#8B1E23]/10 flex items-center justify-center"
          >
            <span
              v-html="ICONS.tasks"
              class="h-6 w-6 text-[#8B1E23]"
            ></span>
          </div>

          <div>
            <p class="text-xs text-slate-400">
              Station
            </p>

            <p class="text-base font-bold text-slate-900">
              BFP Balingasag
            </p>
          </div>

        </div>

      </div>

    </section>


    <!-- ========================================================= -->
    <!-- ACTIVITY SUMMARY -->
    <!-- ========================================================= -->
    <section class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-5">

      <!-- TOTAL -->
      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <div class="flex items-center justify-between">

          <div>
            <p class="text-sm text-slate-500">
              Total Activities
            </p>

            <p class="text-3xl font-bold text-slate-900 mt-1">
              {{ totalActivities }}
            </p>

            <p class="text-xs text-slate-400 mt-1">
              Station activities
            </p>
          </div>

          <div
            class="h-12 w-12 rounded-xl bg-blue-50 flex items-center justify-center"
          >
            <span
              v-html="ICONS.tasks"
              class="h-6 w-6 text-blue-600"
            ></span>
          </div>

        </div>
      </div>


      <!-- SCHEDULED -->
      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <div class="flex items-center justify-between">

          <div>
            <p class="text-sm text-slate-500">
              Scheduled
            </p>

            <p class="text-3xl font-bold text-yellow-600 mt-1">
              {{ scheduledActivities }}
            </p>

            <p class="text-xs text-slate-400 mt-1">
              Upcoming activities
            </p>
          </div>

          <div
            class="h-12 w-12 rounded-xl bg-yellow-50 flex items-center justify-center"
          >
            <span
              v-html="ICONS.clock"
              class="h-6 w-6 text-yellow-600"
            ></span>
          </div>

        </div>
      </div>


      <!-- COMPLETED -->
      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <div class="flex items-center justify-between">

          <div>
            <p class="text-sm text-slate-500">
              Completed
            </p>

            <p class="text-3xl font-bold text-green-600 mt-1">
              {{ completedActivities }}
            </p>

            <p class="text-xs text-slate-400 mt-1">
              Successfully completed
            </p>
          </div>

          <div
            class="h-12 w-12 rounded-xl bg-green-50 flex items-center justify-center"
          >
            <span
              v-html="ICONS.check"
              class="h-6 w-6 text-green-600"
            ></span>
          </div>

        </div>
      </div>


      <!-- OVERDUE -->
      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <div class="flex items-center justify-between">

          <div>
            <p class="text-sm text-slate-500">
              Overdue
            </p>

            <p class="text-3xl font-bold text-[#8B1E23] mt-1">
              {{ overdueActivities }}
            </p>

            <p class="text-xs text-slate-400 mt-1">
              Needs attention
            </p>
          </div>

          <div
            class="h-12 w-12 rounded-xl bg-red-50 flex items-center justify-center"
          >
            <span
              v-html="ICONS.siren"
              class="h-6 w-6 text-[#8B1E23]"
            ></span>
          </div>

        </div>
      </div>

    </section>


    <!-- ========================================================= -->
    <!-- SEARCH + FILTERS -->
    <!-- ========================================================= -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

      <div class="flex flex-col xl:flex-row xl:items-end gap-4">

        <!-- SEARCH -->
        <div class="flex-1">

          <label class="block text-sm font-semibold text-slate-700 mb-2">
            Search Activities
          </label>

          <div class="relative">

            <input
              v-model="searchQuery"
              type="text"
              placeholder="Search activity, location, personnel..."
              class="w-full px-4 py-3 pl-11 rounded-xl border border-slate-300 bg-white text-sm outline-none transition focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
            />

            <span
              class="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400"
            >
              🔎
            </span>

          </div>

        </div>


        <!-- STATUS -->
        <div class="w-full xl:w-52">

          <label class="block text-sm font-semibold text-slate-700 mb-2">
            Status
          </label>

          <select
            v-model="statusFilter"
            class="w-full px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm text-slate-700 outline-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
          >
            <option value="All">All Status</option>
            <option value="Scheduled">Scheduled</option>
            <option value="In Progress">In Progress</option>
            <option value="Completed">Completed</option>
            <option value="Overdue">Overdue</option>
          </select>

        </div>


        <!-- TYPE -->
        <div class="w-full xl:w-52">

          <label class="block text-sm font-semibold text-slate-700 mb-2">
            Activity Type
          </label>

          <select
            v-model="typeFilter"
            class="w-full px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm text-slate-700 outline-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
          >
            <option value="All">All Types</option>
            <option value="Inspection">Inspection</option>
            <option value="Patrol">Patrol</option>
            <option value="Training">Training</option>
            <option value="Drill">Drill</option>
            <option value="Seminar">Seminar</option>
            <option value="Meeting">Meeting</option>
          </select>

        </div>


        <!-- RESET -->
        <button
          @click="resetFilters"
          class="px-5 py-3 rounded-xl border border-slate-300 bg-white text-slate-700 text-sm font-bold hover:bg-slate-100 transition"
        >
          Reset
        </button>

      </div>


      <!-- RESULT COUNT -->
      <div class="mt-4 pt-4 border-t border-slate-100 flex items-center justify-between">

        <p class="text-sm text-slate-500">
          Showing
          <span class="font-bold text-slate-900">
            {{ filteredActivities.length }}
          </span>
          of
          <span class="font-bold text-slate-900">
            {{ totalActivities }}
          </span>
          activities
        </p>

        <p
          v-if="searchQuery || statusFilter !== 'All' || typeFilter !== 'All'"
          class="text-xs text-[#8B1E23] font-semibold"
        >
          Filters active
        </p>

      </div>

    </section>


    <!-- ========================================================= -->
    <!-- MAIN CONTENT -->
    <!-- ========================================================= -->
    <section class="grid grid-cols-1 xl:grid-cols-3 gap-6">

      <!-- ======================================================= -->
      <!-- ACTIVITY LIST -->
      <!-- ======================================================= -->
      <div
        class="xl:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
      >

        <div
          class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 border-b border-slate-200 pb-5"
        >

          <div>
            <h3 class="text-lg font-bold text-slate-900">
              Assigned Activities
            </h3>

            <p class="text-sm text-slate-500 mt-1">
              Activities assigned to your station personnel.
            </p>
          </div>

          <span
            class="w-fit px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold"
          >
            {{ filteredActivities.length }} Results
          </span>

        </div>


        <!-- EMPTY STATE -->
        <div
          v-if="filteredActivities.length === 0"
          class="py-14 text-center"
        >

          <div
            class="mx-auto h-16 w-16 rounded-2xl bg-slate-100 flex items-center justify-center"
          >
            <span class="text-2xl">
              🔎
            </span>
          </div>

          <h4 class="mt-4 text-base font-bold text-slate-900">
            No activities found
          </h4>

          <p class="text-sm text-slate-500 mt-1">
            Try changing your search or filters.
          </p>

          <button
            @click="resetFilters"
            class="mt-4 px-4 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-semibold hover:bg-[#72181D]"
          >
            Clear Filters
          </button>

        </div>


        <!-- ACTIVITY CARDS -->
        <div
          v-else
          class="mt-5 space-y-4"
        >

          <article
            v-for="activity in filteredActivities"
            :key="activity.id"
            class="p-5 rounded-xl border transition-all hover:shadow-sm"
            :class="activityCardClass(activity.status)"
          >

            <div class="flex flex-col lg:flex-row lg:items-start gap-4">

              <!-- ICON -->
              <div
                class="h-12 w-12 rounded-xl flex items-center justify-center shrink-0"
                :class="activityIconClass(activity.status)"
              >
                <span
                  v-html="activityIcon(activity.status)"
                  class="h-6 w-6"
                ></span>
              </div>


              <!-- INFORMATION -->
              <div class="flex-1 min-w-0">

                <div
                  class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-3"
                >

                  <div class="min-w-0">

                    <div class="flex flex-wrap items-center gap-2">

                      <h4 class="text-base font-bold text-slate-900">
                        {{ activity.title }}
                      </h4>

                      <span
                        class="px-2.5 py-1 rounded-full text-xs font-bold"
                        :class="statusClass(activity.status)"
                      >
                        {{ activity.status }}
                      </span>

                    </div>

                    <p class="text-sm text-slate-500 mt-1">
                      {{ activity.location }}
                    </p>

                  </div>

                  <span
                    class="w-fit px-2.5 py-1 rounded-lg bg-slate-100 text-slate-600 text-xs font-semibold"
                  >
                    {{ activity.type }}
                  </span>

                </div>


                <!-- DETAILS -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-x-5 gap-y-2 mt-4">

                  <p class="text-sm text-slate-500">
                    <span class="font-semibold text-slate-700">
                      Date:
                    </span>
                    {{ activity.date }}
                  </p>

                  <p class="text-sm text-slate-500">
                    <span class="font-semibold text-slate-700">
                      Time:
                    </span>
                    {{ activity.time }}
                  </p>

                  <p class="text-sm text-slate-500">
                    <span class="font-semibold text-slate-700">
                      Assigned:
                    </span>
                    {{ activity.assignedTo }}
                  </p>

                  <p class="text-sm text-slate-500">
                    <span class="font-semibold text-slate-700">
                      Station:
                    </span>
                    {{ activity.station }}
                  </p>

                </div>


                <!-- PROGRESS -->
                <div
                  v-if="activity.status === 'In Progress'"
                  class="mt-4"
                >

                  <div class="flex justify-between items-center mb-2">

                    <span class="text-xs font-semibold text-slate-500">
                      Activity Progress
                    </span>

                    <span class="text-xs font-bold text-blue-600">
                      {{ activity.progress }}%
                    </span>

                  </div>

                  <div class="h-2.5 rounded-full bg-slate-200 overflow-hidden">

                    <div
                      class="h-full bg-blue-600 rounded-full transition-all duration-500"
                      :style="{ width: `${activity.progress}%` }"
                    ></div>

                  </div>

                </div>


                <!-- COMPLETED -->
                <p
                  v-if="activity.status === 'Completed'"
                  class="mt-4 text-xs font-semibold text-green-700"
                >
                  ✓ Activity completed successfully
                </p>


                <!-- OVERDUE -->
                <p
                  v-if="activity.status === 'Overdue'"
                  class="mt-4 text-xs font-bold text-[#8B1E23]"
                >
                  ⚠ This activity requires immediate attention.
                </p>


                <!-- ACTIONS -->
                <div class="mt-4 flex flex-wrap gap-2">

                  <button
                    @click="openDetails(activity)"
                    class="px-4 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-semibold hover:bg-[#72181D] transition"
                  >
                    View Details
                  </button>


                  <button
                    v-if="activity.status !== 'Completed'"
                    @click="openStatusModal(activity)"
                    class="px-4 py-2 rounded-lg border border-slate-300 bg-white text-slate-700 text-sm font-semibold hover:bg-slate-100 transition"
                  >
                    Update Status
                  </button>


                  <button
                    v-if="activity.status === 'Overdue'"
                    @click="resolveActivity(activity)"
                    class="px-4 py-2 rounded-lg border border-red-200 bg-red-50 text-[#8B1E23] text-sm font-semibold hover:bg-red-100 transition"
                  >
                    Resolve Activity
                  </button>

                </div>

              </div>

            </div>

          </article>

        </div>

      </div>


      <!-- ======================================================= -->
      <!-- RIGHT SIDEBAR -->
      <!-- ======================================================= -->
      <div class="space-y-6">


        <!-- TODAY'S ACTIVITIES -->
        <div
          class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
        >

          <div class="flex items-center justify-between">

            <div>
              <h3 class="text-lg font-bold text-slate-900">
                Today's Activities
              </h3>

              <p class="text-sm text-slate-500 mt-1">
                September 12, 2026
              </p>
            </div>

            <div
              class="h-10 w-10 rounded-xl bg-[#8B1E23]/10 flex items-center justify-center"
            >
              <span
                v-html="ICONS.clock"
                class="h-5 w-5 text-[#8B1E23]"
              ></span>
            </div>

          </div>


          <div class="mt-5 space-y-4">

            <div
              v-for="item in todaysActivities"
              :key="item.title"
              class="flex gap-3"
            >

              <div
                class="w-1 rounded-full"
                :class="item.completed ? 'bg-green-500' : 'bg-[#8B1E23]'"
              ></div>

              <div>

                <p class="text-sm font-bold text-slate-900">
                  {{ item.title }}
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  {{ item.time }} · {{ item.location }}
                </p>

                <span
                  class="inline-block mt-2 text-xs font-semibold"
                  :class="item.completed ? 'text-green-700' : 'text-yellow-700'"
                >
                  {{ item.completed ? 'Completed' : 'Scheduled' }}
                </span>

              </div>

            </div>

          </div>

        </div>


        <!-- UPCOMING -->
        <div
          class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
        >

          <h3 class="text-lg font-bold text-slate-900">
            Upcoming Activities
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            Next scheduled station activities.
          </p>


          <div class="mt-5 space-y-3">

            <div
              v-for="item in upcomingActivities"
              :key="item.title"
              class="p-4 rounded-xl bg-slate-50 border border-slate-200 hover:border-[#8B1E23]/30 transition"
            >

              <div class="flex items-start justify-between gap-3">

                <div>

                  <p class="text-sm font-bold text-slate-900">
                    {{ item.title }}
                  </p>

                  <p class="text-xs text-slate-500 mt-1">
                    {{ item.date }} · {{ item.time }}
                  </p>

                  <p class="text-xs text-slate-500 mt-1">
                    {{ item.location }}
                  </p>

                </div>

                <span
                  class="text-xs font-bold text-[#8B1E23]"
                >
                  {{ item.days }}
                </span>

              </div>

            </div>

          </div>

        </div>


        <!-- PERFORMANCE -->
        <div
          class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
        >

          <h3 class="text-lg font-bold text-slate-900">
            Activity Performance
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            Current station completion rate.
          </p>


          <div class="mt-5">

            <div class="flex items-end justify-between">

              <p class="text-3xl font-bold text-[#8B1E23]">
                {{ completionRate }}%
              </p>

              <span
                class="text-xs font-semibold"
                :class="completionRate >= 80 ? 'text-green-600' : 'text-yellow-600'"
              >
                {{ completionMessage }}
              </span>

            </div>


            <div class="mt-3 h-3 rounded-full bg-slate-200 overflow-hidden">

              <div
                class="h-full bg-[#8B1E23] rounded-full transition-all duration-500"
                :style="{ width: `${completionRate}%` }"
              ></div>

            </div>


            <div class="grid grid-cols-2 gap-4 mt-5">

              <div>

                <p class="text-xs text-slate-500">
                  Completed
                </p>

                <p class="text-lg font-bold text-green-600">
                  {{ completedActivities }}
                </p>

              </div>

              <div>

                <p class="text-xs text-slate-500">
                  Pending
                </p>

                <p class="text-lg font-bold text-yellow-600">
                  {{ pendingActivities }}
                </p>

              </div>

            </div>

          </div>

        </div>


        <!-- QUICK INFORMATION -->
        <div
          class="rounded-2xl bg-[#8B1E23] text-white p-6 shadow-sm"
        >

          <div class="flex items-start gap-3">

            <div
              class="h-10 w-10 rounded-xl bg-white/10 flex items-center justify-center shrink-0"
            >
              ℹ
            </div>

            <div>

              <h3 class="font-bold">
                Activity Reminder
              </h3>

              <p class="text-sm text-white/75 mt-2 leading-relaxed">
                Keep your assigned activities updated to maintain accurate
                station compliance records.
              </p>

            </div>

          </div>

        </div>

      </div>

    </section>


    <!-- ========================================================= -->
    <!-- ACTIVITY DETAILS MODAL -->
    <!-- ========================================================= -->
    <div
      v-if="showDetailsModal && selectedActivity"
      class="fixed inset-0 z-50 bg-slate-900/50 flex items-center justify-center p-4"
      @click.self="closeDetails"
    >

      <div
        class="w-full max-w-2xl bg-white rounded-2xl shadow-xl overflow-hidden"
      >

        <!-- MODAL HEADER -->
        <div
          class="px-6 py-5 border-b border-slate-200 flex items-center justify-between"
        >

          <div>

            <p class="text-xs font-bold text-[#8B1E23] uppercase">
              Activity Details
            </p>

            <h3 class="text-xl font-bold text-slate-900 mt-1">
              {{ selectedActivity.title }}
            </h3>

          </div>

          <button
            @click="closeDetails"
            class="h-10 w-10 rounded-xl hover:bg-slate-100 text-slate-500 text-xl"
          >
            ×
          </button>

        </div>


        <!-- MODAL BODY -->
        <div class="p-6 space-y-5">

          <div class="flex items-center justify-between">

            <span
              class="px-3 py-1.5 rounded-full text-xs font-bold"
              :class="statusClass(selectedActivity.status)"
            >
              {{ selectedActivity.status }}
            </span>

            <span
              class="px-3 py-1.5 rounded-lg bg-slate-100 text-slate-600 text-xs font-semibold"
            >
              {{ selectedActivity.type }}
            </span>

          </div>


          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-400 uppercase font-semibold">
                Location
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedActivity.location }}
              </p>
            </div>

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-400 uppercase font-semibold">
                Station
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedActivity.station }}
              </p>
            </div>

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-400 uppercase font-semibold">
                Date
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedActivity.date }}
              </p>
            </div>

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-400 uppercase font-semibold">
                Time
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedActivity.time }}
              </p>
            </div>

            <div class="p-4 rounded-xl bg-slate-50 sm:col-span-2">
              <p class="text-xs text-slate-400 uppercase font-semibold">
                Assigned Personnel
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedActivity.assignedTo }}
              </p>
            </div>

          </div>


          <div
            v-if="selectedActivity.status === 'In Progress'"
            class="p-4 rounded-xl border border-blue-100 bg-blue-50"
          >

            <div class="flex justify-between">

              <p class="text-sm font-semibold text-blue-700">
                Progress
              </p>

              <p class="text-sm font-bold text-blue-700">
                {{ selectedActivity.progress }}%
              </p>

            </div>

            <div class="mt-3 h-2.5 rounded-full bg-blue-100 overflow-hidden">

              <div
                class="h-full bg-blue-600 rounded-full"
                :style="{ width: `${selectedActivity.progress}%` }"
              ></div>

            </div>

          </div>


          <div
            v-if="selectedActivity.status === 'Overdue'"
            class="p-4 rounded-xl border border-red-200 bg-red-50"
          >

            <p class="text-sm font-bold text-[#8B1E23]">
              ⚠ Overdue Activity
            </p>

            <p class="text-sm text-slate-600 mt-1">
              This activity has passed its scheduled date and requires
              attention from assigned personnel.
            </p>

          </div>

        </div>


        <!-- MODAL FOOTER -->
        <div
          class="px-6 py-4 bg-slate-50 border-t border-slate-200 flex justify-end gap-3"
        >

          <button
            @click="closeDetails"
            class="px-5 py-2.5 rounded-xl border border-slate-300 bg-white text-slate-700 text-sm font-bold hover:bg-slate-100"
          >
            Close
          </button>

          <button
            v-if="selectedActivity.status !== 'Completed'"
            @click="openStatusModal(selectedActivity); closeDetails()"
            class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]"
          >
            Update Status
          </button>

        </div>

      </div>

    </div>


    <!-- ========================================================= -->
    <!-- UPDATE STATUS MODAL -->
    <!-- ========================================================= -->
    <div
      v-if="showStatusModal && selectedActivity"
      class="fixed inset-0 z-[60] bg-slate-900/50 flex items-center justify-center p-4"
      @click.self="closeStatusModal"
    >

      <div
        class="w-full max-w-md bg-white rounded-2xl shadow-xl overflow-hidden"
      >

        <div class="px-6 py-5 border-b border-slate-200">

          <p class="text-xs font-bold text-[#8B1E23] uppercase">
            Update Activity
          </p>

          <h3 class="text-lg font-bold text-slate-900 mt-1">
            {{ selectedActivity.title }}
          </h3>

        </div>


        <div class="p-6">

          <label class="block text-sm font-semibold text-slate-700 mb-2">
            New Status
          </label>

          <select
            v-model="newStatus"
            class="w-full px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm outline-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
          >
            <option value="Scheduled">Scheduled</option>
            <option value="In Progress">In Progress</option>
            <option value="Completed">Completed</option>
          </select>


          <p class="text-xs text-slate-500 mt-3">
            Updating the status changes the activity record displayed in
            the personnel portal.
          </p>

        </div>


        <div
          class="px-6 py-4 bg-slate-50 border-t border-slate-200 flex justify-end gap-3"
        >

          <button
            @click="closeStatusModal"
            class="px-5 py-2.5 rounded-xl border border-slate-300 bg-white text-slate-700 text-sm font-bold hover:bg-slate-100"
          >
            Cancel
          </button>

          <button
            @click="saveStatus"
            class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]"
          >
            Save Status
          </button>

        </div>

      </div>

    </div>


    <!-- ========================================================= -->
    <!-- SUCCESS NOTIFICATION -->
    <!-- ========================================================= -->
    <transition name="toast">

      <div
        v-if="toastMessage"
        class="fixed bottom-6 right-6 z-[70] bg-white border border-slate-200 shadow-xl rounded-xl px-5 py-4 flex items-center gap-3"
      >

        <div
          class="h-9 w-9 rounded-full bg-green-100 flex items-center justify-center text-green-600 font-bold"
        >
          ✓
        </div>

        <div>

          <p class="text-sm font-bold text-slate-900">
            Action Successful
          </p>

          <p class="text-xs text-slate-500 mt-0.5">
            {{ toastMessage }}
          </p>

        </div>

      </div>

    </transition>

  </div>
</template>


<script setup>
import { computed, ref } from 'vue'


/* =========================================================
   PROPS
========================================================= */

const props = defineProps({
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

const ICONS = props.ICONS


/* =========================================================
   ACTIVITY DATA
   Frontend demo data.
   This can later be replaced with Django API data.
========================================================= */

const activities = ref([
  {
    id: 1,
    title: 'Fire Safety Inspection',
    type: 'Inspection',
    location: 'Public Market Complex',
    date: 'September 12, 2026',
    time: '09:00 AM',
    assignedTo: 'FO3 Juan Dela Cruz',
    station: 'Balingasag',
    status: 'Scheduled',
    progress: 0
  },

  {
    id: 2,
    title: 'Community Fire Safety Seminar',
    type: 'Seminar',
    location: 'Barangay San Isidro Covered Court',
    date: 'September 13, 2026',
    time: '01:00 PM',
    assignedTo: 'FO2 Mark Santos',
    station: 'Balingasag',
    status: 'In Progress',
    progress: 60
  },

  {
    id: 3,
    title: 'Routine Safety Patrol',
    type: 'Patrol',
    location: 'Zone 2 Commercial Area',
    date: 'September 10, 2026',
    time: '08:00 AM',
    assignedTo: 'FO3 Juan Dela Cruz',
    station: 'Balingasag',
    status: 'Completed',
    progress: 100
  },

  {
    id: 4,
    title: 'Fire Drill Monitoring',
    type: 'Drill',
    location: 'Municipal Elementary School',
    date: 'September 09, 2026',
    time: '10:00 AM',
    assignedTo: 'FO1 Carlo Reyes',
    station: 'Balingasag',
    status: 'Overdue',
    progress: 0
  },

  {
    id: 5,
    title: 'Emergency Response Drill',
    type: 'Drill',
    location: 'Balingasag Municipal Hall',
    date: 'September 15, 2026',
    time: '08:30 AM',
    assignedTo: 'FO3 Juan Dela Cruz',
    station: 'Balingasag',
    status: 'Scheduled',
    progress: 0
  },

  {
    id: 6,
    title: 'Personnel Training',
    type: 'Training',
    location: 'BFP Training Room',
    date: 'September 17, 2026',
    time: '09:00 AM',
    assignedTo: 'FO2 Mark Santos',
    station: 'Balingasag',
    status: 'Scheduled',
    progress: 0
  }
])


/* =========================================================
   FILTERS
========================================================= */

const searchQuery = ref('')
const statusFilter = ref('All')
const typeFilter = ref('All')


/* =========================================================
   MODALS
========================================================= */

const showDetailsModal = ref(false)
const showStatusModal = ref(false)

const selectedActivity = ref(null)
const newStatus = ref('Scheduled')


/* =========================================================
   TOAST
========================================================= */

const toastMessage = ref('')

let toastTimer = null

const showToast = (message) => {
  toastMessage.value = message

  clearTimeout(toastTimer)

  toastTimer = setTimeout(() => {
    toastMessage.value = ''
  }, 3000)
}


/* =========================================================
   STATISTICS
========================================================= */

const totalActivities = computed(() => {
  return activities.value.length
})

const scheduledActivities = computed(() => {
  return activities.value.filter(
    activity => activity.status === 'Scheduled'
  ).length
})

const completedActivities = computed(() => {
  return activities.value.filter(
    activity => activity.status === 'Completed'
  ).length
})

const overdueActivities = computed(() => {
  return activities.value.filter(
    activity => activity.status === 'Overdue'
  ).length
})

const pendingActivities = computed(() => {
  return activities.value.filter(
    activity =>
      activity.status === 'Scheduled' ||
      activity.status === 'In Progress' ||
      activity.status === 'Overdue'
  ).length
})


/* =========================================================
   COMPLETION RATE
========================================================= */

const completionRate = computed(() => {

  if (!activities.value.length) {
    return 0
  }

  return Math.round(
    (completedActivities.value / activities.value.length) * 100
  )
})

const completionMessage = computed(() => {

  if (completionRate.value >= 90) {
    return 'Excellent'
  }

  if (completionRate.value >= 80) {
    return 'Good standing'
  }

  if (completionRate.value >= 60) {
    return 'Needs improvement'
  }

  return 'Attention required'
})


/* =========================================================
   FILTERED ACTIVITIES
========================================================= */

const filteredActivities = computed(() => {

  const query = searchQuery.value.trim().toLowerCase()

  return activities.value.filter(activity => {

    const matchesSearch =
      !query ||
      activity.title.toLowerCase().includes(query) ||
      activity.location.toLowerCase().includes(query) ||
      activity.assignedTo.toLowerCase().includes(query) ||
      activity.type.toLowerCase().includes(query)

    const matchesStatus =
      statusFilter.value === 'All' ||
      activity.status === statusFilter.value

    const matchesType =
      typeFilter.value === 'All' ||
      activity.type === typeFilter.value

    return (
      matchesSearch &&
      matchesStatus &&
      matchesType
    )
  })
})


/* =========================================================
   TODAY'S ACTIVITIES
========================================================= */

const todaysActivities = ref([
  {
    title: 'Fire Safety Inspection',
    time: '09:00 AM',
    location: 'Public Market',
    completed: false
  },

  {
    title: 'Station Briefing',
    time: '04:00 PM',
    location: 'BFP Station',
    completed: false
  }
])


/* =========================================================
   UPCOMING ACTIVITIES
========================================================= */

const upcomingActivities = ref([
  {
    title: 'Community Fire Safety Seminar',
    date: 'September 13',
    time: '01:00 PM',
    location: 'Barangay San Isidro',
    days: 'Tomorrow'
  },

  {
    title: 'Emergency Response Drill',
    date: 'September 15',
    time: '08:30 AM',
    location: 'Balingasag Municipal Hall',
    days: 'Sep 15'
  },

  {
    title: 'Personnel Training',
    date: 'September 17',
    time: '09:00 AM',
    location: 'BFP Training Room',
    days: 'Sep 17'
  }
])


/* =========================================================
   FILTER RESET
========================================================= */

const resetFilters = () => {

  searchQuery.value = ''
  statusFilter.value = 'All'
  typeFilter.value = 'All'
}


/* =========================================================
   VIEW DETAILS
========================================================= */

const openDetails = (activity) => {

  selectedActivity.value = activity
  showDetailsModal.value = true
}

const closeDetails = () => {

  showDetailsModal.value = false
}


/* =========================================================
   UPDATE STATUS
========================================================= */

const openStatusModal = (activity) => {

  selectedActivity.value = activity
  newStatus.value = activity.status === 'Overdue'
    ? 'In Progress'
    : activity.status

  showStatusModal.value = true
}

const closeStatusModal = () => {

  showStatusModal.value = false
}

const saveStatus = () => {

  if (!selectedActivity.value) {
    return
  }

  selectedActivity.value.status = newStatus.value

  if (newStatus.value === 'Completed') {
    selectedActivity.value.progress = 100
  }

  if (newStatus.value === 'In Progress') {

    if (
      !selectedActivity.value.progress ||
      selectedActivity.value.progress === 100
    ) {
      selectedActivity.value.progress = 10
    }
  }

  if (newStatus.value === 'Scheduled') {
    selectedActivity.value.progress = 0
  }

  const title = selectedActivity.value.title

  closeStatusModal()

  showToast(`${title} status updated.`)
}


/* =========================================================
   RESOLVE OVERDUE ACTIVITY
========================================================= */

const resolveActivity = (activity) => {

  activity.status = 'In Progress'
  activity.progress = 10

  showToast(
    `${activity.title} has been moved to In Progress.`
  )
}


/* =========================================================
   STATUS STYLING
========================================================= */

const statusClass = (status) => {

  const classes = {

    Scheduled:
      'bg-yellow-100 text-yellow-700',

    'In Progress':
      'bg-blue-100 text-blue-700',

    Completed:
      'bg-green-100 text-green-700',

    Overdue:
      'bg-red-100 text-[#8B1E23]'
  }

  return classes[status] || 'bg-slate-100 text-slate-700'
}


/* =========================================================
   ACTIVITY CARD STYLING
========================================================= */

const activityCardClass = (status) => {

  const classes = {

    Scheduled:
      'border-yellow-200 bg-yellow-50/40',

    'In Progress':
      'border-blue-200 bg-blue-50/40',

    Completed:
      'border-green-200 bg-green-50',

    Overdue:
      'border-red-200 bg-red-50'
  }

  return classes[status] || 'border-slate-200 bg-slate-50'
}


/* =========================================================
   ACTIVITY ICON BACKGROUND
========================================================= */

const activityIconClass = (status) => {

  const classes = {

    Scheduled:
      'bg-yellow-100 text-yellow-700',

    'In Progress':
      'bg-blue-100 text-blue-700',

    Completed:
      'bg-green-100 text-green-700',

    Overdue:
      'bg-red-100 text-[#8B1E23]'
  }

  return classes[status] || 'bg-slate-100 text-slate-600'
}


/* =========================================================
   ACTIVITY ICON
========================================================= */

const activityIcon = (status) => {

  if (status === 'Completed') {
    return ICONS.check
  }

  if (status === 'Overdue') {
    return ICONS.siren
  }

  if (status === 'In Progress') {
    return ICONS.clock
  }

  return ICONS.tasks
}
</script>


<style scoped>
.toast-enter-active,
.toast-leave-active {
  transition: all 0.25s ease;
}

.toast-enter-from,
.toast-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>