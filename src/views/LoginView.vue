<template>
  <div class="login-container view-fade-in">
    <!-- Imagen de fondo a pantalla completa -->
    <div class="background"></div>

  <!-- Encabezado -->
  <div class="about-header container">
    <h2>Dirección de Tecnologías de la Información</h2>
    <p>Accede con tu cuenta</p>
  </div>


    <!-- Contenedor central con dos cajas lado a lado -->
    <div class="centered-content">

      <!-- Caja izquierda: solo logo -->
      <div class="left-box shadow">
        <img src="/img/logos/logo-ubo-color.webp" alt="Logo UBO" class="ubo-logo" />
      </div>

      <!-- Caja derecha: formulario de login -->
      <div class="right-box shadow">
        <h5 class="mb-3">
          Te damos la bienvenida al portal
          <strong>UBO TI</strong>
        </h5>

        <!-- Campo Usuario -->
        <div class="mb-3">
          <label for="username" class="form-label">Ingresa tu Usuario</label>
          <div class="input-group">
            <span class="input-group-text bg-white">
              <i class="fa-solid fa-user"></i>
            </span>
            <input v-model="username" id="username" class="form-control" placeholder="ejemplo@ubo.cl" />
          </div>
        </div>

        <!-- Campo Password -->
        <div class="mb-3">
          <label for="password" class="form-label">Ingresa tu Contraseña</label>
          <div class="input-group">
            <span class="input-group-text bg-white">
              <i class="fa-solid fa-lock"></i>
            </span>
            <input v-model="password" id="password" type="password" class="form-control" placeholder="•••••••" />
          </div>
        </div>

        <!-- Olvido de clave -->
        <div class="mb-4">
          <a href="#" class="link-secondary text-decoration-none">
            <small>¿Olvido de clave?</small>
          </a>
        </div>

        <!-- Botón Login -->
        <button @click="login" class="btn btn-primary w-100 mb-2">
          Ingresar
        </button>

        <!-- Mensaje de error -->
        <p v-if="loginError" class="text-danger mb-0">
          Credenciales incorrectas.
        </p>
        <p v-if="domainError" class="text-warning mb-0">
          Solo se permiten cuentas con dominio @ubo.cl
        </p>
      </div>
    </div>

    <!-- Modal de advertencia para dominio no @ubo.cl -->
    <div v-if="showDomainWarning" class="modal fade show d-block" tabindex="-1" style="background-color: rgba(0,0,0,0.5);">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title text-warning">
              <i class="fa-solid fa-exclamation-triangle me-2"></i>
              Acceso Restringido
            </h5>
          </div>
          <div class="modal-body">
            <p>Solo se permite el acceso con cuentas del dominio <strong>@ubo.cl</strong></p>
            <p>Por favor, utiliza tu cuenta institucional de la Universidad Bernardo O'Higgins.</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="showDomainWarning = false">
              Entendido
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal de desarrollo UBO Insight -->
    <div v-if="showDevelopmentModal" class="modal fade show d-block" tabindex="-1" style="background-color: rgba(0,0,0,0.5);">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title text-info">
              <i class="fa-solid fa-info-circle me-2"></i>
              UBO Insight - En Desarrollo
            </h5>
          </div>
          <div class="modal-body">
            <p>La aplicación <strong>UBO Insight</strong> se encuentra actualmente en desarrollo.</p>
            <p>Las funcionalidades de autenticación y verificación están siendo implementadas.</p>
            <p>Pronto estará disponible con todas sus características completas.</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary" @click="showDevelopmentModal = false">
              Continuar
            </button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>

import usuarios from '@/assets/usuarios.json'

export default {
  name: 'LoginView',
  data() {
    return {
      username: '',
      password: '',
      loginError: false,
      domainError: false,
      showDomainWarning: false,
      showDevelopmentModal: false
    }
  },
  methods: {
    login() {
      // Limpiar errores previos
      this.loginError = false
      this.domainError = false
      
      // Verificar si el usuario está en la lista de excepciones (usuarios.json)
      const user = usuarios.find(
        u => u.username === this.username && u.password === this.password
      )
      
      if (user) {
        // Usuario válido de la lista de excepciones
        this.showDevelopmentModal = true
        setTimeout(() => {
          localStorage.setItem('user', JSON.stringify(user))
          this.$router.push('/dashboard')
        }, 2000) // Esperar 2 segundos después de cerrar el modal
        return
      }
      
      // Verificar dominio @ubo.cl para otros usuarios
      if (!this.username.includes('@ubo.cl')) {
        this.domainError = true
        this.showDomainWarning = true
        return
      }
      
      // Si llega aquí, es dominio @ubo.cl pero no está en usuarios.json
      // Mostrar modal de desarrollo
      this.showDevelopmentModal = true
    }
  }
}
</script>

<style scoped lang="scss">
/* 
  ===== Contenedor general =====
  Ocupa toda la pantalla para mostrar la imagen de fondo. 
*/
.login-container {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
  /* evitar scroll si no es necesario */
}



/* 
  ===== Imagen de fondo =====
  Ocupa todo el contenedor, en capa trasera. 
*/
.background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: url('../assets/img/img20.webp') center center / cover no-repeat;
  z-index: 1;
}

/* Encabezado - Override estilos globales */
.login-container .about-header {
  text-align: left;
  position: relative;
  z-index: 2;
  margin-bottom: -10rem;
}

.about-header h2 {
  color: $primary-color;
}

.about-header p {
  color: $primary-color;
}
@media (max-width: 992px) {
  .login-container .about-header {
    text-align: center;
    margin-bottom: -6rem;
  }
  .login-container {
    height: 110vh;
  }
}


/* 
  ===== Contenido centrado =====
  Caja flexible que centra vertical y horizontalmente.
  Ponemos z-index superior para que quede "encima" de la imagen de fondo.
*/
.centered-content {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  /* espacio entre las dos cajas */
  height: 100%;
  /* para ocupar todo el alto y centrar verticalmente */
  padding: 0 2rem;
  /* margen lateral si deseas */
}

/* 
  ===== Caja izquierda: solo el logo =====
*/
.left-box {
  background: #fff;
  border-radius: 8px;
  padding: 4rem;
  display: flex;
  /* para centrar el logo vertical y horizontal */
  align-items: center;
  justify-content: center;
  min-height: 390px;
  min-width: 360px;
}

/* Ajusta el tamaño del logo a tu gusto */
.ubo-logo {
  max-width: 220px;
}

/* 
  ===== Caja derecha: formulario de login =====
*/
.right-box {
  background: #fff;
  border-radius: 8px;
  padding: 2rem;
  width: 360px;
  /* Ajusta el ancho preferido para el formulario */
  color: $primary-color;
}

.right-box h5 {
  font-family: Roboto;
  font-weight: 400;
  font-size: 24px;
  line-height: 28.13px;
  letter-spacing: 0%;
  text-align: left;
}

.right-box .form-control {
  font-family: Roboto;
  font-weight: 300;
  font-size: 16px;
  line-height: 18.75px;
  letter-spacing: 0%;
  color: #5CBDE0;
  ;
}

/* ==== Ajuste Responsivo ==== */
@media (max-width: 767px) {
  .centered-content {
    flex-direction: column;
    /* Cambia de lado a lado a apilado */
    gap: 1rem;
    /* Reduce el espacio entre el logo y el formulario */
    padding: 1rem;
    /* Ajusta el padding para evitar bordes pegados */
    justify-content: center;
    padding: 0;
  }

  .left-box {
    width: 100%;
    /* Ocupa todo el ancho disponible */
    padding: 1.5rem;
    /* Ajuste del padding */
    max-width: 360px;
    min-height: 200px;
  }

  .right-box {
    width: 100%;
    /* Ocupa todo el ancho */
    max-width: 360px;
    /* No crece demasiado en pantallas grandes */
  }
}

button {
  background-color: $secondary-color;
  border-color: $secondary-color;
}

button:hover {
  background-color: $primary-color;
  border-color: $primary-color;
}
</style>