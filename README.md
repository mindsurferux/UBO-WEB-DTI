# UBO TI App 1.8

Portal web institucional de la **Dirección de Tecnología de la Información (DTI)** de la Universidad Bernardo O'Higgins (UBO).

## 📋 Descripción

Aplicación web moderna desarrollada en Vue.js 3 que permite gestionar proyectos TI, visualizar métricas operativas y proporcionar información sobre los servicios tecnológicos de la universidad.

## 🎯 Objetivos

- **Gestión de Proyectos**: Sistema CRUD para administrar proyectos de tecnología
- **Dashboard Ejecutivo**: Visualización de métricas y KPIs con gráficos interactivos
- **Portal Informativo**: Secciones dedicadas a servicios, ciberseguridad y noticias
- **Mesa de Ayuda**: Punto de contacto centralizado para soporte TI
- **Indicadores de Gestión**: Métricas semanales de tickets y atención

## 🛠️ Stack Tecnológico

### Frontend
- **Vue.js 3** - Framework principal con Composition API
- **Vue Router 4** - Navegación SPA
- **Vuex 4** - Gestión de estado global
- **Bootstrap 5.3.3** - Framework CSS y componentes UI
- **SASS/SCSS** - Preprocesador de estilos

### Visualización
- **Chart.js 4.4.7** - Gráficos y dashboards interactivos
- **FontAwesome 6.7.2** - Iconografía

### Deployment
- **Firebase 11.2.0** - Hosting y despliegue
- **Vue CLI 5** - Herramientas de desarrollo y build

## 🏗️ Estructura del Proyecto

```
src/
├── views/              # Páginas principales (8 vistas)
│   ├── HomeView.vue    # Página de inicio con hero e indicadores
│   ├── DashboardView.vue # Dashboard administrativo
│   ├── LoginView.vue   # Autenticación
│   └── ...
├── components/         # Componentes reutilizables (12 componentes)
│   ├── Navbar.vue     # Navegación principal
│   ├── Card.vue       # Tarjetas de proyectos
│   ├── AddProjectModal.vue # CRUD de proyectos
│   └── ...
├── router/            # Configuración de rutas
├── store/             # Gestión de estado Vuex
└── assets/            # Recursos estáticos y datos
    ├── img/           # Imágenes y logos
    ├── styles/        # Estilos SCSS
    └── proyectos.json # Datos de proyectos
```

## ✨ Funcionalidades Principales

### 🏠 Página de Inicio
- Hero section con imagen destacada de proyectos TI
- Pestañas informativas institucionales
- **Indicadores de gestión semanal**:
  - Tickets ingresados
  - Tickets en atención
  - Tickets resueltos

### 📊 Dashboard Administrativo
- Gráficos interactivos (Chart.js):
  - Proyectos activos (gráfico de dona)
  - Usuarios activos (gráfico de barras)
- Notificaciones recientes
- Enlaces a recursos externos
- Gestión completa de proyectos

### 🔐 Sistema de Autenticación
- Login con roles (admin/usuario)
- Persistencia en localStorage
- Control de acceso por funcionalidades

### 📁 Gestión de Proyectos
- **CRUD completo**: Crear, leer, actualizar, eliminar
- Vista administrativa dedicada
- Almacenamiento local y JSON

### 📑 Secciones Informativas
- **Nosotros**: Información institucional
- **Servicios**: Catálogo de servicios TI
- **Ciberseguridad**: Políticas y recursos
- **Noticias**: Comunicados y actualizaciones

## 🚀 Instalación y Configuración

### Prerrequisitos
- Node.js (v14 o superior)
- npm o yarn
- Vue CLI

### Instalación
```bash
# Clonar el repositorio
git clone <repository-url>
cd ubo-tiapp-1.8

# Instalar dependencias
npm install

# Ejecutar en modo desarrollo
npm run serve

# Build para producción
npm run build
```

### Scripts Disponibles
```bash
npm run serve      # Servidor de desarrollo
npm run build      # Build de producción
npm run test:unit  # Tests unitarios
npm run test:e2e   # Tests end-to-end
```

## 🌐 Despliegue

El proyecto está configurado para despliegue en **Firebase Hosting**:

```bash
# Build del proyecto
npm run build

# Desplegar a Firebase
firebase deploy
```

## 📱 Responsive Design

- **Mobile-first approach**
- Breakpoints optimizados para tablet y desktop
- Navegación colapsible en dispositivos móviles
- Componentes adaptativos

## 🔧 Configuración

### Variables de Entorno
El proyecto utiliza configuraciones específicas para diferentes entornos de despliegue.

### Datos de Proyectos
Los proyectos se gestionan a través de:
- `src/assets/proyectos.json` - Datos iniciales
- `localStorage` - Persistencia local

## 📈 Estado del Proyecto

### ✅ Completado
- Estructura base Vue.js 3
- Sistema de navegación completo
- Dashboard con gráficos interactivos
- CRUD de proyectos funcional
- Autenticación básica
- Diseño responsive
- Configuración Firebase

### ⚠️ En Desarrollo
- Mesa de ayuda TI (funcionalidad completa)
- Integración con backend
- Funcionalidad de búsqueda avanzada
- Datos dinámicos de tickets en tiempo real

## 👥 Contribución

Este proyecto sigue el flujo de trabajo con ramas:
- `master` - Rama principal estable
- `windsurf` - Rama de desarrollo activa

## 📄 Licencia

Proyecto institucional de la Universidad Bernardo O'Higgins - Dirección de Tecnología de la Información.

---

**Desarrollado para UBO DTI** | **Vue.js 3 + Bootstrap 5** | **Firebase Hosting**
