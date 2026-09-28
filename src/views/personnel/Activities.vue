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
            View, monitor, and manage station activities.
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
              Portal
            </p>

            <p class="text-base font-bold text-slate-900">
              Station Activities
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
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
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
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
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
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
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
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
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
            <option value="All">
              All Status
            </option>

            <option value="Scheduled">
              Scheduled
            </option>

            <option value="Assigned">
              Assigned
            </option>

            <option value="In Progress">
              In Progress
            </option>

            <option value="Completed">
              Completed
            </option>

            <option value="For Verification">
              For Verification
            </option>

            <option value="Returned">
              Returned
            </option>

            <option value="Verified">
              Verified
            </option>

            <option value="Overdue">
              Overdue
            </option>
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
            <option value="All">
              All Types
            </option>

            <option value="Inspection">
              Inspection
            </option>

            <option value="Patrol">
              Patrol
            </option>

            <option value="Training">
              Training
            </option>

            <option value="Drill">
              Drill
            </option>

            <option value="Seminar">
              Seminar
            </option>

            <option value="Meeting">
              Meeting
            </option>

            <option value="Other">
              Other
            </option>

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
      <div
        class="mt-4 pt-4 border-t border-slate-100 flex items-center justify-between"
      >

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
              Station Activities
            </h3>

            <p class="text-sm text-slate-500 mt-1">
              Activities created through Activity Management.
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
            No activities match your current filters.
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
                      {{ activity.location || 'No location specified' }}
                    </p>

                  </div>

                  <span
                    class="w-fit px-2.5 py-1 rounded-lg bg-slate-100 text-slate-600 text-xs font-semibold"
                  >
                    {{ activity.type || 'Activity' }}
                  </span>

                </div>


                <!-- DETAILS -->
                <div
                  class="grid grid-cols-1 sm:grid-cols-2 gap-x-5 gap-y-2 mt-4"
                >

                  <p class="text-sm text-slate-500">

                    <span class="font-semibold text-slate-700">
                      Date:
                    </span>

                    {{ formatDate(activity.date) }}

                  </p>


                  <p class="text-sm text-slate-500">

                    <span class="font-semibold text-slate-700">
                      Time:
                    </span>

                    {{ activity.time || 'Not specified' }}

                  </p>


                  <p class="text-sm text-slate-500">

                    <span class="font-semibold text-slate-700">
                      Assigned:
                    </span>

                    {{ assignedPersonnelName(activity) }}

                  </p>


                  <p class="text-sm text-slate-500">

                    <span class="font-semibold text-slate-700">
                      Created:
                    </span>

                    {{ formatCreatedDate(activity.createdAt) }}

                  </p>

                </div>


                <!-- DESCRIPTION -->
                <div
                  v-if="activity.description"
                  class="mt-4 p-3 rounded-lg bg-white/70 border border-slate-200"
                >

                  <p class="text-xs font-semibold text-slate-500 mb-1">
                    Description
                  </p>

                  <p class="text-sm text-slate-600 leading-relaxed">
                    {{ activity.description }}
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
                      {{ normalizedProgress(activity.progress) }}%
                    </span>

                  </div>

                  <div class="h-2.5 rounded-full bg-slate-200 overflow-hidden">

                    <div
                      class="h-full bg-blue-600 rounded-full transition-all duration-500"
                      :style="{
                        width: `${normalizedProgress(activity.progress)}%`
                      }"
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
                  ⚠ This activity requires attention.
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
                    v-if="activity.status === 'Scheduled' || activity.status === 'Assigned' || activity.status === 'Overdue'"
                    @click="startActivity(activity)"
                    class="px-4 py-2 rounded-lg border border-slate-300 bg-white text-slate-700 text-sm font-semibold hover:bg-slate-100 transition"
                  >
                    Start Activity
                  </button>

                  <button
                    v-if="activity.status === 'In Progress' || activity.status === 'Returned'"
                    @click="openSubmissionModal(activity)"
                    class="px-4 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-semibold hover:bg-[#72181D] transition"
                  >
                    {{ activity.status === 'Returned' ? 'Revise Submission' : 'Submit for Verification' }}
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
                {{ formattedToday }}
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


          <div
            v-if="todaysActivities.length"
            class="mt-5 space-y-4"
          >

            <div
              v-for="item in todaysActivities"
              :key="item.id"
              class="flex gap-3"
            >

              <div
                class="w-1 rounded-full"
                :class="
                  item.status === 'Completed'
                    ? 'bg-green-500'
                    : 'bg-[#8B1E23]'
                "
              ></div>

              <div class="min-w-0">

                <p class="text-sm font-bold text-slate-900">
                  {{ item.title }}
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  {{ item.time || 'Time not specified' }}
                  ·
                  {{ item.location || 'No location' }}
                </p>

                <span
                  class="inline-block mt-2 text-xs font-semibold"
                  :class="
                    item.status === 'Completed'
                      ? 'text-green-700'
                      : 'text-yellow-700'
                  "
                >
                  {{ item.status }}
                </span>

              </div>

            </div>

          </div>


          <div
            v-else
            class="mt-5 p-4 rounded-xl bg-slate-50 border border-slate-200 text-center"
          >

            <p class="text-sm text-slate-500">
              No activities scheduled for today.
            </p>

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


          <div
            v-if="upcomingActivities.length"
            class="mt-5 space-y-3"
          >

            <div
              v-for="item in upcomingActivities"
              :key="item.id"
              class="p-4 rounded-xl bg-slate-50 border border-slate-200 hover:border-[#8B1E23]/30 transition"
            >

              <div class="flex items-start justify-between gap-3">

                <div class="min-w-0">

                  <p class="text-sm font-bold text-slate-900">
                    {{ item.title }}
                  </p>

                  <p class="text-xs text-slate-500 mt-1">
                    {{ formatDate(item.date) }}
                    ·
                    {{ item.time || 'Time not specified' }}
                  </p>

                  <p class="text-xs text-slate-500 mt-1">
                    {{ item.location || 'No location specified' }}
                  </p>

                </div>

                <span class="text-xs font-bold text-[#8B1E23] shrink-0">
                  {{ daysUntil(item.date) }}
                </span>

              </div>

            </div>

          </div>


          <div
            v-else
            class="mt-5 p-4 rounded-xl bg-slate-50 border border-slate-200 text-center"
          >

            <p class="text-sm text-slate-500">
              No upcoming activities.
            </p>

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
                :class="
                  completionRate >= 80
                    ? 'text-green-600'
                    : 'text-yellow-600'
                "
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
                Keep activity statuses updated to maintain accurate
                station operations and compliance records.
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

        <!-- HEADER -->
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


        <!-- BODY -->
        <div class="p-6 space-y-5">

          <div class="flex items-center justify-between gap-3">

            <span
              class="px-3 py-1.5 rounded-full text-xs font-bold"
              :class="statusClass(selectedActivity.status)"
            >
              {{ selectedActivity.status }}
            </span>

            <span
              class="px-3 py-1.5 rounded-lg bg-slate-100 text-slate-600 text-xs font-semibold"
            >
              {{ selectedActivity.type || 'Activity' }}
            </span>

          </div>


          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">

            <div class="p-4 rounded-xl bg-slate-50">

              <p class="text-xs text-slate-400 uppercase font-semibold">
                Location
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedActivity.location || 'Not specified' }}
              </p>

            </div>


            <div class="p-4 rounded-xl bg-slate-50">

              <p class="text-xs text-slate-400 uppercase font-semibold">
                Date
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ formatDate(selectedActivity.date) }}
              </p>

            </div>


            <div class="p-4 rounded-xl bg-slate-50">

              <p class="text-xs text-slate-400 uppercase font-semibold">
                Time
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedActivity.time || 'Not specified' }}
              </p>

            </div>


            <div class="p-4 rounded-xl bg-slate-50">

              <p class="text-xs text-slate-400 uppercase font-semibold">
                Assigned Personnel
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ assignedPersonnelName(selectedActivity) }}
              </p>

            </div>


            <div
              v-if="selectedActivity.description"
              class="p-4 rounded-xl bg-slate-50 sm:col-span-2"
            >

              <p class="text-xs text-slate-400 uppercase font-semibold">
                Description
              </p>

              <p class="text-sm text-slate-700 mt-1 leading-relaxed">
                {{ selectedActivity.description }}
              </p>

            </div>

          </div>


          <!-- PROGRESS -->
          <div
            v-if="selectedActivity.status === 'In Progress'"
            class="p-4 rounded-xl border border-blue-100 bg-blue-50"
          >

            <div class="flex justify-between">

              <p class="text-sm font-semibold text-blue-700">
                Progress
              </p>

              <p class="text-sm font-bold text-blue-700">
                {{ normalizedProgress(selectedActivity.progress) }}%
              </p>

            </div>

            <div class="mt-3 h-2.5 rounded-full bg-blue-100 overflow-hidden">

              <div
                class="h-full bg-blue-600 rounded-full"
                :style="{
                  width: `${normalizedProgress(selectedActivity.progress)}%`
                }"
              ></div>

            </div>

          </div>


          <!-- OVERDUE -->
          <div
            v-if="selectedActivity.status === 'Overdue'"
            class="p-4 rounded-xl border border-red-200 bg-red-50"
          >

            <p class="text-sm font-bold text-[#8B1E23]">
              ⚠ Overdue Activity
            </p>

            <p class="text-sm text-slate-600 mt-1">
              This activity has passed its scheduled date and
              requires attention.
            </p>

          </div>

        </div>


        <!-- FOOTER -->
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
            v-if="selectedActivity.status === 'Scheduled' || selectedActivity.status === 'Assigned' || selectedActivity.status === 'Overdue'"
            @click="openStatusFromDetails"
            class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]"
          >
            Start Activity
          </button>

          <button
            v-if="selectedActivity.status === 'In Progress' || selectedActivity.status === 'Returned'"
            @click="openSubmissionModal(selectedActivity); closeDetails()"
            class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]"
          >
            Submit for Verification
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

            <option value="Scheduled">
              Scheduled
            </option>

            <option value="In Progress">
              In Progress
            </option>

          </select>


          <div
            v-if="newStatus === 'In Progress'"
            class="mt-4"
          >

            <label class="block text-sm font-semibold text-slate-700 mb-2">
              Progress
            </label>

            <input
              v-model.number="newProgress"
              type="number"
              min="1"
              max="99"
              class="w-full px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm outline-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
            />

          </div>


          <p class="text-xs text-slate-500 mt-3">
            Updating the status saves the change to the shared
            activity record.
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


    <div
      v-if="submissionActivity"
      class="fixed inset-0 z-[70] bg-slate-900/50 flex items-center justify-center p-4"
      @click.self="closeSubmissionModal"
    >
      <div class="fn-modal-panel w-full max-w-2xl bg-white rounded-2xl shadow-xl overflow-hidden">
        <div class="px-6 py-5 border-b border-slate-200">
          <p class="text-xs font-bold uppercase tracking-wide text-[#8B1E23]">Activity Submission</p>
          <h3 class="text-xl font-bold text-slate-900 mt-1">{{ submissionActivity.title }}</h3>
          <p class="text-sm text-slate-500 mt-1">Submit accomplishment for Admin verification.</p>
          <div class="mt-3 flex flex-wrap gap-3 text-xs text-slate-500">
            <span>Status: {{ submissionActivity.status }}</span>
            <span>Reference: {{ submissionActivity.id }}</span>
          </div>
        </div>

        <div class="p-6 space-y-5">
          <div>
            <label class="block text-sm font-bold text-slate-700 mb-2">
              Accomplishment / Work Summary
              <span class="text-[#8B1E23]">*</span>
            </label>
            <textarea v-model="activityAccomplishment" rows="5" placeholder="Describe the work completed, observations, and outcomes." class="fn-form-control resize-none"></textarea>
            <p class="fn-form-help">Provide the work completed for Admin verification.</p>
          </div>

          <div>
            <label class="block text-sm font-bold text-slate-700 mb-2">
              Remarks <span class="font-normal text-slate-400">(Optional)</span>
            </label>
            <textarea v-model="activityRemarks" rows="3" placeholder="Add additional remarks or notes..." class="fn-form-control resize-none"></textarea>
          </div>
          <div>
            <label class="block text-sm font-bold text-slate-700 mb-2">Evidence Photos <span class="font-normal text-slate-400">(optional)</span></label>
            <input type="file" multiple accept=".jpg,.jpeg,.png,.webp,image/jpeg,image/png,image/webp" @change="handleActivityEvidence" class="block w-full text-sm text-slate-600 file:mr-4 file:py-2.5 file:px-4 file:rounded-xl file:border-0 file:bg-[#8B1E23] file:text-white file:font-semibold" />
            <div v-if="activityEvidenceFiles.length" class="mt-3 grid grid-cols-2 sm:grid-cols-3 gap-3">
              <div v-for="(file, index) in activityEvidenceFiles" :key="`${file.name}-${index}`" class="rounded-xl border border-slate-200 bg-slate-50 p-2">
                <img v-if="activityEvidencePreviews[index]" :src="activityEvidencePreviews[index]" :alt="file.name" class="h-24 w-full rounded-lg object-cover" />
                <p class="truncate text-xs font-semibold text-slate-700 mt-2">{{ file.name }}</p>
                <button type="button" @click="removeActivityEvidence(index)" class="mt-1 text-xs font-bold text-[#8B1E23]">Remove</button>
              </div>
            </div>
          </div>
        </div>

        <div class="px-6 py-4 bg-slate-50 border-t border-slate-200 flex justify-end gap-3">
          <button type="button" @click="closeSubmissionModal" class="px-5 py-2.5 rounded-xl border border-slate-300 text-slate-700 font-bold">Cancel</button>
          <button type="button" @click="submitActivityForVerification" :disabled="!activityAccomplishment.trim()" class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white font-bold disabled:opacity-50">Submit for Verification</button>
        </div>
      </div>
    </div>

    <!-- ========================================================= -->
    <!-- SUCCESS TOAST -->
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
import {
  computed,
  onMounted,
  onBeforeUnmount,
  ref
} from 'vue'

import {
  deleteTaskActivityEvidence,
  saveTaskActivityEvidence
} from '../../utils/reportFileStorage.js'
import { resolvePersonnelName } from '../../utils/personnelName.js'


/* =========================================================
   PROPS
========================================================= */

const props = defineProps({
  currentUser: {
    type: Object,
    required: false,
    default: null
  },

  registeredUsers: {
    type: Array,
    default: () => []
  },

  ICONS: {
    type: Object,
    required: true
  }
})

const ICONS = props.ICONS

const assignedPersonnelName = activity => resolvePersonnelName(
  activity?.assignedPersonnel || activity?.assignedTo || activity?.personnel,
  props.registeredUsers,
  'Personnel unavailable'
)


/* =========================================================
   STORAGE
   IMPORTANT:
   Activities use ONLY this storage key.

   Tasks use:
   firenotify_tasks

   Do NOT mix the two.
========================================================= */

const ACTIVITY_STORAGE_KEY = 'fireNotifyActivities'


/* =========================================================
   ACTIVITY DATA
========================================================= */

const activities = ref([])


/* =========================================================
   LOAD ACTIVITIES
========================================================= */

const loadActivities = () => {

  try {

    const stored = localStorage.getItem(
      ACTIVITY_STORAGE_KEY
    )

    if (!stored) {
      activities.value = []
      return
    }

    const parsed = JSON.parse(stored)

    if (!Array.isArray(parsed)) {
      activities.value = []
      return
    }

    activities.value = parsed.map(normalizeActivity)

    refreshOverdueActivities()

  } catch (error) {

    console.error(
      'Failed to load FireNotify activities:',
      error
    )

    activities.value = []

  }

}


/* =========================================================
   NORMALIZE ACTIVITY

   Supports older Activity Management records.
========================================================= */

const normalizeActivity = (activity) => {

  return {
    ...activity,

    id:
      activity.id ??
      `ACT-${Date.now()}-${Math.random()
        .toString(36)
        .slice(2, 7)}`,

    title:
      activity.title ||
      activity.name ||
      'Untitled Activity',

    type:
      activity.type ||
      activity.activityType ||
      'Other',

    location:
      activity.location ||
      'Not specified',

    date:
      activity.date ||
      activity.activityDate ||
      '',

    time:
      activity.time ||
      activity.activityTime ||
      '',

    assignedTo:
      activity.assignedTo ||
      activity.assignedPersonnel ||
      activity.personnel ||
      'Station Personnel',

    status:
      activity.status ||
      'Scheduled',

    progress:
      Number.isFinite(Number(activity.progress))
        ? Number(activity.progress)
        : 0,

    description:
      activity.description ||
      activity.instructions ||
      '',

    createdAt:
      activity.createdAt ||
      activity.created ||
      null
  }

}


/* =========================================================
   SAVE ACTIVITIES
========================================================= */

const saveActivities = () => {

  try {

    localStorage.setItem(
      ACTIVITY_STORAGE_KEY,
      JSON.stringify(activities.value)
    )

    /*
      Custom event lets another FireNotify component
      know that Activities changed in the same tab.
    */

    window.dispatchEvent(
      new CustomEvent('fireNotifyActivitiesUpdated')
    )

  } catch (error) {

    console.error(
      'Failed to save FireNotify activities:',
      error
    )

  }

}

const notifyAdmin = activity => {
  try {
    const key = 'firenotify_notifications'
    const current = JSON.parse(localStorage.getItem(key) || '[]')
    const notification = {
      id: `notif-activity-${activity.id}-${Date.now()}`,
      title: 'Activity submitted for verification',
      detail: `${activity.title || activity.name} was submitted for verification.`,
      type: 'Activity Reminders',
      status: 'unread',
      read: false,
      createdAt: new Date().toISOString(),
      assignedToId: 'admin-default',
      activityId: activity.id
    }
    localStorage.setItem(key, JSON.stringify([notification, ...current]))
    window.dispatchEvent(new CustomEvent('fireNotifyNotificationsUpdated'))
  } catch (error) {
    console.warn('FireNotify: unable to notify admin about activity submission', error)
  }
}


/* =========================================================
   OVERDUE CHECK
========================================================= */

const refreshOverdueActivities = () => {

  let changed = false

  const today = startOfToday()

  activities.value = activities.value.map(activity => {

    if (
      !activity.date ||
      activity.status === 'Completed'
    ) {
      return activity
    }

    const activityDate = parseDate(activity.date)

    if (!activityDate) {
      return activity
    }

    if (
      activityDate < today &&
      (
        activity.status === 'Scheduled' ||
        activity.status === 'In Progress'
      )
    ) {

      changed = true

      return {
        ...activity,
        status: 'Overdue'
      }

    }

    return activity

  })

  if (changed) {
    saveActivities()
  }

}


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
const newProgress = ref(10)
const submissionActivity = ref(null)
const activityAccomplishment = ref('')
const activityRemarks = ref('')
const activityEvidenceFiles = ref([])
const activityEvidencePreviews = ref([])


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
    activity =>
      activity.status === 'Scheduled' || activity.status === 'Assigned'
  ).length

})


const completedActivities = computed(() => {

  return activities.value.filter(
    activity =>
      activity.status === 'Completed' || activity.status === 'Verified'
  ).length

})


const overdueActivities = computed(() => {

  return activities.value.filter(
    activity =>
      activity.status === 'Overdue'
  ).length

})


const pendingActivities = computed(() => {

  return activities.value.filter(
    activity =>
      activity.status === 'Scheduled' ||
      activity.status === 'Assigned' ||
      activity.status === 'In Progress' ||
      activity.status === 'For Verification' ||
      activity.status === 'Returned' ||
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
    (
      completedActivities.value /
      activities.value.length
    ) * 100
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

  const query =
    searchQuery.value
      .trim()
      .toLowerCase()

  return activities.value
    .filter(activity => {

      const searchableText = [

        activity.title,

        activity.location,

        activity.assignedTo,

        activity.type,

        activity.description

      ]
        .filter(Boolean)
        .join(' ')
        .toLowerCase()


      const matchesSearch =
        !query ||
        searchableText.includes(query)


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
    .sort(sortActivities)

})


/* =========================================================
   TODAY'S ACTIVITIES
========================================================= */

const todaysActivities = computed(() => {

  const today = startOfToday()

  return activities.value
    .filter(activity => {

      const date = parseDate(activity.date)

      if (!date) {
        return false
      }

      return (
        date.getTime() === today.getTime()
      )

    })
    .sort(sortByTime)

})


/* =========================================================
   UPCOMING ACTIVITIES
========================================================= */

const upcomingActivities = computed(() => {

  const today = startOfToday()

  return activities.value
    .filter(activity => {

      if (
        activity.status === 'Completed'
      ) {
        return false
      }

      const date = parseDate(activity.date)

      if (!date) {
        return false
      }

      return date >= today

    })
    .sort((a, b) => {

      const dateA =
        parseDate(a.date)?.getTime() ||
        Infinity

      const dateB =
        parseDate(b.date)?.getTime() ||
        Infinity

      return dateA - dateB

    })
    .slice(0, 5)

})


/* =========================================================
   TODAY LABEL
========================================================= */

const formattedToday = computed(() => {

  return new Intl.DateTimeFormat(
    'en-US',
    {
      month: 'long',
      day: 'numeric',
      year: 'numeric'
    }
  ).format(new Date())

})


/* =========================================================
   DATE HELPERS
========================================================= */

const parseDate = (value) => {

  if (!value) {
    return null
  }

  if (
    value instanceof Date
  ) {
    return new Date(
      value.getFullYear(),
      value.getMonth(),
      value.getDate()
    )
  }


  const raw = String(value).trim()


  /*
    Handles:
    YYYY-MM-DD
  */

  const isoMatch =
    raw.match(
      /^(\d{4})-(\d{2})-(\d{2})/
    )

  if (isoMatch) {

    const year =
      Number(isoMatch[1])

    const month =
      Number(isoMatch[2]) - 1

    const day =
      Number(isoMatch[3])

    return new Date(
      year,
      month,
      day
    )

  }


  /*
    Handles:
    MM/DD/YYYY
  */

  const slashMatch =
    raw.match(
      /^(\d{1,2})\/(\d{1,2})\/(\d{4})/
    )

  if (slashMatch) {

    return new Date(
      Number(slashMatch[3]),
      Number(slashMatch[1]) - 1,
      Number(slashMatch[2])
    )

  }


  /*
    Handles:
    September 12, 2026
  */

  const parsed =
    new Date(raw)

  if (!Number.isNaN(parsed.getTime())) {

    return new Date(
      parsed.getFullYear(),
      parsed.getMonth(),
      parsed.getDate()
    )

  }

  return null

}


const startOfToday = () => {

  const now = new Date()

  return new Date(
    now.getFullYear(),
    now.getMonth(),
    now.getDate()
  )

}


const formatDate = (value) => {

  if (!value) {
    return 'Not specified'
  }

  const date = parseDate(value)

  if (!date) {
    return String(value)
  }

  return new Intl.DateTimeFormat(
    'en-US',
    {
      month: 'long',
      day: 'numeric',
      year: 'numeric'
    }
  ).format(date)

}


const formatCreatedDate = (value) => {

  if (!value) {
    return '—'
  }

  const date =
    new Date(value)

  if (
    Number.isNaN(
      date.getTime()
    )
  ) {
    return '—'
  }

  return new Intl.DateTimeFormat(
    'en-US',
    {
      month: 'short',
      day: 'numeric',
      year: 'numeric'
    }
  ).format(date)

}


/* =========================================================
   DAYS UNTIL
========================================================= */

const daysUntil = (value) => {

  const date = parseDate(value)

  if (!date) {
    return ''
  }

  const today = startOfToday()

  const difference =
    date.getTime() -
    today.getTime()

  const days =
    Math.round(
      difference /
      (1000 * 60 * 60 * 24)
    )

  if (days === 0) {
    return 'Today'
  }

  if (days === 1) {
    return 'Tomorrow'
  }

  if (days < 0) {
    return 'Past'
  }

  return `${days} days`

}


/* =========================================================
   SORTING
========================================================= */

const sortActivities = (a, b) => {

  const dateA =
    parseDate(a.date)?.getTime() ||
    Infinity

  const dateB =
    parseDate(b.date)?.getTime() ||
    Infinity

  return dateA - dateB

}


const sortByTime = (a, b) => {

  const timeA =
    normalizeTimeForSort(a.time)

  const timeB =
    normalizeTimeForSort(b.time)

  return timeA - timeB

}


const normalizeTimeForSort = (time) => {

  if (!time) {
    return 9999
  }

  const raw =
    String(time)
      .trim()
      .toUpperCase()

  const match =
    raw.match(
      /^(\d{1,2})(?::(\d{2}))?\s*(AM|PM)?$/
    )

  if (!match) {
    return 9999
  }

  let hour =
    Number(match[1])

  const minute =
    Number(match[2] || 0)

  const meridiem =
    match[3]

  if (meridiem === 'PM' && hour !== 12) {
    hour += 12
  }

  if (meridiem === 'AM' && hour === 12) {
    hour = 0
  }

  return (
    hour * 60 +
    minute
  )

}


/* =========================================================
   PROGRESS
========================================================= */

const normalizedProgress = (progress) => {

  const value =
    Number(progress)

  if (Number.isNaN(value)) {
    return 0
  }

  return Math.min(
    100,
    Math.max(
      0,
      Math.round(value)
    )
  )

}


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

const startActivity = activity => {
  const item = activities.value.find(record => record.id === activity.id)
  if (!item) return

  item.status = 'In Progress'
  item.progress = Math.max(Number(item.progress || 0), 10)
  item.startedAt = item.startedAt || new Date().toISOString()
  item.updatedAt = new Date().toISOString()
  saveActivities()
  showToast('Activity started.')
}

const openSubmissionModal = activity => {
  submissionActivity.value = activity
  activityAccomplishment.value = activity.accomplishment || ''
  activityRemarks.value = activity.remarks || ''
  activityEvidenceFiles.value = []
  activityEvidencePreviews.value = []
}

const closeSubmissionModal = () => {
  submissionActivity.value = null
  activityAccomplishment.value = ''
  activityRemarks.value = ''
  activityEvidenceFiles.value = []
  activityEvidencePreviews.value.forEach(url => URL.revokeObjectURL(url))
  activityEvidencePreviews.value = []
}

const handleActivityEvidence = event => {
  const files = Array.from(event?.target?.files || [])
  const validFiles = files.filter(file =>
    /\.(jpe?g|png|webp)$/i.test(file.name) ||
    /^image\/(jpeg|png|webp)$/i.test(file.type)
  )

  if (validFiles.length !== files.length) showToast('Please select JPG, PNG, or WEBP image files only.')
  activityEvidencePreviews.value.forEach(url => URL.revokeObjectURL(url))
  activityEvidenceFiles.value = validFiles
  activityEvidencePreviews.value = validFiles.map(file => URL.createObjectURL(file))
}

const removeActivityEvidence = index => {
  const [preview] = activityEvidencePreviews.value.splice(index, 1)
  if (preview) URL.revokeObjectURL(preview)
  activityEvidenceFiles.value.splice(index, 1)
}

const submitActivityForVerification = async () => {
  if (!submissionActivity.value) return

  if (!activityAccomplishment.value.trim()) {
    showToast('Please provide an accomplishment/work summary before submitting.')
    return
  }

  const item = activities.value.find(record => record.id === submissionActivity.value.id)
  if (!item) return

  await deleteTaskActivityEvidence({
    recordId: item.id,
    recordType: 'activity'
  })

  const evidence = await saveTaskActivityEvidence({
    recordId: item.id,
    recordType: 'activity',
    files: activityEvidenceFiles.value
  })

  Object.assign(item, {
    status: 'For Verification',
    progress: 90,
    accomplishment: activityAccomplishment.value.trim(),
    remarks: activityRemarks.value.trim(),
    evidence,
    submittedAt: new Date().toISOString(),
    submittedBy: props.currentUser?.name || props.currentUser?.identifier || 'Personnel',
    updatedAt: new Date().toISOString()
  })

  saveActivities()
  closeSubmissionModal()
  notifyAdmin(item)
  showToast('Activity submitted for verification.')
}

const openStatusModal = (activity) => {

  selectedActivity.value =
    activity

  newStatus.value =
    activity.status === 'Overdue'
      ? 'In Progress'
      : activity.status

  newProgress.value =
    normalizedProgress(
      activity.progress
    ) || 10

  showStatusModal.value = true

}


const openStatusFromDetails = () => {

  if (!selectedActivity.value) {
    return
  }

  openStatusModal(
    selectedActivity.value
  )

  closeDetails()

}


const closeStatusModal = () => {

  showStatusModal.value = false

}


/* =========================================================
   SAVE STATUS
========================================================= */

const saveStatus = () => {

  if (!selectedActivity.value) {
    return
  }


  const activity =
    activities.value.find(
      item =>
        String(item.id) ===
        String(selectedActivity.value.id)
    )


  if (!activity) {

    closeStatusModal()

    return

  }


  activity.status =
    newStatus.value


  if (
    newStatus.value ===
    'Completed'
  ) {

    activity.progress = 100

    activity.completedAt =
      new Date().toISOString()

  }


  if (
    newStatus.value ===
    'In Progress'
  ) {

    activity.progress =
      Math.min(
        99,
        Math.max(
          1,
          Number(newProgress.value) || 10
        )
      )

    if (!activity.startedAt) {

      activity.startedAt =
        new Date().toISOString()

    }

  }


  if (
    newStatus.value ===
    'Scheduled'
  ) {

    activity.progress = 0

    activity.startedAt = null

    activity.completedAt = null

  }


  saveActivities()

  const title =
    activity.title


  closeStatusModal()

  showToast(
    `${title} status updated.`
  )

}


/* =========================================================
   RESOLVE OVERDUE
========================================================= */

const resolveActivity = (activity) => {

  const target =
    activities.value.find(
      item =>
        String(item.id) ===
        String(activity.id)
    )


  if (!target) {
    return
  }


  target.status =
    'In Progress'

  target.progress =
    10


  target.startedAt =
    target.startedAt ||
    new Date().toISOString()


  saveActivities()


  showToast(
    `${target.title} has been moved to In Progress.`
  )

}


/* =========================================================
   STATUS STYLING
========================================================= */

const statusClass = (status) => {

  const classes = {

    Scheduled:
      'bg-yellow-100 text-yellow-700',

    Assigned:
      'bg-slate-100 text-slate-700',

    'In Progress':
      'bg-blue-100 text-blue-700',

    Completed:
      'bg-green-100 text-green-700',

    Verified:
      'bg-green-100 text-green-700',

    'For Verification':
      'bg-purple-100 text-purple-700',

    Returned:
      'bg-yellow-100 text-yellow-700',

    Overdue:
      'bg-red-100 text-[#8B1E23]'

  }

  return (
    classes[status] ||
    'bg-slate-100 text-slate-700'
  )

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

  return (
    classes[status] ||
    'border-slate-200 bg-slate-50'
  )

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

  return (
    classes[status] ||
    'bg-slate-100 text-slate-600'
  )

}


/* =========================================================
   ACTIVITY ICON
========================================================= */

const activityIcon = (status) => {

  if (
    status === 'Completed'
  ) {
    return ICONS.check
  }


  if (
    status === 'Overdue'
  ) {
    return ICONS.siren
  }


  if (
    status === 'In Progress'
  ) {
    return ICONS.clock
  }


  return ICONS.tasks

}


/* =========================================================
   REAL-TIME STORAGE SYNC
========================================================= */

const handleStorageChange = (event) => {

  if (
    event.key ===
    ACTIVITY_STORAGE_KEY
  ) {

    loadActivities()

  }

}


const handleActivitiesUpdated = () => {

  loadActivities()

}


/* =========================================================
   POLLING
   Useful when Admin and Personnel pages are open
   in the same browser/application.
========================================================= */

let activityPoller = null

const startActivityPolling = () => {

  activityPoller =
    setInterval(() => {

      loadActivities()

    }, 1000)

}


/* =========================================================
   LIFECYCLE
========================================================= */

onMounted(() => {

  loadActivities()

  window.addEventListener(
    'storage',
    handleStorageChange
  )

  window.addEventListener(
    'fireNotifyActivitiesUpdated',
    handleActivitiesUpdated
  )

  startActivityPolling()

})


onBeforeUnmount(() => {

  window.removeEventListener(
    'storage',
    handleStorageChange
  )

  window.removeEventListener(
    'fireNotifyActivitiesUpdated',
    handleActivitiesUpdated
  )


  if (activityPoller) {

    clearInterval(
      activityPoller
    )

    activityPoller = null

  }


  if (toastTimer) {

    clearTimeout(
      toastTimer
    )

  }

})
  
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