```vue
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
            Manage your profile, security, and portal appearance.
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
                <span class="text-[#8B1E23]">*</span>
              </label>

              <input
                v-model="form.firstName"
                @input="markUnsaved"
                type="text"
                placeholder="Enter first name"
                class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none transition focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              />
            </div>


            <!-- Last Name -->
            <div>
              <label class="text-sm font-semibold text-slate-700">
                Last Name
                <span class="text-[#8B1E23]">*</span>
              </label>

              <input
                v-model="form.lastName"
                @input="markUnsaved"
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

              <select
                v-model="form.rank"
                @change="markUnsaved"
                required
                class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm outline-none transition focus:border-[#8B1E23] focus:ring-2 focus:ring-[#8B1E23]/10"
              >
                <option value="" disabled>Select rank</option>
                <option v-for="rank in rankOptions" :key="rank.code" :value="rank.code">{{ rank.code }} - {{ rank.title }}</option>
              </select>
            </div>


           

          </div>


          <div class="mt-5 flex justify-end gap-3">
            <button
              @click="resetChanges"
              class="px-5 py-3 rounded-xl border border-slate-300 bg-white text-sm font-semibold text-slate-700 hover:bg-slate-100 transition"
            >
              Reset Profile
            </button>
            <button
              @click="saveProfile"
              class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D] transition"
            >
              Save Profile
            </button>

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


          </div>

        </section>

      </div>


      <!-- =================================================== -->
      <!-- RIGHT COLUMN -->
      <!-- =================================================== -->

      <div class="space-y-6">

        <!-- ACCOUNT SUMMARY -->

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
                {{ form.rank || 'No rank' }}
              </p>

            </div>

          </div>


        

        </section>

      </div>

    </section>


    <!-- ===================================================== -->
    <!-- SETTINGS CENTER -->
    <!-- ===================================================== -->
    <section class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <div class="lg:col-span-2">
        <h3 class="text-xl font-bold text-slate-900">Preferences & Resources</h3>
        <p class="text-sm text-slate-500 mt-1">Configure the portal, manage your data, and find support.</p>
      </div>

      <section class="lg:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
        <div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4 border-b border-slate-200 pb-4">
          <div>
            <h3 class="text-lg font-bold text-slate-900">Appearance</h3>
            <p class="text-sm text-slate-500 mt-1">Choose how the Personnel Portal looks.</p>
          </div>
          <span v-if="appearanceHasChanges" class="text-sm font-semibold text-amber-700">Unsaved appearance changes</span>
        </div>
        <div class="mt-5 grid grid-cols-1 sm:grid-cols-2 gap-4">
          <label class="text-sm font-semibold text-slate-700">Theme
            <select v-model="appearanceDraft.theme" class="w-full mt-2 px-3 py-2.5 rounded-xl border border-slate-300 bg-white">
              <option value="light">Light</option>
              <option value="dark">Dark</option>
              <option value="system">System Default</option>
            </select>
          </label>
          <label class="text-sm font-semibold text-slate-700">Font Size
            <select v-model="appearanceDraft.fontSize" class="w-full mt-2 px-3 py-2.5 rounded-xl border border-slate-300 bg-white">
              <option value="small">Small</option>
              <option value="medium">Medium</option>
              <option value="large">Large</option>
              <option value="xlarge">Extra Large</option>
            </select>
          </label>
        </div>
        <div class="mt-5 flex justify-end">
          <button @click="saveAppearance" :disabled="!appearanceHasChanges" class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D] transition disabled:cursor-not-allowed disabled:opacity-50">
            Save Appearance
          </button>
        </div>
      </section>

      <section class="bg-[#8B1E23] rounded-2xl shadow-sm p-6 text-white lg:col-span-2"><p class="text-xs uppercase tracking-wide text-red-100">About FireNotify</p><h3 class="text-2xl font-bold mt-1">FIRENOTIFY</h3><p class="text-sm text-red-100 mt-1">Personnel Portal</p><div class="grid grid-cols-2 sm:grid-cols-3 gap-4 mt-5 pt-4 border-t border-white/20 text-sm"><div><p class="text-red-100">Version</p><p class="font-bold mt-1">{{ appVersion }}</p></div><div><p class="text-red-100">Environment</p><p class="font-bold mt-1">Frontend</p></div><div><p class="text-red-100">Technology</p><p class="font-bold mt-1">Vue + Vite</p></div></div></section>
    </section>

    <!-- ===================================================== -->
    <!-- CHANGE PASSWORD MODAL -->
    <!-- ===================================================== -->

    <div
      v-if="showPasswordModal"
      class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 p-4"
      @click.self="showPasswordModal = false"
    >

      <div class="fn-modal-panel w-full max-w-md bg-white rounded-2xl shadow-xl overflow-hidden">

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

          <div>

            <label class="text-sm font-semibold text-slate-700">
              Current Password
              <span class="text-[#8B1E23]">*</span>
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


          <div>

            <label class="text-sm font-semibold text-slate-700">
              New Password
              <span class="text-[#8B1E23]">*</span>
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


          <div>

            <label class="text-sm font-semibold text-slate-700">
              Confirm New Password
              <span class="text-[#8B1E23]">*</span>
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
import packageInfo from '../../../package.json'
import {
  getPersonnelSettings,
  savePersonnelSettings
} from '../../utils/personnelSettings.js'

const API_URL = 'http://127.0.0.1:8000/api'
const rankOptions = [
  { code: 'FO1', title: 'Fire Officer I' },
  { code: 'FO2', title: 'Fire Officer II' },
  { code: 'FO3', title: 'Fire Officer III' },
  { code: 'SFO1', title: 'Senior Fire Officer I' },
  { code: 'SFO2', title: 'Senior Fire Officer II' },
  { code: 'SFO3', title: 'Senior Fire Officer III' },
  { code: 'SFO4', title: 'Senior Fire Officer IV' },
  { code: 'FINSP', title: 'Fire Inspector' },
  { code: 'FSINSP', title: 'Fire Senior Inspector' },
  { code: 'FCINSP', title: 'Fire Chief Inspector' }
]


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
// EMITS
// ============================================================

const emit = defineEmits(['update-user', 'open-support'])


// ============================================================
// STORAGE
// ============================================================

const SETTINGS_KEY_PREFIX = 'fireNotifyPersonnelSettings_'


// ============================================================
// PROFILE
// ============================================================

const form = ref({
  firstName: '',
  lastName: '',
  rank: '',

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
const portalSettings = ref(getPersonnelSettings())
const appearanceDraft = ref({
  theme: portalSettings.value.theme,
  fontSize: portalSettings.value.fontSize
})
const appVersion = packageInfo.version || 'Not available'

let toastTimer = null

const appearanceHasChanges = computed(() =>
  appearanceDraft.value.theme !== portalSettings.value.theme
  || appearanceDraft.value.fontSize !== portalSettings.value.fontSize
)

const saveAppearance = () => {
  portalSettings.value = savePersonnelSettings(appearanceDraft.value)
  showToast('Appearance saved.')
}

const exportMyData = () => {
  const userId = props.currentUser?.id || props.currentUser?.identifier || props.currentUser?.email
  const tickets = JSON.parse(localStorage.getItem('firenotify_support_tickets') || '[]')
    .filter(ticket => String(ticket.userId) === String(userId))
  const notifications = JSON.parse(localStorage.getItem('firenotify_notifications') || '[]')
    .filter(item => String(item.recipientId || item.assignedToId) === String(userId))
  const blob = new Blob([JSON.stringify({ profile: props.currentUser, settings: portalSettings.value, tickets, notifications }, null, 2)], { type: 'application/json' })
  const url = URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.href = url
  link.download = 'firenotify-my-data.json'
  link.click()
  URL.revokeObjectURL(url)
  showToast('Your data export is ready.')
}


// ============================================================
// COMPUTED
// ============================================================

const fullName = computed(() => {
  const first = form.value.firstName?.trim() || ''
  const last = form.value.lastName?.trim() || ''

  return `${first} ${last}`.trim() || 'User'
})


// ============================================================
// USER STORAGE KEY
// ============================================================

const getUserStorageKey = () => {
  const identifier =
    props.currentUser?.identifier ||
    props.currentUser?.email ||
    props.currentUser?.username ||
    props.currentUser?.id ||
    'current'

  return `${SETTINGS_KEY_PREFIX}${identifier}`
}


// ============================================================
// INITIALIZE USER
// ============================================================

const initializeUser = () => {

  if (!props.currentUser) {
    return
  }

  form.value.firstName =
    props.currentUser.firstName || ''

  form.value.lastName =
    props.currentUser.lastName || ''

  form.value.rank =
    props.currentUser.rank || ''

  form.value.station =
    props.currentUser.station || ''
}


// ============================================================
// LOAD SAVED SETTINGS
// ============================================================

const loadSavedProfile = () => {
  try {
    const saved = JSON.parse(localStorage.getItem(getUserStorageKey()) || '{}')
    if (saved.form) form.value = { ...form.value, ...saved.form }
  } catch (error) {
    console.error('Failed to load personnel profile settings:', error)
  }
}


// ============================================================
// SAVE SETTINGS
// ============================================================

const saveSettings = () => {

  const profile = {
    firstName: form.value.firstName.trim(),
    lastName: form.value.lastName.trim(),
    rank: form.value.rank.trim(),
    station: form.value.station.trim()
  }
  localStorage.setItem(getUserStorageKey(), JSON.stringify({ form: profile }))
}


// ============================================================
// SAVE PROFILE
// ============================================================

const saveProfile = async () => {
  const firstName = form.value.firstName.trim()
  const lastName = form.value.lastName.trim()

  if (!firstName || !lastName) {
    showToast('Please enter your first and last name.')
    return
  }

  if (!rankOptions.some(rank => rank.code === form.value.rank)) {
    showToast('Please select a valid personnel rank.')
    return
  }

  const userId = props.currentUser?.id
  if (!userId) {
    showToast('Unable to identify your personnel account.')
    return
  }

  try {
    const csrfToken = document.cookie.split('; ').find(item => item.startsWith('csrftoken='))?.split('=')[1] || ''
    const response = await fetch(`${API_URL}/users/${userId}/profile/`, {
      method: 'PATCH',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify({
        first_name: firstName,
        last_name: lastName,
        rank: form.value.rank
      })
    })
    const data = await response.json().catch(() => ({}))

    if (!response.ok) {
      throw new Error(data.error || 'Unable to update personnel rank.')
    }

    form.value.rank = data.user.rank
    saveSettings()
    emit('update-user', {
      ...props.currentUser,
      firstName: data.user.first_name,
      lastName: data.user.last_name,
      name: `${data.user.first_name} ${data.user.last_name}`.trim(),
      rank: data.user.rank,
      station: form.value.station || ''
    })
    hasUnsavedChanges.value = false
    showToast('Profile updated successfully.')
  } catch (error) {
    showToast(error.message || 'Unable to update personnel rank.')
  }
}


// ============================================================
// ============================================================
// RESET
// ============================================================

const resetChanges = () => {
  initializeUser()
  hasUnsavedChanges.value = false
  showToast('Profile changes discarded.')
}


// ============================================================
// PASSWORD
// ============================================================

const changePassword = () => {

  passwordError.value = ''

  if (!passwordForm.value.current) {

    passwordError.value =
      'Enter your current password.'

    return
  }

  const storedPassword = String(props.currentUser?.password || '')

  if (!storedPassword) {
    passwordError.value =
      'Password changes are not available for this account.'

    return
  }

  if (passwordForm.value.current !== storedPassword) {
    passwordError.value =
      'Current password is incorrect.'

    return
  }


  if (!passwordForm.value.newPassword) {

    passwordError.value =
      'Enter a new password.'

    return
  }


  if (
    passwordForm.value.newPassword.length < 8
  ) {

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

  emit('update-user', {
    ...props.currentUser,
    password: passwordForm.value.newPassword
  })


  closePasswordModal()

  showToast(
    'Password updated successfully.'
  )
}


// ============================================================
// CLOSE PASSWORD MODAL
// ============================================================

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
  loadSavedProfile()

  hasUnsavedChanges.value = false

})
</script>
