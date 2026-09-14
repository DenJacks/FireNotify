<template>
  <div class="w-full min-w-0 space-y-6">

    <!-- ===================================================== -->
    <!-- PAGE HEADER -->
    <!-- ===================================================== -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">
        <div>
          <p class="text-sm font-semibold text-[#8B1E23]">
            FIRENOTIFY PERSONNEL PORTAL
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Settings
          </h2>

          <p class="text-sm text-slate-500 mt-1">
            Manage your account, notifications, security, and portal preferences.
          </p>
        </div>

        <div class="h-14 w-14 rounded-2xl bg-[#8B1E23]/10 flex items-center justify-center">
          <span
            v-html="ICONS.settings"
            class="h-8 w-8 text-[#8B1E23]"
          ></span>
        </div>
      </div>
    </section>


    <!-- ===================================================== -->
    <!-- MAIN SETTINGS -->
    <!-- ===================================================== -->
    <section class="grid grid-cols-1 xl:grid-cols-3 gap-6">

      <!-- =================================================== -->
      <!-- LEFT / MAIN COLUMN -->
      <!-- =================================================== -->
      <div class="xl:col-span-2 space-y-6">

        <!-- ================================================= -->
        <!-- PROFILE INFORMATION -->
        <!-- ================================================= -->
        <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <div class="border-b border-slate-200 pb-4">
            <div class="flex items-center justify-between gap-4">
              <div>
                <h3 class="text-lg font-bold text-slate-900">
                  Profile Information
                </h3>

                <p class="text-sm text-slate-500 mt-1">
                  Update the information shown on your personnel account.
                </p>
              </div>

              <span
                v-if="hasUnsavedChanges"
                class="hidden sm:inline-flex px-3 py-1.5 rounded-full bg-amber-50 text-amber-700 text-xs font-bold"
              >
                Unsaved changes
              </span>
            </div>
          </div>


          <div class="mt-5 grid grid-cols-1 sm:grid-cols-2 gap-4">

            <!-- First Name -->
            <div>
              <label class="text-sm font-semibold text-slate-700">
                First Name
              </label>

              <input
                v-model="form.firstName"
                type="text"
                placeholder="Enter first name"
                class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none transition focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              />
            </div>


            <!-- Last Name -->
            <div>
              <label class="text-sm font-semibold text-slate-700">
                Last Name
              </label>

              <input
                v-model="form.lastName"
                type="text"
                placeholder="Enter last name"
                class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none transition focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              />
            </div>


            <!-- Rank -->
            <div>
              <label class="text-sm font-semibold text-slate-700">
                Rank
              </label>

              <input
                v-model="form.rank"
                type="text"
                placeholder="e.g. FO3"
                class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none transition focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              />
            </div>


            <!-- Position -->
            <div>
              <label class="text-sm font-semibold text-slate-700">
                Position
              </label>

              <input
                v-model="form.position"
                type="text"
                placeholder="Enter position"
                class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none transition focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              />
            </div>


            <!-- Station -->
            <div class="sm:col-span-2">
              <label class="text-sm font-semibold text-slate-700">
                Station
              </label>

              <input
                v-model="form.station"
                type="text"
                placeholder="Enter station"
                class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none transition focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              />
            </div>

          </div>


          <div class="mt-5 flex justify-end">
            <button
              @click="saveProfile"
              class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D] transition"
            >
              Save Profile
            </button>
          </div>

        </section>


        <!-- ================================================= -->
        <!-- NOTIFICATION PREFERENCES -->
        <!-- ================================================= -->
        <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <div class="border-b border-slate-200 pb-4">
            <h3 class="text-lg font-bold text-slate-900">
              Notification Preferences
            </h3>

            <p class="text-sm text-slate-500 mt-1">
              Choose which alerts you receive in the portal.
            </p>
          </div>


          <div class="mt-5 divide-y divide-slate-100">

            <div
              v-for="item in notificationPreferences"
              :key="item.key"
              class="flex items-center justify-between gap-5 py-4 first:pt-0 last:pb-0"
            >

              <div>
                <p class="text-sm font-semibold text-slate-800">
                  {{ item.title }}
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  {{ item.description }}
                </p>
              </div>


              <!-- Toggle -->
              <button
                type="button"
                @click="item.enabled = !item.enabled"
                :aria-pressed="item.enabled"
                class="relative flex-shrink-0 w-12 h-7 rounded-full transition"
                :class="item.enabled ? 'bg-[#8B1E23]' : 'bg-slate-300'"
              >

                <span
                  class="absolute top-1 h-5 w-5 rounded-full bg-white shadow transition"
                  :class="item.enabled ? 'left-6' : 'left-1'"
                ></span>

              </button>

            </div>

          </div>

        </section>


        <!-- ================================================= -->
        <!-- SECURITY -->
        <!-- ================================================= -->
        <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <div class="border-b border-slate-200 pb-4">
            <h3 class="text-lg font-bold text-slate-900">
              Security
            </h3>

            <p class="text-sm text-slate-500 mt-1">
              Keep your personnel account protected.
            </p>
          </div>


          <div class="mt-5 space-y-4">

            <!-- Password -->
            <div
              class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 p-4 rounded-xl bg-slate-50 border border-slate-200"
            >

              <div>
                <p class="text-sm font-semibold text-slate-800">
                  Password
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  Keep your password secure and update it regularly.
                </p>
              </div>

              <button
                @click="showPasswordModal = true"
                class="px-4 py-2 rounded-xl border border-slate-300 bg-white text-sm font-semibold text-slate-700 hover:bg-slate-100 transition"
              >
                Change Password
              </button>

            </div>


            <!-- 2FA -->
            <div
              class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 p-4 rounded-xl bg-green-50 border border-green-100"
            >

              <div>
                <p class="text-sm font-semibold text-slate-800">
                  Two-factor authentication
                </p>

                <p class="text-xs text-green-700 mt-1">
                  Your account is protected with 2FA.
                </p>
              </div>

              <span
                class="px-3 py-1.5 rounded-full bg-green-100 text-green-700 text-xs font-bold"
              >
                Enabled
              </span>

            </div>

          </div>

        </section>

      </div>


      <!-- =================================================== -->
      <!-- RIGHT COLUMN -->
      <!-- =================================================== -->
      <div class="space-y-6">

        <!-- ================================================= -->
        <!-- PORTAL PREFERENCES -->
        <!-- ================================================= -->
        <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <h3 class="text-lg font-bold text-slate-900">
            Portal Preferences
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            Customize your portal experience.
          </p>


          <div class="mt-5 space-y-5">

            <!-- Language -->
            <div>
              <label class="text-sm font-semibold text-slate-700">
                Language
              </label>

              <select
                v-model="preferences.language"
                class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm outline-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              >
                <option>English</option>
                <option>Filipino</option>
              </select>
            </div>


            <!-- Time Zone -->
            <div>
              <label class="text-sm font-semibold text-slate-700">
                Time Zone
              </label>

              <select
                v-model="preferences.timezone"
                class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm outline-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              >
                <option>Asia/Manila (UTC+8)</option>
                <option>UTC</option>
              </select>
            </div>


            <!-- Default Landing Page -->
            <div>
              <label class="text-sm font-semibold text-slate-700">
                Default Landing Page
              </label>

              <select
                v-model="preferences.landingPage"
                class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm outline-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              >
                <option>Dashboard</option>
                <option>Tasks</option>
                <option>Activities</option>
                <option>Reports</option>
                <option>Notifications</option>
              </select>
            </div>

          </div>

        </section>


        <!-- ================================================= -->
        <!-- DISPLAY -->
        <!-- ================================================= -->
        <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <h3 class="text-lg font-bold text-slate-900">
            Display
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            Adjust how the portal looks on your device.
          </p>


          <div class="mt-5 space-y-5">

            <!-- Compact Sidebar -->
            <div class="flex items-center justify-between gap-5">

              <div>
                <p class="text-sm font-semibold text-slate-800">
                  Compact sidebar
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  Use a smaller navigation layout.
                </p>
              </div>

              <button
                type="button"
                @click="display.compactSidebar = !display.compactSidebar"
                class="relative flex-shrink-0 w-12 h-7 rounded-full transition"
                :class="display.compactSidebar ? 'bg-[#8B1E23]' : 'bg-slate-300'"
              >
                <span
                  class="absolute top-1 h-5 w-5 rounded-full bg-white shadow transition"
                  :class="display.compactSidebar ? 'left-6' : 'left-1'"
                ></span>
              </button>

            </div>


            <!-- Reduced Motion -->
            <div class="flex items-center justify-between gap-5">

              <div>
                <p class="text-sm font-semibold text-slate-800">
                  Reduced motion
                </p>

                <p class="text-xs text-slate-500 mt-1">
                  Minimize interface transitions.
                </p>
              </div>

              <button
                type="button"
                @click="display.reducedMotion = !display.reducedMotion"
                class="relative flex-shrink-0 w-12 h-7 rounded-full transition"
                :class="display.reducedMotion ? 'bg-[#8B1E23]' : 'bg-slate-300'"
              >
                <span
                  class="absolute top-1 h-5 w-5 rounded-full bg-white shadow transition"
                  :class="display.reducedMotion ? 'left-6' : 'left-1'"
                ></span>
              </button>

            </div>

          </div>

        </section>


        <!-- ================================================= -->
        <!-- ACCOUNT SUMMARY -->
        <!-- ================================================= -->
        <section class="bg-[#8B1E23] rounded-2xl shadow-sm p-6 text-white">

          <div class="flex items-center gap-4">

            <div
              class="h-12 w-12 rounded-xl bg-white/10 flex items-center justify-center text-lg font-bold"
            >
              {{ getInitials() }}
            </div>

            <div>
              <p class="font-bold">
                {{ fullName }}
              </p>

              <p class="text-xs text-white/70 mt-1">
                {{ form.rank }} • {{ form.position }}
              </p>
            </div>

          </div>


          <div class="mt-5 pt-5 border-t border-white/10">

            <p class="text-xs text-white/60">
              Assigned Station
            </p>

            <p class="text-sm font-semibold mt-1">
              {{ form.station }}
            </p>

          </div>

        </section>

      </div>

    </section>


    <!-- ===================================================== -->
    <!-- SAVE CHANGES -->
    <!-- ===================================================== -->
    <section
      class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 bg-white border border-slate-200 rounded-2xl shadow-sm p-6"
    >

      <div>
        <h3 class="text-lg font-bold text-slate-900">
          Save your changes
        </h3>

        <p class="text-sm text-slate-500 mt-1">
          Profile and preference updates apply to this account.
        </p>
      </div>


      <div class="flex gap-3">

        <button
          @click="resetChanges"
          class="px-5 py-3 rounded-xl border border-slate-300 bg-white text-sm font-semibold text-slate-700 hover:bg-slate-100 transition"
        >
          Reset
        </button>

        <button
          @click="saveAllChanges"
          class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D] transition"
        >
          Save Changes
        </button>

      </div>

    </section>


    <!-- ===================================================== -->
    <!-- CHANGE PASSWORD MODAL -->
    <!-- ===================================================== -->
    <div
      v-if="showPasswordModal"
      class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 p-4"
      @click.self="showPasswordModal = false"
    >

      <div class="w-full max-w-md bg-white rounded-2xl shadow-xl overflow-hidden">

        <div class="px-6 py-5 border-b border-slate-200">

          <div class="flex items-center justify-between">

            <div>
              <h3 class="text-lg font-bold text-slate-900">
                Change Password
              </h3>

              <p class="text-sm text-slate-500 mt-1">
                Update your personnel account password.
              </p>
            </div>

            <button
              @click="showPasswordModal = false"
              class="h-9 w-9 rounded-lg hover:bg-slate-100 text-slate-500"
            >
              ✕
            </button>

          </div>

        </div>


        <div class="p-6 space-y-4">

          <!-- Current Password -->
          <div>
            <label class="text-sm font-semibold text-slate-700">
              Current Password
            </label>

            <div class="relative mt-2">

              <input
                v-model="passwordForm.current"
                :type="showCurrentPassword ? 'text' : 'password'"
                class="w-full px-4 py-3 pr-12 rounded-xl border border-slate-300 text-sm outline-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              />

              <button
                @click="showCurrentPassword = !showCurrentPassword"
                class="absolute right-3 top-1/2 -translate-y-1/2 text-xs font-semibold text-slate-500"
              >
                {{ showCurrentPassword ? 'Hide' : 'Show' }}
              </button>

            </div>
          </div>


          <!-- New Password -->
          <div>
            <label class="text-sm font-semibold text-slate-700">
              New Password
            </label>

            <div class="relative mt-2">

              <input
                v-model="passwordForm.newPassword"
                :type="showNewPassword ? 'text' : 'password'"
                class="w-full px-4 py-3 pr-12 rounded-xl border border-slate-300 text-sm outline-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              />

              <button
                @click="showNewPassword = !showNewPassword"
                class="absolute right-3 top-1/2 -translate-y-1/2 text-xs font-semibold text-slate-500"
              >
                {{ showNewPassword ? 'Hide' : 'Show' }}
              </button>

            </div>
          </div>


          <!-- Confirm Password -->
          <div>
            <label class="text-sm font-semibold text-slate-700">
              Confirm New Password
            </label>

            <input
              v-model="passwordForm.confirmPassword"
              type="password"
              class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
            />
          </div>


          <p
            v-if="passwordError"
            class="text-sm text-red-600 bg-red-50 border border-red-100 rounded-xl px-4 py-3"
          >
            {{ passwordError }}
          </p>

        </div>


        <div class="px-6 py-5 border-t border-slate-200 flex justify-end gap-3">

          <button
            @click="closePasswordModal"
            class="px-4 py-2.5 rounded-xl border border-slate-300 text-sm font-semibold text-slate-700 hover:bg-slate-100"
          >
            Cancel
          </button>

          <button
            @click="changePassword"
            class="px-4 py-2.5 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]"
          >
            Update Password
          </button>

        </div>

      </div>

    </div>


    <!-- ===================================================== -->
    <!-- TOAST -->
    <!-- ===================================================== -->
    <transition
      enter-active-class="transition duration-200"
      enter-from-class="opacity-0 translate-y-2"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition duration-200"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >

      <div
        v-if="toastMessage"
        class="fixed bottom-6 right-6 z-[60] bg-slate-900 text-white px-5 py-3 rounded-xl shadow-lg text-sm font-semibold"
      >
        ✓ {{ toastMessage }}
      </div>

    </transition>

  </div>
</template>


<script setup>
import { computed, onMounted, ref } from 'vue'


// ============================================================
// PROPS
// ============================================================

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


// ============================================================
// STORAGE
// ============================================================

const SETTINGS_KEY = 'fireNotifyPersonnelSettings'


// ============================================================
// PROFILE
// ============================================================

const form = ref({
  firstName: 'Juan',
  lastName: 'Dela Cruz',
  rank: 'FO3',
  position: 'Station Inspector',
  station: 'BFP Balingasag'
})


// ============================================================
// NOTIFICATIONS
// ============================================================

const notificationPreferences = ref([
  {
    key: 'taskReminders',
    title: 'Task reminders',
    description: 'Receive alerts for assigned tasks and deadlines.',
    enabled: true
  },
  {
    key: 'reportNotifications',
    title: 'Report notifications',
    description: 'Be notified when reports are submitted or returned.',
    enabled: true
  },
  {
    key: 'activityReminders',
    title: 'Activity reminders',
    description: 'Receive reminders for scheduled station activities.',
    enabled: true
  },
  {
    key: 'emailNotifications',
    title: 'Email notifications',
    description: 'Send important updates to your registered email.',
    enabled: false
  }
])


// ============================================================
// PORTAL PREFERENCES
// ============================================================

const preferences = ref({
  language: 'English',
  timezone: 'Asia/Manila (UTC+8)',
  landingPage: 'Dashboard'
})


// ============================================================
// DISPLAY
// ============================================================

const display = ref({
  compactSidebar: false,
  reducedMotion: false
})


// ============================================================
// PASSWORD
// ============================================================

const showPasswordModal = ref(false)
const showCurrentPassword = ref(false)
const showNewPassword = ref(false)

const passwordError = ref('')

const passwordForm = ref({
  current: '',
  newPassword: '',
  confirmPassword: ''
})


// ============================================================
// UI
// ============================================================

const toastMessage = ref('')
const hasUnsavedChanges = ref(false)

let toastTimer = null


// ============================================================
// COMPUTED
// ============================================================

const fullName = computed(() => {
  return `${form.value.firstName} ${form.value.lastName}`.trim()
})


// ============================================================
// INITIALIZE FROM CURRENT USER
// ============================================================

const initializeUser = () => {
  if (!props.currentUser) return

  form.value.firstName =
    props.currentUser.firstName || form.value.firstName

  form.value.lastName =
    props.currentUser.lastName || form.value.lastName

  form.value.rank =
    props.currentUser.rank || form.value.rank

  form.value.position =
    props.currentUser.position || form.value.position

  form.value.station =
    props.currentUser.station || form.value.station
}


// ============================================================
// LOAD SAVED SETTINGS
// ============================================================

const loadSettings = () => {
  const saved = localStorage.getItem(SETTINGS_KEY)

  if (!saved) return

  try {
    const settings = JSON.parse(saved)

    if (settings.form) {
      form.value = {
        ...form.value,
        ...settings.form
      }
    }

    if (settings.notificationPreferences) {
      notificationPreferences.value =
        settings.notificationPreferences
    }

    if (settings.preferences) {
      preferences.value = {
        ...preferences.value,
        ...settings.preferences
      }
    }

    if (settings.display) {
      display.value = {
        ...display.value,
        ...settings.display
      }
    }

  } catch (error) {
    console.error('Failed to load personnel settings:', error)
  }
}


// ============================================================
// SAVE SETTINGS
// ============================================================

const saveSettings = () => {
  const settings = {
    form: form.value,
    notificationPreferences: notificationPreferences.value,
    preferences: preferences.value,
    display: display.value
  }

  localStorage.setItem(
    SETTINGS_KEY,
    JSON.stringify(settings)
  )

  hasUnsavedChanges.value = false
}


// ============================================================
// SAVE PROFILE
// ============================================================

const saveProfile = () => {

  if (!form.value.firstName.trim()) {
    showToast('First name is required.')
    return
  }

  if (!form.value.lastName.trim()) {
    showToast('Last name is required.')
    return
  }

  saveSettings()

  showToast('Profile information saved successfully.')
}


// ============================================================
// SAVE ALL
// ============================================================

const saveAllChanges = () => {

  if (!form.value.firstName.trim() || !form.value.lastName.trim()) {
    showToast('Please complete your profile information.')
    return
  }

  saveSettings()

  showToast('All settings saved successfully.')
}


// ============================================================
// RESET
// ============================================================

const resetChanges = () => {

  initializeUser()

  notificationPreferences.value = [
    {
      key: 'taskReminders',
      title: 'Task reminders',
      description: 'Receive alerts for assigned tasks and deadlines.',
      enabled: true
    },
    {
      key: 'reportNotifications',
      title: 'Report notifications',
      description: 'Be notified when reports are submitted or returned.',
      enabled: true
    },
    {
      key: 'activityReminders',
      title: 'Activity reminders',
      description: 'Receive reminders for scheduled station activities.',
      enabled: true
    },
    {
      key: 'emailNotifications',
      title: 'Email notifications',
      description: 'Send important updates to your registered email.',
      enabled: false
    }
  ]

  preferences.value = {
    language: 'English',
    timezone: 'Asia/Manila (UTC+8)',
    landingPage: 'Dashboard'
  }

  display.value = {
    compactSidebar: false,
    reducedMotion: false
  }

  hasUnsavedChanges.value = false

  showToast('Settings have been reset.')
}


// ============================================================
// PASSWORD
// ============================================================

const changePassword = () => {

  passwordError.value = ''

  if (!passwordForm.value.current) {
    passwordError.value = 'Enter your current password.'
    return
  }

  if (!passwordForm.value.newPassword) {
    passwordError.value = 'Enter a new password.'
    return
  }

  if (passwordForm.value.newPassword.length < 8) {
    passwordError.value =
      'New password must contain at least 8 characters.'
    return
  }

  if (
    passwordForm.value.newPassword !==
    passwordForm.value.confirmPassword
  ) {
    passwordError.value =
      'New passwords do not match.'
    return
  }

  /*
   * Frontend demo only.
   * Real password changes should be handled by Django
   * using authenticated backend endpoints.
   */

  closePasswordModal()

  showToast('Password updated successfully.')
}


const closePasswordModal = () => {

  showPasswordModal.value = false

  passwordForm.value = {
    current: '',
    newPassword: '',
    confirmPassword: ''
  }

  passwordError.value = ''
  showCurrentPassword.value = false
  showNewPassword.value = false
}


// ============================================================
// TOAST
// ============================================================

const showToast = (message) => {

  toastMessage.value = message

  clearTimeout(toastTimer)

  toastTimer = setTimeout(() => {
    toastMessage.value = ''
  }, 3000)
}


// ============================================================
// INITIALS
// ============================================================

const getInitials = () => {

  const first =
    form.value.firstName?.charAt(0) || ''

  const last =
    form.value.lastName?.charAt(0) || ''

  return `${first}${last}`.toUpperCase()
}


// ============================================================
// TRACK CHANGES
// ============================================================

const markUnsaved = () => {
  hasUnsavedChanges.value = true
}


// ============================================================
// LIFECYCLE
// ============================================================

onMounted(() => {
  initializeUser()
  loadSettings()

  // Reset initial state after loading.
  hasUnsavedChanges.value = false
})
</script>