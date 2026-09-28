<script setup>
import {
  computed,
  onBeforeUnmount,
  onMounted,
  ref
} from 'vue'

import { resolvePersonnelName } from '../../utils/personnelName.js'

const props = defineProps({
  currentUser: {
    type: Object,
    default: null
  },

  registeredUsers: {
    type: Array,
    default: () => []
  }
})

/* =========================================================
   FIRENOTIFY FRONTEND-ONLY LIVE DATA
   ========================================================= */

const KEYS = {
  users: 'fireNotifyRegisteredUsers',
  activities: 'fireNotifyActivities',
  tasks: 'firenotify_tasks',
  reports: 'firenotify_reports'
}

const UPDATE_EVENTS = [
  'fireNotifyUsersUpdated',
  'fireNotifyRegisteredUsersUpdated',
  'fireNotifyActivitiesUpdated',
  'fireNotifyTasksUpdated',
  'fireNotifyReportsUpdated',
  'fireNotifyNotificationsUpdated'
]

const users = ref([])
const activities = ref([])
const tasks = ref([])
const reports = ref([])
const notifications = ref([])

const selected = ref(null)
const selectedType = ref('')

let refreshTimer = null


/* =========================================================
   SAFE LOCAL STORAGE
   ========================================================= */

const readArray = key => {
  try {
    const value = JSON.parse(
      localStorage.getItem(key) || '[]'
    )

    return Array.isArray(value)
      ? value
      : []

  } catch (error) {

    console.warn(
      `FireNotify: unable to read ${key}`,
      error
    )

    return []
  }
}


/* =========================================================
   NOTIFICATIONS
   ========================================================= */

const readNotifications = () => {

  const possibleKeys = [
    'firenotify_notifications',
    'fireNotifyNotifications',
    'fireNotifyNotificationsData',
    'notifications'
  ]

  for (const key of possibleKeys) {

    const value = readArray(key)

    if (value.length) {
      return value
    }
  }


  /*
   * Fallback:
   * Find any localStorage key containing
   * "notification".
   */

  for (
    let index = 0;
    index < localStorage.length;
    index++
  ) {

    const key =
      localStorage.key(index) || ''

    if (
      !key
        .toLowerCase()
        .includes('notification')
    ) {
      continue
    }

    const value =
      readArray(key)

    if (value.length) {
      return value
    }
  }

  return []
}


/* =========================================================
   LOAD ALL LIVE DATA
   ========================================================= */

   const loadUsersFromBackend = async () => {
  try {
    const response = await fetch(
      'http://127.0.0.1:8000/api/users/'
    )

    if (!response.ok) {
      throw new Error(
        `HTTP ${response.status}`
      )
    }

    const data =
      await response.json()

    if (!Array.isArray(data)) {
      throw new Error(
        'Invalid users response'
      )
    }

    users.value = data.map(user => ({
      ...user,

      firstName:
        user.firstName ||
        user.first_name ||
        '',

      lastName:
        user.lastName ||
        user.last_name ||
        '',

      name:
        user.name ||
        `${user.first_name || ''} ${user.last_name || ''}`.trim(),

      role:
        String(
          user.role || 'PERSONNEL'
        ).toLowerCase(),

      status:
        user.status ||
        (user.is_active
          ? 'Active'
          : 'Inactive')
    }))

  } catch (error) {

    console.error(
      'Failed to load personnel from Django:',
      error
    )

    /*
     * Fallback to existing localStorage
     * if Django is temporarily unavailable.
     */

    const storedUsers =
      readArray(KEYS.users)

    users.value =
      storedUsers.length
        ? storedUsers
        : (
            Array.isArray(
              props.registeredUsers
            )
              ? [...props.registeredUsers]
              : []
          )
  }
}

const refresh = async () => {

  await loadUsersFromBackend()

  activities.value =
    readArray(
      KEYS.activities
    )

  tasks.value =
    readArray(
      KEYS.tasks
    )

  reports.value =
    readArray(
      KEYS.reports
    )

  notifications.value =
    readNotifications()
}


/* =========================================================
   GENERAL HELPERS
   ========================================================= */

const normalize = value => {

  return String(
    value || ''
  )
    .trim()
    .toLowerCase()
}


const nameOf = person => {

  if (!person) {
    return 'Unnamed Personnel'
  }

  return (
    person.name ||
    `${person.firstName || ''} ${person.lastName || ''}`.trim() ||
    person.username ||
    person.identifier ||
    'Unnamed Personnel'
  )
}


const parseDate = value => {

  if (!value) {
    return null
  }


  if (value instanceof Date) {

    return Number.isNaN(
      value.getTime()
    )
      ? null
      : value
  }


  const raw =
    String(value)
      .replace(/•/g, ' ')
      .trim()


  const date =
    new Date(raw)


  return Number.isNaN(
    date.getTime()
  )
    ? null
    : date
}


const statusOf = item => {

  return normalize(
    item?.status ||
    item?.state
  )
}


const completed = status => {

  return [
    'completed',
    'complete',
    'done',
    'finished',
    'closed',
    'approved',
    'reviewed',
    'resolved'
  ].includes(
    normalize(status)
  )
}


/* =========================================================
   PERSONNEL
   ========================================================= */

const personnel = computed(() => {

  return users.value.filter(
    user => {

      const role =
        normalize(
          user?.role ||
          'personnel'
        )

      return role !== 'admin'
    }
  )
})


const activePersonnel = computed(() => {

  return personnel.value.filter(
    user => {

      const status =
        normalize(
          user?.status ||
          'Active'
        )


      return ![
        'inactive',
        'deleted',
        'disabled',
        'deactivated'
      ].includes(status)

    }
  ).length
})


const totalPersonnel =
  computed(
    () =>
      personnel.value.length
  )


/* =========================================================
   ACTIVITIES
   ========================================================= */

const activityTitle = item => {

  return (
    item?.title ||
    item?.name ||
    item?.activityName ||
    item?.type ||
    'Station Activity'
  )
}


const activityDate = item => {

  return (
    item?.date ||
    item?.startDate ||
    item?.activityDate ||
    item?.scheduleDate ||
    item?.scheduledDate ||
    ''
  )
}


const activityPerson = item => {
  return resolvePersonnelName(
    item?.assignedPersonnel ||
      item?.assignedToId ||
      item?.assignedToName ||
      item?.assignedTo ||
      item?.personnelName,
    users.value,
    'Unassigned'
  )
}


const completedActivities =
  computed(() => {

    return activities.value.filter(
      item =>
        completed(
          statusOf(item)
        )
    ).length
  })


const activityCompliance =
  computed(() => {

    if (
      !activities.value.length
    ) {
      return 0
    }

    return Math.round(
      (
        completedActivities.value /
        activities.value.length
      ) * 100
    )
  })


const recentActivities =
  computed(() => {

    return [
      ...activities.value
    ]
      .sort(
        (a, b) => {

          const aDate =
            parseDate(
              a?.updatedAt ||
              a?.createdAt ||
              activityDate(a)
            )?.getTime() || 0


          const bDate =
            parseDate(
              b?.updatedAt ||
              b?.createdAt ||
              activityDate(b)
            )?.getTime() || 0


          return bDate - aDate
        }
      )
      .slice(0, 5)
  })


/* =========================================================
   REPORTS
   ========================================================= */

const reportTitle = item => {

  return (
    item?.title ||
    item?.name ||
    'Report'
  )
}


const reportPerson = item => {
  return resolvePersonnelName(
    item?.assignedPersonnel ||
      item?.assignedToId ||
      item?.assignedToName ||
      item?.submittedBy,
    users.value,
    'Unassigned'
  )
}


const pendingReports =
  computed(() => {

    return reports.value.filter(
      item => [

        'pending',
        'submitted',
        'for review',
        'in progress'

      ].includes(
        statusOf(item)
      )
    ).length
  })


const reviewedReports =
  computed(() => {

    return reports.value.filter(
      item => [

        'approved',
        'reviewed'

      ].includes(
        statusOf(item)
      )
    ).length
  })


const reportCompliance =
  computed(() => {

    if (!reports.value.length) {
      return 0
    }

    return Math.round(
      (
        reviewedReports.value /
        reports.value.length
      ) * 100
    )
  })


const recentReports =
  computed(() => {

    return [
      ...reports.value
    ]
      .sort(
        (a, b) => {

          const aDate =
            parseDate(
              a?.updatedAt ||
              a?.createdAt ||
              a?.submittedDate
            )?.getTime() || 0


          const bDate =
            parseDate(
              b?.updatedAt ||
              b?.createdAt ||
              b?.submittedDate
            )?.getTime() || 0


          return bDate - aDate
        }
      )
      .slice(0, 5)
  })


/* =========================================================
   TASKS / DEADLINES
   ========================================================= */

const taskTitle = item => {

  return (
    item?.title ||
    item?.name ||
    item?.taskName ||
    item?.type ||
    'Assigned Task'
  )
}


const taskDate = item => {

  return (
    item?.deadline ||
    item?.dueDate ||
    item?.deadlineDate ||
    item?.due ||
    item?.date ||
    item?.scheduleDate ||
    item?.scheduledDate ||
    ''
  )
}


const isOverdue = item => {

  if (
    completed(
      item?.status
    )
  ) {
    return false
  }


  if (
    statusOf(item) ===
    'overdue'
  ) {
    return true
  }


  const date =
    parseDate(
      taskDate(item)
    )


  if (!date) {
    return false
  }


  return (
    date.getTime() <
    Date.now()
  )
}


const taskDeadlines =
  computed(() => {

    return tasks.value.filter(
      item => {

        return (
          taskDate(item) ||
          statusOf(item) ===
            'overdue'
        )
      }
    )
  })


const overdueTasks =
  computed(() => {

    return taskDeadlines.value.filter(
      isOverdue
    )
  })


/* =========================================================
   REPORT DEADLINES
   ========================================================= */

const reportDeadlines =
  computed(() => {

    return reports.value.filter(
      item => {

        return (
          item?.deadline ||
          item?.dueDate ||
          item?.deadlineDate ||
          statusOf(item) ===
            'overdue'
        )
      }
    )
  })


const overdueReports =
  computed(() => {

    return reportDeadlines.value.filter(
      item => {

        if (
          completed(
            item?.status
          )
        ) {
          return false
        }


        if (
          statusOf(item) ===
          'overdue'
        ) {
          return true
        }


        const date =
          parseDate(
            item?.deadline ||
            item?.dueDate ||
            item?.deadlineDate
          )


        return (
          !!date &&
          date.getTime() <
            Date.now()
        )
      }
    )
  })


const totalDeadlines =
  computed(() => {

    return (
      taskDeadlines.value.length +
      reportDeadlines.value.length
    )
  })


const overdueDeadlines =
  computed(() => {

    return (
      overdueTasks.value.length +
      overdueReports.value.length
    )
  })


const deadlineCompliance =
  computed(() => {

    if (
      !totalDeadlines.value
    ) {
      return 0
    }


    const completedDeadlineCount =
      Math.max(
        totalDeadlines.value -
        overdueDeadlines.value,
        0
      )


    return Math.round(
      (
        completedDeadlineCount /
        totalDeadlines.value
      ) * 100
    )
  })


/* =========================================================
   NOTIFICATIONS
   ========================================================= */

const unreadNotifications =
  computed(() => {

    return notifications.value.filter(
      item =>
        !item?.read &&
        !item?.isRead
    ).length
  })


/* =========================================================
   OVERALL COMPLIANCE
   ========================================================= */

const overallCompliance =
  computed(() => {

    const values = []


    if (
      activities.value.length
    ) {
      values.push(
        activityCompliance.value
      )
    }


    if (
      reports.value.length
    ) {
      values.push(
        reportCompliance.value
      )
    }


    if (
      totalDeadlines.value
    ) {
      values.push(
        deadlineCompliance.value
      )
    }


    if (!values.length) {
      return 0
    }


    return Math.round(
      values.reduce(
        (total, value) =>
          total + value,
        0
      ) / values.length
    )
  })


const overallLabel =
  computed(() => {

    if (
      overallCompliance.value >=
      80
    ) {
      return 'Good Standing'
    }


    if (
      overallCompliance.value >=
      60
    ) {
      return 'Monitor'
    }


    return 'Requires Attention'
  })


/* =========================================================
   STATUS STYLE
   ========================================================= */

const statusClass = status => {

  const value =
    normalize(status)


  if (
    value.includes(
      'complete'
    ) ||
    [
      'approved',
      'reviewed',
      'done',
      'resolved'
    ].includes(value)
  ) {

    return `
      bg-green-50
      text-green-700
      border-green-200
    `
  }


  if (
    value.includes(
      'overdue'
    ) ||
    [
      'rejected',
      'cancelled',
      'canceled'
    ].includes(value)
  ) {

    return `
      bg-red-50
      text-[#8B1E23]
      border-red-200
    `
  }


  if (
    value.includes(
      'progress'
    ) ||
    value ===
      'ongoing'
  ) {

    return `
      bg-blue-50
      text-blue-700
      border-blue-200
    `
  }


  return `
    bg-yellow-50
    text-yellow-700
    border-yellow-200
  `
}


/* =========================================================
   DATE FORMAT
   ========================================================= */

const formatDate = value => {

  if (!value) {
    return 'No date'
  }


  const date =
    parseDate(value)


  if (!date) {
    return String(value)
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
   DETAILS MODAL
   ========================================================= */

const openDetails = (
  item,
  type
) => {

  selected.value =
    item

  selectedType.value =
    type
}


const closeDetails = () => {

  selected.value =
    null

  selectedType.value =
    ''
}


/* =========================================================
   REALTIME SYNC
   ========================================================= */

const handleStorage = event => {

  if (
    !event.key ||
    Object.values(KEYS)
      .includes(event.key) ||
    event.key
      .toLowerCase()
      .includes(
        'notification'
      )
  ) {

    refresh()
  }
}


const handleUpdate = () => {

  refresh()
}


/* =========================================================
   MOUNT
   ========================================================= */

onMounted(() => {

  refresh()


  window.addEventListener(
    'storage',
    handleStorage
  )


  UPDATE_EVENTS.forEach(
    eventName => {

      window.addEventListener(
        eventName,
        handleUpdate
      )
    }
  )


  /*
   * localStorage does not fire
   * a storage event in the same tab.
   *
   * This makes the dashboard
   * update even when the other
   * Vue component saves data
   * in the same browser tab.
   */

  refreshTimer =
    window.setInterval(
      refresh,
      1000
    )
})


/* =========================================================
   UNMOUNT
   ========================================================= */

onBeforeUnmount(() => {

  window.removeEventListener(
    'storage',
    handleStorage
  )


  UPDATE_EVENTS.forEach(
    eventName => {

      window.removeEventListener(
        eventName,
        handleUpdate
      )
    }
  )


  if (refreshTimer) {

    window.clearInterval(
      refreshTimer
    )

    refreshTimer =
      null
  }
})
</script>


<template>

  <div class="space-y-6">

    <!-- =====================================================
         HEADER
    ====================================================== -->

    <section
      class="bg-white border border-slate-200
             rounded-2xl shadow-sm p-6"
    >

      <div
        class="flex flex-col lg:flex-row
               lg:items-center lg:justify-between
               gap-5"
      >

        <div>

          <p
            class="text-sm font-bold uppercase
                   tracking-wide text-[#8B1E23]"
          >
            Administrator Dashboard
          </p>

          <h1
            class="text-3xl font-bold
                   text-slate-900 mt-1"
          >
            Good day,
            {{ currentUser?.name || 'Master Admin' }}!
          </h1>

          <p
            class="text-sm text-slate-500 mt-2"
          >
            Live monitoring of personnel,
            activities, reports, deadlines,
            and operational compliance.
          </p>

        </div>


        <div
          class="bg-[#8B1E23] text-white
                 rounded-xl px-5 py-4
                 min-w-[190px]"
        >

          <p
            class="text-[11px] uppercase
                   tracking-wide opacity-80"
          >
            Current Station
          </p>

          <p
            class="font-bold mt-1"
          >
            BFP Balingasag
          </p>

          <p
            class="text-xs opacity-80 mt-1"
          >
            Operations Management
          </p>

        </div>

      </div>

    </section>


    <!-- =====================================================
         LIVE SUMMARY CARDS
    ====================================================== -->

    <section
      class="grid grid-cols-1
             sm:grid-cols-2
             xl:grid-cols-4 gap-5"
    >

      <!-- PERSONNEL -->

      <div
        class="bg-white border border-slate-200
               rounded-2xl p-5 shadow-sm"
      >

        <div
          class="flex items-center
                 justify-between"
        >

          <div
            class="h-11 w-11 rounded-xl
                   bg-green-50 text-green-600
                   flex items-center
                   justify-center text-xl"
          >
            👥
          </div>

          <span
            class="px-2.5 py-1 rounded-full
                   bg-green-50 text-green-700
                   text-xs font-bold"
          >
            LIVE
          </span>

        </div>


        <p
          class="text-4xl font-bold
                 text-[#8B1E23] mt-5"
        >
          {{ activePersonnel }}
        </p>

        <p
          class="text-sm text-slate-500 mt-1"
        >
          Active Personnel
        </p>

        <p
          class="text-xs text-green-600
                 font-semibold mt-3"
        >
          {{ totalPersonnel }}
          registered personnel
        </p>

      </div>


      <!-- REPORTS -->

      <div
        class="bg-white border border-slate-200
               rounded-2xl p-5 shadow-sm"
      >

        <div
          class="flex items-center
                 justify-between"
        >

          <div
            class="h-11 w-11 rounded-xl
                   bg-yellow-50 text-yellow-600
                   flex items-center
                   justify-center text-xl"
          >
            📄
          </div>

          <span
            class="px-2.5 py-1 rounded-full
                   bg-yellow-50 text-yellow-700
                   text-xs font-bold"
          >
            REVIEW
          </span>

        </div>


        <p
          class="text-4xl font-bold
                 text-[#8B1E23] mt-5"
        >
          {{ pendingReports }}
        </p>

        <p
          class="text-sm text-slate-500 mt-1"
        >
          Pending Reports
        </p>

        <p
          class="text-xs text-yellow-600
                 font-semibold mt-3"
        >
          {{ reports.length }}
          total reports
        </p>

      </div>


      <!-- DEADLINES -->

      <div
        class="bg-white border border-slate-200
               rounded-2xl p-5 shadow-sm"
      >

        <div
          class="flex items-center
                 justify-between"
        >

          <div
            class="h-11 w-11 rounded-xl
                   bg-red-50 text-red-600
                   flex items-center
                   justify-center text-xl"
          >
            ⚠
          </div>

          <span
            class="px-2.5 py-1 rounded-full
                   bg-red-50 text-red-700
                   text-xs font-bold"
          >
            ALERT
          </span>

        </div>


        <p
          class="text-4xl font-bold
                 text-[#8B1E23] mt-5"
        >
          {{ overdueDeadlines }}
        </p>

        <p
          class="text-sm text-slate-500 mt-1"
        >
          Overdue Deadlines
        </p>

        <p
          class="text-xs text-red-600
                 font-semibold mt-3"
        >
          {{ totalDeadlines }}
          tracked deadlines
        </p>

      </div>


      <!-- COMPLIANCE -->

      <div
        class="bg-white border border-slate-200
               rounded-2xl p-5 shadow-sm"
      >

        <div
          class="flex items-center
                 justify-between"
        >

          <div
            class="h-11 w-11 rounded-xl
                   bg-blue-50 text-blue-600
                   flex items-center
                   justify-center text-xl"
          >
            ✓
          </div>

          <span
            class="px-2.5 py-1 rounded-full
                   bg-blue-50 text-blue-700
                   text-xs font-bold"
          >
            MONITOR
          </span>

        </div>


        <p
          class="text-4xl font-bold
                 text-[#8B1E23] mt-5"
        >
          {{ overallCompliance }}%
        </p>

        <p
          class="text-sm text-slate-500 mt-1"
        >
          Overall Compliance
        </p>

        <p
          class="text-xs text-[#8B1E23]
                 font-semibold mt-3"
        >
          {{ overallLabel }}
        </p>

      </div>

    </section>


    <!-- =====================================================
         COMPLIANCE MONITORING
    ====================================================== -->

    <section
      class="bg-white border border-slate-200
             rounded-2xl shadow-sm p-6"
    >

      <div
        class="flex flex-col lg:flex-row
               lg:items-center
               lg:justify-between gap-4
               border-b border-slate-200 pb-5"
      >

        <div>

          <p
            class="text-xs font-bold uppercase
                   tracking-wide text-[#8B1E23]"
          >
            Operations Compliance
          </p>

          <h2
            class="text-2xl font-bold
                   text-slate-900 mt-1"
          >
            Compliance Monitoring
          </h2>

          <p
            class="text-sm text-slate-500 mt-1"
          >
            Calculated from the live records
            in the FireNotify modules.
          </p>

        </div>


        <div
          class="px-4 py-3 rounded-xl
                 bg-slate-50 border
                 border-slate-200"
        >

          <p
            class="text-xs text-slate-400
                   uppercase font-bold"
          >
            Overall Status
          </p>

          <p
            class="font-bold
                   text-[#8B1E23] mt-1"
          >
            {{ overallLabel }}
          </p>

        </div>

      </div>


      <div
        class="grid grid-cols-1
               md:grid-cols-2
               xl:grid-cols-4 gap-4 mt-5"
      >

        <!-- OVERALL -->

        <div
          class="p-5 rounded-xl
                 bg-slate-50 border
                 border-slate-200"
        >

          <div
            class="flex items-center
                   justify-between"
          >

            <p
              class="font-semibold
                     text-slate-700"
            >
              Overall
            </p>

            <span
              class="text-[#8B1E23]"
            >
              ✓
            </span>

          </div>


          <p
            class="text-3xl font-bold
                   text-[#8B1E23] mt-4"
          >
            {{ overallCompliance }}%
          </p>


          <div
            class="h-2.5 bg-slate-200
                   rounded-full overflow-hidden mt-3"
          >

            <div
              class="h-full bg-[#8B1E23]
                     rounded-full transition-all"
              :style="{
                width: overallCompliance + '%'
              }"
            ></div>

          </div>


          <p
            class="text-xs text-slate-400 mt-2"
          >
            Combined live compliance
          </p>

        </div>


        <!-- ACTIVITY -->

        <div
          class="p-5 rounded-xl
                 bg-slate-50 border
                 border-slate-200"
        >

          <div
            class="flex items-center
                   justify-between"
          >

            <p
              class="font-semibold
                     text-slate-700"
            >
              Activity Compliance
            </p>

            <span
              class="text-[#8B1E23]"
            >
              ✓
            </span>

          </div>


          <p
            class="text-3xl font-bold
                   text-[#8B1E23] mt-4"
          >
            {{ activityCompliance }}%
          </p>


          <div
            class="h-2.5 bg-slate-200
                   rounded-full overflow-hidden mt-3"
          >

            <div
              class="h-full bg-[#8B1E23]
                     rounded-full transition-all"
              :style="{
                width: activityCompliance + '%'
              }"
            ></div>

          </div>


          <p
            class="text-xs text-slate-400 mt-2"
          >
            {{ completedActivities }}
            of
            {{ activities.length }}
            completed
          </p>

        </div>


        <!-- REPORT -->

        <div
          class="p-5 rounded-xl
                 bg-slate-50 border
                 border-slate-200"
        >

          <div
            class="flex items-center
                   justify-between"
          >

            <p
              class="font-semibold
                     text-slate-700"
            >
              Report Compliance
            </p>

            <span
              class="text-[#8B1E23]"
            >
              ✓
            </span>

          </div>


          <p
            class="text-3xl font-bold
                   text-[#8B1E23] mt-4"
          >
            {{ reportCompliance }}%
          </p>


          <div
            class="h-2.5 bg-slate-200
                   rounded-full overflow-hidden mt-3"
          >

            <div
              class="h-full bg-[#8B1E23]
                     rounded-full transition-all"
              :style="{
                width: reportCompliance + '%'
              }"
            ></div>

          </div>


          <p
            class="text-xs text-slate-400 mt-2"
          >
            {{ reviewedReports }}
            of
            {{ reports.length }}
            reviewed
          </p>

        </div>


        <!-- DEADLINE -->

        <div
          class="p-5 rounded-xl
                 bg-slate-50 border
                 border-slate-200"
        >

          <div
            class="flex items-center
                   justify-between"
          >

            <p
              class="font-semibold
                     text-slate-700"
            >
              Deadline Compliance
            </p>

            <span
              class="text-[#8B1E23]"
            >
              ✓
            </span>

          </div>


          <p
            class="text-3xl font-bold
                   text-[#8B1E23] mt-4"
          >
            {{ deadlineCompliance }}%
          </p>


          <div
            class="h-2.5 bg-slate-200
                   rounded-full overflow-hidden mt-3"
          >

            <div
              class="h-full bg-[#8B1E23]
                     rounded-full transition-all"
              :style="{
                width:
                  deadlineCompliance + '%'
              }"
            ></div>

          </div>


          <p
            class="text-xs text-slate-400 mt-2"
          >
            {{ overdueDeadlines }}
            overdue of
            {{ totalDeadlines }}
          </p>

        </div>

      </div>

    </section>


    <!-- =====================================================
         REGISTERED PERSONNEL
    ====================================================== -->

    <section
      class="bg-white border border-slate-200
             rounded-2xl shadow-sm p-6"
    >

      <div
        class="flex items-center
               justify-between gap-4
               border-b border-slate-200 pb-5"
      >

        <div>

          <h2
            class="text-xl font-bold
                   text-slate-900"
          >
            Registered Personnel
          </h2>

          <p
            class="text-sm text-slate-500 mt-1"
          >
            Live records from Personnel Management.
          </p>

        </div>


        <span
          class="px-3 py-1.5 rounded-full
                 bg-green-50 text-green-700
                 text-sm font-bold"
        >
          {{ activePersonnel }}
          Active
        </span>

      </div>


      <div
        v-if="personnel.length"
        class="grid grid-cols-1
               md:grid-cols-2
               xl:grid-cols-3 gap-3 mt-5"
      >

        <div
          v-for="person in personnel"
          :key="
            person.id ||
            person.identifier
          "
          class="p-4 rounded-xl
                 border border-slate-200
                 flex items-center gap-3"
        >

          <div
            class="h-11 w-11 rounded-full
                   bg-[#8B1E23] text-white
                   flex items-center
                   justify-center font-bold"
          >
            {{
              nameOf(person)
                .slice(0, 1)
                .toUpperCase()
            }}
          </div>


          <div
            class="min-w-0 flex-1"
          >

            <p
              class="font-bold
                     text-slate-900 truncate"
            >
              {{ nameOf(person) }}
            </p>

            <p
              class="text-xs
                     text-slate-500"
            >
              {{ person.rank || 'FO1' }}
              ·
              {{ person.status || 'Active' }}
            </p>

          </div>


          <span
            class="h-2.5 w-2.5
                   rounded-full bg-green-500"
          ></span>

        </div>

      </div>


      <div
        v-else
        class="py-10 text-center
               text-slate-400"
      >
        No registered personnel found.
      </div>

    </section>


    <!-- =====================================================
         ACTIVITIES + REPORTS
    ====================================================== -->

    <section
      class="grid grid-cols-1
             xl:grid-cols-2 gap-6"
    >

      <!-- ACTIVITIES -->

      <div
        class="bg-white border
               border-slate-200
               rounded-2xl shadow-sm p-6"
      >

        <div
          class="flex items-center
                 justify-between
                 border-b border-slate-200
                 pb-4"
        >

          <div>

            <h2
              class="text-xl font-bold
                     text-slate-900"
            >
              Recent Activities
            </h2>

            <p
              class="text-sm text-slate-500 mt-1"
            >
              {{ activities.length }}
              activity records
            </p>

          </div>


          <span
            class="font-bold
                   text-[#8B1E23]"
          >
            {{ activityCompliance }}%
          </span>

        </div>


        <div
          class="space-y-3 mt-5"
        >

          <button
            v-for="item in recentActivities"
            :key="
              item.id ||
              activityTitle(item)
            "
            @click="
              openDetails(
                item,
                'activity'
              )
            "
            class="w-full text-left
                   p-4 rounded-xl
                   border border-slate-200
                   hover:bg-slate-50
                   transition"
          >

            <div
              class="flex items-center
                     justify-between gap-3"
            >

              <p
                class="font-semibold
                       text-slate-900 truncate"
              >
                {{ activityTitle(item) }}
              </p>


              <span
                :class="[
                  'px-2 py-1 rounded-full border text-xs font-bold',
                  statusClass(item.status)
                ]"
              >
                {{ item.status || 'Scheduled' }}
              </span>

            </div>


            <p
              class="text-xs
                     text-slate-500 mt-1"
            >
              {{ activityPerson(item) }}
              ·
              {{ formatDate(
                activityDate(item)
              ) }}
            </p>

          </button>


          <p
            v-if="!recentActivities.length"
            class="py-8 text-center
                   text-slate-400"
          >
            No activity records found.
          </p>

        </div>

      </div>


      <!-- REPORTS -->

      <div
        class="bg-white border
               border-slate-200
               rounded-2xl shadow-sm p-6"
      >

        <div
          class="flex items-center
                 justify-between
                 border-b border-slate-200
                 pb-4"
        >

          <div>

            <h2
              class="text-xl font-bold
                     text-slate-900"
            >
              Recent Reports
            </h2>

            <p
              class="text-sm text-slate-500 mt-1"
            >
              {{ reports.length }}
              report records
            </p>

          </div>


          <span
            class="font-bold
                   text-[#8B1E23]"
          >
            {{ pendingReports }}
            Pending
          </span>

        </div>


        <div
          class="space-y-3 mt-5"
        >

          <button
            v-for="item in recentReports"
            :key="
              item.id ||
              reportTitle(item)
            "
            @click="
              openDetails(
                item,
                'report'
              )
            "
            class="w-full text-left
                   p-4 rounded-xl
                   border border-slate-200
                   hover:bg-slate-50
                   transition"
          >

            <div
              class="flex items-center
                     justify-between gap-3"
            >

              <p
                class="font-semibold
                       text-slate-900 truncate"
              >
                {{ reportTitle(item) }}
              </p>


              <span
                :class="[
                  'px-2 py-1 rounded-full border text-xs font-bold',
                  statusClass(item.status)
                ]"
              >
                {{ item.status || 'Pending' }}
              </span>

            </div>


            <p
              class="text-xs
                     text-slate-500 mt-1"
            >
              {{ reportPerson(item) }}
            </p>

          </button>


          <p
            v-if="!recentReports.length"
            class="py-8 text-center
                   text-slate-400"
          >
            No report records found.
          </p>

        </div>

      </div>

    </section>


    <!-- =====================================================
         DEADLINES + NOTIFICATIONS
    ====================================================== -->

    <section
      class="grid grid-cols-1
             lg:grid-cols-2 gap-6"
    >

      <!-- DEADLINE MONITOR -->

      <div
        class="bg-white border
               border-slate-200
               rounded-2xl shadow-sm p-6"
      >

        <div
          class="flex items-center
                 justify-between
                 border-b border-slate-200
                 pb-4"
        >

          <div>

            <h2
              class="text-xl font-bold
                     text-slate-900"
            >
              Deadline Monitor
            </h2>

            <p
              class="text-sm text-slate-500 mt-1"
            >
              Tasks and report deadlines
            </p>

          </div>


          <span
            class="px-3 py-1 rounded-full
                   bg-red-50 text-red-700
                   text-xs font-bold"
          >
            {{ overdueDeadlines }}
            Overdue
          </span>

        </div>


        <div
          class="grid grid-cols-2 gap-4 mt-5"
        >

          <div
            class="p-4 rounded-xl
                   bg-red-50"
          >

            <p
              class="text-2xl font-bold
                     text-[#8B1E23]"
            >
              {{ overdueDeadlines }}
            </p>

            <p
              class="text-xs
                     text-slate-500 mt-1"
            >
              Overdue
            </p>

          </div>


          <div
            class="p-4 rounded-xl
                   bg-green-50"
          >

            <p
              class="text-2xl font-bold
                     text-green-600"
            >
              {{
                Math.max(
                  totalDeadlines -
                  overdueDeadlines,
                  0
                )
              }}
            </p>

            <p
              class="text-xs
                     text-slate-500 mt-1"
            >
              On Track
            </p>

          </div>

        </div>


        <div
          class="space-y-2 mt-4"
        >

          <button
            v-for="task in overdueTasks.slice(0, 5)"
            :key="
              task.id ||
              taskTitle(task)
            "
            @click="
              openDetails(
                task,
                'task'
              )
            "
            class="w-full text-left
                   p-3 rounded-lg
                   border border-red-100
                   bg-red-50"
          >

            <p
              class="font-semibold
                     text-slate-800 text-sm"
            >
              {{ taskTitle(task) }}
            </p>

            <p
              class="text-xs
                     text-red-700 mt-1"
            >
              Due
              {{ formatDate(
                taskDate(task)
              ) }}
            </p>

          </button>


          <p
            v-if="
              !overdueTasks.length &&
              !overdueReports.length
            "
            class="text-sm
                   text-green-600
                   font-semibold py-4"
          >
            No overdue deadlines.
          </p>

        </div>

      </div>


      <!-- NOTIFICATIONS -->

      <div
        class="bg-white border
               border-slate-200
               rounded-2xl shadow-sm p-6"
      >

        <div
          class="flex items-center
                 justify-between
                 border-b border-slate-200
                 pb-4"
        >

          <div>

            <h2
              class="text-xl font-bold
                     text-slate-900"
            >
              Notifications
            </h2>

            <p
              class="text-sm text-slate-500 mt-1"
            >
              Live notification count
            </p>

          </div>


          <span
            class="px-3 py-1 rounded-full
                   bg-red-50 text-red-700
                   text-xs font-bold"
          >
            {{ unreadNotifications }}
            New
          </span>

        </div>


        <div
          class="grid grid-cols-3 gap-3 mt-5"
        >

          <div
            class="p-4 rounded-xl
                   bg-slate-50 text-center"
          >

            <p
              class="text-2xl font-bold
                     text-slate-900"
            >
              {{ notifications.length }}
            </p>

            <p
              class="text-xs
                     text-slate-500"
            >
              Total
            </p>

          </div>


          <div
            class="p-4 rounded-xl
                   bg-red-50 text-center"
          >

            <p
              class="text-2xl font-bold
                     text-[#8B1E23]"
            >
              {{ unreadNotifications }}
            </p>

            <p
              class="text-xs
                     text-slate-500"
            >
              Unread
            </p>

          </div>


          <div
            class="p-4 rounded-xl
                   bg-green-50 text-center"
          >

            <p
              class="text-2xl font-bold
                     text-green-600"
            >
              {{
                Math.max(
                  notifications.length -
                  unreadNotifications,
                  0
                )
              }}
            </p>

            <p
              class="text-xs
                     text-slate-500"
            >
              Read
            </p>

          </div>

        </div>


        <div
          class="mt-4 space-y-2"
        >

          <div
            v-for="
              notification in
                notifications.slice(0, 4)
            "
            :key="
              notification.id ||
              notification.createdAt ||
              notification.title
            "
            class="p-3 rounded-lg
                   bg-slate-50
                   border border-slate-100"
          >

            <div
              class="flex justify-between
                     gap-2"
            >

              <p
                class="font-semibold
                       text-sm
                       text-slate-800"
              >
                {{
                  notification.title ||
                  notification.message ||
                  notification.type ||
                  'Notification'
                }}
              </p>


              <span
                v-if="
                  !notification.read &&
                  !notification.isRead
                "
                class="text-[10px]
                       font-bold
                       text-red-700"
              >
                UNREAD
              </span>

            </div>


            <p
              v-if="
                notification.message &&
                notification.title
              "
              class="text-xs
                     text-slate-500 mt-1"
            >
              {{ notification.message }}
            </p>

          </div>


          <p
            v-if="!notifications.length"
            class="py-6 text-center
                   text-slate-400"
          >
            No notifications found.
          </p>

        </div>

      </div>

    </section>


    <!-- =====================================================
         DETAILS MODAL
    ====================================================== -->

    <div
      v-if="selected"
      class="fixed inset-0 z-50
             bg-slate-900/50
             flex items-center
             justify-center p-4"
      @click.self="closeDetails"
    >

      <div
        class="w-full max-w-lg
               bg-white rounded-2xl
               shadow-2xl overflow-hidden"
      >

        <div
          class="h-2 bg-[#8B1E23]"
        ></div>


        <div class="p-6">

          <div
            class="flex items-start
                   justify-between gap-4"
          >

            <div>

              <p
                class="text-xs uppercase
                       font-bold tracking-wide
                       text-[#8B1E23]"
              >
                {{ selectedType }}
                Details
              </p>


              <h3
                class="text-xl font-bold
                       text-slate-900 mt-1"
              >
                {{
                  selectedType === 'activity'
                    ? activityTitle(selected)
                    : selectedType === 'report'
                      ? reportTitle(selected)
                      : taskTitle(selected)
                }}
              </h3>

            </div>


            <button
              @click="closeDetails"
              class="text-slate-400
                     hover:text-slate-700
                     text-2xl"
            >
              ×
            </button>

          </div>


          <div
            class="mt-5 space-y-3
                   text-sm
                   text-slate-700"
          >

            <p>

              <b>Status:</b>

              {{ selected.status || 'Pending' }}

            </p>


            <p
              v-if="
                selectedType ===
                'activity'
              "
            >

              <b>Personnel:</b>

              {{ activityPerson(selected) }}

            </p>


            <p
              v-if="
                selectedType ===
                'report'
              "
            >

              <b>Personnel:</b>

              {{ reportPerson(selected) }}

            </p>


            <p
              v-if="
                selectedType ===
                'activity'
              "
            >

              <b>Date:</b>

              {{
                formatDate(
                  activityDate(
                    selected
                  )
                )
              }}

            </p>


            <p
              v-if="
                selectedType ===
                'task'
              "
            >

              <b>Deadline:</b>

              {{
                formatDate(
                  taskDate(selected)
                )
              }}

            </p>


            <p
              v-if="
                selectedType ===
                  'report' &&
                (
                  selected.deadline ||
                  selected.dueDate
                )
              "
            >

              <b>Deadline:</b>

              {{
                formatDate(
                  selected.deadline ||
                  selected.dueDate
                )
              }}

            </p>


            <p
              v-if="
                selected.description
              "
            >

              <b>Description:</b>

              {{ selected.description }}

            </p>

          </div>


          <div
            class="flex justify-end mt-6"
          > 

            <button
              @click="closeDetails"
              class="px-5 py-2.5
                     rounded-xl
                     bg-[#8B1E23]
                     text-white
                     font-semibold
                     hover:bg-[#72181D]"
            >
              Close
            </button>

          </div>

        </div>

      </div>

    </div>

  </div>

</template>