<template>
  <div>

    <!-- ===================================================== -->
    <!-- LOGIN PAGE -->
    <!-- ===================================================== -->

    <LoginSignup
      v-if="!isLoggedIn"
      :registered-users="registeredUsers"
      @login-success="handleLoginSuccess"
      @register-user="handleRegisterUser"
    />


    <!-- ===================================================== -->
    <!-- LOGGED-IN USER -->
    <!-- ===================================================== -->

    <div v-else-if="currentUser">

      <!-- ADMIN -->
      <AdminDashboard
        v-if="currentUser.role === 'admin'"
        :current-user="currentUser"
        @logout="handleLogout"
      />


      <!-- PERSONNEL / AUTH / INSPECTOR -->
      <PersonnelDashboard
        v-else-if="
          ['auth', 'personnel', 'inspector'].includes(
            currentUser.role
          )
        "
        :current-user="currentUser"
        @logout="handleLogout"
        @update-user="handleUserUpdate"
      />


      <!-- UNKNOWN ROLE -->
      <div
        v-else
        class="min-h-screen bg-slate-950 text-white flex items-center justify-center"
      >

        <div class="text-center">

          <h1 class="text-3xl font-bold mb-4">
            ⚠️ Unknown User Role
          </h1>

          <p class="text-slate-400 mb-6">
            Role: {{ currentUser.role }}
          </p>

          <button
            @click="handleLogout"
            class="px-5 py-3 bg-red-600 hover:bg-red-700 rounded-xl font-semibold"
          >
            Back to Login
          </button>

        </div>

      </div>

    </div>

  </div>
</template>


<script setup>

import { ref, computed } from 'vue'

import LoginSignup from './views/auth/LoginSignup.vue'
import AdminDashboard from './views/admin/AdminDashboard.vue'
import PersonnelDashboard from './views/personnel/PersonnelDashboard.vue'


/* =========================================================
   STORAGE KEYS
========================================================= */

const USERS_STORAGE_KEY = 'fireNotifyRegisteredUsers'
const CURRENT_USER_KEY = 'fireNotifyCurrentUser'


/* =========================================================
   DEFAULT USERS
========================================================= */

const defaultUsers = [
  {
    identifier: 'admin@bfp.gov.ph',
    password: 'admin',
    role: 'admin',
    firstName: 'Master',
    lastName: 'Admin',
    name: 'Master Admin',
    rank: 'ADMIN',
    position: 'System Administrator',
    station: 'BFP Station'
  },

  {
    identifier: 'personnel@bfp.gov.ph',
    password: 'personnel',
    role: 'personnel',
    firstName: 'Fire',
    lastName: 'Officer',
    name: 'Fire Officer',
    rank: 'FO3',
    position: 'Fire Officer',
    station: 'BFP Station'
  },

  {
    identifier: 'auth@bfp.gov.ph',
    password: 'auth',
    role: 'auth',
    firstName: 'Auth',
    lastName: 'Officer',
    name: 'Auth Officer',
    rank: 'FO3',
    position: 'Fire Officer',
    station: 'BFP Station'
  }
]


/* =========================================================
   STATE
========================================================= */

const registeredUsers = ref([])
const currentUser = ref(null)


/* =========================================================
   AUTHENTICATION STATE
========================================================= */

const isLoggedIn = computed(() => {
  return currentUser.value !== null
})


/* =========================================================
   LOAD CURRENT USER
========================================================= */

const loadCurrentUser = () => {

  const savedUser = localStorage.getItem(
    CURRENT_USER_KEY
  )

  if (!savedUser) {
    return
  }

  try {

    const user = JSON.parse(savedUser)

    if (
      user &&
      user.identifier &&
      user.role
    ) {

      currentUser.value = user

    }

  } catch (error) {

    console.error(
      'Failed to restore user session:',
      error
    )

    localStorage.removeItem(
      CURRENT_USER_KEY
    )

  }
}


/* =========================================================
   LOAD REGISTERED USERS
========================================================= */

const loadRegisteredUsers = () => {

  const savedUsers = localStorage.getItem(
    USERS_STORAGE_KEY
  )

  if (savedUsers) {

    try {

      const parsedUsers = JSON.parse(
        savedUsers
      )

      if (
        Array.isArray(parsedUsers) &&
        parsedUsers.length > 0
      ) {

        registeredUsers.value =
          parsedUsers.map(user => ({
            ...user,
            role: user.role || 'personnel'
          }))

        return

      }

    } catch (error) {

      console.error(
        'Failed to load registered users:',
        error
      )

    }

  }

  registeredUsers.value = [
    ...defaultUsers
  ]

  localStorage.setItem(
    USERS_STORAGE_KEY,
    JSON.stringify(
      registeredUsers.value
    )
  )
}


/* =========================================================
   LOGIN SUCCESS
========================================================= */

const handleLoginSuccess = (user) => {

  if (!user) {
    return
  }

  /*
   * Always start from Dashboard
   */

  localStorage.removeItem(
    'fireNotifyAdminActiveMenu'
  )

  localStorage.removeItem(
    'fireNotifyPersonnelActiveTab'
  )

  currentUser.value = {
    ...user,

    name:
      user.name ||
      `${user.firstName || ''} ${user.lastName || ''}`.trim()
  }

  localStorage.setItem(
    CURRENT_USER_KEY,
    JSON.stringify(
      currentUser.value
    )
  )
}


/* =========================================================
   UPDATE CURRENT USER
========================================================= */

const handleUserUpdate = (updatedUser) => {

  if (!updatedUser) {
    return
  }

  /*
   * Update active session
   */

  currentUser.value = {
    ...currentUser.value,
    ...updatedUser,

    name:
      updatedUser.name ||
      `${updatedUser.firstName || ''} ${updatedUser.lastName || ''}`.trim()
  }


  /*
   * Update current session storage
   */

  localStorage.setItem(
    CURRENT_USER_KEY,
    JSON.stringify(
      currentUser.value
    )
  )


  /*
   * Update registered users list
   */

  registeredUsers.value =
    registeredUsers.value.map(user => {

      if (
        user.identifier ===
        currentUser.value.identifier
      ) {

        return {
          ...user,
          ...currentUser.value
        }

      }

      return user

    })


  /*
   * Save updated users
   */

  localStorage.setItem(
    USERS_STORAGE_KEY,
    JSON.stringify(
      registeredUsers.value
    )
  )
}


/* =========================================================
   LOGOUT
========================================================= */

const handleLogout = () => {

  currentUser.value = null

  localStorage.removeItem(
    CURRENT_USER_KEY
  )

  /*
   * Return to Dashboard next time user logs in
   */

  localStorage.removeItem(
    'fireNotifyPersonnelActiveTab'
  )

  localStorage.removeItem(
    'fireNotifyAdminActiveMenu'
  )
}


/* =========================================================
   REGISTER USER
========================================================= */

const handleRegisterUser = (newUser) => {

  if (
    !newUser ||
    newUser.role === 'admin'
  ) {

    return
  }


  const duplicate =
    registeredUsers.value.some(
      user =>
        user.identifier &&
        newUser.identifier &&
        user.identifier.toLowerCase() ===
        newUser.identifier.toLowerCase()
    )


  if (duplicate) {
    return
  }


  const userToSave = {
    ...newUser,

    name:
      newUser.name ||
      `${newUser.firstName || ''} ${newUser.lastName || ''}`.trim(),

    role:
      newUser.role || 'personnel'
  }


  registeredUsers.value = [
    ...registeredUsers.value,
    userToSave
  ]


  localStorage.setItem(
    USERS_STORAGE_KEY,
    JSON.stringify(
      registeredUsers.value
    )
  )
}


/* =========================================================
   INITIALIZE APPLICATION
========================================================= */

loadRegisteredUsers()
loadCurrentUser()

</script>