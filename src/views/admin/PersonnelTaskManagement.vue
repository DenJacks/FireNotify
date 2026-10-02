<script setup>
import {
  computed,
  ref,
  onMounted,
  onUnmounted
} from 'vue'

import { getTaskActivityEvidence } from '../../utils/reportFileStorage.js'
import { resolvePersonnelName } from '../../utils/personnelName.js'
import { createTask as createTaskInApi, deleteTask as deleteTaskFromApi, getTasks, updateTask as updateTaskInApi } from '../../utils/taskService.js'
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

  registeredUsers: {
    type: Array,
    default: () => []
  }
})

/* =========================================================
   EMITS
========================================================= */

const emit = defineEmits([
  'update-user',
  'delete-user'
])

/* =========================================================
   TASK STORAGE
   IMPORTANT:
   ADMIN TASKS ARE STORED HERE ONLY.
   DO NOT USE fireNotifyActivities.
========================================================= */

const TASK_STORAGE_KEY = 'firenotify_tasks'

const tasks = ref([])
const personnelDirectory = ref([])

/* =========================================================
   FILTERS
========================================================= */

const searchQuery = ref('')
const selectedStatus = ref('All Duty Status')
const selectedRank = ref('All Ranks')

/* =========================================================
   MODALS
========================================================= */

const showDetailsModal = ref(false)
const showDeleteModal = ref(false)
const showTaskModal = ref(false)
const showAssignmentModal = ref(false)
const showSubmissionModal = ref(false)

/* =========================================================
   SELECTED PERSONNEL
========================================================= */

const selectedPersonnel = ref(null)
const personnelToDelete = ref(null)
const selectedTaskSubmission = ref(null)
const editingTask = ref(null)
const submissionEvidence = ref([])
const submissionEvidenceUrls = ref([])
const returnNote = ref('')

/* =========================================================
   OLD PERSONNEL ASSIGNMENT
========================================================= */

const assignmentInput = ref('')

/* =========================================================
   TOAST
========================================================= */

const toastMessage = ref('')
const toastType = ref('success')

/* =========================================================
   TASK FORM
========================================================= */

const taskForm = ref({
  title: '',
  subtopic: '',
  type: 'General Task',
  priority: 'Medium',
  location: '',
  dueDate: '',
  time: '',
  description: ''
})

/* =========================================================
   PERSONNEL
========================================================= */

const personnel = computed(() => {
  const users = personnelDirectory.value.length
    ? personnelDirectory.value
    : props.registeredUsers

  return users
    .filter(user => String(user?.role || '').trim().toUpperCase() === 'PERSONNEL')
    .map(user => ({
      ...user,

      id: user.id,

      username:
        user.username ||
        user.identifier ||
        '',

      firstName:
        user.firstName || '',

      lastName:
        user.lastName || '',

      name:
        user.name ||
        `${user.firstName || ''} ${user.lastName || ''}`.trim(),

      rank:
        user.rank || 'FO1',

      position:
        user.position || 'Fire Officer',

      shift:
        user.shift || 'Morning',

      status:
        user.status || 'On Duty',

      contact:
        user.contact || '',

      email:
        user.email ||
        user.identifier ||
        '',

      assignment:
        user.assignment || ''
    }))
})

/* =========================================================
   RANKS
========================================================= */

const ranks = computed(() => {
  return [
    ...new Set(
      personnel.value
        .map(person => person.rank)
        .filter(Boolean)
    )
  ]
})

/* =========================================================
   FILTERED PERSONNEL
========================================================= */

const filteredPersonnel = computed(() => {

  const query =
    searchQuery.value
      .toLowerCase()
      .trim()

  return personnel.value.filter(person => {

    const searchText = [
      fullName(person),
      person.id,
      person.rank,
      person.position,
      person.shift,
      person.assignment,
      person.email
    ]
      .filter(Boolean)
      .join(' ')
      .toLowerCase()

    const matchesSearch =
      !query ||
      searchText.includes(query)

    const matchesStatus =
      selectedStatus.value === 'All Duty Status' ||
      person.status === selectedStatus.value

    const matchesRank =
      selectedRank.value === 'All Ranks' ||
      person.rank === selectedRank.value

    return (
      matchesSearch &&
      matchesStatus &&
      matchesRank
    )
  })
})

/* =========================================================
   STATISTICS
========================================================= */

const totalPersonnel = computed(() =>
  personnel.value.length
)

const onDutyCount = computed(() =>
  personnel.value.filter(
    person => person.status === 'On Duty'
  ).length
)

const leaveCount = computed(() =>
  personnel.value.filter(
    person => person.status === 'On Leave'
  ).length
)

const offDutyCount = computed(() =>
  personnel.value.filter(
    person => person.status === 'Off Duty'
  ).length
)

const onDutyPercentage = computed(() => {

  if (!totalPersonnel.value) {
    return 0
  }

  return Math.round(
    (onDutyCount.value /
      totalPersonnel.value) *
      100
  )
})

/* =========================================================
   SHIFT SUMMARY
========================================================= */

const shiftSummary = computed(() => {

  const shifts = [
    'Morning',
    'Afternoon',
    'Night'
  ]

  return shifts.map(shift => {

    const members =
      personnel.value.filter(
        person =>
          person.shift === shift
      )

    const onDuty =
      members.filter(
        person =>
          person.status === 'On Duty'
      ).length

    const coverage =
      members.length
        ? Math.round(
            (onDuty /
              members.length) *
              100
          )
        : 0

    let status = 'Low Coverage'

    if (coverage >= 80) {
      status = 'Fully Staffed'
    } else if (coverage >= 50) {
      status = 'On Schedule'
    }

    return {
      shift,
      total: members.length,
      onDuty,
      coverage,
      status
    }
  })
})

/* =========================================================
   HELPERS
========================================================= */

const fullName = person => {

  return (
    person?.name ||
    `${person?.firstName || ''} ${person?.lastName || ''}`
  ).trim()
}

const initials = person => {

  return (
    `${person?.firstName?.charAt(0) || ''}${person?.lastName?.charAt(0) || ''}`
  ).toUpperCase()
}

const getCurrentUserName = () => {

  const user = props.currentUser

  if (!user) {
    return 'Administrator'
  }

  return (
    user.name ||
    `${user.firstName || ''} ${user.lastName || ''}`.trim() ||
    user.username ||
    'Administrator'
  )
}

const assignedPersonnelName = task => {
  const assigned = task?.assignedToId ?? task?.assigned_to ?? task?.assigned_personnel ?? task?.assignedToName ?? task?.assignedTo
  const assignedId = assigned && typeof assigned === 'object'
    ? assigned.id ?? assigned.userId ?? ''
    : assigned
  const person = personnel.value.find(user => String(user.id) === String(assignedId))

  if (person) {
    return fullName(person) || person.username || person.email || 'Personnel unavailable'
  }

  if (assigned && typeof assigned === 'object') {
    const name = `${assigned.firstName || assigned.first_name || ''} ${assigned.lastName || assigned.last_name || ''}`.trim()
    return name || assigned.username || assigned.email || 'Personnel unavailable'
  }

  return resolvePersonnelName(assigned, personnel.value, 'Personnel unavailable')
}

const showToast = (
  message,
  type = 'success'
) => {

  toastMessage.value = message
  toastType.value = type

  setTimeout(() => {
    toastMessage.value = ''
  }, 3000)
}

/* =========================================================
   FILTER HELPERS
========================================================= */

const hasFilters = computed(() => {

  return (
    searchQuery.value ||
    selectedStatus.value !==
      'All Duty Status' ||
    selectedRank.value !==
      'All Ranks'
  )
})

const clearFilters = () => {

  searchQuery.value = ''

  selectedStatus.value =
    'All Duty Status'

  selectedRank.value =
    'All Ranks'
}

/* =========================================================
   STATUS CLASS
========================================================= */

const getStatusClass = status => {

  const classes = {

    'On Duty':
      'bg-green-50 text-green-700 border-green-200',

    'On Leave':
      'bg-yellow-50 text-yellow-700 border-yellow-200',

    'Off Duty':
      'bg-slate-100 text-slate-600 border-slate-200'
  }

  return (
    classes[status] ||
    classes['Off Duty']
  )
}

/* =========================================================
   TASK STATUS CLASS
========================================================= */

const getTaskStatusClass = status => {

  const classes = {

    Pending:
      'bg-amber-50 text-amber-700',

    Assigned:
      'bg-slate-100 text-slate-700',

    'In Progress':
      'bg-blue-50 text-blue-700',

    Submitted:
      'bg-purple-50 text-purple-700',

    'For Verification':
      'bg-purple-50 text-purple-700',

    Returned:
      'bg-yellow-50 text-yellow-700',

    Verified:
      'bg-green-50 text-green-700',

    Completed:
      'bg-green-50 text-green-700',

    Overdue:
      'bg-red-50 text-red-700'
  }

  return (
    classes[status] ||
    'bg-slate-100 text-slate-600'
  )
}

const openTaskSubmission = async task => {
  selectedTaskSubmission.value = task
  returnNote.value = ''
  submissionEvidenceUrls.value.forEach(url => URL.revokeObjectURL(url))
  submissionEvidence.value = await getTaskActivityEvidence({
    recordId: task.id,
    recordType: 'task'
  })
  submissionEvidenceUrls.value = submissionEvidence.value.map(item => URL.createObjectURL(item.file))
  showSubmissionModal.value = true
}

const verifyTask = async task => {
  try {
    const updated = await updateTaskInApi(task.id, { status: 'Verified', progress: 100 })
    tasks.value = tasks.value.map(item => item.id === task.id ? updated : item)
  } catch (error) {
    showToast(error.message, 'error')
    return
  }
  saveTasks()
  showSubmissionModal.value = false
  submissionEvidenceUrls.value.forEach(url => URL.revokeObjectURL(url))
  submissionEvidenceUrls.value = []
  showToast('Task submission verified successfully.')
}

const returnTaskForRevision = async task => {
  const note = returnNote.value.trim()
  if (!note) {
    showToast('Please provide a revision note.', 'error')
    return
  }

  try {
    const updated = await updateTaskInApi(task.id, { status: 'Returned', revisionNote: note })
    tasks.value = tasks.value.map(item => item.id === task.id ? updated : item)
  } catch (error) {
    showToast(error.message, 'error')
    return
  }
  saveTasks()
  showSubmissionModal.value = false
  submissionEvidenceUrls.value.forEach(url => URL.revokeObjectURL(url))
  submissionEvidenceUrls.value = []
  showToast('Task returned for revision.')
}

const openEvidence = item => {
  if (!item?.file) return
  const url = URL.createObjectURL(item.file)
  const preview = window.open(url, '_blank')
  if (!preview) window.location.href = url
  setTimeout(() => URL.revokeObjectURL(url), 15000)
}

/* =========================================================
   ASSIGNMENT CLASS
========================================================= */

const getAssignmentClass = status => {

  const classes = {

    Assigned:
      'bg-blue-50 text-blue-700',

    Updated:
      'bg-green-50 text-green-700',

    Promotion:
      'bg-yellow-50 text-yellow-700'
  }

  return (
    classes[status] ||
    'bg-slate-100 text-slate-600'
  )
}

/* =========================================================
   LOAD TASKS
========================================================= */

const loadPersonnelUsers = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/users/')
    if (!response.ok) throw new Error(`Users API HTTP ${response.status}`)
    const users = await response.json()
    if (!Array.isArray(users)) throw new Error('Invalid users response')

    personnelDirectory.value = users.map(user => {
      const firstName = user.firstName || user.first_name || ''
      const lastName = user.lastName || user.last_name || ''
      return {
        ...user,
        firstName,
        lastName,
        name: user.name || `${firstName} ${lastName}`.trim() || user.username || user.email || ''
      }
    })
  } catch (error) {
    console.error('FireNotify: Failed to load personnel from Django', error)
    personnelDirectory.value = []
  }
}

const loadTasks = async () => {
  try {
    tasks.value = await getTasks()
  } catch (error) {
    console.error('FireNotify: Failed to load tasks from Django', error)
    showToast('Unable to load tasks from the server.', 'error')
  }
}

/* =========================================================
   SAVE TASKS
========================================================= */

const saveTasks = () => window.dispatchEvent(new CustomEvent('fireNotifyTasksUpdated'))

/* =========================================================
   RESET TASK FORM
========================================================= */

const resetTaskForm = () => {
  taskForm.value = {
    title: '',
    subtopic: '',
    type: 'General Task',
    priority: 'Medium',
    location: '',
    dueDate: '',
    time: '',
    description: ''
  }
}

/* =========================================================
   VIEW PERSONNEL
========================================================= */

const viewPersonnel = person => {
  if (!person) return
  selectedPersonnel.value = person
  showDetailsModal.value = true
}

/* =========================================================
   EDIT PERSONNEL
========================================================= */

const openEditPersonnel = person => {

  if (!person) {
    return
  }

  selectedPersonnel.value = {
    ...person
  }

  showDetailsModal.value = false

  showToast(
    'Personnel account details are managed through Registration.'
  )
}

/* =========================================================
   DELETE PERSONNEL
========================================================= */

const openDeletePersonnel = person => {

  if (!person) {
    return
  }

  personnelToDelete.value =
    person

  showDeleteModal.value = true
}

const cancelDelete = () => {

  showDeleteModal.value = false

  personnelToDelete.value =
    null
}

const deletePersonnel = () => {

  if (!personnelToDelete.value) {
    return
  }

  const userId =
    personnelToDelete.value.id

  const personName =
    fullName(
      personnelToDelete.value
    )

  if (!userId) {

    showToast(
      'Unable to delete personnel account.',
      'error'
    )

    return
  }

  /* REMOVE USER */
  emit(
    'delete-user',
    userId
  )

  /* REMOVE THEIR TASKS */
  tasks.value =
    tasks.value.filter(
      task =>
        String(
          task.assignedToId
        ) !==
        String(userId)
    )

  saveTasks()

  showDeleteModal.value =
    false

  personnelToDelete.value =
    null

  selectedPersonnel.value =
    null

  showDetailsModal.value =
    false

  showToast(
    `${personName} was removed from the roster.`
  )
}

/* =========================================================
   PERSONNEL ASSIGNMENT
   This is NOT the Task system.
========================================================= */

const openAssignment = person => {

  if (!person) {
    return
  }

  selectedPersonnel.value =
    person

  assignmentInput.value =
    person.assignment || ''

  showDetailsModal.value =
    false

  showAssignmentModal.value =
    true
}

const saveAssignment = () => {

  if (!selectedPersonnel.value) {
    return
  }

  const updatedUser = {

    ...selectedPersonnel.value,

    assignment:
      assignmentInput.value.trim()
  }

  emit(
    'update-user',
    updatedUser
  )

  showAssignmentModal.value =
    false

  showToast(
    'Personnel assignment updated successfully.'
  )
}

/* =========================================================
   UPDATE DUTY STATUS
========================================================= */

const updateStatus = (
  person,
  status
) => {

  if (!person) {
    return
  }

  emit(
    'update-user',
    {
      ...person,
      status
    }
  )

  showToast(
    `${fullName(person)} status changed to ${status}.`
  )
}

/* =========================================================
   OPEN TASK MODAL
========================================================= */

const openTaskModal = person => {

  if (!person) {
    return
  }

  selectedPersonnel.value =
    person

  editingTask.value = null

  resetTaskForm()

  showDetailsModal.value =
    false

  showTaskModal.value =
    true
}

const openEditTask = task => {
  const person = personnel.value.find(item => String(item.id) === String(task.assignedToId))
  if (!person) {
    showToast('Assigned personnel could not be found.', 'error')
    return
  }

  selectedPersonnel.value = person
  editingTask.value = task
  taskForm.value = {
    title: task.title || '',
    subtopic: task.subtopic || '',
    type: task.type || 'General Task',
    priority: task.priority || 'Medium',
    location: task.location || '',
    dueDate: task.dueDate || '',
    time: task.time || '',
    description: task.description || ''
  }
  showTaskModal.value = true
}

/* =========================================================
   SAVE / ASSIGN TASK
========================================================= */

const saveTask = async () => {

  if (!selectedPersonnel.value) {

    showToast(
      'Please select a personnel.',
      'error'
    )

    return
  }

  if (
    !taskForm.value.title.trim()
  ) {

    showToast(
      'Task title is required.',
      'error'
    )

    return
  }

  if (
    !taskForm.value.dueDate
  ) {

    showToast(
      'Due date is required.',
      'error'
    )

    return
  }

  const person =
    selectedPersonnel.value
  const wasEditing = Boolean(editingTask.value)

  /* =====================================================
     CREATE TASK
  ===================================================== */

  const newTask = {

    title:
      taskForm.value.title.trim(),

    subtopic:
      taskForm.value.subtopic.trim(),

    type:
      taskForm.value.type,

    priority:
      taskForm.value.priority,

    location:
      taskForm.value.location.trim() ||
      'BFP Balingasag',

    dueDate:
      taskForm.value.dueDate,

    time:
      taskForm.value.time ||
      '08:00',

    description:
      taskForm.value.description.trim(),

    /* =================================================
       PERSONNEL IDENTIFICATION
       NO BADGE NUMBER
       NO STATION FIELD
    ================================================= */

    assignedToId:
      person.id,

    assignedToUsername:
      person.username || '',

    assignedToName:
      fullName(person),

    assignedToEmail:
      person.email || '',

    /* =================================================
       ADMIN
    ================================================= */

    assignedBy:
      getCurrentUserName(),

    assignedById:
      props.currentUser?.id ||
      'admin-default',

    /* =================================================
       STATUS
    ================================================= */

    status:
      'Assigned',

    progress:
      0,

    startedAt:
      null,

    submittedAt:
      null,

    accomplishment:
      '',

    submittedBy:
      null,

    createdAt:
      new Date().toISOString()
  }

  /* =====================================================
     ADD TO TASK LIST
  ===================================================== */

  try {
    if (editingTask.value) {
      const updated = await updateTaskInApi(editingTask.value.id, {
        title: newTask.title,
        description: newTask.description,
        type: newTask.type,
        priority: newTask.priority,
        location: newTask.location,
        dueDate: newTask.dueDate,
        time: newTask.time,
        assignedToId: newTask.assignedToId
      })
      tasks.value = tasks.value.map(item => item.id === updated.id ? updated : item)
    } else {
      tasks.value.unshift(await createTaskInApi(newTask))
    }
  } catch (error) {
    showToast(error.message, 'error')
    return
  }
  saveTasks()

  /* =====================================================
     CLOSE MODAL
  ===================================================== */

  showTaskModal.value =
    false

  editingTask.value = null

  resetTaskForm()

  showToast(wasEditing
    ? `Task updated for ${fullName(person)}.`
    : `Task assigned to ${fullName(person)} successfully.`)

  console.log(
    'FireNotify: New task assigned',
    newTask
  )
}

/* =========================================================
   DELETE TASK
========================================================= */

const deleteTask = async task => {

  if (!task) {
    return
  }

  try {
    await deleteTaskFromApi(task.id)
  } catch (error) {
    showToast(error.message, 'error')
    return
  }
  tasks.value = tasks.value.filter(item => item.id !== task.id)

  saveTasks()

  showToast(
    'Task deleted successfully.'
  )
}

/* =========================================================
   ASSIGNED TASKS
========================================================= */

const assignedTasks = computed(() => {

  return tasks.value
})

/* =========================================================
   STORAGE SYNC
========================================================= */

const handleStorage = event => {

  if (
    event.key ===
    TASK_STORAGE_KEY
  ) {
    loadTasks()
  }
}

const handleTaskUpdate = () => {

  loadTasks()
}

/* =========================================================
   LIFECYCLE
========================================================= */

let taskSyncInterval = null

onMounted(async () => {
  await loadPersonnelUsers()
  await loadTasks()

  window.addEventListener(
    'storage',
    handleStorage
  )

  window.addEventListener(
    'fireNotifyTasksUpdated',
    handleTaskUpdate
  )

  /*
   * Backup sync.
   */
  taskSyncInterval = setInterval(loadTasks, 30000)
})

onUnmounted(() => {

  window.removeEventListener(
    'storage',
    handleStorage
  )

  window.removeEventListener(
    'fireNotifyTasksUpdated',
    handleTaskUpdate
  )

  if (taskSyncInterval) {

    clearInterval(
      taskSyncInterval
    )

    taskSyncInterval =
      null
  }
})
</script>

<template>

  <div class="space-y-4">

    <!-- =====================================================
         HEADER
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div
        class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4"
      >

        <div>

          <p
            class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]"
          >
            Personnel Management
          </p>

          <h2
            class="text-2xl font-bold text-slate-900 mt-1"
          >
            Station Personnel
          </h2>

          <p
            class="text-base text-slate-500 mt-1"
          >
            Manage registered personnel,
            assign tasks, and monitor duty status.
          </p>

        </div>

        <div
          class="px-5 py-3 rounded-xl bg-slate-50 border border-slate-200"
        >

          <p
            class="text-sm font-semibold text-slate-700"
          >
            Personnel accounts are created through Registration.
          </p>

        </div>

      </div>

    </section>


    <!-- =====================================================
         STATISTICS
    ====================================================== -->

    <section
      class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5"
    >

      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >

        <p
          class="text-3xl font-bold text-slate-900"
        >
          {{ totalPersonnel }}
        </p>

        <p
          class="text-sm text-slate-500 mt-1"
        >
          Total Personnel
        </p>

      </div>


      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >

        <p
          class="text-3xl font-bold text-green-600"
        >
          {{ onDutyCount }}
        </p>

        <p
          class="text-sm text-slate-500 mt-1"
        >
          On Duty
        </p>

        <p
          class="text-xs text-green-600 font-semibold mt-2"
        >
          {{ onDutyPercentage }}% staffing availability
        </p>

      </div>


      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >

        <p
          class="text-3xl font-bold text-yellow-600"
        >
          {{ String(leaveCount).padStart(2, '0') }}
        </p>

        <p
          class="text-sm text-slate-500 mt-1"
        >
          On Leave
        </p>

      </div>


      <div
        class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"
      >

        <p
          class="text-3xl font-bold text-slate-500"
        >
          {{ String(offDutyCount).padStart(2, '0') }}
        </p>

        <p
          class="text-sm text-slate-500 mt-1"
        >
          Off Duty
        </p>

      </div>

    </section>


    <!-- =====================================================
         FILTERS
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5"
    >

      <div
        class="flex flex-col lg:flex-row gap-4"
      >

        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search name, ID, rank, position, or assignment..."
          class="flex-1 h-12 px-4 rounded-xl border border-slate-300 text-base focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]"
        />

        <select
          v-model="selectedRank"
          class="h-12 px-4 rounded-xl border border-slate-300 text-base bg-white"
        >

          <option>
            All Ranks
          </option>

          <option
            v-for="rank in ranks"
            :key="rank"
          >
            {{ rank }}
          </option>

        </select>

        <select
          v-model="selectedStatus"
          class="h-12 px-4 rounded-xl border border-slate-300 text-base bg-white"
        >

          <option>
            All Duty Status
          </option>

          <option>
            On Duty
          </option>

          <option>
            Off Duty
          </option>

          <option>
            On Leave
          </option>

        </select>

        <button
          v-if="hasFilters"
          @click="clearFilters"
          class="h-12 px-5 rounded-xl border border-slate-300 text-slate-600 font-semibold hover:bg-slate-50"
        >
          Clear
        </button>

      </div>

      <p
        class="text-sm text-slate-500 mt-4"
      >

        Showing

        <span
          class="font-bold text-slate-800"
        >
          {{ filteredPersonnel.length }}
        </span>

        of

        <span
          class="font-bold text-slate-800"
        >
          {{ totalPersonnel }}
        </span>

        personnel

      </p>

    </section>


    <!-- =====================================================
         PERSONNEL ROSTER
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div class="mb-5">

        <h2
          class="text-xl font-bold text-slate-900"
        >
          Personnel Roster
        </h2>

        <p
          class="text-sm text-slate-500 mt-1"
        >
          Current registered station personnel
        </p>

      </div>


      <div
        v-if="filteredPersonnel.length"
        class="overflow-x-auto"
      >

        <table class="w-full text-left">

          <thead>

            <tr
              class="border-b border-slate-200 text-xs font-bold uppercase tracking-wide text-slate-400"
            >

              <th class="pb-4 pr-5">
                Personnel
              </th>

              <th class="pb-4 pr-5">
                Rank
              </th>

              <th class="pb-4 pr-5">
                Position
              </th>

              <th class="pb-4 pr-5">
                Shift
              </th>

              <th class="pb-4 pr-5">
                Assignment
              </th>

              <th class="pb-4 pr-5">
                Duty Status
              </th>

              <th class="pb-4 text-right">
                Actions
              </th>

            </tr>

          </thead>


          <tbody
            class="divide-y divide-slate-100"
          >

            <tr
              v-for="person in filteredPersonnel"
              :key="person.id"
              class="hover:bg-slate-50 transition"
            >

              <!-- PERSONNEL -->

              <td class="py-5 pr-5">

                <div
                  class="flex items-center gap-3"
                >

                  <div
                    class="h-11 w-11 flex-shrink-0 rounded-full bg-[#8B1E23] text-white flex items-center justify-center text-xs font-bold"
                  >
                    {{ initials(person) }}
                  </div>

                  <div>

                    <p
                      class="font-bold text-slate-900"
                    >
                      {{ fullName(person) }}
                    </p>

                  </div>

                </div>

              </td>


              <!-- RANK -->

              <td class="py-5 pr-5">

                <span
                  class="font-semibold text-slate-700"
                >
                  {{ person.rank }}
                </span>

              </td>


              <!-- POSITION -->

              <td
                class="py-5 pr-5 text-sm text-slate-600"
              >
                {{ person.position }}
              </td>


              <!-- SHIFT -->

              <td class="py-5 pr-5">

                <span
                  class="text-sm text-slate-600"
                >
                  {{ person.shift }}
                </span>

              </td>


              <!-- ASSIGNMENT -->

              <td class="py-5 pr-5">

                <p
                  class="text-sm text-slate-700 max-w-[220px]"
                >
                  {{
                    person.assignment ||
                    'No assignment'
                  }}
                </p>

              </td>


              <!-- STATUS -->

              <td class="py-5 pr-5">

                <span
                  class="inline-flex px-3 py-1.5 rounded-full border text-xs font-bold"
                  :class="getStatusClass(person.status)"
                >
                  {{ person.status }}
                </span>

              </td>


              <!-- ACTIONS -->

              <td class="py-5">

                <div
                  class="flex justify-end gap-2 flex-wrap"
                >

                  <button
                    @click="viewPersonnel(person)"
                    class="px-3 py-2 rounded-lg border border-slate-200 text-slate-600 text-xs font-bold hover:bg-slate-100"
                  >
                    View
                  </button>


                  <!-- IMPORTANT:
                       THIS ASSIGNS A TASK -->
                  <button
                    @click="openTaskModal(person)"
                    class="px-3 py-2 rounded-lg bg-[#8B1E23] text-white text-xs font-bold hover:bg-[#72181D]"
                  >
                    Assign Task
                  </button>


                  <button
                    @click="openAssignment(person)"
                    class="px-3 py-2 rounded-lg bg-slate-900 text-white text-xs font-bold hover:bg-slate-700"
                  >
                    Assignment
                  </button>


                  <button
                    @click="openDeletePersonnel(person)"
                    class="px-3 py-2 rounded-lg text-red-700 bg-red-50 text-xs font-bold hover:bg-red-100"
                  >
                    Delete
                  </button>

                </div>

              </td>

            </tr>

          </tbody>

        </table>

      </div>


      <!-- EMPTY -->

      <div
        v-else
        class="py-16 text-center"
      >

        <div class="text-4xl mb-3">
          👥
        </div>

        <h3
          class="font-bold text-slate-900"
        >
          No personnel found
        </h3>

        <p
          class="text-sm text-slate-500 mt-1"
        >
          Try changing your search or filters.
        </p>

        <button
          @click="clearFilters"
          class="mt-4 px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white text-sm font-bold"
        >
          Clear Filters
        </button>

      </div>

    </section>


    <!-- =====================================================
         ASSIGNED TASKS
    ====================================================== -->

    <section class="fn-operations-panel">

      <div class="fn-operations-heading">

        <div>

          <h2
            class="text-base font-bold text-slate-900"
          >
            Assigned Tasks
          </h2>

          <p
            class="text-sm text-slate-500 mt-1"
          >
            Tasks assigned by the administrator
          </p>

        </div>

        <span
          class="text-xs font-semibold text-slate-600"
        >
          {{ assignedTasks.length }} {{ assignedTasks.length === 1 ? 'task' : 'tasks' }}
        </span>

      </div>


      <div v-if="assignedTasks.length" class="fn-operations-table-wrap">
        <table class="fn-operations-table">
          <thead>
            <tr><th>Task</th><th>Assigned To</th><th>Deadline</th><th>Priority</th><th>Status</th><th class="text-right">Actions</th></tr>
          </thead>
          <tbody>
            <tr v-for="task in assignedTasks" :key="task.id">
              <td data-label="Task" class="min-w-0">
                <div class="flex min-w-0 flex-col gap-1">
                  <span class="break-words text-sm font-semibold leading-5 text-slate-900">{{ task.title }}</span>
                  <span v-if="task.subtopic" class="break-words text-xs leading-5 text-slate-500">{{ task.subtopic }}</span>
                  <span v-if="task.description" class="break-words whitespace-pre-wrap text-xs leading-5 text-slate-500">{{ task.description }}</span>
                  <span v-if="task.location" class="break-words text-xs leading-5 text-slate-500">{{ task.location }}</span>
                  <span v-if="task.accomplishment || task.submissionNote" class="break-words whitespace-pre-wrap pt-1 text-xs leading-5 text-slate-600">Submission: {{ task.accomplishment || task.submissionNote }}</span>
                  <span v-if="task.submittedAt" class="flex flex-col gap-0.5 pt-1 text-xs leading-5 text-slate-500"><span>Submitted</span><span>{{ formatOperationDate(task.submittedAt) }}</span><span v-if="hasTimeValue(task.submittedAt)">{{ formatOperationTime(task.submittedAt) }}</span></span>
                </div>
              </td>
              <td data-label="Assigned To"><span class="block min-w-0 break-words leading-5">{{ assignedPersonnelName(task) }}</span></td>
              <td data-label="Schedule"><div class="flex flex-col gap-0.5"><span class="leading-5">{{ formatOperationDate(task.dueDate) }}</span><span class="text-xs leading-5 text-slate-500">{{ formatOperationTime(task.time) }}</span></div></td>
              <td data-label="Priority"><span class="fn-operations-badge">{{ (task.priority || 'Medium').toUpperCase() }}</span></td>
              <td data-label="Status"><span class="fn-operations-badge" :class="getTaskStatusClass(task.status)">{{ task.status }}</span></td>
              <td data-label="Actions">
                <div class="flex flex-wrap gap-1.5 sm:justify-end">
                  <button @click="openEditTask(task)" class="fn-operations-action">Edit</button>
                  <button v-if="task.status === 'For Verification' || task.status === 'Submitted'" @click="openTaskSubmission(task)" class="fn-operations-action">View Submission</button>
                  <button @click="deleteTask(task)" class="fn-operations-action fn-operations-action--danger">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>


      <div
        v-else
        class="py-12 text-center"
      >

        <div class="text-4xl mb-3">
          📋
        </div>

        <p
          class="font-bold text-slate-700"
        >
          No tasks assigned yet
        </p>

        <p
          class="text-sm text-slate-500 mt-1"
        >
          Click "Assign Task" beside a personnel.
        </p>

      </div>

    </section>


    <!-- =====================================================
         TEAM AVAILABILITY
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div
        class="border-b border-slate-200 pb-5"
      >

        <h2
          class="text-xl font-bold text-slate-900"
        >
          Team Availability
        </h2>

        <p
          class="text-sm text-slate-500 mt-1"
        >
          Current staffing by shift
        </p>

      </div>


      <div class="mt-5 space-y-4">

        <div
          v-for="item in shiftSummary"
          :key="item.shift"
          class="p-4 rounded-xl border border-slate-200 bg-slate-50"
        >

          <div
            class="flex justify-between items-center gap-4"
          >

            <div>

              <p
                class="text-sm font-bold text-slate-900"
              >
                {{ item.shift }} Shift
              </p>

              <p
                class="text-xs text-slate-500 mt-1"
              >
                {{ item.onDuty }}
                of
                {{ item.total }}
                personnel on duty
              </p>

            </div>


            <span
              class="text-sm font-bold"
              :class="{
                'text-green-600':
                  item.status === 'Fully Staffed',

                'text-blue-600':
                  item.status === 'On Schedule',

                'text-yellow-600':
                  item.status === 'Low Coverage'
              }"
            >
              {{ item.status }}
            </span>

          </div>


          <div
            class="mt-3 h-2 rounded-full bg-slate-200 overflow-hidden"
          >

            <div
              class="h-full rounded-full bg-[#8B1E23] transition-all duration-500"
              :style="{
                width: `${item.coverage}%`
              }"
            ></div>

          </div>


          <div
            class="flex justify-between mt-2 text-xs text-slate-500"
          >

            <span>
              Coverage
            </span>

            <span
              class="font-bold text-slate-700"
            >
              {{ item.coverage }}%
            </span>

          </div>

        </div>

      </div>

    </section>


    <!-- =====================================================
         PERSONNEL NOTES
    ====================================================== -->

    <section
      class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div
        class="border-b border-slate-200 pb-5"
      >

        <h2
          class="text-xl font-bold text-slate-900"
        >
          Personnel Notes
        </h2>

        <p
          class="text-sm text-slate-500 mt-1"
        >
          Admin reminders and coordination updates
        </p>

      </div>


      <div
        class="mt-5 grid grid-cols-1 md:grid-cols-3 gap-4"
      >

        <div
          class="p-4 rounded-xl border border-emerald-200 bg-emerald-50"
        >

          <p
            class="text-sm font-bold text-slate-900"
          >
            Training Readiness
          </p>

          <p
            class="text-sm text-slate-600 mt-1"
          >
            All new trainees have completed orientation and are scheduled for field drills next week.
          </p>

        </div>


        <div
          class="p-4 rounded-xl border border-orange-200 bg-orange-50"
        >

          <p
            class="text-sm font-bold text-slate-900"
          >
            Coverage Alert
          </p>

          <p
            class="text-sm text-slate-600 mt-1"
          >
            Night shift should be reviewed regularly to maintain emergency response coverage.
          </p>

        </div>


        <div
          class="p-4 rounded-xl border border-indigo-200 bg-indigo-50"
        >

          <p
            class="text-sm font-bold text-slate-900"
          >
            Leave Management
          </p>

          <p
            class="text-sm text-slate-600 mt-1"
          >
            Review approved leave requests and ensure backup personnel are assigned.
          </p>

        </div>

      </div>

    </section>


    <!-- =====================================================
         DETAILS MODAL
    ====================================================== -->

    <div
      v-if="showDetailsModal && selectedPersonnel"
      class="fixed inset-0 z-50 bg-slate-900/50 backdrop-blur-sm flex items-center justify-center p-4"
    >

      <div
        class="w-full max-w-xl bg-white rounded-2xl shadow-2xl overflow-hidden"
      >

        <!-- HEADER -->

        <div
          class="bg-[#8B1E23] p-6 text-white"
        >

          <div
            class="flex items-center gap-4"
          >

            <div
              class="h-16 w-16 rounded-full bg-white/20 flex items-center justify-center text-lg font-bold"
            >
              {{ initials(selectedPersonnel) }}
            </div>


            <div>

              <p
                class="text-2xl font-bold"
              >
                {{ fullName(selectedPersonnel) }}
              </p>

              <p
                class="text-white/80"
              >
                {{ selectedPersonnel.rank }}
                •
                {{ selectedPersonnel.position }}
              </p>

            </div>

          </div>

        </div>


        <!-- CONTENT -->

        <div class="p-6 space-y-4">

          <div
            class="grid grid-cols-2 gap-4"
          >

            <div
              class="p-4 rounded-xl bg-slate-50"
            >

            </div>


            <div
              class="p-4 rounded-xl bg-slate-50"
            >

              <p
                class="text-xs text-slate-400 uppercase font-bold"
              >
                Duty Status
              </p>

              <span
                class="inline-flex mt-1 px-2.5 py-1 rounded-full border text-xs font-bold"
                :class="getStatusClass(selectedPersonnel.status)"
              >
                {{ selectedPersonnel.status }}
              </span>

            </div>

          </div>


          <div>

            <p
              class="text-xs text-slate-400 uppercase font-bold"
            >
              Shift
            </p>

            <p
              class="text-slate-700 mt-1"
            >
              {{ selectedPersonnel.shift }}
            </p>

          </div>


          <div>

            <p
              class="text-xs text-slate-400 uppercase font-bold"
            >
              Assignment
            </p>

            <p
              class="text-slate-700 mt-1"
            >
              {{
                selectedPersonnel.assignment ||
                'No assignment'
              }}
            </p>

          </div>


          <div>

            <p
              class="text-xs text-slate-400 uppercase font-bold"
            >
              Contact
            </p>

            <p
              class="text-slate-700 mt-1"
            >
              {{
                selectedPersonnel.contact ||
                'Not provided'
              }}
            </p>

          </div>


          <div>

            <p
              class="text-xs text-slate-400 uppercase font-bold"
            >
              Email
            </p>

            <p
              class="text-slate-700 mt-1"
            >
              {{
                selectedPersonnel.email ||
                'Not provided'
              }}
            </p>

          </div>

        </div>


        <!-- FOOTER -->

        <div
          class="px-6 py-5 border-t border-slate-200 flex flex-wrap justify-end gap-3"
        >

          <button
            @click="openTaskModal(selectedPersonnel)"
            class="px-4 py-2.5 rounded-xl bg-[#8B1E23] text-white font-bold"
          >
            Assign Task
          </button>


          <button
            @click="openAssignment(selectedPersonnel)"
            class="px-4 py-2.5 rounded-xl border border-slate-300 text-slate-700 font-semibold"
          >
            Assignment
          </button>


          <button
            @click="openEditPersonnel(selectedPersonnel)"
            class="px-4 py-2.5 rounded-xl bg-slate-900 text-white font-bold"
          >
            Edit
          </button>


          <button
            @click="openDeletePersonnel(selectedPersonnel)"
            class="px-4 py-2.5 rounded-xl bg-red-50 text-red-700 font-semibold"
          >
            Delete
          </button>


          <button
            @click="showDetailsModal = false"
            class="px-4 py-2.5 rounded-xl border border-slate-300 text-slate-600 font-semibold"
          >
            Close
          </button>

        </div>

      </div>

    </div>


    <!-- =====================================================
         ASSIGN TASK MODAL
    ====================================================== -->

    <div
      v-if="showTaskModal && selectedPersonnel"
      class="fixed inset-0 z-[55] bg-slate-900/60 backdrop-blur-sm flex items-center justify-center p-4"
    >

      <div
        class="fn-modal-panel w-full max-w-2xl bg-white rounded-2xl shadow-2xl overflow-hidden"
      >

        <!-- HEADER -->

        <div
          class="bg-[#8B1E23] p-6 text-white"
        >

          <div
            class="flex items-start justify-between gap-4"
          >

            <div>

              <p
                class="text-xs uppercase tracking-wider font-bold text-white/70"
              >
                Personnel Task Assignment
              </p>

              <h2
                class="text-2xl font-bold mt-1"
              >
                {{ editingTask ? 'Edit Task' : 'Assign Task' }}
              </h2>

              <p
                class="text-sm text-white/80 mt-1"
              >
                Assigned to
                {{ fullName(selectedPersonnel) }}
              </p>

            </div>


            <button
              @click="showTaskModal = false"
              class="h-9 w-9 rounded-lg bg-white/10 hover:bg-white/20 text-white"
            >
              ✕
            </button>

          </div>

        </div>


        <!-- FORM -->

        <div
          class="p-6 space-y-5 max-h-[70vh] overflow-y-auto"
        >

          <!-- TITLE -->

          <div>

            <label
              class="block text-sm font-bold text-slate-700 mb-2"
            >
              Task Title *
            </label>

            <input
              v-model="taskForm.title"
              type="text"
              placeholder="Example: Conduct Fire Safety Inspection"
              class="w-full h-12 px-4 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]"
            />

          </div>


          <!-- SUBTOPIC -->

          <div>

            <label
              class="block text-sm font-bold text-slate-700 mb-2"
            >
              Sub-topic
            </label>

            <input
              v-model="taskForm.subtopic"
              type="text"
              placeholder="Example: Building Inspection"
              class="w-full h-12 px-4 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]"
            />

          </div>


          <!-- TYPE + PRIORITY -->

          <div
            class="grid grid-cols-1 md:grid-cols-2 gap-4"
          >

            <div>

              <label
                class="block text-sm font-bold text-slate-700 mb-2"
              >
                Task Type
              </label>

              <select
                v-model="taskForm.type"
                class="w-full h-12 px-4 rounded-xl border border-slate-300 bg-white"
              >

                <option>
                  General Task
                </option>

                <option>
                  Inspection
                </option>

                <option>
                  Report
                </option>

                <option>
                  Training
                </option>

                <option>
                  Documentation
                </option>

                <option>
                  Emergency Duty
                </option>

                <option>
                  Compliance
                </option>

              </select>

            </div>


            <div>

              <label
                class="block text-sm font-bold text-slate-700 mb-2"
              >
                Priority
              </label>

              <select
                v-model="taskForm.priority"
                class="w-full h-12 px-4 rounded-xl border border-slate-300 bg-white"
              >

                <option>
                  High
                </option>

                <option>
                  Medium
                </option>

                <option>
                  Low
                </option>

              </select>

            </div>

          </div>


          <!-- LOCATION -->

          <div>

            <label
              class="block text-sm font-bold text-slate-700 mb-2"
            >
              Task Location
            </label>

            <input
              v-model="taskForm.location"
              type="text"
              placeholder="Example: Public Market"
              class="w-full h-12 px-4 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]"
            />

          </div>


          <!-- DATE + TIME -->

          <div
            class="grid grid-cols-1 md:grid-cols-2 gap-4"
          >

            <div>

              <label
                class="block text-sm font-bold text-slate-700 mb-2"
              >
                Due Date *
              </label>

              <input
                v-model="taskForm.dueDate"
                type="date"
                class="w-full h-12 px-4 rounded-xl border border-slate-300"
              />

            </div>


            <div>

              <label
                class="block text-sm font-bold text-slate-700 mb-2"
              >
                Time
              </label>

              <input
                v-model="taskForm.time"
                type="time"
                class="w-full h-12 px-4 rounded-xl border border-slate-300"
              />

            </div>

          </div>


          <!-- DESCRIPTION -->

          <div>

            <label
              class="block text-sm font-bold text-slate-700 mb-2"
            >
              Instructions / Description
            </label>

            <textarea
              v-model="taskForm.description"
              rows="5"
              placeholder="Write instructions for the personnel..."
              class="w-full px-4 py-3 rounded-xl border border-slate-300 resize-none focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]"
            ></textarea>

          </div>

        </div>


        <!-- FOOTER -->

        <div
          class="px-6 py-5 bg-slate-50 border-t border-slate-200 flex justify-end gap-3"
        >

          <button
            @click="showTaskModal = false"
            class="px-5 py-2.5 rounded-xl border border-slate-300 text-slate-700 font-semibold"
          >
            Cancel
          </button>


          <button
            @click="saveTask"
            class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D]"
          >
            {{ editingTask ? 'Save Changes' : 'Assign Task' }}
          </button>

        </div>

      </div>

    </div>


    <!-- =====================================================
         OLD PERSONNEL ASSIGNMENT MODAL
    ====================================================== -->

    <div
      v-if="showAssignmentModal && selectedPersonnel"
      class="fixed inset-0 z-50 bg-slate-900/50 backdrop-blur-sm flex items-center justify-center p-4"
    >

      <div
        class="w-full max-w-lg bg-white rounded-2xl shadow-2xl overflow-hidden"
      >

        <div
          class="p-6 border-b border-slate-200"
        >

          <h3
            class="text-xl font-bold text-slate-900"
          >
            Update Assignment
          </h3>

          <p
            class="text-sm text-slate-500 mt-1"
          >
            {{ fullName(selectedPersonnel) }}
          </p>

        </div>


        <div class="p-6">

          <label
            class="text-sm font-bold text-slate-700"
          >
            Personnel Assignment
          </label>

          <input
            v-model="assignmentInput"
            type="text"
            placeholder="Enter personnel assignment"
            class="mt-2 w-full h-12 px-4 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-red-200"
          />

        </div>


        <div
          class="px-6 py-5 bg-slate-50 border-t border-slate-200 flex justify-end gap-3"
        >

          <button
            @click="showAssignmentModal = false"
            class="px-5 py-2.5 rounded-xl border border-slate-300 font-semibold"
          >
            Cancel
          </button>


          <button
            @click="saveAssignment"
            class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white font-bold"
          >
            Save Assignment
          </button>

        </div>

      </div>

    </div>


    <!-- =====================================================
         DELETE MODAL
    ====================================================== -->

    <div
      v-if="showDeleteModal && personnelToDelete"
      class="fixed inset-0 z-[60] bg-slate-900/50 backdrop-blur-sm flex items-center justify-center p-4"
    >

      <div
        class="w-full max-w-md bg-white rounded-2xl shadow-2xl p-6"
      >

        <div
          class="h-12 w-12 rounded-full bg-red-50 text-red-600 flex items-center justify-center text-xl font-bold"
        >
          !
        </div>


        <h3
          class="text-xl font-bold text-slate-900 mt-4"
        >
          Remove Personnel?
        </h3>


        <p
          class="text-sm text-slate-500 mt-2"
        >

          Are you sure you want to remove

          <span
            class="font-bold text-slate-700"
          >
            {{ fullName(personnelToDelete) }}
          </span>

          from the station roster?

        </p>


        <div
          class="flex justify-end gap-3 mt-6"
        >

          <button
            @click="cancelDelete"
            class="px-5 py-2.5 rounded-xl border border-slate-300 font-semibold text-slate-600"
          >
            Cancel
          </button>


          <button
            @click="deletePersonnel"
            class="px-5 py-2.5 rounded-xl bg-red-600 text-white font-bold"
          >
            Remove
          </button>

        </div>

      </div>

    </div>


    <div
      v-if="showSubmissionModal && selectedTaskSubmission"
      class="fixed inset-0 z-[65] bg-slate-900/50 flex items-center justify-center p-4"
      @click.self="showSubmissionModal = false"
    >
      <div class="fn-modal-panel w-full max-w-2xl bg-white rounded-2xl shadow-2xl overflow-hidden">
        <div class="p-6 border-b border-slate-200">
          <p class="text-xs font-bold uppercase tracking-wide text-[#8B1E23]">Task Submission</p>
          <h3 class="text-xl font-bold text-slate-900 mt-1">{{ selectedTaskSubmission.title }}</h3>
          <p class="text-sm text-slate-500 mt-1">{{ assignedPersonnelName(selectedTaskSubmission) }}</p>
        </div>

        <div class="p-6 space-y-5">
          <div class="flex items-center justify-between gap-3">
            <span class="px-3 py-1.5 rounded-full text-xs font-bold" :class="getTaskStatusClass(selectedTaskSubmission.status)">{{ selectedTaskSubmission.status }}</span>
            <span class="flex flex-col gap-0.5 text-right text-xs leading-5 text-slate-500">
              <span>{{ selectedTaskSubmission.submittedAt ? formatOperationDate(selectedTaskSubmission.submittedAt) : 'Not submitted' }}</span>
              <span v-if="hasTimeValue(selectedTaskSubmission.submittedAt)">{{ formatOperationTime(selectedTaskSubmission.submittedAt) }}</span>
            </span>
          </div>

          <div>
            <p class="text-xs font-bold uppercase tracking-wide text-slate-500">Accomplishment / Work Summary</p>
            <p class="mt-2 rounded-xl border border-slate-200 bg-slate-50 p-4 text-sm text-slate-700 whitespace-pre-line">{{ selectedTaskSubmission.accomplishment || selectedTaskSubmission.submissionNote || 'No accomplishment provided.' }}</p>
          </div>

          <div v-if="selectedTaskSubmission.submissionRemarks">
            <p class="text-xs font-bold uppercase tracking-wide text-slate-500">Remarks</p>
            <p class="mt-2 text-sm text-slate-700 whitespace-pre-line">{{ selectedTaskSubmission.submissionRemarks }}</p>
          </div>

          <div v-if="submissionEvidence.length">
            <p class="text-xs font-bold uppercase tracking-wide text-slate-500 mb-2">Evidence</p>
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-3">
              <button v-for="(item, index) in submissionEvidence" :key="item.id" type="button" class="rounded-xl border border-slate-200 p-2 text-left" @click="openEvidence(item)">
                <img :src="submissionEvidenceUrls[index]" :alt="item.filename" class="h-24 w-full rounded-lg object-cover" />
                <span class="block truncate text-xs font-semibold text-slate-700">{{ item.filename }}</span>
              </button>
            </div>
          </div>

          <textarea v-if="selectedTaskSubmission.status === 'For Verification' || selectedTaskSubmission.status === 'Submitted'" v-model="returnNote" rows="3" placeholder="Revision note when returning the submission..." class="fn-form-control resize-none"></textarea>
        </div>

        <div class="p-6 border-t border-slate-200 flex flex-wrap justify-end gap-3">
          <button type="button" @click="showSubmissionModal = false" class="px-5 py-2.5 rounded-xl border border-slate-300 text-slate-700 font-semibold">Close</button>
          <button v-if="selectedTaskSubmission.status === 'For Verification' || selectedTaskSubmission.status === 'Submitted'" type="button" @click="returnTaskForRevision(selectedTaskSubmission)" class="px-5 py-2.5 rounded-xl bg-yellow-600 text-white font-bold">Return for Revision</button>
          <button v-if="selectedTaskSubmission.status === 'For Verification' || selectedTaskSubmission.status === 'Submitted'" type="button" @click="verifyTask(selectedTaskSubmission)" class="px-5 py-2.5 rounded-xl bg-green-600 text-white font-bold">Verify</button>
        </div>
      </div>
    </div>

    <!-- =====================================================
         TOAST
    ====================================================== -->

    <Transition
      enter-active-class="transition duration-200"
      enter-from-class="opacity-0 translate-y-2"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition duration-200"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >

      <div
        v-if="toastMessage"
        class="fixed bottom-6 right-6 z-[70] max-w-sm px-5 py-4 rounded-xl shadow-xl text-sm font-semibold"
        :class="
          toastType === 'error'
            ? 'bg-red-600 text-white'
            : 'bg-slate-900 text-white'
        "
      >
        {{ toastMessage }}
      </div>

    </Transition>

  </div>

</template>