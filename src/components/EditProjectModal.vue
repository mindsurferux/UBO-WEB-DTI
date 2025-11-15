<template>
  <div class="modal-overlay">
    <div class="modal-content">
      <h3>Editar Proyecto: {{ projectData?.name }}</h3>

      <!-- Resumen de datos -->
      <p><strong>Descripción:</strong> {{ projectData?.description }}</p>
      <p><strong>Progreso:</strong> {{ projectData?.progress }}%</p>
      <p><strong>Estado:</strong> {{ projectData?.status }}</p>

      <!-- Formulario de edición -->
      <form @submit.prevent="saveChanges">
        <div>
          <label for="name">Nombre del Proyecto:</label>
          <input v-model="editedProject.name" type="text" id="name" required />
        </div>

        <div>
          <label for="description">Descripción:</label>
          <textarea v-model="editedProject.description" id="description" required></textarea>
        </div>

        <div>
          <label for="progress">Progreso (%):</label>
          <input v-model="editedProject.progress" type="number" id="progress" min="0" max="100" required />
        </div>

        <div>
          <label for="status">Estado:</label>
          <select v-model="editedProject.status" id="status" required>
            <option value="Activo">Activo</option>
            <option value="En Progreso">En Progreso</option>
            <option value="Finalizado">Finalizado</option>
          </select>
        </div>

        <button type="submit">Guardar Cambios</button>
      </form>

      <!-- Botón de eliminar -->
      <button @click="deleteProject">Eliminar Proyecto</button>

      <!-- Botón de cerrar -->
      <button @click="closeModal">Cerrar</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    projectData: Object // Recibe los datos del proyecto seleccionado para editar
  },
  data() {
    return {
      editedProject: { ...this.projectData } // Crear una copia para modificar sin afectar los datos originales
    };
  },
  methods: {
    saveChanges() {
      this.$emit('updateProject', this.editedProject); // Emitir evento con los cambios
      this.closeModal();
    },
    deleteProject() {
      if (confirm("¿Estás seguro de eliminar este proyecto?")) {
        this.$emit('deleteProject', this.editedProject.id); // Emitir evento para eliminar el proyecto
        this.closeModal();
      }
    },
    closeModal() {
      this.$emit('close'); // Cerrar el modal
    }
  }
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  width: 500px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

form div {
  margin-bottom: 15px;
}

form label {
  display: block;
  margin-bottom: 5px;
}

form input,
form textarea,
form select {
  width: 100%;
  padding: 8px;
  margin-top: 5px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  border-radius: 5px;
}

button:hover {
  background-color: #0056b3;
}
</style>
