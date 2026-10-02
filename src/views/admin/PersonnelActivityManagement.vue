```vue
<template>
  <div class="space-y-4">

    <!-- =====================================================
         HEADER
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >
      <div
        class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5"
      >
        <div>
          <p
            class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]"
          >
            Operations Management
          </p>

          <h2
            class="text-2xl font-bold text-slate-900 mt-1"
          >
            Activity Management
          </h2>

          <p class="text-base text-slate-500 mt-1">
            Create, schedule, assign, and monitor station activities.
          </p>

          <p class="text-xs text-slate-400 mt-2">
            Today:
            <span class="font-semibold text-slate-600">
              {{ formatDate(today) }}
            </span>
          </p>
        </div>

        <button
          @click="openCreateModal"
          class="px-6 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition shadow-sm"
        >
          + Create New Activity
        </button>
      </div>
    </section>


    <!-- =====================================================
         STATISTICS
    ====================================================== -->

    <section
      class="fn-operations-summary fn-operations-summary--five"
    >

      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-3xl font-bold text-slate-900">
          {{ String(todaysActivities).padStart(2, '0') }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Today's Activities
        </p>
      </div>

      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-3xl font-bold text-blue-600">
          {{ String(scheduledCount).padStart(2, '0') }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Scheduled
        </p>
      </div>

      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-3xl font-bold text-green-600">
          {{ String(completedCount).padStart(2, '0') }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Completed
        </p>
      </div>

      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-3xl font-bold text-[#8B1E23]">
          {{ String(delayedCount).padStart(2, '0') }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Delayed
        </p>
      </div>

      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-3xl font-bold text-emerald-600">
          {{ completionRate }}%
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Completion Rate
        </p>
      </div>

    </section>


    <!-- =====================================================
         SEARCH & FILTERS
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5"
    >
      <div
        class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4"
      >

        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search activity..."
          class="h-12 px-4 rounded-xl border border-slate-300 text-base focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]"
        />

        <select
          v-model="selectedType"
          class="h-12 px-4 rounded-xl border border-slate-300 text-base focus:outline-none focus:ring-2 focus:ring-red-200"
        >
          <option>All Activity Types</option>
          <option>Inspection</option>
          <option>Fire Drill</option>
          <option>Training</option>
          <option>Emergency Response</option>
        </select>

        <select
          v-model="selectedStatus"
          class="h-12 px-4 rounded-xl border border-slate-300 text-base focus:outline-none focus:ring-2 focus:ring-red-200"
        >
          <option>All Status</option>
          <option>Scheduled</option>
          <option>Ongoing</option>
          <option>Completed</option>
          <option>Delayed</option>
        </select>

        <select
          v-model="selectedPriority"
          class="h-12 px-4 rounded-xl border border-slate-300 text-base focus:outline-none focus:ring-2 focus:ring-red-200"
        >
          <option>All Priorities</option>
          <option>High</option>
          <option>Medium</option>
          <option>Low</option>
        </select>

      </div>

      <div
        v-if="hasActiveFilters"
        class="mt-4 flex justify-end"
      >
        <button
          @click="clearFilters"
          class="text-sm font-bold text-[#8B1E23] hover:underline"
        >
          Clear Filters
        </button>
      </div>
    </section>


    <!-- =====================================================
         ACTIVITY TABLE
    ====================================================== -->

    <section class="fn-operations-panel">

      <div class="fn-operations-heading">
        <div>
          <h2 class="text-base font-bold text-slate-900">
            Station Activities
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            {{ filteredActivities.length }} {{ filteredActivities.length === 1 ? 'activity' : 'activities' }} found
          </p>
        </div>
      </div>

      <div class="fn-operations-table-wrap">

        <table class="fn-operations-table">

          <thead>
            <tr
              class="border-b border-slate-200 text-xs font-bold uppercase tracking-wide text-slate-400"
            >

              <th class="pb-4 pr-5">
                Activity
              </th>

              <th class="pb-4 pr-5">
                Type
              </th>

              <th class="pb-4 pr-5">
                Assigned Personnel
              </th>

              <th class="pb-4 pr-5">
                Deadline
              </th>

              <th class="pb-4 pr-5">
                Priority
              </th>

              <th class="pb-4 pr-5">
                Status
              </th>

              <th class="pb-4 text-right">
                Actions
              </th>

            </tr>
          </thead>

          <tbody class="divide-y divide-slate-100">

            <tr
              v-for="activity in filteredActivities"
              :key="activity.id"
              class="hover:bg-slate-50 transition"
            >

              <td data-label="Activity" class="min-w-0">
                <div class="flex min-w-0 flex-col gap-1">
                  <p class="break-words text-sm font-bold leading-5 text-slate-900">{{ activity.name }}</p>
                  <p v-if="activity.description" class="break-words whitespace-pre-wrap text-xs leading-5 text-slate-500">{{ activity.description }}</p>
                  <p v-if="activity.location" class="break-words text-xs leading-5 text-slate-500">{{ activity.location }}</p>
                </div>
              </td>

              <td data-label="Type">

                <span
                  :class="getTypeClass(activity.type)"
                  class="fn-operations-badge"
                >
                  {{ activity.type }}
                </span>

              </td>

              <td data-label="Assigned Personnel" class="min-w-[220px]">

                <div
                  v-if="activity.assignedPersonnel?.length"
                  class="space-y-1.5"
                >

                  <div
                    v-for="person in activity.assignedPersonnel"
                    :key="person.id"
                    class="flex items-center gap-2"
                  >

                    <div
                      class="h-7 w-7 rounded-full bg-[#8B1E23] text-white flex items-center justify-center text-[10px] font-bold shrink-0"
                    >
                      {{ getInitials(assignedPersonnelName(person)) }}
                    </div>

                    <div class="min-w-0">

                      <p
                        class="break-words text-sm font-semibold leading-5 text-slate-700"
                      >
                        {{ assignedPersonnelName(person) }}
                      </p>

                      <p class="text-[11px] text-slate-400">
                        {{ person.rank }}
                      </p>

                    </div>

                  </div>

                </div>

                <div v-else>
                  <span class="text-sm text-slate-400">
                    No personnel assigned
                  </span>
                </div>

              </td>

              <td data-label="Schedule">
                <div class="flex flex-col gap-0.5">
                  <span class="text-sm font-semibold leading-5 text-slate-700">{{ formatDate(activity.schedule) }}</span>
                  <span class="text-xs leading-5 text-slate-500">{{ formatTime(activity.time) }}</span>
                </div>
              </td>

              <td data-label="Priority">

                <span
                  :class="getPriorityClass(activity.priority)"
                  class="fn-operations-badge"
                >
                 {{ (activity.priority || 'Medium').toUpperCase() }}
                </span>

              </td>

              <td data-label="Status">

                <span
                  :class="getStatusClass(activity.status)"
                  class="fn-operations-badge"
                >
                  {{ activity.status.toUpperCase() }}
                </span>

              </td>

              <td data-label="Actions" class="text-right">

                <div class="flex justify-end gap-2">

                  <button
                    @click="viewActivity(activity)"
                    class="fn-operations-action"
                  >
                    View
                  </button>

                  <button
                    v-if="activity.status === 'For Verification'"
                    @click="openActivitySubmission(activity)"
                    class="fn-operations-action"
                  >
                    View Submission
                  </button>

                  <button
                    @click="openEditModal(activity)"
                    class="fn-operations-action"
                  >
                    Edit
                  </button>

                  <button
                    @click="openDeleteModal(activity)"
                    class="fn-operations-action fn-operations-action--danger"
                  >
                    Delete
                  </button>

                </div>

              </td>

            </tr>

            <tr v-if="!filteredActivities.length">

              <td
                colspan="7"
                class="py-12 text-center"
              >

                <p class="font-bold text-slate-700">
                  No activities found
                </p>

                <p class="text-sm text-slate-500 mt-1">
                  Try changing your search or filters.
                </p>

              </td>

            </tr>

          </tbody>

        </table>

      </div>

    </section>


    <!-- =====================================================
         PLANNED ACTIVITIES + WORKLOAD
    ====================================================== -->

    <section
      class="grid grid-cols-1 xl:grid-cols-2 gap-6"
    >

      <!-- Planned -->

      <div
        class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
      >

        <div
          class="flex items-center justify-between border-b border-slate-200 pb-5"
        >

          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Planned Activities
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              Upcoming station schedule
            </p>
          </div>

          <span
            class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold"
          >
            {{ plannedActivities.length }}
            ITEMS
          </span>

        </div>

        <div class="mt-5 space-y-4">

          <div
            v-for="activity in plannedActivities"
            :key="activity.id"
            class="p-4 rounded-xl border border-slate-200 bg-slate-50 hover:bg-white transition"
          >

            <div class="flex justify-between gap-4">

              <div>

                <p class="font-bold text-slate-900">
                  {{ activity.name }}
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  {{ formatDate(activity.schedule) }}
                  •
                  {{ formatTime(activity.time) }}
                </p>

                <p class="text-xs text-slate-400 mt-1">
                  {{ activity.location }}
                </p>

                <p
                  v-if="activity.assignedPersonnel?.length"
                  class="text-xs text-slate-500 mt-2"
                >
                  Assigned:
                  <span class="font-semibold">
                    {{ assignedPersonnelName(activity.assignedPersonnel) }}
                  </span>
                </p>

              </div>

              <span
                :class="getStatusClass(activity.status)"
                class="h-fit px-2.5 py-1 rounded-full text-xs font-bold whitespace-nowrap"
              >
                {{ activity.status }}
              </span>

            </div>

          </div>

          <div
            v-if="!plannedActivities.length"
            class="py-8 text-center"
          >
            <p class="font-semibold text-slate-600">
              No upcoming activities
            </p>

            <p class="text-sm text-slate-400 mt-1">
              Create or schedule an activity to see it here.
            </p>
          </div>

        </div>

      </div>


      <!-- Workload -->

      <div
        class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
      >

        <div class="border-b border-slate-200 pb-5">

          <h2 class="text-xl font-bold text-slate-900">
            Workload Summary
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Activity allocation by type
          </p>

        </div>

        <div class="mt-5 space-y-5">

          <div
            v-for="item in workload"
            :key="item.type"
          >

            <div
              class="flex justify-between text-sm font-semibold text-slate-700 mb-2"
            >
              <span>
                {{ item.type }}
              </span>

              <span>
                {{ item.percentage }}%
              </span>
            </div>

            <div
              class="h-2.5 rounded-full bg-slate-100 overflow-hidden"
            >

              <div
                class="h-full rounded-full bg-[#8B1E23] transition-all duration-500"
                :style="{
                  width: `${item.percentage}%`
                }"
              ></div>

            </div>

          </div>

        </div>

      </div>

    </section>


    <!-- =====================================================
         QUICK STATUS
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div class="border-b border-slate-200 pb-5">

        <h2 class="text-xl font-bold text-slate-900">
          Activity Status Overview
        </h2>

        <p class="text-sm text-slate-500 mt-1">
          Current operational activity distribution
        </p>

      </div>

      <div
        class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-5"
      >

        <div
          class="p-4 rounded-xl bg-blue-50 border border-blue-100"
        >
          <p class="text-2xl font-bold text-blue-700">
            {{ scheduledCount }}
          </p>

          <p
            class="text-sm text-blue-700 mt-1 font-semibold"
          >
            Scheduled Activities
          </p>
        </div>

        <div
          class="p-4 rounded-xl bg-indigo-50 border border-indigo-100"
        >
          <p class="text-2xl font-bold text-indigo-700">
            {{ ongoingCount }}
          </p>

          <p
            class="text-sm text-indigo-700 mt-1 font-semibold"
          >
            Ongoing Activities
          </p>
        </div>

        <div
          class="p-4 rounded-xl bg-green-50 border border-green-100"
        >
          <p class="text-2xl font-bold text-green-700">
            {{ completedCount }}
          </p>

          <p
            class="text-sm text-green-700 mt-1 font-semibold"
          >
            Completed Activities
          </p>
        </div>

        <div
          class="p-4 rounded-xl bg-red-50 border border-red-100"
        >
          <p class="text-2xl font-bold text-[#8B1E23]">
            {{ delayedCount }}
          </p>

          <p
            class="text-sm text-[#8B1E23] mt-1 font-semibold"
          >
            Delayed Activities
          </p>
        </div>

      </div>

    </section>


    <!-- =====================================================
         ACTIVITY NOTES
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div class="border-b border-slate-200 pb-5">

        <h2 class="text-xl font-bold text-slate-900">
          Activity Notes
        </h2>

        <p class="text-sm text-slate-500 mt-1">
          Important operational reminders
        </p>

      </div>

      <div class="mt-5 space-y-4">

        <div
          class="p-4 rounded-xl border border-lime-200 bg-lime-50"
        >
          <p class="text-sm font-bold text-slate-900">
            Reminder
          </p>

          <p class="text-sm text-slate-600 mt-1">
            All inspection teams must bring updated checklist forms before deployment.
          </p>
        </div>

        <div
          class="p-4 rounded-xl border border-amber-200 bg-amber-50"
        >
          <p class="text-sm font-bold text-slate-900">
            Coordination
          </p>

          <p class="text-sm text-slate-600 mt-1">
            Coordinate with the barangay office for drill participation and crowd control support.
          </p>
        </div>

        <div
          class="p-4 rounded-xl border border-sky-200 bg-sky-50"
        >
          <p class="text-sm font-bold text-slate-900">
            Escalation
          </p>

          <p class="text-sm text-slate-600 mt-1">
            Any delay in scheduled drills must be logged and escalated to the operations section chief.
          </p>
        </div>

      </div>

    </section>


    <!-- =====================================================
         CREATE / EDIT MODAL
    ====================================================== -->

    <div
      v-if="showActivityModal"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div
        class="fn-modal-panel bg-white w-full max-w-2xl rounded-2xl shadow-xl"
      >

        <div class="p-6 border-b border-slate-200">

          <h2 class="text-xl font-bold text-slate-900">
            {{
              editingActivity
                ? 'Edit Activity'
                : 'Create New Activity'
            }}
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Enter the activity details and assign personnel below.
          </p>

        </div>


        <div class="p-6 space-y-5">

          <!-- Activity Name -->

          <div>

            <label
              class="block text-sm font-bold text-slate-700 mb-2"
            >
              Activity Name *
            </label>

            <input
              v-model="activityForm.name"
              type="text"
              placeholder="e.g. Fire Safety Inspection"
              class="w-full h-12 px-4 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]"
            />

          </div>


          <!-- Type -->

          <div>

            <label
              class="block text-sm font-bold text-slate-700 mb-2"
            >
              Activity Type
            </label>

            <select
              v-model="activityForm.type"
              class="w-full h-12 px-4 rounded-xl border border-slate-300"
            >
              <option v-for="type in activityTypes" :key="type" :value="type">
                {{ type }}
              </option>
            </select>

            <button
              v-if="!showNewActivityType"
              type="button"
              @click="showNewActivityType = true"
              class="mt-2 text-sm font-bold text-[#8B1E23] hover:underline"
            >
              + Create New Activity Type
            </button>

            <div v-else class="mt-3 flex flex-wrap items-center gap-2">
              <input
                v-model="newActivityTypeName"
                type="text"
                placeholder="New Activity Type"
                class="min-w-0 flex-1 h-10 px-3 rounded-lg border border-slate-300"
                @keyup.enter="createActivityType"
              />
              <button type="button" @click="createActivityType" class="px-3 py-2 rounded-lg bg-[#8B1E23] text-white text-sm font-bold">
                Create Type
              </button>
              <button type="button" @click="showNewActivityType = false; newActivityTypeName = ''" class="px-3 py-2 rounded-lg border border-slate-300 text-sm font-semibold">
                Cancel
              </button>
            </div>

          </div>


          <!-- =================================================
               ASSIGN PERSONNEL
          ================================================== -->

          <div>

            <div
              class="flex items-center justify-between mb-2"
            >

              <label
                class="block text-sm font-bold text-slate-700"
              >
                Assign Personnel *
              </label>

              <span
                class="text-xs font-bold text-[#8B1E23]"
              >
                {{ selectedPersonnelIds.length }}
                selected
              </span>

            </div>


            <!-- Search Personnel -->

            <input
              v-model="personnelSearch"
              type="text"
              placeholder="Search personnel..."
              class="w-full h-11 px-4 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]"
            />


            <!-- Select / Clear -->

            <div
              class="flex items-center justify-between mt-3"
            >

              <button
                type="button"
                @click="selectAllPersonnel"
                class="text-xs font-bold text-[#8B1E23] hover:underline"
              >
                Select All
              </button>

              <button
                type="button"
                @click="clearSelectedPersonnel"
                class="text-xs font-bold text-slate-500 hover:text-slate-800"
              >
                Clear
              </button>

            </div>


            <!-- Personnel List -->

            <div
              class="mt-3 border border-slate-200 rounded-xl overflow-hidden max-h-64 overflow-y-auto"
            >

              <label
                v-for="person in filteredPersonnel"
                :key="person.id"
                class="flex items-center gap-3 p-3 border-b border-slate-100 last:border-b-0 hover:bg-slate-50 cursor-pointer"
              >

                <input
                  type="checkbox"
                  :checked="
                    selectedPersonnelIds.includes(
                      person.id
                    )
                  "
                  @change="
                    togglePersonnel(person.id)
                  "
                  class="h-4 w-4 accent-[#8B1E23]"
                />


                <div
                  class="h-10 w-10 rounded-full bg-[#8B1E23] text-white flex items-center justify-center text-xs font-bold shrink-0"
                >
                  {{ getInitials(person.name) }}
                </div>


                <div class="flex-1 min-w-0">

                  <p
                    class="text-sm font-bold text-slate-800 truncate"
                  >
                    {{ person.name || 'Unnamed Personnel' }}
                  </p>

                  <p
                    class="text-xs text-slate-500"
                  >
                    {{ person.rank }}
                    •
                    {{ person.position }}
                  </p>

                </div>


                <span
                  v-if="
                    selectedPersonnelIds.includes(
                      person.id
                    )
                  "
                  class="text-xs font-bold text-green-600"
                >
                  Assigned
                </span>

              </label>


              <div
                v-if="!filteredPersonnel.length"
                class="p-6 text-center"
              >

                <p
                  class="font-semibold text-slate-600"
                >
                  No personnel found
                </p>

                <p
                  class="text-xs text-slate-400 mt-1"
                >
                  Registered personnel will appear here.
                </p>

              </div>

            </div>


            <!-- Selected Personnel -->

            <div
              v-if="selectedPersonnel.length"
              class="mt-3 p-3 rounded-xl bg-red-50 border border-red-100"
            >

              <p
                class="text-xs font-bold uppercase tracking-wide text-[#8B1E23] mb-2"
              >
                Selected Personnel
              </p>

              <div class="flex flex-wrap gap-2">

                <span
                  v-for="person in selectedPersonnel"
                  :key="person.id"
                  class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white border border-red-100 text-xs font-semibold text-slate-700"
                >

                  <span>
                    {{ person.name }}
                  </span>

                  <button
                    type="button"
                    @click="togglePersonnel(person.id)"
                    class="text-[#8B1E23] hover:text-red-700 font-bold"
                  >
                    ×
                  </button>

                </span>

              </div>

            </div>

          </div>


          <!-- Schedule + Time -->

          <div
            class="grid grid-cols-1 md:grid-cols-2 gap-4"
          >

            <div>

              <label
                class="block text-sm font-bold text-slate-700 mb-2"
              >
                Schedule *
              </label>

              <input
                v-model="activityForm.schedule"
                type="date"
                class="w-full h-12 px-4 rounded-xl border border-slate-300"
              />

            </div>


            <div>

              <label
                class="block text-sm font-bold text-slate-700 mb-2"
              >
                Time *
              </label>

              <input
                v-model="activityForm.time"
                type="time"
                class="w-full h-12 px-4 rounded-xl border border-slate-300"
              />

            </div>

          </div>


          <!-- Location -->

          <div>

            <label
              class="block text-sm font-bold text-slate-700 mb-2"
            >
              Location *
            </label>

            <input
              v-model="activityForm.location"
              type="text"
              placeholder="Activity location"
              class="w-full h-12 px-4 rounded-xl border border-slate-300"
            />

          </div>


          <!-- Description -->

          <div>

            <label
              class="block text-sm font-bold text-slate-700 mb-2"
            >
              Description
            </label>

            <textarea
              v-model="activityForm.description"
              rows="4"
              placeholder="Activity description or instructions..."
              class="w-full px-4 py-3 rounded-xl border border-slate-300 resize-none focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]"
            ></textarea>

          </div>

        </div>


        <!-- Modal Footer -->

        <div
          class="p-6 border-t border-slate-200 flex justify-end gap-3"
        >

          <button
            @click="showActivityModal = false"
            class="px-5 py-2.5 rounded-xl border border-slate-300 text-slate-700 font-bold hover:bg-slate-50"
          >
            Cancel
          </button>

          <button
            @click="saveActivity"
            class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D]"
          >
            {{
              editingActivity
                ? 'Save Changes'
                : 'Create Activity'
            }}
          </button>

        </div>

      </div>

    </div>


    <!-- =====================================================
         DETAILS MODAL
    ====================================================== -->

    <div
      v-if="
        showDetailsModal &&
        selectedActivity
      "
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div
        class="bg-white w-full max-w-xl rounded-2xl shadow-xl max-h-[90vh] overflow-y-auto"
      >

        <div
          class="p-6 border-b border-slate-200 flex justify-between"
        >

          <div>

            <h2
              class="text-xl font-bold text-slate-900 mt-1"
            >
              {{ selectedActivity.name }}
            </h2>

          </div>

          <button
            @click="showDetailsModal = false"
            class="text-slate-400 hover:text-slate-700 text-xl"
          >
            ×
          </button>

        </div>


        <div class="p-6 space-y-5">

          <div
            class="grid grid-cols-2 gap-4"
          >

            <div>

              <p
                class="text-xs text-slate-400 uppercase font-bold"
              >
                Type
              </p>

              <p
                class="font-semibold text-slate-800 mt-1"
              >
                {{ selectedActivity.type }}
              </p>

            </div>


            <div>

              <p
                class="text-xs text-slate-400 uppercase font-bold"
              >
                Personnel
              </p>

              <p
                class="font-semibold text-slate-800 mt-1"
              >
                {{ selectedActivity.personnel }}
              </p>

            </div>


            <div>

              <p
                class="text-xs text-slate-400 uppercase font-bold"
              >
                Schedule
              </p>

              <p
                class="font-semibold text-slate-800 mt-1"
              >
                {{ formatDate(selectedActivity.schedule) }}
              </p>

            </div>


            <div>

              <p
                class="text-xs text-slate-400 uppercase font-bold"
              >
                Time
              </p>

              <p
                class="font-semibold text-slate-800 mt-1"
              >
                {{ formatTime(selectedActivity.time) }}
              </p>

            </div>


            <div>

              <p
                class="text-xs text-slate-400 uppercase font-bold"
              >
                Priority
              </p>

              <span
                :class="
                  getPriorityClass(
                    selectedActivity.priority
                  )
                "
                class="inline-block px-3 py-1 rounded-full text-xs font-bold mt-1"
              >
                {{ selectedActivity.priority }}
              </span>

            </div>


            <div>

              <p
                class="text-xs text-slate-400 uppercase font-bold"
              >
                Status
              </p>

              <span
                :class="
                  getStatusClass(
                    selectedActivity.status
                  )
                "
                class="inline-block px-3 py-1 rounded-full text-xs font-bold mt-1"
              >
                {{ selectedActivity.status }}
              </span>

            </div>

          </div>


          <!-- Assigned Personnel -->

          <div>

            <p
              class="text-xs text-slate-400 uppercase font-bold"
            >
              Assigned Personnel
            </p>

            <div
              v-if="selectedActivity.assignedPersonnel?.length"
              class="mt-3 space-y-2"
            >

              <div
                v-for="person in selectedActivity.assignedPersonnel"
                :key="person.id"
                class="flex items-center gap-3 p-3 rounded-xl bg-slate-50 border border-slate-200"
              >

                <div
                  class="h-9 w-9 rounded-full bg-[#8B1E23] text-white flex items-center justify-center text-xs font-bold"
                >
                  {{ getInitials(person.name) }}
                </div>

                <div>

                  <p
                    class="text-sm font-bold text-slate-800"
                  >
                    {{ person.name }}
                  </p>

                  <p class="text-xs text-slate-500">
                    {{ person.rank }}
                    •
                    {{ person.position }}
                  </p>

                </div>

              </div>

            </div>

            <p
              v-else
              class="text-sm text-slate-400 mt-2"
            >
              No personnel assigned.
            </p>

          </div>


          <!-- Location -->

          <div>

            <p
              class="text-xs text-slate-400 uppercase font-bold"
            >
              Location
            </p>

            <p
              class="font-semibold text-slate-800 mt-1"
            >
              {{ selectedActivity.location }}
            </p>

          </div>


          <!-- Description -->

          <div>

            <p
              class="text-xs text-slate-400 uppercase font-bold"
            >
              Description
            </p>

            <p
              class="text-sm text-slate-600 mt-1"
            >
              {{
                selectedActivity.description ||
                'No description provided.'
              }}
            </p>

          </div>


          <!-- Status Actions -->

          <div class="flex flex-wrap gap-2 pt-2">

            <button
              v-if="
                selectedActivity.status === 'Scheduled' ||
                selectedActivity.status === 'Assigned'
              "
              @click="
                updateStatus(
                  selectedActivity,
                  'Ongoing'
                );
                showDetailsModal = false
              "
              class="px-4 py-2 rounded-lg bg-blue-50 text-blue-700 text-sm font-bold"
            >
              Mark Ongoing
            </button>

            <button
              v-if="selectedActivity.status === 'For Verification'"
              @click="openActivitySubmission(selectedActivity); showDetailsModal = false"
              class="px-4 py-2 rounded-lg bg-purple-50 text-purple-700 text-sm font-bold"
            >
              Review Submission
            </button>

            <button
              v-if="
                selectedActivity.status !==
                'Delayed'
              "
              @click="
                updateStatus(
                  selectedActivity,
                  'Delayed'
                );
                showDetailsModal = false
              "
              class="px-4 py-2 rounded-lg bg-red-50 text-[#8B1E23] text-sm font-bold"
            >
              Mark Delayed
            </button>

          </div>

        </div>

      </div>

    </div>


    <!-- =====================================================
         DELETE MODAL
    ====================================================== -->

    <div
      v-if="
        showDeleteModal &&
        selectedActivity
      "
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div
        class="bg-white w-full max-w-md rounded-2xl shadow-xl p-6"
      >

        <div
          class="w-12 h-12 rounded-full bg-red-50 text-[#8B1E23] flex items-center justify-center text-xl font-bold"
        >
          !
        </div>

        <h2
          class="text-xl font-bold text-slate-900 mt-4"
        >
          Delete Activity?
        </h2>

        <p
          class="text-sm text-slate-500 mt-2"
        >
          Are you sure you want to delete
          <strong>
            {{ selectedActivity.name }}
          </strong>
          ?
          This action cannot be undone.
        </p>

        <div
          class="flex justify-end gap-3 mt-6"
        >

          <button
            @click="
              showDeleteModal = false
            "
            class="px-5 py-2.5 rounded-xl border border-slate-300 font-bold text-slate-700"
          >
            Cancel
          </button>

          <button
            @click="deleteActivity"
            class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D]"
          >
            Delete Activity
          </button>

        </div>

      </div>

    </div>


    <div
      v-if="showSubmissionModal && selectedActivitySubmission"
      class="fixed inset-0 z-[65] bg-slate-900/50 flex items-center justify-center p-4"
      @click.self="showSubmissionModal = false"
    >
      <div class="fn-modal-panel w-full max-w-2xl bg-white rounded-2xl shadow-xl overflow-hidden">
        <div class="p-6 border-b border-slate-200">
          <p class="text-xs font-bold uppercase tracking-wide text-[#8B1E23]">Activity Submission</p>
          <h3 class="text-xl font-bold text-slate-900 mt-1">{{ selectedActivitySubmission.title || selectedActivitySubmission.name }}</h3>
          <p class="text-sm text-slate-500 mt-1">{{ assignedPersonnelName(selectedActivitySubmission.assignedPersonnel || selectedActivitySubmission.assignedTo || selectedActivitySubmission.personnel) }}</p>
        </div>
        <div class="p-6 space-y-5">
          <div class="flex items-center justify-between gap-3">
            <span class="px-3 py-1.5 rounded-full text-xs font-bold" :class="getStatusClass(selectedActivitySubmission.status)">{{ selectedActivitySubmission.status }}</span>
            <span class="flex flex-col gap-0.5 text-right text-xs leading-5 text-slate-500">
              <span>{{ selectedActivitySubmission.submittedAt ? formatOperationDate(selectedActivitySubmission.submittedAt) : 'Not submitted' }}</span>
              <span v-if="hasTimeValue(selectedActivitySubmission.submittedAt)">{{ formatOperationTime(selectedActivitySubmission.submittedAt) }}</span>
            </span>
          </div>
         <div>
  <p class="text-xs font-bold uppercase tracking-wide text-slate-500">
    Accomplishment / Work Summary
  </p>

  <p
    class="mt-2 rounded-xl border border-slate-200 bg-slate-50 p-4 text-sm text-slate-700 whitespace-pre-line"
  >
    {{ selectedActivitySubmission.accomplishment || 'No accomplishment provided.' }}
  </p>
</div>

<!-- EVIDENCE PHOTOS -->
<div>
  <p class="text-xs font-bold uppercase tracking-wide text-slate-500">
    Evidence Photos
  </p>

  <div
    v-if="
      selectedActivitySubmission &&
      selectedActivitySubmission.evidence &&
      selectedActivitySubmission.evidence.length > 0
    "
    class="mt-2 grid grid-cols-2 gap-3 md:grid-cols-3"
  >
    <div
      v-for="photo in selectedActivitySubmission.evidence"
      :key="photo.id"
      class="overflow-hidden rounded-xl border border-slate-200 bg-slate-50"
    >
      <img
        :src="photo.file"
        alt="Submitted evidence photo"
        class="h-40 w-full object-cover"
        @error="console.error('EVIDENCE IMAGE ERROR:', photo.file)"
        @load="console.log('EVIDENCE IMAGE LOADED:', photo.file)"
      />

      <p class="px-3 py-2 text-xs text-slate-500">
        Evidence
      </p>
    </div>
  </div>

  <p
    v-else
    class="mt-2 rounded-xl border border-dashed border-slate-300 bg-slate-50 p-4 text-sm text-slate-500"
  >
    No evidence photos submitted.
  </p>
</div>
<!-- REMARKS -->
<div v-if="selectedActivitySubmission.remarks">
  <p class="text-xs font-bold uppercase tracking-wide text-slate-500">
    Remarks
  </p>

  <p class="mt-2 text-sm text-slate-700 whitespace-pre-line">
    {{ selectedActivitySubmission.remarks }}
  </p>
</div>

<textarea
  v-model="returnNote"
  rows="3"
  placeholder="Revision note when returning the submission..."
  class="fn-form-control resize-none"
></textarea>
        </div>
        <div class="p-6 border-t border-slate-200 flex flex-wrap justify-end gap-3">
          <button type="button" @click="showSubmissionModal = false" class="px-5 py-2.5 rounded-xl border border-slate-300 text-slate-700 font-semibold">Close</button>
          <button type="button" @click="returnActivityForRevision(selectedActivitySubmission)" class="px-5 py-2.5 rounded-xl bg-yellow-600 text-white font-bold">Return for Revision</button>
          <button type="button" @click="verifyActivity(selectedActivitySubmission)" class="px-5 py-2.5 rounded-xl bg-green-600 text-white font-bold">Verify</button>
        </div>
      </div>
    </div>

    <!-- =====================================================
         TOAST
    ====================================================== -->

    <transition name="toast">

      <div
        v-if="toastMessage"
        class="fixed bottom-6 right-6 z-[60] bg-slate-900 text-white px-5 py-4 rounded-xl shadow-xl flex items-center gap-3"
      >

        <div
          :class="
            toastType === 'error'
              ? 'bg-red-500'
              : 'bg-green-500'
          "
          class="w-2 h-2 rounded-full"
        ></div>

        <p class="text-sm font-semibold">
          {{ toastMessage }}
        </p>

      </div>

    </transition>

  </div>
</template>


<script setup>

import {
  computed,
  onMounted,
  onUnmounted,
  ref,
  watch
} from 'vue'

import { getTaskActivityEvidence } from '../../utils/reportFileStorage.js'
import { resolvePersonnelName } from '../../utils/personnelName.js'
import '../../styles/operations.css'
import { formatOperationDate, formatOperationTime } from '../../utils/operationsFormat.js'
const hasTimeValue = value => /(?:T|\s)\d{1,2}:\d{2}/.test(String(value || ''))


/* =========================================================
   PROPS
========================================================= */

const props = defineProps({

  currentUser: {
    type: Object,
    default: null
  },

  /*
   * Registered users come from:
   *
   * App.vue
   *   ↓
   * AdminDashboard.vue
   *   ↓
   * ActivityManagement.vue
   */
  registeredUsers: {
    type: Array,
    default: () => []
  }

})


/* =========================================================
   STORAGE
========================================================= */

const ACTIVITY_STORAGE_KEY =
  'fireNotifyActivities'

const ACTIVITY_SYNC_EVENT =
  'fireNotifyActivitiesUpdated'


/* =========================================================
   STATE
========================================================= */

const searchQuery = ref('')

const selectedType =
  ref('All Activity Types')

const selectedStatus =
  ref('All Status')

const selectedPriority =
  ref('All Priorities')


const showActivityModal =
  ref(false)

const showDetailsModal =
  ref(false)

const showDeleteModal =
  ref(false)

const showSubmissionModal =
  ref(false)


const editingActivity =
  ref(null)

const selectedActivity =
  ref(null)

const selectedActivitySubmission = ref(null)
const submissionEvidence = ref([])
const submissionEvidenceUrls = ref([])
const returnNote = ref('')


const toastMessage =
  ref('')

const toastType =
  ref('success')


/* =========================================================
   PERSONNEL ASSIGNMENT STATE
========================================================= */

const selectedPersonnelIds =
  ref([])

const personnelSearch =
  ref('')


/* =========================================================
   ACTIVITY FORM
========================================================= */

const activityForm = ref({

  name: '',

  type: 'Inspection',

  personnel: 0,

  schedule: '',

  time: '',

  location: '',

  description: ''

})

const ACTIVITY_TYPES_KEY = 'fireNotifyActivityTypes'
const activityTypes = ref([
  'Inspection',
  'Fire Drill',
  'Training',
  'Emergency Response'
])
const showNewActivityType = ref(false)
const newActivityTypeName = ref('')

const mergeActivityTypes = values => {
  const types = [...activityTypes.value, ...values]
    .map(value => String(value || '').trim())
    .filter(Boolean)
  const uniqueTypes = [...new Map(types.map(type => [type.toLowerCase(), type])).values()]
  activityTypes.value = uniqueTypes
  localStorage.setItem(ACTIVITY_TYPES_KEY, JSON.stringify(uniqueTypes))
}

const loadSavedActivityTypes = () => {
  try {
    const saved = JSON.parse(localStorage.getItem(ACTIVITY_TYPES_KEY) || '[]')
    if (Array.isArray(saved)) mergeActivityTypes(saved)
  } catch (error) {
    console.warn('FireNotify: unable to load saved activity types', error)
  }
}

const createActivityType = () => {
  const name = newActivityTypeName.value.trim()
  if (!name) return
  const existing = activityTypes.value.find(type => type.toLowerCase() === name.toLowerCase())
  if (!existing) mergeActivityTypes([name])
  activityForm.value.type = existing || name
  newActivityTypeName.value = ''
  showNewActivityType.value = false
}


const activities =
  ref([])


/* =========================================================
   DEMO DATA
========================================================= */

const demoActivities = [

  {
    id: 'ACT-001',
    name: 'Fire Safety Inspection',
    type: 'Inspection',
    personnel: 5,
    schedule: '2026-09-09',
    time: '09:00',
    priority: 'High',
    status: 'Ongoing',
    location: 'Public Market Complex',
    description:
      'Conduct fire safety inspection and verify compliance requirements.'
  },

  {
    id: 'ACT-002',
    name: 'Community Fire Drill',
    type: 'Fire Drill',
    personnel: 8,
    schedule: '2026-09-10',
    time: '13:30',
    priority: 'Medium',
    status: 'Scheduled',
    location: 'Barangay San Isidro',
    description:
      'Community fire drill and emergency response coordination.'
  },

  {
    id: 'ACT-003',
    name: 'Station Equipment Inspection',
    type: 'Inspection',
    personnel: 4,
    schedule: '2026-09-11',
    time: '08:30',
    priority: 'Low',
    status: 'Scheduled',
    location: 'BFP Balingasag Station',
    description:
      'Inspect fire equipment and verify serviceability.'
  },

  {
    id: 'ACT-004',
    name: 'Emergency Response Training',
    type: 'Training',
    personnel: 10,
    schedule: '2026-09-14',
    time: '09:00',
    priority: 'High',
    status: 'Scheduled',
    location: 'BFP Training Room',
    description:
      'Emergency response and incident management training.'
  },

  {
    id: 'ACT-005',
    name: 'Vehicle Maintenance Check',
    type: 'Inspection',
    personnel: 3,
    schedule: '2026-09-14',
    time: '14:00',
    priority: 'Medium',
    status: 'Scheduled',
    location: 'BFP Motor Pool',
    description:
      'Routine inspection and maintenance check of response vehicles.'
  },

  {
    id: 'ACT-006',
    name: 'Barangay Rescue Coordination Drill',
    type: 'Emergency Response',
    personnel: 7,
    schedule: '2026-09-15',
    time: '13:30',
    priority: 'High',
    status: 'Scheduled',
    location: 'Barangay Coordination Center',
    description:
      'Coordinate rescue response procedures with barangay personnel.'
  },

  {
    id: 'ACT-007',
    name: 'High-rise Building Inspection',
    type: 'Inspection',
    personnel: 6,
    schedule: '2026-09-16',
    time: '08:00',
    priority: 'High',
    status: 'Scheduled',
    location: 'Municipal Commercial Building',
    description:
      'Conduct inspection of fire exits, alarms and emergency equipment.'
  },

  {
    id: 'ACT-008',
    name: 'Station Briefing',
    type: 'Training',
    personnel: 12,
    schedule: '2026-09-12',
    time: '16:00',
    priority: 'Low',
    status: 'Completed',
    location: 'BFP Balingasag Station',
    description:
      'Weekly station operations briefing.'
  },

  {
    id: 'ACT-009',
    name: 'Routine Safety Patrol',
    type: 'Emergency Response',
    personnel: 4,
    schedule: '2026-09-13',
    time: '10:00',
    priority: 'Medium',
    status: 'Delayed',
    location: 'Zone 2 Commercial Area',
    description:
      'Routine safety patrol and fire hazard monitoring.'
  }

]


/* =========================================================
   DATE
========================================================= */

const today = computed(() => {

  const now = new Date()

  const year =
    now.getFullYear()

  const month =
    String(
      now.getMonth() + 1
    ).padStart(2, '0')

  const day =
    String(
      now.getDate()
    ).padStart(2, '0')

  return `${year}-${month}-${day}`

})


/* =========================================================
   REGISTERED PERSONNEL
========================================================= */

const personnel = computed(() => {

  return props.registeredUsers

    .filter(
      user =>
        user &&
        String(user.role || '').trim().toUpperCase() === 'PERSONNEL'
    )

    .map(user => ({

      id:
        user.id,

      username:
        user.username ||
        user.identifier ||
        '',

      name:
        user.name ||
        `${user.firstName || ''} ${user.lastName || ''}`
          .trim(),

      rank:
        user.rank ||
        'FO1',

      position:
        user.position ||
        'Fire Officer',

      email:
        user.email ||
        user.identifier ||
        ''

    }))

})


/* =========================================================
   FILTERED PERSONNEL
========================================================= */

const filteredPersonnel =
  computed(() => {

    const query =
      personnelSearch.value
        .toLowerCase()
        .trim()

    if (!query) {
      return personnel.value
    }

    return personnel.value.filter(
      person => {

        const searchText = [

          person.name,

          person.username,

          person.rank,

          person.position,

          person.email

        ]
          .join(' ')
          .toLowerCase()

        return searchText.includes(query)

      }
    )

  })


/* =========================================================
   SELECTED PERSONNEL
========================================================= */

const selectedPersonnel =
  computed(() => {

    return personnel.value.filter(
      person =>
        selectedPersonnelIds.value.includes(
          person.id
        )
    )

  })


/* =========================================================
   PERSONNEL HELPERS
========================================================= */

const getInitials = name => {

  if (!name) {
    return 'P'
  }

  return name
    .split(' ')
    .filter(Boolean)
    .slice(0, 2)
    .map(
      part =>
        part.charAt(0).toUpperCase()
    )
    .join('')

}

const assignedPersonnelName = value => resolvePersonnelName(
  value,
  props.registeredUsers,
  'Personnel unavailable'
)


const togglePersonnel = personId => {

  if (!personId) {
    return
  }

  if (
    selectedPersonnelIds.value.includes(
      personId
    )
  ) {

    selectedPersonnelIds.value =
      selectedPersonnelIds.value.filter(
        id =>
          id !== personId
      )

  } else {

    selectedPersonnelIds.value = [

      ...selectedPersonnelIds.value,

      personId

    ]

  }

}


const selectAllPersonnel = () => {

  selectedPersonnelIds.value =
    personnel.value.map(
      person =>
        person.id
    )

}


const clearSelectedPersonnel = () => {

  selectedPersonnelIds.value = []

}


/* =========================================================
   CREATE ACTIVITY ID
========================================================= */

const createActivityId = () => {

  const numbers =
    activities.value

      .map(activity => {

        const match =
          String(
            activity.id || ''
          ).match(
            /^ACT-(\d+)$/
          )

        return match
          ? Number(match[1])
          : 0

      })

      .filter(
        number =>
          number > 0
      )

  const nextNumber =
    numbers.length > 0
      ? Math.max(...numbers) + 1
      : 1

  return `ACT-${String(
    nextNumber
  ).padStart(3, '0')}`

}


/* =========================================================
   NORMALIZE ACTIVITY
========================================================= */

const normalizeActivity =
  activity => {

    const assignedPersonnel =
      Array.isArray(
        activity.assignedPersonnel
      )

        ? activity.assignedPersonnel
            .map(person => ({

              id:
                person.id,

              username:
                person.username || '',

              name:
                person.name || '',

              rank:
                person.rank ||
                'FO1',

              position:
                person.position ||
                'Fire Officer',

              email:
                person.email || ''

            }))

        : []


    return {

      ...activity,

      id:
        activity.id ||
        createActivityId(),

      name:
        activity.name ||
        '',

      type:
        activity.type ||
        'Inspection',

      personnel:
        assignedPersonnel.length > 0

          ? assignedPersonnel.length

          : Math.max(
              0,
              Number(
                activity.personnel
              ) || 0
            ),

      assignedPersonnel,

      schedule:
        activity.schedule ||
        '',

      time:
        activity.time ||
        '',

      priority:
        activity.priority ||
        'Medium',

      status:
        activity.status ||
        'Scheduled',

      location:
        activity.location ||
        '',

      description:
        activity.description ||
        '',

      createdAt:
        activity.createdAt ||
        new Date().toISOString(),

      updatedAt:
        activity.updatedAt ||
        new Date().toISOString()

    }

}


/* =========================================================
   LOAD ACTIVITIES
========================================================= */

const loadActivities = () => {

  if (
    typeof window === 'undefined'
  ) {
    return
  }

  try {

    const saved =
      localStorage.getItem(
        ACTIVITY_STORAGE_KEY
      )


    if (!saved) {

      activities.value =
        demoActivities.map(
          activity =>
            normalizeActivity(
              activity
            )
        )

      saveActivities(false)

      return

    }


    const parsed =
      JSON.parse(saved)


    if (
      Array.isArray(parsed)
    ) {

      activities.value =
        parsed.map(
          activity =>
            normalizeActivity(
              activity
            )
        )

    } else {

      activities.value =
        demoActivities.map(
          activity =>
            normalizeActivity(
              activity
            )
        )

      saveActivities(false)

    }

  } catch (error) {

    console.error(
      'Failed to load activities:',
      error
    )

    activities.value =
      demoActivities.map(
        activity =>
          normalizeActivity(
            activity
          )
      )

    saveActivities(false)

  }

}


/* =========================================================
   SAVE ACTIVITIES
========================================================= */

const saveActivities =
  (
    showErrorToast = true
  ) => {

    if (
      typeof window ===
      'undefined'
    ) {
      return
    }

    try {

      localStorage.setItem(
        ACTIVITY_STORAGE_KEY,
        JSON.stringify(
          activities.value
        )
      )

      window.dispatchEvent(
        new CustomEvent(
          ACTIVITY_SYNC_EVENT
        )
      )

    } catch (error) {

      console.error(
        'Failed to save activities:',
        error
      )

      if (showErrorToast) {

        showToast(
          'Failed to save activity data.',
          'error'
        )

      }

    }

  }

const notifyPersonnel = (activity, title, detail) => {
  try {
    const key = 'firenotify_notifications'
    const current = JSON.parse(localStorage.getItem(key) || '[]')
    const notification = {
      id: `notif-activity-${activity.id}-${Date.now()}`,
      title,
      detail,
      type: 'Activity Reminders',
      status: 'unread',
      read: false,
      createdAt: new Date().toISOString(),
      assignedToId: activity.assignedPersonnel?.[0]?.id || activity.assignedToId,
      activityId: activity.id
    }
    localStorage.setItem(key, JSON.stringify([notification, ...current]))
    window.dispatchEvent(new CustomEvent('fireNotifyNotificationsUpdated'))
  } catch (error) {
    console.warn('FireNotify: unable to notify personnel about activity review', error)
  }
}


/* =========================================================
   SYNC ACTIVITIES
========================================================= */

const syncActivitiesFromStorage =
  () => {

    if (
      typeof window ===
      'undefined'
    ) {
      return
    }

    try {

      const saved =
        localStorage.getItem(
          ACTIVITY_STORAGE_KEY
        )

      if (!saved) {
        return
      }

      const parsed =
        JSON.parse(saved)

      if (
        !Array.isArray(parsed)
      ) {
        return
      }

      activities.value =
        parsed.map(
          activity =>
            normalizeActivity(
              activity
            )
        )

    } catch (error) {

      console.error(
        'Failed to sync activities:',
        error
      )

    }

  }

 const loadActivitiesFromBackend = async () => {
  try {
    // =========================================
    // LOAD ACTIVITIES
    // =========================================

    const activitiesResponse = await fetch(
      'http://127.0.0.1:8000/api/activities/'
    )

    if (!activitiesResponse.ok) {
      throw new Error(
        `Activities API HTTP ${activitiesResponse.status}`
      )
    }

    const activitiesData = await activitiesResponse.json()

    if (!Array.isArray(activitiesData)) {
      throw new Error(
        'Invalid activities response'
      )
    }

    mergeActivityTypes(activitiesData.map(activity => activity.activity_type))


    // =========================================
    // LOAD ACTIVITY SUBMISSIONS
    // =========================================

    const submissionsResponse = await fetch(
      'http://127.0.0.1:8000/api/activity-submissions/'
    )

    if (!submissionsResponse.ok) {
      throw new Error(
        `Submissions API HTTP ${submissionsResponse.status}`
      )
    }

    const submissionsData =
      await submissionsResponse.json()

    if (!Array.isArray(submissionsData)) {
      throw new Error(
        'Invalid submissions response'
      )
    }


    // =========================================
    // MERGE SUBMISSIONS INTO ACTIVITIES
    // =========================================

    activities.value = activitiesData.map(activity => {

      // Find submission belonging to this activity
      const submission =
        submissionsData.find(
          item =>
            String(item.activity) ===
            String(activity.id)
        )


      // =========================================
      // ACTIVITY STATUS
      // =========================================

      const statusMap = {
        SCHEDULED: 'Scheduled',
        ONGOING: 'Ongoing',
        COMPLETED: 'Completed',
        DELAYED: 'Delayed',
        FOR_VERIFICATION: 'For Verification',
        VERIFIED: 'Verified',
        RETURNED: 'Returned'
      }


      // =========================================
      // RETURN MERGED ACTIVITY
      // =========================================

      return {

        ...activity,

        // Existing UI fields
        name:
          activity.title || '',

        type:
          activity.activity_type ||
          'Inspection',

        priority:
          activity.priority
            ? activity.priority.charAt(0) +
              activity.priority.slice(1).toLowerCase()
            : 'Medium',

        schedule:
          activity.activity_date || '',

        time:
          activity.activity_time || '',

        assignedPersonnel:
          activity.assigned_personnel
            ? [
                personnel.value.find(
                  person =>
                    person.id ===
                    activity.assigned_personnel
                )
              ].filter(Boolean)
            : [],

        personnel:
          activity.assigned_personnel
            ? 1
            : 0,


        // =====================================
        // IMPORTANT STATUS
        // =====================================

        status:
          statusMap[activity.status] ||
          'Scheduled',


        // =====================================
        // SUBMISSION DATA
        // =====================================

        submissionId:
          submission?.id || null,

        submissionStatus:
          submission?.status || null,

        accomplishment:
          submission?.accomplishment || '',

          

        submissionRemarks:
          submission?.remarks || '',

        revisionNote:
          submission?.revision_note || '',

        submittedAt:
          submission?.submitted_at || null,

        submittedById:
          submission?.submitted_by || null,

        evidence:
          submission?.evidence || [],

        hasSubmission:
          !!submission,


          


        // =====================================
        // DATES
        // =====================================

        createdAt:
          activity.created_at,

        updatedAt:
          activity.updated_at
      }
    })


    // =========================================
    // DEBUG
    // =========================================

    console.log(
      'Activities loaded from Django:',
      activities.value
    )

    console.log(
      'Activity submissions loaded from Django:',
      submissionsData
    )

  } catch (error) {

    console.error(
      'Failed to load activities/submissions from Django:',
      error
    )

  }
}


/* =========================================================
   STORAGE EVENTS
========================================================= */

const handleStorageChange =
  event => {

    if (
      event.key ===
      ACTIVITY_STORAGE_KEY
    ) {

      syncActivitiesFromStorage()
      void loadActivitiesFromBackend()

    }

  }


const handleActivitySync =
  () => {

    syncActivitiesFromStorage()
    void loadActivitiesFromBackend()

  }


/* =========================================================
   FILTERED ACTIVITIES
========================================================= */

const filteredActivities =
  computed(() => {

    const query =
      searchQuery.value
        .toLowerCase()
        .trim()

    return activities.value.filter(
      activity => {

        const assignedNames =
          Array.isArray(
            activity.assignedPersonnel
          )
            ? activity.assignedPersonnel
                .map(
                  person =>
                    person.name
                )
                .join(' ')
            : ''

        const searchText = [

          activity.name,

          activity.id,

          activity.type,

          activity.location,

          activity.description,

          assignedNames

        ]
          .join(' ')
          .toLowerCase()


        const matchesSearch =
          !query ||
          searchText.includes(
            query
          )


        const matchesType =
          selectedType.value ===
            'All Activity Types' ||
          activity.type ===
            selectedType.value


        const matchesStatus =
          selectedStatus.value ===
            'All Status' ||
          activity.status ===
            selectedStatus.value


        const matchesPriority =
          selectedPriority.value ===
            'All Priorities' ||
          activity.priority ===
            selectedPriority.value


        return (
          matchesSearch &&
          matchesType &&
          matchesStatus &&
          matchesPriority
        )

      }
    )

  })


/* =========================================================
   STATISTICS
========================================================= */

const todaysActivities =
  computed(() =>
    activities.value.filter(
      activity =>
        activity.schedule ===
        today.value
    ).length
  )


const scheduledCount =
  computed(() =>
    activities.value.filter(
      activity =>
        activity.status ===
        'Scheduled'
    ).length
  )


const completedCount =
  computed(() =>
    activities.value.filter(
      activity =>
        activity.status ===
        'Completed'
    ).length
  )


const delayedCount =
  computed(() =>
    activities.value.filter(
      activity =>
        activity.status ===
        'Delayed'
    ).length
  )


const ongoingCount =
  computed(() =>
    activities.value.filter(
      activity =>
        activity.status ===
        'Ongoing'
    ).length
  )


const completionRate =
  computed(() => {

    if (
      !activities.value.length
    ) {
      return 0
    }

    return Math.round(

      (
        completedCount.value /
        activities.value.length
      ) * 100

    )

  })

  /* =========================================================
   COMPLIANCE / DEADLINE
========================================================= */

const overdueCount = computed(() => {
  const todayDate = new Date(`${today.value}T23:59:59`)

  return activities.value.filter(activity => {
    if (!activity.schedule) return false

    const activityDate =
      new Date(`${activity.schedule}T23:59:59`)

    const isPastDeadline =
      activityDate < todayDate

    const isFinished =
      [
        'Completed',
        'Verified'
      ].includes(activity.status)

    return isPastDeadline && !isFinished
  }).length
})


const forVerificationCount = computed(() =>
  activities.value.filter(
    activity =>
      activity.status ===
      'For Verification'
  ).length
)


const verifiedCount = computed(() =>
  activities.value.filter(
    activity =>
      activity.status ===
      'Verified'
  ).length
)


const returnedCount = computed(() =>
  activities.value.filter(
    activity =>
      activity.status ===
      'Returned'
  ).length
)


const complianceRate = computed(() => {
  const total = activities.value.length

  if (!total) return 0

  const compliant =
    activities.value.filter(
      activity =>
        [
          'Completed',
          'Verified'
        ].includes(activity.status)
    ).length

  return Math.round(
    (compliant / total) * 100
  )
})


/* =========================================================
   WORKLOAD
========================================================= */

const workload =
  computed(() => {

    const total =
      activities.value.length ||
      1

    const types = [

      'Inspection',

      'Fire Drill',

      'Training',

      'Emergency Response'

    ]

    return types.map(
      type => {

        const count =
          activities.value.filter(
            activity =>
              activity.type ===
              type
          ).length

        return {

          type,

          count,

          percentage:
            Math.round(
              (count / total) *
              100
            )

        }

      }
    )

  })


/* =========================================================
   UPCOMING ACTIVITIES
========================================================= */

const plannedActivities =
  computed(() => {

    return activities.value

      .filter(activity => {

        const validStatus =
          [
            'Scheduled',
            'Ongoing'
          ].includes(
            activity.status
          )

        const isUpcoming =
          activity.schedule >=
          today.value

        const isOngoing =
          activity.status ===
          'Ongoing'

        return (
          validStatus &&
          (
            isUpcoming ||
            isOngoing
          )
        )

      })

      .sort((a, b) => {

        const dateA =
          `${a.schedule} ${
            a.time || '00:00'
          }`

        const dateB =
          `${b.schedule} ${
            b.time || '00:00'
          }`

        return dateA.localeCompare(
          dateB
        )

      })

      .slice(0, 5)

  })


/* =========================================================
   RESET FORM
========================================================= */

const resetActivityForm =
  () => {

    activityForm.value = {

      name: '',

      type: 'Inspection',

      personnel: 0,

      schedule: '',

      time: '',

      location: '',

      description: ''

    }

    selectedPersonnelIds.value = []

    personnelSearch.value = ''

  }


/* =========================================================
   CREATE MODAL
========================================================= */

const openCreateModal =
  () => {

    editingActivity.value =
      null

    resetActivityForm()

    showActivityModal.value =
      true

  }


/* =========================================================
   EDIT MODAL
========================================================= */

const openEditModal =
  activity => {

    editingActivity.value =
      activity


    activityForm.value = {

      name:
        activity.name ||
        '',

      type:
        activity.type ||
        'Inspection',

      personnel:
        Array.isArray(
          activity.assignedPersonnel
        )
          ? activity.assignedPersonnel
              .length
          : Number(
              activity.personnel
            ) || 0,

      schedule:
        activity.schedule ||
        '',

      time:
        activity.time ||
        '',

      location:
        activity.location ||
        '',

      description:
        activity.description ||
        ''

    }


    selectedPersonnelIds.value =
      Array.isArray(
        activity.assignedPersonnel
      )

        ? activity.assignedPersonnel
            .map(
              person =>
                person.id
            )
            .filter(Boolean)

        : []


    personnelSearch.value =
      ''

    showActivityModal.value =
      true

  }


/* =========================================================
   VIEW
========================================================= */

const viewActivity =
  activity => {

    selectedActivity.value =
      activity

    showDetailsModal.value =
      true

  }


/* =========================================================
   DELETE MODAL
========================================================= */

const openDeleteModal =
  activity => {

    selectedActivity.value =
      activity

    showDeleteModal.value =
      true

  }


/* =========================================================
   CREATE / UPDATE ACTIVITY
========================================================= */

const saveActivity =
  async () => {

    const form =
      activityForm.value


    if (
      !form.name.trim() ||
      !form.schedule ||
      !form.time ||
      !form.location.trim()
    ) {

      showToast(
        'Please complete all required fields.',
        'error'
      )

      return

    }


    if (
      selectedPersonnelIds.value
        .length === 0
    ) {

      showToast(
        'Please assign at least one personnel.',
        'error'
      )

      return

    }


    const assignedPersonnel =
      personnel.value

        .filter(
          person =>
            selectedPersonnelIds.value
              .includes(
                person.id
              )
        )

        .map(person => ({

          id:
            person.id,

          username:
            person.username,

          name:
            person.name,

          rank:
            person.rank,

          position:
            person.position,

          email:
            person.email

        }))


    const now =
      new Date().toISOString()

    const API_URL =
  'http://127.0.0.1:8000/api'


    /* =====================================================
       UPDATE
    ====================================================== */

    if (
  editingActivity.value
) {

  try {

    const activityId =
      editingActivity.value.id

    const response =
      await fetch(
        `${API_URL}/activities/${activityId}/`,
        {
          method: 'PATCH',

          headers: {
            'Content-Type': 'application/json'
          },

          body: JSON.stringify({

            activity_type:
            form.type || '',

            title:
              form.name.trim(),

            description:
              form.description || '',

            activity_date:
              form.schedule,

            activity_time:
              form.time,

            location:
              form.location.trim(),

            assigned_personnel:
              assignedPersonnel[0]?.id || null,

          })
        }
      )


    const data =
      await response.json()


    if (!response.ok) {

      console.error(
        'Django activity update failed:',
        data
      )

      showToast(
        data.detail ||
        data.error ||
        'Failed to update activity.',
        'error'
      )

      return

    }


    console.log(
      'Activity successfully updated in Django:',
      data
    )


    const index =
      activities.value.findIndex(
        activity =>
          activity.id ===
          activityId
      )


    if (index !== -1) {

      activities.value[index] =
        normalizeActivity({

          ...activities.value[index],

          ...form,

          id:
            data.id,

          personnel:
            assignedPersonnel.length,

          assignedPersonnel,

          updatedAt:
            data.updated_at ||
            now

        })

    }


    showToast(
      'Activity updated successfully.'
    )


  } catch (error) {

    console.error(
      'Django activity update error:',
      error
    )

    showToast(
      'Unable to connect to Django server.',
      'error'
    )

    return

  }

}


    /* =====================================================
       CREATE
    ====================================================== */

   else {

  try {

    const response = await fetch(
      `${API_URL}/activities/`,
      {
        method: 'POST',

        headers: {
          'Content-Type': 'application/json'
        },

        body: JSON.stringify({
          title: form.name.trim(),


          activity_type:
          form.type || '',

          priority: 'MEDIUM',

          description:
            form.description || '',

          activity_date:
            form.schedule,

          activity_time:
            form.time,

          location:
            form.location.trim(),

          assigned_personnel:
            assignedPersonnel[0]?.id || null,

          status: 'SCHEDULED',

          created_by:
            props.currentUser?.id || null
        })
      }
    )


    const data =
      await response.json()


    if (!response.ok) {

      console.error(
        'Django activity creation failed:',
        data
      )

      showToast(
        data.detail ||
        data.error ||
        'Failed to create activity.',
        'error'
      )

      return

    }


    console.log(
      'Activity successfully saved to Django:',
      data
    )


    const newActivity =
      normalizeActivity({

        id:
          data.id,

        ...form,

        personnel:
          assignedPersonnel.length,

        assignedPersonnel,

        status: 'Scheduled',

        createdAt:
          data.created_at ||
          now,

        updatedAt:
          data.updated_at ||
          now

      })


    activities.value.unshift(
      newActivity
    )


    showToast(
      'Activity created and saved successfully.'
    )


  } catch (error) {

    console.error(
      'Django activity creation error:',
      error
    )

    showToast(
      'Unable to connect to Django server.',
      'error'
    )

    return

  }

}


    saveActivities()


    showActivityModal.value =
      false

    editingActivity.value =
      null

    selectedPersonnelIds.value =
      []

    personnelSearch.value =
      ''

  }


/* =========================================================
   DELETE ACTIVITY
========================================================= */

const deleteActivity = async () => {
  if (!selectedActivity.value) return

  const activityId = selectedActivity.value.id

  try {
    const response = await fetch(
  `http://127.0.0.1:8000/api/activities/${activityId}/`,
  {
    method: 'DELETE'
  }
)

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`)
    }

    activities.value =
      activities.value.filter(
        activity => activity.id !== activityId
      )

    saveActivities(false)

    showDeleteModal.value = false
    selectedActivity.value = null

    showToast(
      'Activity deleted successfully.'
    )

  } catch (error) {
    console.error(
      'Failed to delete activity:',
      error
    )

    showToast(
      'Failed to delete activity.',
      'error'
    )
  }
}


/* =========================================================
   STATUS
========================================================= */

const updateStatus =
  (
    activity,
    status
  ) => {

    if (!activity) {
      return
    }


    const index =
      activities.value.findIndex(
        item =>
          item.id ===
          activity.id
      )


    if (index === -1) {
      return
    }


    activities.value[index] =
      normalizeActivity({

        ...activities.value[index],

        status,

        updatedAt:
          new Date().toISOString()

      })


    saveActivities()


    showToast(
      `Activity marked as ${status}.`
    )

  }

const openActivitySubmission = async activity => {
  selectedActivitySubmission.value = activity
  returnNote.value = ''
  submissionEvidenceUrls.value.forEach(url => URL.revokeObjectURL(url))
  submissionEvidence.value = await getTaskActivityEvidence({
    recordId: activity.id,
    recordType: 'activity'
  })
  submissionEvidenceUrls.value = submissionEvidence.value.map(item => URL.createObjectURL(item.file))
  showSubmissionModal.value = true
}

const verifyActivity = async activity => {
  if (!activity?.id) return

  try {
    const submissionId =
      activity.submissionId ||
      selectedActivitySubmission.value?.id

    if (!submissionId) {
      throw new Error('Submission ID not found.')
    }

    // 1. Verify the submission in Django
    const submissionResponse = await fetch(
      `http://127.0.0.1:8000/api/activity-submissions/${submissionId}/`,
      {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          status: 'VERIFIED'
        })
      }
    )

    if (!submissionResponse.ok) {
      const errorData = await submissionResponse.json().catch(() => ({}))

      throw new Error(
        errorData?.detail ||
        errorData?.error ||
        `Submission verification failed: HTTP ${submissionResponse.status}`
      )
    }

    const updatedSubmission =
      await submissionResponse.json()

    // 2. Verify the activity itself in Django
    const activityResponse = await fetch(
      `http://127.0.0.1:8000/api/activities/${activity.id}/`,
      {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          status: 'VERIFIED'
        })
      }
    )

    if (!activityResponse.ok) {
      const errorData = await activityResponse.json().catch(() => ({}))

      throw new Error(
        errorData?.detail ||
        errorData?.error ||
        `Activity verification failed: HTTP ${activityResponse.status}`
      )
    }

    const updatedActivity =
      await activityResponse.json()

    // 3. Update frontend state
    const item = activities.value.find(
      record =>
        String(record.id) ===
        String(activity.id)
    )

    if (item) {
      Object.assign(item, {
        ...updatedActivity,
        status: 'Verified',
        submissionId:
          updatedSubmission.id ||
          submissionId,
        submissionStatus:
          updatedSubmission.status ||
          'VERIFIED',
        accomplishment:
          updatedSubmission.accomplishment ||
          item.accomplishment ||
          '',
        submissionRemarks:
          updatedSubmission.remarks ||
          item.submissionRemarks ||
          '',
        revisionNote:
          updatedSubmission.revision_note ||
          '',
        submittedAt:
          updatedSubmission.submitted_at ||
          item.submittedAt ||
          null,
        updatedAt:
          updatedActivity.updated_at ||
          new Date().toISOString()
      })
    }

    saveActivities(false)

    showSubmissionModal.value = false

    submissionEvidenceUrls.value.forEach(
      url => URL.revokeObjectURL(url)
    )

    submissionEvidenceUrls.value = []

    notifyPersonnel(
      activity,
      'Your activity has been verified',
      `${activity.title || activity.name} was verified by Admin.`
    )

    showToast(
      'Activity submission verified successfully.'
    )
  } catch (error) {
    console.error(
      'Failed to verify activity:',
      error
    )

    showToast(
      error.message ||
      'Failed to verify activity.',
      'error'
    )
  }
}

  

const returnActivityForRevision = async activity => {
  const note = returnNote.value.trim()

  if (!note) {
    showToast(
      'Please provide a revision note.',
      'error'
    )
    return
  }

  const item = activities.value.find(
    record =>
      String(record.id) ===
      String(activity.id)
  )

  if (!item) {
    showToast(
      'Activity not found.',
      'error'
    )
    return
  }

  try {
    // ==========================================
    // 1. FIND SUBMISSION ID
    // ==========================================
    const submissionId =
      item.submissionId ||
      selectedActivitySubmission.value?.id

    if (!submissionId) {
      throw new Error(
        'Submission ID not found.'
      )
    }

    // ==========================================
    // 2. SAVE RETURN STATUS TO DJANGO
    // ==========================================
    const submissionResponse =
      await fetch(
        `http://127.0.0.1:8000/api/activity-submissions/${submissionId}/`,
        {
          method: 'PATCH',
          headers: {
            'Content-Type':
              'application/json'
          },
          body: JSON.stringify({
            status: 'RETURNED',
            revision_note: note
          })
        }
      )

    if (!submissionResponse.ok) {
      const errorData =
        await submissionResponse
          .json()
          .catch(() => ({}))

      throw new Error(
        errorData?.detail ||
        errorData?.error ||
        `Return failed: HTTP ${submissionResponse.status}`
      )
    }

    const updatedSubmission =
      await submissionResponse.json()

    // ==========================================
    // 3. UPDATE ACTIVITY STATUS IN DJANGO
    // ==========================================
    const activityResponse =
      await fetch(
        `http://127.0.0.1:8000/api/activities/${activity.id}/`,
        {
          method: 'PATCH',
          headers: {
            'Content-Type':
              'application/json'
          },
          body: JSON.stringify({
            status: 'RETURNED'
          })
        }
      )

    if (!activityResponse.ok) {
      const errorData =
        await activityResponse
          .json()
          .catch(() => ({}))

      throw new Error(
        errorData?.detail ||
        errorData?.error ||
        `Activity return failed: HTTP ${activityResponse.status}`
      )
    }

    const updatedActivity =
      await activityResponse.json()

    // ==========================================
    // 4. UPDATE FRONTEND
    // ==========================================
    Object.assign(item, {
      ...updatedActivity,

      status: 'Returned',

      submissionId:
        updatedSubmission.id ||
        submissionId,

      submissionStatus:
        updatedSubmission.status ||
        'RETURNED',

      revisionNote:
        updatedSubmission.revision_note ||
        note,

      updatedAt:
        updatedActivity.updated_at ||
        new Date().toISOString()
    })

    // ==========================================
    // 5. OPTIONAL LOCAL CACHE UPDATE
    // ==========================================
    saveActivities(false)

    // ==========================================
    // 6. CLOSE MODAL / CLEAN EVIDENCE URLS
    // ==========================================
    showSubmissionModal.value = false

    submissionEvidenceUrls.value.forEach(
      url =>
        URL.revokeObjectURL(url)
    )

    submissionEvidenceUrls.value = []

    // ==========================================
    // 7. NOTIFY PERSONNEL
    // ==========================================
    notifyPersonnel(
      activity,
      'Your activity requires revision',
      `${activity.title || activity.name}: ${note}`
    )

    showToast(
      'Activity returned for revision.'
    )

  } catch (error) {
    console.error(
      'Failed to return activity:',
      error
    )

    showToast(
      error.message ||
      'Failed to return activity.',
      'error'
    )
  }
}
const openEvidence = item => {
  if (!item?.file) return
  const url = URL.createObjectURL(item.file)
  const preview = window.open(url, '_blank')
  if (!preview) window.location.href = url
  setTimeout(() => URL.revokeObjectURL(url), 15000)
}


/* =========================================================
   FILTERS
========================================================= */

const clearFilters =
  () => {

    searchQuery.value =
      ''

    selectedType.value =
      'All Activity Types'

    selectedStatus.value =
      'All Status'

    selectedPriority.value =
      'All Priorities'

  }


const hasActiveFilters =
  computed(() =>
    searchQuery.value ||

    selectedType.value !==
      'All Activity Types' ||

    selectedStatus.value !==
      'All Status' ||

    selectedPriority.value !==
      'All Priorities'
  )


/* =========================================================
   TOAST
========================================================= */

const showToast =
  (
    message,
    type = 'success'
  ) => {

    toastMessage.value =
      message

    toastType.value =
      type


    setTimeout(() => {

      toastMessage.value =
        ''

    }, 3000)

  }


/* =========================================================
   FORMATTERS
========================================================= */

const formatDate =
  date => {
    return formatOperationDate(date)
  }


const formatTime =
  time => {
    return formatOperationTime(time)
  }


/* =========================================================
   BADGES
========================================================= */

const getPriorityClass =
  priority => {

    const classes = {

      High:
        'bg-red-50 text-[#8B1E23]',

      Medium:
        'bg-yellow-50 text-yellow-700',

      Low:
        'bg-green-50 text-green-700'

    }


    return (
      classes[priority] ||
      'bg-slate-100 text-slate-600'
    )

  }


const getStatusClass =
  status => {

    const classes = {

      Scheduled:
        'bg-yellow-50 text-yellow-700',

      Assigned:
        'bg-slate-100 text-slate-700',

      Ongoing:
        'bg-blue-50 text-blue-700',

      Completed:
        'bg-green-50 text-green-700',

      Verified:
        'bg-green-50 text-green-700',

      'For Verification':
        'bg-purple-50 text-purple-700',

      Returned:
        'bg-yellow-50 text-yellow-700',

      Delayed:
        'bg-red-50 text-[#8B1E23]'

    }


    return (
      classes[status] ||
      'bg-slate-100 text-slate-600'
    )

  }


const getTypeClass =
  type => {

    const classes = {

      Inspection:
        'bg-purple-50 text-purple-700',

      'Fire Drill':
        'bg-orange-50 text-orange-700',

      Training:
        'bg-green-50 text-green-700',

      'Emergency Response':
        'bg-blue-50 text-blue-700'

    }


    return (
      classes[type] ||
      'bg-slate-100 text-slate-600'
    )

  }

onMounted(async () => {

  loadSavedActivityTypes()
  await loadActivitiesFromBackend()

  window.addEventListener(
    'storage',
    handleStorageChange
  )

  window.addEventListener(
    ACTIVITY_SYNC_EVENT,
    handleActivitySync
  )

})


onUnmounted(() => {

  window.removeEventListener(
    'storage',
    handleStorageChange
  )


  window.removeEventListener(
    ACTIVITY_SYNC_EVENT,
    handleActivitySync
  )

})

</script>


<style scoped>

.toast-enter-active,
.toast-leave-active {
  transition:
    all 0.25s ease;
}

.toast-enter-from,
.toast-leave-to {
  opacity: 0;

  transform:
    translateY(10px);
}

</style>
```
