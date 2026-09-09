<template>
  <div
    class="min-h-screen w-full bg-slate-100 flex items-center justify-center p-4 sm:p-6 lg:p-10 font-sans"
  >

    <!-- MAIN CARD -->
    <div
      class="w-full max-w-6xl bg-white rounded-2xl shadow-xl overflow-hidden border border-slate-200"
    >

      <!-- TOP HEADER -->
      <div class="bg-[#8B1E23] text-white px-6 sm:px-8 py-5">
        <div class="flex items-center gap-4">

          <!-- FIRE ICON -->
          <div
            class="w-14 h-14 rounded-xl bg-white flex items-center justify-center shadow-md flex-shrink-0"
          >
            <svg
              class="w-8 h-8 text-[#8B1E23]"
              viewBox="0 0 24 24"
              fill="currentColor"
            >
              <path
                d="M13.5 2.5c.3 3.2-1.5 5.1-3.1 7-1.3 1.5-2.5 3-2.5 5.3
                0 1.8.8 3.4 2.1 4.5-.1-.4-.2-.9-.2-1.4
                0-1.7 1-3.1 2.5-4.2.7-.5 1.5-1.1 2.1-2
                .5 1.1.8 2.2.8 3.4 0 1.7-.7 3.2-1.8 4.3
                3.2-.9 5.6-3.8 5.6-7.3 0-4.3-3.2-7.5-5.5-9.6z"
              />
            </svg>
          </div>

          <div>
            <h1 class="text-2xl sm:text-3xl font-bold tracking-wide">
              FIRE<span class="text-[#F5C542]">NOTIFY</span>
            </h1>

            <p class="text-sm sm:text-base text-white/90 mt-1">
              Bureau of Fire Protection
            </p>
          </div>

        </div>
      </div>


      <!-- CONTENT -->
      <div class="grid lg:grid-cols-[0.9fr_1.1fr]">

        <!-- LEFT INFORMATION PANEL -->
        <div
          class="hidden lg:flex bg-slate-50 border-r border-slate-200 p-10 flex-col justify-between"
        >

          <div>

            <div
              class="inline-flex items-center gap-2 px-4 py-2 rounded-lg bg-red-50 border border-red-200 text-[#8B1E23]"
            >
              <span
                class="w-3 h-3 rounded-full bg-green-500"
              ></span>

              <span class="text-sm font-semibold">
                Secure Personnel Portal
              </span>
            </div>


            <h2
              class="mt-8 text-3xl font-bold text-slate-800 leading-tight"
            >
              Operations Compliance
              <br />
              Monitoring System
            </h2>


            <p
              class="mt-5 text-lg leading-8 text-slate-600"
            >
              FireNotify helps BFP personnel manage assigned
              activities, reports, deadlines, and operational
              compliance in one place.
            </p>


            <!-- FEATURES -->
            <div class="mt-8 space-y-5">

              <div class="flex items-start gap-4">

                <div
                  class="w-11 h-11 rounded-lg bg-red-100 flex items-center justify-center flex-shrink-0"
                >
                  <svg
                    class="w-6 h-6 text-[#8B1E23]"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M9 12l2 2 4-4"
                    />
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M12 3l7 4v5c0 4.5-3 7.8-7 9-4-1.2-7-4.5-7-9V7l7-4z"
                    />
                  </svg>
                </div>

                <div>
                  <h3 class="font-bold text-lg text-slate-800">
                    Track Compliance
                  </h3>

                  <p class="text-base text-slate-600 mt-1">
                    Monitor assigned activities and report submissions.
                  </p>
                </div>

              </div>


              <div class="flex items-start gap-4">

                <div
                  class="w-11 h-11 rounded-lg bg-amber-100 flex items-center justify-center flex-shrink-0"
                >
                  <svg
                    class="w-6 h-6 text-amber-700"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M15 17h5l-1.5-1.5V11a6.5 6.5 0 00-13 0v4.5L4 17h5"
                    />
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M10 21h4"
                    />
                  </svg>
                </div>

                <div>
                  <h3 class="font-bold text-lg text-slate-800">
                    Receive Notifications
                  </h3>

                  <p class="text-base text-slate-600 mt-1">
                    Stay informed about deadlines and assigned tasks.
                  </p>
                </div>

              </div>


              <div class="flex items-start gap-4">

                <div
                  class="w-11 h-11 rounded-lg bg-green-100 flex items-center justify-center flex-shrink-0"
                >
                  <svg
                    class="w-6 h-6 text-green-700"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M9 17v-2a4 4 0 014-4h6"
                    />
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M15 7h6v6"
                    />
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M3 5h6v6"
                    />
                  </svg>
                </div>

                <div>
                  <h3 class="font-bold text-lg text-slate-800">
                    View Reports
                  </h3>

                  <p class="text-base text-slate-600 mt-1">
                    Access accomplishment and compliance reports.
                  </p>
                </div>

              </div>

            </div>

          </div>


          <!-- STATUS -->
          <div
            class="mt-10 bg-white rounded-xl border border-slate-200 p-5"
          >

            <div class="flex items-center justify-between">

              <span class="text-base font-semibold text-slate-700">
                System Status
              </span>

              <span
                class="flex items-center gap-2 text-green-700 font-semibold"
              >
                <span class="w-3 h-3 rounded-full bg-green-500"></span>
                Online
              </span>

            </div>

            <div
              class="grid grid-cols-3 mt-5 divide-x divide-slate-200"
            >

              <div class="text-center px-2">
                <p class="text-2xl font-bold text-[#8B1E23]">
                  48
                </p>

                <p class="text-sm text-slate-500 mt-1">
                  On Duty
                </p>
              </div>

              <div class="text-center px-2">
                <p class="text-2xl font-bold text-[#8B1E23]">
                  12
                </p>

                <p class="text-sm text-slate-500 mt-1">
                  Reports
                </p>
              </div>

              <div class="text-center px-2">
                <p class="text-2xl font-bold text-[#8B1E23]">
                  94.5%
                </p>

                <p class="text-sm text-slate-500 mt-1">
                  Readiness
                </p>
              </div>

            </div>

          </div>

        </div>


        <!-- RIGHT FORM PANEL -->
        <div class="p-6 sm:p-8 lg:p-12">

          <!-- TITLE -->
          <div class="mb-8">

            <p
              class="text-sm font-semibold text-[#8B1E23] uppercase tracking-wide"
            >
              Personnel Access
            </p>

            <h2
              class="mt-2 text-3xl font-bold text-slate-800"
            >
              {{ isLogin ? 'Welcome Back' : 'Create Your Account' }}
            </h2>

            <p class="mt-2 text-base text-slate-600">
              {{
                isLogin
                  ? 'Sign in to access your FireNotify account.'
                  : 'Register your BFP personnel account.'
              }}
            </p>

          </div>


          <!-- TABS -->
          <div
            class="grid grid-cols-2 border-b-2 border-slate-200 mb-8"
          >

            <button
              @click="switchToLogin"
              type="button"
              class="py-4 text-base sm:text-lg font-bold transition-colors"
              :class="
                isLogin
                  ? 'text-[#8B1E23] border-b-4 border-[#8B1E23] -mb-[2px]'
                  : 'text-slate-500 hover:text-slate-700'
              "
            >
              Sign In
            </button>


            <button
              @click="switchToRegister"
              type="button"
              class="py-4 text-base sm:text-lg font-bold transition-colors"
              :class="
                !isLogin
                  ? 'text-[#8B1E23] border-b-4 border-[#8B1E23] -mb-[2px]'
                  : 'text-slate-500 hover:text-slate-700'
              "
            >
              Register
            </button>

          </div>


          <!-- ERROR MESSAGE -->
          <div
            v-if="errorMessage"
            class="mb-6 flex items-start gap-3 rounded-lg border border-red-200 bg-red-50 px-4 py-4"
          >

            <svg
              class="w-6 h-6 text-red-600 flex-shrink-0"
              viewBox="0 0 24 24"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M12 2a10 10 0 100 20 10 10 0 000-20zm1 14a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V8a1 1 0 00-1-1z"
                clip-rule="evenodd"
              />
            </svg>

            <span class="text-base font-medium text-red-700">
              {{ errorMessage }}
            </span>

          </div>


          <!-- SUCCESS MESSAGE -->
          <div
            v-else-if="successMessage"
            class="mb-6 flex items-start gap-3 rounded-lg border border-green-200 bg-green-50 px-4 py-4"
          >

            <svg
              class="w-6 h-6 text-green-600 flex-shrink-0"
              viewBox="0 0 24 24"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M12 2a10 10 0 100 20 10 10 0 000-20zm5 7l-6 6-3-3 1.4-1.4L11 12.2l4.6-4.6L17 9z"
                clip-rule="evenodd"
              />
            </svg>

            <span class="text-base font-medium text-green-700">
              {{ successMessage }}
            </span>

          </div>


          <!-- ========================= -->
          <!-- LOGIN FORM -->
          <!-- ========================= -->

          <form
            v-if="isLogin"
            @submit.prevent="handleLogin"
            class="space-y-6"
          >

            <!-- EMAIL -->
            <div>

              <label
                class="mb-2 block text-base font-semibold text-slate-700"
              >
                BFP Email Address
              </label>

              <input
                v-model="loginForm.identifier"
                type="email"
                required
                placeholder="Enter your BFP email"
                class="w-full h-14 rounded-lg border-2 border-slate-300 bg-white px-4 text-base text-slate-800 placeholder:text-slate-400 focus:border-[#8B1E23] focus:outline-none focus:ring-4 focus:ring-red-100 transition"
              />

            </div>


            <!-- PASSWORD -->
            <div>

              <div class="mb-2 flex items-center justify-between">

                <label
                  class="text-base font-semibold text-slate-700"
                >
                  Password
                </label>

                <button
                  type="button"
                  class="text-base font-semibold text-[#8B1E23] hover:underline"
                >
                  Forgot Password?
                </button>

              </div>


              <div class="relative">

                <input
                  v-model="loginForm.password"
                  :type="showLoginPassword ? 'text' : 'password'"
                  required
                  placeholder="Enter your password"
                  class="w-full h-14 rounded-lg border-2 border-slate-300 bg-white px-4 pr-20 text-base text-slate-800 placeholder:text-slate-400 focus:border-[#8B1E23] focus:outline-none focus:ring-4 focus:ring-red-100 transition"
                />

                <button
                  type="button"
                  @click="showLoginPassword = !showLoginPassword"
                  class="absolute right-4 top-1/2 -translate-y-1/2 text-base font-semibold text-[#8B1E23] hover:underline"
                >
                  {{ showLoginPassword ? 'Hide' : 'Show' }}
                </button>

              </div>

            </div>


            <!-- REMEMBER -->
            <label
              class="flex items-center gap-3 cursor-pointer text-base text-slate-700"
            >

              <input
                id="remember-me"
                v-model="loginForm.remember"
                type="checkbox"
                class="w-5 h-5 rounded border-slate-300 text-[#8B1E23] focus:ring-[#8B1E23]"
              />

              <span>
                Keep me logged in
              </span>

            </label>


            <!-- LOGIN BUTTON -->
            <button
              type="submit"
              class="w-full h-14 rounded-lg bg-[#8B1E23] text-white text-lg font-bold flex items-center justify-center gap-3 hover:bg-[#71181D] focus:outline-none focus:ring-4 focus:ring-red-200 transition shadow-md"
            >

              <svg
                class="w-6 h-6"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <rect
                  x="4"
                  y="10"
                  width="16"
                  height="11"
                  rx="2"
                />

                <path
                  d="M8 10V7a4 4 0 018 0v3"
                />
              </svg>

              Sign In

            </button>

          </form>


          <!-- ========================= -->
          <!-- REGISTER FORM -->
          <!-- ========================= -->

          <form
            v-else
            @submit.prevent="handleSignup"
            class="space-y-5"
          >

            <!-- FIRST / LAST NAME -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">

              <div>

                <label
                  class="mb-2 block text-base font-semibold text-slate-700"
                >
                  First Name
                </label>

                <input
                  v-model="signupForm.firstName"
                  type="text"
                  placeholder="Enter first name"
                  class="w-full h-14 rounded-lg border-2 border-slate-300 px-4 text-base text-slate-800 placeholder:text-slate-400 focus:border-[#8B1E23] focus:outline-none focus:ring-4 focus:ring-red-100 transition"
                />

              </div>


              <div>

                <label
                  class="mb-2 block text-base font-semibold text-slate-700"
                >
                  Last Name
                </label>

                <input
                  v-model="signupForm.lastName"
                  type="text"
                  placeholder="Enter last name"
                  class="w-full h-14 rounded-lg border-2 border-slate-300 px-4 text-base text-slate-800 placeholder:text-slate-400 focus:border-[#8B1E23] focus:outline-none focus:ring-4 focus:ring-red-100 transition"
                />

              </div>

            </div>


            <!-- EMAIL -->
            <div>

              <label
                class="mb-2 block text-base font-semibold text-slate-700"
              >
                BFP Email Address
              </label>

              <input
                v-model="signupForm.email"
                type="email"
                placeholder="officer@bfp.gov.ph"
                class="w-full h-14 rounded-lg border-2 border-slate-300 px-4 text-base text-slate-800 placeholder:text-slate-400 focus:border-[#8B1E23] focus:outline-none focus:ring-4 focus:ring-red-100 transition"
              />

            </div>


            <!-- BADGE / STATION -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">

              <div>

                <label
                  class="mb-2 block text-base font-semibold text-slate-700"
                >
                  Badge Number
                </label>

                <input
                  v-model="signupForm.badgeNumber"
                  type="text"
                  placeholder="BFP-2026-XXXX"
                  class="w-full h-14 rounded-lg border-2 border-slate-300 px-4 text-base text-slate-800 placeholder:text-slate-400 focus:border-[#8B1E23] focus:outline-none focus:ring-4 focus:ring-red-100 transition"
                />

              </div>


              <div>

                <label
                  class="mb-2 block text-base font-semibold text-slate-700"
                >
                  Station / Unit
                </label>

                <select
                  v-model="signupForm.station"
                  class="w-full h-14 rounded-lg border-2 border-slate-300 bg-white px-4 text-base text-slate-800 focus:border-[#8B1E23] focus:outline-none focus:ring-4 focus:ring-red-100 transition"
                >

                  <option value="" disabled>
                    Select Station
                  </option>

                  <option value="Central Station">
                    Central Station
                  </option>

                  <option value="Sub-Station 1">
                    Sub-Station 1
                  </option>

                  <option value="Sub-Station 2">
                    Sub-Station 2
                  </option>

                  <option value="HQ District">
                    HQ District
                  </option>

                </select>

              </div>

            </div>


            <!-- PASSWORD -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">

              <div>

                <label
                  class="mb-2 block text-base font-semibold text-slate-700"
                >
                  Password
                </label>

                <div class="relative">

                  <input
                    v-model="signupForm.password"
                    :type="showSignupPassword ? 'text' : 'password'"
                    placeholder="Enter password"
                    class="w-full h-14 rounded-lg border-2 border-slate-300 px-4 pr-20 text-base text-slate-800 placeholder:text-slate-400 focus:border-[#8B1E23] focus:outline-none focus:ring-4 focus:ring-red-100 transition"
                  />

                  <button
                    type="button"
                    @click="showSignupPassword = !showSignupPassword"
                    class="absolute right-4 top-1/2 -translate-y-1/2 text-base font-semibold text-[#8B1E23] hover:underline"
                  >
                    {{ showSignupPassword ? 'Hide' : 'Show' }}
                  </button>

                </div>

              </div>


              <div>

                <label
                  class="mb-2 block text-base font-semibold text-slate-700"
                >
                  Confirm Password
                </label>

                <input
                  v-model="signupForm.confirmPassword"
                  :type="showSignupPassword ? 'text' : 'password'"
                  placeholder="Re-enter password"
                  class="w-full h-14 rounded-lg border-2 border-slate-300 px-4 text-base text-slate-800 placeholder:text-slate-400 focus:border-[#8B1E23] focus:outline-none focus:ring-4 focus:ring-red-100 transition"
                />

              </div>

            </div>


            <!-- REGISTER BUTTON -->
            <button
              type="submit"
              class="mt-4 w-full h-14 rounded-lg bg-[#8B1E23] text-white text-lg font-bold flex items-center justify-center gap-3 hover:bg-[#71181D] focus:outline-none focus:ring-4 focus:ring-red-200 transition shadow-md"
            >

              <svg
                class="w-6 h-6"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <path d="M12 5v14" />
                <path d="M5 12h14" />
              </svg>

              Create Account

            </button>

          </form>


          <!-- FOOTER -->
          <div
            class="mt-8 pt-5 border-t border-slate-200 text-center"
          >

            <p class="text-sm text-slate-500">
              FireNotify — Official Operations Compliance
              Monitoring Portal
            </p>

            <p class="text-sm text-slate-400 mt-1">
              Bureau of Fire Protection
            </p>

          </div>

        </div>

      </div>

    </div>

  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'

const props = defineProps({
  registeredUsers: {
    type: Array,
    required: true
  }
})

const emit = defineEmits(['login-success', 'register-user'])

const isLogin = ref(true)
const errorMessage = ref('')
const successMessage = ref('')
const showLoginPassword = ref(false)
const showSignupPassword = ref(false)

const loginForm = reactive({
  identifier: '',
  password: '',
  remember: false
})

const signupForm = reactive({
  firstName: '',
  lastName: '',
  badgeNumber: '',
  station: '',
  email: '',
  password: '',
  confirmPassword: ''
})

const switchToLogin = () => {
  isLogin.value = true
  errorMessage.value = ''
  successMessage.value = ''
}

const switchToRegister = () => {
  isLogin.value = false
  errorMessage.value = ''
  successMessage.value = ''
}

const handleLogin = () => {
  errorMessage.value = ''
  successMessage.value = ''

  if (!loginForm.identifier.trim() || !loginForm.password.trim()) {
    errorMessage.value = 'Please enter both your email and password.'
    return
  }

  const userFound = props.registeredUsers.find(
    (user) => user.identifier.toLowerCase() === loginForm.identifier.trim().toLowerCase() && user.password === loginForm.password
  )

  if (userFound) {
    emit('login-success', userFound)
  } else {
    errorMessage.value = 'Invalid email or password. Please try again.'
  }
}

const handleSignup = () => {
  errorMessage.value = ''
  successMessage.value = ''

  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/

  if (!signupForm.firstName.trim() || !signupForm.lastName.trim()) {
    errorMessage.value = 'Please complete your first and last name.'
    return
  }

  if (!signupForm.email.trim() || !emailPattern.test(signupForm.email.trim())) {
    errorMessage.value = 'Please enter a valid BFP email address.'
    return
  }

  if (!signupForm.badgeNumber.trim()) {
    errorMessage.value = 'Please enter your badge number.'
    return
  }

  if (!signupForm.station) {
    errorMessage.value = 'Please select your assigned station.'
    return
  }

  if (!signupForm.password || signupForm.password.length < 8) {
    errorMessage.value = 'Password must be at least 8 characters long.'
    return
  }

  if (signupForm.password !== signupForm.confirmPassword) {
    errorMessage.value = 'Passwords do not match.'
    return
  }

  const emailExists = props.registeredUsers.some(
    (user) => user.identifier.toLowerCase() === signupForm.email.trim().toLowerCase()
  )

  if (emailExists) {
    errorMessage.value = 'This email is already registered.'
    return
  }

  const newUser = {
    identifier: signupForm.email.trim(),
    password: signupForm.password,
    firstName: signupForm.firstName.trim(),
    lastName: signupForm.lastName.trim(),
    badgeNumber: signupForm.badgeNumber.trim(),
    station: signupForm.station,
    role: 'personnel'
  }

  emit('register-user', newUser)
  successMessage.value = 'Registration successful. You may now sign in with your account.'

  Object.assign(signupForm, {
    firstName: '',
    lastName: '',
    badgeNumber: '',
    station: '',
    email: '',
    password: '',
    confirmPassword: ''
  })

  isLogin.value = true
}
</script>

<style>
.font-display {
  font-family: 'Oswald', 'Arial Narrow', sans-serif;
}
.font-body {
  font-family: 'IBM Plex Sans', 'Helvetica Neue', sans-serif;
}
.font-mono {
  font-family: 'IBM Plex Mono', 'SFMono-Regular', monospace;
}
</style>