<template>
  <div v-if="show" class="modal-backdrop">
    <div class="modal-content">
      <button class="close-button" @click="closeModal">&times;</button>
      <h2 class="mb-3">En construcción</h2>
      <p>Estamos trabajando en esta funcionalidad. ¡Vuelve pronto!</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "UnderConstructionModal",
  props: {
    show: {
      type: Boolean,
      default: false
    }
  },
  emits: ["close"],
  methods: {
    closeModal() {
      this.$emit("close"); // Emite un evento para que el padre oculte el modal
    }
  }
};
</script>

<style scoped>
.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.modal-content {
  background: #fff;
  width: 90%;
  max-width: 500px;
  padding: 1.5rem;
  border-radius: 8px;
  position: relative;
}

.close-button {
  background: none;
  border: none;
  font-size: 1.5rem;
  position: absolute;
  right: 1rem;
  top: 1rem;
  cursor: pointer;
}
</style>
