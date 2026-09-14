<script setup>
import { computed, ref } from 'vue'

const props = defineProps({
  currentUser: {
    type: Object,
    default: null
  }
})

const searchQuery = ref('')
const selectedStatus = ref('All Duty Status')
const selectedRank = ref('All Ranks')

const showPersonnelModal = ref(false)
const showDetailsModal = ref(false)
const showDeleteModal = ref(false)
const showAssignmentModal = ref(false)

const editingPersonnel = ref(null)
const selectedPersonnel = ref(null)
const personnelToDelete = ref(null)

const toastMessage = ref('')
const toastType = ref('success')

const personnelForm = ref({
  id: '',
  firstName: '',
  lastName: '',
  rank: 'FO1',
  position: 'Fire Officer',
  shift: 'Morning',
  status: 'On Duty',
  contact: '',
  email: '',
  assignment: ''
})

const personnel = ref([
  {
    id: 'BFP-001',
    firstName: 'Juan',
    lastName: 'Dela Cruz',
    rank: 'FO3',
    position: 'Fire Officer',
    shift: 'Morning',
    status: 'On Duty',
    contact: '0917-123-4567',
    email: 'juan.delacruz@bfp.gov.ph',
    assignment: 'Fire Safety Inspection Team'
  },
  {
    id: 'BFP-002',
    firstName: 'Maria',
    lastName: 'Santos',
    rank: 'SFO1',
    position: 'Senior Fire Officer',
    shift: 'Afternoon',
    status: 'On Duty',
    contact: '0918-234-5678',
    email: 'maria.santos@bfp.gov.ph',
    assignment: 'Community Drill Operations'
  },
  {
    id: 'BFP-003',
    firstName: 'Roberto',
    lastName: 'Reyes',
    rank: 'FO2',
    position: 'Fire Officer',
    shift: 'Night',
    status: 'On Leave',
    contact: '0919-345-6789',
    email: 'roberto.reyes@bfp.gov.ph',
    assignment: 'Dispatch Support'
  },
  {
    id: 'BFP-004',
    firstName: 'Carlo',
    lastName: 'Garcia',
    rank: 'FO1',
    position: 'Fire Officer',
    shift: 'Morning',
    status: 'On Duty',
    contact: '0920-456-7890',
    email: 'carlo.garcia@bfp.gov.ph',
    assignment: 'Station Equipment Team'
  },
  {
    id: 'BFP-005',
    firstName: 'Ana',
    lastName: 'Villanueva',
    rank: 'FO2',
    position: 'Fire Officer',
    shift: 'Afternoon',
    status: 'Off Duty',
    contact: '0921-567-8901',
    email: 'ana.villanueva@bfp.gov.ph',
    assignment: 'Training Coordination'
  },
  {
    id: 'BFP-006',
    firstName: 'Mark',
    lastName: 'Santos',
    rank: 'FO2',
    position: 'Fire Officer',
    shift: 'Morning',
    status: 'On Duty',
    contact: '0922-678-9012',
    email: 'mark.santos@bfp.gov.ph',
    assignment: 'Emergency Response Team'
  }
])

const assignments = ref([
  {
    personnel: 'Juan Dela Cruz',
    description: 'Assigned to Fire Safety Inspection Team',
    status: 'Assigned'
  },
  {
    personnel: 'Roberto Reyes',
    description: 'Transferred to Night Shift Dispatch Support',
    status: 'Updated'
  },
  {
    personnel: 'Maria Santos',
    description: 'Promoted as Operations Lead for community drills',
    status: 'Promotion'
  }
])

const ranks = computed(() => {
  return [...new Set(personnel.value.map(person => person.rank))]
})

const filteredPersonnel = computed(() => {
  const query = searchQuery.value.toLowerCase().trim()

  return personnel.value.filter(person => {
    const fullName = `${person.firstName} ${person.lastName}`.toLowerCase()

    const searchText = [
      fullName,
      person.id,
      person.rank,
      person.position,
      person.shift,
      person.assignment
    ]
      .filter(Boolean)
      .join(' ')
      .toLowerCase()

    const matchesSearch =
      !query || searchText.includes(query)

    const matchesStatus =
      selectedStatus.value === 'All Duty Status' ||
      person.status === selectedStatus.value

    const matchesRank =
      selectedRank.value === 'All Ranks' ||
      person.rank === selectedRank.value

    return matchesSearch && matchesStatus && matchesRank
  })
})

const totalPersonnel = computed(() => personnel.value.length)

const onDutyCount = computed(() =>
  personnel.value.filter(person => person.status === 'On Duty').length
)

const leaveCount = computed(() =>
  personnel.value.filter(person => person.status === 'On Leave').length
)

const offDutyCount = computed(() =>
  personnel.value.filter(person => person.status === 'Off Duty').length
)

const onDutyPercentage = computed(() => {
  if (!totalPersonnel.value) return 0
  return Math.round((onDutyCount.value / totalPersonnel.value) * 100)
})

const shiftSummary = computed(() => {
  const shifts = ['Morning', 'Afternoon', 'Night']

  return shifts.map(shift => {
    const members = personnel.value.filter(
      person => person.shift === shift
    )

    const onDuty = members.filter(
      person => person.status === 'On Duty'
    ).length

    const coverage =
      members.length > 0
        ? Math.round((onDuty / members.length) * 100)
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

const hasFilters = computed(() => {
  return (
    searchQuery.value ||
    selectedStatus.value !== 'All Duty Status' ||
    selectedRank.value !== 'All Ranks'
  )
})

const fullName = person =>
  `${person.firstName} ${person.lastName}`

const initials = person => {
  return `${person.firstName?.charAt(0) || ''}${person.lastName?.charAt(0) || ''}`
}

const showToast = (message, type = 'success') => {
  toastMessage.value = message
  toastType.value = type

  setTimeout(() => {
    toastMessage.value = ''
  }, 3000)
}

const clearFilters = () => {
  searchQuery.value = ''
  selectedStatus.value = 'All Duty Status'
  selectedRank.value = 'All Ranks'
}

const openAddPersonnel = () => {
  editingPersonnel.value = null

  personnelForm.value = {
    id: '',
    firstName: '',
    lastName: '',
    rank: 'FO1',
    position: 'Fire Officer',
    shift: 'Morning',
    status: 'On Duty',
    contact: '',
    email: '',
    assignment: ''
  }

  showPersonnelModal.value = true
}

const openEditPersonnel = person => {
  editingPersonnel.value = person

  personnelForm.value = {
    id: person.id,
    firstName: person.firstName,
    lastName: person.lastName,
    rank: person.rank,
    position: person.position,
    shift: person.shift,
    status: person.status,
    contact: person.contact || '',
    email: person.email || '',
    assignment: person.assignment || ''
  }

  showPersonnelModal.value = true
}

const savePersonnel = () => {
  if (
    !personnelForm.value.firstName.trim() ||
    !personnelForm.value.lastName.trim() ||
    !personnelForm.value.rank ||
    !personnelForm.value.position
  ) {
    showToast('Please complete all required fields.', 'error')
    return
  }

  if (editingPersonnel.value) {
    Object.assign(
      editingPersonnel.value,
      personnelForm.value
    )

    showToast('Personnel record updated successfully.')
  } else {
    const newId = `BFP-${String(personnel.value.length + 1).padStart(3, '0')}`

    personnel.value.unshift({
      ...personnelForm.value,
      id: newId
    })

    showToast('New personnel added successfully.')
  }

  showPersonnelModal.value = false
}

const viewPersonnel = person => {
  selectedPersonnel.value = person
  showDetailsModal.value = true
}

const openDeletePersonnel = person => {
  personnelToDelete.value = person
  showDeleteModal.value = true
}

const deletePersonnel = () => {
  if (!personnelToDelete.value) return

  personnel.value = personnel.value.filter(
    person => person.id !== personnelToDelete.value.id
  )

  showDeleteModal.value = false

  showToast(
    `${fullName(personnelToDelete.value)} was removed from the roster.`
  )

  personnelToDelete.value = null
}

const openAssignment = person => {
  selectedPersonnel.value = person

  personnelForm.value.assignment =
    person.assignment || ''

  showAssignmentModal.value = true
}

const saveAssignment = () => {
  if (!selectedPersonnel.value) return

  selectedPersonnel.value.assignment =
    personnelForm.value.assignment.trim()

  assignments.value.unshift({
    personnel: fullName(selectedPersonnel.value),
    description: selectedPersonnel.value.assignment
      ? `Assignment updated to ${selectedPersonnel.value.assignment}`
      : 'Personnel assignment cleared',
    status: 'Updated'
  })

  showAssignmentModal.value = false

  showToast('Personnel assignment updated successfully.')
}

const updateStatus = (person, status) => {
  person.status = status

  showToast(
    `${fullName(person)} status changed to ${status}.`
  )
}

const getStatusClass = status => {
  const classes = {
    'On Duty': 'bg-green-50 text-green-700 border-green-200',
    'On Leave': 'bg-yellow-50 text-yellow-700 border-yellow-200',
    'Off Duty': 'bg-slate-100 text-slate-600 border-slate-200'
  }

  return classes[status] || classes['Off Duty']
}

const getAssignmentClass = status => {
  const classes = {
    Assigned: 'bg-blue-50 text-blue-700',
    Updated: 'bg-green-50 text-green-700',
    Promotion: 'bg-yellow-50 text-yellow-700'
  }

  return classes[status] || 'bg-slate-100 text-slate-600'
}
</script>

<template>
  <div class="space-y-6">

    <!-- HEADER -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

        <div>
          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">
            Personnel Management
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Station Personnel
          </h2>

          <p class="text-base text-slate-500 mt-1">
            Manage personnel records, ranks, assignments, and duty status.
          </p>
        </div>

        <button
          @click="openAddPersonnel"
          class="px-6 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D] transition shadow-sm"
        >
          + Add Personnel
        </button>

      </div>
    </section>

    <!-- STATISTICS -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-slate-900">
          {{ totalPersonnel }}
        </p>
        <p class="text-sm text-slate-500 mt-1">
          Total Personnel
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">
          {{ onDutyCount }}
        </p>
        <p class="text-sm text-slate-500 mt-1">
          On Duty
        </p>
        <p class="text-xs text-green-600 font-semibold mt-2">
          {{ onDutyPercentage }}% staffing availability
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">
          {{ String(leaveCount).padStart(2, '0') }}
        </p>
        <p class="text-sm text-slate-500 mt-1">
          On Leave
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-slate-500">
          {{ String(offDutyCount).padStart(2, '0') }}
        </p>
        <p class="text-sm text-slate-500 mt-1">
          Off Duty
        </p>
      </div>

    </section>

    <!-- FILTERS -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

      <div class="flex flex-col lg:flex-row gap-4">

        <div class="relative flex-1">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search name, ID, rank, position, or assignment..."
            class="w-full h-12 px-4 rounded-xl border border-slate-300 text-base focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]"
          />
        </div>

        <select
          v-model="selectedRank"
          class="h-12 px-4 rounded-xl border border-slate-300 text-base bg-white focus:outline-none focus:ring-2 focus:ring-red-200"
        >
          <option>All Ranks</option>
          <option
            v-for="rank in ranks"
            :key="rank"
          >
            {{ rank }}
          </option>
        </select>

        <select
          v-model="selectedStatus"
          class="h-12 px-4 rounded-xl border border-slate-300 text-base bg-white focus:outline-none focus:ring-2 focus:ring-red-200"
        >
          <option>All Duty Status</option>
          <option>On Duty</option>
          <option>Off Duty</option>
          <option>On Leave</option>
        </select>

        <button
          v-if="hasFilters"
          @click="clearFilters"
          class="h-12 px-5 rounded-xl border border-slate-300 text-slate-600 font-semibold hover:bg-slate-50 transition"
        >
          Clear
        </button>

      </div>

      <div class="mt-4 flex items-center justify-between">
        <p class="text-sm text-slate-500">
          Showing
          <span class="font-bold text-slate-800">
            {{ filteredPersonnel.length }}
          </span>
          of
          <span class="font-bold text-slate-800">
            {{ totalPersonnel }}
          </span>
          personnel
        </p>
      </div>

    </section>

    <!-- PERSONNEL TABLE -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex items-center justify-between mb-5">
        <div>
          <h2 class="text-xl font-bold text-slate-900">
            Personnel Roster
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Current station personnel records
          </p>
        </div>
      </div>

      <div
        v-if="filteredPersonnel.length"
        class="overflow-x-auto"
      >

        <table class="w-full text-left">

          <thead>
            <tr class="border-b border-slate-200 text-xs font-bold uppercase tracking-wide text-slate-400">
              <th class="pb-4 pr-5">Personnel</th>
              <th class="pb-4 pr-5">Rank</th>
              <th class="pb-4 pr-5">Position</th>
              <th class="pb-4 pr-5">Shift</th>
              <th class="pb-4 pr-5">Assignment</th>
              <th class="pb-4 pr-5">Duty Status</th>
              <th class="pb-4 text-right">Actions</th>
            </tr>
          </thead>

          <tbody class="divide-y divide-slate-100">

            <tr
              v-for="person in filteredPersonnel"
              :key="person.id"
              class="hover:bg-slate-50 transition"
            >

              <td class="py-5 pr-5">
                <div class="flex items-center gap-3">

                  <div
                    class="h-11 w-11 flex-shrink-0 rounded-full bg-[#8B1E23] text-white flex items-center justify-center text-xs font-bold"
                  >
                    {{ initials(person) }}
                  </div>

                  <div>
                    <p class="font-bold text-slate-900">
                      {{ fullName(person) }}
                    </p>

                    <p class="text-xs text-slate-500 mt-1">
                      {{ person.id }}
                    </p>
                  </div>

                </div>
              </td>

              <td class="py-5 pr-5">
                <span class="font-semibold text-slate-700">
                  {{ person.rank }}
                </span>
              </td>

              <td class="py-5 pr-5 text-sm text-slate-600">
                {{ person.position }}
              </td>

              <td class="py-5 pr-5">
                <span class="text-sm text-slate-600">
                  {{ person.shift }}
                </span>
              </td>

              <td class="py-5 pr-5">
                <p class="text-sm text-slate-700 max-w-[220px]">
                  {{ person.assignment || 'No assignment' }}
                </p>
              </td>

              <td class="py-5 pr-5">
                <span
                  class="inline-flex px-3 py-1.5 rounded-full border text-xs font-bold"
                  :class="getStatusClass(person.status)"
                >
                  {{ person.status.toUpperCase() }}
                </span>
              </td>

              <td class="py-5 text-right">

                <div class="flex justify-end gap-2">

                  <button
                    @click="viewPersonnel(person)"
                    class="px-3 py-2 rounded-lg border border-slate-200 text-slate-600 text-xs font-bold hover:bg-slate-100 transition"
                  >
                    View
                  </button>

                  <button
                    @click="openEditPersonnel(person)"
                    class="px-3 py-2 rounded-lg bg-slate-900 text-white text-xs font-bold hover:bg-slate-700 transition"
                  >
                    Edit
                  </button>

                </div>

              </td>

            </tr>

          </tbody>

        </table>

      </div>

      <!-- EMPTY STATE -->
      <div
        v-else
        class="py-16 text-center"
      >
        <div class="text-4xl mb-3">
          👥
        </div>

        <h3 class="font-bold text-slate-900">
          No personnel found
        </h3>

        <p class="text-sm text-slate-500 mt-1">
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

    <!-- ASSIGNMENTS + AVAILABILITY -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- RECENT ASSIGNMENTS -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">

          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Recent Assignments
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              Latest personnel assignments and updates
            </p>
          </div>

        </div>

        <div class="mt-5 space-y-4">

          <div
            v-for="(assignment, index) in assignments.slice(0, 5)"
            :key="index"
            class="p-4 rounded-xl border border-slate-200 bg-slate-50"
          >

            <div class="flex justify-between gap-3">

              <div>
                <p class="font-bold text-slate-900">
                  {{ assignment.personnel }}
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  {{ assignment.description }}
                </p>
              </div>

              <span
                class="h-fit px-2.5 py-1 rounded-full text-xs font-bold"
                :class="getAssignmentClass(assignment.status)"
              >
                {{ assignment.status }}
              </span>

            </div>

          </div>

        </div>

      </div>

      <!-- TEAM AVAILABILITY -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="border-b border-slate-200 pb-5">

          <h2 class="text-xl font-bold text-slate-900">
            Team Availability
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Current staffing by shift
          </p>

        </div>

        <div class="mt-5 space-y-4">

          <div
            v-for="item in shiftSummary"
            :key="item.shift"
            class="p-4 rounded-xl border border-slate-200 bg-slate-50"
          >

            <div class="flex justify-between items-center gap-4">

              <div>
                <p class="text-sm font-bold text-slate-900">
                  {{ item.shift }} Shift
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  {{ item.onDuty }} of {{ item.total }} personnel on duty
                </p>
              </div>

              <span
                class="text-sm font-bold"
                :class="{
                  'text-green-600': item.status === 'Fully Staffed',
                  'text-blue-600': item.status === 'On Schedule',
                  'text-yellow-600': item.status === 'Low Coverage'
                }"
              >
                {{ item.status }}
              </span>

            </div>

            <div class="mt-3 h-2 rounded-full bg-slate-200 overflow-hidden">

              <div
                class="h-full rounded-full bg-[#8B1E23] transition-all duration-500"
                :style="{ width: `${item.coverage}%` }"
              ></div>

            </div>

            <div class="flex justify-between mt-2 text-xs text-slate-500">
              <span>Coverage</span>
              <span class="font-bold text-slate-700">
                {{ item.coverage }}%
              </span>
            </div>

          </div>

        </div>

      </div>

    </section>

    <!-- PERSONNEL NOTES -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="border-b border-slate-200 pb-5">

        <h2 class="text-xl font-bold text-slate-900">
          Personnel Notes
        </h2>

        <p class="text-sm text-slate-500 mt-1">
          Admin reminders and coordination updates
        </p>

      </div>

      <div class="mt-5 grid grid-cols-1 md:grid-cols-3 gap-4">

        <div class="p-4 rounded-xl border border-emerald-200 bg-emerald-50">
          <p class="text-sm font-bold text-slate-900">
            Training Readiness
          </p>

          <p class="text-sm text-slate-600 mt-1">
            All new trainees have completed orientation and are scheduled for field drills next week.
          </p>
        </div>

        <div class="p-4 rounded-xl border border-orange-200 bg-orange-50">
          <p class="text-sm font-bold text-slate-900">
            Coverage Alert
          </p>

          <p class="text-sm text-slate-600 mt-1">
            Night shift should be reviewed regularly to maintain emergency response coverage.
          </p>
        </div>

        <div class="p-4 rounded-xl border border-indigo-200 bg-indigo-50">
          <p class="text-sm font-bold text-slate-900">
            Leave Management
          </p>

          <p class="text-sm text-slate-600 mt-1">
            Review approved leave requests and ensure backup personnel are assigned.
          </p>
        </div>

      </div>

    </section>

    <!-- ADD / EDIT MODAL -->
    <div
      v-if="showPersonnelModal"
      class="fixed inset-0 z-50 bg-slate-900/50 backdrop-blur-sm flex items-center justify-center p-4"
    >

      <div class="w-full max-w-3xl bg-white rounded-2xl shadow-2xl overflow-hidden">

        <div class="px-6 py-5 border-b border-slate-200 flex items-center justify-between">

          <div>
            <h3 class="text-xl font-bold text-slate-900">
              {{ editingPersonnel ? 'Edit Personnel' : 'Add Personnel' }}
            </h3>

            <p class="text-sm text-slate-500 mt-1">
              {{ editingPersonnel
                ? 'Update personnel information and duty status.'
                : 'Create a new station personnel record.' }}
            </p>
          </div>

          <button
            @click="showPersonnelModal = false"
            class="text-slate-400 hover:text-slate-700 text-2xl"
          >
            ×
          </button>

        </div>

        <div class="p-6 grid grid-cols-1 md:grid-cols-2 gap-4">

          <div>
            <label class="text-sm font-bold text-slate-700">
              First Name *
            </label>

            <input
              v-model="personnelForm.firstName"
              class="mt-2 w-full h-11 px-4 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]"
              placeholder="First name"
            />
          </div>

          <div>
            <label class="text-sm font-bold text-slate-700">
              Last Name *
            </label>

            <input
              v-model="personnelForm.lastName"
              class="mt-2 w-full h-11 px-4 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]"
              placeholder="Last name"
            />
          </div>

          <div>
            <label class="text-sm font-bold text-slate-700">
              Rank *
            </label>

            <select
              v-model="personnelForm.rank"
              class="mt-2 w-full h-11 px-4 rounded-xl border border-slate-300 bg-white"
            >
              <option>FO1</option>
              <option>FO2</option>
              <option>FO3</option>
              <option>SFO1</option>
              <option>SFO2</option>
              <option>F01</option>
            </select>
          </div>

          <div>
            <label class="text-sm font-bold text-slate-700">
              Position *
            </label>

            <select
              v-model="personnelForm.position"
              class="mt-2 w-full h-11 px-4 rounded-xl border border-slate-300 bg-white"
            >
              <option>Fire Officer</option>
              <option>Senior Fire Officer</option>
              <option>Station Inspector</option>
              <option>Operations Lead</option>
              <option>Administrative Officer</option>
              <option>Driver / Operator</option>
            </select>
          </div>

          <div>
            <label class="text-sm font-bold text-slate-700">
              Shift
            </label>

            <select
              v-model="personnelForm.shift"
              class="mt-2 w-full h-11 px-4 rounded-xl border border-slate-300 bg-white"
            >
              <option>Morning</option>
              <option>Afternoon</option>
              <option>Night</option>
            </select>
          </div>

          <div>
            <label class="text-sm font-bold text-slate-700">
              Duty Status
            </label>

            <select
              v-model="personnelForm.status"
              class="mt-2 w-full h-11 px-4 rounded-xl border border-slate-300 bg-white"
            >
              <option>On Duty</option>
              <option>Off Duty</option>
              <option>On Leave</option>
            </select>
          </div>

          <div>
            <label class="text-sm font-bold text-slate-700">
              Contact Number
            </label>

            <input
              v-model="personnelForm.contact"
              class="mt-2 w-full h-11 px-4 rounded-xl border border-slate-300"
              placeholder="09XX-XXX-XXXX"
            />
          </div>

          <div>
            <label class="text-sm font-bold text-slate-700">
              Email
            </label>

            <input
              v-model="personnelForm.email"
              type="email"
              class="mt-2 w-full h-11 px-4 rounded-xl border border-slate-300"
              placeholder="personnel@bfp.gov.ph"
            />
          </div>

          <div class="md:col-span-2">
            <label class="text-sm font-bold text-slate-700">
              Assignment
            </label>

            <input
              v-model="personnelForm.assignment"
              class="mt-2 w-full h-11 px-4 rounded-xl border border-slate-300"
              placeholder="Example: Fire Safety Inspection Team"
            />
          </div>

        </div>

        <div class="px-6 py-5 bg-slate-50 border-t border-slate-200 flex justify-end gap-3">

          <button
            @click="showPersonnelModal = false"
            class="px-5 py-2.5 rounded-xl border border-slate-300 text-slate-600 font-semibold hover:bg-white"
          >
            Cancel
          </button>

          <button
            @click="savePersonnel"
            class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D]"
          >
            {{ editingPersonnel ? 'Save Changes' : 'Add Personnel' }}
          </button>

        </div>

      </div>

    </div>

    <!-- DETAILS MODAL -->
    <div
      v-if="showDetailsModal && selectedPersonnel"
      class="fixed inset-0 z-50 bg-slate-900/50 backdrop-blur-sm flex items-center justify-center p-4"
    >

      <div class="w-full max-w-xl bg-white rounded-2xl shadow-2xl overflow-hidden">

        <div class="bg-[#8B1E23] p-6 text-white">

          <div class="flex items-center gap-4">

            <div class="h-16 w-16 rounded-full bg-white/20 flex items-center justify-center text-lg font-bold">
              {{ initials(selectedPersonnel) }}
            </div>

            <div>
              <p class="text-2xl font-bold">
                {{ fullName(selectedPersonnel) }}
              </p>

              <p class="text-white/80">
                {{ selectedPersonnel.rank }} • {{ selectedPersonnel.position }}
              </p>

            </div>

          </div>

        </div>

        <div class="p-6 space-y-4">

          <div class="grid grid-cols-2 gap-4">

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-400 uppercase font-bold">
                Personnel ID
              </p>

              <p class="font-bold text-slate-900 mt-1">
                {{ selectedPersonnel.id }}
              </p>
            </div>

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-400 uppercase font-bold">
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
            <p class="text-xs text-slate-400 uppercase font-bold">
              Shift
            </p>

            <p class="text-slate-700 mt-1">
              {{ selectedPersonnel.shift }}
            </p>
          </div>

          <div>
            <p class="text-xs text-slate-400 uppercase font-bold">
              Assignment
            </p>

            <p class="text-slate-700 mt-1">
              {{ selectedPersonnel.assignment || 'No assignment' }}
            </p>
          </div>

          <div>
            <p class="text-xs text-slate-400 uppercase font-bold">
              Contact
            </p>

            <p class="text-slate-700 mt-1">
              {{ selectedPersonnel.contact || 'Not provided' }}
            </p>
          </div>

          <div>
            <p class="text-xs text-slate-400 uppercase font-bold">
              Email
            </p>

            <p class="text-slate-700 mt-1">
              {{ selectedPersonnel.email || 'Not provided' }}
            </p>
          </div>

        </div>

        <div class="px-6 py-5 border-t border-slate-200 flex flex-wrap justify-end gap-3">

          <button
            @click="openAssignment(selectedPersonnel); showDetailsModal = false"
            class="px-4 py-2.5 rounded-xl border border-slate-300 text-slate-700 font-semibold hover:bg-slate-50"
          >
            Assignment
          </button>

          <button
            @click="openEditPersonnel(selectedPersonnel); showDetailsModal = false"
            class="px-4 py-2.5 rounded-xl bg-slate-900 text-white font-bold"
          >
            Edit
          </button>

          <button
            @click="showDetailsModal = false"
            class="px-4 py-2.5 rounded-xl bg-[#8B1E23] text-white font-bold"
          >
            Close
          </button>

        </div>

      </div>

    </div>

    <!-- ASSIGNMENT MODAL -->
    <div
      v-if="showAssignmentModal && selectedPersonnel"
      class="fixed inset-0 z-50 bg-slate-900/50 backdrop-blur-sm flex items-center justify-center p-4"
    >

      <div class="w-full max-w-lg bg-white rounded-2xl shadow-2xl">

        <div class="p-6 border-b border-slate-200">

          <h3 class="text-xl font-bold text-slate-900">
            Update Assignment
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            {{ fullName(selectedPersonnel) }}
          </p>

        </div>

        <div class="p-6">

          <label class="text-sm font-bold text-slate-700">
            Current Assignment
          </label>

          <input
            v-model="personnelForm.assignment"
            class="mt-2 w-full h-12 px-4 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-red-200 focus:border-[#8B1E23]"
            placeholder="Enter assignment"
          />

        </div>

        <div class="px-6 py-5 bg-slate-50 border-t border-slate-200 flex justify-end gap-3">

          <button
            @click="showAssignmentModal = false"
            class="px-5 py-2.5 rounded-xl border border-slate-300 font-semibold text-slate-600"
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

    <!-- DELETE MODAL -->
    <div
      v-if="showDeleteModal && personnelToDelete"
      class="fixed inset-0 z-50 bg-slate-900/50 backdrop-blur-sm flex items-center justify-center p-4"
    >

      <div class="w-full max-w-md bg-white rounded-2xl shadow-2xl p-6">

        <div class="h-12 w-12 rounded-full bg-red-50 text-red-600 flex items-center justify-center text-xl">
          !
        </div>

        <h3 class="text-xl font-bold text-slate-900 mt-4">
          Remove Personnel?
        </h3>

        <p class="text-sm text-slate-500 mt-2">
          Are you sure you want to remove
          <span class="font-bold text-slate-700">
            {{ fullName(personnelToDelete) }}
          </span>
          from the station roster?
        </p>

        <div class="flex justify-end gap-3 mt-6">

          <button
            @click="showDeleteModal = false"
            class="px-5 py-2.5 rounded-xl border border-slate-300 font-semibold text-slate-600"
          >
            Cancel
          </button>

          <button
            @click="deletePersonnel"
            class="px-5 py-2.5 rounded-xl bg-red-600 text-white font-bold hover:bg-red-700"
          >
            Remove
          </button>

        </div>

      </div>

    </div>

    <!-- TOAST -->
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
        class="fixed bottom-6 right-6 z-[60] max-w-sm px-5 py-4 rounded-xl shadow-xl text-sm font-semibold"
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