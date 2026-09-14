<template>
  <div class="w-full min-w-0 space-y-6">

    <!-- =========================================================
         HEADER
    ========================================================== -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">

        <div>
          <p class="text-sm font-semibold text-[#8B1E23]">
            PERSONNEL MANAGEMENT
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Personnel Roster
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            View personnel currently assigned to your station
          </p>
        </div>

        <div class="flex items-center gap-3">

          <div
            class="h-12 w-12 rounded-xl bg-[#8B1E23]
                   flex items-center justify-center text-white"
          >
            <span
              v-html="ICONS.users || ICONS.check"
              class="h-6 w-6"
            ></span>
          </div>

          <div>
            <p class="text-xs text-slate-400">
              Station Personnel
            </p>

            <p class="text-lg font-bold text-slate-900">
              {{ roster.length }} Personnel
            </p>
          </div>

        </div>

      </div>
    </section>


    <!-- =========================================================
         STATISTICS
    ========================================================== -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">

      <!-- TOTAL -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">

          <div>
            <p class="text-sm text-slate-500">
              Total Personnel
            </p>

            <p class="text-3xl font-bold text-slate-900 mt-1">
              {{ roster.length }}
            </p>

            <p class="text-xs text-slate-400 mt-1">
              Assigned to station
            </p>
          </div>

          <div class="h-11 w-11 rounded-xl bg-slate-100 flex items-center justify-center">
            <span
              v-html="ICONS.users || ICONS.check"
              class="h-5 w-5 text-slate-600"
            ></span>
          </div>

        </div>
      </div>


      <!-- ACTIVE -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">

          <div>
            <p class="text-sm text-slate-500">
              Active
            </p>

            <p class="text-3xl font-bold text-green-600 mt-1">
              {{ activeCount }}
            </p>

            <p class="text-xs text-slate-400 mt-1">
              Active personnel
            </p>
          </div>

          <div class="h-11 w-11 rounded-xl bg-green-100 flex items-center justify-center">
            <span class="text-green-600 font-bold text-lg">
              ✓
            </span>
          </div>

        </div>
      </div>


      <!-- ON DUTY -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">

          <div>
            <p class="text-sm text-slate-500">
              On Duty
            </p>

            <p class="text-3xl font-bold text-[#8B1E23] mt-1">
              {{ onDutyCount }}
            </p>

            <p class="text-xs text-slate-400 mt-1">
              Currently on duty
            </p>
          </div>

          <div class="h-11 w-11 rounded-xl bg-red-50 flex items-center justify-center">
            <span class="text-[#8B1E23] font-bold">
              ●
            </span>
          </div>

        </div>
      </div>


      <!-- OFF DUTY -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <div class="flex items-center justify-between">

          <div>
            <p class="text-sm text-slate-500">
              Off Duty
            </p>

            <p class="text-3xl font-bold text-amber-600 mt-1">
              {{ offDutyCount }}
            </p>

            <p class="text-xs text-slate-400 mt-1">
              Not currently on duty
            </p>
          </div>

          <div class="h-11 w-11 rounded-xl bg-amber-100 flex items-center justify-center">
            <span class="text-amber-600 font-bold">
              ◷
            </span>
          </div>

        </div>
      </div>

    </section>


    <!-- =========================================================
         SEARCH + FILTERS
    ========================================================== -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

      <div class="flex flex-col lg:flex-row gap-4">

        <!-- SEARCH -->
        <div class="flex-1">

          <label class="block text-sm font-semibold text-slate-700 mb-2">
            Search Personnel
          </label>

          <div class="relative">

            <input
              v-model="searchQuery"
              type="text"
              placeholder="Search by name, rank, role, or shift..."
              class="w-full px-4 py-3 rounded-xl border border-slate-300
                     focus:outline-none focus:ring-2
                     focus:ring-[#8B1E23]
                     focus:border-[#8B1E23]"
            />

          </div>

        </div>


        <!-- DUTY STATUS -->
        <div class="w-full lg:w-52">

          <label class="block text-sm font-semibold text-slate-700 mb-2">
            Duty Status
          </label>

          <select
            v-model="selectedStatus"
            class="w-full px-4 py-3 rounded-xl border border-slate-300
                   bg-white focus:outline-none
                   focus:ring-2 focus:ring-[#8B1E23]"
          >
            <option value="All Status">All Status</option>
            <option value="On Duty">On Duty</option>
            <option value="Off Duty">Off Duty</option>
            <option value="Leave">Leave</option>
          </select>

        </div>


        <!-- RANK -->
        <div class="w-full lg:w-52">

          <label class="block text-sm font-semibold text-slate-700 mb-2">
            Rank
          </label>

          <select
            v-model="selectedRank"
            class="w-full px-4 py-3 rounded-xl border border-slate-300
                   bg-white focus:outline-none
                   focus:ring-2 focus:ring-[#8B1E23]"
          >
            <option value="All Ranks">All Ranks</option>
            <option
              v-for="rank in availableRanks"
              :key="rank"
              :value="rank"
            >
              {{ rank }}
            </option>
          </select>

        </div>

      </div>


      <!-- FILTER SUMMARY -->
      <div class="mt-4 pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-3">

        <p class="text-xs text-slate-500">
          Showing
          <span class="font-bold text-slate-800">
            {{ filteredRoster.length }}
          </span>
          of
          <span class="font-bold text-slate-800">
            {{ roster.length }}
          </span>
          personnel
        </p>

        <button
          v-if="hasActiveFilters"
          @click="clearFilters"
          class="text-xs font-semibold text-[#8B1E23]
                 hover:underline"
        >
          Clear Filters
        </button>

      </div>

    </section>


    <!-- =========================================================
         MAIN CONTENT
    ========================================================== -->
    <section class="grid grid-cols-1 lg:grid-cols-3 gap-6">

      <!-- =======================================================
           PERSONNEL LIST
      ======================================================== -->
      <div class="lg:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 border-b border-slate-200 pb-4">

          <div>
            <h3 class="text-lg font-bold text-slate-900">
              Station Personnel
            </h3>

            <p class="text-sm text-slate-500 mt-1">
              Current personnel assigned to this station
            </p>
          </div>

          <span class="px-3 py-1.5 rounded-full bg-slate-100
                       text-slate-700 text-xs font-bold">
            {{ filteredRoster.length }} Members
          </span>

        </div>


        <!-- PERSONNEL CARDS -->
        <div
          v-if="filteredRoster.length > 0"
          class="mt-5 grid grid-cols-1 md:grid-cols-2 gap-4"
        >

          <div
            v-for="person in filteredRoster"
            :key="person.id || person.name"
            class="p-5 bg-slate-50 border border-slate-200
                   rounded-xl hover:border-[#8B1E23]
                   hover:shadow-md transition"
          >

            <!-- TOP -->
            <div class="flex items-start gap-4">

              <!-- AVATAR -->
              <div
                class="h-14 w-14 rounded-full bg-[#8B1E23]
                       flex items-center justify-center text-white
                       font-bold text-xs shrink-0"
              >
                {{ getInitials(person.name) }}
              </div>


              <!-- INFO -->
              <div class="flex-1 min-w-0">

                <div class="flex items-start justify-between gap-2">

                  <div class="min-w-0">

                    <p class="text-base font-bold text-slate-900 truncate">
                      {{ person.name }}
                    </p>

                    <p class="text-sm text-[#8B1E23] font-semibold mt-1">
                      {{ person.role || person.rank }}
                    </p>

                  </div>

                  <!-- STATUS -->
                  <span
                    :class="getStatusClass(person.status)"
                    class="px-2.5 py-1 rounded-full text-[10px]
                           font-bold whitespace-nowrap"
                  >
                    {{ person.status || 'Active' }}
                  </span>

                </div>

                <p class="text-sm text-slate-500 mt-1">
                  {{ person.shift || 'Station Duty' }}
                </p>

              </div>

            </div>


            <!-- DETAILS -->
            <div class="mt-4 pt-4 border-t border-slate-200 grid grid-cols-2 gap-3">

              <div>
                <p class="text-xs text-slate-400">
                  Rank
                </p>

                <p class="text-sm font-semibold text-slate-700 mt-1">
                  {{ person.rank || 'Fire Officer' }}
                </p>
              </div>

              <div>
                <p class="text-xs text-slate-400">
                  Availability
                </p>

                <p
                  class="text-sm font-semibold mt-1"
                  :class="getAvailabilityColor(person)"
                >
                  {{ person.availability || getAvailability(person) }}
                </p>
              </div>

            </div>


            <!-- CURRENT USER -->
            <div
              v-if="isCurrentUser(person)"
              class="mt-4 px-3 py-2 rounded-lg
                     bg-red-50 border border-red-100"
            >
              <p class="text-xs font-semibold text-[#8B1E23]">
                You are viewing your own personnel record
              </p>
            </div>


            <!-- VIEW BUTTON -->
            <button
              @click="viewPersonnel(person)"
              class="w-full mt-4 px-4 py-2.5 rounded-lg
                     border border-slate-300 bg-white
                     text-sm font-semibold text-slate-700
                     hover:bg-[#8B1E23] hover:text-white
                     hover:border-[#8B1E23] transition"
            >
              View Personnel Details
            </button>

          </div>

        </div>


        <!-- EMPTY STATE -->
        <div
          v-else
          class="py-12 text-center"
        >

          <div
            class="h-16 w-16 mx-auto rounded-full bg-slate-100
                   flex items-center justify-center"
          >
            <span
              v-html="ICONS.users || ICONS.check"
              class="h-7 w-7 text-slate-400"
            ></span>
          </div>

          <h3 class="text-lg font-bold text-slate-900 mt-4">
            No personnel found
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            Try changing your search or filter criteria.
          </p>

          <button
            @click="clearFilters"
            class="mt-4 px-4 py-2 rounded-lg
                   bg-[#8B1E23] text-white
                   text-sm font-semibold hover:bg-[#72181D]"
          >
            Clear Filters
          </button>

        </div>

      </div>


      <!-- =======================================================
           RIGHT SIDEBAR
      ======================================================== -->
      <div class="space-y-6">

        <!-- DUTY OVERVIEW -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <h3 class="text-lg font-bold text-slate-900">
            Duty Overview
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            Personnel availability today
          </p>


          <div class="mt-5 space-y-5">

            <!-- ON DUTY -->
            <div>

              <div class="flex justify-between text-sm mb-2">

                <span class="font-medium text-slate-600">
                  On Duty
                </span>

                <span class="font-bold text-slate-900">
                  {{ onDutyCount }} / {{ roster.length }}
                </span>

              </div>

              <div class="h-2 bg-slate-100 rounded-full overflow-hidden">

                <div
                  class="h-full bg-[#8B1E23] rounded-full transition-all"
                  :style="{ width: onDutyPercentage + '%' }"
                ></div>

              </div>

              <p class="text-xs text-slate-400 mt-1">
                {{ onDutyPercentage }}% of personnel
              </p>

            </div>


            <!-- OFF DUTY -->
            <div>

              <div class="flex justify-between text-sm mb-2">

                <span class="font-medium text-slate-600">
                  Off Duty
                </span>

                <span class="font-bold text-slate-900">
                  {{ offDutyCount }} / {{ roster.length }}
                </span>

              </div>

              <div class="h-2 bg-slate-100 rounded-full overflow-hidden">

                <div
                  class="h-full bg-amber-400 rounded-full transition-all"
                  :style="{ width: offDutyPercentage + '%' }"
                ></div>

              </div>

              <p class="text-xs text-slate-400 mt-1">
                {{ offDutyPercentage }}% of personnel
              </p>

            </div>


            <!-- LEAVE -->
            <div v-if="leaveCount > 0">

              <div class="flex justify-between text-sm mb-2">

                <span class="font-medium text-slate-600">
                  On Leave
                </span>

                <span class="font-bold text-slate-900">
                  {{ leaveCount }} / {{ roster.length }}
                </span>

              </div>

              <div class="h-2 bg-slate-100 rounded-full overflow-hidden">

                <div
                  class="h-full bg-slate-400 rounded-full transition-all"
                  :style="{ width: leavePercentage + '%' }"
                ></div>

              </div>

            </div>

          </div>

        </div>


        <!-- SHIFT INFORMATION -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <h3 class="text-lg font-bold text-slate-900">
            Shift Information
          </h3>

          <div class="mt-5 space-y-4">

            <div class="flex justify-between items-center gap-4">

              <span class="text-sm text-slate-500">
                Current Shift
              </span>

              <span class="text-sm font-bold text-slate-900">
                Day Shift
              </span>

            </div>

            <div class="flex justify-between items-center gap-4">

              <span class="text-sm text-slate-500">
                Time
              </span>

              <span class="text-sm font-bold text-slate-900 text-right">
                08:00 AM – 05:00 PM
              </span>

            </div>

            <div class="flex justify-between items-center gap-4">

              <span class="text-sm text-slate-500">
                Duty Officer
              </span>

              <span class="text-sm font-bold text-[#8B1E23] text-right">
                Station Inspector
              </span>

            </div>

          </div>

        </div>


        <!-- STAFFING STATUS -->
        <div class="bg-[#8B1E23] rounded-2xl shadow-sm p-6 text-white">

          <p class="text-sm text-red-100">
            Current Staffing
          </p>

          <div class="flex items-end gap-2 mt-1">

            <p class="text-3xl font-bold">
              {{ onDutyCount }}
            </p>

            <p class="text-sm text-red-100 mb-1">
              personnel on duty
            </p>

          </div>

          <div class="mt-4 pt-4 border-t border-white/20">

            <div class="flex justify-between text-sm">

              <span class="text-red-100">
                Staffing Level
              </span>

              <span class="font-bold">
                {{ staffingStatus }}
              </span>

            </div>

          </div>

        </div>

      </div>

    </section>


    <!-- =========================================================
         PERSONNEL DETAILS MODAL
    ========================================================== -->
    <div
      v-if="selectedPersonnel"
      class="fixed inset-0 z-50 bg-black/40
             flex items-center justify-center p-4"
      @click.self="selectedPersonnel = null"
    >

      <div
        class="bg-white w-full max-w-lg rounded-2xl
               shadow-2xl overflow-hidden"
      >

        <!-- MODAL HEADER -->
        <div class="bg-[#8B1E23] px-6 py-5 text-white">

          <div class="flex items-start justify-between gap-4">

            <div class="flex items-center gap-4">

              <div
                class="h-14 w-14 rounded-full bg-white/15
                       flex items-center justify-center
                       font-bold text-sm"
              >
                {{ getInitials(selectedPersonnel.name) }}
              </div>

              <div>

                <p class="text-xs text-red-100 uppercase tracking-wide">
                  Personnel Record
                </p>

                <h3 class="text-xl font-bold mt-1">
                  {{ selectedPersonnel.name }}
                </h3>

              </div>

            </div>

            <button
              @click="selectedPersonnel = null"
              class="h-9 w-9 rounded-lg bg-white/10
                     hover:bg-white/20 transition"
            >
              ✕
            </button>

          </div>

        </div>


        <!-- MODAL BODY -->
        <div class="p-6 space-y-5">

          <!-- STATUS -->
          <div class="flex items-center justify-between">

            <span class="text-sm text-slate-500">
              Current Status
            </span>

            <span
              :class="getStatusClass(selectedPersonnel.status)"
              class="px-3 py-1.5 rounded-full text-xs font-bold"
            >
              {{ selectedPersonnel.status || 'Active' }}
            </span>

          </div>


          <!-- DETAILS -->
          <div class="grid grid-cols-2 gap-4">

            <div class="bg-slate-50 rounded-xl p-4">

              <p class="text-xs text-slate-500">
                Rank
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedPersonnel.rank || 'Fire Officer' }}
              </p>

            </div>

            <div class="bg-slate-50 rounded-xl p-4">

              <p class="text-xs text-slate-500">
                Role
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedPersonnel.role || 'Station Personnel' }}
              </p>

            </div>

            <div class="bg-slate-50 rounded-xl p-4">

              <p class="text-xs text-slate-500">
                Shift
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedPersonnel.shift || 'Station Duty' }}
              </p>

            </div>

            <div class="bg-slate-50 rounded-xl p-4">

              <p class="text-xs text-slate-500">
                Availability
              </p>

              <p
                class="text-sm font-bold mt-1"
                :class="getAvailabilityColor(selectedPersonnel)"
              >
                {{ selectedPersonnel.availability || getAvailability(selectedPersonnel) }}
              </p>

            </div>

          </div>


          <!-- CONTACT -->
          <div
            v-if="selectedPersonnel.contact || selectedPersonnel.phone || selectedPersonnel.email"
            class="border-t border-slate-200 pt-5"
          >

            <p class="text-sm font-bold text-slate-900">
              Contact Information
            </p>

            <div class="mt-3 space-y-2">

              <p
                v-if="selectedPersonnel.phone || selectedPersonnel.contact"
                class="text-sm text-slate-600"
              >
                <span class="font-semibold">Phone:</span>
                {{ selectedPersonnel.phone || selectedPersonnel.contact }}
              </p>

              <p
                v-if="selectedPersonnel.email"
                class="text-sm text-slate-600"
              >
                <span class="font-semibold">Email:</span>
                {{ selectedPersonnel.email }}
              </p>

            </div>

          </div>


          <!-- CLOSE -->
          <div class="flex justify-end pt-2">

            <button
              @click="selectedPersonnel = null"
              class="px-5 py-2.5 rounded-xl
                     bg-[#8B1E23] text-white
                     text-sm font-semibold
                     hover:bg-[#72181D] transition"
            >
              Close
            </button>

          </div>

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

  roster: {
    type: Array,
    required: false,
    default: () => []
  }
})


/* =========================================================
   FILTER STATE
========================================================= */

const searchQuery = ref('')
const selectedStatus = ref('All Status')
const selectedRank = ref('All Ranks')

const selectedPersonnel = ref(null)


/* =========================================================
   AVAILABLE RANKS
========================================================= */

const availableRanks = computed(() => {

  const ranks = props.roster
    .map(person => person.rank)
    .filter(Boolean)

  return [...new Set(ranks)]
})


/* =========================================================
   FILTERED ROSTER
========================================================= */

const filteredRoster = computed(() => {

  const query = searchQuery.value
    .toLowerCase()
    .trim()

  return props.roster.filter(person => {

    const searchText = [
      person.name,
      person.rank,
      person.role,
      person.shift
    ]
      .filter(Boolean)
      .join(' ')
      .toLowerCase()

    const matchesSearch =
      !query || searchText.includes(query)

    const personStatus =
      person.status || 'Active'

    const matchesStatus =
      selectedStatus.value === 'All Status' ||
      personStatus === selectedStatus.value

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

const activeCount = computed(() => {

  return props.roster.filter(
    person => (person.status || 'Active') === 'Active'
  ).length

})


const onDutyCount = computed(() => {

  return props.roster.filter(
    person => person.status === 'On Duty'
  ).length

})


const offDutyCount = computed(() => {

  return props.roster.filter(
    person => person.status === 'Off Duty'
  ).length

})


const leaveCount = computed(() => {

  return props.roster.filter(
    person => person.status === 'Leave'
  ).length

})


/* =========================================================
   PERCENTAGES
========================================================= */

const calculatePercentage = count => {

  if (!props.roster.length) {
    return 0
  }

  return Math.round(
    (count / props.roster.length) * 100
  )

}


const onDutyPercentage = computed(() =>
  calculatePercentage(onDutyCount.value)
)


const offDutyPercentage = computed(() =>
  calculatePercentage(offDutyCount.value)
)


const leavePercentage = computed(() =>
  calculatePercentage(leaveCount.value)
)


/* =========================================================
   STAFFING STATUS
========================================================= */

const staffingStatus = computed(() => {

  if (!props.roster.length) {
    return 'No Data'
  }

  const percentage = onDutyPercentage.value

  if (percentage >= 70) {
    return 'Good'
  }

  if (percentage >= 40) {
    return 'Moderate'
  }

  return 'Low'
})


/* =========================================================
   FILTER HELPERS
========================================================= */

const hasActiveFilters = computed(() => {

  return (
    searchQuery.value !== '' ||
    selectedStatus.value !== 'All Status' ||
    selectedRank.value !== 'All Ranks'
  )

})


const clearFilters = () => {

  searchQuery.value = ''
  selectedStatus.value = 'All Status'
  selectedRank.value = 'All Ranks'

}


/* =========================================================
   PERSONNEL ACTIONS
========================================================= */

const viewPersonnel = person => {

  selectedPersonnel.value = person

}


const isCurrentUser = person => {

  if (!props.currentUser) {
    return false
  }

  const currentIdentifier =
    props.currentUser.identifier ||
    props.currentUser.email ||
    props.currentUser.name

  const personIdentifier =
    person.identifier ||
    person.email ||
    person.name

  return (
    currentIdentifier &&
    personIdentifier &&
    currentIdentifier === personIdentifier
  )

}


/* =========================================================
   INITIALS
========================================================= */

const getInitials = name => {

  if (!name) {
    return 'FP'
  }

  return name
    .split(' ')
    .filter(Boolean)
    .slice(0, 2)
    .map(word => word.charAt(0).toUpperCase())
    .join('')

}


/* =========================================================
   STATUS STYLING
========================================================= */

const getStatusClass = status => {

  if (status === 'On Duty') {
    return 'bg-green-100 text-green-700'
  }

  if (status === 'Off Duty') {
    return 'bg-amber-100 text-amber-700'
  }

  if (status === 'Leave') {
    return 'bg-slate-100 text-slate-600'
  }

  if (status === 'Inactive') {
    return 'bg-red-100 text-red-700'
  }

  return 'bg-green-100 text-green-700'

}


/* =========================================================
   AVAILABILITY
========================================================= */

const getAvailability = person => {

  if (person.status === 'On Duty') {
    return 'Available'
  }

  if (person.status === 'Off Duty') {
    return 'Off Station'
  }

  if (person.status === 'Leave') {
    return 'On Leave'
  }

  return 'Available'

}


const getAvailabilityColor = person => {

  const availability =
    person.availability ||
    getAvailability(person)

  if (availability === 'Available') {
    return 'text-green-600'
  }

  if (
    availability === 'Off Station' ||
    availability === 'Busy'
  ) {
    return 'text-amber-600'
  }

  if (availability === 'On Leave') {
    return 'text-slate-500'
  }

  return 'text-slate-700'

}
</script>