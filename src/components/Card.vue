<template>
    <div class="card-container">
      <div class="card">
        <!-- Verificar si cardData tiene el nombre -->
        <h3>{{ cardData?.name || 'Sin nombre' }}</h3>
        <p>{{ cardData?.description || 'No hay descripción' }}</p>
        <p><strong>Progreso:</strong> {{ cardData?.progress }}%</p>
        <p><strong>Estado:</strong> {{ cardData?.status }}</p>
  
        <button v-if="isAdmin" @click="editCard">
          <i class="fas fa-pencil-alt"></i> Editar
        </button>
  
        <button v-if="isAdmin" @click="deleteCard">
          <i class="fas fa-trash-alt"></i> Eliminar
        </button>
  
        <button v-if="isAdmin && !cardData.id" @click="addCard">
          <i class="fas fa-plus"></i> Agregar Proyecto
        </button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      cardData: Object,
      isAdmin: Boolean
    },
    methods: {
      editCard() {
        this.$emit('edit', this.cardData);
      },
      deleteCard() {
        if (confirm('¿Estás seguro de eliminar este proyecto?')) {
          this.$emit('delete', this.cardData.id);
        }
      },
      addCard() {
        this.$emit('add');
      }
    }
  };
  </script>
  
  <style scoped>
  .card-container {
    margin: 10px;
    padding: 1rem;
    background-color: #f4f4f4;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    text-align: center;
  }
  
  .card h3 {
    font-size: 1.5rem;
    font-weight: bold;
    color: #003366;
  }
  
  .card p {
    font-size: 1rem;
    color: #666;
  }
  
  button {
    margin-top: 10px;
    padding: 8px 15px;
    cursor: pointer;
    background-color: #007bff;
    color: white;
    border: none;
    font-size: 14px;
    border-radius: 5px;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  
  button i {
    margin-right: 5px;
  }
  </style>
  