<template>
  <div class="view-fade-in">
    <!-- Header de la noticia -->
    <div class="section">

      <!-- Banner de imagen -->
      <div class="banner">
        <img :src="news?.image" :alt="news?.title" class="img-fluid" />
      </div>

      <div class="news-header container">
        <div class="breadcrumb">
          <router-link to="/news" class="breadcrumb-link">
            <i class="fas fa-arrow-left"></i> Volver a Noticias
          </router-link>
        </div>
        <div class="category-badge">{{ news?.category }}</div>
        <h1>{{ news?.title }}</h1>
        <div class="news-meta">
          <span class="author">{{ news?.author }}</span>
          <span class="date">{{ news?.date }}</span>
        </div>
      </div>



      <!-- Contenido principal -->
      <div class="content container">
        <div class="content-wrapper">
          <!-- Descripción inicial -->
          <div class="lead-paragraph">
            {{ news?.description }}
          </div>

          <!-- Contenido completo -->
          <div class="full-content" v-html="formattedContent"></div>


        </div>

        <!-- Sidebar con información adicional -->
        <div class="sidebar">
          <!-- Imagen adicional asociada a la noticia -->
          <div class="additional-image">
            <img :src="news?.sidebarImage || '/img/noticias/noticia-estrategia-nacional.webp'" alt="Imagen adicional" class="img-fluid" />
          </div>
          <div class="info-card">
            <h4>Información del artículo</h4>
            <div class="info-item">
              <strong>Categoría:</strong> {{ news?.category }}
            </div>
            <div class="info-item">
              <strong>Autor:</strong> {{ news?.author }}
            </div>
            <div class="info-item">
              <strong>Fecha:</strong> {{ news?.date }}
            </div>
            
            <!-- Botones en sidebar -->
            <div class="sidebar-actions">
              <button class="custom-btn share-btn" @click="shareNews">
                <i class="fas fa-share-alt"></i>
                <span>Compartir</span>
              </button>
              <router-link to="/news" class="custom-btn more-news-btn">
                <i class="fas fa-list"></i>
                <span>Ver más noticias</span>
              </router-link>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import noticiasData from '@/assets/noticias.json'

export default {
  name: 'NewsDetailView',
  setup() {
    const route = useRoute()
    const router = useRouter()
    const news = ref(null)

    const loadNews = () => {
      const newsId = parseInt(route.params.id)
      news.value = noticiasData.find(item => item.id === newsId)
      
      if (!news.value) {
        // Redirigir a página de noticias si no se encuentra
        router.push('/news')
      }
    }

    const formattedContent = computed(() => {
      if (!news.value?.fullContent) return ''
      
      // Convertir markdown básico a HTML
      return news.value.fullContent
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\n\n/g, '</p><p>')
        .replace(/\n/g, '<br>')
        .replace(/^/, '<p>')
        .replace(/$/, '</p>')
        .replace(/• /g, '<li>')
        .replace(/<p><li>/g, '<ul><li>')
        .replace(/<\/p>/g, (match, offset, string) => {
          if (string.substring(offset + 4, offset + 8) === '<li>') {
            return '</li></ul>'
          }
          return match
        })
    })

    const shareNews = () => {
      if (navigator.share) {
        navigator.share({
          title: news.value?.title,
          text: news.value?.description,
          url: window.location.href
        })
      } else {
        // Fallback para navegadores que no soportan Web Share API
        navigator.clipboard.writeText(window.location.href)
        alert('Enlace copiado al portapapeles')
      }
    }

    // Cargar noticia inicial
    onMounted(() => {
      loadNews()
    })

    // Watcher para detectar cambios en el parámetro de ruta
    watch(() => route.params.id, (newId, oldId) => {
      if (newId !== oldId) {
        loadNews()
        // Scroll al top cuando cambie la noticia
        window.scrollTo({ top: 0, behavior: 'smooth' })
      }
    })

    return {
      news,
      formattedContent,
      shareNews
    }
  }
}
</script>

<style scoped lang="scss">
/* Header de la noticia */
.news-header {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px 20px 10px 20px;
  text-align: left;
}

.breadcrumb {
  margin-bottom: 20px;
}

.breadcrumb-link {
  color: $primary-color;
  text-decoration: none;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: color 0.3s;
}

.breadcrumb-link:hover {
  color: $secondary-color;
}

.category-badge {
  display: inline-block;
  background-color: $secondary-color;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
  margin-bottom: 15px;
}

.news-header h1 {
  font-family: 'Roboto', sans-serif;
  font-weight: 700;
  font-size: 2rem;
  line-height: 1.3;
  color: $primary-color;
  margin-bottom: 15px;
}

.news-meta {
  display: flex;
  gap: 20px;
  margin-bottom: 10px;
  color: #666;
  font-size: 0.9rem;
}

.author {
  font-weight: 600;
}

.date {
  font-style: italic;
}


/* Banner */
.banner {
  width: 100%;
  height: 350px;
  background-color: #ccc;
  margin-bottom: 30px;
}

.banner img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Contenido principal */
.content {
  display: grid;
  grid-template-columns: 1.8fr 1fr;
  gap: 50px;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  margin-bottom: 60px;
}

.content-wrapper {
  background: white;
  text-align: left;
  font-family: 'Roboto', sans-serif;
}

.additional-image {
  margin: 0;
  text-align: left;
  
  img {
    width: 100%;
    height: auto;
    min-height: 600px; /* altura mínima */
    object-fit: cover; /* mantiene proporción sin deformar */
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
}

.lead-paragraph {
  font-size: 1.05rem;
  line-height: 1.7;
  color: #333;
  font-weight: 400;
  margin-bottom: 25px;
  padding: 0;
  background-color: transparent;
  border-left: none;
  border-radius: 0;
  font-family: 'Roboto', sans-serif;
}

.full-content {
  font-size: 0.95rem;
  line-height: 1.8;
  color: #333;
  font-family: 'Roboto', sans-serif;
  
  :deep(p) {
    margin-bottom: 18px;
  }
  
  :deep(strong) {
    color: $primary-color;
    font-weight: 600;
  }
  
  :deep(ul) {
    margin: 20px 0;
    padding-left: 0;
  }
  
  :deep(li) {
    list-style: none;
    padding: 8px 0;
    padding-left: 20px;
    position: relative;
    
    &:before {
      content: "•";
      color: $secondary-color;
      font-weight: bold;
      position: absolute;
      left: 0;
    }
  }
}

/* Botones personalizados UBO */
.custom-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.95rem;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  
  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: left 0.5s;
  }
  
  &:hover::before {
    left: 100%;
  }
  
  i {
    font-size: 1rem;
  }
}

.share-btn {
  background: $secondary-color;
  color: white;
  box-shadow: none;
  border: none;
  
  &:hover {
    background: #4fa8c5;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(92, 189, 224, 0.3);
    color: white;
  }
}

.more-news-btn {
  background: $primary-color;
  color: white;
  border: none;
  box-shadow: none;
  
  &:hover {
    background: #1a3a5c;
    color: white;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(35, 64, 99, 0.3);
    text-decoration: none;
  }
}



/* Sidebar */
.sidebar {
  display: flex;
  flex-direction: column;
  gap: 0px;
 /* Empuja el sidebar hacia abajo para alinearlo con el contenido */
  justify-content: space-between;
}

.info-card {
  background: #f5f5f5;
  border: none;
  border-radius: 12px;
  padding: 35px 25px;
  box-shadow: none;
}

.info-card h4 {
  color: $primary-color;
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 25px;
  border-bottom: none;
  padding-bottom: 0;
  line-height: 1.3;
  font-family: 'Roboto', sans-serif;
}

.info-item {
  margin-bottom: 12px;
  font-size: 0.95rem;
  line-height: 1.6;
  color: #333;
  font-family: 'Roboto', sans-serif;
  
  strong {
    color: $primary-color;
    display: inline;
    font-weight: 700;
  }
}

.sidebar-actions {
  margin-top: 30px;
  padding-top: 0;
  border-top: none;
  display: flex;
  flex-direction: row;
  gap: 12px;
  
  .share-btn, .more-news-btn {
    flex: 1;
    justify-content: center;
    font-size: 0.85rem;
    padding: 12px 16px;
    border-radius: 20px;
    font-family: 'Roboto', sans-serif;
    font-weight: 500;
  }
}


/* Responsive */
@media (max-width: 992px) {
  .content {
    grid-template-columns: 1fr;
    gap: 30px;
  }
  
  .sidebar {
    margin-top: 0;
  }
  
  .news-header h1 {
    font-size: 2rem;
  }
  
  .banner {
    height: 300px;
  }
  
  .additional-image img {
    min-height: 400px;
  }
}

@media (max-width: 768px) {
  .news-header {
    padding: 20px 20px;
  }
  
  .news-header h1 {
    font-size: 1.8rem;
  }
  
  .content {
    padding: 0 20px;
  }
  
  .news-meta {
    flex-direction: column;
    gap: 10px;
  }
  
  .additional-image {
    margin: 20px 0;
    text-align: center;
    
    img {
      max-width: 100%;
      min-height: 300px;
    }
  }
  
  .lead-paragraph {
    font-size: 1.1rem;
    padding: 16px;
  }
  
  .banner {
    height: 250px;
  }
  
  .sidebar-actions {
    flex-direction: column;
    gap: 12px;
    
    .share-btn, .more-news-btn {
      font-size: 0.9rem;
      padding: 12px 16px;
    }
  }
  
  .info-card {
    padding: 25px 20px;
    border-radius: 10px;
    
    h4 {
      font-size: 1.3rem;
      margin-bottom: 20px;
    }
  }
  
  .info-item {
    font-size: 0.9rem;
    margin-bottom: 10px;
  }
}
</style>
