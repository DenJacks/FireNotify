import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

if (import.meta.env.DEV && window.location.hostname === 'localhost') {
	const canonicalUrl = new URL(window.location.href)
	canonicalUrl.hostname = '127.0.0.1'
	window.location.replace(canonicalUrl.href)
} else {
	createApp(App).mount('#app')
}