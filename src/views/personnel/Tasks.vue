<template>
  <div class="w-full min-w-0 space-y-4">

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
    <section class="fn-operations-summary">

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
        <section class="fn-operations-panel">

      <div class="fn-operations-heading">

        <div>
          <h3 class="text-base font-bold text-slate-900">
            Assigned Tasks
          </h3>

          <p class="text-xs text-slate-500 mt-1">
            Tasks assigned by the administrator.
          </p>
        </div>

        <span v-if="hasLoadedTasks" class="text-xs font-semibold text-slate-600">{{ filteredTasks.length }} tasks</span>
        <span v-else class="text-xs font-semibold text-slate-500">Loading tasks...</span>

      </div>

      <div class="flex gap-2 border-b border-slate-200 px-5 pt-4">
        <button type="button" @click="taskView = 'active'" class="border-b-2 px-4 py-3 text-sm font-bold" :class="taskView === 'active' ? 'border-[#8B1E23] text-[#8B1E23]' : 'border-transparent text-slate-500'">
          Active Tasks <span class="ml-1 text-xs">{{ activeTaskCount }}</span>
        </button>
        <button type="button" @click="taskView = 'archived'" class="border-b-2 px-4 py-3 text-sm font-bold" :class="taskView === 'archived' ? 'border-[#8B1E23] text-[#8B1E23]' : 'border-transparent text-slate-500'">
          Archived Tasks <span class="ml-1 text-xs">{{ archivedTaskCount }}</span>
        </button>
      </div>

      <div class="fn-operations-table-wrap">
        <table class="fn-operations-table">
          <thead>
            <tr><th>Task</th><th>Assigned To</th><th>Location</th><th>Deadline</th><th>Priority</th><th>Status</th><th class="text-right">Actions</th></tr>
          </thead>
          <tbody>
            <tr v-for="task in filteredTasks" :key="task.id">
              <td data-label="Task">
                <div class="flex min-w-0 flex-col gap-1">
                  <p class="break-words text-sm font-semibold leading-5 text-slate-900">{{ task.title }}</p>
                  <p v-if="task.subtopic" class="break-words text-xs leading-5 text-slate-600">{{ task.subtopic }}</p>
                  <p v-if="task.description" class="break-words whitespace-pre-wrap text-xs leading-5 text-slate-500">{{ task.description }}</p>
                  <p v-if="task.status === 'Returned' && task.revisionNote" class="break-words whitespace-pre-wrap text-xs font-semibold leading-5 text-amber-700">Revision requested: {{ task.revisionNote }}</p>
                </div>
              </td>
              <td data-label="Assigned To"><span class="block min-w-0 break-words leading-5">{{ task.assignedToName || props.currentUser?.name || [props.currentUser?.firstName, props.currentUser?.lastName].filter(Boolean).join(' ') || task.assignedToUsername || 'You' }}</span></td>
              <td data-label="Location"><span class="block min-w-0 break-words leading-5">{{ task.location || 'Not specified' }}</span></td>
              <td data-label="Schedule">
                <div class="flex flex-col gap-0.5">
                  <span class="leading-5">{{ formatOperationDate(task.due || task.dueDate) }}</span>
                  <span class="text-xs leading-5 text-slate-500">{{ formatOperationTime(task.time) }}</span>
                </div>
              </td>
              <td data-label="Priority"><span class="fn-operations-badge" :class="priorityClass(task.priority)">{{ task.priority || 'Medium' }}</span></td>
              <td data-label="Status">
                <span class="fn-operations-badge" :class="statusClass(task.status)">{{ task.status }}</span>
                <span class="mt-1 block text-xs text-slate-500">{{ task.progress || 0 }}% complete</span>
                <span class="mt-1 block h-1.5 overflow-hidden rounded-full bg-slate-100"><span class="block h-full" :class="progressClass(task.status)" :style="{ width: `${task.progress || 0}%` }"></span></span>
              </td>
              <td data-label="Actions">
                <div class="flex flex-wrap gap-1.5 sm:justify-end">
                  <template v-if="taskView === 'archived'">
                    <button type="button" v-if="['For Verification', 'Verified', 'Returned'].includes(task.status)" @click="openTaskSubmission(task)" class="fn-operations-action">View Submission</button>
                    <button type="button" @click="restoreTask(task)" class="fn-operations-action">Restore</button>
                    <button type="button" @click="requestDeleteTask(task)" class="fn-operations-action fn-operations-action--danger">Delete</button>
                  </template>
                  <template v-else>
                    <button type="button" v-if="!['For Verification', 'Verified', 'Completed', 'Returned'].includes(task.status)" @click="viewDetails(task)" class="fn-operations-action">View</button>
                    <button type="button" v-if="['For Verification', 'Verified'].includes(task.status)" @click="openTaskSubmission(task)" class="fn-operations-action">View Submission</button>
                    <button type="button" v-if="['Pending', 'Assigned', 'Overdue', 'In Progress', 'Returned'].includes(task.status)" @click="openSubmitModal(task)" class="fn-operations-action fn-operations-action--primary">{{ task.status === 'Returned' ? 'Revise' : 'Submit Task' }}</button>
                    <button type="button" @click="archiveTask(task)" class="fn-operations-action">Archive</button>
                    <button type="button" @click="requestDeleteTask(task)" class="fn-operations-action fn-operations-action--danger">Delete</button>
                  </template>
                </div>
              </td>
            </tr>
            <tr v-if="!hasLoadedTasks">
              <td colspan="7" class="px-4 py-8 text-center text-sm text-slate-500">Loading tasks...</td>
            </tr>
            <tr v-else-if="!filteredTasks.length">
              <td colspan="7" class="px-4 py-8 text-center">
                <p class="font-bold text-slate-700">No tasks found</p>
                <p class="mt-1 text-sm text-slate-500">Try changing your search or filters.</p>
                <button @click="clearFilters" class="mt-3 fn-operations-action">Clear Filters</button>
              </td>
            </tr>
          </tbody>
        </table>
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
                {{ formatOperationDate(selectedTask.due || selectedTask.dueDate) }}
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
            v-if="['Submitted', 'For Verification', 'Verified', 'Returned'].includes(selectedTask.status)"
            class="p-4 rounded-xl bg-blue-50 border border-blue-100"
          >

            <p class="text-sm font-bold text-blue-800">
              Task Submitted
            </p>

            <p class="text-sm text-blue-700 mt-1">
              {{ selectedTask.accomplishment || selectedTask.submissionNote || 'Submitted successfully.' }}
            </p>

            <p v-if="selectedTask.submittedAt" class="mt-2 flex flex-col gap-0.5 text-xs leading-5 text-blue-600">
              <span>Submitted</span>
              <span>{{ formatOperationDate(selectedTask.submittedAt) }}</span>
              <span v-if="hasTimeValue(selectedTask.submittedAt)">{{ formatOperationTime(selectedTask.submittedAt) }}</span>
            </p>

          </div>

          <div v-if="['Submitted', 'For Verification', 'Verified', 'Returned'].includes(selectedTask.status)" class="rounded-xl border border-slate-200 p-4">
            <p class="text-xs font-bold uppercase tracking-wide text-slate-500">Evidence Photos</p>
            <div v-if="taskSubmissionEvidence.length" class="mt-3 grid grid-cols-2 gap-3 md:grid-cols-3">
              <a v-for="(item, index) in taskSubmissionEvidence" :key="item.id" :href="taskSubmissionEvidenceUrls[index]" target="_blank" rel="noreferrer" class="overflow-hidden rounded-lg border border-slate-200 bg-slate-50">
                <img :src="taskSubmissionEvidenceUrls[index]" :alt="item.filename || 'Task evidence photo'" class="h-32 w-full object-cover" />
                <span class="block truncate px-2 py-1.5 text-xs text-slate-600">{{ item.filename || 'Evidence' }}</span>
              </a>
            </div>
            <p v-else class="mt-2 text-sm text-slate-500">No evidence photos submitted.</p>
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
            v-if="['Pending', 'Assigned', 'Overdue', 'In Progress', 'Returned'].includes(selectedTask.status)"
            @click="openSubmitModal(selectedTask)"
            class="px-5 py-3 rounded-xl bg-[#8B1E23]
                   text-white text-sm font-bold
                   hover:bg-[#72181D]"
          >
            {{ selectedTask.status === 'Returned' ? 'Revise Submission' : 'Submit Task' }}
          </button>

        </div>

      </div>

    </div>


    <div
      v-if="pendingDeleteTask"
      class="fixed inset-0 z-[75] flex items-center justify-center bg-slate-900/50 p-4"
      @click.self="pendingDeleteTask = null"
    >
      <div class="w-full max-w-md rounded-2xl bg-white p-6 shadow-xl">
        <p class="text-xs font-bold uppercase tracking-wide text-[#8B1E23]">Task Action</p>
        <h3 class="mt-2 text-xl font-bold text-slate-900">
          {{ taskView === 'active' ? 'Move Task to Archive?' : 'Remove Task Assignment?' }}
        </h3>
        <p class="mt-2 text-sm text-slate-600">
          <template v-if="taskView === 'active'">
            Move <strong>{{ pendingDeleteTask.title }}</strong> to your Archived Tasks? Admin's task will remain unchanged.
          </template>
          <template v-else>
            Remove <strong>{{ pendingDeleteTask.title }}</strong> from your assignments? The shared task and submission evidence will remain intact.
          </template>
        </p>
        <div class="mt-6 flex justify-end gap-3">
          <button type="button" @click="pendingDeleteTask = null" class="rounded-xl border border-slate-300 px-5 py-2.5 font-semibold text-slate-700">Cancel</button>
          <button type="button" :disabled="taskActionPending" @click="deleteTask(pendingDeleteTask)" class="rounded-xl bg-[#8B1E23] px-5 py-2.5 font-bold text-white disabled:cursor-wait disabled:opacity-60">
            {{ taskActionPending ? 'Saving...' : taskView === 'active' ? 'Move to Archive' : 'Remove Assignment' }}
          </button>
        </div>
      </div>
    </div>

    <!-- =========================================================
         SUBMIT TASK MODAL
    ========================================================== -->
    <div
      v-if="submitTask"
      class="fixed inset-0 z-[60] bg-slate-900/60 backdrop-blur-sm flex items-center justify-center p-4"
      @click.self="closeSubmitModal"
    >

      <div class="fn-modal-panel flex max-h-[calc(100dvh-2rem)] w-full max-w-2xl flex-col overflow-hidden rounded-2xl bg-white shadow-2xl">

        <div class="fn-modal-header shrink-0 bg-[#8B1E23] p-6 text-white">

          <div class="flex items-start justify-between gap-4">
            <div class="min-w-0">
              <p class="fn-modal-header-label text-xs font-bold uppercase tracking-wide">
                Task Submission
              </p>

              <h3 class="mt-1 text-2xl font-bold text-white">
                {{ submitTask.status === 'Returned' ? 'Revise Task Submission' : 'Submit Task' }}
              </h3>

              <p class="fn-modal-header-description mt-1 break-words text-sm">
                {{ submitTask.title }}
              </p>

              <span class="mt-3 inline-flex rounded-full bg-white/15 px-3 py-1 text-xs font-semibold text-white">
                {{ submitTask.status }}
              </span>
            </div>

            <button
              type="button"
              @click="closeSubmitModal"
              class="h-9 w-9 shrink-0 rounded-lg bg-white/10 text-white hover:bg-white/20"
              aria-label="Close task submission"
            >
              ✕
            </button>
          </div>

        </div>


        <div class="min-h-0 flex-1 space-y-5 overflow-y-auto overscroll-contain p-6">

          <div>
            <label class="mb-2 block text-sm font-bold text-slate-700">
              Accomplishment / Work Summary
              <span class="text-[#8B1E23]">*</span>
            </label>

            <textarea
              v-model="accomplishment"
              rows="5"
              placeholder="Describe the work completed, observations, and outcomes."
              class="w-full resize-none rounded-xl border border-slate-300 px-4 py-3 text-sm focus:border-[#8B1E23] focus:outline-none focus:ring-2 focus:ring-[#8B1E23]/20"
            ></textarea>

            <p class="mt-2 text-xs text-slate-500">
              Provide the work completed for Admin verification.
            </p>
          </div>

          <div>
            <label class="mb-2 block text-sm font-bold text-slate-700">
              Remarks <span class="font-normal text-slate-400">(Optional)</span>
            </label>

            <textarea
              v-model="submissionRemarks"
              rows="3"
              placeholder="Remarks (optional)"
              class="w-full resize-none rounded-xl border border-slate-300 px-4 py-3 text-sm focus:border-[#8B1E23] focus:outline-none focus:ring-2 focus:ring-[#8B1E23]/20"
            ></textarea>
          </div>

          <div>
            <label class="mb-2 block text-sm font-bold text-slate-700">
              Evidence Photos <span class="font-normal text-slate-400">(optional)</span>
            </label>

            <input
              type="file"
              multiple
              accept=".jpg,.jpeg,.png,.webp,image/jpeg,image/png,image/webp"
              @change="handleEvidenceSelection"
              class="block w-full text-sm text-slate-600 file:mr-4 file:rounded-xl file:border-0 file:bg-[#8B1E23] file:px-4 file:py-2.5 file:font-semibold file:text-white"
            />

            <div v-if="evidenceFiles.length" class="mt-3 grid grid-cols-2 gap-3 sm:grid-cols-3">
              <div v-for="(file, index) in evidenceFiles" :key="`${file.name}-${index}`" class="rounded-xl border border-slate-200 bg-slate-50 p-2">
                <img v-if="evidencePreviews[index]" :src="evidencePreviews[index]" :alt="file.name" class="h-24 w-full rounded-lg object-cover" />
                <p class="mt-2 truncate text-xs font-semibold text-slate-700">{{ file.name }}</p>
                <button type="button" @click="removeEvidence(index)" class="mt-1 text-xs font-bold text-[#8B1E23]">Remove</button>
              </div>
            </div>
          </div>

        </div>


        <div
          class="flex shrink-0 justify-end gap-3 border-t border-slate-200 bg-slate-50 px-6 py-5"
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

    <Transition name="toast">
      <div
        v-if="toastMessage"
        class="fixed bottom-6 right-6 z-[90] flex max-w-sm items-center gap-3 rounded-xl border border-slate-200 bg-white px-5 py-4 shadow-xl"
      >
        <div
          class="flex h-9 w-9 shrink-0 items-center justify-center rounded-full font-bold"
          :class="toastType === 'error' ? 'bg-red-100 text-red-600' : 'bg-green-100 text-green-600'"
        >
          {{ toastType === 'error' ? '!' : '✓' }}
        </div>
        <div>
          <p class="text-sm font-bold text-slate-900">
            {{ toastType === 'error' ? 'Action Failed' : 'Action Successful' }}
          </p>
          <p class="mt-0.5 text-xs text-slate-500">{{ toastMessage }}</p>
        </div>
      </div>
    </Transition>

  </div>
</template>


<script setup>
import {
  computed,
  onMounted,
  onBeforeUnmount,
  ref
} from 'vue'

import '../../styles/operations.css'
import { formatOperationDate, formatOperationTime } from '../../utils/operationsFormat.js'
import { getTaskActivityEvidence } from '../../utils/reportFileStorage.js'
import {
  deleteTaskActivityEvidence,
  saveTaskActivityEvidence
} from '../../utils/reportFileStorage.js'
import { getTaskArchiveIds, getTasks, removeTaskAssignment, setTaskArchive, updateTask } from '../../utils/taskService.js'
const hasTimeValue = value => /(?:T|\s)\d{1,2}:\d{2}/.test(String(value || ''))


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
const hasLoadedTasks = ref(false)
const taskView = ref('active')
const archivedTaskIds = ref(new Set())


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
const pendingDeleteTask = ref(null)
const taskActionPending = ref(false)
const taskSubmissionEvidence = ref([])
const taskSubmissionEvidenceUrls = ref([])


/* =========================================================
   SUBMISSION
========================================================= */

const submitTask = ref(null)
const accomplishment = ref('')
const submissionRemarks = ref('')
const evidenceFiles = ref([])
const evidencePreviews = ref([])
const toastMessage = ref('')
const toastType = ref('success')
let toastTimer = null

const showToast = (message, type = 'success') => {
  toastMessage.value = message
  toastType.value = type
  clearTimeout(toastTimer)
  toastTimer = setTimeout(() => {
    toastMessage.value = ''
  }, 3000)
}


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

/* =========================================================
   LOAD TASKS FROM ADMIN
========================================================= */

const loadTasks = async () => {
  const user = getCurrentUser()
  if (!user) {
    tasks.value = []
    archivedTaskIds.value = new Set()
    hasLoadedTasks.value = true
    return
  }

  try {
    const allTasks = await getTasks()
    tasks.value = allTasks.filter(task =>
      String(task.assignedToId) === String(user.id || user.userId) ||
      String(task.assignedToUsername || '').toLowerCase() === String(user.username || '').toLowerCase()
    )
    try {
      archivedTaskIds.value = new Set(await getTaskArchiveIds(user.id || user.userId))
    } catch (error) {
      archivedTaskIds.value = new Set()
      console.warn('Failed to load Personnel task archive state:', error)
    }
  } catch (error) {
    console.error('Failed to load FireNotify tasks from Django:', error)
    tasks.value = []
  } finally {
    hasLoadedTasks.value = true
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

    const isArchived = archivedTaskIds.value.has(String(task.id))
    const matchesArchiveView = taskView.value === 'archived' ? isArchived : !isArchived


    return (
      matchesSearch &&
      matchesStatus &&
      matchesPriority &&
      matchesArchiveView
    )

  })

})

const activeTaskCount = computed(() =>
  tasks.value.filter(task => !archivedTaskIds.value.has(String(task.id))).length
)

const archivedTaskCount = computed(() =>
  tasks.value.filter(task => archivedTaskIds.value.has(String(task.id))).length
)


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

const openTaskSubmission = async task => {
  taskSubmissionEvidenceUrls.value.forEach(url => URL.revokeObjectURL(url))
  taskSubmissionEvidenceUrls.value = []
  selectedTask.value = task
  try {
    taskSubmissionEvidence.value = await getTaskActivityEvidence({
      recordId: task.id,
      recordType: 'task'
    })
  } catch (error) {
    taskSubmissionEvidence.value = []
    console.error('Failed to load task submission evidence:', error)
  }
  taskSubmissionEvidenceUrls.value = taskSubmissionEvidence.value.map(item => URL.createObjectURL(item.file))
}


/* =========================================================
   CLOSE DETAILS
========================================================= */

const closeDetails = () => {

  selectedTask.value = null
  taskSubmissionEvidenceUrls.value.forEach(url => URL.revokeObjectURL(url))
  taskSubmissionEvidenceUrls.value = []
  taskSubmissionEvidence.value = []

}

const archiveTask = async task => {
  const user = getCurrentUser()
  const userId = user?.id || user?.userId
  if (userId === null || userId === undefined) {
    showToast('Unable to identify the current Personnel user.', 'error')
    return false
  }

  try {
    await setTaskArchive(task.id, userId, true)
    archivedTaskIds.value = new Set([...archivedTaskIds.value, String(task.id)])
    window.dispatchEvent(new CustomEvent('fireNotifyTasksUpdated'))
    showToast('Task archived for Personnel.')
    return true
  } catch (error) {
    showToast(error.message || 'Unable to archive task.', 'error')
    return false
  }
}

const restoreTask = async task => {
  const user = getCurrentUser()
  const userId = user?.id || user?.userId
  if (userId === null || userId === undefined) {
    showToast('Unable to identify the current Personnel user.', 'error')
    return
  }

  try {
    await setTaskArchive(task.id, userId, false)
    const archivedIds = new Set(archivedTaskIds.value)
    archivedIds.delete(String(task.id))
    archivedTaskIds.value = archivedIds
    window.dispatchEvent(new CustomEvent('fireNotifyTasksUpdated'))
    showToast('Task restored to your active tasks.')
  } catch (error) {
    showToast(error.message || 'Unable to restore task.', 'error')
  }
}

const requestDeleteTask = task => {
  pendingDeleteTask.value = task
}

const deleteTask = async task => {
  const user = getCurrentUser()
  const userId = user?.id || user?.userId
  if (!task || taskActionPending.value) return
  if (userId === null || userId === undefined) {
    showToast('Unable to identify the current Personnel user.', 'error')
    return
  }

  taskActionPending.value = true
  try {
    if (taskView.value === 'active') {
      await setTaskArchive(task.id, userId, true)
      archivedTaskIds.value = new Set([...archivedTaskIds.value, String(task.id)])
      pendingDeleteTask.value = null
      showToast('Task moved to your archive.')
    } else {
      await removeTaskAssignment(task.id, userId)
      tasks.value = tasks.value.filter(item => String(item.id) !== String(task.id))
      const archivedIds = new Set(archivedTaskIds.value)
      archivedIds.delete(String(task.id))
      archivedTaskIds.value = archivedIds
      pendingDeleteTask.value = null
      showToast('Task removed from your assignments.')
    }

    window.dispatchEvent(new CustomEvent('fireNotifyTasksUpdated'))
  } catch (error) {
    showToast(error.message || 'Unable to remove task assignment.', 'error')
  } finally {
    taskActionPending.value = false
  }
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
    showToast('Please select JPG, PNG, or WEBP image files only.', 'error')
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
    showToast('Please provide an accomplishment/work summary before submitting.', 'error')
    return
  }


  const user = getCurrentUser()


  await deleteTaskActivityEvidence({
    recordId: submitTask.value.id,
    recordType: 'task'
  })

  const evidence = await saveTaskActivityEvidence({
    recordId: submitTask.value.id,
    recordType: 'task',
    files: evidenceFiles.value
  })

  try {
    await updateTask(submitTask.value.id, {
      status: 'For Verification',
      progress: 90,
      accomplishment: accomplishment.value.trim()
    })
  } catch (error) {
    showToast(error.message || 'Unable to submit this task.', 'error')
    return
  }

  window.dispatchEvent(new CustomEvent('fireNotifyTasksUpdated'))

  await loadTasks()


  closeSubmitModal()
  showToast('Task submitted for verification.')

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

  window.addEventListener(
    'fireNotifyTasksUpdated',
    loadTasks
  )

})


onBeforeUnmount(() => {

  window.removeEventListener(
    'storage',
    loadTasks
  )

  window.removeEventListener(
    'fireNotifyTasksUpdated',
    loadTasks
  )

  if (toastTimer) clearTimeout(toastTimer)

})
</script>