<script setup>
import { ref, computed, onMounted } from 'vue'

defineProps({
  currentUser: {
    type: Object,
    required: false,
    default: null
  }
})

const STORAGE_KEY = 'fireNotifyComplianceHealth'

const stations = ref([])
const riskAreas = ref([])
const remediationPlans = ref([])

const searchQuery = ref('')
const stationStatusFilter = ref('All')

const showStationModal = ref(false)
const showRiskModal = ref(false)
const showPlanModal = ref(false)
const showDetailsModal = ref(false)

const selectedStation = ref(null)
const selectedRisk = ref(null)
const selectedPlan = ref(null)

const toastMessage = ref('')
const showToast = ref(false)

const stationForm = ref({
  name: '',
  description: '',
  compliance: 90,
  status: 'Good Standing'
})

const riskForm = ref({
  title: '',
  description: '',
  severity: 'Medium'
})

const planForm = ref({
  priority: 'Priority 1',
  title: '',
  description: '',
  status: 'Pending'
})

/* =========================================================
   DEFAULT DATA
========================================================= */

const defaultStations = [
  {
    id: 'ST-001',
    name: 'Station 1',
    description: 'Submission quality and adherence',
    compliance: 95,
    status: 'Good Standing',
    lastAudit: '2026-09-12'
  },
  {
    id: 'ST-002',
    name: 'Station 2',
    description: 'Equipment checks and reporting',
    compliance: 82,
    status: 'Needs Attention',
    lastAudit: '2026-09-10'
  },
  {
    id: 'ST-003',
    name: 'Station 3',
    description: 'Documentation completeness',
    compliance: 91,
    status: 'Good Standing',
    lastAudit: '2026-09-11'
  }
]

const defaultRisks = [
  {
    id: 'RISK-001',
    title: 'Delayed Report Submission',
    description: 'Two station reports remain unsubmitted beyond target deadlines.',
    severity: 'High',
    status: 'Open'
  },
  {
    id: 'RISK-002',
    title: 'Incomplete Attachments',
    description: 'Several reports lack required photos, signatures, or supporting documents.',
    severity: 'Medium',
    status: 'Open'
  },
  {
    id: 'RISK-003',
    title: 'Equipment Verification Window',
    description: 'One station missed a scheduled maintenance verification audit this cycle.',
    severity: 'Low',
    status: 'Open'
  }
]

const defaultPlans = [
  {
    id: 'PLAN-001',
    priority: 'Priority 1',
    title: 'Complete overdue reports',
    description: 'Complete all overdue reports and apply review notes before end of day.',
    status: 'Pending'
  },
  {
    id: 'PLAN-002',
    priority: 'Priority 2',
    title: 'Reconcile missing attachments',
    description: 'Reconcile missing attachments and require station-level verification before submission.',
    status: 'Pending'
  },
  {
    id: 'PLAN-003',
    priority: 'Priority 3',
    title: 'Reschedule equipment verification',
    description: 'Reschedule equipment verification for the affected station and document corrective action.',
    status: 'Pending'
  }
]

/* =========================================================
   LOAD / SAVE
========================================================= */

const loadData = () => {
  const saved = localStorage.getItem(STORAGE_KEY)

  if (saved) {
    try {
      const data = JSON.parse(saved)

      stations.value = data.stations || defaultStations
      riskAreas.value = data.riskAreas || defaultRisks
      remediationPlans.value = data.remediationPlans || defaultPlans

      return
    } catch (error) {
      console.error('Failed to load compliance health data:', error)
    }
  }

  stations.value = defaultStations
  riskAreas.value = defaultRisks
  remediationPlans.value = defaultPlans

  saveData()
}

const saveData = () => {
  localStorage.setItem(
    STORAGE_KEY,
    JSON.stringify({
      stations: stations.value,
      riskAreas: riskAreas.value,
      remediationPlans: remediationPlans.value
    })
  )
}

onMounted(() => {
  loadData()
})

/* =========================================================
   COMPUTED
========================================================= */

const overallHealth = computed(() => {
  if (!stations.value.length) return 0

  return Math.round(
    stations.value.reduce(
      (total, station) => total + Number(station.compliance),
      0
    ) / stations.value.length
  )
})

const goodStandingCount = computed(() =>
  stations.value.filter(
    station => station.compliance >= 90
  ).length
)

const needsAttentionCount = computed(() =>
  stations.value.filter(
    station => station.compliance < 90
  ).length
)

const deadlineAdherence = computed(() => {
  const health = overallHealth.value

  if (health >= 95) return 96
  if (health >= 90) return 93
  if (health >= 85) return 89

  return 82
})

const openRiskCount = computed(() =>
  riskAreas.value.filter(
    risk => risk.status === 'Open'
  ).length
)

const completedPlanCount = computed(() =>
  remediationPlans.value.filter(
    plan => plan.status === 'Completed'
  ).length
)

const filteredStations = computed(() => {
  const query = searchQuery.value.toLowerCase().trim()

  return stations.value.filter(station => {
    const matchesSearch =
      !query ||
      station.name.toLowerCase().includes(query) ||
      station.description.toLowerCase().includes(query)

    const matchesStatus =
      stationStatusFilter.value === 'All' ||
      station.status === stationStatusFilter.value

    return matchesSearch && matchesStatus
  })
})

/* =========================================================
   STATION MANAGEMENT
========================================================= */

const openStationDetails = station => {
  selectedStation.value = station
  showDetailsModal.value = true
}

const openStationEdit = station => {
  selectedStation.value = station

  stationForm.value = {
    name: station.name,
    description: station.description,
    compliance: station.compliance,
    status: station.status
  }

  showStationModal.value = true
}

const saveStation = () => {
  if (!stationForm.value.name.trim()) {
    showNotification('Station name is required.')
    return
  }

  if (selectedStation.value) {
    const index = stations.value.findIndex(
      station => station.id === selectedStation.value.id
    )

    if (index !== -1) {
      stations.value[index] = {
        ...stations.value[index],
        name: stationForm.value.name,
        description: stationForm.value.description,
        compliance: Number(stationForm.value.compliance),
        status:
          Number(stationForm.value.compliance) >= 90
            ? 'Good Standing'
            : 'Needs Attention'
      }
    }

    showNotification('Station compliance updated.')
  }

  saveData()
  showStationModal.value = false
}

/* =========================================================
   RISK MANAGEMENT
========================================================= */

const openRiskDetails = risk => {
  selectedRisk.value = risk
  showRiskModal.value = true
}

const resolveRisk = risk => {
  const item = riskAreas.value.find(
    record => record.id === risk.id
  )

  if (!item) return

  item.status = 'Resolved'

  saveData()

  showNotification('Risk area marked as resolved.')
}

/* =========================================================
   REMEDIATION MANAGEMENT
========================================================= */

const openPlanDetails = plan => {
  selectedPlan.value = plan
  showPlanModal.value = true
}

const updatePlanStatus = plan => {
  const item = remediationPlans.value.find(
    record => record.id === plan.id
  )

  if (!item) return

  item.status =
    item.status === 'Completed'
      ? 'Pending'
      : 'Completed'

  saveData()

  showNotification(
    item.status === 'Completed'
      ? 'Remediation plan completed.'
      : 'Remediation plan reopened.'
  )
}

/* =========================================================
   FILTERS
========================================================= */

const clearFilters = () => {
  searchQuery.value = ''
  stationStatusFilter.value = 'All'
}

/* =========================================================
   UTILITIES
========================================================= */

const showNotification = message => {
  toastMessage.value = message
  showToast.value = true

  setTimeout(() => {
    showToast.value = false
  }, 2500)
}

const formatDate = date => {
  if (!date) return 'No audit date'

  return new Date(`${date}T00:00:00`).toLocaleDateString(
    'en-US',
    {
      month: 'short',
      day: 'numeric',
      year: 'numeric'
    }
  )
}

const stationProgressClass = percentage => {
  if (percentage >= 90) {
    return 'bg-emerald-500'
  }

  if (percentage >= 80) {
    return 'bg-yellow-500'
  }

  return 'bg-red-500'
}

const stationTextClass = percentage => {
  if (percentage >= 90) {
    return 'text-green-600'
  }

  if (percentage >= 80) {
    return 'text-yellow-600'
  }

  return 'text-red-600'
}

const riskClass = severity => {
  if (severity === 'High') {
    return 'border-red-200 bg-red-50'
  }

  if (severity === 'Medium') {
    return 'border-yellow-200 bg-yellow-50'
  }

  return 'border-blue-200 bg-blue-50'
}

const riskBadgeClass = severity => {
  if (severity === 'High') {
    return 'bg-red-100 text-red-700'
  }

  if (severity === 'Medium') {
    return 'bg-yellow-100 text-yellow-700'
  }

  return 'bg-blue-100 text-blue-700'
}

const planClass = priority => {
  if (priority === 'Priority 1') {
    return 'border-emerald-200 bg-emerald-50'
  }

  if (priority === 'Priority 2') {
    return 'border-orange-200 bg-orange-50'
  }

  return 'border-indigo-200 bg-indigo-50'
}

/* =========================================================
   REPORT
========================================================= */

const viewFullReport = () => {
  const report = [
    'FIRENOTIFY - COMPLIANCE HEALTH REPORT',
    '',
    `Overall Health: ${overallHealth.value}%`,
    `Good Standing: ${goodStandingCount.value}`,
    `Needs Attention: ${needsAttentionCount.value}`,
    `Deadline Adherence: ${deadlineAdherence.value}%`,
    '',
    'STATION COMPLIANCE',
    ...stations.value.map(
      station =>
        `${station.name} - ${station.compliance}% - ${station.status}`
    ),
    '',
    'RISK AREAS',
    ...riskAreas.value.map(
      risk =>
        `${risk.title} - ${risk.severity} - ${risk.status}`
    ),
    '',
    'REMEDIATION PLANS',
    ...remediationPlans.value.map(
      plan =>
        `${plan.priority}: ${plan.title} - ${plan.status}`
    )
  ].join('\n')

  const blob = new Blob([report], {
    type: 'text/plain;charset=utf-8'
  })

  const url = URL.createObjectURL(blob)

  const link = document.createElement('a')
  link.href = url
  link.download = 'FireNotify-Compliance-Health-Report.txt'
  link.click()

  URL.revokeObjectURL(url)

  showNotification('Compliance report generated.')
}
</script>

<template>
  <div class="space-y-6">

    <!-- TOAST -->
    <transition name="fade">
      <div
        v-if="showToast"
        class="fixed top-6 right-6 z-[100] bg-slate-900 text-white px-5 py-3 rounded-xl shadow-lg text-sm font-semibold"
      >
        {{ toastMessage }}
      </div>
    </transition>

    <!-- HEADER -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

        <div>
          <p class="text-sm font-bold uppercase tracking-wide text-[#8B1E23]">
            Operational Health
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Compliance Health
          </h2>

          <p class="text-base text-slate-500 mt-1">
            Monitor station compliance, review health indicators, and track corrective actions.
          </p>
        </div>

        <button
          @click="viewFullReport"
          class="px-5 py-3 rounded-xl border border-slate-300 bg-white text-slate-700 font-bold hover:bg-slate-100 transition"
        >
          View Full Report
        </button>

      </div>
    </section>

    <!-- STATS -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-[#8B1E23]">
          {{ overallHealth }}%
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Overall Health
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-green-600">
          {{ String(goodStandingCount).padStart(2, '0') }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Good Standing
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-yellow-600">
          {{ String(needsAttentionCount).padStart(2, '0') }}
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Needs Attention
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-3xl font-bold text-blue-600">
          {{ deadlineAdherence }}%
        </p>

        <p class="text-sm text-slate-500 mt-1">
          Deadline Adherence
        </p>
      </div>

    </section>

    <!-- SEARCH -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

      <div class="flex flex-col lg:flex-row gap-4">

        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search station or compliance area..."
          class="flex-1 px-4 py-3 border border-slate-200 rounded-xl outline-none focus:border-[#8B1E23]"
        />

        <select
          v-model="stationStatusFilter"
          class="px-4 py-3 border border-slate-200 rounded-xl bg-white"
        >
          <option value="All">All Status</option>
          <option value="Good Standing">Good Standing</option>
          <option value="Needs Attention">Needs Attention</option>
        </select>

        <button
          @click="clearFilters"
          class="px-5 py-3 rounded-xl border border-slate-200 font-bold text-slate-700 hover:bg-slate-50"
        >
          Clear
        </button>

      </div>

    </section>

    <!-- STATION + STANDARDS -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- STATION SNAPSHOT -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">

          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Station Compliance Snapshot
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              Performance of each station and unit
            </p>
          </div>

          <span class="text-xs font-bold text-slate-500">
            {{ filteredStations.length }} Stations
          </span>

        </div>

        <div class="mt-5 space-y-4">

          <div
            v-for="station in filteredStations"
            :key="station.id"
            class="p-4 rounded-xl border border-slate-200 bg-slate-50 hover:bg-slate-100 transition"
          >

            <div class="flex justify-between items-start gap-4">

              <div>
                <p class="text-sm font-bold text-slate-900">
                  {{ station.name }}
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  {{ station.description }}
                </p>

                <p class="text-xs text-slate-400 mt-2">
                  Last audit: {{ formatDate(station.lastAudit) }}
                </p>
              </div>

              <div class="text-right">

                <p
                  class="text-sm font-bold"
                  :class="stationTextClass(station.compliance)"
                >
                  {{ station.compliance }}%
                </p>

                <p class="text-[11px] text-slate-400">
                  {{ station.status }}
                </p>

              </div>

            </div>

            <div class="h-2 rounded-full bg-slate-200 overflow-hidden mt-4">

              <div
                class="h-full rounded-full transition-all"
                :class="stationProgressClass(station.compliance)"
                :style="{ width: `${station.compliance}%` }"
              ></div>

            </div>

            <div class="flex justify-end gap-2 mt-4">

              <button
                @click="openStationDetails(station)"
                class="px-3 py-2 rounded-lg bg-white border border-slate-200 text-xs font-bold text-slate-700 hover:bg-slate-100"
              >
                View
              </button>

              <button
                @click="openStationEdit(station)"
                class="px-3 py-2 rounded-lg bg-blue-50 text-blue-700 text-xs font-bold hover:bg-blue-100"
              >
                Update
              </button>

            </div>

          </div>

          <div
            v-if="filteredStations.length === 0"
            class="py-10 text-center"
          >
            <p class="text-3xl">🔎</p>

            <p class="font-bold text-slate-700 mt-2">
              No stations found
            </p>
          </div>

        </div>
      </div>

      <!-- STANDARDS -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="border-b border-slate-200 pb-5">

          <h2 class="text-xl font-bold text-slate-900">
            Standards Check Status
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Current compliance checklist progress
          </p>

        </div>

        <div class="mt-5 space-y-6">

          <div>

            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Daily Logs</span>
              <span>98%</span>
            </div>

            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[98%] rounded-full bg-emerald-500"></div>
            </div>

          </div>

          <div>

            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Equipment Verification</span>
              <span>87%</span>
            </div>

            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[87%] rounded-full bg-blue-500"></div>
            </div>

          </div>

          <div>

            <div class="flex justify-between text-sm font-semibold text-slate-700 mb-2">
              <span>Attachment Completeness</span>
              <span>84%</span>
            </div>

            <div class="h-2.5 rounded-full bg-slate-100 overflow-hidden">
              <div class="h-full w-[84%] rounded-full bg-yellow-500"></div>
            </div>

          </div>

        </div>

        <div class="mt-8 p-4 rounded-xl bg-slate-50 border border-slate-200">

          <div class="flex justify-between items-center">

            <div>
              <p class="text-sm font-bold text-slate-900">
                Open Risk Areas
              </p>

              <p class="text-xs text-slate-500 mt-1">
                Items requiring corrective action
              </p>
            </div>

            <span class="text-2xl font-bold text-red-600">
              {{ openRiskCount }}
            </span>

          </div>

        </div>

      </div>

    </section>

    <!-- RISK + REMEDIATION -->
    <section class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <!-- RISK AREAS -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">

          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Risk Areas
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              Potential gaps affecting compliance
            </p>
          </div>

          <span class="px-3 py-1 rounded-full bg-red-100 text-red-700 text-xs font-bold">
            {{ openRiskCount }} Open
          </span>

        </div>

        <div class="mt-5 space-y-4">

          <div
            v-for="risk in riskAreas"
            :key="risk.id"
            class="p-4 rounded-xl border"
            :class="riskClass(risk.severity)"
          >

            <div class="flex justify-between gap-3">

              <div>
                <p class="text-sm font-bold text-slate-900">
                  {{ risk.title }}
                </p>

                <p class="text-sm text-slate-600 mt-1">
                  {{ risk.description }}
                </p>
              </div>

              <span
                class="h-fit px-2.5 py-1 rounded-full text-xs font-bold"
                :class="riskBadgeClass(risk.severity)"
              >
                {{ risk.severity }}
              </span>

            </div>

            <div class="flex justify-end gap-2 mt-4">

              <button
                @click="openRiskDetails(risk)"
                class="px-3 py-2 rounded-lg bg-white/80 border border-slate-200 text-xs font-bold text-slate-700"
              >
                View
              </button>

              <button
                v-if="risk.status === 'Open'"
                @click="resolveRisk(risk)"
                class="px-3 py-2 rounded-lg bg-green-100 text-green-700 text-xs font-bold hover:bg-green-200"
              >
                Resolve
              </button>

            </div>

          </div>

        </div>
      </div>

      <!-- REMEDIATION -->
      <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex items-center justify-between border-b border-slate-200 pb-5">

          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Remediation Plan
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              Immediate steps to improve health scores
            </p>
          </div>

          <span class="text-xs font-bold text-slate-500">
            {{ completedPlanCount }}/{{ remediationPlans.length }} Complete
          </span>

        </div>

        <div class="mt-5 space-y-4">

          <div
            v-for="plan in remediationPlans"
            :key="plan.id"
            class="p-4 rounded-xl border"
            :class="planClass(plan.priority)"
          >

            <div class="flex justify-between gap-3">

              <div>
                <p class="text-xs font-bold text-slate-500">
                  {{ plan.priority }}
                </p>

                <p class="text-sm font-bold text-slate-900 mt-1">
                  {{ plan.title }}
                </p>

                <p class="text-sm text-slate-600 mt-1">
                  {{ plan.description }}
                </p>
              </div>

              <span
                class="h-fit px-2.5 py-1 rounded-full text-xs font-bold"
                :class="
                  plan.status === 'Completed'
                    ? 'bg-green-100 text-green-700'
                    : 'bg-yellow-100 text-yellow-700'
                "
              >
                {{ plan.status }}
              </span>

            </div>

            <div class="flex justify-end gap-2 mt-4">

              <button
                @click="openPlanDetails(plan)"
                class="px-3 py-2 rounded-lg bg-white/80 border border-slate-200 text-xs font-bold text-slate-700"
              >
                View
              </button>

              <button
                @click="updatePlanStatus(plan)"
                class="px-3 py-2 rounded-lg bg-green-100 text-green-700 text-xs font-bold hover:bg-green-200"
              >
                {{ plan.status === 'Completed' ? 'Reopen' : 'Complete' }}
              </button>

            </div>

          </div>

        </div>
      </div>

    </section>

    <!-- STATION DETAILS MODAL -->
    <div
      v-if="showDetailsModal && selectedStation"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div class="bg-white rounded-2xl shadow-2xl w-full max-w-lg">

        <div class="p-6 border-b border-slate-200 flex justify-between">

          <div>
            <p class="text-xs font-bold text-[#8B1E23]">
              {{ selectedStation.id }}
            </p>

            <h2 class="text-xl font-bold text-slate-900 mt-1">
              {{ selectedStation.name }}
            </h2>
          </div>

          <button
            @click="showDetailsModal = false"
            class="text-2xl text-slate-400"
          >
            ×
          </button>

        </div>

        <div class="p-6 space-y-5">

          <div class="text-center">

            <p
              class="text-5xl font-bold"
              :class="stationTextClass(selectedStation.compliance)"
            >
              {{ selectedStation.compliance }}%
            </p>

            <p class="text-sm text-slate-500 mt-1">
              Compliance Score
            </p>

          </div>

          <div class="grid grid-cols-2 gap-4">

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-400 uppercase font-bold">
                Status
              </p>

              <p class="font-bold text-slate-800 mt-1">
                {{ selectedStation.status }}
              </p>
            </div>

            <div class="p-4 rounded-xl bg-slate-50">
              <p class="text-xs text-slate-400 uppercase font-bold">
                Last Audit
              </p>

              <p class="font-bold text-slate-800 mt-1">
                {{ formatDate(selectedStation.lastAudit) }}
              </p>
            </div>

          </div>

          <div>
            <p class="text-xs text-slate-400 uppercase font-bold">
              Monitoring Area
            </p>

            <p class="text-sm text-slate-600 mt-1">
              {{ selectedStation.description }}
            </p>
          </div>

        </div>

        <div class="p-6 border-t border-slate-200 flex justify-end">

          <button
            @click="showDetailsModal = false"
            class="px-5 py-3 rounded-xl bg-slate-100 font-bold text-slate-700"
          >
            Close
          </button>

        </div>

      </div>
    </div>

    <!-- STATION EDIT MODAL -->
    <div
      v-if="showStationModal"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div class="bg-white rounded-2xl shadow-2xl w-full max-w-lg">

        <div class="p-6 border-b border-slate-200 flex justify-between">

          <div>
            <h2 class="text-xl font-bold text-slate-900">
              Update Compliance
            </h2>

            <p class="text-sm text-slate-500 mt-1">
              Update the station health indicator.
            </p>
          </div>

          <button
            @click="showStationModal = false"
            class="text-2xl text-slate-400"
          >
            ×
          </button>

        </div>

        <div class="p-6 space-y-5">

          <div>
            <label class="block text-sm font-bold text-slate-700 mb-2">
              Station
            </label>

            <input
              v-model="stationForm.name"
              type="text"
              class="w-full px-4 py-3 border border-slate-200 rounded-xl"
            />
          </div>

          <div>
            <label class="block text-sm font-bold text-slate-700 mb-2">
              Monitoring Area
            </label>

            <input
              v-model="stationForm.description"
              type="text"
              class="w-full px-4 py-3 border border-slate-200 rounded-xl"
            />
          </div>

          <div>

            <div class="flex justify-between mb-2">

              <label class="text-sm font-bold text-slate-700">
                Compliance Score
              </label>

              <span class="font-bold text-[#8B1E23]">
                {{ stationForm.compliance }}%
              </span>

            </div>

            <input
              v-model.number="stationForm.compliance"
              type="range"
              min="0"
              max="100"
              class="w-full"
            />

          </div>

        </div>

        <div class="p-6 border-t border-slate-200 flex justify-end gap-3">

          <button
            @click="showStationModal = false"
            class="px-5 py-3 rounded-xl border border-slate-200 font-bold"
          >
            Cancel
          </button>

          <button
            @click="saveStation"
            class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold"
          >
            Save Changes
          </button>

        </div>

      </div>
    </div>

    <!-- RISK DETAILS MODAL -->
    <div
      v-if="showRiskModal && selectedRisk"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div class="bg-white rounded-2xl shadow-2xl w-full max-w-lg p-6">

        <div class="flex justify-between">

          <div>
            <p class="text-xs font-bold text-red-600">
              {{ selectedRisk.id }}
            </p>

            <h2 class="text-xl font-bold text-slate-900 mt-1">
              {{ selectedRisk.title }}
            </h2>
          </div>

          <button
            @click="showRiskModal = false"
            class="text-2xl text-slate-400"
          >
            ×
          </button>

        </div>

        <div class="mt-5">

          <span
            class="px-3 py-1 rounded-full text-xs font-bold"
            :class="riskBadgeClass(selectedRisk.severity)"
          >
            {{ selectedRisk.severity }} Risk
          </span>

          <p class="text-sm text-slate-600 mt-5">
            {{ selectedRisk.description }}
          </p>

          <p class="text-sm text-slate-500 mt-4">
            Status:
            <strong class="text-slate-800">
              {{ selectedRisk.status }}
            </strong>
          </p>

        </div>

        <div class="flex justify-end mt-6">

          <button
            @click="showRiskModal = false"
            class="px-5 py-3 rounded-xl bg-slate-100 font-bold"
          >
            Close
          </button>

        </div>

      </div>
    </div>

    <!-- PLAN DETAILS MODAL -->
    <div
      v-if="showPlanModal && selectedPlan"
      class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4"
    >

      <div class="bg-white rounded-2xl shadow-2xl w-full max-w-lg p-6">

        <div class="flex justify-between">

          <div>

            <p class="text-xs font-bold text-[#8B1E23]">
              {{ selectedPlan.priority }}
            </p>

            <h2 class="text-xl font-bold text-slate-900 mt-1">
              {{ selectedPlan.title }}
            </h2>

          </div>

          <button
            @click="showPlanModal = false"
            class="text-2xl text-slate-400"
          >
            ×
          </button>

        </div>

        <p class="text-sm text-slate-600 mt-5">
          {{ selectedPlan.description }}
        </p>

        <div class="mt-5">

          <span
            class="px-3 py-1 rounded-full text-xs font-bold"
            :class="
              selectedPlan.status === 'Completed'
                ? 'bg-green-100 text-green-700'
                : 'bg-yellow-100 text-yellow-700'
            "
          >
            {{ selectedPlan.status }}
          </span>

        </div>

        <div class="flex justify-end gap-3 mt-6">

          <button
            @click="showPlanModal = false"
            class="px-5 py-3 rounded-xl bg-slate-100 font-bold"
          >
            Close
          </button>

          <button
            @click="updatePlanStatus(selectedPlan); showPlanModal = false"
            class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold"
          >
            {{ selectedPlan.status === 'Completed' ? 'Reopen' : 'Complete' }}
          </button>

        </div>

      </div>
    </div>

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