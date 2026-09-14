<template>
  <div class="w-full min-w-0 space-y-6">

    <!-- ========================================================= -->
    <!-- HEADER -->
    <!-- ========================================================= -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">
        <div>
          <p class="text-sm font-semibold text-[#8B1E23]">
            FIRENOTIFY PERSONNEL PORTAL
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Support Center
          </h2>

          <p class="text-sm text-slate-500 mt-1 max-w-2xl">
            Get help with tasks, reports, activities, equipment, and your
            personnel account.
          </p>
        </div>

        <div
          class="h-14 w-14 rounded-2xl bg-[#8B1E23]/10 flex items-center justify-center"
        >
          <span
            v-html="ICONS.support"
            class="h-8 w-8 text-[#8B1E23]"
          ></span>
        </div>
      </div>
    </section>


    <!-- ========================================================= -->
    <!-- SUPPORT CATEGORIES -->
    <!-- ========================================================= -->
    <section class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-5">

      <button
        v-for="category in supportCategories"
        :key="category.title"
        @click="selectIssueType(category.issueType)"
        class="text-left bg-white border border-slate-200 rounded-2xl p-5 shadow-sm hover:shadow-md hover:border-slate-300 transition"
      >
        <div class="flex items-center gap-3">

          <div
            :class="[
              'h-11 w-11 rounded-xl flex items-center justify-center',
              category.bg
            ]"
          >
            <span
              v-html="ICONS[category.icon]"
              :class="['h-5 w-5', category.color]"
            ></span>
          </div>

          <div>
            <p class="text-sm font-bold text-slate-900">
              {{ category.title }}
            </p>

            <p class="text-xs text-slate-500 mt-1">
              {{ category.description }}
            </p>
          </div>

        </div>
      </button>

    </section>


    <!-- ========================================================= -->
    <!-- FAQ + CONTACT -->
    <!-- ========================================================= -->
    <section class="grid grid-cols-1 lg:grid-cols-3 gap-6">

      <!-- FAQ -->
      <div class="lg:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="border-b border-slate-200 pb-4">
          <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">

            <div>
              <h3 class="text-lg font-bold text-slate-900">
                Frequently Asked Questions
              </h3>

              <p class="text-sm text-slate-500 mt-1">
                Quick answers for common portal tasks.
              </p>
            </div>

            <div class="relative w-full sm:w-64">

              <svg
                class="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-slate-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="m21 21-4.35-4.35m2.1-5.4a7.5 7.5 0 1 1-15 0 7.5 7.5 0 0 1 15 0Z"
                />
              </svg>

              <input
                v-model="faqSearch"
                type="text"
                placeholder="Search FAQs..."
                class="w-full pl-9 pr-3 py-2.5 rounded-xl border border-slate-300 text-sm outline-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
              />

            </div>

          </div>
        </div>


        <div class="mt-5 space-y-3">

          <div
            v-for="faq in filteredFaqs"
            :key="faq.id"
            class="rounded-xl border border-slate-200 overflow-hidden"
          >

            <button
              @click="toggleFaq(faq.id)"
              class="w-full flex items-center justify-between gap-4 p-4 text-left bg-slate-50 hover:bg-slate-100 transition"
            >

              <div class="flex items-start gap-3">

                <div
                  class="mt-0.5 h-8 w-8 rounded-lg bg-[#8B1E23]/10 flex items-center justify-center flex-shrink-0"
                >
                  <span
                    v-html="ICONS.support"
                    class="h-4 w-4 text-[#8B1E23]"
                  ></span>
                </div>

                <span class="font-semibold text-sm text-slate-900">
                  {{ faq.question }}
                </span>

              </div>

              <svg
                class="h-5 w-5 text-slate-400 flex-shrink-0 transition-transform"
                :class="{ 'rotate-180': openFaq === faq.id }"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="m19 9-7 7-7-7"
                />
              </svg>

            </button>


            <div
              v-if="openFaq === faq.id"
              class="px-4 pb-4 pt-1 bg-white"
            >
              <p class="text-sm leading-6 text-slate-500">
                {{ faq.answer }}
              </p>

              <button
                @click="selectIssueType(faq.issueType)"
                class="mt-3 text-xs font-bold text-[#8B1E23] hover:underline"
              >
                Need more help? Submit a request →
              </button>
            </div>

          </div>


          <div
            v-if="filteredFaqs.length === 0"
            class="text-center py-10"
          >
            <div
              class="mx-auto h-12 w-12 rounded-full bg-slate-100 flex items-center justify-center"
            >
              <svg
                class="h-6 w-6 text-slate-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="m21 21-4.35-4.35m2.1-5.4a7.5 7.5 0 1 1-15 0 7.5 7.5 0 0 1 15 0Z"
                />
              </svg>
            </div>

            <p class="mt-3 text-sm font-semibold text-slate-700">
              No FAQs found
            </p>

            <p class="text-xs text-slate-500 mt-1">
              Try a different search term.
            </p>
          </div>

        </div>

      </div>


      <!-- CONTACT SUPPORT -->
      <div class="space-y-6">

        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <h3 class="text-lg font-bold text-slate-900">
            Contact Support
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            Our station support team can assist with portal issues.
          </p>


          <div class="mt-5 space-y-4">

            <div>
              <p class="text-xs text-slate-500">
                Support Office
              </p>

              <p class="font-semibold text-slate-900 mt-1">
                BFP Balingasag Station Office
              </p>
            </div>

            <div>
              <p class="text-xs text-slate-500">
                Office Hours
              </p>

              <p class="font-semibold text-slate-900 mt-1">
                Monday - Friday
              </p>

              <p class="text-xs text-slate-500 mt-1">
                08:00 AM - 05:00 PM
              </p>
            </div>

            <div>
              <p class="text-xs text-slate-500">
                Expected Response
              </p>

              <p class="font-semibold text-green-600 mt-1">
                Within one business day
              </p>
            </div>

          </div>

        </div>


        <!-- REQUEST STATS -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <h3 class="text-lg font-bold text-slate-900">
            My Support Requests
          </h3>

          <div class="mt-5 grid grid-cols-2 gap-3">

            <div class="rounded-xl bg-slate-50 border border-slate-200 p-4">
              <p class="text-xs text-slate-500">
                Total
              </p>

              <p class="text-2xl font-bold text-slate-900 mt-1">
                {{ requests.length }}
              </p>
            </div>

            <div class="rounded-xl bg-yellow-50 border border-yellow-100 p-4">
              <p class="text-xs text-yellow-700">
                Pending
              </p>

              <p class="text-2xl font-bold text-yellow-800 mt-1">
                {{ pendingRequests }}
              </p>
            </div>

            <div class="rounded-xl bg-blue-50 border border-blue-100 p-4">
              <p class="text-xs text-blue-700">
                In Progress
              </p>

              <p class="text-2xl font-bold text-blue-800 mt-1">
                {{ inProgressRequests }}
              </p>
            </div>

            <div class="rounded-xl bg-green-50 border border-green-100 p-4">
              <p class="text-xs text-green-700">
                Resolved
              </p>

              <p class="text-2xl font-bold text-green-800 mt-1">
                {{ resolvedRequests }}
              </p>
            </div>

          </div>

        </div>

      </div>

    </section>


    <!-- ========================================================= -->
    <!-- SUBMIT SUPPORT REQUEST -->
    <!-- ========================================================= -->
    <section
      ref="requestSection"
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div class="border-b border-slate-200 pb-4">

        <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">

          <div>
            <h3 class="text-lg font-bold text-slate-900">
              Submit a Support Request
            </h3>

            <p class="text-sm text-slate-500 mt-1">
              Describe the issue so the support team can assist you.
            </p>
          </div>

          <span
            v-if="formChanged"
            class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-yellow-50 text-yellow-700 text-xs font-bold"
          >
            <span class="h-2 w-2 rounded-full bg-yellow-500"></span>
            Unsaved request
          </span>

        </div>

      </div>


      <form
        @submit.prevent="submitRequest"
        class="mt-5 grid grid-cols-1 lg:grid-cols-2 gap-5"
      >

        <!-- ISSUE TYPE -->
        <div>

          <label class="text-sm font-semibold text-slate-700">
            Issue Type
            <span class="text-[#8B1E23]">*</span>
          </label>

          <select
            v-model="form.issueType"
            class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm text-slate-700 outline-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
          >
            <option value="">
              Select issue type
            </option>

            <option>
              Account Access
            </option>

            <option>
              Task or Activity
            </option>

            <option>
              Report Submission
            </option>

            <option>
              Equipment Record
            </option>

            <option>
              Station Duty Log
            </option>

            <option>
              Notifications
            </option>

            <option>
              Other
            </option>
          </select>

        </div>


        <!-- PRIORITY -->
        <div>

          <label class="text-sm font-semibold text-slate-700">
            Priority
            <span class="text-[#8B1E23]">*</span>
          </label>

          <select
            v-model="form.priority"
            class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm text-slate-700 outline-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
          >
            <option>
              Normal
            </option>

            <option>
              High
            </option>

            <option>
              Urgent
            </option>
          </select>

        </div>


        <!-- SUBJECT -->
        <div class="lg:col-span-2">

          <label class="text-sm font-semibold text-slate-700">
            Subject
            <span class="text-[#8B1E23]">*</span>
          </label>

          <input
            v-model="form.subject"
            type="text"
            maxlength="100"
            placeholder="Example: Unable to submit accomplishment report"
            class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm text-slate-700 outline-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
          />

          <p class="text-xs text-slate-400 text-right mt-1">
            {{ form.subject.length }}/100
          </p>

        </div>


        <!-- MESSAGE -->
        <div class="lg:col-span-2">

          <div class="flex items-center justify-between">

            <label class="text-sm font-semibold text-slate-700">
              Message
              <span class="text-[#8B1E23]">*</span>
            </label>

            <span class="text-xs text-slate-400">
              {{ form.message.length }}/1000
            </span>

          </div>

          <textarea
            v-model="form.message"
            rows="5"
            maxlength="1000"
            placeholder="Describe your concern, what happened, and what assistance you need..."
            class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm text-slate-700 outline-none resize-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
          ></textarea>

        </div>


        <!-- INFO -->
        <div class="lg:col-span-2">

          <div class="rounded-xl bg-slate-50 border border-slate-200 p-4">

            <div class="flex items-start gap-3">

              <div
                class="h-9 w-9 rounded-lg bg-blue-50 flex items-center justify-center flex-shrink-0"
              >
                <svg
                  class="h-5 w-5 text-blue-600"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M13 16h-1v-4h-1m1-4h.01M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20Z"
                  />
                </svg>
              </div>

              <div>
                <p class="text-sm font-semibold text-slate-800">
                  Before submitting
                </p>

                <p class="text-xs text-slate-500 mt-1 leading-5">
                  Include the affected module, what you were trying to do,
                  and any error message you received.
                </p>
              </div>

            </div>

          </div>

        </div>


        <!-- BUTTONS -->
        <div class="lg:col-span-2 flex flex-col sm:flex-row justify-end gap-3">

          <button
            type="button"
            @click="resetForm"
            :disabled="!formChanged"
            class="px-5 py-3 rounded-xl border border-slate-300 text-slate-600 text-sm font-bold hover:bg-slate-50 disabled:opacity-40 disabled:cursor-not-allowed transition"
          >
            Clear
          </button>

          <button
            type="submit"
            :disabled="submitting"
            class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D] disabled:opacity-60 disabled:cursor-not-allowed transition flex items-center justify-center gap-2"
          >

            <svg
              v-if="submitting"
              class="animate-spin h-4 w-4"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                class="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                stroke-width="4"
              ></circle>

              <path
                class="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"
              ></path>
            </svg>

            {{ submitting ? 'Sending...' : 'Send Support Request' }}

          </button>

        </div>

      </form>

    </section>


    <!-- ========================================================= -->
    <!-- REQUEST HISTORY -->
    <!-- ========================================================= -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

        <div>
          <h3 class="text-lg font-bold text-slate-900">
            My Support Requests
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            Track the status of your submitted concerns.
          </p>
        </div>

        <select
          v-model="requestFilter"
          class="px-4 py-2.5 rounded-xl border border-slate-300 bg-white text-sm text-slate-700 outline-none focus:ring-2 focus:ring-[#8B1E23]/20"
        >
          <option value="All">All Requests</option>
          <option value="Pending">Pending</option>
          <option value="In Progress">In Progress</option>
          <option value="Resolved">Resolved</option>
          <option value="Cancelled">Cancelled</option>
        </select>

      </div>


      <div class="mt-5 overflow-x-auto">

        <table class="w-full min-w-[760px]">

          <thead>
            <tr class="border-b border-slate-200 text-left">

              <th class="pb-3 text-xs font-bold uppercase tracking-wide text-slate-500">
                Request
              </th>

              <th class="pb-3 text-xs font-bold uppercase tracking-wide text-slate-500">
                Type
              </th>

              <th class="pb-3 text-xs font-bold uppercase tracking-wide text-slate-500">
                Priority
              </th>

              <th class="pb-3 text-xs font-bold uppercase tracking-wide text-slate-500">
                Status
              </th>

              <th class="pb-3 text-xs font-bold uppercase tracking-wide text-slate-500">
                Date
              </th>

              <th class="pb-3 text-xs font-bold uppercase tracking-wide text-slate-500 text-right">
                Action
              </th>

            </tr>
          </thead>


          <tbody class="divide-y divide-slate-100">

            <tr
              v-for="request in filteredRequests"
              :key="request.id"
              class="hover:bg-slate-50 transition"
            >

              <td class="py-4">

                <div>
                  <p class="text-sm font-bold text-slate-900">
                    {{ request.subject }}
                  </p>

                  <p class="text-xs text-slate-500 mt-1">
                    {{ request.id }}
                  </p>
                </div>

              </td>


              <td class="py-4 text-sm text-slate-600">
                {{ request.issueType }}
              </td>


              <td class="py-4">

                <span
                  :class="getPriorityClass(request.priority)"
                  class="inline-flex px-2.5 py-1 rounded-full text-xs font-bold"
                >
                  {{ request.priority }}
                </span>

              </td>


              <td class="py-4">

                <span
                  :class="getStatusClass(request.status)"
                  class="inline-flex px-2.5 py-1 rounded-full text-xs font-bold"
                >
                  {{ request.status }}
                </span>

              </td>


              <td class="py-4 text-sm text-slate-500">
                {{ request.date }}
              </td>


              <td class="py-4">

                <div class="flex justify-end gap-2">

                  <button
                    @click="viewRequest(request)"
                    class="px-3 py-2 rounded-lg border border-slate-200 text-xs font-bold text-slate-600 hover:bg-slate-100"
                  >
                    View
                  </button>

                  <button
                    v-if="request.status === 'Pending'"
                    @click="cancelRequest(request.id)"
                    class="px-3 py-2 rounded-lg border border-red-200 text-xs font-bold text-red-600 hover:bg-red-50"
                  >
                    Cancel
                  </button>

                </div>

              </td>

            </tr>

          </tbody>

        </table>


        <div
          v-if="filteredRequests.length === 0"
          class="text-center py-12"
        >
          <div
            class="mx-auto h-12 w-12 rounded-full bg-slate-100 flex items-center justify-center"
          >
            <svg
              class="h-6 w-6 text-slate-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M8 10h8m-8 4h5m7-2a8 8 0 1 1-16 0 8 8 0 0 1 16 0Z"
              />
            </svg>
          </div>

          <p class="mt-3 text-sm font-semibold text-slate-700">
            No support requests found
          </p>

          <p class="text-xs text-slate-500 mt-1">
            Your submitted requests will appear here.
          </p>
        </div>

      </div>

    </section>


    <!-- ========================================================= -->
    <!-- REQUEST DETAILS MODAL -->
    <!-- ========================================================= -->
    <div
      v-if="selectedRequest"
      class="fixed inset-0 z-50 bg-black/40 flex items-center justify-center p-4"
      @click.self="selectedRequest = null"
    >

      <div
        class="w-full max-w-2xl bg-white rounded-2xl shadow-2xl overflow-hidden"
      >

        <div class="px-6 py-5 border-b border-slate-200 flex items-center justify-between">

          <div>
            <p class="text-xs font-bold text-[#8B1E23] uppercase tracking-wide">
              Support Request
            </p>

            <h3 class="text-xl font-bold text-slate-900 mt-1">
              {{ selectedRequest.subject }}
            </h3>
          </div>

          <button
            @click="selectedRequest = null"
            class="h-9 w-9 rounded-lg hover:bg-slate-100 text-slate-500"
          >
            ✕
          </button>

        </div>


        <div class="p-6 space-y-5">

          <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">

            <div class="rounded-xl bg-slate-50 p-3">
              <p class="text-xs text-slate-500">
                Request ID
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedRequest.id }}
              </p>
            </div>

            <div class="rounded-xl bg-slate-50 p-3">
              <p class="text-xs text-slate-500">
                Type
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedRequest.issueType }}
              </p>
            </div>

            <div class="rounded-xl bg-slate-50 p-3">
              <p class="text-xs text-slate-500">
                Priority
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedRequest.priority }}
              </p>
            </div>

            <div class="rounded-xl bg-slate-50 p-3">
              <p class="text-xs text-slate-500">
                Status
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedRequest.status }}
              </p>
            </div>

          </div>


          <div>
            <p class="text-xs font-bold uppercase tracking-wide text-slate-500">
              Message
            </p>

            <div class="mt-2 rounded-xl border border-slate-200 bg-slate-50 p-4">

              <p class="text-sm text-slate-700 leading-6 whitespace-pre-line">
                {{ selectedRequest.message }}
              </p>

            </div>
          </div>


          <div class="flex justify-end">

            <button
              @click="selectedRequest = null"
              class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]"
            >
              Close
            </button>

          </div>

        </div>

      </div>

    </div>


    <!-- ========================================================= -->
    <!-- TOAST -->
    <!-- ========================================================= -->
    <transition
      enter-active-class="transition duration-200"
      enter-from-class="opacity-0 translate-y-2"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition duration-200"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 translate-y-2"
    >

      <div
        v-if="toastMessage"
        class="fixed bottom-6 right-6 z-[60] bg-slate-900 text-white px-5 py-3 rounded-xl shadow-xl text-sm font-semibold"
      >
        {{ toastMessage }}
      </div>

    </transition>

  </div>
</template>


<script setup>
import { computed, onMounted, ref, watch } from 'vue'

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


/* =========================================================
   STORAGE
   ========================================================= */

const STORAGE_KEY = 'fireNotifyPersonnelSupportRequests'


/* =========================================================
   FORM
   ========================================================= */

const defaultForm = () => ({
  issueType: '',
  priority: 'Normal',
  subject: '',
  message: ''
})

const form = ref(defaultForm())

const submitting = ref(false)
const toastMessage = ref('')
const requestSection = ref(null)


/* =========================================================
   FAQ
   ========================================================= */

const faqSearch = ref('')
const openFaq = ref(null)

const faqs = ref([
  {
    id: 1,
    question: 'How do I update a task status?',
    answer:
      'Open Tasks from the sidebar, select the assigned activity, and use Update Status after completing the required duty.',
    issueType: 'Task or Activity'
  },
  {
    id: 2,
    question: 'How do I submit a report?',
    answer:
      'Open Reports, choose the pending report, complete the required information, attach supporting documentation when required, and submit the report.',
    issueType: 'Report Submission'
  },
  {
    id: 3,
    question: 'What should I do when equipment is damaged?',
    answer:
      'Open Equipment Audit and record the equipment condition, issue details, and recommended maintenance or replacement action.',
    issueType: 'Equipment Record'
  },
  {
    id: 4,
    question: 'Where can I view station duty records?',
    answer:
      'Open Station Duty Log to review your shifts, attendance, logged activities, and pending duty entries.',
    issueType: 'Station Duty Log'
  },
  {
    id: 5,
    question: 'Why am I not receiving notifications?',
    answer:
      'Check your notification settings and make sure task, report, and activity notifications are enabled. If the issue continues, submit a support request.',
    issueType: 'Notifications'
  },
  {
    id: 6,
    question: 'How do I update my account information?',
    answer:
      'Open Settings from the sidebar and update the available profile and portal preferences. For restricted account changes, contact station support.',
    issueType: 'Account Access'
  }
])


const filteredFaqs = computed(() => {
  const query = faqSearch.value.trim().toLowerCase()

  if (!query) {
    return faqs.value
  }

  return faqs.value.filter(faq =>
    `${faq.question} ${faq.answer} ${faq.issueType}`
      .toLowerCase()
      .includes(query)
  )
})


const toggleFaq = id => {
  openFaq.value = openFaq.value === id ? null : id
}


/* =========================================================
   SUPPORT CATEGORIES
   ========================================================= */

const supportCategories = [
  {
    title: 'Task Help',
    description: 'Assignments and status updates',
    issueType: 'Task or Activity',
    icon: 'tasks',
    bg: 'bg-blue-50',
    color: 'text-blue-600'
  },
  {
    title: 'Report Help',
    description: 'Submission and corrections',
    issueType: 'Report Submission',
    icon: 'reports',
    bg: 'bg-green-50',
    color: 'text-green-600'
  },
  {
    title: 'Activity Help',
    description: 'Schedules and duty activities',
    issueType: 'clock',
    bg: 'bg-yellow-50',
    color: 'text-yellow-600'
  },
  {
    title: 'Urgent Support',
    description: 'Immediate station assistance',
    issueType: 'Other',
    icon: 'siren',
    bg: 'bg-red-50',
    color: 'text-[#8B1E23]'
  }
]


/* =========================================================
   REQUESTS
   ========================================================= */

const requests = ref([])

const requestFilter = ref('All')
const selectedRequest = ref(null)


/* =========================================================
   LOAD SAVED REQUESTS
   ========================================================= */

onMounted(() => {
  const saved = localStorage.getItem(STORAGE_KEY)

  if (!saved) return

  try {
    const parsed = JSON.parse(saved)

    if (Array.isArray(parsed)) {
      requests.value = parsed
    }
  } catch (error) {
    console.error('Failed to load support requests:', error)
  }
})


/* =========================================================
   SAVE REQUESTS
   ========================================================= */

watch(
  requests,
  value => {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(value))
  },
  { deep: true }
)


/* =========================================================
   FORM STATE
   ========================================================= */

const formChanged = computed(() => {
  return (
    form.value.issueType !== '' ||
    form.value.priority !== 'Normal' ||
    form.value.subject.trim() !== '' ||
    form.value.message.trim() !== ''
  )
})


/* =========================================================
   REQUEST STATISTICS
   ========================================================= */

const pendingRequests = computed(() =>
  requests.value.filter(request => request.status === 'Pending').length
)

const inProgressRequests = computed(() =>
  requests.value.filter(request => request.status === 'In Progress').length
)

const resolvedRequests = computed(() =>
  requests.value.filter(request => request.status === 'Resolved').length
)


/* =========================================================
   FILTERED REQUESTS
   ========================================================= */

const filteredRequests = computed(() => {
  if (requestFilter.value === 'All') {
    return requests.value
  }

  return requests.value.filter(
    request => request.status === requestFilter.value
  )
})


/* =========================================================
   SELECT ISSUE TYPE
   ========================================================= */

const selectIssueType = issueType => {
  form.value.issueType = issueType

  setTimeout(() => {
    requestSection.value?.scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    })
  }, 50)

  showToast(`${issueType} selected`)
}


/* =========================================================
   SUBMIT REQUEST
   ========================================================= */

const submitRequest = async () => {

  if (!form.value.issueType) {
    showToast('Please select an issue type.')
    return
  }

  if (!form.value.subject.trim()) {
    showToast('Please enter a subject.')
    return
  }

  if (!form.value.message.trim()) {
    showToast('Please describe your concern.')
    return
  }

  if (form.value.message.trim().length < 10) {
    showToast('Please provide more details about the issue.')
    return
  }

  submitting.value = true

  await new Promise(resolve => setTimeout(resolve, 700))

  const request = {
    id: `SUP-${Date.now().toString().slice(-6)}`,
    issueType: form.value.issueType,
    priority: form.value.priority,
    subject: form.value.subject.trim(),
    message: form.value.message.trim(),
    status: 'Pending',
    date: formatDate(new Date()),
    submittedBy:
      props.currentUser?.name ||
      props.currentUser?.fullName ||
      props.currentUser?.identifier ||
      'Current Personnel'
  }

  requests.value.unshift(request)

  resetForm()

  submitting.value = false

  showToast(`Support request ${request.id} submitted successfully.`)
}


/* =========================================================
   RESET FORM
   ========================================================= */

const resetForm = () => {
  form.value = defaultForm()
}


/* =========================================================
   VIEW REQUEST
   ========================================================= */

const viewRequest = request => {
  selectedRequest.value = request
}


/* =========================================================
   CANCEL REQUEST
   ========================================================= */

const cancelRequest = id => {

  const request = requests.value.find(item => item.id === id)

  if (!request) return

  request.status = 'Cancelled'

  showToast('Support request cancelled.')
}


/* =========================================================
   STATUS STYLES
   ========================================================= */

const getStatusClass = status => {

  const classes = {
    Pending: 'bg-yellow-50 text-yellow-700',
    'In Progress': 'bg-blue-50 text-blue-700',
    Resolved: 'bg-green-50 text-green-700',
    Cancelled: 'bg-slate-100 text-slate-600'
  }

  return classes[status] || 'bg-slate-100 text-slate-600'
}


const getPriorityClass = priority => {

  const classes = {
    Normal: 'bg-slate-100 text-slate-600',
    High: 'bg-orange-50 text-orange-700',
    Urgent: 'bg-red-50 text-red-700'
  }

  return classes[priority] || 'bg-slate-100 text-slate-600'
}


/* =========================================================
   DATE
   ========================================================= */

const formatDate = date => {

  return new Intl.DateTimeFormat('en-PH', {
    year: 'numeric',
    month: 'short',
    day: '2-digit'
  }).format(date)
}


/* =========================================================
   TOAST
   ========================================================= */

let toastTimer = null

const showToast = message => {

  toastMessage.value = message

  clearTimeout(toastTimer)

  toastTimer = setTimeout(() => {
    toastMessage.value = ''
  }, 3000)
}
</script>