<template>
  <div class="min-h-screen w-full bg-slate-950 flex items-center justify-center p-4 sm:p-6 lg:p-8 relative overflow-hidden font-sans">
    <div class="absolute -top-24 -left-20 w-72 h-72 bg-red-600/20 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[32rem] h-[32rem] bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute -bottom-24 -right-20 w-72 h-72 bg-orange-500/10 rounded-full blur-3xl pointer-events-none"></div>

    <div class="relative z-10 w-full max-w-5xl overflow-hidden rounded-[28px] border border-slate-800/80 bg-slate-900/75 shadow-[0_25px_80px_rgba(15,23,42,0.8)] backdrop-blur-xl">
      <div class="grid lg:grid-cols-[1.08fr_0.92fr]">
        <div class="hidden lg:flex flex-col justify-between bg-gradient-to-br from-slate-950 via-slate-900 to-red-950/80 p-8 xl:p-10 border-r border-slate-800/80">
          <div>
            <div class="inline-flex items-center gap-3 px-3 py-2 rounded-full border border-red-500/30 bg-red-500/10 text-[10px] font-semibold uppercase tracking-[0.3em] text-red-300">
              <span class="h-2 w-2 rounded-full bg-red-500 shadow-[0_0_12px_rgba(239,68,68,0.9)]"></span>
              Secure Access Portal
            </div>

            <div class="mt-8 inline-flex items-center justify-center w-20 h-20 rounded-2xl bg-gradient-to-br from-red-600 to-amber-500 p-[1px] shadow-lg shadow-red-600/30">
              <div class="flex h-full w-full items-center justify-center rounded-2xl bg-slate-950">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M17.657 18.657A8 8 0 016.343 7.343S7 9 9 10c0-2 .5-5 2.986-7C14 5 16.09 5.777 17.656 7.343A7.975 7.975 0 0120 13a7.975 7.975 0 01-2.343 5.657z" />
                  <path stroke-linecap="round" stroke-linejoin="round" d="M9.879 16.121A3 3 0 1012.015 11L11 14H9.879z" />
                </svg>
              </div>
            </div>

            <h1 class="mt-6 text-4xl font-black tracking-[0.18em] text-white">FIRE<span class="text-red-500">NOTIFY</span></h1>
            <p class="mt-3 max-w-sm text-sm leading-6 text-slate-300">Modern compliance monitoring for BFP personnel, reporting, and field operations.</p>
          </div>

          <div class="space-y-4">
            <div class="rounded-2xl border border-slate-800 bg-slate-950/60 p-4">
              <p class="text-[10px] uppercase tracking-[0.25em] text-slate-400">Operational status</p>
              <div class="mt-3 flex items-center justify-between">
                <span class="text-sm text-slate-200">Station Access</span>
                <span class="inline-flex items-center rounded-full border border-emerald-500/30 bg-emerald-500/10 px-2.5 py-1 text-[10px] font-semibold text-emerald-300">ONLINE</span>
              </div>
            </div>

            <div class="grid grid-cols-3 gap-3 text-center">
              <div class="rounded-2xl border border-slate-800 bg-slate-950/50 p-3">
                <div class="text-xl font-bold text-white">48</div>
                <div class="text-[10px] uppercase tracking-[0.2em] text-slate-400">Officers</div>
              </div>
              <div class="rounded-2xl border border-slate-800 bg-slate-950/50 p-3">
                <div class="text-xl font-bold text-white">12</div>
                <div class="text-[10px] uppercase tracking-[0.2em] text-slate-400">Reports</div>
              </div>
              <div class="rounded-2xl border border-slate-800 bg-slate-950/50 p-3">
                <div class="text-xl font-bold text-white">94.5%</div>
                <div class="text-[10px] uppercase tracking-[0.2em] text-slate-400">Score</div>
              </div>
            </div>
          </div>
        </div>

        <div class="bg-slate-900/70 p-6 sm:p-8 lg:p-10">
          <div class="mb-7 flex items-center justify-between gap-3">
            <div>
              <p class="text-[10px] uppercase tracking-[0.35em] text-slate-500">Bureau of Fire Protection</p>
              <h2 class="mt-2 text-2xl font-bold text-white">{{ isLogin ? 'Welcome back' : 'Create account' }}</h2>
            </div>
            <div class="rounded-full border border-slate-700 bg-slate-950/60 px-3 py-1.5 text-[10px] font-semibold uppercase tracking-[0.2em] text-slate-300">
              Secure
            </div>
          </div>

          <div class="mb-6 flex rounded-2xl border border-slate-800 bg-slate-950/60 p-1">
            <button
              @click="switchToLogin"
              :class="[
                'flex-1 rounded-xl px-4 py-2.5 text-sm font-semibold transition-all duration-200',
                isLogin ? 'bg-red-600 text-white shadow-lg shadow-red-600/20' : 'text-slate-400 hover:text-slate-200'
              ]"
            >
              Sign In
            </button>
            <button
              @click="switchToRegister"
              :class="[
                'flex-1 rounded-xl px-4 py-2.5 text-sm font-semibold transition-all duration-200',
                !isLogin ? 'bg-red-600 text-white shadow-lg shadow-red-600/20' : 'text-slate-400 hover:text-slate-200'
              ]"
            >
              Register
            </button>
          </div>

          <div v-if="errorMessage" class="mb-5 rounded-xl border border-red-500/40 bg-red-500/10 px-3 py-2.5 text-xs text-red-200 text-center">
            {{ errorMessage }}
          </div>

          <div v-else-if="successMessage" class="mb-5 rounded-xl border border-emerald-500/40 bg-emerald-500/10 px-3 py-2.5 text-xs text-emerald-200 text-center">
            {{ successMessage }}
          </div>

          <form v-if="isLogin" @submit.prevent="handleLogin" class="space-y-5">
            <div>
              <label class="mb-2 block text-[10px] font-semibold uppercase tracking-[0.25em] text-slate-300">BFP Email Address</label>
              <input
                v-model="loginForm.identifier"
                type="text"
                placeholder="bfp.officer@bfp.gov.ph"
                class="w-full rounded-xl border border-slate-700 bg-slate-950/70 px-4 py-3 text-sm text-slate-100 placeholder:text-slate-500 focus:border-red-500 focus:outline-none focus:ring-2 focus:ring-red-500/20 transition-all"
              />
            </div>

            <div>
              <div class="mb-2 flex items-center justify-between">
                <label class="block text-[10px] font-semibold uppercase tracking-[0.25em] text-slate-300">Password</label>
                <button type="button" class="text-xs text-slate-400 transition-colors hover:text-red-300">Forgot?</button>
              </div>
              <div class="relative">
                <input
                  v-model="loginForm.password"
                  :type="showLoginPassword ? 'text' : 'password'"
                  placeholder="••••••••"
                  class="w-full rounded-xl border border-slate-700 bg-slate-950/70 px-4 py-3 pr-11 text-sm text-slate-100 placeholder:text-slate-500 focus:border-red-500 focus:outline-none focus:ring-2 focus:ring-red-500/20 transition-all"
                />
                <button type="button" @click="showLoginPassword = !showLoginPassword" class="absolute right-3 top-1/2 -translate-y-1/2 text-xs text-slate-400 hover:text-slate-200">
                  {{ showLoginPassword ? 'Hide' : 'Show' }}
                </button>
              </div>
            </div>

            <label class="flex items-center gap-3 text-sm text-slate-300">
              <input id="remember-me" v-model="loginForm.remember" type="checkbox" class="h-4 w-4 rounded border-slate-700 bg-slate-950 text-red-600 focus:ring-red-500 focus:ring-offset-slate-900" />
              Keep me logged in
            </label>

            <button type="submit" class="flex w-full items-center justify-center gap-2 rounded-xl bg-gradient-to-r from-red-600 to-red-500 px-4 py-3 text-sm font-semibold text-white shadow-lg shadow-red-950/40 transition-transform duration-200 hover:-translate-y-0.5 hover:from-red-500 hover:to-red-400 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 focus:ring-offset-slate-900">
              <span>🔐</span>
              Sign In
            </button>
          </form>

          <form v-else @submit.prevent="handleSignup" class="space-y-4">
            <div class="grid grid-cols-2 gap-3">
              <div>
                <label class="mb-1.5 block text-[10px] font-semibold uppercase tracking-[0.25em] text-slate-300">First Name</label>
                <input v-model="signupForm.firstName" type="text" placeholder="Juan" class="w-full rounded-xl border border-slate-700 bg-slate-950/70 px-3.5 py-2.5 text-sm text-slate-100 placeholder:text-slate-500 focus:border-red-500 focus:outline-none focus:ring-2 focus:ring-red-500/20 transition-all" />
              </div>
              <div>
                <label class="mb-1.5 block text-[10px] font-semibold uppercase tracking-[0.25em] text-slate-300">Last Name</label>
                <input v-model="signupForm.lastName" type="text" placeholder="Dela Cruz" class="w-full rounded-xl border border-slate-700 bg-slate-950/70 px-3.5 py-2.5 text-sm text-slate-100 placeholder:text-slate-500 focus:border-red-500 focus:outline-none focus:ring-2 focus:ring-red-500/20 transition-all" />
              </div>
            </div>

            <div>
              <label class="mb-1.5 block text-[10px] font-semibold uppercase tracking-[0.25em] text-slate-300">BFP Email Address</label>
              <input v-model="signupForm.email" type="email" placeholder="officer@bfp.gov.ph" class="w-full rounded-xl border border-slate-700 bg-slate-950/70 px-3.5 py-2.5 text-sm text-slate-100 placeholder:text-slate-500 focus:border-red-500 focus:outline-none focus:ring-2 focus:ring-red-500/20 transition-all" />
            </div>

            <div>
              <label class="mb-1.5 block text-[10px] font-semibold uppercase tracking-[0.25em] text-slate-300">Badge Number</label>
              <input v-model="signupForm.badgeNumber" type="text" placeholder="BFP-2026-XXXX" class="w-full rounded-xl border border-slate-700 bg-slate-950/70 px-3.5 py-2.5 text-sm text-slate-100 placeholder:text-slate-500 focus:border-red-500 focus:outline-none focus:ring-2 focus:ring-red-500/20 transition-all" />
            </div>

            <div class="grid grid-cols-2 gap-3">
              <div>
                <label class="mb-1.5 block text-[10px] font-semibold uppercase tracking-[0.25em] text-slate-300">Password</label>
                <div class="relative">
                  <input v-model="signupForm.password" :type="showSignupPassword ? 'text' : 'password'" placeholder="••••••••" class="w-full rounded-xl border border-slate-700 bg-slate-950/70 px-3.5 py-2.5 pr-11 text-sm text-slate-100 placeholder:text-slate-500 focus:border-red-500 focus:outline-none focus:ring-2 focus:ring-red-500/20 transition-all" />
                  <button type="button" @click="showSignupPassword = !showSignupPassword" class="absolute right-3 top-1/2 -translate-y-1/2 text-xs text-slate-400 hover:text-slate-200">
                    {{ showSignupPassword ? 'Hide' : 'Show' }}
                  </button>
                </div>
              </div>

              <div>
                <label class="mb-1.5 block text-[10px] font-semibold uppercase tracking-[0.25em] text-slate-300">Confirm</label>
                <input v-model="signupForm.confirmPassword" :type="showSignupPassword ? 'text' : 'password'" placeholder="Re-enter" class="w-full rounded-xl border border-slate-700 bg-slate-950/70 px-3.5 py-2.5 text-sm text-slate-100 placeholder:text-slate-500 focus:border-red-500 focus:outline-none focus:ring-2 focus:ring-red-500/20 transition-all" />
              </div>
            </div>

            <button type="submit" class="mt-2 flex w-full items-center justify-center gap-2 rounded-xl bg-gradient-to-r from-red-600 to-red-500 px-4 py-3 text-sm font-semibold text-white shadow-lg shadow-red-950/40 transition-transform duration-200 hover:-translate-y-0.5 hover:from-red-500 hover:to-red-400 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 focus:ring-offset-slate-900">
              <span>✅</span>
              Create Account
            </button>
          </form>

          <p class="mt-6 text-center text-[11px] text-slate-500">Official Operations Compliance Monitoring Portal</p>
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
    (user) => user.identifier === loginForm.identifier && user.password === loginForm.password
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
