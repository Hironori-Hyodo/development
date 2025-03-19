import { createApp } from 'vue'
import App from './App.vue'
import './reset.css'
import router from './router/index'
import './style.css'



// Vuetifyのインポート
import { createVuetify } from 'vuetify'



const app = createApp(App)
const vuetify = createVuetify()

app.use(router)
app.use(vuetify)
app.mount("#app")