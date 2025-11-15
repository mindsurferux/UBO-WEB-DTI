import noticiasData from '@/assets/noticias.json'

/**
 * Obtiene las noticias más recientes
 * @param {number} limit - Número máximo de noticias a retornar
 * @returns {Array} Array de noticias ordenadas por fecha (más recientes primero)
 */
export function getRecentNews(limit = 3) {
  // Convertir fechas a objetos Date para ordenamiento
  const sortedNews = [...noticiasData].sort((a, b) => {
    const dateA = parseSpanishDate(a.date)
    const dateB = parseSpanishDate(b.date)
    return dateB - dateA // Orden descendente (más reciente primero)
  })
  
  return sortedNews.slice(0, limit)
}

/**
 * Convierte fecha en español a objeto Date
 * @param {string} spanishDate - Fecha en formato "15 de Marzo, 2024"
 * @returns {Date} Objeto Date
 */
function parseSpanishDate(spanishDate) {
  const monthMap = {
    'enero': 0, 'febrero': 1, 'marzo': 2, 'abril': 3,
    'mayo': 4, 'junio': 5, 'julio': 6, 'agosto': 7,
    'septiembre': 8, 'octubre': 9, 'noviembre': 10, 'diciembre': 11
  }
  
  // Extraer día, mes y año de la fecha
  const parts = spanishDate.toLowerCase().split(' ')
  const day = parseInt(parts[0])
  const month = monthMap[parts[2].replace(',', '')]
  const year = parseInt(parts[3])
  
  return new Date(year, month, day)
}

/**
 * Obtiene una noticia por ID
 * @param {number} id - ID de la noticia
 * @returns {Object|null} Objeto de noticia o null si no se encuentra
 */
export function getNewsById(id) {
  return noticiasData.find(news => news.id === parseInt(id)) || null
}

/**
 * Obtiene noticias por categoría
 * @param {string} category - Categoría de noticias
 * @returns {Array} Array de noticias de la categoría especificada
 */
export function getNewsByCategory(category) {
  return noticiasData.filter(news => 
    news.category.toLowerCase() === category.toLowerCase()
  )
}

/**
 * Busca noticias por término
 * @param {string} searchTerm - Término de búsqueda
 * @returns {Array} Array de noticias que coinciden con el término
 */
export function searchNews(searchTerm) {
  const term = searchTerm.toLowerCase()
  return noticiasData.filter(news => 
    news.title.toLowerCase().includes(term) ||
    news.description.toLowerCase().includes(term) ||
    news.tags.some(tag => tag.toLowerCase().includes(term))
  )
}

/**
 * Formatea fecha para mostrar
 * @param {string} dateString - Fecha en formato español
 * @returns {string} Fecha formateada para mostrar
 */
export function formatDisplayDate(dateString) {
  return dateString // Por ahora mantener formato original
}

/**
 * Trunca texto a una longitud específica
 * @param {string} text - Texto a truncar
 * @param {number} maxLength - Longitud máxima
 * @returns {string} Texto truncado con "..."
 */
export function truncateText(text, maxLength = 100) {
  if (text.length <= maxLength) return text
  return text.substring(0, maxLength).trim() + '...'
}
