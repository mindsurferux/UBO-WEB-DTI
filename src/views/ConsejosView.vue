<template>
  <div class="consejos-view view-fade-in">
    <!-- Sección principal / Hero -->
    <div class="section">
      <div class="about-header container">
        <h2>Consejos y Buenas Prácticas para evitar el Phishing</h2>
        <p>en sistemas TI</p>
      </div>

      <!-- Banner de ancho completo -->
      <div class="banner">
        <img src="/img/banners/banner-consejos.webp" alt="Banner Consejos" class="img-fluid" />
      </div>
    </div>

    <!-- Carrusel de Consejos -->
    <div class="consejos-section">
      <div class="container-ubo">
        <CarruselConsejos :consejos="consejos" />
      </div>
    </div>

    <!-- Sección de Banderas Rojas -->
    <div class="banderas-rojas-section">
      <div class="container">
        <h2>Si detectas "banderas rojas de alerta" en un correo electrónico o mensaje de texto</h2>
        
        <ul class="banderas-list">
          <li>No hagas clic en él.</li>
          <li>No respondas ni reenvíes el correo.</li>
          <li>No abras archivos adjuntos.</li>
          <li>Borra inmediatamente el correo o mensaje.</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import CarruselConsejos from '@/components/CarruselConsejos.vue'
import consejosData from '@/assets/consejos.json'

// Reactive data
const consejos = ref(consejosData)
</script>

<style scoped lang="scss">
.consejos-view {
  min-height: 100vh;
}

// Header styles (reutilizando estilos existentes)
.about-header {
  padding: 20px 20px !important;
  text-align: left;
  
  h2 {
    font-family: 'DM Sans', sans-serif;
    font-weight: 700;
    font-size: 2.5rem;
    color: $primary-color;
    margin-bottom: 0.5rem;
    
    @media (max-width: 768px) {
      font-size: 1.8rem;
    }
  }
  
  p {
    font-size: 1.1rem;
    color: #666;
    font-weight: 300;
  }
}

// Banner styles (reutilizando estilos existentes del proyecto)
.banner {
  width: 100%;
  height: 400px;
  background-color: #ccc;
  margin-bottom: 40px;
  
  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  @media (max-width: 768px) {
    height: 250px;
    margin-bottom: 30px;
  }
  
  @media (max-width: 480px) {
    height: 200px;
    margin-bottom: 20px;
  }
}

// Sección del carrusel
.consejos-section {
  padding: 4rem 0 3rem; // Aumentado para dar espacio a la card destacada
  background: #f8f9fa;
  margin-top: -3rem;
  
  @media (max-width: 768px) {
    padding: 5rem 0 2rem; // Ajustado para mobile
    margin-top: -2rem;
  }
  
  @media (max-width: 480px) {
    padding: 4rem 0 1.5rem; // Ajustado para mobile pequeño
    margin-top: -1.5rem;
  }
}

// Sección de banderas rojas
.banderas-rojas-section {
  padding: 4rem 0;
  background: white;
  text-align: left; // Override global center alignment
  
  h2 {
    font-family: 'DM Sans', sans-serif;
    font-weight: 600;
    font-size: 1.8rem;
    color: $primary-color;
    text-align: left;
    margin-bottom: 2rem;
    max-width: 900px;
    
    @media (max-width: 768px) {
      font-size: 1.4rem;
      margin-bottom: 1.5rem;
    }
  }
  
  .banderas-list {
    list-style-type: disc;
    list-style-position: outside;
    padding-left: 2rem;
    max-width: 900px;
    text-align: left; // Ensure list items are left-aligned
    
    li {
      font-size: 1rem;
      color: $primary-color;
      line-height: 1.8;
      margin-bottom: 0.5rem;
      text-align: left; // Explicitly left-align text
      
      @media (max-width: 768px) {
        font-size: 0.95rem;
      }
    }
  }
}

// La animación de entrada se aplica con la clase global .view-fade-in
</style>
