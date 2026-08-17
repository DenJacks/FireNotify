<template>
  <div>
    <LoginSignup
      v-if="!isLoggedIn"
      :registered-users="registeredUsers"
      @login-success="handleLoginSuccess"
      @register-user="handleRegisterUser"
    />

    <div v-else-if="isLoggedIn && currentUser">
      <AdminDashboard
        v-if="currentUser.role === 'admin'"
        :current-user="currentUser"
        @logout="handleLogout"
      />

      <PersonnelDashboard
        v-else-if="['auth', 'personnel', 'inspector'].includes(currentUser.role)"
        :current-user="currentUser"
        @logout="handleLogout"
      />

      <div v-else class="min-h-screen bg-slate-950 text-slate-100 flex items-center justify-center">
        <div class="text-center">
          <h1 class="text-3xl font-bold mb-4">⚠️ Error</h1>
          <p class="text-slate-400 mb-6">Unknown user role: {{ currentUser.role }}</p>
          <button @click="handleLogout" class="px-4 py-2 bg-red-600 hover:bg-red-700 rounded-lg text-white">
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

const STORAGE_KEY = 'fireNotifyRegisteredUsers'
const CURRENT_USER_KEY = 'fireNotifyCurrentUser'

const defaultUsers = [
  {
    identifier: 'admin@bfp.gov.ph',
    password: 'admin',
    role: 'admin',
    firstName: 'Master',
    lastName: 'Admin'
  },
  {
    identifier: 'personnel@bfp.gov.ph',
    password: 'personnel',
    role: 'personnel',
    firstName: 'Fire',
    lastName: 'Officer'
  },
  {
    identifier: 'auth@bfp.gov.ph',
    password: 'auth',
    role: 'auth',
    firstName: 'Auth',
    lastName: 'Officer'
  }
]

const registeredUsers = ref([])
const currentUser = ref(null)

const savedUser = localStorage.getItem(CURRENT_USER_KEY)
if (savedUser) {
  try {
    currentUser.value = JSON.parse(savedUser)
  } catch (error) {
    console.error('Failed to parse saved user:', error)
  }
}

const isLoggedIn = computed(() => currentUser.value !== null)

const loadRegisteredUsers = () => {
  const savedUsers = localStorage.getItem(STORAGE_KEY)

  if (savedUsers) {
    try {
      const parsedUsers = JSON.parse(savedUsers)
      if (Array.isArray(parsedUsers) && parsedUsers.length) {
        registeredUsers.value = parsedUsers.map((user) => ({
          ...user,
          role: user.role || 'personnel'
        }))
        localStorage.setItem(STORAGE_KEY, JSON.stringify(registeredUsers.value))
        return
      }
    } catch (error) {
      console.error('Failed to parse saved users:', error)
    }
  }

  registeredUsers.value = [...defaultUsers]
  localStorage.setItem(STORAGE_KEY, JSON.stringify(registeredUsers.value))
}

const handleLoginSuccess = (user) => {
  currentUser.value = user
  localStorage.setItem(CURRENT_USER_KEY, JSON.stringify(user))
}

const handleLogout = () => {
  currentUser.value = null
  localStorage.removeItem(CURRENT_USER_KEY)
}

const handleRegisterUser = (newUser) => {
  if (!newUser || newUser.role === 'admin') {
    return
  }

  const duplicate = registeredUsers.value.some(
    (user) => user.identifier.toLowerCase() === newUser.identifier.toLowerCase()
  )

  if (duplicate) {
    return
  }

  registeredUsers.value = [...registeredUsers.value, newUser]
  localStorage.setItem(STORAGE_KEY, JSON.stringify(registeredUsers.value))
}

loadRegisteredUsers()
</script>

<style scoped>
@keyframes sidebarItemEnter {
  from {
    opacity: 0;
    transform: translateX(-12px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.animate-sidebar-item {
  animation: sidebarItemEnter 0.45s ease-out both;
}

@keyframes logoFloat {
  0%,
  100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-2px);
  }
}

.sidebar-logo {
  animation: logoFloat 3s ease-in-out infinite;
}
</style>
