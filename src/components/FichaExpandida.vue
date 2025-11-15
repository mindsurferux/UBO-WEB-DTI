<template>
  <transition name="modal">
    <div v-if="visible" class="modal-overlay">
      <div class="modal-content">
        <!-- Botón para cerrar -->
        <button class="close-button" @click="close">&times;</button>

        <!-- Encabezado con banner e imagen de perfil -->
        <div class="modal-header-banner">
          <img :src="user.image" alt="Foto de usuario" class="profile-pic" />
        </div>

        <!-- Contenido de la ficha -->
        <div class="modal-body">
          <h3>{{ user.name }}</h3>
          <h4>{{ user.role }}</h4>
          <p><strong>Departamento:</strong> {{ user.department }}</p>
          <p><strong>Email:</strong> {{ user.email }}</p>
          <p><strong>Teléfono:</strong> {{ user.phone }}</p>
          <p class="description">{{ user.description }}</p>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'FichaExpandida',
  props: {
    user: {
      type: Object,
      default: () => ({})
    },
    visible: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    close() {
      this.$emit('close');
    }
  }
};
</script>

<style scoped>
/* Transición del modal */
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.2s;
}
.modal-enter,
.modal-leave-to {
  opacity: 0;
}

/* Overlay */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0,0,0,0.4);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

/* Contenido principal del modal */
.modal-content {
  background: #fff;
  width: 90%;
  max-width: 500px;
  position: relative;
  border-radius: 8px;
  overflow: hidden; /* Para que el banner no sobresalga */
}

/* Botón de cierre (con hitbox centrada) */
.close-button {
  position: absolute;
  top: 10px;
  right: 15px;
  background: none;
  border: none;
  font-size: 1.6rem;
  cursor: pointer;
  line-height: 1;
  width: 32px;
  height: 32px;
  color: #666;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 3;
}
.close-button:hover {
  color: #111;
}

/* Banner de encabezado */
.modal-header-banner {
  width: 100%;
  height: 120px;
  background: grey; /* Cambia la imagen según tu gusto, cambiar a una url */
  position: relative;
}

/* Imagen de perfil superpuesta sobre el banner */
.profile-pic {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  position: absolute;
  bottom: -60px; /* Sobrepasa la altura del banner a la mitad */
  left: 50%;
  transform: translateX(-50%);
  border: 4px solid #fff; /* Borde para resaltar la foto */
}

/* Contenido textual debajo de la imagen */
.modal-body {
  margin-top: 60px; /* Deja espacio para la imagen superpuesta */
  padding: 20px;
  text-align: center;
}

.modal-body h3 {
  margin: 5px 0;
  font-size: 1.2rem;
}
.modal-body h4 {
  margin: 5px 0 15px 0;
  font-size: 1rem;
  color: #666;
}
.modal-body p {
  margin: 5px 0;
  font-size: 0.9rem;
}
.description {
  margin-top: 15px;
  text-align: justify;
}
</style>
