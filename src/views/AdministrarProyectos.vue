<template>
  <div class="admin-projects view-fade-in">
    <h1>Administrar Proyectos</h1>

    <!-- Mostrar proyectos en tarjetas -->
    <div class="projects-list">
      <Card 
        v-for="project in proyectos" 
        :key="project.id" 
        :cardData="project" 
        :isAdmin="isAdmin"
        @edit="editProject"
        @delete="deleteProject"
      />
    </div>

    <!-- Botón para agregar un nuevo proyecto -->
    <button @click="showAddModal = true">Agregar Proyecto</button>

    <!-- Modal de edición de proyecto -->
    <EditProjectModal 
      v-if="showEditModal" 
      :projectData="selectedProject" 
      @close="closeEditModal" 
      @updateProject="updateProject"
      @deleteProject="deleteProject"
    />

    <!-- Modal para agregar un nuevo proyecto -->
    <AddProjectModal 
      v-if="showAddModal" 
      @close="closeAddModal" 
      @addProject="addProject"
    />
  </div>
</template>

<script>
import Card from "@/components/Card.vue";
import EditProjectModal from "@/components/EditProjectModal.vue";
import AddProjectModal from "@/components/AddProjectModal.vue";

export default {
  name: "AdministrarProyectos",
  components: { Card, EditProjectModal, AddProjectModal },
  data() {
    return {
      isAdmin: true,  // Define si el usuario tiene privilegios de admin
      proyectos: [],  // Inicialmente está vacío, se cargará desde localStorage o desde proyectos.json
      selectedProject: null,  // Proyecto seleccionado para editar
      showEditModal: false,  // Controlar la visibilidad del modal de edición
      showAddModal: false  // Controlar la visibilidad del modal de agregar
    };
  },
  created() {
    // Intentamos cargar los proyectos desde localStorage
    const storedProjects = JSON.parse(localStorage.getItem('proyectos'));

    // Si localStorage está vacío, cargamos los datos desde proyectos.json (simulando la carga desde un archivo)
    if (!storedProjects || storedProjects.length === 0) {
      // Cargar los proyectos desde proyectos.json (de manera simulada)
      fetch('/path/to/proyectos.json')
        .then(response => response.json())
        .then(data => {
          this.proyectos = data;
          // Guardar los proyectos en localStorage para la próxima vez
          localStorage.setItem('proyectos', JSON.stringify(this.proyectos));
        })
        .catch(error => {
          console.error('Error cargando proyectos.json:', error);
          this.proyectos = [];  // En caso de que no haya proyectos.json, asignar arreglo vacío
        });
    } else {
      this.proyectos = storedProjects;
    }
  },
  methods: {
    editProject(project) {
      this.selectedProject = project;
      this.showEditModal = true;  // Mostrar el modal de edición
    },
    deleteProject(projectId) {
      const confirmed = confirm("¿Estás seguro de eliminar este proyecto?");
      if (confirmed) {
        this.proyectos = this.proyectos.filter(project => project.id !== projectId);
        localStorage.setItem('proyectos', JSON.stringify(this.proyectos)); // Actualizar localStorage
      }
    },
    addProject(newProject) {
      newProject.id = Date.now();  // Asignar un ID único al nuevo proyecto
      this.proyectos.push(newProject);  // Agregar el nuevo proyecto a la lista
      localStorage.setItem('proyectos', JSON.stringify(this.proyectos)); // Guardar en localStorage
      this.closeAddModal();
    },
    updateProject(updatedProject) {
      const index = this.proyectos.findIndex(project => project.id === updatedProject.id);
      if (index !== -1) {
        this.proyectos[index] = updatedProject;  // Actualizar los datos del proyecto
        localStorage.setItem('proyectos', JSON.stringify(this.proyectos)); // Guardar en localStorage
      }
      this.closeEditModal();
    },
    closeEditModal() {
      this.showEditModal = false;  // Cerrar el modal de edición
    },
    closeAddModal() {
      this.showAddModal = false;  // Cerrar el modal de agregar
    }
  }
};
</script>

<style scoped>
/* Estilos para la vista de administración de proyectos */
.admin-projects {
  padding: 20px;
}
.projects-list {
  display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-top: 2rem;
    padding: 1rem;
}
button {
  margin-top: 20px;
  padding: 10px 20px;
  cursor: pointer;
  background-color: #8f8f8f;
  color: white;
  border: none;
  border-radius: 5px;
}
button:hover {
  background-color: #9a9a9a;
}
</style>
