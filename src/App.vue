```vue
<template>

  <div v-if="!authInitializing">

    <!-- =====================================================
         LOGIN
    ====================================================== -->

    <LoginSignup
      v-if="!isLoggedIn"
      :registered-users="registeredUsers"
      @login-success="handleLoginSuccess"
      @register-user="handleRegisterUser"
    />


    <!-- =====================================================
         LOGGED IN
    ====================================================== -->

    <div
      v-else-if="currentUser"
    >

      <!-- =================================================
           ADMIN
      ================================================== -->

      <AdminDashboard
        v-if="String(currentUser.role || '').toUpperCase() === 'ADMIN'"
        :current-user="currentUser"
        :registered-users="registeredUsers"
        @logout="handleLogout"
        @delete-user="handleDeleteUser"
        @update-user="handleUserUpdate"
      />


      <!-- =================================================
           PERSONNEL
      ================================================== -->

      <PersonnelDashboard
        v-else-if="
          ['ADMIN', 'AUTH', 'PERSONNEL', 'INSPECTOR'].includes(
            String(currentUser.role || '').toUpperCase()
          ) && String(currentUser.role || '').toUpperCase() !== 'ADMIN'
        "
        :current-user="currentUser"
        :registered-users="registeredUsers"
        @logout="handleLogout"
        @update-user="handleUserUpdate"
      />


      <!-- =================================================
           UNKNOWN ROLE
      ================================================== -->

      <div
        v-else
        class="min-h-screen bg-slate-950 text-white flex items-center justify-center p-6"
      >

        <div class="text-center">

          <h1
            class="text-3xl font-bold mb-4"
          >
            Unknown User Role
          </h1>

          <p
            class="text-slate-400 mb-6"
          >
            Role:
            {{ currentUser.role }}
          </p>

          <button
            @click="handleLogout"
            class="px-5 py-3 bg-red-600 hover:bg-red-700 rounded-xl font-semibold"
          >
            Log Out
          </button>

        </div>

      </div>

    </div>

  </div>

</template>


<script setup>

import {
  ref,
  computed,
  onMounted
} from 'vue'

import LoginSignup
  from './views/auth/LoginSignup.vue'

import AdminDashboard
  from './views/admin/AdminDashboard.vue'

import PersonnelDashboard
  from './views/personnel/PersonnelDashboard.vue'


/* =========================================================
   STORAGE
========================================================= */

const USERS_STORAGE_KEY =
  'fireNotifyRegisteredUsers'

const CURRENT_USER_KEY =
  'fireNotifyCurrentUser'
const AUTH_SESSION_KEY =
  'fireNotifyAuthenticated'

const clearSavedAuthentication = () => {
  localStorage.removeItem(CURRENT_USER_KEY)
  localStorage.removeItem('fireNotifyUser')
  localStorage.removeItem(AUTH_SESSION_KEY)
  sessionStorage.removeItem('fireNotifyUser')
  sessionStorage.removeItem(AUTH_SESSION_KEY)
}


/* =========================================================
   DEFAULT ADMIN
========================================================= */

const defaultUsers = [

  {

    id:
      'admin-default',

    identifier:
      'admin@firenotify.local',

    password:
      'admin111',

    role:
      'admin',

    firstName:
      'Master',

    lastName:
      'Admin',

    name:
      'Master Admin',

    rank:
      'ADMIN',

    position:
      'System Administrator',

    status:
      'Active',

    createdAt:
      new Date().toISOString()

  }

]


/* =========================================================
   STATE
========================================================= */

const registeredUsers =
  ref([])

const currentUser =
  ref(null)

const authInitializing =
  ref(true)


/* =========================================================
   LOGIN STATE
========================================================= */

const isLoggedIn =
  computed(() =>
    currentUser.value !== null
  )


/* =========================================================
   LOAD USERS
========================================================= */

const loadRegisteredUsers = () => {

  try {

    const stored =
      localStorage.getItem(
        USERS_STORAGE_KEY
      )


    if (!stored) {

      const users =
        [...defaultUsers]

      localStorage.setItem(
        USERS_STORAGE_KEY,
        JSON.stringify(users)
      )

      return users

    }


    const parsed =
      JSON.parse(stored)


    if (!Array.isArray(parsed)) {
      throw new Error(
        'Invalid users data'
      )
    }


    const normalizedUsers =
      parsed.map(user => ({

        ...user,

        id:
          user.id ||
          crypto.randomUUID(),

        identifier:
          user.identifier
            ?.trim()
            .toLowerCase() ||
          '',

        firstName:
          user.firstName ||
          '',

        lastName:
          user.lastName ||
          '',

        name:
          user.name ||
          `${user.firstName || ''} ${user.lastName || ''}`
            .trim(),

        status:
          user.status ||
          'Active'

      }))


    const adminExists =
      normalizedUsers.some(
        user =>
          user.identifier
            ?.trim()
            .toLowerCase() ===
          'admin@firenotify.local'
      )


    if (!adminExists) {

      normalizedUsers.unshift(
        {
          ...defaultUsers[0]
        }
      )

    }


    localStorage.setItem(
      USERS_STORAGE_KEY,
      JSON.stringify(
        normalizedUsers
      )
    )


    return normalizedUsers

  } catch (error) {

    console.error(
      'Failed to load registered users:',
      error
    )


    const fallbackUsers =
      [...defaultUsers]


    localStorage.setItem(
      USERS_STORAGE_KEY,
      JSON.stringify(
        fallbackUsers
      )
    )


    return fallbackUsers

  }

}


/* =========================================================
   SAVE USERS
========================================================= */

const saveRegisteredUsers = () => {

  localStorage.setItem(
    USERS_STORAGE_KEY,
    JSON.stringify(
      registeredUsers.value
    )
  )

}


/* =========================================================
   REGISTER USER
========================================================= */

const handleRegisterUser = newUser => {

  if (!newUser) {
    return
  }


  if (
    newUser.role === 'admin'
  ) {

    console.warn(
      'Admin registration is not allowed.'
    )

    return

  }


  const newIdentifier =
    newUser.identifier
      ?.trim()
      .toLowerCase()


  if (!newIdentifier) {

    console.warn(
      'Registration failed: email is required.'
    )

    return

  }


  const duplicate =
    registeredUsers.value.some(
      user =>
        user.identifier
          ?.trim()
          .toLowerCase() ===
        newIdentifier
    )


  if (duplicate) {

    console.warn(
      'Registration blocked: email already exists.'
    )

    return

  }


  const firstName =
    newUser.firstName
      ?.trim() ||
    ''


  const lastName =
    newUser.lastName
      ?.trim() ||
    ''


  const fullName =
    `${firstName} ${lastName}`
      .trim()


  const userToSave = {

    id:
      newUser.id ||
      crypto.randomUUID(),

    identifier:
      newIdentifier,

    password:
      newUser.password,

    firstName,

    lastName,

    name:
      newUser.name ||
      fullName,

    role:
      'personnel',

    status:
      'Active',

    createdAt:
      newUser.createdAt ||
      new Date().toISOString()

  }


  registeredUsers.value = [

    ...registeredUsers.value,

    userToSave

  ]


  saveRegisteredUsers()


  console.log(
    'Personnel account registered:',
    userToSave
  )

}


/* =========================================================
   LOGIN
========================================================= */

const handleLoginSuccess = user => {

  if (!user) {
    return
  }


  localStorage.removeItem(
    'fireNotifyAdminActiveMenu'
  )

  localStorage.removeItem(
    'fireNotifyPersonnelActiveTab'
  )


 const loggedInUser = {

  ...user,

  // Django uses first_name / last_name
  // while Vue uses firstName / lastName

  firstName:
    user.firstName ||
    user.first_name ||
    '',

  lastName:
    user.lastName ||
    user.last_name ||
    '',

  name:
    user.name ||
    `${user.firstName || user.first_name || ''} ${
      user.lastName || user.last_name || ''
    }`.trim(),

  // Normalize Django role to lowercase
  role:
    String(user.role || '').toUpperCase(),

  badge_number:
    user.badge_number || user.badgeNumber || '',

  badgeNumber:
    user.badge_number || user.badgeNumber || '',

  rank:
    user.rank || user.employeeRank || '',

  status:
    user.status || 'PENDING'

}


  currentUser.value =
    loggedInUser


  localStorage.setItem(
    CURRENT_USER_KEY,
    JSON.stringify(
      loggedInUser
    )
  )

}


/* =========================================================
   RESTORE SESSION
========================================================= */

const loadCurrentUser = () => {

  const authStorage =
    localStorage.getItem(AUTH_SESSION_KEY) === 'true'
      ? localStorage
      : sessionStorage.getItem(AUTH_SESSION_KEY) === 'true'
        ? sessionStorage
        : null

  if (!authStorage) {
    clearSavedAuthentication()
    return
  }

  const loginSession = authStorage.getItem('fireNotifyUser')

  if (!loginSession) {
    clearSavedAuthentication()
    return
  }


  try {

    const authenticatedUser = JSON.parse(loginSession)
    const cachedUser = JSON.parse(
      localStorage.getItem(CURRENT_USER_KEY) || 'null'
    )


    if (
      !authenticatedUser ||
      !authenticatedUser.role
    ) {

      clearSavedAuthentication()

      return

    }

    const authenticatedIdentity = String(
      authenticatedUser.email ||
      authenticatedUser.identifier ||
      authenticatedUser.username ||
      ''
    ).trim().toLowerCase()
    const cachedIdentity = String(
      cachedUser?.email ||
      cachedUser?.identifier ||
      cachedUser?.username ||
      ''
    ).trim().toLowerCase()
    const cachedUserMatchesSession = Boolean(
      cachedUser?.role && (
        authenticatedUser.id && cachedUser.id
          ? String(authenticatedUser.id) === String(cachedUser.id)
          : authenticatedIdentity && authenticatedIdentity === cachedIdentity
      )
    )
    const user = cachedUserMatchesSession ? cachedUser : authenticatedUser


    const userEmail =
      (
        user.email ||
        user.identifier ||
        ''
      )
        .trim()
        .toLowerCase()


    const storedUser =
      registeredUsers.value.find(
        item => {

          const itemEmail =
            (
              item.email ||
              item.identifier ||
              ''
            )
              .trim()
              .toLowerCase()

          return (
            itemEmail ===
            userEmail
          )

        }
      )


    /*
      If the user came from Django,
      use the saved Django user directly.
    */

    if (!storedUser) {

      currentUser.value = {

        ...user,

        firstName:
          user.firstName ||
          user.first_name ||
          '',

        lastName:
          user.lastName ||
          user.last_name ||
          '',

        name:
          user.name ||
          `${user.firstName || user.first_name || ''} ${
            user.lastName || user.last_name || ''
          }`.trim(),

        role:
          String(
            user.role || ''
          ).toUpperCase(),

        badge_number:
          user.badge_number || user.badgeNumber || '',

        badgeNumber:
          user.badge_number || user.badgeNumber || '',

        rank:
          user.rank || user.employeeRank || '',

        status:
          user.status || 'PENDING'

      }

      return

    }


    currentUser.value = {

      ...storedUser,

      ...user,

      firstName:
        user.firstName ||
        user.first_name ||
        storedUser.firstName ||
        '',

      lastName:
        user.lastName ||
        user.last_name ||
        storedUser.lastName ||
        '',

      name:
        user.name ||
        `${user.firstName || user.first_name || storedUser.firstName || ''} ${
          user.lastName || user.last_name || storedUser.lastName || ''
        }`.trim(),

      role:
        String(
          user.role ||
          storedUser.role ||
          ''
        ).toUpperCase(),

      badge_number:
        user.badge_number || user.badgeNumber || storedUser.badge_number || storedUser.badgeNumber || '',

      badgeNumber:
        user.badge_number || user.badgeNumber || storedUser.badge_number || storedUser.badgeNumber || '',

      rank:
        user.rank || user.employeeRank || storedUser.rank || storedUser.employeeRank || '',

      status:
        user.status || storedUser.status || 'PENDING'

    }


  } catch (error) {

    console.error(
      'Failed to restore user session:',
      error
    )

    clearSavedAuthentication()

    currentUser.value =
      null

  }

}


/* =========================================================
   UPDATE USER
========================================================= */

const handleUserUpdate =
  updatedUser => {

    if (
      !updatedUser
    ) {
      return
    }


    /*
     * If the current logged-in user
     * is being updated.
     */

    if (
      currentUser.value?.id ===
      updatedUser.id
    ) {

      const updatedSession = {

        ...currentUser.value,

        ...updatedUser,

        name:
          updatedUser.name ||
          `${updatedUser.firstName || ''} ${updatedUser.lastName || ''}`
            .trim()

      }


      currentUser.value =
        updatedSession


      localStorage.setItem(
        CURRENT_USER_KEY,
        JSON.stringify(
          updatedSession
        )
      )

    }


    /*
     * Update user in registered users.
     */

    registeredUsers.value =
      registeredUsers.value.map(
        user => {

          const sameId =
            user.id &&
            updatedUser.id &&
            user.id ===
              updatedUser.id


          const sameEmail =
            user.identifier
              ?.trim()
              .toLowerCase() ===
            updatedUser.identifier
              ?.trim()
              .toLowerCase()


          if (
            sameId ||
            sameEmail
          ) {

            return {

              ...user,

              ...updatedUser,

              name:
                updatedUser.name ||
                `${updatedUser.firstName || ''} ${updatedUser.lastName || ''}`
                  .trim()

            }

          }


          return user

        }
      )


    saveRegisteredUsers()

}


/* =========================================================
   DELETE USER
========================================================= */

const handleDeleteUser =
  userId => {

    if (!userId) {
      return
    }


    if (
      currentUser.value?.id ===
      userId
    ) {

      console.warn(
        'Cannot delete current account.'
      )

      return

    }


    registeredUsers.value =
      registeredUsers.value.filter(
        user =>
          user.id !==
          userId
      )


    saveRegisteredUsers()

  }


/* =========================================================
   LOGOUT
========================================================= */

const handleLogout = () => {

  currentUser.value =
    null

  clearSavedAuthentication()


  localStorage.removeItem(
    'fireNotifyPersonnelActiveTab'
  )


  localStorage.removeItem(
    'fireNotifyAdminActiveMenu'
  )

}


/* =========================================================
   INITIALIZE
========================================================= */

onMounted(async () => {

  registeredUsers.value =
    loadRegisteredUsers()

  try {

    const response =
      await fetch(
        'http://127.0.0.1:8000/api/users/'
      )

    if (response.ok) {

      const data =
        await response.json()

      if (Array.isArray(data)) {

        registeredUsers.value =
          data.map(user => ({

            ...user,

            identifier:
              user.email ||
              user.username ||
              '',

            firstName:
              user.first_name ||
              user.firstName ||
              '',

            lastName:
              user.last_name ||
              user.lastName ||
              '',

            name:
              `${user.first_name || user.firstName || ''} ${
                user.last_name || user.lastName || ''
              }`.trim(),

            role:
              String(
                user.role || ''
              ).toLowerCase(),

            status:
              user.is_active
                ? 'Active'
                : 'Inactive'

          }))

      }

    }

  } catch (error) {

    console.error(
      'Failed to load users from Django:',
      error
    )

  }

  loadCurrentUser()
  authInitializing.value = false

})
</script>
```
