<template>
  <div class="w-full min-w-0 space-y-6">

    <!-- ===================================================== -->
    <!-- PAGE HEADER -->
    <!-- ===================================================== -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">
        <div>
          <p class="text-sm font-semibold text-[#8B1E23]">
            FIRENOTIFY PERSONNEL PORTAL
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Station Duty Log
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Track duty assignments, shift attendance, and station activities.
          </p>
        </div>

        <button
          @click="openAddModal"
          class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D] transition shadow-sm"
        >
          + Add Duty Entry
        </button>
      </div>
    </section>


    <!-- ===================================================== -->
    <!-- STATISTICS -->
    <!-- ===================================================== -->
    <section class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-5">

      <!-- Duty Days -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-sm text-slate-500">
          Duty Days This Month
        </p>

        <p class="text-3xl font-bold text-slate-900 mt-2">
          {{ dutyDays }}
        </p>

        <p class="text-xs text-green-600 font-semibold mt-2">
          {{ dutyDays >= 22 ? 'On schedule' : 'Below schedule' }}
        </p>
      </div>


      <!-- Hours -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-sm text-slate-500">
          Hours Completed
        </p>

        <p class="text-3xl font-bold text-blue-600 mt-2">
          {{ hoursCompleted }}
        </p>

        <p class="text-xs text-slate-400 mt-2">
          Of {{ scheduledHours }} scheduled hours
        </p>
      </div>


      <!-- Activities -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-sm text-slate-500">
          Activities Logged
        </p>

        <p class="text-3xl font-bold text-green-600 mt-2">
          {{ activitiesLogged }}
        </p>

        <p class="text-xs text-slate-400 mt-2">
          This month
        </p>
      </div>


      <!-- Pending -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-sm text-slate-500">
          Pending Entries
        </p>

        <p class="text-3xl font-bold text-[#8B1E23] mt-2">
          {{ pendingCount.toString().padStart(2, '0') }}
        </p>

        <p
          class="text-xs font-semibold mt-2"
          :class="pendingCount > 0 ? 'text-red-600' : 'text-green-600'"
        >
          {{ pendingCount > 0 ? 'Needs completion' : 'All entries complete' }}
        </p>
      </div>

    </section>


    <!-- ===================================================== -->
    <!-- FILTERS -->
    <!-- ===================================================== -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

      <div class="flex flex-col lg:flex-row lg:items-end gap-4">

        <!-- Date Range -->
        <div class="flex-1">
          <label class="text-sm font-semibold text-slate-700">
            Date Range
          </label>

          <select
            v-model="dateRange"
            class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm text-slate-700 outline-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
          >
            <option>This Month</option>
            <option>This Week</option>
            <option>Last Month</option>
            <option>All Records</option>
          </select>
        </div>


        <!-- Status -->
        <div class="flex-1">
          <label class="text-sm font-semibold text-slate-700">
            Duty Status
          </label>

          <select
            v-model="statusFilter"
            class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm text-slate-700 outline-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
          >
            <option>All Statuses</option>
            <option>Completed</option>
            <option>Verified</option>
            <option>Pending Review</option>
            <option>Archived</option>
          </select>
        </div>


        <!-- Search -->
        <div class="flex-1">
          <label class="text-sm font-semibold text-slate-700">
            Search Entries
          </label>

          <div class="relative mt-2">
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Search duty logs..."
              class="w-full px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm outline-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
            />

            <button
              v-if="searchQuery"
              @click="searchQuery = ''"
              class="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-700"
            >
              ✕
            </button>
          </div>
        </div>


        <!-- Clear -->
        <button
          v-if="hasActiveFilters"
          @click="clearFilters"
          class="px-5 py-3 rounded-xl border border-slate-300 bg-white text-sm font-semibold text-slate-700 hover:bg-slate-100 transition"
        >
          Clear
        </button>

      </div>

    </section>


    <!-- ===================================================== -->
    <!-- LOG + SIDE PANEL -->
    <!-- ===================================================== -->
    <section class="grid grid-cols-1 xl:grid-cols-3 gap-6">

      <!-- =================================================== -->
      <!-- DUTY LOG -->
      <!-- =================================================== -->
      <div class="xl:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 border-b border-slate-200 pb-4">

          <div>
            <h3 class="text-lg font-bold text-slate-900">
              Duty Log Entries
            </h3>

            <p class="text-sm text-slate-500 mt-1">
              Recent attendance and station duty records
            </p>
          </div>

          <span class="w-fit px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">
            {{ filteredEntries.length }} Records
          </span>

        </div>


        <!-- Empty State -->
        <div
          v-if="filteredEntries.length === 0"
          class="py-14 text-center"
        >
          <div class="mx-auto h-14 w-14 rounded-2xl bg-slate-100 flex items-center justify-center text-2xl">
            📋
          </div>

          <h4 class="text-base font-bold text-slate-900 mt-4">
            No duty entries found
          </h4>

          <p class="text-sm text-slate-500 mt-1">
            Try changing your filters or add a new duty entry.
          </p>

          <button
            @click="openAddModal"
            class="mt-4 px-4 py-2.5 rounded-xl bg-[#8B1E23] text-white text-sm font-bold"
          >
            Add Duty Entry
          </button>
        </div>


        <!-- Entries -->
        <div v-else class="mt-5 space-y-4">

          <article
            v-for="entry in filteredEntries"
            :key="entry.id"
            class="p-5 rounded-xl border transition hover:shadow-sm"
            :class="getEntryContainerClass(entry.status)"
          >

            <div class="flex flex-col lg:flex-row lg:items-start lg:justify-between gap-4">

              <div class="flex gap-4 min-w-0">

                <!-- Icon -->
                <div
                  class="h-11 w-11 rounded-xl flex items-center justify-center shrink-0"
                  :class="getEntryIconBackground(entry.status)"
                >
                  <span
                    v-html="entry.status === 'Completed' ? ICONS.check : ICONS.clock"
                    class="h-5 w-5"
                    :class="getEntryIconColor(entry.status)"
                  ></span>
                </div>


                <!-- Details -->
                <div class="min-w-0">

                  <p class="text-base font-bold text-slate-900">
                    {{ entry.title }}
                  </p>

                  <p class="text-sm text-slate-500 mt-1">
                    {{ formatDate(entry.date) }} · {{ entry.location }}
                  </p>

                  <p class="text-sm text-slate-500 mt-1">
                    Shift: {{ entry.startTime }} - {{ entry.endTime }}
                  </p>

                  <p class="text-sm text-slate-500 mt-1">
                    {{ entry.description }}
                  </p>

                  <p
                    v-if="entry.loggedBy"
                    class="text-xs text-slate-400 mt-2"
                  >
                    Logged by {{ entry.loggedBy }}
                  </p>

                </div>

              </div>


              <!-- Status -->
              <span
                class="w-fit shrink-0 px-3 py-1.5 rounded-full text-xs font-bold"
                :class="getStatusClass(entry.status)"
              >
                {{ entry.status }}
              </span>

            </div>


            <!-- Actions -->
            <div class="flex flex-wrap gap-2 mt-4 pt-4 border-t border-black/5">

              <button
                @click="viewEntry(entry)"
                class="px-3 py-2 rounded-lg bg-white border border-slate-200 text-xs font-semibold text-slate-700 hover:bg-slate-100 transition"
              >
                View Details
              </button>

              <button
                @click="editEntry(entry)"
                class="px-3 py-2 rounded-lg bg-white border border-slate-200 text-xs font-semibold text-slate-700 hover:bg-slate-100 transition"
              >
                Edit
              </button>

              <button
                v-if="entry.status === 'Pending Review'"
                @click="markCompleted(entry)"
                class="px-3 py-2 rounded-lg bg-green-600 text-white text-xs font-bold hover:bg-green-700 transition"
              >
                Mark Complete
              </button>

              <button
                @click="deleteEntry(entry.id)"
                class="px-3 py-2 rounded-lg bg-white border border-red-200 text-xs font-semibold text-red-600 hover:bg-red-50 transition"
              >
                Delete
              </button>

            </div>

          </article>

        </div>

      </div>


      <!-- =================================================== -->
      <!-- RIGHT SIDE -->
      <!-- =================================================== -->
      <div class="space-y-6">

        <!-- Current Shift -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <div class="flex items-center justify-between">
            <h3 class="text-lg font-bold text-slate-900">
              Current Shift
            </h3>

            <span
              class="h-2.5 w-2.5 rounded-full"
              :class="currentShiftActive ? 'bg-green-500' : 'bg-slate-300'"
            ></span>
          </div>


          <div
            class="mt-5 p-5 rounded-xl border"
            :class="currentShiftActive
              ? 'bg-green-50 border-green-100'
              : 'bg-slate-50 border-slate-200'"
          >

            <div class="flex items-center gap-3">

              <div
                class="h-3 w-3 rounded-full"
                :class="currentShiftActive ? 'bg-green-500' : 'bg-slate-400'"
              ></div>

              <p
                class="font-bold"
                :class="currentShiftActive ? 'text-green-700' : 'text-slate-700'"
              >
                {{ currentShiftActive ? 'Currently On Duty' : 'Off Duty' }}
              </p>

            </div>

            <p class="text-sm text-slate-500 mt-3">
              Station 1 · BFP Balingasag
            </p>

            <p class="text-sm text-slate-500 mt-1">
              08:00 AM - 05:00 PM
            </p>

            <p class="text-xs text-slate-400 mt-3">
              {{ currentShiftActive ? 'Started today at 08:00 AM' : 'No active shift recorded' }}
            </p>

          </div>

        </div>


        <!-- Attendance Summary -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <h3 class="text-lg font-bold text-slate-900">
            Attendance Summary
          </h3>

          <div class="mt-5 space-y-5">

            <!-- Present -->
            <div>

              <div class="flex justify-between text-sm">
                <span class="text-slate-500">
                  Present
                </span>

                <span class="font-bold text-green-600">
                  {{ presentDays }} days
                </span>
              </div>

              <div class="h-2 mt-2 rounded-full bg-slate-200 overflow-hidden">
                <div
                  class="h-full rounded-full bg-green-500 transition-all"
                  :style="{ width: `${presentPercentage}%` }"
                ></div>
              </div>

            </div>


            <!-- Leave -->
            <div>

              <div class="flex justify-between text-sm">
                <span class="text-slate-500">
                  Leave
                </span>

                <span class="font-bold text-yellow-600">
                  {{ leaveDays }} days
                </span>
              </div>

              <div class="h-2 mt-2 rounded-full bg-slate-200 overflow-hidden">
                <div
                  class="h-full rounded-full bg-yellow-500 transition-all"
                  :style="{ width: `${leavePercentage}%` }"
                ></div>
              </div>

            </div>


            <!-- Pending -->
            <div>

              <div class="flex justify-between text-sm">
                <span class="text-slate-500">
                  Pending Review
                </span>

                <span class="font-bold text-[#8B1E23]">
                  {{ pendingCount }} entries
                </span>
              </div>

            </div>

          </div>

        </div>

      </div>

    </section>


    <!-- ===================================================== -->
    <!-- MONTHLY PERFORMANCE -->
    <!-- ===================================================== -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

        <div>
          <h3 class="text-lg font-bold text-slate-900">
            Monthly Duty Performance
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            Your station attendance and duty completion rate
          </p>
        </div>

        <p class="text-3xl font-bold text-[#8B1E23]">
          {{ performanceRate }}%
        </p>

      </div>


      <div class="mt-4 h-3 rounded-full bg-slate-200 overflow-hidden">

        <div
          class="h-full rounded-full bg-[#8B1E23] transition-all duration-500"
          :style="{ width: `${performanceRate}%` }"
        ></div>

      </div>


      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mt-5">

        <div>
          <p class="text-xs text-slate-500">
            Scheduled Shifts
          </p>

          <p class="text-xl font-bold text-slate-900 mt-1">
            {{ scheduledShifts }}
          </p>
        </div>


        <div>
          <p class="text-xs text-slate-500">
            Completed Shifts
          </p>

          <p class="text-xl font-bold text-green-600 mt-1">
            {{ completedShifts }}
          </p>
        </div>


        <div>
          <p class="text-xs text-slate-500">
            Logs Pending Review
          </p>

          <p class="text-xl font-bold text-yellow-600 mt-1">
            {{ pendingCount }}
          </p>
        </div>

      </div>

    </section>


    <!-- ===================================================== -->
    <!-- ADD / EDIT MODAL -->
    <!-- ===================================================== -->
    <div
      v-if="showFormModal"
      class="fixed inset-0 z-50 bg-slate-900/50 flex items-center justify-center p-4"
      @click.self="closeFormModal"
    >

      <div class="w-full max-w-2xl bg-white rounded-2xl shadow-xl overflow-hidden">

        <!-- Modal Header -->
        <div class="px-6 py-5 border-b border-slate-200">

          <div class="flex items-center justify-between">

            <div>
              <h3 class="text-lg font-bold text-slate-900">
                {{ editingEntry ? 'Edit Duty Entry' : 'Add Duty Entry' }}
              </h3>

              <p class="text-sm text-slate-500 mt-1">
                Record your station duty and attendance details.
              </p>
            </div>

            <button
              @click="closeFormModal"
              class="h-9 w-9 rounded-lg text-slate-400 hover:bg-slate-100 hover:text-slate-700"
            >
              ✕
            </button>

          </div>

        </div>


        <!-- Form -->
        <form
          @submit.prevent="saveEntry"
          class="p-6 space-y-5"
        >

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">

            <!-- Title -->
            <div class="sm:col-span-2">

              <label class="text-sm font-semibold text-slate-700">
                Duty / Activity Title
              </label>

              <input
                v-model="form.title"
                type="text"
                required
                placeholder="e.g. Regular Station Duty"
                class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              />

            </div>


            <!-- Date -->
            <div>

              <label class="text-sm font-semibold text-slate-700">
                Date
              </label>

              <input
                v-model="form.date"
                type="date"
                required
                class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              />

            </div>


            <!-- Location -->
            <div>

              <label class="text-sm font-semibold text-slate-700">
                Location
              </label>

              <input
                v-model="form.location"
                type="text"
                required
                placeholder="BFP Balingasag"
                class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              />

            </div>


            <!-- Start -->
            <div>

              <label class="text-sm font-semibold text-slate-700">
                Start Time
              </label>

              <input
                v-model="form.startTime"
                type="time"
                required
                class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              />

            </div>


            <!-- End -->
            <div>

              <label class="text-sm font-semibold text-slate-700">
                End Time
              </label>

              <input
                v-model="form.endTime"
                type="time"
                required
                class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              />

            </div>


            <!-- Status -->
            <div>

              <label class="text-sm font-semibold text-slate-700">
                Status
              </label>

              <select
                v-model="form.status"
                class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm outline-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              >
                <option>Completed</option>
                <option>Verified</option>
                <option>Pending Review</option>
                <option>Archived</option>
              </select>

            </div>


            <!-- Activities -->
            <div>

              <label class="text-sm font-semibold text-slate-700">
                Activities Logged
              </label>

              <input
                v-model.number="form.activities"
                type="number"
                min="0"
                placeholder="0"
                class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              />

            </div>


            <!-- Description -->
            <div class="sm:col-span-2">

              <label class="text-sm font-semibold text-slate-700">
                Duty Description
              </label>

              <textarea
                v-model="form.description"
                rows="3"
                placeholder="Describe the duty or activities performed..."
                class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none resize-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              ></textarea>

            </div>

          </div>


          <!-- Footer -->
          <div class="flex justify-end gap-3 pt-4 border-t border-slate-200">

            <button
              type="button"
              @click="closeFormModal"
              class="px-5 py-3 rounded-xl border border-slate-300 bg-white text-sm font-semibold text-slate-700 hover:bg-slate-100"
            >
              Cancel
            </button>

            <button
              type="submit"
              class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]"
            >
              {{ editingEntry ? 'Update Entry' : 'Save Entry' }}
            </button>

          </div>

        </form>

      </div>

    </div>


    <!-- ===================================================== -->
    <!-- DETAILS MODAL -->
    <!-- ===================================================== -->
    <div
      v-if="selectedEntry"
      class="fixed inset-0 z-50 bg-slate-900/50 flex items-center justify-center p-4"
      @click.self="selectedEntry = null"
    >

      <div class="w-full max-w-lg bg-white rounded-2xl shadow-xl overflow-hidden">

        <div class="px-6 py-5 border-b border-slate-200">

          <div class="flex items-center justify-between">

            <div>
              <p class="text-xs font-semibold text-[#8B1E23]">
                DUTY LOG DETAILS
              </p>

              <h3 class="text-lg font-bold text-slate-900 mt-1">
                {{ selectedEntry.title }}
              </h3>
            </div>

            <button
              @click="selectedEntry = null"
              class="h-9 w-9 rounded-lg hover:bg-slate-100 text-slate-400"
            >
              ✕
            </button>

          </div>

        </div>


        <div class="p-6 space-y-4">

          <div class="grid grid-cols-2 gap-4">

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-500">
                Date
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ formatDate(selectedEntry.date) }}
              </p>
            </div>

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-500">
                Status
              </p>

              <p class="text-sm font-bold mt-1">
                {{ selectedEntry.status }}
              </p>
            </div>

          </div>


          <div>
            <p class="text-xs text-slate-500">
              Location
            </p>

            <p class="text-sm font-semibold text-slate-900 mt-1">
              {{ selectedEntry.location }}
            </p>
          </div>


          <div>
            <p class="text-xs text-slate-500">
              Shift
            </p>

            <p class="text-sm font-semibold text-slate-900 mt-1">
              {{ selectedEntry.startTime }} - {{ selectedEntry.endTime }}
            </p>
          </div>


          <div>
            <p class="text-xs text-slate-500">
              Activities
            </p>

            <p class="text-sm font-semibold text-slate-900 mt-1">
              {{ selectedEntry.activities }} activities logged
            </p>
          </div>


          <div>
            <p class="text-xs text-slate-500">
              Description
            </p>

            <p class="text-sm text-slate-700 mt-1 leading-6">
              {{ selectedEntry.description || 'No description provided.' }}
            </p>
          </div>


          <div
            v-if="selectedEntry.loggedBy"
            class="pt-4 border-t border-slate-200"
          >
            <p class="text-xs text-slate-500">
              Logged By
            </p>

            <p class="text-sm font-semibold text-slate-900 mt-1">
              {{ selectedEntry.loggedBy }}
            </p>
          </div>

        </div>


        <div class="px-6 py-4 border-t border-slate-200 flex justify-end">

          <button
            @click="selectedEntry = null"
            class="px-5 py-2.5 rounded-xl bg-slate-100 text-sm font-semibold text-slate-700 hover:bg-slate-200"
          >
            Close
          </button>

        </div>

      </div>

    </div>


    <!-- ===================================================== -->
    <!-- TOAST -->
    <!-- ===================================================== -->
    <transition
      enter-active-class="transition duration-200"
      enter-from-class="opacity-0 translate-y-2"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition duration-200"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >

      <div
        v-if="toastMessage"
        class="fixed bottom-6 right-6 z-[70] bg-slate-900 text-white px-5 py-3 rounded-xl shadow-xl text-sm font-semibold"
      >
        ✓ {{ toastMessage }}
      </div>

    </transition>

  </div>
</template>


<script setup>
import { computed, onMounted, ref } from 'vue'


// ============================================================
// PROPS
// ============================================================

const props = defineProps({
  ICONS: {
    type: Object,
    required: true
  }
})


// ============================================================
// STORAGE
// ============================================================

const STORAGE_KEY = 'fireNotifyPersonnelDutyLogs'


// ============================================================
// DUTY LOG DATA
// ============================================================

const entries = ref([
  {
    id: 1,
    title: 'Regular Station Duty',
    date: '2026-09-12',
    location: 'Station 1',
    startTime: '08:00 AM',
    endTime: '05:00 PM',
    description: 'Activities: Briefing, equipment check, fire safety inspection',
    activities: 3,
    status: 'Completed',
    loggedBy: 'FO3 Juan Dela Cruz'
  },

  {
    id: 2,
    title: 'Field Inspection Duty',
    date: '2026-09-11',
    location: 'Public Market Complex',
    startTime: '09:00 AM',
    endTime: '04:30 PM',
    description: 'Fire safety inspection and field assessment.',
    activities: 2,
    status: 'Verified',
    loggedBy: 'FO3 Juan Dela Cruz'
  },

  {
    id: 3,
    title: 'Station Support Duty',
    date: '2026-09-10',
    location: 'BFP Balingasag',
    startTime: '08:00 AM',
    endTime: '05:00 PM',
    description: 'Daily log requires supervisor review.',
    activities: 1,
    status: 'Pending Review',
    loggedBy: 'FO3 Juan Dela Cruz'
  },

  {
    id: 4,
    title: 'Emergency Response Drill',
    date: '2026-09-09',
    location: 'Municipal Training Ground',
    startTime: '08:00 AM',
    endTime: '12:00 PM',
    description: 'Emergency response drill with station personnel.',
    activities: 1,
    status: 'Archived',
    loggedBy: 'FO3 Juan Dela Cruz'
  }
])


// ============================================================
// FILTERS
// ============================================================

const dateRange = ref('This Month')
const statusFilter = ref('All Statuses')
const searchQuery = ref('')


// ============================================================
// MODALS
// ============================================================

const showFormModal = ref(false)
const editingEntry = ref(null)
const selectedEntry = ref(null)


// ============================================================
// TOAST
// ============================================================

const toastMessage = ref('')
let toastTimer = null


// ============================================================
// FORM
// ============================================================

const defaultForm = () => ({
  title: '',
  date: new Date().toISOString().split('T')[0],
  location: 'BFP Balingasag',
  startTime: '08:00 AM',
  endTime: '05:00 PM',
  description: '',
  activities: 0,
  status: 'Pending Review'
})

const form = ref(defaultForm())


// ============================================================
// FILTERED ENTRIES
// ============================================================

const filteredEntries = computed(() => {

  const query = searchQuery.value.toLowerCase().trim()

  return entries.value.filter(entry => {

    const matchesSearch =
      !query ||
      [
        entry.title,
        entry.location,
        entry.description,
        entry.status,
        entry.loggedBy
      ]
        .filter(Boolean)
        .join(' ')
        .toLowerCase()
        .includes(query)


    const matchesStatus =
      statusFilter.value === 'All Statuses' ||
      entry.status === statusFilter.value


    const matchesDate =
      dateRange.value === 'All Records' ||
      isWithinDateRange(entry.date, dateRange.value)


    return matchesSearch && matchesStatus && matchesDate
  })
})


// ============================================================
// STATISTICS
// ============================================================

const completedEntries = computed(() =>
  entries.value.filter(entry =>
    ['Completed', 'Verified'].includes(entry.status)
  )
)

const pendingCount = computed(() =>
  entries.value.filter(entry =>
    entry.status === 'Pending Review'
  ).length
)

const dutyDays = computed(() => {
  return completedEntries.value.length
})

const hoursCompleted = computed(() => {

  return completedEntries.value.reduce((total, entry) => {

    const start = convertTimeToMinutes(entry.startTime)
    const end = convertTimeToMinutes(entry.endTime)

    if (end <= start) return total

    return total + ((end - start) / 60)

  }, 0).toFixed(0)
})

const scheduledHours = computed(() => 176)

const activitiesLogged = computed(() =>
  entries.value.reduce(
    (total, entry) => total + Number(entry.activities || 0),
    0
  )
)

const scheduledShifts = computed(() =>
  entries.value.length
)

const completedShifts = computed(() =>
  completedEntries.value.length
)

const performanceRate = computed(() => {

  if (!scheduledShifts.value) return 0

  return Math.min(
    100,
    Math.round(
      (completedShifts.value / scheduledShifts.value) * 100
    )
  )
})


// ============================================================
// ATTENDANCE
// ============================================================

const presentDays = computed(() =>
  completedEntries.value.length
)

const leaveDays = computed(() => 0)

const attendanceTotal = computed(() =>
  Math.max(
    1,
    presentDays.value + leaveDays.value
  )
)

const presentPercentage = computed(() =>
  Math.round(
    (presentDays.value / attendanceTotal.value) * 100
  )
)

const leavePercentage = computed(() =>
  Math.round(
    (leaveDays.value / attendanceTotal.value) * 100
  )
)


// ============================================================
// CURRENT SHIFT
// ============================================================

const currentShiftActive = computed(() => {

  const today = new Date().toISOString().split('T')[0]

  return entries.value.some(entry =>
    entry.date === today &&
    ['Completed', 'Verified', 'Pending Review'].includes(entry.status)
  )
})


// ============================================================
// ACTIVE FILTERS
// ============================================================

const hasActiveFilters = computed(() => {

  return (
    dateRange.value !== 'This Month' ||
    statusFilter.value !== 'All Statuses' ||
    searchQuery.value !== ''
  )
})


// ============================================================
// DATE RANGE
// ============================================================

const isWithinDateRange = (dateString, range) => {

  const date = new Date(`${dateString}T00:00:00`)
  const now = new Date()

  if (range === 'All Records') {
    return true
  }


  if (range === 'This Month') {

    return (
      date.getMonth() === now.getMonth() &&
      date.getFullYear() === now.getFullYear()
    )
  }


  if (range === 'This Week') {

    const currentDay = now.getDay()

    const mondayOffset =
      currentDay === 0 ? -6 : 1 - currentDay

    const start = new Date(now)

    start.setDate(now.getDate() + mondayOffset)
    start.setHours(0, 0, 0, 0)

    const end = new Date(start)

    end.setDate(start.getDate() + 6)
    end.setHours(23, 59, 59, 999)

    return date >= start && date <= end
  }


  if (range === 'Last Month') {

    const previousMonth =
      new Date(now.getFullYear(), now.getMonth() - 1, 1)

    return (
      date.getMonth() === previousMonth.getMonth() &&
      date.getFullYear() === previousMonth.getFullYear()
    )
  }


  return true
}


// ============================================================
// TIME HELPERS
// ============================================================

const convertTimeToMinutes = (time) => {

  if (!time) return 0

  const parts = time.trim().split(' ')

  const clock = parts[0]
  const modifier = parts[1]

  let [hours, minutes] =
    clock.split(':').map(Number)

  if (modifier === 'PM' && hours !== 12) {
    hours += 12
  }

  if (modifier === 'AM' && hours === 12) {
    hours = 0
  }

  return hours * 60 + minutes
}


// ============================================================
// DATE FORMAT
// ============================================================

const formatDate = (dateString) => {

  if (!dateString) return ''

  const date = new Date(`${dateString}T00:00:00`)

  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}


// ============================================================
// STATUS STYLING
// ============================================================

const getStatusClass = (status) => {

  const classes = {
    Completed: 'bg-green-100 text-green-700',
    Verified: 'bg-blue-100 text-blue-700',
    'Pending Review': 'bg-yellow-100 text-yellow-700',
    Archived: 'bg-slate-200 text-slate-700'
  }

  return classes[status] || 'bg-slate-100 text-slate-700'
}


const getEntryContainerClass = (status) => {

  const classes = {
    Completed: 'border-green-200 bg-green-50',
    Verified: 'border-blue-200 bg-blue-50',
    'Pending Review': 'border-yellow-200 bg-yellow-50',
    Archived: 'border-slate-200 bg-slate-50'
  }

  return classes[status] || 'border-slate-200 bg-white'
}


const getEntryIconBackground = (status) => {

  const classes = {
    Completed: 'bg-green-100',
    Verified: 'bg-blue-100',
    'Pending Review': 'bg-yellow-100',
    Archived: 'bg-slate-200'
  }

  return classes[status] || 'bg-slate-100'
}


const getEntryIconColor = (status) => {

  const classes = {
    Completed: 'text-green-600',
    Verified: 'text-blue-600',
    'Pending Review': 'text-yellow-600',
    Archived: 'text-slate-500'
  }

  return classes[status] || 'text-slate-500'
}


// ============================================================
// ADD ENTRY
// ============================================================

const openAddModal = () => {

  editingEntry.value = null

  form.value = defaultForm()

  showFormModal.value = true
}


// ============================================================
// EDIT ENTRY
// ============================================================

const editEntry = (entry) => {

  editingEntry.value = entry

  form.value = {
    title: entry.title,
    date: entry.date,
    location: entry.location,
    startTime: entry.startTime,
    endTime: entry.endTime,
    description: entry.description,
    activities: entry.activities,
    status: entry.status
  }

  showFormModal.value = true
}


// ============================================================
// SAVE ENTRY
// ============================================================

const saveEntry = () => {

  if (editingEntry.value) {

    const index = entries.value.findIndex(
      entry => entry.id === editingEntry.value.id
    )

    if (index !== -1) {

      entries.value[index] = {
        ...entries.value[index],
        ...form.value
      }
    }

    showToast('Duty entry updated successfully.')

  } else {

    entries.value.unshift({
      id: Date.now(),
      ...form.value,
      loggedBy: 'FO3 Juan Dela Cruz'
    })

    showToast('Duty entry added successfully.')
  }


  persistEntries()

  closeFormModal()
}


// ============================================================
// MARK COMPLETE
// ============================================================

const markCompleted = (entry) => {

  entry.status = 'Completed'

  persistEntries()

  showToast('Duty entry marked as completed.')
}


// ============================================================
// VIEW DETAILS
// ============================================================

const viewEntry = (entry) => {
  selectedEntry.value = entry
}


// ============================================================
// DELETE ENTRY
// ============================================================

const deleteEntry = (id) => {

  const confirmed =
    window.confirm(
      'Are you sure you want to delete this duty entry?'
    )

  if (!confirmed) return

  entries.value = entries.value.filter(
    entry => entry.id !== id
  )

  persistEntries()

  showToast('Duty entry deleted.')
}


// ============================================================
// CLOSE FORM
// ============================================================

const closeFormModal = () => {

  showFormModal.value = false

  editingEntry.value = null

  form.value = defaultForm()
}


// ============================================================
// CLEAR FILTERS
// ============================================================

const clearFilters = () => {

  dateRange.value = 'This Month'
  statusFilter.value = 'All Statuses'
  searchQuery.value = ''
}


// ============================================================
// LOCAL STORAGE
// ============================================================

const persistEntries = () => {

  localStorage.setItem(
    STORAGE_KEY,
    JSON.stringify(entries.value)
  )
}


const loadEntries = () => {

  const saved =
    localStorage.getItem(STORAGE_KEY)

  if (!saved) return

  try {

    const parsed = JSON.parse(saved)

    if (Array.isArray(parsed)) {
      entries.value = parsed
    }

  } catch (error) {

    console.error(
      'Failed to load duty logs:',
      error
    )
  }
}


// ============================================================
// TOAST
// ============================================================

const showToast = (message) => {

  toastMessage.value = message

  clearTimeout(toastTimer)

  toastTimer = setTimeout(() => {
    toastMessage.value = ''
  }, 3000)
}


// ============================================================
// LIFECYCLE
// ============================================================

onMounted(() => {
  loadEntries()
})
</script>