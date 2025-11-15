<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-column">
          <h5>Nosotros</h5>
          <ul>
            <li><a href="#">Dirección de tecnología</a></li>
            <li><a href="#">Jefatura</a></li>
          </ul>
        </div>

        <div class="footer-column">
          <h5>Servicios</h5>
          <ul>
            <li><a @click="navigateToService(0)" href="#">Seguimiento Proyectos</a></li>
            <li><a @click="navigateToService(1)" href="#">Mesa de Ayuda TI</a></li>
            <li><a @click="navigateToService(2)" href="#">Consultoría TI</a></li>
            <li><a @click="navigateToService(3)" href="#">Accesos Inalámbricos</a></li>
            <li><a @click="navigateToService(4)" href="#">Licencias de Softwares</a></li>
            <li><a @click="navigateToService(5)" href="#">Capacitaciones</a></li>
          </ul>
        </div>

        <div class="footer-column">
          <h5>Ciberseguridad</h5>
          <ul>
            <li><a @click="navigateToCyber(0)" href="#">Registrar Incidente</a></li>
            <li><a @click="navigateToCyber(1)" href="#">Políticas de contraseñas</a></li>
            <li><a @click="navigateToCyber(2)" href="#">Phishing</a></li>
            <li><a @click="navigateToCyber(3)" href="#">Antivirus Corporativo</a></li>
          </ul>
        </div>

        <div class="footer-column">
          <h5>Noticias</h5>
          <ul>
            <li v-for="news in recentNews" :key="news.id">
              <router-link :to="`/news/${news.id}`">
                {{ truncateTitle(news.title) }}
              </router-link>
              <small class="news-date">{{ news.date }}</small>
            </li>
          </ul>
        </div>

        <div class="footer-column footer-last">
          <h5>Mesa de ayuda TI</h5>
        </div>
      </div>
    </div>

    <!-- Botón flotante Scroll-Up (Solo aparece cuando el usuario llega al footer) -->
    <button
      v-show="isInFooter"
      @click="scrollToTop"
      class="scroll-up"
    >
      <i class="fas fa-chevron-up"></i>
    </button>
  </footer>
</template>

<script>
import { getRecentNews, truncateText } from '@/utils/newsUtils'

export default {
  name: "CustomFooter",
  data() {
    return {
      isInFooter: false, // Indica si el usuario está en el footer
      recentNews: [], // Noticias más recientes
    };
  },
  mounted() {
    window.addEventListener("scroll", this.checkScroll);
    this.loadRecentNews();
  },
  beforeUnmount() {
    window.removeEventListener("scroll", this.checkScroll);
  },
  methods: {
    scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    },
    checkScroll() {
      const scrollPosition = window.scrollY + window.innerHeight;
      const pageHeight = document.body.scrollHeight;
      const footerHeight = document.querySelector(".footer").offsetHeight;
      const footerStart = pageHeight - footerHeight;

      // El botón solo aparece cuando el usuario entra en el footer
      this.isInFooter = scrollPosition >= footerStart;
    },
    navigateToService(cardIndex) {
      this.$router.push({
        path: '/services',
        query: { card: cardIndex }
      });
    },
    navigateToCyber(cardIndex) {
      this.$router.push({
        path: '/cybersecurity',
        query: { card: cardIndex }
      });
    },
    loadRecentNews() {
      // Obtener las 3 noticias más recientes
      this.recentNews = getRecentNews(3);
    },
    truncateTitle(title) {
      // Truncar títulos largos para el footer
      return truncateText(title, 45);
    }
  },
};
</script>

<style scoped>
/* ==== Footer General ==== */
.footer {
  background-color: #f5f5f5;
  padding: 2rem 0;
  box-shadow: 0 -1px 4px rgba(0, 0, 0, 0.1);
  position: relative; /* Necesario para que el botón absolute funcione correctamente */
}

.footer h5 {
  font-size: 1rem;
  font-weight: 700;
  color: #333;
  margin-bottom: 0.8rem;
}

.footer ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer ul li {
  margin-bottom: 0.4rem;
}

.footer ul li a {
  text-decoration: none;
  color: #666;
  transition: color 0.3s;
}

.footer ul li a:hover {
  color: #0d2c5b;
}

/* Estilos específicos para noticias en footer */
.footer ul li .news-date {
  display: block;
  color: #999;
  font-size: 0.75rem;
  margin-top: 2px;
  font-style: italic;
}

.footer ul li a[href*="/news/"] {
  display: block;
  font-weight: 500;
  line-height: 1.3;
  margin-bottom: 2px;
}

/* ==== Distribución de columnas con Grid ==== */
.footer-grid {
  display: grid;
  grid-template-columns: 2fr 2fr 2fr 2fr 2fr;
  gap: 1rem;
  max-width: 1100px;
  margin: 0 auto;
}

.footer-column {
  text-align: left;
}

.footer-last {
  text-align: right;
}

/* ==== Botón Scroll-Up con Absolute ==== */
.scroll-up {
  position: absolute;
  right: 15px;
  bottom: 320px; /* Lo posicionamos 300px sobre el footer */
  width: 40px;
  height: 40px;
  background-color: #5cbde0;
  color: white;
  border: none;
  border-radius: 8px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: opacity 0.3s ease-in-out;
  z-index: 6;
}

/* Efecto Hover */
.scroll-up:hover {
  background-color: #479ec4;
}

.scroll-up i {
  font-size: 1rem;
}

/* ==== Responsividad para mobile ==== */
@media (max-width: 768px) {
  .footer-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .footer-column {
    text-align: center;
  }

  .footer-last {
    text-align: center;
  }
  
  .scroll-up {
    bottom: 500px; /* Lo posicionamos 500px sobre el footer */
  }
}

/* ==== Responsividad para tablets ==== */
@media (min-width: 769px) and (max-width: 992px) {
  .footer-grid {
    grid-template-columns: repeat(3, 1fr);
    gap: 1.2rem;
  }

  .footer-last {
    text-align: left;
  }
}
</style>
