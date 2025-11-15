<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-white">
    <div class="container">
      <!-- Logo -->
      <router-link to="/" class="navbar-brand">
        <img src="/img/logos/logo-ubo-color.png" alt="Logo UBO" style="height: 60px;" />
      </router-link>

      <!-- Botón hamburguesa en móvil -->
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- Links de navegación -->
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <router-link to="/about" class="nav-link">Nosotros</router-link>
          </li>
          <li class="nav-item">
            <router-link 
              to="/services" 
              class="nav-link"
              @click.prevent="handleClick('/services')">
              Servicios
            </router-link>
          </li>
          <li class="nav-item">
            <router-link 
              to="/cybersecurity" 
              class="nav-link"
              @click.prevent="handleClick('/cybersecurity')">
              Ciberseguridad
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/consejos" class="nav-link">Consejos</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/news" class="nav-link">Noticias</router-link>
          </li>
        </ul>

        <!-- Sección derecha: lupa, barra de búsqueda inline y botón Mesa de Ayuda -->
        <div class="d-flex align-items-center extras">
          <!-- Barra de búsqueda inline -->
          <div class="search-inline d-flex align-items-center" v-if="showSearch">
            <input ref="searchInput" v-model="searchTerm" type="text" class="form-control form-control-sm me-2"
              placeholder="Buscar..." @keyup.enter="doSearch" />
          </div>

          <!-- Botón Mesa de Ayuda TI -->
          <a href="https://serviciosti.ubo.cl/portal/es/home" target="_blank" class="btn btn-primary">
            MESA DE AYUDA TI
          </a>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import UnderConstructionModal from '@/components/UnderConstructionModal.vue'
import { ref } from 'vue'

export default {
  name: 'Navbar',
  components: {
    UnderConstructionModal
  },
  data() {
    return {
      showSearch: false,
      searchTerm: '',
      searchInput: null
    }
  },
  methods: {
    toggleSearch() {
      this.showSearch = !this.showSearch
    },
    doSearch() {
      console.log('Buscando:', this.searchTerm)
    },
    handleClick(path) {
      if (this.$route.path === path) {
        // Si ya estamos en la ruta activa, refresca la página
        window.location.reload()
      } else {
        // Navega normalmente
        this.$router.push(path)
      }
    }
  },
  updated() {
    // Focus en input si showSearch
    if (this.showSearch && this.$refs.searchInput) {
      this.$refs.searchInput.focus()
    }
  }
}
</script>

<style scoped lang="scss">
nav {
  background-color: $secondary-color;
  margin-top: 15px;
  box-shadow: 0px 0px 30px rgba(0,0,0,0.1);
}

.search-inline {
  max-width: 250px;
  margin-right: 30px;
}

.btn-primary {
  background-color: $primary-color;
  border-radius: 25px;
  padding: 10px 22px;
  font-family: Roboto;
  font-weight: 400;
  font-size: 16px;
  line-height: 18.75px;
}

.btn-primary:hover {
  background-color: $secondary-color;
  border-color: $secondary-color;
}

.navbar-brand {
  margin: -2rem 4rem -2rem 0rem;
}

nav {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  margin-bottom: 0.25rem;

  .nav-link {
    text-decoration: none;
    font-family: roboto;
    color: $primary-color;
    font-weight: 500;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    transition: background-color 0.3s ease, color 0.3s ease;

    &:hover {
      color: $secondary-color;
      font-weight: 900;
    }
  }
}

@media (max-width: 950px) {
  .extras {
    display: flex;
    flex-direction: column;
  }
  .search-inline {
    padding: 5px;
    margin-right: 0;
  }
  .search-inline input {
    padding: 5px;
    margin-bottom: 10px;
    margin-right: 0;
  }
  .navbar-brand {
    margin: 1rem;
  }
}
</style>
