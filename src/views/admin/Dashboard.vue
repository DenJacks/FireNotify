<script setup>
import { computed, ref } from 'vue'

const props = defineProps({
  currentUser: {
    type: Object,
    default: null
  }
})

/* =========================================================
   DASHBOARD DATA
   Frontend demo data - ready for Django API later
========================================================= */

const activities = ref([
  {
    id: 1,
    title: 'Fire Safety Inspection',
    assignedTo: 'FO3 Juan Dela Cruz',
    date: 'September 9, 2026',
    time: '8:00 AM',
    status: 'Ongoing',
    location: 'Balingasag Public Market',
    description:
      'Fire safety inspection of commercial establishments in the central district.'
  },
  {
    id: 2,
    title: 'Community Fire Drill',
    assignedTo: 'SFO1 M. Santos',
    date: 'September 10, 2026',
    time: '1:00 PM',
    status: 'Scheduled',
    location: 'Barangay San Roque',
    description:
      'Community evacuation and emergency response drill.'
  },
  {
    id: 3,
    title: 'Station Equipment Inspection',
    assignedTo: 'FO2 R. Reyes',
    date: 'September 11, 2026',
    time: '3:00 PM',
    status: 'Scheduled',
    location: 'BFP Balingasag Station',
    description:
      'Inspection and verification of station equipment readiness.'
  },
  {
    id: 4,
    title: 'Emergency Response Training',
    assignedTo: 'FO1 Carlo Reyes',
    date: 'September 12, 2026',
    time: '9:00 AM',
    status: 'Completed',
    location: 'BFP Training Room',
    description:
      'Emergency response and incident command training session.'
  }
])

const deadlines = ref([
  {
    id: 1,
    title: 'Fire Incident Report',
    due: 'Due today • 8:00 PM',
    status: 'Overdue',
    description: 'Incident report requires immediate administrative review.',
    color: 'red'
  },
  {
    id: 2,
    title: 'Weekly Accomplishment Report',
    due: 'Due tomorrow • 5:00 PM',
    status: 'Upcoming',
    description: 'Weekly accomplishment report from station personnel.',
    color: 'yellow'
  },
  {
    id: 3,
    title: 'Monthly Compliance Report',
    due: 'Due in 5 days',
    status: 'Upcoming',
    description: 'Monthly operations compliance report.',
    color: 'blue'
  }
])

const reports = ref([
  {
    id: 1,
    name: 'After-Operation Incident Report',
    submittedBy: 'FO3 Juan Dela Cruz',
    date: 'Sept. 9, 2026',
    status: 'Pending',
    description:
      'After-operation report submitted for administrative review.'
  },
  {
    id: 2,
    name: 'Monthly Compliance Summary',
    submittedBy: 'SFO1 Maria Santos',
    date: 'Sept. 8, 2026',
    status: 'Approved',
    description:
      'Monthly compliance summary approved by station administration.'
  },
  {
    id: 3,
    name: 'Barangay Fire Drill Summary',
    submittedBy: 'FO2 R. Reyes',
    date: 'Sept. 7, 2026',
    status: 'Reviewed',
    description:
      'Summary report of the completed barangay fire drill.'
  }
])

const alerts = ref([
  {
    id: 1,
    title: 'Unresolved Fire Investigation',
    details: 'Case #FI-2048 • Barangay San Roque',
    priority: 'High',
    description:
      'Fire investigation remains unresolved and requires administrative attention.'
  },
  {
    id: 2,
    title: 'Equipment Calibration Due',
    details: 'Portable pump unit • due tomorrow',
    priority: 'Medium',
    description:
      'Portable pump unit requires calibration before the next scheduled inspection.'
  },
  {
    id: 3,
    title: 'Training Attendance Update',
    details: '2 personnel still pending attendance',
    priority: 'Info',
    description:
      'Two assigned personnel have not yet completed their attendance confirmation.'
  }
])

const systemActivities = ref([
  {
    action: 'Report Submitted',
    subject: 'FO3 Juan Dela Cruz',
    time: '10 minutes ago',
    icon: '✓'
  },
  {
    action: 'Activity Completed',
    subject: 'Station Equipment Check',
    time: '25 minutes ago',
    icon: '✓'
  },
  {
    action: 'Deadline Reminder',
    subject: 'Weekly Report',
    time: '40 minutes ago',
    icon: '!'
  },
  {
    action: 'New Activity',
    subject: 'Community Fire Drill',
    time: '1 hour ago',
    icon: '+'
  }
])

/* =========================================================
   SEARCH
========================================================= */

const searchQuery = ref('')

const filteredActivities = computed(() => {
  const query = searchQuery.value.toLowerCase().trim()

  if (!query) return activities.value

  return activities.value.filter(activity =>
    [
      activity.title,
      activity.assignedTo,
      activity.location,
      activity.status
    ]
      .join(' ')
      .toLowerCase()
      .includes(query)
  )
})

/* =========================================================
   DASHBOARD STATS
========================================================= */

const activePersonnel = ref(48)
const pendingReports = computed(
  () => reports.value.filter(report => report.status === 'Pending').length + 11
)

const overdueDeadlines = computed(
  () => deadlines.value.filter(deadline => deadline.status === 'Overdue').length
)

const complianceScore = ref(94.5)

const completedActivities = computed(
  () => activities.value.filter(activity => activity.status === 'Completed').length
)

const ongoingActivities = computed(
  () => activities.value.filter(activity => activity.status === 'Ongoing').length
)

const scheduledActivities = computed(
  () => activities.value.filter(activity => activity.status === 'Scheduled').length
)

/* =========================================================
   MODALS
========================================================= */

const selectedActivity = ref(null)
const selectedReport = ref(null)
const selectedDeadline = ref(null)
const selectedAlert = ref(null)

const showActivityModal = ref(false)
const showReportModal = ref(false)
const showDeadlineModal = ref(false)
const showAlertModal = ref(false)

const toastMessage = ref('')

const showToast = message => {
  toastMessage.value = message

  setTimeout(() => {
    toastMessage.value = ''
  }, 2500)
}

const viewActivity = activity => {
  selectedActivity.value = activity
  showActivityModal.value = true
}

const viewReport = report => {
  selectedReport.value = report
  showReportModal.value = true
}

const viewDeadline = deadline => {
  selectedDeadline.value = deadline
  showDeadlineModal.value = true
}

const viewAlert = alert => {
  selectedAlert.value = alert
  showAlertModal.value = true
}

/* =========================================================
   STATUS STYLING
========================================================= */

const getStatusClass = status => {
  const classes = {
    Ongoing: 'bg-blue-50 text-blue-700 border-blue-100',
    Scheduled: 'bg-yellow-50 text-yellow-700 border-yellow-100',
    Completed: 'bg-green-50 text-green-700 border-green-100',
    Pending: 'bg-yellow-50 text-yellow-700 border-yellow-100',
    Approved: 'bg-green-50 text-green-700 border-green-100',
    Reviewed: 'bg-blue-50 text-blue-700 border-blue-100',
    Overdue: 'bg-red-50 text-[#8B1E23] border-red-100',
    Upcoming: 'bg-blue-50 text-blue-700 border-blue-100'
  }

  return classes[status] || 'bg-slate-50 text-slate-600 border-slate-100'
}

const getPriorityClass = priority => {
  const classes = {
    High: 'bg-red-100 text-[#8B1E23]',
    Medium: 'bg-yellow-100 text-yellow-700',
    Info: 'bg-blue-100 text-blue-700'
  }

  return classes[priority] || 'bg-slate-100 text-slate-600'
}
</script>

<template>
  <div class="space-y-7">

    <!-- =====================================================
         WELCOME HEADER
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-7"
    >
      <div
        class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5"
      >
        <div>
          <p
            class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]"
          >
            Administrator Dashboard
          </p>

          <h2 class="text-3xl font-bold text-slate-900 mt-2">
            Good day, {{ currentUser?.name || 'Administrator' }}!
          </h2>

          <p class="text-base text-slate-500 mt-2 max-w-3xl">
            Monitor personnel, activities, reports, deadlines, and station
            compliance from one place.
          </p>
        </div>

        <div
          class="px-5 py-4 rounded-xl bg-[#8B1E23] text-white min-w-[190px]"
        >
          <p class="text-xs uppercase tracking-wide text-red-100">
            Station
          </p>

          <p class="font-bold text-lg mt-1">
            BFP Balingasag
          </p>

          <p class="text-xs text-red-100 mt-1">
            Operations Management
          </p>
        </div>
      </div>
    </section>

    <!-- =====================================================
         STATISTICS
    ====================================================== -->

    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">

      <!-- Active Personnel -->
      <div
        class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm"
      >
        <div class="flex items-center justify-between">
          <div
            class="h-12 w-12 rounded-xl bg-green-50 flex items-center justify-center"
          >
            <svg
              class="w-6 h-6 fill-current text-green-600"
              viewBox="0 0 24 24"
            >
              <path
                d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5s-3 1.34-3 3 1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5C15 14.17 10.33 13 8 13zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"
              />
            </svg>
          </div>

          <span
            class="px-3 py-1 rounded-full bg-green-50 text-green-700 text-xs font-bold"
          >
            ACTIVE
          </span>
        </div>

        <p class="mt-5 text-4xl font-bold text-slate-900">
          {{ activePersonnel }}
        </p>

        <p class="mt-1 text-base text-slate-500">
          Active Personnel
        </p>

        <p class="mt-3 text-sm font-semibold text-green-600">
          All shifts covered
        </p>
      </div>

      <!-- Reports -->
      <div
        class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm"
      >
        <div class="flex items-center justify-between">
          <div
            class="h-12 w-12 rounded-xl bg-yellow-50 flex items-center justify-center"
          >
            <svg
              class="w-6 h-6 fill-current text-yellow-600"
              viewBox="0 0 24 24"
            >
              <path
                d="M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1 1.9 2 2 2h12c1.1 0 2-.9 2-2V8l-6-6zM15 9V3.5L18.5 9H15zM8 13h8v2H8v-2zm0 4h8v2H8v-2z"
              />
            </svg>
          </div>

          <span
            class="px-3 py-1 rounded-full bg-yellow-50 text-yellow-700 text-xs font-bold"
          >
            REVIEW
          </span>
        </div>

        <p class="mt-5 text-4xl font-bold text-slate-900">
          {{ pendingReports }}
        </p>

        <p class="mt-1 text-base text-slate-500">
          Pending Reports
        </p>

        <p class="mt-3 text-sm font-semibold text-yellow-700">
          Requires review
        </p>
      </div>

      <!-- Deadlines -->
      <div
        class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm"
      >
        <div class="flex items-center justify-between">
          <div
            class="h-12 w-12 rounded-xl bg-red-50 flex items-center justify-center"
          >
            <svg
              class="w-6 h-6 fill-current text-[#8B1E23]"
              viewBox="0 0 24 24"
            >
              <path
                d="M1 21h22L12 2 1 21zm12-3h-2v2h2v-2zm0-2h-2v-4h2v4z"
              />
            </svg>
          </div>

          <span
            class="px-3 py-1 rounded-full bg-red-50 text-[#8B1E23] text-xs font-bold"
          >
            ALERT
          </span>
        </div>

        <p class="mt-5 text-4xl font-bold text-[#8B1E23]">
          {{ overdueDeadlines.toString().padStart(2, '0') }}
        </p>

        <p class="mt-1 text-base text-slate-500">
          Overdue Deadlines
        </p>

        <p class="mt-3 text-sm font-semibold text-[#8B1E23]">
          Immediate attention
        </p>
      </div>

      <!-- Compliance -->
      <div
        class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm"
      >
        <div class="flex items-center justify-between">
          <div
            class="h-12 w-12 rounded-xl bg-blue-50 flex items-center justify-center"
          >
            <svg
              class="w-6 h-6 fill-current text-blue-600"
              viewBox="0 0 24 24"
            >
              <path
                d="M12 2L4 5v6c0 5.55 3.84 10.74 8 12 4.16-1.26 8-6.45 8-12V5l-8-3zm-1.5 15l-3.5-3.5 1.41-1.41 2.09 2.08 5.59-5.59 1.41 1.41-7 7z"
              />
            </svg>
          </div>

          <span
            class="px-3 py-1 rounded-full bg-blue-50 text-blue-700 text-xs font-bold"
          >
            MONTHLY
          </span>
        </div>

        <p class="mt-5 text-4xl font-bold text-slate-900">
          {{ complianceScore }}%
        </p>

        <p class="mt-1 text-base text-slate-500">
          Compliance Score
        </p>

        <div class="mt-3">
          <div class="h-2 rounded-full bg-slate-100 overflow-hidden">
            <div
              class="h-full bg-blue-600 rounded-full transition-all"
              :style="{ width: `${complianceScore}%` }"
            ></div>
          </div>

          <p class="text-xs text-blue-600 font-semibold mt-2">
            Station performance
          </p>
        </div>
      </div>

    </section>

    <!-- =====================================================
         QUICK OPERATION SUMMARY
    ====================================================== -->

    <section class="grid grid-cols-1 md:grid-cols-3 gap-5">

      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-sm text-slate-500">
          Scheduled Activities
        </p>

        <p class="text-3xl font-bold text-slate-900 mt-2">
          {{ scheduledActivities }}
        </p>

        <p class="text-xs text-slate-400 mt-1">
          Currently scheduled
        </p>
      </div>

      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-sm text-slate-500">
          Ongoing Activities
        </p>

        <p class="text-3xl font-bold text-blue-600 mt-2">
          {{ ongoingActivities }}
        </p>

        <p class="text-xs text-slate-400 mt-1">
          Personnel currently working
        </p>
      </div>

      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >
        <p class="text-sm text-slate-500">
          Completed Activities
        </p>

        <p class="text-3xl font-bold text-green-600 mt-2">
          {{ completedActivities }}
        </p>

        <p class="text-xs text-slate-400 mt-1">
          Successfully completed
        </p>
      </div>

    </section>

    <!-- =====================================================
         ACTIVITIES + DEADLINES
    ====================================================== -->

    <section class="grid grid-cols-1 xl:grid-cols-3 gap-6">

      <!-- Activities -->
      <div
        class="xl:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
      >
        <div
          class="flex flex-col md:flex-row md:items-center md:justify-between gap-4 border-b border-slate-200 pb-5"
        >
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Recent Operational Activities
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              Latest activities assigned to station personnel
            </p>
          </div>

          <button
            @click="showToast('Activities module selected')"
            class="text-sm font-bold text-[#8B1E23] hover:underline"
          >
            View Activities →
          </button>
        </div>

        <!-- Search -->
        <div class="mt-5">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search activities, personnel, location..."
            class="w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 focus:outline-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
          />
        </div>

        <div class="mt-5 space-y-3">

          <div
            v-for="activity in filteredActivities"
            :key="activity.id"
            @click="viewActivity(activity)"
            class="p-4 rounded-xl border border-slate-200 hover:bg-slate-50 hover:border-[#8B1E23]/30 cursor-pointer transition"
          >
            <div
              class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4"
            >
              <div>
                <p class="font-bold text-slate-900">
                  {{ activity.title }}
                </p>

                <p class="text-sm text-slate-500 mt-1">
                  Assigned to {{ activity.assignedTo }}
                </p>

                <p class="text-sm text-slate-400 mt-1">
                  {{ activity.date }} • {{ activity.time }}
                </p>

                <p class="text-xs text-slate-400 mt-1">
                  {{ activity.location }}
                </p>
              </div>

              <span
                class="px-3 py-1.5 rounded-full border text-xs font-bold whitespace-nowrap"
                :class="getStatusClass(activity.status)"
              >
                {{ activity.status.toUpperCase() }}
              </span>
            </div>
          </div>

          <div
            v-if="filteredActivities.length === 0"
            class="py-10 text-center text-slate-400"
          >
            No activities found.
          </div>

        </div>
      </div>

      <!-- Deadlines -->
      <div
        class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
      >
        <div
          class="flex items-center justify-between border-b border-slate-200 pb-5"
        >
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Upcoming Deadlines
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              Reports requiring attention
            </p>
          </div>

          <button
            @click="showToast('Deadline Monitor selected')"
            class="text-xs font-bold text-[#8B1E23] hover:underline"
          >
            View All
          </button>
        </div>

        <div class="mt-5 space-y-4">

          <div
            v-for="deadline in deadlines"
            :key="deadline.id"
            @click="viewDeadline(deadline)"
            class="p-4 rounded-xl border cursor-pointer hover:shadow-sm transition"
            :class="
              deadline.color === 'red'
                ? 'bg-red-50 border-red-200'
                : deadline.color === 'yellow'
                  ? 'bg-yellow-50 border-yellow-200'
                  : 'bg-blue-50 border-blue-200'
            "
          >
            <div class="flex items-start gap-3">

              <span class="text-xl">
                {{
                  deadline.status === 'Overdue'
                    ? '🚨'
                    : deadline.color === 'yellow'
                      ? '⚠️'
                      : '📋'
                }}
              </span>

              <div>
                <p class="text-sm font-bold text-slate-900">
                  {{ deadline.title }}
                </p>

                <p
                  class="text-xs mt-1"
                  :class="
                    deadline.status === 'Overdue'
                      ? 'text-[#8B1E23]'
                      : deadline.color === 'yellow'
                        ? 'text-yellow-700'
                        : 'text-blue-700'
                  "
                >
                  {{ deadline.due }}
                </p>

                <span
                  class="inline-block mt-2 px-2.5 py-1 rounded-full text-xs font-bold"
                  :class="getStatusClass(deadline.status)"
                >
                  {{ deadline.status.toUpperCase() }}
                </span>
              </div>

            </div>
          </div>

        </div>
      </div>

    </section>

    <!-- =====================================================
         SYSTEM ACTIVITY
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >
      <div class="border-b border-slate-200 pb-5">
        <h2 class="text-xl font-bold text-slate-900">
          Recent System Activity
        </h2>

        <p class="text-sm text-slate-500 mt-1">
          Latest actions performed in FireNotify
        </p>
      </div>

      <div class="mt-5 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">

        <div
          v-for="item in systemActivities"
          :key="item.action"
          class="p-4 rounded-xl bg-slate-50 border border-slate-200"
        >
          <div class="flex items-center gap-2">
            <span
              class="h-7 w-7 rounded-full bg-white border border-slate-200 flex items-center justify-center font-bold text-[#8B1E23]"
            >
              {{ item.icon }}
            </span>

            <p class="text-sm font-semibold text-slate-900">
              {{ item.action }}
            </p>
          </div>

          <p class="text-xs text-slate-500 mt-2">
            {{ item.subject }}
          </p>

          <p class="text-xs text-slate-400 mt-2">
            {{ item.time }}
          </p>
        </div>

      </div>
    </section>

    <!-- =====================================================
         MISSION READINESS + PRIORITY ALERTS
    ====================================================== -->

    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- Mission Readiness -->
      <div
        class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
      >
        <div
          class="flex items-center justify-between border-b border-slate-200 pb-5"
        >
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Mission Readiness
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              Station preparedness summary
            </p>
          </div>

          <span
            class="px-3 py-1.5 rounded-full bg-green-50 text-green-700 text-xs font-bold"
          >
            READY
          </span>
        </div>

        <div class="mt-5 space-y-5">

          <div>
            <div class="flex justify-between mb-2">
              <div>
                <p class="text-sm font-bold text-slate-900">
                  Engine Availability
                </p>

                <p class="text-xs text-slate-500">
                  4 of 5 engines operational
                </p>
              </div>

              <span class="text-sm font-bold text-green-600">
                80%
              </span>
            </div>

            <div class="h-2 bg-slate-100 rounded-full overflow-hidden">
              <div
                class="h-full bg-green-500 rounded-full"
                style="width: 80%"
              ></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between mb-2">
              <div>
                <p class="text-sm font-bold text-slate-900">
                  Communication Systems
                </p>

                <p class="text-xs text-slate-500">
                  Radios and dispatch links stable
                </p>
              </div>

              <span class="text-sm font-bold text-blue-600">
                Stable
              </span>
            </div>

            <div class="h-2 bg-slate-100 rounded-full overflow-hidden">
              <div
                class="h-full bg-blue-500 rounded-full"
                style="width: 95%"
              ></div>
            </div>
          </div>

          <div>
            <div class="flex justify-between mb-2">
              <div>
                <p class="text-sm font-bold text-slate-900">
                  Medical Kits
                </p>

                <p class="text-xs text-slate-500">
                  Fully stocked across all units
                </p>
              </div>

              <span class="text-sm font-bold text-emerald-600">
                100%
              </span>
            </div>

            <div class="h-2 bg-slate-100 rounded-full overflow-hidden">
              <div
                class="h-full bg-emerald-500 rounded-full"
                style="width: 100%"
              ></div>
            </div>
          </div>

        </div>
      </div>

      <!-- Priority Alerts -->
      <div
        class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
      >
        <div
          class="flex items-center justify-between border-b border-slate-200 pb-5"
        >
          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Priority Alerts
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              Items requiring immediate attention
            </p>
          </div>

          <button
            @click="showToast('Priority alerts opened')"
            class="text-sm font-bold text-[#8B1E23] hover:underline"
          >
            View All
          </button>
        </div>

        <div class="mt-5 space-y-4">

          <div
            v-for="alert in alerts"
            :key="alert.id"
            @click="viewAlert(alert)"
            class="p-4 rounded-xl border cursor-pointer hover:shadow-sm transition"
            :class="
              alert.priority === 'High'
                ? 'bg-red-50 border-red-200'
                : alert.priority === 'Medium'
                  ? 'bg-yellow-50 border-yellow-200'
                  : 'bg-blue-50 border-blue-200'
            "
          >
            <div class="flex justify-between items-start gap-3">

              <div>
                <p class="text-sm font-bold text-slate-900">
                  {{ alert.title }}
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  {{ alert.details }}
                </p>
              </div>

              <span
                class="px-2.5 py-1 rounded-full text-xs font-bold"
                :class="getPriorityClass(alert.priority)"
              >
                {{ alert.priority }}
              </span>

            </div>
          </div>

        </div>
      </div>

    </section>

    <!-- =====================================================
         OPERATIONS TIMELINE
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >
      <div class="border-b border-slate-200 pb-5">
        <h2 class="text-xl font-bold text-slate-900">
          Operations Timeline
        </h2>

        <p class="text-sm text-slate-500 mt-1">
          Key events and updates from today
        </p>
      </div>

      <div class="mt-5 space-y-4">

        <div class="flex gap-4 p-4 rounded-xl border border-slate-200">
          <div class="flex flex-col items-center">
            <span class="h-3 w-3 rounded-full bg-[#8B1E23]"></span>
            <span class="w-px h-full bg-slate-200 mt-2"></span>
          </div>

          <div>
            <p class="text-sm font-bold text-slate-900">
              08:00 AM • Morning Briefing
            </p>

            <p class="text-sm text-slate-500 mt-1">
              All station personnel attended the daily operations briefing
              and reviewed updated response protocols.
            </p>
          </div>
        </div>

        <div class="flex gap-4 p-4 rounded-xl border border-slate-200">
          <div class="flex flex-col items-center">
            <span class="h-3 w-3 rounded-full bg-blue-500"></span>
            <span class="w-px h-full bg-slate-200 mt-2"></span>
          </div>

          <div>
            <p class="text-sm font-bold text-slate-900">
              10:30 AM • Fire Safety Inspection
            </p>

            <p class="text-sm text-slate-500 mt-1">
              Inspection status reported for three commercial establishments
              in the central district.
            </p>
          </div>
        </div>

        <div class="flex gap-4 p-4 rounded-xl border border-slate-200">
          <div>
            <span class="h-3 w-3 rounded-full bg-green-500 block"></span>
          </div>

          <div>
            <p class="text-sm font-bold text-slate-900">
              01:00 PM • Community Drill
            </p>

            <p class="text-sm text-slate-500 mt-1">
              Final logistics approved for the barangay evacuation drill
              scheduled this afternoon.
            </p>
          </div>
        </div>

      </div>
    </section>

    <!-- =====================================================
         RECENT REPORTS
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >
      <div
        class="flex flex-col md:flex-row md:items-center md:justify-between gap-3 border-b border-slate-200 pb-5"
      >
        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Recent Reports
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Latest submissions and their current status
          </p>
        </div>

        <button
          @click="showToast('Report Management selected')"
          class="text-sm font-bold text-[#8B1E23] hover:underline"
        >
          Open Reports →
        </button>
      </div>

      <div class="mt-5 overflow-x-auto">

        <table class="w-full text-left min-w-[700px]">

          <thead>
            <tr
              class="border-b border-slate-200 text-xs font-bold uppercase tracking-wide text-slate-400"
            >
              <th class="pb-3 pr-4">Report</th>
              <th class="pb-3 pr-4">Submitted By</th>
              <th class="pb-3 pr-4">Date</th>
              <th class="pb-3 text-right">Status</th>
            </tr>
          </thead>

          <tbody class="divide-y divide-slate-100">

            <tr
              v-for="report in reports"
              :key="report.id"
              @click="viewReport(report)"
              class="hover:bg-slate-50 cursor-pointer transition"
            >
              <td class="py-4 pr-4 font-semibold text-slate-900">
                {{ report.name }}
              </td>

              <td class="py-4 pr-4 text-sm text-slate-600">
                {{ report.submittedBy }}
              </td>

              <td class="py-4 pr-4 text-sm text-slate-600">
                {{ report.date }}
              </td>

              <td class="py-4 text-right">
                <span
                  class="px-3 py-1.5 rounded-full border text-xs font-bold"
                  :class="getStatusClass(report.status)"
                >
                  {{ report.status }}
                </span>
              </td>
            </tr>

          </tbody>

        </table>

      </div>
    </section>

    <!-- =====================================================
         ACTIVITY MODAL
    ====================================================== -->

    <div
      v-if="showActivityModal"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
      @click.self="showActivityModal = false"
    >
      <div
        class="bg-white w-full max-w-lg rounded-2xl shadow-xl p-6"
      >
        <div class="flex items-center justify-between">
          <div>
            <p class="text-xs font-bold uppercase text-[#8B1E23]">
              Activity Details
            </p>

            <h3 class="text-xl font-bold text-slate-900 mt-1">
              {{ selectedActivity?.title }}
            </h3>
          </div>

          <button
            @click="showActivityModal = false"
            class="h-9 w-9 rounded-lg bg-slate-100 hover:bg-slate-200"
          >
            ✕
          </button>
        </div>

        <div class="mt-5 space-y-4">

          <div>
            <p class="text-xs text-slate-400 uppercase font-bold">
              Assigned Personnel
            </p>

            <p class="text-sm font-semibold text-slate-900 mt-1">
              {{ selectedActivity?.assignedTo }}
            </p>
          </div>

          <div>
            <p class="text-xs text-slate-400 uppercase font-bold">
              Schedule
            </p>

            <p class="text-sm text-slate-700 mt-1">
              {{ selectedActivity?.date }} •
              {{ selectedActivity?.time }}
            </p>
          </div>

          <div>
            <p class="text-xs text-slate-400 uppercase font-bold">
              Location
            </p>

            <p class="text-sm text-slate-700 mt-1">
              {{ selectedActivity?.location }}
            </p>
          </div>

          <div>
            <p class="text-xs text-slate-400 uppercase font-bold">
              Description
            </p>

            <p class="text-sm text-slate-600 mt-1">
              {{ selectedActivity?.description }}
            </p>
          </div>

          <span
            class="inline-block px-3 py-1.5 rounded-full border text-xs font-bold"
            :class="getStatusClass(selectedActivity?.status)"
          >
            {{ selectedActivity?.status }}
          </span>

        </div>
      </div>
    </div>

    <!-- =====================================================
         REPORT MODAL
    ====================================================== -->

    <div
      v-if="showReportModal"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
      @click.self="showReportModal = false"
    >
      <div
        class="bg-white w-full max-w-lg rounded-2xl shadow-xl p-6"
      >
        <div class="flex justify-between items-start">
          <div>
            <p class="text-xs font-bold uppercase text-[#8B1E23]">
              Report Details
            </p>

            <h3 class="text-xl font-bold text-slate-900 mt-1">
              {{ selectedReport?.name }}
            </h3>
          </div>

          <button
            @click="showReportModal = false"
            class="h-9 w-9 rounded-lg bg-slate-100"
          >
            ✕
          </button>
        </div>

        <div class="mt-5 space-y-4">

          <div>
            <p class="text-xs text-slate-400 uppercase font-bold">
              Submitted By
            </p>

            <p class="text-sm text-slate-700 mt-1">
              {{ selectedReport?.submittedBy }}
            </p>
          </div>

          <div>
            <p class="text-xs text-slate-400 uppercase font-bold">
              Submission Date
            </p>

            <p class="text-sm text-slate-700 mt-1">
              {{ selectedReport?.date }}
            </p>
          </div>

          <div>
            <p class="text-xs text-slate-400 uppercase font-bold">
              Description
            </p>

            <p class="text-sm text-slate-600 mt-1">
              {{ selectedReport?.description }}
            </p>
          </div>

          <span
            class="inline-block px-3 py-1.5 rounded-full border text-xs font-bold"
            :class="getStatusClass(selectedReport?.status)"
          >
            {{ selectedReport?.status }}
          </span>

        </div>
      </div>
    </div>

    <!-- =====================================================
         DEADLINE MODAL
    ====================================================== -->

    <div
      v-if="showDeadlineModal"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
      @click.self="showDeadlineModal = false"
    >
      <div
        class="bg-white w-full max-w-lg rounded-2xl shadow-xl p-6"
      >
        <div class="flex justify-between items-start">
          <div>
            <p class="text-xs font-bold uppercase text-[#8B1E23]">
              Deadline Details
            </p>

            <h3 class="text-xl font-bold text-slate-900 mt-1">
              {{ selectedDeadline?.title }}
            </h3>
          </div>

          <button
            @click="showDeadlineModal = false"
            class="h-9 w-9 rounded-lg bg-slate-100"
          >
            ✕
          </button>
        </div>

        <div class="mt-5">

          <p class="text-sm text-slate-600">
            {{ selectedDeadline?.description }}
          </p>

          <p class="text-sm font-semibold text-slate-900 mt-4">
            {{ selectedDeadline?.due }}
          </p>

          <span
            class="inline-block mt-4 px-3 py-1.5 rounded-full border text-xs font-bold"
            :class="getStatusClass(selectedDeadline?.status)"
          >
            {{ selectedDeadline?.status }}
          </span>

        </div>
      </div>
    </div>

    <!-- =====================================================
         ALERT MODAL
    ====================================================== -->

    <div
      v-if="showAlertModal"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
      @click.self="showAlertModal = false"
    >
      <div
        class="bg-white w-full max-w-lg rounded-2xl shadow-xl p-6"
      >
        <div class="flex justify-between items-start">
          <div>
            <p class="text-xs font-bold uppercase text-[#8B1E23]">
              Priority Alert
            </p>

            <h3 class="text-xl font-bold text-slate-900 mt-1">
              {{ selectedAlert?.title }}
            </h3>
          </div>

          <button
            @click="showAlertModal = false"
            class="h-9 w-9 rounded-lg bg-slate-100"
          >
            ✕
          </button>
        </div>

        <div class="mt-5">

          <span
            class="px-3 py-1.5 rounded-full text-xs font-bold"
            :class="getPriorityClass(selectedAlert?.priority)"
          >
            {{ selectedAlert?.priority }} Priority
          </span>

          <p class="text-sm font-semibold text-slate-800 mt-4">
            {{ selectedAlert?.details }}
          </p>

          <p class="text-sm text-slate-600 mt-2">
            {{ selectedAlert?.description }}
          </p>

        </div>
      </div>
    </div>

    <!-- =====================================================
         TOAST
    ====================================================== -->

    <transition name="fade">
      <div
        v-if="toastMessage"
        class="fixed bottom-6 right-6 z-[60] bg-slate-900 text-white px-5 py-3 rounded-xl shadow-lg text-sm font-semibold"
      >
        {{ toastMessage }}
      </div>
    </transition>

  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>