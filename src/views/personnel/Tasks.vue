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
            Monitor and manage your assigned duties and activities.
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
            <p class="text-sm text-slate-500">Total Tasks</p>
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
            <p class="text-sm text-slate-500">Pending</p>
            <p class="text-3xl font-bold text-amber-600 mt-1">
              {{ pendingTasks.toString().padStart(2, '0') }}
            </p>
          </div>

          <div class="h-12 w-12 rounded-xl bg-amber-50 flex items-center justify-center">
            <span class="text-xl">⏳</span>
          </div>
        </div>
      </div>


      <!-- COMPLETED -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-slate-500">Completed</p>
            <p class="text-3xl font-bold text-green-600 mt-1">
              {{ completedTasks.toString().padStart(2, '0') }}
            </p>
          </div>

          <div class="h-12 w-12 rounded-xl bg-green-50 flex items-center justify-center">
            <span class="text-xl font-bold">✓</span>
          </div>
        </div>
      </div>


      <!-- OVERDUE -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-slate-500">Overdue</p>
            <p class="text-3xl font-bold text-red-600 mt-1">
              {{ overdueTasks.toString().padStart(2, '0') }}
            </p>
          </div>

          <div class="h-12 w-12 rounded-xl bg-red-50 flex items-center justify-center">
            <span class="text-xl font-bold">!</span>
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
            Search and filter your current assignments.
          </p>
        </div>


        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 w-full lg:w-auto">

          <!-- SEARCH -->
          <div class="relative">
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
            <option value="In Progress">In Progress</option>
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
            Tasks assigned to your personnel account.
          </p>
        </div>

        <span class="px-4 py-2 rounded-full bg-blue-50 text-blue-700
                     text-sm font-bold">
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

            <!-- TASK INFO -->
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


                <p class="text-sm text-slate-500 mt-1">
                  {{ task.description }}
                </p>

                <div class="flex flex-wrap gap-x-5 gap-y-1 mt-2">

                  <p class="text-sm text-slate-500">
                    <span class="font-semibold">Due:</span>
                    {{ task.due }}
                  </p>

                  <p class="text-sm text-slate-500">
                    <span class="font-semibold">Location:</span>
                    {{ task.location }}
                  </p>

                </div>

              </div>

            </div>


            <!-- ACTION BUTTONS -->
            <div class="flex flex-col sm:flex-row gap-3 shrink-0">

              <button
                @click="viewDetails(task)"
                class="px-4 py-3 rounded-xl border border-slate-300
                       bg-white text-slate-700 text-sm font-bold
                       hover:bg-slate-100 transition"
              >
                View Details
              </button>

              <button
                v-if="task.status !== 'Completed'"
                @click="updateStatus(task)"
                class="px-5 py-3 rounded-xl bg-[#8B1E23]
                       text-white text-sm font-bold
                       hover:bg-[#72181D] transition"
              >
                Update Status
              </button>

              <span
                v-else
                class="px-5 py-3 rounded-xl bg-green-100
                       text-green-700 text-sm font-bold text-center"
              >
                Completed
              </span>

            </div>

          </div>


          <!-- PROGRESS -->
          <div class="mt-5">

            <div class="flex justify-between mb-2">

              <span class="text-xs font-semibold text-slate-500">
                Task Progress
              </span>

              <span class="text-xs font-bold text-slate-700">
                {{ task.progress }}%
              </span>

            </div>

            <div class="w-full h-2.5 bg-slate-200 rounded-full overflow-hidden">

              <div
                class="h-full rounded-full transition-all duration-500"
                :class="progressClass(task.status)"
                :style="{ width: `${task.progress}%` }"
              ></div>

            </div>

          </div>

        </div>

      </div>


      <!-- EMPTY STATE -->
      <div
        v-else
        class="mt-6 py-14 text-center border-2 border-dashed
               border-slate-200 rounded-xl"
      >
        <div class="text-4xl mb-3">
          📋
        </div>

        <h4 class="font-bold text-slate-900">
          No tasks found
        </h4>

        <p class="text-sm text-slate-500 mt-1">
          Try changing your search or filters.
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

                <p class="text-sm text-slate-500 mt-1">
                  {{ task.location }}
                </p>

                <p
                  class="text-xs font-bold mt-2"
                  :class="task.priority === 'High'
                    ? 'text-red-600'
                    : 'text-amber-600'"
                >
                  {{ task.priority }} Priority • Due {{ task.due }}
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
          Your latest completed assignments.
        </p>


        <div class="mt-5 space-y-4">

          <div
            v-for="task in recentlyCompleted"
            :key="task.id"
            class="flex items-center gap-4 p-4 rounded-xl bg-green-50"
          >

            <div class="h-10 w-10 rounded-full bg-green-100
                        flex items-center justify-center shrink-0">

              <span class="text-green-600 font-bold">
                ✓
              </span>

            </div>

            <div class="min-w-0">

              <p class="font-bold text-slate-900">
                {{ task.title }}
              </p>

              <p class="text-xs text-slate-500 mt-1">
                {{ task.completedAt }}
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

      <div class="bg-white rounded-2xl shadow-xl w-full max-w-2xl
                  max-h-[90vh] overflow-y-auto">

        <!-- MODAL HEADER -->
        <div class="flex items-start justify-between p-6
                    border-b border-slate-200">

          <div>
            <p class="text-xs font-bold uppercase tracking-wide text-[#8B1E23]">
              Task Details
            </p>

            <h3 class="text-xl font-bold text-slate-900 mt-1">
              {{ selectedTask.title }}
            </h3>
          </div>

          <button
            @click="closeDetails"
            class="h-9 w-9 rounded-lg bg-slate-100
                   text-slate-500 hover:bg-slate-200
                   text-xl"
          >
            ×
          </button>

        </div>


        <!-- MODAL BODY -->
        <div class="p-6 space-y-6">

          <div>
            <p class="text-sm font-semibold text-slate-500">
              Description
            </p>

            <p class="text-sm text-slate-800 mt-1">
              {{ selectedTask.description }}
            </p>
          </div>


          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">

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


            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-500">
                Due Date
              </p>

              <p class="font-bold text-slate-900 mt-1">
                {{ selectedTask.due }}
              </p>
            </div>


            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-500">
                Location
              </p>

              <p class="font-bold text-slate-900 mt-1">
                {{ selectedTask.location }}
              </p>
            </div>

          </div>


          <!-- PROGRESS -->
          <div>

            <div class="flex justify-between mb-2">

              <span class="text-sm font-semibold text-slate-600">
                Progress
              </span>

              <span class="text-sm font-bold text-slate-900">
                {{ selectedTask.progress }}%
              </span>

            </div>

            <div class="w-full h-3 bg-slate-200 rounded-full overflow-hidden">

              <div
                class="h-full rounded-full transition-all"
                :class="progressClass(selectedTask.status)"
                :style="{ width: `${selectedTask.progress}%` }"
              ></div>

            </div>

          </div>

        </div>


        <!-- MODAL FOOTER -->
        <div class="flex flex-col sm:flex-row justify-end gap-3
                    p-6 border-t border-slate-200">

          <button
            @click="closeDetails"
            class="px-5 py-3 rounded-xl border border-slate-300
                   text-slate-700 text-sm font-bold
                   hover:bg-slate-100"
          >
            Close
          </button>

          <button
            v-if="selectedTask.status !== 'Completed'"
            @click="updateStatus(selectedTask)"
            class="px-5 py-3 rounded-xl bg-[#8B1E23]
                   text-white text-sm font-bold
                   hover:bg-[#72181D]"
          >
            Update Status
          </button>

        </div>

      </div>

    </div>

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
  },

  taskList: {
    type: Array,
    required: false,
    default: () => []
  }
})


/* =========================================================
   LOCAL TASK DATA
   Temporary frontend data.
   This can later be replaced with Django API data.
========================================================= */
const tasks = ref([
  {
    id: 1,
    title: 'Fire Safety Inspection',
    description: 'Conduct fire safety inspection and submit the inspection findings.',
    due: 'Today • 09:00 AM',
    location: 'Public Market Complex',
    priority: 'High',
    status: 'Pending',
    progress: 60
  },

  {
    id: 2,
    title: 'Monthly Activity Report',
    description: 'Prepare and submit the monthly station activity report.',
    due: 'Tomorrow',
    location: 'BFP Balingasag Station',
    priority: 'High',
    status: 'Pending',
    progress: 40
  },

  {
    id: 3,
    title: 'Equipment Inspection',
    description: 'Inspect assigned firefighting equipment and update equipment records.',
    due: 'Sept. 16, 2026',
    location: 'BFP Balingasag Station',
    priority: 'Medium',
    status: 'In Progress',
    progress: 70
  },

  {
    id: 4,
    title: 'Fire Drill Evaluation',
    description: 'Evaluate the recent fire drill and record the results.',
    due: 'Completed',
    location: 'Station Training Area',
    priority: 'Medium',
    status: 'Completed',
    progress: 100,
    completedAt: 'Completed today'
  },

  {
    id: 5,
    title: 'Station Safety Checklist',
    description: 'Complete the assigned station safety checklist.',
    due: 'Sept. 14, 2026',
    location: 'BFP Balingasag Station',
    priority: 'Low',
    status: 'Overdue',
    progress: 20
  }
])


/* =========================================================
   IF PARENT PASSES TASKS
========================================================= */
if (props.taskList.length > 0) {
  tasks.value = props.taskList
}


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
   FILTERED TASKS
========================================================= */
const filteredTasks = computed(() => {
  return tasks.value.filter(task => {

    const matchesSearch =
      task.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      task.description.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      task.location.toLowerCase().includes(searchQuery.value.toLowerCase())

    const matchesStatus =
      selectedStatus.value === 'All' ||
      task.status === selectedStatus.value

    const matchesPriority =
      selectedPriority.value === 'All' ||
      task.priority === selectedPriority.value

    return matchesSearch && matchesStatus && matchesPriority
  })
})


/* =========================================================
   STATISTICS
========================================================= */
const pendingTasks = computed(() =>
  tasks.value.filter(task => task.status === 'Pending').length
)

const completedTasks = computed(() =>
  tasks.value.filter(task => task.status === 'Completed').length
)

const overdueTasks = computed(() =>
  tasks.value.filter(task => task.status === 'Overdue').length
)


/* =========================================================
   PRIORITY TASKS
========================================================= */
const priorityTasks = computed(() =>
  tasks.value.filter(
    task =>
      task.status !== 'Completed' &&
      task.priority === 'High'
  )
)


/* =========================================================
   RECENTLY COMPLETED
========================================================= */
const recentlyCompleted = computed(() =>
  tasks.value.filter(
    task => task.status === 'Completed'
  )
)


/* =========================================================
   VIEW DETAILS
========================================================= */
const viewDetails = (task) => {
  selectedTask.value = task
}


/* =========================================================
   CLOSE DETAILS
========================================================= */
const closeDetails = () => {
  selectedTask.value = null
}


/* =========================================================
   UPDATE STATUS
========================================================= */
const updateStatus = (task) => {

  if (task.status === 'Pending') {
    task.status = 'In Progress'
    task.progress = Math.max(task.progress, 60)
  }

  else if (task.status === 'In Progress') {
    task.status = 'Completed'
    task.progress = 100
    task.completedAt = 'Completed just now'
  }

  else if (task.status === 'Overdue') {
    task.status = 'In Progress'
    task.progress = Math.max(task.progress, 40)
  }

  else {
    task.status = 'Completed'
    task.progress = 100
  }

  selectedTask.value = null
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
const statusClass = (status) => {

  const classes = {
    Pending: 'bg-amber-100 text-amber-700',
    'In Progress': 'bg-blue-100 text-blue-700',
    Completed: 'bg-green-100 text-green-700',
    Overdue: 'bg-red-100 text-red-700'
  }

  return classes[status] || 'bg-slate-100 text-slate-700'
}


/* =========================================================
   PRIORITY COLORS
========================================================= */
const priorityClass = (priority) => {

  const classes = {
    High: 'bg-red-100 text-red-700',
    Medium: 'bg-amber-100 text-amber-700',
    Low: 'bg-green-100 text-green-700'
  }

  return classes[priority] || 'bg-slate-100 text-slate-700'
}


/* =========================================================
   PRIORITY ICON BACKGROUND
========================================================= */
const priorityIconBg = (priority) => {

  const classes = {
    High: 'bg-red-100',
    Medium: 'bg-amber-100',
    Low: 'bg-green-100'
  }

  return classes[priority] || 'bg-blue-100'
}


/* =========================================================
   PRIORITY ICON COLOR
========================================================= */
const priorityIconColor = (priority) => {

  const classes = {
    High: 'text-red-600',
    Medium: 'text-amber-600',
    Low: 'text-green-600'
  }

  return classes[priority] || 'text-blue-600'
}


/* =========================================================
   PROGRESS COLOR
========================================================= */
const progressClass = (status) => {

  const classes = {
    Pending: 'bg-amber-500',
    'In Progress': 'bg-blue-600',
    Completed: 'bg-green-600',
    Overdue: 'bg-red-600'
  }

  return classes[status] || 'bg-[#8B1E23]'
}
</script>