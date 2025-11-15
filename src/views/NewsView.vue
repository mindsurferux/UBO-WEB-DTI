<template>
  <div class="view-fade-in">
    <div class="about-header container">
    <h2>Noticias</h2>
    <p>en sistemas TI</p>
  </div>

  <!-- "Banner gris" a lo ancho. -->


  <div v-if="heroNews" class="hero-container">
    <div class="hero-content-wrapper container">
      <div class="hero-content">
        <h1 class="hero-title">{{ heroNews.title }}</h1>
        <p class="hero-description">
          {{ heroNews.description }}
        </p>
        <router-link :to="`/news/${heroNews.id}`" class="hero-link">
          {{ heroNews.buttonText }}
        </router-link>
      </div>
      <div class="hero-image-container">
        <img :src="heroNews.image" :alt="heroNews.title" class="hero-image" />
      </div>
    </div>
  </div>





  <!-- Resto de noticias (formato anterior) -->

  <div class="news-container container">
    <Noticia v-for="news in otherNews" :key="news.id" :item="news" @openModal="showConstructionModal" />
  </div>


  <!-- Modal de En Construcción -->
  <UnderConstructionModal :show="showModal" @close="showModal = false" />
  </div>
</template>

<script>
import newsData from '@/assets/noticias.json'
import UnderConstructionModal from '@/components/UnderConstructionModal.vue'
import Noticia from '@/components/Noticia.vue'

export default {
  name: 'NewsView',
  components: {
    UnderConstructionModal,
    Noticia,
  },
  data() {
    return {
      newsItems: newsData,
      showModal: false
    }
  },
  computed: {
    heroNews() {
      return this.newsItems.length > 0 ? this.newsItems[0] : null
    },
    otherNews() {
      return this.newsItems.slice(1)
    }
  },
  methods: {
    showConstructionModal() {
      this.showModal = true
    }
  }
}
</script>

<style scoped lang="scss">
/* Estilos específicos de NewsView - los estilos comunes están en main.scss */
.flex-row-reverse {
  flex-direction: row-reverse !important;
}
</style>
