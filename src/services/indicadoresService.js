// Servicio para obtener datos de indicadores
// Preparado para integración futura con Google Sheets API

class IndicadoresService {
  constructor() {
    this.CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQ5HdP5yRh0sR9AA9ARgZTJwcr9W3VNqtR0QWr4p_G-p6jPry3uL3iiascMhK-6FpVwlpyqCcVFiwTA/pub?output=csv'
    this.fallbackData = {
      ticketsIngresados: 247,
      ticketsEnAtencion: 18,
      ticketsResueltos: 229,
      fechaActualizacion: new Date().toISOString().split('T')[0]
    }
  }

  // Método para obtener datos desde Google Sheets (futuro)
  async fetchFromGoogleSheets() {
    if (!this.API_KEY) {
      console.warn('API Key no configurada, usando datos locales')
      return this.fallbackData
    }

    try {
      const RANGE = 'Sheet1!A1:C10' // Ajustar según la estructura del sheet
      const url = `https://sheets.googleapis.com/v4/spreadsheets/${this.SHEET_ID}/values/${RANGE}?key=${this.API_KEY}`
      
      const response = await fetch(url)
      const data = await response.json()
      
      if (data.values) {
        // Procesar los datos según la estructura del spreadsheet
        return this.processSheetData(data.values)
      }
    } catch (error) {
      console.error('Error al obtener datos de Google Sheets:', error)
      return this.fallbackData
    }
  }

  // Método para obtener datos desde CSV público
  async fetchFromPublicCSV() {
    try {
      const response = await fetch(this.CSV_URL)
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      const csvText = await response.text()
      
      return this.processCSVData(csvText)
    } catch (error) {
      console.error('Error al obtener CSV:', error)
      return this.fallbackData
    }
  }

  // Procesar datos del sheet
  processSheetData(values) {
    // Implementar según la estructura específica del spreadsheet
    // Ejemplo básico:
    return {
      ticketsIngresados: parseInt(values[1][0]) || 0,
      ticketsEnAtencion: parseInt(values[1][1]) || 0,
      ticketsResueltos: parseInt(values[1][2]) || 0,
      fechaActualizacion: new Date().toISOString().split('T')[0]
    }
  }

  // Procesar datos CSV
  processCSVData(csvText) {
    console.log('CSV Raw Data:', csvText)
    const lines = csvText.split('\n').filter(line => line.trim() !== '')
    console.log('CSV Lines:', lines)
    
    if (lines.length < 1) {
      console.error('CSV vacío')
      return this.fallbackData
    }
    
    let ticketsIngresados = 0
    let ticketsEnAtencion = 0
    let ticketsResueltos = 0
    
    // Procesar cada línea buscando los labels específicos
    lines.forEach((line, index) => {
      const parts = line.split(',').map(val => val.trim())
      if (parts.length >= 2) {
        const label = parts[0].toLowerCase()
        const value = parseInt(parts[1]) || 0
        
        console.log(`Línea ${index}: label="${label}", value=${value}`)
        
        if (label.includes('ingresado')) {
          ticketsIngresados = value
          console.log('Match: tickets ingresados =', value)
        } else if (label.includes('atencion')) {
          ticketsEnAtencion = value
          console.log('Match: tickets en atención =', value)
        } else if (label.includes('resuelto')) {
          ticketsResueltos = value
          console.log('Match: tickets resueltos =', value)
        }
      }
    })
    
    const result = {
      ticketsIngresados,
      ticketsEnAtencion,
      ticketsResueltos,
      fechaActualizacion: new Date().toISOString().split('T')[0]
    }
    
    console.log('Processed Data:', result)
    return result
  }

  // Método principal para obtener indicadores
  async getIndicadores() {
    // Intentar obtener datos desde CSV público primero
    try {
      return await this.fetchFromPublicCSV()
    } catch (error) {
      console.error('Fallback a datos locales:', error)
      return this.fallbackData
    }
  }

  // Configurar API Key para Google Sheets
  setApiKey(apiKey) {
    this.API_KEY = apiKey
  }
}

export default new IndicadoresService()
