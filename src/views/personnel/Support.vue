<script setup>
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
import {
  addTicketReply,
  confirmTicketResolution,
  createSupportTicket,
  deleteSupportTicket,
  getTicketsForUser,
  markTicketRead,
  SUPPORT_UPDATED_EVENT
} from '../../utils/supportTicketService.js'

const props = defineProps({
  currentUser: { type: Object, default: null },
  ICONS: { type: Object, required: true }
})

const STORAGE_KEY = 'firenotify_support_tickets'
const formOpen = ref(false)
const detailsOpen = ref(false)
const selectedTicket = ref(null)
const tickets = ref([])
const search = ref('')
const statusFilter = ref('All')
const priorityFilter = ref('All')
const categoryFilter = ref('All')
const faqSearch = ref('')
const openFaq = ref(null)
const openGuide = ref(null)
const reply = ref('')
const attachment = ref(null)
const relatedModule = ref('')
const relatedRecord = ref('')
const toast = ref('')
const formError = ref('')
let toastTimer = null

const categories = ['Task', 'Activity', 'Report', 'Notification', 'Account', 'System Error', 'Other']
const statuses = ['All', 'Open', 'In Review', 'Waiting for Personnel', 'Resolved', 'Closed']
const priorities = ['All', 'Low', 'Normal', 'High', 'Urgent']
const form = ref({ subject: '', category: '', priority: 'Normal', description: '' })

const faqs = [
  ['How do I complete a task?', 'Open Tasks, choose the assigned task, update its status, and submit the accomplishment when finished.', 'Task'],
  ['How do I submit a report?', 'Open Reports, select the assigned report, attach the supported document, and submit it for review.', 'Report'],
  ['Why was my work returned?', 'Open the task, activity, or report details and review the administrator revision note before resubmitting.', 'Task'],
  ['How do notifications work?', 'Notifications are generated from live assignments, deadlines, returns, and verification events for your account.', 'Notification'],
  ['How do I update my account?', 'Open Settings from the Personnel navigation and update the editable profile and portal preferences.', 'Account']
].map((item, index) => ({ id: index + 1, question: item[0], answer: item[1], category: item[2] }))

const guides = [
  { id: 'task', title: 'How to Complete a Task', steps: ['Open Tasks from the Personnel navigation.', 'Review the due date and instructions.', 'Update the status and submit the accomplishment for verification.'] },
  { id: 'activity', title: 'How to Submit an Activity', steps: ['Open Activities and select the assigned activity.', 'Start the activity and record the accomplishment.', 'Submit it for administrator verification.'] },
  { id: 'report', title: 'How to Submit a Report', steps: ['Open Reports and select an assigned report.', 'Attach a supported PDF, DOC, DOCX, PPT, or PPTX file.', 'Submit the report and monitor its status.'] },
  { id: 'notifications', title: 'How to Check Notifications', steps: ['Open Notifications from the sidebar.', 'Use the unread and type filters.', 'Open a notification to mark it read.'] }
]

const currentUserId = computed(() => props.currentUser?.id || props.currentUser?.userId || props.currentUser?.identifier || props.currentUser?.email || '')
const currentUserName = computed(() => props.currentUser?.name || `${props.currentUser?.firstName || ''} ${props.currentUser?.lastName || ''}`.trim() || props.currentUser?.username || 'Personnel')
const filteredFaqs = computed(() => faqs.filter(item => `${item.question} ${item.answer} ${item.category}`.toLowerCase().includes(faqSearch.value.toLowerCase().trim())))
const filteredTickets = computed(() => {
  const query = search.value.toLowerCase().trim()
  return tickets.value.filter(ticket => {
    const matchesQuery = !query || `${ticket.ticketNumber} ${ticket.subject} ${ticket.category} ${ticket.description}`.toLowerCase().includes(query)
    return matchesQuery && (statusFilter.value === 'All' || ticket.status === statusFilter.value) && (priorityFilter.value === 'All' || ticket.priority === priorityFilter.value) && (categoryFilter.value === 'All' || ticket.category === categoryFilter.value)
  })
})
const stats = computed(() => ({
  total: tickets.value.length,
  open: tickets.value.filter(item => item.status === 'Open').length,
  review: tickets.value.filter(item => item.status === 'In Review' || item.status === 'Waiting for Personnel').length,
  resolved: tickets.value.filter(item => item.status === 'Resolved').length,
  closed: tickets.value.filter(item => item.status === 'Closed').length
}))
const unreadActivity = ticket => (ticket.messages || []).some(message => message.role === 'Admin' && !message.readByPersonnel)

const loadTickets = () => {
  tickets.value = getTicketsForUser(props.currentUser)
  if (selectedTicket.value) selectedTicket.value = tickets.value.find(item => item.id === selectedTicket.value.id) || null
}
const showToast = message => { toast.value = message; clearTimeout(toastTimer); toastTimer = setTimeout(() => { toast.value = '' }, 3000) }
const resetForm = () => { form.value = { subject: '', category: '', priority: 'Normal', description: '' }; attachment.value = null; relatedModule.value = ''; relatedRecord.value = ''; formError.value = '' }
const openCreateTicket = (category = '') => { resetForm(); form.value.category = category; formOpen.value = true }
const selectFaq = category => openCreateTicket(category)
const handleAttachment = event => {
  const file = event.target.files?.[0]
  if (!file) return
  const allowed = /^(image\/(png|jpe?g|webp)|application\/(pdf|msword)|text\/plain|application\/vnd\.openxmlformats-officedocument\.(wordprocessingml\.document|presentationml\.presentation)|application\/vnd\.ms-powerpoint)$/i
  if (!allowed.test(file.type) || file.size > 10 * 1024 * 1024) { formError.value = 'Use an image or document up to 10MB.'; event.target.value = ''; return }
  const reader = new FileReader()
  reader.onload = () => { attachment.value = { name: file.name, type: file.type, size: file.size, data: reader.result } }
  reader.readAsDataURL(file)
}
const submitTicket = () => {
  if (!currentUserId.value) { formError.value = 'Your personnel account could not be identified.'; return }
  if (!form.value.subject.trim() || !form.value.category || !form.value.description.trim()) { formError.value = 'Subject, category, and description are required.'; return }
  createSupportTicket({ user: props.currentUser, subject: form.value.subject, category: form.value.category, priority: form.value.priority, description: form.value.description, attachment: attachment.value, module: relatedModule.value, referenceId: relatedRecord.value })
  formOpen.value = false; loadTickets(); showToast('Support ticket submitted.')
}
const viewTicket = ticket => { selectedTicket.value = ticket; detailsOpen.value = true; markTicketRead({ ticketId: ticket.id, user: props.currentUser }); loadTickets() }
const sendReply = () => { if (!selectedTicket.value || !reply.value.trim()) return; addTicketReply({ ticketId: selectedTicket.value.id, user: props.currentUser, message: reply.value }); reply.value = ''; loadTickets(); selectedTicket.value = tickets.value.find(item => item.id === selectedTicket.value.id); showToast('Reply sent.') }
const confirmResolution = () => { if (!selectedTicket.value) return; confirmTicketResolution({ ticketId: selectedTicket.value.id, user: props.currentUser }); loadTickets(); selectedTicket.value = tickets.value.find(item => item.id === selectedTicket.value.id); showToast('Resolution confirmed.') }
const cancelTicket = ticket => { if (deleteSupportTicket({ ticketId: ticket.id, user: props.currentUser })) { loadTickets(); detailsOpen.value = false; showToast('Support ticket deleted.') } }
const formatDate = value => value ? new Date(value).toLocaleString('en-US', { dateStyle: 'medium', timeStyle: 'short' }) : 'Not recorded'
const statusClass = status => ({ Open: 'bg-blue-50 text-blue-700', 'In Review': 'bg-yellow-50 text-yellow-700', 'Waiting for Personnel': 'bg-orange-50 text-orange-700', Resolved: 'bg-green-50 text-green-700', Closed: 'bg-slate-100 text-slate-600' }[status] || 'bg-slate-100 text-slate-600')
const priorityClass = priority => ({ Low: 'bg-slate-100 text-slate-600', Normal: 'bg-blue-50 text-blue-700', High: 'bg-orange-50 text-orange-700', Urgent: 'bg-red-50 text-red-700' }[priority] || 'bg-slate-100 text-slate-600')
const reportProblem = (module, referenceId) => { relatedModule.value = module; relatedRecord.value = referenceId || ''; openCreateTicket(module === 'Task Management' ? 'Task' : module === 'Activity Management' ? 'Activity' : module === 'Report Management' ? 'Report' : 'Other') }

onMounted(() => { loadTickets(); window.addEventListener(SUPPORT_UPDATED_EVENT, loadTickets); window.addEventListener('storage', loadTickets) })
onBeforeUnmount(() => { window.removeEventListener(SUPPORT_UPDATED_EVENT, loadTickets); window.removeEventListener('storage', loadTickets); clearTimeout(toastTimer) })
</script>

<template>
  <div class="w-full min-w-0 space-y-6">
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5"><div><p class="text-sm font-semibold text-[#8B1E23]">FIRENOTIFY PERSONNEL PORTAL</p><h2 class="text-2xl font-bold text-slate-900 mt-1">Support Center</h2><p class="text-sm text-slate-500 mt-1">Track support requests, get help, and contact the station support team.</p></div><button @click="openCreateTicket()" class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white font-bold hover:bg-[#72181D]">Create Support Ticket</button></div></section>

    <section class="grid grid-cols-2 lg:grid-cols-5 gap-4"><div v-for="item in [['Total', stats.total, 'text-slate-900'], ['Open', stats.open, 'text-blue-700'], ['In Review', stats.review, 'text-yellow-700'], ['Resolved', stats.resolved, 'text-green-700'], ['Closed', stats.closed, 'text-slate-600']]" :key="item[0]" class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm"><p class="text-3xl font-bold" :class="item[2]">{{ item[1] }}</p><p class="text-sm text-slate-500 mt-1">{{ item[0] }}</p></div></section>

    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5"><div class="flex items-center justify-between"><div><h3 class="text-lg font-bold text-slate-900">Support Announcements</h3><p class="text-sm text-slate-500 mt-1">Live notices relevant to the Personnel Portal.</p></div><span class="px-3 py-1 rounded-full bg-slate-100 text-slate-600 text-xs font-bold">Live</span></div><p class="mt-4 text-sm text-slate-500">No current announcements.</p></section>

    <section class="grid grid-cols-1 xl:grid-cols-3 gap-6">
      <div class="xl:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4 border-b border-slate-200 pb-5"><div><h3 class="text-xl font-bold text-slate-900">My Support Tickets</h3><p class="text-sm text-slate-500 mt-1">Only tickets belonging to your account are shown.</p></div><div class="flex flex-wrap gap-2"><input v-model="search" placeholder="Search tickets..." class="px-3 py-2 rounded-xl border border-slate-300 text-sm" /><select v-model="statusFilter" class="px-3 py-2 rounded-xl border border-slate-300 text-sm"><option v-for="item in statuses" :key="item">{{ item }}</option></select></div></div><div class="mt-5 space-y-3"><article v-for="ticket in filteredTickets" :key="ticket.id" class="p-4 rounded-xl border border-slate-200 hover:bg-slate-50"><div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-3"><div><p class="text-xs font-bold text-[#8B1E23]">{{ ticket.ticketNumber }} <span v-if="unreadActivity(ticket)" class="ml-2 px-2 py-0.5 rounded-full bg-red-100 text-red-700">New reply</span></p><h4 class="font-bold text-slate-900 mt-1">{{ ticket.subject }}</h4><p class="text-xs text-slate-500 mt-1">{{ ticket.category }} · {{ formatDate(ticket.updatedAt) }}</p></div><div class="flex items-center gap-2"><span class="px-2.5 py-1 rounded-full text-xs font-bold" :class="priorityClass(ticket.priority)">{{ ticket.priority }}</span><span class="px-2.5 py-1 rounded-full text-xs font-bold" :class="statusClass(ticket.status)">{{ ticket.status }}</span></div></div><div class="flex justify-end gap-2 mt-3"><button @click="viewTicket(ticket)" class="px-3 py-2 rounded-lg border border-slate-300 text-xs font-bold">View Ticket</button><button v-if="ticket.status === 'Open'" @click="cancelTicket(ticket)" class="px-3 py-2 rounded-lg border border-red-200 text-red-700 text-xs font-bold">Delete</button></div></article><div v-if="!filteredTickets.length" class="py-10 text-center text-sm text-slate-500">{{ tickets.length ? 'No support tickets match your search.' : 'You have no support requests.' }}</div></div></div>

      <div class="space-y-6"><div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Search Help</h3><input v-model="faqSearch" placeholder="Search help articles..." class="w-full mt-3 px-3 py-2.5 rounded-xl border border-slate-300 text-sm" /><div class="mt-4 space-y-2"><button v-for="faq in filteredFaqs" :key="faq.id" @click="openFaq = openFaq === faq.id ? null : faq.id" class="w-full text-left p-3 rounded-xl bg-slate-50 border border-slate-200 text-sm font-semibold">{{ faq.question }}<p v-if="openFaq === faq.id" class="font-normal text-xs text-slate-500 mt-2">{{ faq.answer }}</p></button><p v-if="!filteredFaqs.length" class="text-sm text-slate-500">No help articles match your search.</p></div></div><div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6"><h3 class="text-lg font-bold text-slate-900">Quick Guides</h3><div class="mt-4 space-y-2"><button v-for="guide in guides" :key="guide.id" @click="openGuide = openGuide === guide.id ? null : guide.id" class="w-full text-left p-3 rounded-xl bg-slate-50 border border-slate-200 text-sm font-semibold">{{ guide.title }}<ol v-if="openGuide === guide.id" class="mt-2 ml-5 list-decimal text-xs text-slate-500 font-normal space-y-1"><li v-for="step in guide.steps" :key="step">{{ step }}</li></ol></button></div></div></div>
    </section>

    <div v-if="formOpen" class="fixed inset-0 z-50 bg-slate-900/50 flex items-center justify-center p-4" @click.self="formOpen = false"><form @submit.prevent="submitTicket" class="bg-white rounded-2xl shadow-xl w-full max-w-2xl max-h-[90vh] overflow-y-auto p-6 space-y-4"><div class="flex justify-between"><div><p class="text-xs font-bold text-[#8B1E23] uppercase">Support Request</p><h3 class="text-xl font-bold text-slate-900 mt-1">Create Support Ticket</h3></div><button type="button" @click="formOpen = false" class="text-xl text-slate-400">×</button></div><p v-if="formError" class="p-3 rounded-xl bg-red-50 text-red-700 text-sm">{{ formError }}</p><input v-model="form.subject" required placeholder="Subject" class="w-full px-4 py-3 rounded-xl border border-slate-300" /><div class="grid grid-cols-2 gap-3"><select v-model="form.category" required class="px-4 py-3 rounded-xl border border-slate-300"><option value="">Category</option><option v-for="item in categories" :key="item">{{ item }}</option></select><select v-model="form.priority" required class="px-4 py-3 rounded-xl border border-slate-300"><option v-for="item in priorities.slice(1)" :key="item">{{ item }}</option></select></div><div class="grid grid-cols-2 gap-3"><input v-model="relatedModule" placeholder="Related module (optional)" class="px-4 py-3 rounded-xl border border-slate-300" /><input v-model="relatedRecord" placeholder="Reference ID (optional)" class="px-4 py-3 rounded-xl border border-slate-300" /></div><textarea v-model="form.description" required rows="5" placeholder="Describe your concern..." class="w-full px-4 py-3 rounded-xl border border-slate-300 resize-none"></textarea><input type="file" @change="handleAttachment" accept="image/*,.pdf,.doc,.docx,.ppt,.pptx,.txt" class="w-full text-sm" /><p v-if="attachment" class="text-xs text-slate-500">{{ attachment.name }} · {{ Math.round(attachment.size / 1024) }} KB <button type="button" @click="attachment = null" class="text-red-700 font-bold ml-2">Remove</button></p><div class="flex justify-end gap-3"><button type="button" @click="formOpen = false" class="px-4 py-2.5 rounded-xl border border-slate-300 font-bold">Cancel</button><button type="submit" class="px-4 py-2.5 rounded-xl bg-[#8B1E23] text-white font-bold">Submit Ticket</button></div></form></div>

    <div v-if="detailsOpen && selectedTicket" class="fixed inset-0 z-50 bg-slate-900/50 flex items-center justify-center p-4" @click.self="detailsOpen = false"><div class="bg-white rounded-2xl shadow-xl w-full max-w-2xl max-h-[90vh] overflow-y-auto"><div class="p-6 border-b border-slate-200 flex justify-between"><div><p class="text-xs font-bold text-[#8B1E23]">{{ selectedTicket.ticketNumber }}</p><h3 class="text-xl font-bold text-slate-900 mt-1">{{ selectedTicket.subject }}</h3></div><button @click="detailsOpen = false" class="text-xl text-slate-400">×</button></div><div class="p-6 space-y-5"><div class="flex flex-wrap gap-2"><span class="px-3 py-1 rounded-full text-xs font-bold" :class="statusClass(selectedTicket.status)">{{ selectedTicket.status }}</span><span class="px-3 py-1 rounded-full text-xs font-bold" :class="priorityClass(selectedTicket.priority)">{{ selectedTicket.priority }}</span><span class="px-3 py-1 rounded-full bg-slate-100 text-slate-600 text-xs font-bold">{{ selectedTicket.category }}</span></div><p class="text-sm text-slate-600 whitespace-pre-line">{{ selectedTicket.description }}</p><p class="text-xs text-slate-500">Created {{ formatDate(selectedTicket.createdAt) }} · Updated {{ formatDate(selectedTicket.updatedAt) }}<span v-if="selectedTicket.module"> · {{ selectedTicket.module }}</span></p><div class="border-t border-slate-200 pt-4"><h4 class="font-bold text-slate-900">Conversation</h4><div class="mt-3 space-y-3"><div v-for="message in selectedTicket.messages" :key="message.id" class="p-3 rounded-xl" :class="message.role === 'Admin' ? 'bg-blue-50' : 'bg-slate-50'"><p class="text-xs font-bold text-slate-600">{{ message.sender }} · {{ message.role }} · {{ formatDate(message.createdAt) }}</p><p class="text-sm text-slate-700 mt-1 whitespace-pre-line">{{ message.message }}</p></div></div><div v-if="selectedTicket.status !== 'Closed'" class="mt-4 flex gap-2"><input v-model="reply" placeholder="Write a reply..." class="flex-1 px-3 py-2.5 rounded-xl border border-slate-300" /><button @click="sendReply" class="px-4 py-2.5 rounded-xl bg-[#8B1E23] text-white font-bold">Send Reply</button></div></div><button v-if="selectedTicket.status === 'Resolved'" @click="confirmResolution" class="px-4 py-2.5 rounded-xl bg-green-600 text-white font-bold">Confirm Resolution</button></div></div></div>

    <transition name="toast"><div v-if="toast" class="fixed bottom-6 right-6 z-[60] bg-slate-900 text-white px-5 py-3 rounded-xl shadow-xl text-sm font-semibold">{{ toast }}</div></transition>
  </div>
</template>
