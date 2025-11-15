  <template>
    <div id="app">
      <!-- Navegación -->
       <Navbar  />
    <router-view />

      <Footer />
    </div>
  </template>


  <script>
  import Navbar from './components/Navbar.vue';
  import Footer from './components/Footer.vue';

  export default {
    name: "App",
    components: { Navbar, Footer }
  };

  </script>


  <style lang="scss">
  @import "./assets/styles/main.scss";
  /* Estilos del contenedor */
  #app {
    text-align: center;
  }
  </style>
