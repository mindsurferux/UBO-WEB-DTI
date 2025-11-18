<template>
  <div class="carrusel-container">
    <div class="carrusel-wrapper">
      <!-- Navegación izquierda -->
      <button 
        class="nav-btn nav-prev" 
        @click="prevSlide"
      >
        <i class="fas fa-chevron-left"></i>
      </button>

      <!-- Cards del carrusel -->
      <div class="carrusel-content">
        <div 
          v-for="(consejo, index) in consejos" 
          :key="consejo.id"
          class="card-consejo"
          :class="{
            'active': index === currentIndex,
            'prev': index === getPrevIndex(currentIndex),
            'next': index === getNextIndex(currentIndex),
            'hidden': !isVisible(index, currentIndex)
          }"
          @click="selectCard(index)"
          :style="{ backgroundImage: `url(${consejo.image})` }"
        >
          <div class="card-text-box">
            <div class="card-content">
              <h3 class="card-title" :class="{ 'show': index === currentIndex }">{{ consejo.title }}</h3>
              <transition name="description-fade">
                <div class="card-description" v-if="index === currentIndex">
                  <p>{{ consejo.description }}</p>
                </div>
              </transition>
            </div>
          </div>
        </div>
      </div>

      <!-- Navegación derecha -->
      <button 
        class="nav-btn nav-next" 
        @click="nextSlide"
      >
        <i class="fas fa-chevron-right"></i>
      </button>
    </div>

    <!-- Indicadores -->
    <div class="carrusel-indicators">
      <button
        v-for="(consejo, index) in consejos"
        :key="`indicator-${consejo.id}`"
        class="indicator"
        :class="{ active: index === currentIndex }"
        @click="goToSlide(index)"
      ></button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  consejos: {
    type: Array,
    required: true
  }
})

const currentIndex = ref(0)
const touchStartX = ref(0)
const touchEndX = ref(0)

const nextSlide = () => {
  if (currentIndex.value < props.consejos.length - 1) {
    currentIndex.value++
  } else {
    currentIndex.value = 0 // Volver al inicio
  }
}

const prevSlide = () => {
  if (currentIndex.value > 0) {
    currentIndex.value--
  } else {
    currentIndex.value = props.consejos.length - 1 // Ir al final
  }
}

const goToSlide = (index) => {
  currentIndex.value = index
}

const selectCard = (index) => {
  currentIndex.value = index
}

// Funciones helper para cálculo circular de índices
const getPrevIndex = (current) => {
  return current === 0 ? props.consejos.length - 1 : current - 1
}

const getNextIndex = (current) => {
  return current === props.consejos.length - 1 ? 0 : current + 1
}

const isVisible = (index, current) => {
  const prev = getPrevIndex(current)
  const next = getNextIndex(current)
  return index === current || index === prev || index === next
}

// Touch gestures para mobile
const handleTouchStart = (e) => {
  touchStartX.value = e.touches[0].clientX
}

const handleTouchMove = (e) => {
  touchEndX.value = e.touches[0].clientX
}

const handleTouchEnd = () => {
  const swipeThreshold = 50
  const diff = touchStartX.value - touchEndX.value
  
  if (Math.abs(diff) > swipeThreshold) {
    if (diff > 0) {
      nextSlide()
    } else {
      prevSlide()
    }
  }
  
  touchStartX.value = 0
  touchEndX.value = 0
}

onMounted(() => {
  const carruselContent = document.querySelector('.carrusel-content')
  if (carruselContent) {
    carruselContent.addEventListener('touchstart', handleTouchStart, { passive: true })
    carruselContent.addEventListener('touchmove', handleTouchMove, { passive: true })
    carruselContent.addEventListener('touchend', handleTouchEnd)
  }
})

onUnmounted(() => {
  const carruselContent = document.querySelector('.carrusel-content')
  if (carruselContent) {
    carruselContent.removeEventListener('touchstart', handleTouchStart)
    carruselContent.removeEventListener('touchmove', handleTouchMove)
    carruselContent.removeEventListener('touchend', handleTouchEnd)
  }
})
</script>

<style scoped lang="scss">
.carrusel-container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 6rem 0;
  overflow: hidden; // Prevenir scroll horizontal
}

.carrusel-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  min-height: 400px;
  margin-bottom: 120px;
}

.nav-btn {
  background: white;
  border: none;
  border-radius: 8px;
  width: 70px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: $secondary-color;
  cursor: pointer;
  transition: all 0.3s ease;
  z-index: 10;
  
  &:hover {
    background: $primary-color;
    transform: scale(1.1);
  }
  
  i {
    font-size: 1.2rem;
  }
}

.nav-prev {
  margin-right: 6rem;
}

.nav-next {
  margin-left: 6rem;
}

.carrusel-content {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  width: 100%;
  height: 400px;
  overflow: visible;
  touch-action: pan-y; // Permitir scroll vertical pero capturar swipe horizontal
}

.card-consejo {
  position: absolute;
  border-radius: 15px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  overflow: hidden;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  
  // Add overlay to prevent ghost effect on background image
  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.3);
    opacity: 1;
    transition: opacity 0.3s ease;
    z-index: 1;
  }
  
  &.active::before {
    opacity: 0;
  }
  
  // Separate transitions for smoother effect
  transition-property: transform, opacity, left, right, width, height, box-shadow;
  transition-duration: 0.5s, 0.4s, 0.5s, 0.5s, 0.5s, 0.5s, 0.4s;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1),      // Smooth ease for transform
                              cubic-bezier(0.4, 0, 0.2, 1),      // Smooth ease for opacity
                              cubic-bezier(0.4, 0, 0.2, 1),      // Smooth ease for position
                              cubic-bezier(0.4, 0, 0.2, 1),      // Smooth ease for position
                              cubic-bezier(0.4, 0, 0.2, 1),      // Smooth ease for size
                              cubic-bezier(0.4, 0, 0.2, 1),      // Smooth ease for size
                              cubic-bezier(0.4, 0, 0.2, 1);      // Smooth ease for shadow
  
  // Performance optimization
  will-change: transform, opacity;
  
  // Card inactiva (lateral)
  width: 400px;
  height: 450px;
  opacity: 0.7;
  transform: scale(0.85);
  z-index: 1;
  
  // Card activa (centro)
  &.active {
    width: 420px;
    height: 540px;
    opacity: 1;
    transform: scale(1);
    z-index: 5;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
    // Faster entrance for active card
    transition-duration: 0.6s, 0.5s, 0.6s, 0.6s, 0.6s, 0.6s, 0.5s;
  }
  
  // Posicionamiento con transición suave
  &.prev {
    left: -150px;
    // Quick exit when becoming prev
    transition-duration: 0.35s, 0.25s, 0.35s, 0.35s, 0.35s, 0.35s, 0.25s;
  }
  
  &.next {
    right: -150px;
    // Quick exit when becoming next
    transition-duration: 0.35s, 0.25s, 0.35s, 0.35s, 0.35s, 0.35s, 0.25s;
  }
  
  &.hidden {
    opacity: 0;
    transform: scale(0.7) translateX(-100px);
    pointer-events: none;
    transition-duration: 0.3s, 0.2s, 0.3s, 0.3s, 0.3s, 0.3s, 0.2s; // Fast exit
  }
  
  &:hover:not(.active) {
    opacity: 0.9;
    transform: scale(0.88);
    transition-duration: 0.25s, 0.25s, 0.25s, 0.25s, 0.25s, 0.25s, 0.25s; // Quick hover response
  }
}

.card-text-box {
  position: absolute;
  bottom: 20px;
  left: 20px;
  right: 20px;
  background: white;
  padding: 1.5rem;
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  margin: 0;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 2; // Above the overlay
}

.card-content {
  display: block;
  text-align: left;
}

.card-title {
  font-family: 'DM Sans', sans-serif;
  font-weight: 600;
  font-size: 1.1rem;
  color: $primary-color;
  margin-bottom: 0.5rem;
  line-height: 1.3;
  opacity: 0.7;
  transform: translateY(-5px);
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  
  &.show {
    opacity: 1;
    transform: translateY(0);
  }
}

.card-description {
  overflow: hidden;
  
  p {
    font-size: 0.9rem;
    color: $primary-color;
    line-height: 1.5;
    text-align: left;
    margin: 0;
  }
}

// Vue transition for description with smooth fade and slide
.description-fade-enter-active {
  transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1) 0.2s; // 0.2s delay for stagger effect
}

.description-fade-leave-active {
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.description-fade-enter-from {
  opacity: 0;
  transform: translateY(10px);
  max-height: 0;
}

.description-fade-enter-to {
  opacity: 1;
  transform: translateY(0);
  max-height: 200px;
}

.description-fade-leave-from {
  opacity: 1;
  transform: translateY(0);
  max-height: 200px;
}

.description-fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
  max-height: 0;
}

.carrusel-indicators {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  margin-top: 2rem;
}

.indicator {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  border: none;
  background: #ddd;
  cursor: pointer;
  transition: all 0.3s ease;
  
  &.active {
    background: $secondary-color;
    transform: scale(1.2);
  }
  
  &:hover {
    background: $primary-color;
  }
}


// Responsive - Tablets
@media (max-width: 1024px) and (min-width: 769px) {
  .nav-prev {
    margin-right: 3rem;
  }
  
  .nav-next {
    margin-left: 3rem;
  }
  
  .card-consejo {
    width: 350px;
    height: 400px;
    
    &.active {
      width: 380px;
      height: 480px;
    }
    
    &.prev {
      left: -120px;
    }
    
    &.next {
      right: -120px;
    }
  }
}

// Responsive - Mobile
@media (max-width: 768px) {
  .carrusel-container {
    padding: 1rem 0;
  }
  
  .carrusel-wrapper {
    flex-direction: column;
    min-height: 380px;
    margin-bottom: 60px;
  }
  
  .carrusel-content {
    height: 380px;
  }
  
  .nav-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 40px;
    height: 40px;
    z-index: 20;
    background: rgba(255, 255, 255, 0.95);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    
    i {
      font-size: 1rem;
    }
  }
  
  .nav-prev {
    left: 5px;
    margin-right: 0;
  }
  
  .nav-next {
    right: 5px;
    margin-left: 0;
  }
  
  .card-consejo {
    width: 280px;
    height: 320px;
    
    &.active {
      width: 320px;
      height: 380px;
    }
    
    // Ocultar completamente las cards laterales en mobile
    &.prev,
    &.next {
      opacity: 0;
      transform: scale(0.7);
      pointer-events: none;
    }
    
    &.prev {
      left: -200px;
    }
    
    &.next {
      right: -200px;
    }
  }
  
  .card-text-box {
    bottom: 12px;
    left: 12px;
    right: 12px;
    padding: 0.9rem;
  }
  
  .card-title {
    font-size: 0.95rem;
    margin-bottom: 0.4rem;
  }
  
  .card-description p {
    font-size: 0.8rem;
    line-height: 1.4;
  }
  
  .carrusel-indicators {
    margin-top: 1.5rem;
  }
}

// Responsive - Mobile pequeño
@media (max-width: 480px) {
  .carrusel-wrapper {
    min-height: 350px;
    margin-bottom: 50px;
  }
  
  .carrusel-content {
    height: 350px;
  }
  
  .card-consejo {
    width: 260px;
    height: 300px;
    
    &.active {
      width: 280px;
      height: 340px;
    }
  }
  
  .card-text-box {
    bottom: 10px;
    left: 10px;
    right: 10px;
    padding: 0.8rem;
  }
  
  .card-title {
    font-size: 0.9rem;
  }
  
  .card-description p {
    font-size: 0.75rem;
  }
}
</style>
