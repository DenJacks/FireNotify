<template>
  <div class="min-h-screen w-full bg-[#15120F] flex items-center justify-center p-4 sm:p-6 lg:p-8 relative overflow-hidden font-body">
    <!-- Ambient glow elements -->
    <div class="absolute top-1/3 left-1/4 -translate-x-1/2 -translate-y-1/2 w-[28rem] h-[28rem] bg-[#C1272D]/10 rounded-full blur-[100px] pointer-events-none"></div>
    <div class="absolute bottom-0 right-0 w-96 h-96 bg-[#E8A33D]/[0.06] rounded-full blur-[100px] pointer-events-none"></div>

    <div class="relative z-10 w-full max-w-5xl overflow-hidden rounded-2xl border border-[#3A3530] bg-[#1B1815] shadow-[0_30px_90px_rgba(0,0,0,0.65)]">

      <!-- Hazard-stripe header motif -->
      <div class="h-[7px] w-full" style="background-image: repeating-linear-gradient(135deg, #E8A33D 0 14px, #15120F 14px 28px);"></div>

      <div class="grid lg:grid-cols-[1.05fr_0.95fr]">

        <!-- LEFT: Station Plaque / Readout -->
        <div class="hidden lg:flex flex-col justify-between bg-[#181410] p-9 xl:p-11 border-r border-[#3A3530]/70 relative">
          <div>
            <div class="inline-flex items-center gap-2.5 px-3 py-1.5 rounded-sm border border-[#E8A33D]/25 bg-[#E8A33D]/[0.06]">
              <span class="relative flex h-1.5 w-1.5">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#E8A33D]/60"></span>
                <span class="relative inline-flex rounded-full h-1.5 w-1.5 bg-[#E8A33D]"></span>
              </span>
              <span class="font-mono text-[10px] font-medium uppercase tracking-[0.28em] text-[#E8A33D]/90">Secure Access Portal</span>
            </div>

            <!-- Emblem + Branding -->
            <div class="mt-9 flex items-center gap-4">
              <svg viewBox="0 0 64 64" class="h-16 w-16 shrink-0" fill="none">
                <path d="M32 4 L58 13 V29 C58 45 47 55 32 60 C17 55 6 45 6 29 V13 Z"
                      stroke="#C9A227" stroke-width="1.6" fill="#15120F"/>
                <path d="M32 4 L58 13 V29 C58 45 47 55 32 60 C17 55 6 45 6 29 V13 Z"
                      stroke="#C9A227" stroke-width="1.6" fill="none" opacity="0.5" transform="scale(0.92) translate(2.8 2.8)"/>
                <path d="M32 20c-4.5 4.5-7 8.2-7 12.2 0 4.4 3.3 7.8 7.4 7.8 4.5 0 7.9-3.2 7.9-7.5 0-2.2-.9-3.9-2.3-5.6.1 1.7-.5 2.9-1.6 3.7.3-2.9-.7-6.4-4.4-10.6Z"
                      fill="#C9A227" opacity="0.9"/>
              </svg>
              <div>
                <h1 class="font-display text-[28px] leading-none font-semibold tracking-[0.14em] text-[#EDE6D6]">FIRE<span class="text-[#C1272D]">NOTIFY</span></h1>
                <p class="mt-2 font-mono text-[10px] uppercase tracking-[0.2em] text-[#9A9086]">Bureau of Fire Protection</p>
              </div>
            </div>

            <p class="mt-5 max-w-sm text-sm leading-6 text-[#B5ACA1]">Compliance monitoring, incident reporting, and field operations — built for BFP personnel.</p>
          </div>

          <!-- Dispatch-board readout -->
          <div class="rounded-lg border border-[#3A3530] bg-[#100D0B] px-5 py-4">
            <div class="flex items-center justify-between">
              <p class="font-mono text-[9px] uppercase tracking-[0.3em] text-[#6E645A]">Station Readout</p>
              <span class="font-mono text-[9px] uppercase tracking-[0.25em] text-[#7BA88A]">● Online</span>
            </div>
            <div class="mt-3.5 grid grid-cols-3 divide-x divide-[#3A3530]">
              <div class="px-1 text-center first:pl-0">
                <div class="font-mono text-2xl font-medium text-[#E8A33D] [text-shadow:0_0_12px_rgba(232,163,61,0.35)]">48</div>
                <div class="mt-1 font-mono text-[8px] uppercase tracking-[0.2em] text-[#7A6F63]">On Duty</div>
              </div>
              <div class="px-1 text-center">
                <div class="font-mono text-2xl font-medium text-[#E8A33D] [text-shadow:0_0_12px_rgba(232,163,61,0.35)]">12</div>
                <div class="mt-1 font-mono text-[8px] uppercase tracking-[0.2em] text-[#7A6F63]">Reports</div>
              </div>
              <div class="px-1 text-center last:pr-0">
                <div class="font-mono text-2xl font-medium text-[#E8A33D] [text-shadow:0_0_12px_rgba(232,163,61,0.35)]">94.5%</div>
                <div class="mt-1 font-mono text-[8px] uppercase tracking-[0.2em] text-[#7A6F63]">Readiness</div>
              </div>
            </div>
          </div>
        </div>

        <!-- RIGHT: Form panel -->
        <div class="bg-[#1B1815] p-6 sm:p-8 lg:p-10">
          <div class="mb-7">
            <p class="font-mono text-[10px] uppercase tracking-[0.3em] text-[#7A6F63]">Personnel Access</p>
            <h2 class="mt-2 font-display text-2xl font-semibold tracking-wide text-[#EDE6D6]">{{ isLogin ? 'Welcome back' : 'Create account' }}</h2>
          </div>

          <!-- Sliding tab buttons -->
          <div class="mb-7 flex gap-6 border-b border-[#3A3530]">
            <button
              @click="switchToLogin"
              type="button"
              class="relative pb-3 font-mono text-xs font-medium uppercase tracking-[0.2em] transition-colors duration-200"
              :class="isLogin ? 'text-[#EDE6D6]' : 'text-[#6E645A] hover:text-[#9A9086]'"
            >
              Sign In
              <span class="absolute -bottom-px left-0 h-[2px] bg-[#C1272D] transition-all duration-300" :class="isLogin ? 'w-full' : 'w-0'"></span>
            </button>
            <button
              @click="switchToRegister"
              type="button"
              class="relative pb-3 font-mono text-xs font-medium uppercase tracking-[0.2em] transition-colors duration-200"
              :class="!isLogin ? 'text-[#EDE6D6]' : 'text-[#6E645A] hover:text-[#9A9086]'"
            >
              Register
              <span class="absolute -bottom-px left-0 h-[2px] bg-[#C1272D] transition-all duration-300" :class="!isLogin ? 'w-full' : 'w-0'"></span>
            </button>
          </div>

          <!-- Status Banners -->
          <div v-if="errorMessage" class="mb-5 flex items-center gap-2.5 rounded-md border border-[#C1272D]/30 bg-[#C1272D]/[0.08] px-3.5 py-2.5">
            <svg class="h-3.5 w-3.5 shrink-0 text-[#E4595E]" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm.75-11a.75.75 0 00-1.5 0v4a.75.75 0 001.5 0V7zm-.75 6.25a.875.875 0 100 1.75.875.875 0 000-1.75z" clip-rule="evenodd"/></svg>
            <span class="text-xs text-[#E4959A]">{{ errorMessage }}</span>
          </div>

          <div v-else-if="successMessage" class="mb-5 flex items-center gap-2.5 rounded-md border border-[#7BA88A]/30 bg-[#7BA88A]/[0.08] px-3.5 py-2.5">
            <svg class="h-3.5 w-3.5 shrink-0 text-[#7BA88A]" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.7 5.3a1 1 0 010 1.4l-7.5 7.5a1 1 0 01-1.4 0l-3.5-3.5a1 1 0 111.4-1.4l2.8 2.8 6.8-6.8a1 1 0 011.4 0z" clip-rule="evenodd"/></svg>
            <span class="text-xs text-[#A9CBB4]">{{ successMessage }}</span>
          </div>

          <!-- LOGIN FORM -->
          <form v-if="isLogin" @submit.prevent="handleLogin" class="space-y-5">
            <div>
              <label class="mb-2 block font-mono text-[10px] font-medium uppercase tracking-[0.22em] text-[#9A9086]">BFP Email Address</label>
              <input
                v-model="loginForm.identifier"
                type="email"
                required
                placeholder="bfp.officer@bfp.gov.ph"
                class="w-full rounded-md border border-[#3A3530] bg-[#100D0B] px-4 py-3 text-sm text-[#EDE6D6] placeholder:text-[#5A5148] focus:border-[#E8A33D]/60 focus:outline-none focus:ring-1 focus:ring-[#E8A33D]/30 transition-all"
              />
            </div>

            <div>
              <div class="mb-2 flex items-center justify-between">
                <label class="font-mono text-[10px] font-medium uppercase tracking-[0.22em] text-[#9A9086]">Password</label>
                <button type="button" class="text-[11px] text-[#7A6F63] transition-colors hover:text-[#E8A33D]">Forgot?</button>
              </div>
              <div class="relative">
                <input
                  v-model="loginForm.password"
                  :type="showLoginPassword ? 'text' : 'password'"
                  required
                  placeholder="••••••••"
                  class="w-full rounded-md border border-[#3A3530] bg-[#100D0B] px-4 py-3 pr-12 text-sm text-[#EDE6D6] placeholder:text-[#5A5148] focus:border-[#E8A33D]/60 focus:outline-none focus:ring-1 focus:ring-[#E8A33D]/30 transition-all"
                />
                <button type="button" @click="showLoginPassword = !showLoginPassword" class="absolute right-3.5 top-1/2 -translate-y-1/2 font-mono text-[10px] uppercase tracking-wide text-[#7A6F63] hover:text-[#B5ACA1]">
                  {{ showLoginPassword ? 'Hide' : 'Show' }}
                </button>
              </div>
            </div>

            <label class="flex items-center gap-2.5 text-sm text-[#B5ACA1] cursor-pointer">
              <input id="remember-me" v-model="loginForm.remember" type="checkbox" class="h-3.5 w-3.5 rounded-sm border-[#3A3530] bg-[#100D0B] text-[#C1272D] focus:ring-[#E8A33D]/40 focus:ring-offset-0" />
              Keep me logged in
            </label>

            <button type="submit" class="flex w-full items-center justify-center gap-2.5 rounded-md bg-[#C1272D] px-4 py-3 text-sm font-semibold tracking-wide text-[#EDE6D6] shadow-[0_10px_30px_rgba(193,39,45,0.25)] transition-colors duration-200 hover:bg-[#A82126] focus:outline-none focus:ring-1 focus:ring-[#E8A33D]/50">
              <svg class="h-4 w-4" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="4.5" y="9" width="11" height="8" rx="1.2"/><path d="M7 9V6.5a3 3 0 016 0V9"/></svg>
              Sign In
            </button>
          </form>

          <!-- SIGNUP FORM -->
          <form v-else @submit.prevent="handleSignup" class="space-y-3.5">
            <div class="grid grid-cols-2 gap-3">
              <div>
                <label class="mb-1.5 block font-mono text-[10px] font-medium uppercase tracking-[0.22em] text-[#9A9086]">First Name</label>
                <input v-model="signupForm.firstName" type="text" placeholder="Juan" class="w-full rounded-md border border-[#3A3530] bg-[#100D0B] px-3.5 py-2 text-sm text-[#EDE6D6] placeholder:text-[#5A5148] focus:border-[#E8A33D]/60 focus:outline-none focus:ring-1 focus:ring-[#E8A33D]/30 transition-all" />
              </div>
              <div>
                <label class="mb-1.5 block font-mono text-[10px] font-medium uppercase tracking-[0.22em] text-[#9A9086]">Last Name</label>
                <input v-model="signupForm.lastName" type="text" placeholder="Dela Cruz" class="w-full rounded-md border border-[#3A3530] bg-[#100D0B] px-3.5 py-2 text-sm text-[#EDE6D6] placeholder:text-[#5A5148] focus:border-[#E8A33D]/60 focus:outline-none focus:ring-1 focus:ring-[#E8A33D]/30 transition-all" />
              </div>
            </div>

            <div>
              <label class="mb-1.5 block font-mono text-[10px] font-medium uppercase tracking-[0.22em] text-[#9A9086]">BFP Email Address</label>
              <input v-model="signupForm.email" type="email" placeholder="officer@bfp.gov.ph" class="w-full rounded-md border border-[#3A3530] bg-[#100D0B] px-3.5 py-2 text-sm text-[#EDE6D6] placeholder:text-[#5A5148] focus:border-[#E8A33D]/60 focus:outline-none focus:ring-1 focus:ring-[#E8A33D]/30 transition-all" />
            </div>

            <div class="grid grid-cols-2 gap-3">
              <div>
                <label class="mb-1.5 block font-mono text-[10px] font-medium uppercase tracking-[0.22em] text-[#9A9086]">Badge Number</label>
                <input v-model="signupForm.badgeNumber" type="text" placeholder="BFP-2026-XXXX" class="w-full rounded-md border border-[#3A3530] bg-[#100D0B] px-3.5 py-2 text-sm text-[#EDE6D6] placeholder:text-[#5A5148] focus:border-[#E8A33D]/60 focus:outline-none focus:ring-1 focus:ring-[#E8A33D]/30 transition-all" />
              </div>
              <div>
                <label class="mb-1.5 block font-mono text-[10px] font-medium uppercase tracking-[0.22em] text-[#9A9086]">Station / Unit</label>
                <select v-model="signupForm.station" class="w-full rounded-md border border-[#3A3530] bg-[#100D0B] px-3 py-2 text-sm text-[#EDE6D6] focus:border-[#E8A33D]/60 focus:outline-none focus:ring-1 focus:ring-[#E8A33D]/30 transition-all">
                  <option value="" disabled selected>Select Station</option>
                  <option value="Central Station">Central Station</option>
                  <option value="Sub-Station 1">Sub-Station 1</option>
                  <option value="Sub-Station 2">Sub-Station 2</option>
                  <option value="HQ District">HQ District</option>
                </select>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-3">
              <div>
                <label class="mb-1.5 block font-mono text-[10px] font-medium uppercase tracking-[0.22em] text-[#9A9086]">Password</label>
                <div class="relative">
                  <input v-model="signupForm.password" :type="showSignupPassword ? 'text' : 'password'" placeholder="••••••••" class="w-full rounded-md border border-[#3A3530] bg-[#100D0B] px-3.5 py-2 pr-10 text-sm text-[#EDE6D6] placeholder:text-[#5A5148] focus:border-[#E8A33D]/60 focus:outline-none focus:ring-1 focus:ring-[#E8A33D]/30 transition-all" />
                  <button type="button" @click="showSignupPassword = !showSignupPassword" class="absolute right-3 top-1/2 -translate-y-1/2 font-mono text-[10px] uppercase tracking-wide text-[#7A6F63] hover:text-[#B5ACA1]">
                    {{ showSignupPassword ? 'Hide' : 'Show' }}
                  </button>
                </div>
              </div>

              <div>
                <label class="mb-1.5 block font-mono text-[10px] font-medium uppercase tracking-[0.22em] text-[#9A9086]">Confirm</label>
                <input v-model="signupForm.confirmPassword" :type="showSignupPassword ? 'text' : 'password'" placeholder="Re-enter" class="w-full rounded-md border border-[#3A3530] bg-[#100D0B] px-3.5 py-2 text-sm text-[#EDE6D6] placeholder:text-[#5A5148] focus:border-[#E8A33D]/60 focus:outline-none focus:ring-1 focus:ring-[#E8A33D]/30 transition-all" />
              </div>
            </div>

            <button type="submit" class="mt-3 flex w-full items-center justify-center gap-2.5 rounded-md bg-[#C1272D] px-4 py-3 text-sm font-semibold tracking-wide text-[#EDE6D6] shadow-[0_10px_30px_rgba(193,39,45,0.25)] transition-colors duration-200 hover:bg-[#A82126] focus:outline-none focus:ring-1 focus:ring-[#E8A33D]/50">
              <svg class="h-4 w-4" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 10.5l4 4 8-9"/></svg>
              Create Account
            </button>
          </form>

          <p class="mt-6 text-center font-mono text-[10px] uppercase tracking-[0.18em] text-[#5A5148]">Official Operations Compliance Monitoring Portal</p>
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