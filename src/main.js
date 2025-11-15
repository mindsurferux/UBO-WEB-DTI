// Importa el archivo SCSS personalizado
import './assets/styles/main.scss';

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// Importa el CSS de Bootstrap
import 'bootstrap/dist/css/bootstrap.min.css';

// (Opcional) Importa el JS de Bootstrap si necesitas funcionalidades interactivas
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

createApp(App).use(store).use(router).mount('#app')
