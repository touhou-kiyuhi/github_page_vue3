import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import '@/assets/defaultStyle/defaultBodyStyle.css'
import '@/assets/defaultStyle/defaultMainStyle.css'
import '@/assets/defaultStyle/defaultAsideStyle.css'

const app = createApp(App)

app.use(router)

app.mount('#app')
