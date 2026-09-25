<template>
  <div class="w-full min-w-0 space-y-6">

    <!-- =========================================================
         PAGE HEADER
    ========================================================== -->
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
            Tasks assigned to you by the administrator.
          </p>
        </div>

        <button
          @click="clearFilters"
          class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold
                 hover:bg-[#72181D] transition"
        >
          View All Tasks
        </button>

      </div>
    </section>


    <!-- =========================================================
         STATISTICS
    ========================================================== -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">

      <!-- TOTAL -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">

          <div>
            <p class="text-sm text-slate-500">
              Total Tasks
            </p>

            <p class="text-3xl font-bold text-slate-900 mt-1">
              {{ tasks.length.toString().padStart(2, '0') }}
            </p>
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
            <p class="text-sm text-slate-500">
              Pending
            </p>

            <p class="text-3xl font-bold text-amber-600 mt-1">
              {{ pendingTasks.toString().padStart(2, '0') }}
            </p>
          </div>

          <div class="h-12 w-12 rounded-xl bg-amber-50 flex items-center justify-center">
            <span class="text-xl">
              ⏳
            </span>
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
              {{ completedTasks.toString().padStart(2, '0') }}
            </p>
          </div>

          <div class="h-12 w-12 rounded-xl bg-green-50 flex items-center justify-center">
            <span class="text-xl font-bold">
              ✓
            </span>
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

            <p class="text-3xl font-bold text-red-600 mt-1">
              {{ overdueTasks.toString().padStart(2, '0') }}
            </p>
          </div>

          <div class="h-12 w-12 rounded-xl bg-red-50 flex items-center justify-center">
            <span class="text-xl font-bold">
              !
            </span>
          </div>

        </div>
      </div>

    </section>


    <!-- =========================================================
         FILTERS
    ========================================================== -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

      <div class="flex flex-col lg:flex-row gap-4 lg:items-end lg:justify-between">

        <div class="flex-1">
          <h3 class="font-bold text-slate-900">
            Task List
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            Tasks assigned to your personnel account.
          </p>
        </div>


        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 w-full lg:w-auto">

          <!-- SEARCH -->
          <div>
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Search tasks..."
              class="w-full sm:w-64 px-4 py-3 rounded-xl border border-slate-300
                     text-sm focus:outline-none focus:ring-2 focus:ring-[#8B1E23]/20
                     focus:border-[#8B1E23]"
            />
          </div>


          <!-- STATUS -->
          <select
            v-model="selectedStatus"
            class="px-4 py-3 rounded-xl border border-slate-300
                   text-sm font-medium bg-white focus:outline-none
                   focus:border-[#8B1E23]"
          >
            <option value="All">All Tasks</option>
            <option value="Pending">Pending</option>
            <option value="Assigned">Assigned</option>
            <option value="In Progress">In Progress</option>
            <option value="For Verification">For Verification</option>
            <option value="Returned">Returned</option>
            <option value="Verified">Verified</option>
            <option value="Completed">Completed</option>
            <option value="Overdue">Overdue</option>
          </select>


          <!-- PRIORITY -->
          <select
            v-model="selectedPriority"
            class="px-4 py-3 rounded-xl border border-slate-300
                   text-sm font-medium bg-white focus:outline-none
                   focus:border-[#8B1E23]"
          >
            <option value="All">All Priorities</option>
            <option value="High">High Priority</option>
            <option value="Medium">Medium Priority</option>
            <option value="Low">Low Priority</option>
          </select>

        </div>

      </div>

    </section>


    <!-- =========================================================
         CURRENT ASSIGNMENTS
    ========================================================== -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between
                  gap-3 border-b border-slate-200 pb-5">

        <div>
          <h3 class="text-xl font-bold text-slate-900">
            Current Assignments
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            Tasks assigned by the administrator.
          </p>
        </div>

        <span
          class="px-4 py-2 rounded-full bg-blue-50 text-blue-700
                 text-sm font-bold"
        >
          {{ filteredTasks.length }} Showing
        </span>

      </div>


      <!-- =======================================================
           TASK CARDS
      ======================================================== -->
      <div
        v-if="filteredTasks.length"
        class="mt-5 space-y-4"
      >

        <div
          v-for="task in filteredTasks"
          :key="task.id"
          class="p-5 rounded-xl border border-slate-200 bg-slate-50
                 hover:border-[#8B1E23] hover:shadow-sm transition"
        >

          <div class="flex flex-col xl:flex-row xl:items-center
                      xl:justify-between gap-5">

            <!-- TASK INFORMATION -->
            <div class="flex items-start gap-4">

              <div
                class="h-12 w-12 rounded-xl flex items-center
                       justify-center shrink-0"
                :class="priorityIconBg(task.priority)"
              >

                <span
                  v-html="ICONS.tasks"
                  class="h-6 w-6"
                  :class="priorityIconColor(task.priority)"
                ></span>

              </div>


              <div class="min-w-0">

                <div class="flex flex-wrap items-center gap-2">

                  <p class="text-base font-bold text-slate-900">
                    {{ task.title }}
                  </p>

                  <span
                    class="px-2.5 py-1 rounded-full text-xs font-bold"
                    :class="statusClass(task.status)"
                  >
                    {{ task.status }}
                  </span>

                  <span
                    class="px-2.5 py-1 rounded-full text-xs font-bold"
                    :class="priorityClass(task.priority)"
                  >
                    {{ task.priority }}
                  </span>

                </div>


                <!-- SUBTOPIC -->
                <p
                  v-if="task.subtopic"
                  class="text-sm font-semibold text-[#8B1E23] mt-1"
                >
                  Subtopic: {{ task.subtopic }}
                </p>


                <p class="text-sm text-slate-500 mt-1">
                  {{ task.description }}
                </p>


                <div class="flex flex-wrap gap-x-5 gap-y-1 mt-2">

                  <p class="text-sm text-slate-500">
                    <span class="font-semibold">
                      Due:
                    </span>
                    {{ task.due || task.dueDate || 'No due date' }}
                  </p>

                  <p
                    v-if="task.location"
                    class="text-sm text-slate-500"
                  >
                    <span class="font-semibold">
                      Location:
                    </span>
                    {{ task.location }}
                  </p>

                </div>

              </div>

            </div>


            <!-- ACTIONS -->
            <div class="flex flex-col sm:flex-row gap-3 shrink-0">

              <button
                @click="viewDetails(task)"
                class="px-4 py-3 rounded-xl border border-slate-300
                       bg-white text-slate-700 text-sm font-bold
                       hover:bg-slate-100 transition"
              >
                View Details
              </button>


              <!-- START TASK -->
              <button
                v-if="task.status === 'Pending' || task.status === 'Assigned' || task.status === 'Overdue'"
                @click="startTask(task)"
                class="px-5 py-3 rounded-xl bg-[#8B1E23]
                       text-white text-sm font-bold
                       hover:bg-[#72181D] transition"
              >
                Start Task
              </button>


              <!-- SUBMIT TASK -->
              <button
                v-else-if="task.status === 'In Progress' || task.status === 'Returned'"
                @click="openSubmitModal(task)"
                class="px-5 py-3 rounded-xl bg-green-600
                       text-white text-sm font-bold
                       hover:bg-green-700 transition"
              >
                {{ task.status === 'Returned' ? 'Revise Submission' : 'Submit for Verification' }}
              </button>


              <!-- SUBMITTED -->
              <span
                v-else-if="task.status === 'For Verification'"
                class="px-5 py-3 rounded-xl bg-blue-100
                       text-blue-700 text-sm font-bold text-center"
              >
                For Verification
              </span>


              <!-- COMPLETED -->
              <span
                v-else-if="task.status === 'Verified' || task.status === 'Completed'"
                class="px-5 py-3 rounded-xl bg-green-100
                       text-green-700 text-sm font-bold text-center"
              >
                Verified
              </span>


              <!-- OVERDUE -->
              <button
                v-else-if="task.status === 'Overdue'"
                @click="startTask(task)"
                class="px-5 py-3 rounded-xl bg-[#8B1E23]
                       text-white text-sm font-bold
                       hover:bg-[#72181D] transition"
              >
                Start Task
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
                {{ task.progress || 0 }}%
              </span>

            </div>

            <div class="w-full h-2.5 bg-slate-200 rounded-full overflow-hidden">

              <div
                class="h-full rounded-full transition-all duration-500"
                :class="progressClass(task.status)"
                :style="{ width: `${task.progress || 0}%` }"
              ></div>

            </div>

          </div>

        </div>

      </div>


      <!-- EMPTY -->
      <div
        v-else
        class="mt-6 py-14 text-center border-2 border-dashed
               border-slate-200 rounded-xl"
      >

        <div class="text-4xl mb-3">
          📋
        </div>

        <h4 class="font-bold text-slate-900">
          No assigned tasks
        </h4>

        <p class="text-sm text-slate-500 mt-1">
          Your administrator has not assigned any tasks to you yet.
        </p>

        <button
          @click="clearFilters"
          class="mt-4 px-4 py-2 rounded-lg bg-slate-100
                 text-slate-700 text-sm font-bold hover:bg-slate-200"
        >
          Clear Filters
        </button>

      </div>

    </section>


    <!-- =========================================================
         TODAY'S PRIORITY + RECENTLY COMPLETED
    ========================================================== -->
    <section class="grid grid-cols-1 lg:grid-cols-2 gap-6">

      <!-- TODAY'S PRIORITY -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <h3 class="text-lg font-bold text-slate-900">
          Today's Priority
        </h3>

        <p class="text-sm text-slate-500 mt-1">
          Tasks that require immediate attention.
        </p>


        <div class="mt-5 space-y-4">

          <div
            v-for="task in priorityTasks"
            :key="task.id"
            class="p-4 rounded-xl border"
            :class="task.priority === 'High'
              ? 'bg-red-50 border-red-100'
              : 'bg-amber-50 border-amber-100'"
          >

            <div class="flex items-start gap-3">

              <span
                class="font-bold text-lg"
                :class="task.priority === 'High'
                  ? 'text-red-600'
                  : 'text-amber-600'"
              >
                !
              </span>

              <div class="min-w-0">

                <p class="font-bold text-slate-900">
                  {{ task.title }}
                </p>

                <p
                  v-if="task.subtopic"
                  class="text-xs font-semibold text-[#8B1E23] mt-1"
                >
                  {{ task.subtopic }}
                </p>

                <p class="text-sm text-slate-500 mt-1">
                  {{ task.location || 'No location specified' }}
                </p>

                <p
                  class="text-xs font-bold mt-2"
                  :class="task.priority === 'High'
                    ? 'text-red-600'
                    : 'text-amber-600'"
                >
                  {{ task.priority }} Priority • Due {{ task.due || task.dueDate }}
                </p>

              </div>

            </div>

          </div>


          <div
            v-if="priorityTasks.length === 0"
            class="text-sm text-slate-500 py-4"
          >
            No high-priority tasks at the moment.
          </div>

        </div>

      </div>


      <!-- RECENTLY COMPLETED -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <h3 class="text-lg font-bold text-slate-900">
          Recently Completed
        </h3>

        <p class="text-sm text-slate-500 mt-1">
          Your latest submitted and completed assignments.
        </p>


        <div class="mt-5 space-y-4">

          <div
            v-for="task in recentlyCompleted"
            :key="task.id"
            class="flex items-center gap-4 p-4 rounded-xl bg-green-50"
          >

            <div
              class="h-10 w-10 rounded-full bg-green-100
                     flex items-center justify-center shrink-0"
            >
              <span class="text-green-600 font-bold">
                ✓
              </span>
            </div>

            <div class="min-w-0">

              <p class="font-bold text-slate-900">
                {{ task.title }}
              </p>

              <p class="text-xs text-slate-500 mt-1">
                {{ task.completedAt || task.submittedAt || 'Completed' }}
              </p>

            </div>

          </div>


          <div
            v-if="recentlyCompleted.length === 0"
            class="text-sm text-slate-500 py-4"
          >
            No completed tasks yet.
          </div>

        </div>

      </div>

    </section>


    <!-- =========================================================
         TASK DETAILS MODAL
    ========================================================== -->
    <div
      v-if="selectedTask"
      class="fixed inset-0 z-50 bg-black/40 flex items-center
             justify-center p-4"
      @click.self="closeDetails"
    >

      <div
        class="bg-white rounded-2xl shadow-xl w-full max-w-2xl
               max-h-[90vh] overflow-y-auto"
      >

        <!-- HEADER -->
        <div
          class="flex items-start justify-between p-6
                 border-b border-slate-200"
        >

          <div>

            <p class="text-xs font-bold uppercase tracking-wide text-[#8B1E23]">
              Assigned Task
            </p>

            <h3 class="text-xl font-bold text-slate-900 mt-1">
              {{ selectedTask.title }}
            </h3>

          </div>

          <button
            @click="closeDetails"
            class="h-9 w-9 rounded-lg bg-slate-100
                   text-slate-500 hover:bg-slate-200 text-xl"
          >
            ×
          </button>

        </div>


        <!-- BODY -->
        <div class="p-6 space-y-6">

          <div v-if="selectedTask.subtopic">

            <p class="text-sm font-semibold text-slate-500">
              Subtopic
            </p>

            <p class="text-sm font-bold text-[#8B1E23] mt-1">
              {{ selectedTask.subtopic }}
            </p>

          </div>


          <div>

            <p class="text-sm font-semibold text-slate-500">
              Task Instructions
            </p>

            <p class="text-sm text-slate-800 mt-1 whitespace-pre-line">
              {{ selectedTask.description || 'No instructions provided.' }}
            </p>

          </div>


          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">

            <!-- STATUS -->
            <div class="p-4 rounded-xl bg-slate-50">

              <p class="text-xs text-slate-500">
                Status
              </p>

              <span
                class="inline-block mt-2 px-3 py-1 rounded-full
                       text-xs font-bold"
                :class="statusClass(selectedTask.status)"
              >
                {{ selectedTask.status }}
              </span>

            </div>


            <!-- PRIORITY -->
            <div class="p-4 rounded-xl bg-slate-50">

              <p class="text-xs text-slate-500">
                Priority
              </p>

              <span
                class="inline-block mt-2 px-3 py-1 rounded-full
                       text-xs font-bold"
                :class="priorityClass(selectedTask.priority)"
              >
                {{ selectedTask.priority }}
              </span>

            </div>


            <!-- DUE -->
            <div class="p-4 rounded-xl bg-slate-50">

              <p class="text-xs text-slate-500">
                Due Date
              </p>

              <p class="font-bold text-slate-900 mt-1">
                {{ selectedTask.due || selectedTask.dueDate || 'No due date' }}
              </p>

            </div>


            <!-- LOCATION -->
            <div class="p-4 rounded-xl bg-slate-50">

              <p class="text-xs text-slate-500">
                Location
              </p>

              <p class="font-bold text-slate-900 mt-1">
                {{ selectedTask.location || 'Not specified' }}
              </p>

            </div>

          </div>


          <!-- SUBMISSION INFO -->
          <div
            v-if="selectedTask.status === 'Submitted'"
            class="p-4 rounded-xl bg-blue-50 border border-blue-100"
          >

            <p class="text-sm font-bold text-blue-800">
              Task Submitted
            </p>

            <p class="text-sm text-blue-700 mt-1">
              {{ selectedTask.accomplishment || selectedTask.submissionNote || 'Submitted successfully.' }}
            </p>

            <p
              v-if="selectedTask.submittedAt"
              class="text-xs text-blue-600 mt-2"
            >
              Submitted: {{ selectedTask.submittedAt }}
            </p>

          </div>


          <!-- PROGRESS -->
          <div>

            <div class="flex justify-between mb-2">

              <span class="text-sm font-semibold text-slate-600">
                Progress
              </span>

              <span class="text-sm font-bold text-slate-900">
                {{ selectedTask.progress || 0 }}%
              </span>

            </div>

            <div class="w-full h-3 bg-slate-200 rounded-full overflow-hidden">

              <div
                class="h-full rounded-full transition-all"
                :class="progressClass(selectedTask.status)"
                :style="{ width: `${selectedTask.progress || 0}%` }"
              ></div>

            </div>

          </div>

        </div>


        <!-- FOOTER -->
        <div
          class="flex flex-col sm:flex-row justify-end gap-3
                 p-6 border-t border-slate-200"
        >

          <button
            @click="closeDetails"
            class="px-5 py-3 rounded-xl border border-slate-300
                   text-slate-700 text-sm font-bold
                   hover:bg-slate-100"
          >
            Close
          </button>


          <button
            v-if="selectedTask.status === 'Pending' || selectedTask.status === 'Assigned' || selectedTask.status === 'Overdue'"
            @click="startTask(selectedTask)"
            class="px-5 py-3 rounded-xl bg-[#8B1E23]
                   text-white text-sm font-bold
                   hover:bg-[#72181D]"
          >
            Start Task
          </button>


          <button
            v-if="selectedTask.status === 'In Progress' || selectedTask.status === 'Returned'"
            @click="openSubmitModal(selectedTask)"
            class="px-5 py-3 rounded-xl bg-green-600
                   text-white text-sm font-bold
                   hover:bg-green-700"
          >
            {{ selectedTask.status === 'Returned' ? 'Revise Submission' : 'Submit for Verification' }}
          </button>

        </div>

      </div>

    </div>


    <!-- =========================================================
         SUBMIT TASK MODAL
    ========================================================== -->
    <div
      v-if="submitTask"
      class="fixed inset-0 z-[60] bg-black/50 flex items-center
             justify-center p-4"
      @click.self="closeSubmitModal"
    >

      <div class="bg-white rounded-2xl shadow-xl w-full max-w-lg">

        <div class="p-6 border-b border-slate-200">

          <p class="text-xs font-bold uppercase tracking-wide text-[#8B1E23]">
            Task Submission
          </p>

          <h3 class="text-xl font-bold text-slate-900 mt-1">
            Submit Task
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            {{ submitTask.title }}
          </p>

          <div class="mt-3 flex flex-wrap gap-3 text-xs text-white/80">
            <span>Status: {{ submitTask.status }}</span>
            <span>Reference: {{ submitTask.id }}</span>
          </div>

        </div>


        <div class="p-6">

          <label class="block text-sm font-bold text-slate-700 mb-2">
            Accomplishment / Work Summary
            <span class="text-[#8B1E23]">*</span>
          </label>

          <textarea
            v-model="accomplishment"
            rows="5"
            placeholder="Describe the work completed, observations, and outcomes."
            class="w-full px-4 py-3 rounded-xl border border-slate-300
                   text-sm resize-none focus:outline-none
                   focus:ring-2 focus:ring-[#8B1E23]/20
                   focus:border-[#8B1E23]"
          ></textarea>

          <p class="text-xs text-slate-500 mt-2">
            Provide the work completed for Admin verification.
          </p>

          <label class="block text-sm font-bold text-slate-700 mt-4 mb-2">
            Remarks <span class="font-normal text-slate-400">(Optional)</span>
          </label>

          <textarea
            v-model="submissionRemarks"
            rows="3"
            placeholder="Remarks (optional)"
            class="mt-4 w-full rounded-xl border border-slate-300 px-4 py-3 text-sm resize-none focus:outline-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
          ></textarea>

          <label class="block text-sm font-bold text-slate-700 mt-5 mb-2">
            Evidence Photos <span class="font-normal text-slate-400">(optional)</span>
          </label>

          <input
            type="file"
            multiple
            accept=".jpg,.jpeg,.png,.webp,image/jpeg,image/png,image/webp"
            @change="handleEvidenceSelection"
            class="block w-full text-sm text-slate-600 file:mr-4 file:py-2.5 file:px-4 file:rounded-xl file:border-0 file:bg-[#8B1E23] file:text-white file:font-semibold"
          />

          <div v-if="evidenceFiles.length" class="mt-3 grid grid-cols-2 sm:grid-cols-3 gap-3">
            <div v-for="(file, index) in evidenceFiles" :key="`${file.name}-${index}`" class="rounded-xl border border-slate-200 bg-slate-50 p-2">
              <img v-if="evidencePreviews[index]" :src="evidencePreviews[index]" :alt="file.name" class="h-24 w-full rounded-lg object-cover" />
              <p class="truncate text-xs font-semibold text-slate-700 mt-2">{{ file.name }}</p>
              <button type="button" @click="removeEvidence(index)" class="mt-1 text-xs font-bold text-[#8B1E23]">Remove</button>
            </div>
          </div>

        </div>


        <div
          class="flex justify-end gap-3 p-6 border-t border-slate-200"
        >

          <button
            @click="closeSubmitModal"
            class="px-5 py-3 rounded-xl border border-slate-300
                   text-slate-700 text-sm font-bold
                   hover:bg-slate-100"
          >
            Cancel
          </button>

          <button
            @click="submitTaskToAdmin"
            :disabled="!accomplishment.trim()"
            class="px-5 py-3 rounded-xl bg-[#8B1E23]
                   text-white text-sm font-bold
                   hover:bg-[#72181D]
                   disabled:opacity-50 disabled:cursor-not-allowed"
          >
            Submit for Verification
          </button>

        </div>

      </div>

    </div>

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
  },

  taskList: {
    type: Array,
    required: false,
    default: () => []
  }
})


/* =========================================================
   SHARED STORAGE KEY
   IMPORTANT:
   ADMIN MUST SAVE ASSIGNED TASKS USING THIS SAME KEY.
========================================================= */

const TASK_STORAGE_KEY = 'firenotify_tasks'


/* =========================================================
   TASK DATA
   NO MORE HARDCODED TASKS
========================================================= */

const tasks = ref([])


/* =========================================================
   FILTER STATE
========================================================= */

const searchQuery = ref('')
const selectedStatus = ref('All')
const selectedPriority = ref('All')


/* =========================================================
   SELECTED TASK
========================================================= */

const selectedTask = ref(null)


/* =========================================================
   SUBMISSION
========================================================= */

const submitTask = ref(null)
const accomplishment = ref('')
const submissionRemarks = ref('')
const evidenceFiles = ref([])
const evidencePreviews = ref([])


/* =========================================================
   GET CURRENT USER
========================================================= */

const getCurrentUser = () => {

  if (props.currentUser) {
    return props.currentUser
  }

  try {

    const savedUser = localStorage.getItem('currentUser')

    if (savedUser) {
      return JSON.parse(savedUser)
    }

  } catch (error) {

    console.error(
      'Unable to read currentUser:',
      error
    )

  }

  return null
}

const notifyAdmin = task => {
  try {
    const key = 'firenotify_notifications'
    const current = JSON.parse(localStorage.getItem(key) || '[]')
    const notification = {
      id: `notif-task-${task.id}-${Date.now()}`,
      title: 'Task submitted for verification',
      detail: `${task.title} was submitted for verification.`,
      type: 'Task Alerts',
      status: 'unread',
      read: false,
      createdAt: new Date().toISOString(),
      assignedToId: 'admin-default',
      taskId: task.id
    }
    localStorage.setItem(key, JSON.stringify([notification, ...current]))
    window.dispatchEvent(new CustomEvent('fireNotifyNotificationsUpdated'))
  } catch (error) {
    console.warn('FireNotify: unable to notify admin about task submission', error)
  }
}


/* =========================================================
   LOAD TASKS FROM ADMIN
========================================================= */

const loadTasks = () => {

  try {

    const storedTasks =
      JSON.parse(
        localStorage.getItem(TASK_STORAGE_KEY) || '[]'
      )

    const user = getCurrentUser()

    /*
      Only show tasks assigned to THIS personnel.
    */

    if (!user) {

      tasks.value = []

      return
    }


    /*
      Match by personnel ID first.
      Username is used as fallback.
    */

    tasks.value = storedTasks.filter(task => {

      const assignedId =
        String(
          task.assignedToId ??
          task.assignedTo ??
          ''
        )

      const userId =
        String(
          user.id ??
          user.userId ??
          ''
        )


      const assignedUsername =
        String(
          task.assignedToUsername ??
          ''
        ).toLowerCase()


      const username =
        String(
          user.username ??
          ''
        ).toLowerCase()


      const idMatch =
        assignedId &&
        userId &&
        assignedId === userId


      const usernameMatch =
        assignedUsername &&
        username &&
        assignedUsername === username


      return idMatch || usernameMatch

    })

  } catch (error) {

    console.error(
      'Failed to load FireNotify tasks:',
      error
    )

    tasks.value = []

  }

}


/* =========================================================
   FILTERED TASKS
========================================================= */

const filteredTasks = computed(() => {

  const search =
    searchQuery.value.trim().toLowerCase()

  return tasks.value.filter(task => {

    const title =
      String(task.title || '').toLowerCase()

    const description =
      String(task.description || '').toLowerCase()

    const subtopic =
      String(task.subtopic || '').toLowerCase()

    const location =
      String(task.location || '').toLowerCase()


    const matchesSearch =
      !search ||
      title.includes(search) ||
      description.includes(search) ||
      subtopic.includes(search) ||
      location.includes(search)


    const matchesStatus =
      selectedStatus.value === 'All' ||
      task.status === selectedStatus.value


    const matchesPriority =
      selectedPriority.value === 'All' ||
      task.priority === selectedPriority.value


    return (
      matchesSearch &&
      matchesStatus &&
      matchesPriority
    )

  })

})


/* =========================================================
   STATISTICS
========================================================= */

const pendingTasks = computed(() =>
  tasks.value.filter(
    task => [
      'Pending',
      'Assigned',
      'In Progress',
      'For Verification',
      'Returned'
    ].includes(task.status)
  ).length
)


const completedTasks = computed(() =>
  tasks.value.filter(
    task => task.status === 'Completed' || task.status === 'Verified'
  ).length
)


const overdueTasks = computed(() =>
  tasks.value.filter(
    task => task.status === 'Overdue'
  ).length
)


/* =========================================================
   PRIORITY TASKS
========================================================= */

const priorityTasks = computed(() =>
  tasks.value.filter(task =>
    task.status !== 'Completed' &&
    task.status !== 'Submitted' &&
    task.priority === 'High'
  )
)


/* =========================================================
   RECENTLY COMPLETED
========================================================= */

const recentlyCompleted = computed(() =>
  tasks.value
    .filter(task =>
      task.status === 'Completed' ||
      task.status === 'Submitted'
    )
    .slice(0, 5)
)


/* =========================================================
   VIEW DETAILS
========================================================= */

const viewDetails = task => {

  selectedTask.value = task

}


/* =========================================================
   CLOSE DETAILS
========================================================= */

const closeDetails = () => {

  selectedTask.value = null

}


/* =========================================================
   START TASK
========================================================= */

const startTask = task => {

  const allTasks =
    JSON.parse(
      localStorage.getItem(TASK_STORAGE_KEY) || '[]'
    )


  const index =
    allTasks.findIndex(
      item => String(item.id) === String(task.id)
    )


  if (index === -1) {
    return
  }


  allTasks[index] = {
    ...allTasks[index],

    status: 'In Progress',

    progress: Math.max(
      Number(allTasks[index].progress || 0),
      10
    ),

    startedAt:
      allTasks[index].startedAt ||
      new Date().toLocaleString()
  }


  localStorage.setItem(
    TASK_STORAGE_KEY,
    JSON.stringify(allTasks)
  )


  loadTasks()


  selectedTask.value = null

}


/* =========================================================
   OPEN SUBMIT MODAL
========================================================= */

const openSubmitModal = task => {

  submitTask.value = task

  accomplishment.value =
    task.accomplishment || task.submissionNote || ''
  submissionRemarks.value = task.submissionRemarks || ''

  evidencePreviews.value.forEach(url => URL.revokeObjectURL(url))
  evidenceFiles.value = []
  evidencePreviews.value = []

}


/* =========================================================
   CLOSE SUBMIT MODAL
========================================================= */

const closeSubmitModal = () => {

  submitTask.value = null

  accomplishment.value = ''
  submissionRemarks.value = ''

  evidenceFiles.value = []
  evidencePreviews.value.forEach(url => URL.revokeObjectURL(url))
  evidencePreviews.value = []

}

const handleEvidenceSelection = event => {
  const files = Array.from(event?.target?.files || [])
  const validFiles = files.filter(file =>
    /\.(jpe?g|png|webp)$/i.test(file.name) ||
    /^image\/(jpeg|png|webp)$/i.test(file.type)
  )

  if (validFiles.length !== files.length) {
    showToast('Please select JPG, PNG, or WEBP image files only.')
  }

  evidencePreviews.value.forEach(url => URL.revokeObjectURL(url))
  evidenceFiles.value = validFiles
  evidencePreviews.value = validFiles.map(file => URL.createObjectURL(file))
}

const removeEvidence = index => {
  const [preview] = evidencePreviews.value.splice(index, 1)
  if (preview) URL.revokeObjectURL(preview)
  evidenceFiles.value.splice(index, 1)
}


/* =========================================================
   SUBMIT TASK TO ADMIN
========================================================= */

const submitTaskToAdmin = async () => {

  if (
    !submitTask.value ||
    !accomplishment.value.trim()
  ) {
    showToast('Please provide an accomplishment/work summary before submitting.')
    return
  }


  const allTasks =
    JSON.parse(
      localStorage.getItem(TASK_STORAGE_KEY) || '[]'
    )


  const index =
    allTasks.findIndex(
      item =>
        String(item.id) ===
        String(submitTask.value.id)
    )


  if (index === -1) {
    return
  }


  const user = getCurrentUser()


  await deleteTaskActivityEvidence({
    recordId: allTasks[index].id,
    recordType: 'task'
  })

  const evidence = await saveTaskActivityEvidence({
    recordId: allTasks[index].id,
    recordType: 'task',
    files: evidenceFiles.value
  })

  allTasks[index] = {

    ...allTasks[index],

    status: 'For Verification',

    progress: 90,

    accomplishment:
      accomplishment.value.trim(),

    submissionRemarks:
      submissionRemarks.value.trim(),

    submittedAt:
      new Date().toLocaleString(),

    submittedBy:
      user?.username ||
      user?.name ||
      'Personnel',

    evidence,

    submissionStatus: 'For Verification'

  }


  localStorage.setItem(
    TASK_STORAGE_KEY,
    JSON.stringify(allTasks)
  )

  window.dispatchEvent(new CustomEvent('fireNotifyTasksUpdated'))

  notifyAdmin(allTasks[index])


  loadTasks()


  closeSubmitModal()

}


/* =========================================================
   CLEAR FILTERS
========================================================= */

const clearFilters = () => {

  searchQuery.value = ''

  selectedStatus.value = 'All'

  selectedPriority.value = 'All'

}


/* =========================================================
   STATUS COLORS
========================================================= */

const statusClass = status => {

  const classes = {

    Pending:
      'bg-amber-100 text-amber-700',

    Assigned:
      'bg-slate-100 text-slate-700',

    'In Progress':
      'bg-blue-100 text-blue-700',

    Submitted:
      'bg-indigo-100 text-indigo-700',

    'For Verification':
      'bg-purple-100 text-purple-700',

    Returned:
      'bg-yellow-100 text-yellow-700',

    Verified:
      'bg-green-100 text-green-700',

    Completed:
      'bg-green-100 text-green-700',

    Overdue:
      'bg-red-100 text-red-700'

  }

  return (
    classes[status] ||
    'bg-slate-100 text-slate-700'
  )

}


/* =========================================================
   PRIORITY COLORS
========================================================= */

const priorityClass = priority => {

  const classes = {

    High:
      'bg-red-100 text-red-700',

    Medium:
      'bg-amber-100 text-amber-700',

    Low:
      'bg-green-100 text-green-700'

  }

  return (
    classes[priority] ||
    'bg-slate-100 text-slate-700'
  )

}


/* =========================================================
   PRIORITY ICON BACKGROUND
========================================================= */

const priorityIconBg = priority => {

  const classes = {

    High:
      'bg-red-100',

    Medium:
      'bg-amber-100',

    Low:
      'bg-green-100'

  }

  return (
    classes[priority] ||
    'bg-blue-100'
  )

}


/* =========================================================
   PRIORITY ICON COLOR
========================================================= */

const priorityIconColor = priority => {

  const classes = {

    High:
      'text-red-600',

    Medium:
      'text-amber-600',

    Low:
      'text-green-600'

  }

  return (
    classes[priority] ||
    'text-blue-600'
  )

}


/* =========================================================
   PROGRESS COLOR
========================================================= */

const progressClass = status => {

  const classes = {

    Pending:
      'bg-amber-500',

    'In Progress':
      'bg-blue-600',

    Submitted:
      'bg-indigo-600',

    Completed:
      'bg-green-600',

    Overdue:
      'bg-red-600'

  }

  return (
    classes[status] ||
    'bg-[#8B1E23]'
  )

}


/* =========================================================
   REAL-TIME SYNC
   ADMIN + PERSONNEL SHARE SAME LOCAL STORAGE.
========================================================= */

let syncInterval = null


onMounted(() => {

  loadTasks()


  /*
    Storage event:
    Works when Admin and Personnel are open
    in different browser tabs/windows.
  */

  window.addEventListener(
    'storage',
    loadTasks
  )


  /*
    Polling:
    Also detects changes when both interfaces
    are running in the same browser tab/app.
  */

  syncInterval =
    setInterval(
      loadTasks,
      1000
    )

})


onBeforeUnmount(() => {

  window.removeEventListener(
    'storage',
    loadTasks
  )


  if (syncInterval) {

    clearInterval(
      syncInterval
    )

  }

})
</script>