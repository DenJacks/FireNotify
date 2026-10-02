<template>
  <div class="auth-page">

    <!-- =====================================================
         MAIN AUTH CONTAINER
    ====================================================== -->

    <div class="auth-container">

      <!-- ===================================================
           LEFT BRAND / INFORMATION PANEL
      ==================================================== -->

      <section class="auth-brand">

        <div class="brand-glow brand-glow-top"></div>
        <div class="brand-glow brand-glow-bottom"></div>

        <!-- Logo -->
        <div class="auth-logo">

          <div class="auth-logo-icon">
            <svg
              viewBox="0 0 24 24"
              fill="currentColor"
              class="w-8 h-8"
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
            <h1 class="auth-logo-name">
              FIRE<span>NOTIFY</span>
            </h1>

            <p class="auth-logo-subtitle">
              Bureau of Fire Protection
            </p>
          </div>

        </div>


        <!-- Brand Content -->
        <div class="auth-brand-content">

          <div class="auth-badge">
            <span class="auth-badge-dot"></span>

            <span>
              Secure Personnel Portal
            </span>
          </div>


          <h2 class="auth-brand-title">
            Operations Compliance
            <br />
            Monitoring System
          </h2>


          <p class="auth-brand-description">
            FireNotify helps BFP personnel manage assigned
            activities, reports, deadlines, and operational
            compliance in one place.
          </p>


          <!-- FEATURES -->

          <div class="auth-features">

            <!-- Feature 1 -->
            <div class="auth-feature">

              <div class="auth-feature-icon feature-red">

                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  class="w-6 h-6"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M12 3l7 4v5c0 4.5-3 7.8-7 9-4-1.2-7-4.5-7-9V7l7-4z"
                  />

                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M9 12l2 2 4-4"
                  />
                </svg>

              </div>

              <div class="auth-feature-text">

                <strong>
                  Track Compliance
                </strong>

                <span>
                  Monitor assigned activities and report submissions.
                </span>

              </div>

            </div>


            <!-- Feature 2 -->
            <div class="auth-feature">

              <div class="auth-feature-icon feature-gold">

                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  class="w-6 h-6"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M15 17h5l-1.5-1.5V11a6.5 6.5 0 00-13 0v4.5L4 17h5"
                  />

                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M10 21h4"
                  />
                </svg>

              </div>

              <div class="auth-feature-text">

                <strong>
                  Receive Notifications
                </strong>

                <span>
                  Stay informed about deadlines and assigned tasks.
                </span>

              </div>

            </div>


            <!-- Feature 3 -->
            <div class="auth-feature">

              <div class="auth-feature-icon feature-green">

                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  class="w-6 h-6"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M4 19V5"
                  />

                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M4 19h16"
                  />

                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M8 16v-5"
                  />

                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M12 16V8"
                  />

                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M16 16v-8"
                  />
                </svg>

              </div>

              <div class="auth-feature-text">

                <strong>
                  View Reports
                </strong>

                <span>
                  Access accomplishment and compliance reports.
                </span>

              </div>

            </div>

          </div>

        </div>


        <!-- SYSTEM STATUS -->

        <div class="auth-status">

          <div class="status-header">

            <span>
              System Status
            </span>

            <span class="status-online">

              <span class="status-dot"></span>

              Online

            </span>

          </div>


          <div class="status-metrics">

            <div class="status-metric">

              <strong>
                48
              </strong>

              <span>
                On Duty
              </span>

            </div>


            <div class="status-divider"></div>


            <div class="status-metric">

              <strong>
                12
              </strong>

              <span>
                Reports
              </span>

            </div>


            <div class="status-divider"></div>


            <div class="status-metric">

              <strong>
                94.5%
              </strong>

              <span>
                Readiness
              </span>

            </div>

          </div>

        </div>


        <div class="brand-stripe brand-stripe-one"></div>
        <div class="brand-stripe brand-stripe-two"></div>
        <div class="brand-stripe brand-stripe-three"></div>

      </section>


      <!-- ===================================================
           RIGHT AUTH PANEL
      ==================================================== -->

      <section class="auth-form-panel">

        <div class="form-top-line"></div>


        <!-- Header -->

        <div class="form-header">

          <p class="form-eyebrow">
            Personnel Access
          </p>

          <h2>
            {{ isLogin ? 'Welcome Back' : 'Create Your Account' }}
          </h2>

          <p>
            {{
              isLogin
                ? 'Sign in to access your FireNotify account.'
                : 'Register your BFP personnel account.'
            }}
          </p>

        </div>


        <!-- =================================================
             AUTH TABS
        ================================================== -->

        <div class="auth-tabs">

          <button
            type="button"
            @click="switchToLogin"
            :class="[
              'auth-tab',
              isLogin ? 'auth-tab-active' : ''
            ]"
          >

            <svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              class="w-5 h-5"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M15 21v-2a4 4 0 00-4-4H7a4 4 0 00-4 4v2"
              />

              <circle
                cx="9"
                cy="7"
                r="4"
              />

              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M19 8v6"
              />

              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M16 11h6"
              />
            </svg>

            Sign In

          </button>


          <button
            type="button"
            @click="switchToRegister"
            :class="[
              'auth-tab',
              !isLogin ? 'auth-tab-active' : ''
            ]"
          >

            <svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              class="w-5 h-5"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M16 21v-2a4 4 0 00-4-4H6a4 4 0 00-4 4v2"
              />

              <circle
                cx="9"
                cy="7"
                r="4"
              />

              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M19 8v6"
              />

              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M16 11h6"
              />
            </svg>

            Register

          </button>

        </div>


        <!-- ERROR -->

        <div
          v-if="errorMessage"
          class="message-box message-error"
        >

          <div class="message-icon">

            <svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              class="w-5 h-5"
            >
              <circle
                cx="12"
                cy="12"
                r="9"
              />

              <path d="M12 8v4" />

              <path d="M12 16h.01" />
            </svg>

          </div>

          <span>
            {{ errorMessage }}
          </span>

        </div>


        <!-- SUCCESS -->

        <div
          v-if="successMessage"
          class="message-box message-success"
        >

          <div class="message-icon">

            <svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              class="w-5 h-5"
            >
              <circle
                cx="12"
                cy="12"
                r="9"
              />

              <path d="M8 12l2.5 2.5L16 9" />

            </svg>

          </div>

          <div class="success-message-content">
            <span>{{ successMessage }}</span>
          </div>

        </div>


        <!-- =================================================
             LOGIN FORM
        ================================================== -->

        <form
          v-if="isLogin"
          @submit.prevent="handleLogin"
          class="auth-form"
        >

          <!-- Email -->

          <div class="form-field">

            <label>
              Email Address
            </label>

            <div class="input-wrapper">

              <svg
                class="input-icon"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <rect
                  x="3"
                  y="5"
                  width="18"
                  height="14"
                  rx="2"
                />

                <path d="M3 7l9 6 9-6" />
              </svg>

              <input
                v-model="loginForm.identifier"
                type="email"
                required
                autocomplete="email"
                placeholder="Enter your email"
              />

            </div>

          </div>


          <!-- Password -->

          <div class="form-field">

            <div class="field-label-row">

              <label>
                Password
              </label>

              <button
                type="button"
                class="forgot-button"
                @click="handleForgotPassword"
              >
                Forgot Password?
              </button>

            </div>


            <div class="input-wrapper">

              <svg
                class="input-icon"
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


              <input
                v-model="loginForm.password"
                :type="
                  showLoginPassword
                    ? 'text'
                    : 'password'
                "
                required
                autocomplete="current-password"
                placeholder="Enter your password"
              />


              <button
                type="button"
                class="password-button"
                @click="
                  showLoginPassword =
                    !showLoginPassword
                "
              >

                <svg
                  v-if="!showLoginPassword"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path
                    d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6S2 12 2 12z"
                  />

                  <circle
                    cx="12"
                    cy="12"
                    r="3"
                  />
                </svg>

                <svg
                  v-else
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path d="M3 3l18 18" />

                  <path
                    d="M10.6 10.6a2 2 0 002.8 2.8"
                  />

                  <path
                    d="M9.9 5.2A10.7 10.7 0 0112 5c6.5 0 10 7 10 7a17 17 0 01-3 3.8"
                  />

                  <path
                    d="M6.6 6.6C3.7 8.5 2 12 2 12s3.5 7 10 7c1.4 0 2.7-.3 3.8-.8"
                  />
                </svg>

              </button>

            </div>

          </div>


          <!-- Remember -->

          <label class="remember-row">

            <input
              v-model="loginForm.remember"
              type="checkbox"
            />

            <span>
              Keep me logged in
            </span>

          </label>


          <!-- Sign In -->

          <button
            type="submit"
            class="primary-button"
          >

            <svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
            >
              <path
                d="M15 3h4a2 2 0 012 2v14a2 2 0 01-2 2h-4"
              />

              <path
                d="M10 17l5-5-5-5"
              />

              <path
                d="M15 12H3"
              />
            </svg>

            Sign In

          </button>


          <!-- Divider -->

          <div class="divider">

            <span></span>

            <small>OR</small>

            <span></span>

          </div>


          <!-- BFP Account -->

          <button
            type="button"
            class="secondary-button"
            @click="handleBfpLogin"
          >

            <svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
            >
              <path
                d="M12 3l7 4v5c0 4.5-3 7.8-7 9-4-1.2-7-4.5-7-9V7l7-4z"
              />

              <path
                d="M9 12l2 2 4-4"
              />
            </svg>

            Login with BFP Account

          </button>

        </form>


        <!-- =================================================
             REGISTER FORM
        ================================================== -->

        <form
          v-else
          @submit.prevent="handleSignup"
          class="auth-form register-form"
        >

          <div class="form-section-title">Personal Information</div>

          <div class="two-column">

            <div class="form-field">

              <label>
                First Name
              </label>

              <div class="input-wrapper">

                <svg
                  class="input-icon"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <circle
                    cx="12"
                    cy="7"
                    r="4"
                  />

                  <path
                    d="M4 21a8 8 0 0116 0"
                  />
                </svg>

                <input
                  v-model="signupForm.firstName"
                  type="text"
                  required
                  autocomplete="given-name"
                  placeholder="Enter first name"
                />

              </div>

            </div>


            <div class="form-field">

              <label>
                Last Name
              </label>

              <div class="input-wrapper">

                <svg
                  class="input-icon"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <circle
                    cx="12"
                    cy="7"
                    r="4"
                  />

                  <path
                    d="M4 21a8 8 0 0116 0"
                  />
                </svg>

                <input
                  v-model="signupForm.lastName"
                  type="text"
                  required
                  autocomplete="family-name"
                  placeholder="Enter last name"
                />

              </div>

            </div>

          </div>

          <div class="two-column">
            <div class="form-field">
              <label>Email Address</label>
              <div class="input-wrapper">
                <svg class="input-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="5" width="18" height="14" rx="2"/>
                  <path d="M3 7l9 6 9-6"/>
                </svg>
                <input v-model="signupForm.email" type="email" required autocomplete="email" placeholder="name@example.com" />
              </div>
            </div>

            <div class="form-field">
              <label>Username</label>
              <div class="input-wrapper">
                <svg class="input-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="12" cy="8" r="4"/>
                  <path d="M4 20a8 8 0 0116 0"/>
                </svg>
                <input v-model="signupForm.username" type="text" required autocomplete="username" placeholder="Enter username" />
              </div>
            </div>
          </div>

          <div class="form-section-title">BFP Information</div>

          <div class="two-column">
            <div class="form-field">
              <label>Badge Number</label>
              <div class="input-wrapper">
                <svg class="input-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M7 7h10v10H7z"/>
                  <path d="M9 10h6M9 14h6"/>
                </svg>
                <input v-model="signupForm.badgeNumber" type="text" required placeholder="Example: BFP-1001" />
              </div>
            </div>

            <div class="form-field">
              <label>Rank</label>
              <div class="input-wrapper select-wrapper">
                <svg class="input-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M6 9l6 6 6-6"/>
                </svg>
                <select v-model="signupForm.rank" required>
                  <option value="">Select rank</option>
                  <option value="FO1">FO1</option>
                  <option value="FO2">FO2</option>
                  <option value="FO3">FO3</option>
                  <option value="FO4">FO4</option>
                  <option value="SFO1">SFO1</option>
                  <option value="SFO2">SFO2</option>
                  <option value="SFO3">SFO3</option>
                  <option value="SFO4">SFO4</option>
                </select>
              </div>
            </div>
          </div>

          <div class="form-section-title">Account Security</div>

          <div class="two-column">

            <div class="form-field">
              <label>Password</label>
              <div class="input-wrapper">
                <svg class="input-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="4" y="10" width="16" height="11" rx="2"/>
                  <path d="M8 10V7a4 4 0 018 0v3"/>
                </svg>
                <input v-model="signupForm.password" :type="showSignupPassword ? 'text' : 'password'" required autocomplete="new-password" placeholder="Enter password" />
                <button type="button" class="password-button" @click="showSignupPassword = !showSignupPassword">
                  <svg v-if="!showSignupPassword" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>
                  <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3l18 18"/><path d="M9.9 5.2A10.7 10.7 0 0112 5c6.5 0 10 7 10 7a17 17 0 01-3 3.8"/><path d="M6.6 6.6C3.7 8.5 2 12 2 12s3.5 7 10 7c1.4 0 2.7-.3 3.8-.8"/></svg>
                </button>
              </div>
            </div>

            <div class="form-field">
              <label>Confirm Password</label>
              <div class="input-wrapper">
                <svg class="input-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="4" y="10" width="16" height="11" rx="2"/>
                  <path d="M8 10V7a4 4 0 018 0v3"/>
                </svg>
                <input v-model="signupForm.confirmPassword" :type="showSignupPassword ? 'text' : 'password'" required autocomplete="new-password" placeholder="Re-enter password" />
              </div>
            </div>

          </div>

          <button type="submit" class="primary-button">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 5v14"/>
              <path d="M5 12h14"/>
            </svg>
            Create Account
          </button>

          <div class="divider">
            <span></span>
            <small>OR</small>
            <span></span>
          </div>

          <button type="button" class="secondary-button" @click="handleBfpRegister">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 3l7 4v5c0 4.5-3 7.8-7 9-4-1.2-7-4.5-7-9V7l7-4z"/>
              <path d="M9 12l2 2 4-4"/>
            </svg>
            Register with BFP Account
          </button>

        </form>


        <!-- =================================================
             FOOTER
        ================================================== -->

        <div class="auth-footer">

          <div class="footer-emblem">

            <svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="1.4"
            >
              <circle
                cx="12"
                cy="12"
                r="8"
              />

              <path d="M12 6v12" />
              <path d="M6 12h12" />
              <path d="M8 8l8 8" />
              <path d="M16 8l-8 8" />
            </svg>

          </div>

          <div>

            <p>
              FireNotify — Official Operations
              Compliance Monitoring Portal
            </p>

            <span>
              Bureau of Fire Protection
            </span>

          </div>

        </div>

      </section>

    </div>

  </div>
</template>


<script setup>
import { ref, reactive } from 'vue'


/* =========================================================
   EVENTS
========================================================= */

const emit = defineEmits([
  'login-success'
])


/* =========================================================
   API
========================================================= */

const API_URL = 'http://127.0.0.1:8000/api'


/* =========================================================
   AUTH STATE
========================================================= */

const isLogin = ref(true)

const errorMessage = ref('')
const successMessage = ref('')

const showLoginPassword = ref(false)
const showSignupPassword = ref(false)

const isLoading = ref(false)


/* =========================================================
   LOGIN FORM
========================================================= */

const loginForm = reactive({
  identifier: '',
  password: '',
  remember: false
})


/* =========================================================
   SIGNUP FORM
========================================================= */

const signupForm = reactive({
  firstName: '',
  lastName: '',
  email: '',
  username: '',
  badgeNumber: '',
  rank: '',
  password: '',
  confirmPassword: ''
})


/* =========================================================
   SWITCH TO LOGIN
========================================================= */

const switchToLogin = () => {

  isLogin.value = true

  errorMessage.value = ''
  successMessage.value = ''

  showLoginPassword.value = false
}


/* =========================================================
   SWITCH TO REGISTER
========================================================= */

const switchToRegister = () => {

  isLogin.value = false

  errorMessage.value = ''
  successMessage.value = ''

  showSignupPassword.value = false
}


/* =========================================================
   LOGIN
========================================================= */

const handleLogin = async () => {

  errorMessage.value = ''
  successMessage.value = ''

  const email =
    loginForm.identifier
      .trim()
      .toLowerCase()

  const password =
    loginForm.password


  /* ---------------------------------------------
     Validate input
  --------------------------------------------- */

  if (!email || !password) {

    errorMessage.value =
      'Please enter both your email and password.'

    return
  }


  /* ---------------------------------------------
     Start loading
  --------------------------------------------- */

  isLoading.value = true


  try {

    /* -------------------------------------------
       Send login request to Django
    ------------------------------------------- */

    const response = await fetch(
      `${API_URL}/auth/login/`,
      {
        method: 'POST',

        headers: {
          'Content-Type': 'application/json'
        },

        body: JSON.stringify({
          email: email,
          password: password
        })
      }
    )


    const data = await response.json()


    /* -------------------------------------------
       Handle Django error
    ------------------------------------------- */

    if (!response.ok) {

      errorMessage.value =
        data.error ||
        'Invalid email or password. Please try again.'

      return
    }


    /* -------------------------------------------
       Login successful
    ------------------------------------------- */

    const user = data.user


    console.log(
      'FireNotify login successful:',
      user
    )


    /* -------------------------------------------
       Save logged-in user
    ------------------------------------------- */

    if (loginForm.remember) {

      localStorage.setItem(
        'fireNotifyUser',
        JSON.stringify(user)
      )
      localStorage.setItem(
        'fireNotifyAuthenticated',
        'true'
      )
      sessionStorage.removeItem('fireNotifyUser')
      sessionStorage.removeItem('fireNotifyAuthenticated')

    } else {

      sessionStorage.setItem(
        'fireNotifyUser',
        JSON.stringify(user)
      )
      sessionStorage.setItem(
        'fireNotifyAuthenticated',
        'true'
      )
      localStorage.removeItem('fireNotifyUser')
      localStorage.removeItem('fireNotifyAuthenticated')
    }


    /* -------------------------------------------
       Send user to App.vue
    ------------------------------------------- */

    emit(
      'login-success',
      user
    )


  } catch (error) {

    console.error(
      'FireNotify login error:',
      error
    )

    errorMessage.value =
      'Unable to connect to the FireNotify server. Please make sure Django is running.'

  } finally {

    isLoading.value = false
  }
}


/* =========================================================
   SIGN UP
========================================================= */

const handleSignup = async () => {

  errorMessage.value = ''
  successMessage.value = ''


  /* ---------------------------------------------
     Normalize form values
  --------------------------------------------- */

  const firstName =
    signupForm.firstName.trim()

  const lastName =
    signupForm.lastName.trim()

  const email =
    signupForm.email
      .trim()
      .toLowerCase()

  const username =
    signupForm.username
      .trim()

  const badgeNumber =
    signupForm.badgeNumber
      .trim()

  const rank =
    signupForm.rank
      .trim()
      .toUpperCase()

  const password =
    signupForm.password

  const confirmPassword =
    signupForm.confirmPassword


  /* ---------------------------------------------
     Email validation
  --------------------------------------------- */

  const emailPattern =
    /^[^\s@]+@[^\s@]+\.[^\s@]+$/

  const namePattern =
    /^[A-Za-zÀ-ÖØ-öø-ÿ]+(?:[ '’-][A-Za-zÀ-ÖØ-öø-ÿ]+)*$/


  /* ---------------------------------------------
     Validate names
  --------------------------------------------- */

  if (!firstName || !namePattern.test(firstName)) {
    errorMessage.value = 'First name must contain only letters, spaces, hyphens, and apostrophes.'
    return
  }

  if (!lastName || !namePattern.test(lastName)) {
    errorMessage.value = 'Last name must contain only letters, spaces, hyphens, and apostrophes.'
    return
  }

  if (!email || !emailPattern.test(email)) {
    errorMessage.value = 'Please enter a valid email address.'
    return
  }

  if (!username) {
    errorMessage.value = 'Username is required.'
    return
  }

  if (!badgeNumber) {
    errorMessage.value = 'Badge number is required.'
    return
  }

  if (!rank) {
    errorMessage.value = 'Please select your BFP rank.'
    return
  }

  if (!password || password.length < 8) {
    errorMessage.value = 'Password must be at least 8 characters long.'
    return
  }

  if (password !== confirmPassword) {
    errorMessage.value = 'Passwords do not match.'
    return
  }


  /* ---------------------------------------------
     Start loading
  --------------------------------------------- */

  isLoading.value = true


  try {

    /* -------------------------------------------
       Send registration request to Django
    ------------------------------------------- */

    const response = await fetch(
      `${API_URL}/auth/register/`,
      {
        method: 'POST',

        headers: {
          'Content-Type': 'application/json'
        },

        body: JSON.stringify({
          first_name: firstName,
          last_name: lastName,
          email: email,
          username: username,
          badge_number: badgeNumber,
          rank: rank,
          password: password
        })
      }
    )


    const data =
      await response.json()


    /* -------------------------------------------
       Handle Django registration error
    ------------------------------------------- */

    if (!response.ok) {

      errorMessage.value =
        data.error ||
        'Registration failed. Please try again.'

      return
    }


    /* -------------------------------------------
       Registration successful
    ------------------------------------------- */

    console.log(
      'FireNotify registration successful:',
      data.user
    )


    successMessage.value =
      'Registration submitted successfully. Your account is now pending administrator approval. You can log in once your account has been approved.'

    Object.assign(
      signupForm,
      {
        firstName: '',
        lastName: '',
        email: '',
        username: '',
        badgeNumber: '',
        rank: '',
        password: '',
        confirmPassword: ''
      }
    )

    isLogin.value = true
    showSignupPassword.value = false


  } catch (error) {

    console.error(
      'FireNotify registration error:',
      error
    )

    errorMessage.value =
      'Unable to connect to the FireNotify server. Please make sure Django is running.'

  } finally {

    isLoading.value = false
  }
}


/* =========================================================
   FORGOT PASSWORD
========================================================= */

const handleForgotPassword = () => {

  errorMessage.value =
    'Password recovery is not available yet. Please contact the system administrator.'
}


/* =========================================================
   BFP LOGIN BUTTON
========================================================= */

const handleBfpLogin = () => {

  errorMessage.value =
    'BFP account authentication is not connected yet.'
}


/* =========================================================
   BFP REGISTER BUTTON
========================================================= */

const handleBfpRegister = () => {

  errorMessage.value =
    'BFP account registration is not connected yet.'
}
</script>
<style scoped>

/* =========================================================
   FIRENOTIFY AUTH DESIGN
   ========================================================= */

* {
  box-sizing: border-box;
}


/* =========================================================
   PAGE
   ========================================================= */

.auth-page {

  min-height: 100vh;

  width: 100%;

  display: flex;

  align-items: center;

  justify-content: center;

  padding: 28px;

  background:
    radial-gradient(
      circle at top left,
      rgba(139, 30, 35, 0.12),
      transparent 35%
    ),
    radial-gradient(
      circle at bottom right,
      rgba(245, 197, 66, 0.10),
      transparent 30%
    ),
    #eef2f6;

  font-family:
    Inter,
    ui-sans-serif,
    system-ui,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    sans-serif;
}


/* =========================================================
   MAIN CARD
   ========================================================= */

.auth-container {

  width: min(1180px, 100%);

  min-height: 720px;

  display: grid;

  grid-template-columns:
    46% 54%;

  background: white;

  border-radius: 24px;

  overflow: hidden;

  border: 1px solid
    rgba(255, 255, 255, 0.9);

  box-shadow:
    0 30px 80px
    rgba(15, 23, 42, 0.16),

    0 8px 25px
    rgba(15, 23, 42, 0.08);
}


/* =========================================================
   LEFT BRAND PANEL
   ========================================================= */

.auth-brand {

  position: relative;

  padding: 48px;

  overflow: hidden;

  color: white;

  background:
    linear-gradient(
      145deg,
      #4e080c 0%,
      #74151a 42%,
      #9f1d24 100%
    );

  display: flex;

  flex-direction: column;

  justify-content: space-between;
}


/* =========================================================
   DECORATIVE GLOW
   ========================================================= */

.brand-glow {

  position: absolute;

  border-radius: 50%;

  pointer-events: none;
}

.brand-glow-top {

  width: 420px;

  height: 420px;

  right: -200px;

  top: -200px;

  background:
    rgba(255, 255, 255, 0.07);
}

.brand-glow-bottom {

  width: 420px;

  height: 420px;

  left: -250px;

  bottom: -250px;

  background:
    rgba(244, 197, 66, 0.08);
}


/* =========================================================
   LOGO
   ========================================================= */

.auth-logo {

  position: relative;

  z-index: 5;

  display: flex;

  align-items: center;

  gap: 16px;
}

.auth-logo-icon {

  width: 62px;

  height: 62px;

  flex-shrink: 0;

  display: flex;

  align-items: center;

  justify-content: center;

  border-radius: 15px;

  background: white;

  color: #9f1d24;

  box-shadow:
    0 8px 25px
    rgba(0, 0, 0, 0.20);
}

.auth-logo-name {

  margin: 0;

  font-size: 28px;

  line-height: 1;

  font-weight: 900;

  letter-spacing: -0.5px;
}

.auth-logo-name span {

  color: #f5c542;
}

.auth-logo-subtitle {

  margin-top: 8px;

  font-size: 14px;

  color:
    rgba(255, 255, 255, 0.88);
}


/* =========================================================
   BRAND CONTENT
   ========================================================= */

.auth-brand-content {

  position: relative;

  z-index: 5;

  margin-top: 45px;
}


.auth-badge {

  display: inline-flex;

  align-items: center;

  gap: 9px;

  padding: 9px 14px;

  border-radius: 8px;

  background:
    rgba(255, 255, 255, 0.09);

  border:
    1px solid
    rgba(255, 255, 255, 0.18);

  backdrop-filter:
    blur(8px);

  font-size: 13px;

  font-weight: 600;
}


.auth-badge-dot {

  width: 8px;

  height: 8px;

  border-radius: 50%;

  background: #22c55e;

  box-shadow:
    0 0 0 4px
    rgba(34, 197, 94, 0.14);
}


/* =========================================================
   BRAND TITLE
   ========================================================= */

.auth-brand-title {

  margin-top: 25px;

  font-size: clamp(
    32px,
    3.2vw,
    43px
  );

  line-height: 1.08;

  font-weight: 900;

  letter-spacing: -1.5px;
}


.auth-brand-description {

  margin-top: 20px;

  max-width: 440px;

  font-size: 16px;

  line-height: 1.8;

  color:
    rgba(255, 255, 255, 0.82);
}


/* =========================================================
   FEATURES
   ========================================================= */

.auth-features {

  margin-top: 38px;

  display: flex;

  flex-direction: column;

  gap: 21px;
}


.auth-feature {

  display: flex;

  align-items: center;

  gap: 15px;
}


.auth-feature-icon {

  width: 47px;

  height: 47px;

  flex-shrink: 0;

  display: flex;

  align-items: center;

  justify-content: center;

  border-radius: 12px;

  background:
    rgba(255, 255, 255, 0.12);

  border:
    1px solid
    rgba(255, 255, 255, 0.12);
}


.feature-red {

  color: #ffb3b7;
}


.feature-gold {

  color: #f5c542;
}


.feature-green {

  color: #5ee59b;
}


.auth-feature-text {

  display: flex;

  flex-direction: column;

  gap: 4px;
}


.auth-feature-text strong {

  font-size: 16px;

  font-weight: 800;

  color: white;
}


.auth-feature-text span {

  font-size: 13px;

  line-height: 1.45;

  color:
    rgba(255, 255, 255, 0.70);
}


/* =========================================================
   SYSTEM STATUS
   ========================================================= */

.auth-status {

  position: relative;

  z-index: 5;

  margin-top: 35px;

  padding: 19px;

  border-radius: 13px;

  background:
    rgba(15, 7, 8, 0.35);

  border:
    1px solid
    rgba(255, 255, 255, 0.18);

  backdrop-filter:
    blur(10px);
}


.status-header {

  display: flex;

  align-items: center;

  justify-content: space-between;

  font-size: 14px;

  font-weight: 700;
}


.status-online {

  display: flex;

  align-items: center;

  gap: 8px;

  color: #4ade80;
}


.status-dot {

  width: 9px;

  height: 9px;

  border-radius: 50%;

  background: #22c55e;

  box-shadow:
    0 0 0 4px
    rgba(34, 197, 94, 0.13);
}


.status-metrics {

  display: grid;

  grid-template-columns:
    1fr auto 1fr auto 1fr;

  margin-top: 17px;

  align-items: center;
}


.status-metric {

  text-align: center;
}


.status-metric strong {

  display: block;

  font-size: 24px;

  color: #f5c542;

  font-weight: 900;
}


.status-metric span {

  display: block;

  margin-top: 4px;

  font-size: 11px;

  color:
    rgba(255, 255, 255, 0.62);
}


.status-divider {

  height: 35px;

  width: 1px;

  background:
    rgba(255, 255, 255, 0.15);
}


/* =========================================================
   DECORATIVE STRIPES
   ========================================================= */

.brand-stripe {

  position: absolute;

  height: 16px;

  bottom: -5px;

  transform: rotate(-10deg);

  z-index: 3;
}


.brand-stripe-one {

  width: 180px;

  left: -25px;

  background: #8b1e23;
}


.brand-stripe-two {

  width: 180px;

  left: 100px;

  background: #f5c542;
}


.brand-stripe-three {

  width: 180px;

  left: 220px;

  background: #b2222b;
}


/* =========================================================
   RIGHT FORM PANEL
   ========================================================= */

.auth-form-panel {

  position: relative;

  padding: 48px 52px 35px;

  background: #ffffff;

  display: flex;

  flex-direction: column;
}


.form-top-line {

  width: 55px;

  height: 5px;

  border-radius: 10px;

  background:
    linear-gradient(
      90deg,
      #9f1d24,
      #f5c542
    );

  margin-bottom: 25px;
}


/* =========================================================
   FORM HEADER
   ========================================================= */

.form-header {

  margin-bottom: 25px;
}


.form-eyebrow {

  margin: 0;

  font-size: 13px;

  font-weight: 800;

  text-transform: uppercase;

  letter-spacing: 0.8px;

  color: #9f1d24;
}


.form-header h2 {

  margin-top: 8px;

  margin-bottom: 7px;

  color: #10233f;

  font-size: 34px;

  line-height: 1.15;

  font-weight: 900;

  letter-spacing: -0.8px;
}


.form-header > p:last-child {

  margin: 0;

  font-size: 14px;

  color: #68778c;
}


/* =========================================================
   TABS
   ========================================================= */

.auth-tabs {

  display: grid;

  grid-template-columns:
    1fr 1fr;

  gap: 0;

  border-bottom:
    1px solid #dce2ea;

  margin-bottom: 27px;
}


.auth-tab {

  position: relative;

  min-height: 51px;

  display: flex;

  align-items: center;

  justify-content: center;

  gap: 9px;

  border: none;

  background: transparent;

  color: #718096;

  font-size: 15px;

  font-weight: 700;

  cursor: pointer;

  transition:
    color 0.2s ease,
    background 0.2s ease;
}


.auth-tab:hover {

  color: #9f1d24;

  background:
    rgba(159, 29, 36, 0.025);
}


.auth-tab-active {

  color: #9f1d24;
}


.auth-tab-active::after {

  content: "";

  position: absolute;

  left: 0;

  right: 0;

  bottom: -1px;

  height: 3px;

  border-radius:
    5px 5px 0 0;

  background: #9f1d24;
}


/* =========================================================
   MESSAGE
   ========================================================= */

.message-box {

  display: flex;

  align-items: flex-start;

  gap: 10px;

  padding: 12px 14px;

  border-radius: 9px;

  margin-bottom: 18px;

  font-size: 13px;

  font-weight: 600;

  line-height: 1.5;
}


.message-icon {

  flex-shrink: 0;
}


.message-error {

  color: #a61b24;

  background: #fff1f2;

  border:
    1px solid #fecdd3;
}


.message-success {

  color: #167a43;

  background: #effdf5;

  border:
    1px solid #bbf7d0;
}

.success-message-content {
  display: flex;
  flex-direction: column;
  gap: 12px;
  width: 100%;
}

.compact-button {
  width: fit-content;
  margin-top: 4px;
}


/* =========================================================
   FORM
   ========================================================= */

.auth-form {

  display: flex;

  flex-direction: column;

  gap: 20px;
}


.register-form {

  gap: 17px;
}

.form-section-title {
  margin-top: 6px;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #9f1d24;
}

.form-field {

  width: 100%;
}


.form-field label {

  display: block;

  margin-bottom: 8px;

  font-size: 13px;

  font-weight: 800;

  color: #25364f;
}


.field-label-row {

  display: flex;

  align-items: center;

  justify-content: space-between;

  margin-bottom: 8px;
}


.field-label-row label {

  margin-bottom: 0;
}


.forgot-button {

  border: none;

  background: transparent;

  color: #9f1d24;

  font-size: 12px;

  font-weight: 700;

  cursor: pointer;

  padding: 0;
}


.forgot-button:hover {

  text-decoration: underline;
}


/* =========================================================
   INPUT
   ========================================================= */

.input-wrapper {

  position: relative;

  width: 100%;
}


.input-wrapper input,
.input-wrapper select {

  width: 100%;

  height: 53px;

  border-radius: 9px;

  border: 1.5px solid #ccd5e1;

  background: #ffffff;

  color: #17243a;

  font-size: 14px;

  outline: none;

  padding:
    0 46px 0 44px;

  transition:
    border-color 0.2s ease,
    box-shadow 0.2s ease,
    background 0.2s ease;
}

.input-wrapper select {
  appearance: none;
  background-image: none;
}

.input-wrapper input::placeholder {

  color: #9aa8bb;
}


.input-wrapper input:hover,
.input-wrapper select:hover {

  border-color: #b8c4d3;
}


.input-wrapper input:focus,
.input-wrapper select:focus {

  border-color: #9f1d24;

  background: #fff;

  box-shadow:
    0 0 0 4px
    rgba(159, 29, 36, 0.09);
}


.input-icon {

  position: absolute;

  left: 15px;

  top: 50%;

  width: 18px;

  height: 18px;

  transform: translateY(-50%);

  color: #8492a6;

  pointer-events: none;

  z-index: 2;
}


.password-button {

  position: absolute;

  right: 13px;

  top: 50%;

  transform: translateY(-50%);

  width: 30px;

  height: 30px;

  display: flex;

  align-items: center;

  justify-content: center;

  border: none;

  background: transparent;

  color: #738196;

  cursor: pointer;

  border-radius: 6px;
}


.password-button:hover {

  color: #9f1d24;

  background:
    rgba(159, 29, 36, 0.06);
}


.password-button svg {

  width: 18px;

  height: 18px;
}


/* =========================================================
   TWO COLUMN
   ========================================================= */

.two-column {

  display: grid;

  grid-template-columns:
    1fr 1fr;

  gap: 15px;
}


/* =========================================================
   REMEMBER ME
   ========================================================= */

.remember-row {

  display: flex;

  align-items: center;

  gap: 9px;

  margin-top: -4px;

  color: #53647a;

  font-size: 13px;

  cursor: pointer;

  user-select: none;
}


.remember-row input {

  width: 17px;

  height: 17px;

  margin: 0;

  accent-color: #9f1d24;

  cursor: pointer;
}


/* =========================================================
   PRIMARY BUTTON
   ========================================================= */

.primary-button {

  width: 100%;

  height: 54px;

  border: none;

  border-radius: 9px;

  display: flex;

  align-items: center;

  justify-content: center;

  gap: 10px;

  background:
    linear-gradient(
      135deg,
      #9f1d24,
      #8b1e23
    );

  color: white;

  font-size: 15px;

  font-weight: 800;

  cursor: pointer;

  box-shadow:
    0 8px 18px
    rgba(139, 30, 35, 0.20);

  transition:
    transform 0.18s ease,
    box-shadow 0.18s ease,
    background 0.18s ease;
}


.primary-button svg {

  width: 20px;

  height: 20px;
}


.primary-button:hover {

  transform: translateY(-1px);

  background:
    linear-gradient(
      135deg,
      #b1222b,
      #8b1e23
    );

  box-shadow:
    0 11px 25px
    rgba(139, 30, 35, 0.28);
}


.primary-button:active {

  transform: translateY(0);
}


/* =========================================================
   DIVIDER
   ========================================================= */

.divider {

  display: grid;

  grid-template-columns:
    1fr auto 1fr;

  align-items: center;

  gap: 12px;

  margin: -2px 0;
}


.divider span {

  height: 1px;

  background: #e0e5eb;
}


.divider small {

  font-size: 11px;

  color: #99a5b5;

  font-weight: 700;

  letter-spacing: 0.8px;
}


/* =========================================================
   SECONDARY BUTTON
   ========================================================= */

.secondary-button {

  width: 100%;

  min-height: 50px;

  border-radius: 9px;

  border: 1px solid #aeb9c8;

  background: white;

  color: #33445d;

  display: flex;

  align-items: center;

  justify-content: center;

  gap: 9px;

  font-size: 13px;

  font-weight: 700;

  cursor: pointer;

  transition:
    border-color 0.2s ease,
    color 0.2s ease,
    background 0.2s ease;
}


.secondary-button svg {

  width: 19px;

  height: 19px;
}


.secondary-button:hover {

  border-color: #9f1d24;

  color: #9f1d24;

  background: #fff8f8;
}


/* =========================================================
   FOOTER
   ========================================================= */

.auth-footer {

  display: flex;

  align-items: center;

  justify-content: center;

  gap: 12px;

  margin-top: auto;

  padding-top: 25px;

  border-top: 1px solid #e6eaf0;

  color: #8491a4;

  text-align: left;
}


.auth-footer p {

  margin: 0;

  font-size: 11px;

  line-height: 1.5;
}


.auth-footer span {

  display: block;

  margin-top: 2px;

  font-size: 10px;

  color: #a2acba;
}


.footer-emblem {

  width: 42px;

  height: 42px;

  flex-shrink: 0;

  color: #9aa5b4;
}


.footer-emblem svg {

  width: 100%;

  height: 100%;
}


/* =========================================================
   TABLET
   ========================================================= */

@media (max-width: 1024px) {

  .auth-page {

    padding: 20px;
  }


  .auth-container {

    grid-template-columns:
      42% 58%;

    min-height: 680px;
  }


  .auth-brand {

    padding: 35px;
  }


  .auth-form-panel {

    padding:
      38px 38px 30px;
  }


  .auth-brand-title {

    font-size: 34px;
  }

}


/* =========================================================
   MOBILE
   ========================================================= */

@media (max-width: 768px) {

  .auth-page {

    padding: 0;

    align-items: stretch;
  }


  .auth-container {

    width: 100%;

    min-height: 100vh;

    border-radius: 0;

    display: block;

    box-shadow: none;
  }


  .auth-brand {

    min-height: auto;

    padding: 28px 24px 30px;
  }


  .auth-brand-content {

    margin-top: 30px;
  }


  .auth-brand-title {

    font-size: 30px;
  }


  .auth-brand-description {

    font-size: 14px;

    line-height: 1.7;
  }


  .auth-features {

    margin-top: 25px;

    gap: 15px;
  }


  .auth-feature-text span {

    font-size: 12px;
  }


  .auth-status {

    margin-top: 25px;
  }


  .auth-form-panel {

    padding:
      32px 24px 25px;
  }


  .form-header h2 {

    font-size: 30px;
  }


  .auth-footer {

    margin-top: 30px;
  }

}


/* =========================================================
   SMALL MOBILE
   ========================================================= */

@media (max-width: 500px) {

  .auth-logo-icon {

    width: 52px;

    height: 52px;
  }


  .auth-logo-name {

    font-size: 23px;
  }


  .auth-brand-title {

    font-size: 27px;
  }


  .status-metric strong {

    font-size: 20px;
  }


  .two-column {

    grid-template-columns: 1fr;

    gap: 17px;
  }


  .form-header h2 {

    font-size: 27px;
  }


  .auth-form-panel {

    padding:
      28px 20px 22px;
  }

}

</style>