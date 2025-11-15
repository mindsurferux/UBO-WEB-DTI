<template>
  <div class="home-container view-fade-in">

    <!-- ====================== HERO / PROYECTOS TI ====================== -->
    <section class="hero-section container mb-3">
      <!-- Encabezado -->
      <div class="hero-header">
        <h1 class="hero-title">Nuestros proyectos TI</h1>
        <p class="hero-subtitle">destacados este año 2024</p>
      </div>

      <!-- Imagen principal con slider -->
      <div class="hero-image-container position-relative">
        <img :src="heroSlides[currentSlideIndex].image" :alt="heroSlides[currentSlideIndex].title" class="img-fluid hero-image" />

        <!-- Pestañas en el pie de la imagen con contenido dinámico -->
        <div class="hero-tabs">
          <!-- Primera pestaña (color primario) -->
          <div class="tab-item tab-item-left">
            {{ heroSlides[currentSlideIndex].title }}
          </div>

          <!-- Segunda pestaña (color secundario o claro) -->
          <div class="tab-item tab-item-right">
            {{ heroSlides[currentSlideIndex].subtitle }}
          </div>
        </div>
      </div>

      <!-- Dots de navegación fuera del contenedor de imagen -->
      <div class="slider-dots-container">
        <div class="slider-dots">
          <span 
            v-for="(slide, index) in heroSlides" 
            :key="index"
            class="dot"
            :class="{ active: currentSlideIndex === index }"
            @click="goToSlide(index)"
          ></span>
        </div>
      </div>
    </section>



    <!-- ====================== INDICADOR DE GESTIÓN SEMANAL ====================== -->
    <section class="container titulo-gestion-semanal">
      <div class="row mb-5">
        <div class="col">
          <hr />
          <h2 class="section-title">Indicador de gestión semanal</h2>
          <p class="section-subtitle">destacados este semestre</p>
        </div>
      </div>

      <!-- Contenedor de tarjetas -->
      <div class="row justify-content-center tarjetas-indicadores">
        <!-- Tarjeta 1 -->
        <div class="col-12 col-sm-6 col-md-4 d-flex justify-content-center">
          <div class="indicator-card">
            <h3 class="indicator-number">
              <span v-if="isLoadingIndicadores">...</span>
              <span v-else>{{ indicadores.ticketsIngresados }}</span>
            </h3>
            <p class="indicator-label">TICKET INGRESADOS</p>
          </div>
        </div>
        <!-- Tarjeta 2 -->
        <div class="col-12 col-sm-6 col-md-4 d-flex justify-content-center">
          <div class="indicator-card">
            <h3 class="indicator-number">
              <span v-if="isLoadingIndicadores">...</span>
              <span v-else>{{ indicadores.ticketsEnAtencion }}</span>
            </h3>
            <p class="indicator-label">TICKET EN ATENCIÓN</p>
          </div>
        </div>
        <!-- Tarjeta 3 -->
        <div class="col-12 col-sm-6 col-md-4 d-flex justify-content-center">
          <div class="indicator-card">
            <h3 class="indicator-number">
              <span v-if="isLoadingIndicadores">...</span>
              <span v-else>{{ indicadores.ticketsResueltos }}</span>
            </h3>
            <p class="indicator-label">TICKET RESUELTOS</p>
          </div>
        </div>
      </div>
    </section>


  </div>
</template>

<script>
import heroSlidesData from '@/assets/heroSlides.json'
import indicadoresService from '@/services/indicadoresService.js'

export default {
  name: 'HomeView',
  data() {
    return {
      heroSlides: heroSlidesData,
      currentSlideIndex: 0,
      autoSlideInterval: null,
      touchStartX: 0,
      touchEndX: 0,
      indicadores: {
        ticketsIngresados: 0,
        ticketsEnAtencion: 0,
        ticketsResueltos: 0,
        fechaActualizacion: ''
      },
      isLoadingIndicadores: true
    }
  },
  mounted() {
    this.startAutoSlide()
    this.loadIndicadores()
    this.setupTouchEvents()
  },
  beforeUnmount() {
    this.stopAutoSlide()
    this.removeTouchEvents()
  },
  methods: {
    goToSlide(index) {
      this.currentSlideIndex = index
      this.resetAutoSlide()
    },
    nextSlide() {
      this.currentSlideIndex = (this.currentSlideIndex + 1) % this.heroSlides.length
    },
    startAutoSlide() {
      this.autoSlideInterval = setInterval(() => {
        this.nextSlide()
      }, 5000) // Cambio automático cada 5 segundos
    },
    stopAutoSlide() {
      if (this.autoSlideInterval) {
        clearInterval(this.autoSlideInterval)
      }
    },
    resetAutoSlide() {
      this.stopAutoSlide()
      this.startAutoSlide()
    },
    async loadIndicadores() {
      try {
        this.isLoadingIndicadores = true
        this.indicadores = await indicadoresService.getIndicadores()
      } catch (error) {
        console.error('Error cargando indicadores:', error)
      } finally {
        this.isLoadingIndicadores = false
      }
    },
    // Touch gestures para mobile
    handleTouchStart(e) {
      this.touchStartX = e.touches[0].clientX
    },
    handleTouchMove(e) {
      this.touchEndX = e.touches[0].clientX
    },
    handleTouchEnd() {
      const swipeThreshold = 50
      const diff = this.touchStartX - this.touchEndX
      
      if (Math.abs(diff) > swipeThreshold) {
        if (diff > 0) {
          // Swipe left - next slide
          this.nextSlide()
        } else {
          // Swipe right - previous slide
          this.prevSlide()
        }
        this.resetAutoSlide()
      }
      
      this.touchStartX = 0
      this.touchEndX = 0
    },
    prevSlide() {
      if (this.currentSlideIndex > 0) {
        this.currentSlideIndex--
      } else {
        this.currentSlideIndex = this.heroSlides.length - 1
      }
    },
    setupTouchEvents() {
      const heroImage = document.querySelector('.hero-image-container')
      if (heroImage) {
        heroImage.addEventListener('touchstart', this.handleTouchStart, { passive: true })
        heroImage.addEventListener('touchmove', this.handleTouchMove, { passive: true })
        heroImage.addEventListener('touchend', this.handleTouchEnd)
      }
    },
    removeTouchEvents() {
      const heroImage = document.querySelector('.hero-image-container')
      if (heroImage) {
        heroImage.removeEventListener('touchstart', this.handleTouchStart)
        heroImage.removeEventListener('touchmove', this.handleTouchMove)
        heroImage.removeEventListener('touchend', this.handleTouchEnd)
      }
    }
  }
}
</script>

<style scoped lang="scss">
/* 
   ====== CONTENEDOR GENERAL ====== 
   Ajusta márgenes / fondos globales aquí
*/
.home-container {
  background-color: #fff;
  /* Ajusta tu fondo general si lo necesitas */
}

/* 
   ====== HERO SECTION ====== 
*/
.hero-section {
  padding-top: 1rem;
}

/* Títulos de la sección Hero */
.hero-title {
  font-size: 1.75rem;
  font-weight: 700;
  color: $text-color;
  /* Ajusta al color corporativo */
  text-align: left;

  font-family: Roboto;
  font-weight: 700;
  font-size: 32px;
  line-height: 37.5px;

}

.hero-subtitle {
  font-size: 1rem;
  color: $text-color;
  margin-bottom: 1rem;
  text-align: left;

  font-family: Roboto;
  font-weight: 400;
  font-size: 24px;
  line-height: 28.13px;

}

.hero-image-container {
  position: relative;
  /* Mantiene una relación de aspecto 16:9 para la sección hero */
  aspect-ratio: 2.34 / 1;
  border-radius: 12px;
  overflow: hidden;
  touch-action: pan-y; /* Permite scroll vertical pero captura swipe horizontal */
  cursor: grab;
  user-select: none;
  /* O un max-width: 100%; si quieres asegurar que no exceda el ancho del contenedor padre */
  
  &:active {
    cursor: grabbing;
  }
}

/* Estilos del slider - dots de navegación */
.slider-dots-container {
  display: flex;
  justify-content: flex-end;
  margin-top: 15px;
  padding-right: 20px;
}

.slider-dots {
  display: flex;
  gap: 10px;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background-color: $primary-color;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.dot.active {
  background-color: $secondary-color;
}

.dot:hover {
  background-color: $secondary-color;
}

.hero-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  /* recorta la imagen para llenar el contenedor */
  display: block;
  border-radius: 12px;
  transition: opacity 0.5s ease-in-out;
}


/* Botón "VER PROYECTO" flotando en la esquina superior derecha */
.btn-ver-proyecto {
  position: absolute;
  top: 1rem;
  right: 1rem;
  font-size: 0.9rem;
  border-radius: 8px;
  /* Usa tu color preferido, .btn-light es un ejemplo */
  box-shadow: 0px 4px 4px 0px #00000040;


}

.hero-section.container {
  padding-left: 0 !important;
  padding-right: 0 !important;
}

/* 
   ====== PESTAÑAS AL PIE DE LA IMAGEN ====== 
   */

.hero-tabs {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  display: flex;
  background-color: #f4f4f4;
}

/* Estilo genérico para ambas pestañas */
.tab-item {
  padding: 1.2rem 1rem;
  text-align: center;
  font-family: Roboto;
  font-weight: 400;
  font-size: clamp(18px, 2.5vw, 28px);
  line-height: 1.2;
  align-self: flex-end;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 80px;
  word-wrap: break-word;
  hyphens: auto;
}

/* Primera pestaña: color primario (fondo azul, texto blanco, flexible) */
.tab-item-left {
  background-color: #0d2c5b;
  color: #fff;
  flex: 0 1 auto;
  min-width: 25%;
  max-width: 45%;
  border-top-right-radius: 12px;
}

/* Segunda pestaña: color secundario (fondo claro, texto azul, flexible) */
.tab-item-right {
  background-color: #f4f4f4;
  color: #0d2c5b;
  flex: 1 1 auto;
  min-width: 55%;
}


hr {
  /* Quita el borde default y define uno superior */
  border: none;
  border-top: 3px solid $secondary-color;
  /* Haz que el hr ocupe todo el espacio sobrante */
  // flex: 1;
  /* Separación a izquierda/derecha del botón, por ejemplo */
  // margin-left: 70px;
  margin-right: 70vw;
  margin-bottom: 3rem;

}


/* indicadores*/

.titulo-gestion-semanal {
  text-align: left;
  color: $text-color;

}

.titulo-gestion-semanal .section-title {
  font-family: Roboto;
  font-weight: 700;
  font-size: 32px;
  line-height: 37.5px;
}

.titulo-gestion-semanal .section-subtitle {
  font-family: Roboto;
  font-weight: 400;
  font-size: 24px;
  line-height: 28.13px;
}

.tarjetas-indicadores {
  display: flex;
  justify-content: center;
  /* Centra todas las tarjetas */
  align-items: center;
  flex-wrap: nowrap;
  /* Evita que una tarjeta baje de línea en desktop */
  gap: 3rem;
  /* Ajusta el espacio entre las tarjetas */
  max-width: 1000px;
  /* Asegura que las tarjetas se distribuyan correctamente */
  margin: 0 auto;
  /* Centra el contenedor */
  margin-bottom: 100px;
}

/* Ajusta el tamaño y evita que las tarjetas sean demasiado pequeñas */
.indicator-card {
  background-color: $background-color;
  color: $primary-color;
  border-radius: 15px;
  max-width: 320px;
  /* Asegura que sean más grandes */
  width: 100%;
  min-height: 140px;
  text-align: center;
  // box-shadow: 0 4px 10px 0 rgba(0, 0, 0, 0.102);
  box-shadow: 0px 4px 20px 0px #0000001A;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  padding: 1.5rem;
}

/* Corrección para pantallas medianas */
@media (max-width: 1024px) {
  .tarjetas-indicadores {
    flex-wrap: wrap;
    /* Permite que las tarjetas se acomoden correctamente */
    justify-content: center;
    align-items: center;
  }

}

/* Responsividad para mobile */
@media (max-width: 768px) {
  .tarjetas-indicadores {
    flex-direction: column;
    align-items: center;
  }
  .titulo-gestion-semanal {
  text-align: center;
  }
}



.indicator-number {
  font-family: Roboto;
  font-weight: 700;
  font-size: 64px;
  line-height: 75px;
  letter-spacing: 0%;

}

.indicator-label {
  font-family: Roboto;
  font-weight: 400;
  font-size: 24px;
  line-height: 28.13px;
  letter-spacing: 0%;

}

@media (max-width: 768px) {
  .hero-section {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .hero-title {
    font-size: 1.5rem;
    text-align: center;
  }

  .hero-subtitle {
    font-size: 0.9rem;
    text-align: center;
  }

  .hero-image-container {
    width: 100%;
    height: 70vh;
    aspect-ratio: unset;
    position: relative;
  }

  .hero-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  /* Ajustes para dots en mobile */
  .slider-dots-container {
    padding-right: 15px;
    margin-top: 10px;
  }

  /* 🔥 Asegurar que las pestañas estén por encima de la imagen */
  .hero-tabs {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    z-index: 20;
    display: flex;
    flex-direction: column;
    background-color: rgba(255, 255, 255, 0.95);
    padding: 0.8rem;
    text-align: center;
  }

  .tab-item {
    font-size: clamp(16px, 4vw, 20px);
    padding: 0.8rem 0.5rem;
    min-height: 60px;
    line-height: 1.1;
  }

  .tab-item-left,
  .tab-item-right {
    width: 100%;
    border-radius: 8px;
    margin-bottom: 0.5rem;
    min-width: unset;
    max-width: unset;
    flex: none;
  }

  .tab-item-left {
    border-top-right-radius: 8px;
  }
}
</style>
