<template>
  <div class="row">
    <!-- Recorremos los servicios -->
    <div
      v-for="(service, index) in services"
      :key="index"
      class="col-lg-4 col-md-6 col-sm-12 mb-4"
    >
      <!-- Tarjeta personalizada -->
      <div class="service-card" @click="selectCard(index)">
        <!-- Imagen superior -->
        <div class="image-container">
          <img
            :src="service.image"
            alt="Imagen del servicio"
            class="img-fluid"
          />
        </div>
        <!-- Área inferior con el nombre y el botón "+" -->
        <div class="label-area">
          <span class="service-name">
            {{ service.name }}
          </span>
          <div class="plus-btn" @click.stop="selectCard(index)">
            <i class="fa fa-plus"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue'

const props = defineProps({
  services: {
    type: Array,
    required: true,
  },
})

const emits = defineEmits(['selectService'])

function selectCard(index) {
  // Emitimos al padre qué tarjeta se seleccionó
  emits('selectService', index)
}
</script>

<style scoped>
.service-card {
  /* Forzamos un tamaño fijo de 305x305 */
  width: 305px;
  height: 305px;
  border-radius: 16px;
  overflow: hidden;
  background-color: #fff;
  cursor: pointer;
  position: relative;
  transition: transform 0.2s ease;
  margin: 0 auto; /* Para centrar en su columna si gustas */
  box-shadow: 1px 1px 6px rgba(0, 0, 0, 0.1);
}

/* Al hacer hover, se eleva un poco */
.service-card:hover {
  transform: translateY(-4px);
}

/* Contenedor de la imagen: ocupará el 70% superior (ajusta según tus gustos) */
.image-container {
  width: 100%;
  height: 80%;
}

/* Imagen con object-fit cover para que rellene su contenedor sin deformarse */
.image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* Zona inferior (30% restante) para el nombre y el botón "+" */
.label-area {
  height: 20%;
  position: relative;
  background: #fff;
  padding: 0.75rem 1rem;
  border-bottom-left-radius: 16px;
  border-bottom-right-radius: 16px;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Estilo del nombre */
.service-name {
  font-size: 1rem;
  font-weight: 500;
  color: #0d2c5b; /* Ajusta al color corporativo */
  text-align: left;
}

/* Botón "+" flotante a la derecha */
.plus-btn {
  position: absolute;
  right: 1rem;
  background: #fff;
  border-radius: 8px;
  width: 32px;
  height: 32px;
  top: 50%;
  transform: translateY(-150%);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.plus-btn i {
  color: #1ea3e1;
  font-size: 1.1rem;
}

</style>
