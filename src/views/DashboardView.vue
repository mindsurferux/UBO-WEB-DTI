<template>
  <div class="dashboard-container view-fade-in">
    <!-- Header del Dashboard -->
    <div class="dashboard-header">
      <div class="header-content">
        <div class="user-info">
          <h1>Dashboard de Proyectos TI</h1>
          <p>Bienvenido, <strong>{{ currentUser.role === 'admin' ? 'Jefe de Proyectos' : 'Stakeholder' }}</strong></p>
        </div>
        <div class="header-actions">
          <button @click="logout" class="btn btn-outline-secondary">
            <i class="fa-solid fa-sign-out-alt me-2"></i>Cerrar Sesión
          </button>
        </div>
      </div>
    </div>

    <!-- Métricas Principales -->
    <div class="metrics-section">
      <div class="metrics-grid">
        <div class="metric-card">
          <div class="metric-icon">
            <i class="fa-solid fa-project-diagram"></i>
          </div>
          <div class="metric-content">
            <h3>{{ userProjects.length }}</h3>
            <p>Proyectos Asignados</p>
          </div>
        </div>
        <div class="metric-card">
          <div class="metric-icon">
            <i class="fa-solid fa-tasks"></i>
          </div>
          <div class="metric-content">
            <h3>{{ totalTasks.inProgress }}</h3>
            <p>Tareas en Progreso</p>
          </div>
        </div>
        <div class="metric-card">
          <div class="metric-icon">
            <i class="fa-solid fa-clock"></i>
          </div>
          <div class="metric-content">
            <h3>{{ overdueTasks }}</h3>
            <p>Tareas Vencidas</p>
          </div>
        </div>
        <div class="metric-card" v-if="permissions.features.budgetView">
          <div class="metric-icon">
            <i class="fa-solid fa-dollar-sign"></i>
          </div>
          <div class="metric-content">
            <h3>${{ totalBudget.spent.toLocaleString() }}</h3>
            <p>Presupuesto Utilizado</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Selector de Vistas -->
    <div class="view-selector">
      <div class="view-tabs">
        <button 
          v-for="view in availableViews" 
          :key="view.id"
          :class="['view-tab', { active: currentView === view.id }]"
          @click="setCurrentView(view.id)"
        >
          <i :class="view.icon"></i>
          {{ view.name }}
        </button>
      </div>
    </div>

    <!-- Contenido Principal según la Vista -->
    <div class="main-content">
      <!-- Vista Overview -->
      <div v-if="currentView === 'overview'" class="overview-view">
        <div class="projects-overview">
          <h2>Resumen de Proyectos</h2>
          <div class="projects-grid">
            <div v-for="project in userProjects" :key="project.id" class="project-card">
              <div class="project-header">
                <h3>{{ project.name }}</h3>
                <span :class="['status-badge', project.status.toLowerCase().replace(' ', '-')]">
                  {{ project.status }}
                </span>
              </div>
              <p class="project-description">{{ project.description }}</p>
              <div class="project-progress">
                <div class="progress-bar">
                  <div class="progress-fill" :style="{ width: project.progress + '%' }"></div>
                </div>
                <span class="progress-text">{{ project.progress }}%</span>
              </div>
              <div class="project-details">
                <div class="detail-item">
                  <i class="fa-solid fa-calendar"></i>
                  <span>{{ formatDate(project.endDate) }}</span>
                </div>
                <div class="detail-item">
                  <i class="fa-solid fa-users"></i>
                  <span>{{ project.team.length }} miembros</span>
                </div>
                <div class="detail-item" v-if="permissions.features.budgetView">
                  <i class="fa-solid fa-dollar-sign"></i>
                  <span>${{ project.budget.remaining.toLocaleString() }} restante</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Vista de Tareas -->
      <div v-if="currentView === 'tasks'" class="tasks-view">
        <h2>Gestión de Tareas</h2>
        <div class="tasks-container">
          <div class="task-columns">
            <div class="task-column">
              <h3><i class="fa-solid fa-clock text-warning"></i> Pendientes</h3>
              <div class="task-list">
                <div v-for="task in tasksByStatus.pending" :key="task.id" class="task-item pending">
                  <h4>{{ task.title }}</h4>
                  <p>{{ task.project }}</p>
                  <span class="task-date">{{ formatDate(task.dueDate) }}</span>
                </div>
              </div>
            </div>
            <div class="task-column">
              <h3><i class="fa-solid fa-spinner text-primary"></i> En Progreso</h3>
              <div class="task-list">
                <div v-for="task in tasksByStatus.inProgress" :key="task.id" class="task-item in-progress">
                  <h4>{{ task.title }}</h4>
                  <p>{{ task.project }}</p>
                  <span class="task-date">{{ formatDate(task.dueDate) }}</span>
                </div>
              </div>
            </div>
            <div class="task-column">
              <h3><i class="fa-solid fa-check text-success"></i> Completadas</h3>
              <div class="task-list">
                <div v-for="task in tasksByStatus.completed" :key="task.id" class="task-item completed">
                  <h4>{{ task.title }}</h4>
                  <p>{{ task.project }}</p>
                  <span class="task-date">{{ formatDate(task.completedDate) }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Vista Calendario -->
      <div v-if="currentView === 'calendar'" class="calendar-view">
        <div class="calendar-container">
          <div class="calendar-header">
            <button @click="previousMonth" class="nav-btn">
              <i class="fa-solid fa-chevron-left"></i>
            </button>
            <h3>{{ currentMonthYear }}</h3>
            <button @click="nextMonth" class="nav-btn">
              <i class="fa-solid fa-chevron-right"></i>
            </button>
          </div>
          
          <div class="calendar-grid">
            <div class="calendar-weekdays">
              <div v-for="day in weekdays" :key="day" class="weekday">{{ day }}</div>
            </div>
            
            <div class="calendar-days">
              <div 
                v-for="day in calendarDays" 
                :key="day.date" 
                :class="['calendar-day', { 
                  'other-month': !day.isCurrentMonth,
                  'today': day.isToday,
                  'has-events': day.events.length > 0
                }]"
              >
                <span class="day-number">{{ day.day }}</span>
                <div class="day-events">
                  <div 
                    v-for="event in day.events.slice(0, 2)" 
                    :key="event.id"
                    :class="['event-dot', event.type]"
                    :title="event.title"
                  ></div>
                  <span v-if="day.events.length > 2" class="more-events">+{{ day.events.length - 2 }}</span>
                </div>
              </div>
            </div>
          </div>
          
          <div class="calendar-legend">
            <div class="legend-item">
              <div class="event-dot deadline"></div>
              <span>Fechas límite</span>
            </div>
            <div class="legend-item">
              <div class="event-dot milestone"></div>
              <span>Hitos</span>
            </div>
            <div class="legend-item">
              <div class="event-dot meeting"></div>
              <span>Reuniones</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Vista Gantt (Solo Admin) -->
      <div v-if="currentView === 'gantt' && permissions.features.gantt" class="gantt-view">
        <h2>Diagrama de Gantt</h2>
        <div class="gantt-container">
          <div class="gantt-header">
            <div class="gantt-controls">
              <button @click="ganttZoom = 'month'" :class="['zoom-btn', { active: ganttZoom === 'month' }]">
                Mes
              </button>
              <button @click="ganttZoom = 'week'" :class="['zoom-btn', { active: ganttZoom === 'week' }]">
                Semana
              </button>
              <button @click="ganttZoom = 'day'" :class="['zoom-btn', { active: ganttZoom === 'day' }]">
                Día
              </button>
            </div>
          </div>
          
          <div class="gantt-chart">
            <div class="gantt-timeline">
              <div class="timeline-header">
                <div class="project-column">Proyecto</div>
                <div class="dates-column">
                  <div 
                    v-for="date in ganttDates" 
                    :key="date.key" 
                    class="date-cell"
                    :style="{ width: ganttCellWidth + 'px' }"
                  >
                    {{ date.label }}
                  </div>
                </div>
              </div>
              
              <div class="gantt-rows">
                <div v-for="project in userProjects" :key="project.id" class="gantt-row">
                  <div class="project-info">
                    <h4>{{ project.name }}</h4>
                    <span class="project-duration">{{ formatDate(project.startDate) }} - {{ formatDate(project.endDate) }}</span>
                  </div>
                  <div class="timeline-row">
                    <div 
                      class="project-bar"
                      :style="getProjectBarStyle(project)"
                    >
                      <div class="progress-overlay" :style="{ width: project.progress + '%' }"></div>
                      <span class="project-label">{{ project.progress }}%</span>
                    </div>
                    
                    <!-- Tareas del proyecto -->
                    <div v-for="task in getProjectTasks(project)" :key="task.id" class="task-bar" :style="getTaskBarStyle(task)">
                      <span class="task-label">{{ task.title }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <div class="gantt-legend">
            <div class="legend-item">
              <div class="legend-bar project-bar-sample"></div>
              <span>Proyectos</span>
            </div>
            <div class="legend-item">
              <div class="legend-bar task-bar-sample"></div>
              <span>Tareas</span>
            </div>
            <div class="legend-item">
              <div class="legend-bar progress-sample"></div>
              <span>Progreso completado</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Vista de Reportes (Solo Admin) -->
      <div v-if="currentView === 'reports' && permissions.features.reports" class="reports-view">
        <h2>Reportes y Análisis</h2>
        <div class="reports-grid">
          <div class="report-card">
            <h3>Rendimiento de Proyectos</h3>
            <div class="chart-placeholder">
              <i class="fa-solid fa-chart-line"></i>
              <p>Gráfico de progreso temporal</p>
            </div>
          </div>
          <div class="report-card">
            <h3>Utilización de Recursos</h3>
            <div class="chart-placeholder">
              <i class="fa-solid fa-chart-pie"></i>
              <p>Distribución de presupuesto</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Vista de Equipo (Solo Admin) -->
      <div v-if="currentView === 'team' && permissions.features.teamManagement" class="team-view">
        <h2>Gestión de Equipo</h2>
        <div class="team-grid">
          <div v-for="member in allTeamMembers" :key="member.name" class="team-member-card">
            <div class="member-avatar">
              <i class="fa-solid fa-user"></i>
            </div>
            <h4>{{ member.name }}</h4>
            <p>{{ member.projects.length }} proyecto(s)</p>
            <div class="member-projects">
              <span v-for="project in member.projects" :key="project" class="project-tag">
                {{ project }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import proyectosData from '@/assets/proyectos-dashboard.json'
import permissionsData from '@/assets/dashboard-permissions.json'

export default {
  name: "DashboardView",
  data() {
    return {
      currentUser: null,
      permissions: {},
      userProjects: [],
      currentView: 'overview',
      allViews: [
        { id: 'overview', name: 'Resumen', icon: 'fa-solid fa-home' },
        { id: 'tasks', name: 'Tareas', icon: 'fa-solid fa-tasks' },
        { id: 'calendar', name: 'Calendario', icon: 'fa-solid fa-calendar' },
        { id: 'gantt', name: 'Gantt', icon: 'fa-solid fa-chart-gantt' },
        { id: 'reports', name: 'Reportes', icon: 'fa-solid fa-chart-line' },
        { id: 'team', name: 'Equipo', icon: 'fa-solid fa-users' }
      ],
      sampleTasks: [
        { id: 1, title: 'Configurar base de datos', project: 'Sistema Académico', status: 'pending', dueDate: '2024-01-20' },
        { id: 2, title: 'Diseño de interfaz', project: 'Portal Estudiantil', status: 'inProgress', dueDate: '2024-01-25' },
        { id: 3, title: 'Testing de seguridad', project: 'Sistema Académico', status: 'inProgress', dueDate: '2024-01-18' },
        { id: 4, title: 'Documentación API', project: 'Portal Estudiantil', status: 'completed', completedDate: '2024-01-15' },
        { id: 5, title: 'Configurar servidor', project: 'Infraestructura Cloud', status: 'completed', completedDate: '2024-01-10' },
        { id: 6, title: 'Implementar autenticación', project: 'Sistema Seguridad', status: 'pending', dueDate: '2024-01-30' }
      ],
      // Calendar data
      currentCalendarDate: new Date(),
      weekdays: ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'],
      calendarEvents: [
        { id: 1, title: 'Entrega Sistema Académico', date: '2024-01-20', type: 'deadline' },
        { id: 2, title: 'Reunión de seguimiento', date: '2024-01-22', type: 'meeting' },
        { id: 3, title: 'Hito Portal Estudiantil', date: '2024-01-25', type: 'milestone' },
        { id: 4, title: 'Review de seguridad', date: '2024-01-18', type: 'meeting' },
        { id: 5, title: 'Entrega final Infraestructura', date: '2024-01-30', type: 'deadline' }
      ],
      // Gantt data
      ganttZoom: 'month',
      ganttCellWidth: 80
    }
  },
  computed: {
    availableViews() {
      return this.allViews.filter(view => 
        this.permissions.allowedViews && this.permissions.allowedViews.includes(view.id)
      )
    },
    totalTasks() {
      const tasks = this.sampleTasks.filter(task => 
        this.userProjects.some(project => 
          project.name.includes(task.project.split(' ')[0])
        )
      )
      return {
        completed: tasks.filter(t => t.status === 'completed').length,
        inProgress: tasks.filter(t => t.status === 'inProgress').length,
        pending: tasks.filter(t => t.status === 'pending').length,
        total: tasks.length
      }
    },
    overdueTasks() {
      const today = new Date()
      return this.sampleTasks.filter(task => 
        task.status !== 'completed' && 
        new Date(task.dueDate) < today &&
        this.userProjects.some(project => 
          project.name.includes(task.project.split(' ')[0])
        )
      ).length
    },
    totalBudget() {
      return this.userProjects.reduce((acc, project) => ({
        allocated: acc.allocated + project.budget.allocated,
        spent: acc.spent + project.budget.spent,
        remaining: acc.remaining + project.budget.remaining
      }), { allocated: 0, spent: 0, remaining: 0 })
    },
    tasksByStatus() {
      const userTasks = this.sampleTasks.filter(task => 
        this.userProjects.some(project => 
          project.name.includes(task.project.split(' ')[0])
        )
      )
      return {
        pending: userTasks.filter(t => t.status === 'pending'),
        inProgress: userTasks.filter(t => t.status === 'inProgress'),
        completed: userTasks.filter(t => t.status === 'completed')
      }
    },
    allTeamMembers() {
      const members = new Map()
      this.userProjects.forEach(project => {
        project.team.forEach(member => {
          if (!members.has(member)) {
            members.set(member, { name: member, projects: [] })
          }
          members.get(member).projects.push(project.name)
        })
      })
      return Array.from(members.values())
    },
    currentMonthYear() {
      const months = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
      ]
      return `${months[this.currentCalendarDate.getMonth()]} ${this.currentCalendarDate.getFullYear()}`
    },
    calendarDays() {
      const year = this.currentCalendarDate.getFullYear()
      const month = this.currentCalendarDate.getMonth()
      
      // First day of the month
      const firstDay = new Date(year, month, 1)
      const lastDay = new Date(year, month + 1, 0)
      
      // Start from Sunday of the week containing the first day
      const startDate = new Date(firstDay)
      startDate.setDate(firstDay.getDate() - firstDay.getDay())
      
      // End on Saturday of the week containing the last day
      const endDate = new Date(lastDay)
      endDate.setDate(lastDay.getDate() + (6 - lastDay.getDay()))
      
      const days = []
      const currentDate = new Date(startDate)
      const today = new Date()
      
      while (currentDate <= endDate) {
        const dayEvents = this.calendarEvents.filter(event => {
          const eventDate = new Date(event.date)
          return eventDate.toDateString() === currentDate.toDateString()
        })
        
        days.push({
          date: new Date(currentDate),
          day: currentDate.getDate(),
          isCurrentMonth: currentDate.getMonth() === month,
          isToday: currentDate.toDateString() === today.toDateString(),
          events: dayEvents
        })
        
        currentDate.setDate(currentDate.getDate() + 1)
      }
      
      return days
    },
    ganttDates() {
      const dates = []
      const startDate = new Date('2024-01-01')
      const endDate = new Date('2024-03-31')
      
      if (this.ganttZoom === 'month') {
        const current = new Date(startDate)
        while (current <= endDate) {
          dates.push({
            key: current.getTime(),
            label: current.toLocaleDateString('es-ES', { month: 'short', year: 'numeric' }),
            date: new Date(current)
          })
          current.setMonth(current.getMonth() + 1)
        }
      } else if (this.ganttZoom === 'week') {
        const current = new Date(startDate)
        let weekNum = 1
        while (current <= endDate) {
          dates.push({
            key: current.getTime(),
            label: `S${weekNum}`,
            date: new Date(current)
          })
          current.setDate(current.getDate() + 7)
          weekNum++
        }
      } else { // day
        const current = new Date(startDate)
        while (current <= endDate && dates.length < 30) { // Limit to 30 days for performance
          dates.push({
            key: current.getTime(),
            label: current.getDate().toString(),
            date: new Date(current)
          })
          current.setDate(current.getDate() + 1)
        }
      }
      
      return dates
    }
  },
  created() {
    this.loadUserData()
  },
  methods: {
    loadUserData() {
      // Obtener usuario actual del localStorage
      const user = JSON.parse(localStorage.getItem('user'))
      if (!user) {
        this.$router.push('/')
        return
      }
      
      this.currentUser = user
      
      // Cargar permisos según el rol
      this.permissions = permissionsData[user.role] || permissionsData.user
      
      // Cargar proyectos según el rol
      this.userProjects = proyectosData[user.role] || proyectosData.user
      
      // Establecer vista inicial según permisos
      this.currentView = this.permissions.allowedViews[0] || 'overview'
    },
    setCurrentView(viewId) {
      if (this.permissions.allowedViews.includes(viewId)) {
        this.currentView = viewId
      }
    },
    formatDate(dateString) {
      return new Date(dateString).toLocaleDateString('es-ES', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
      })
    },
    previousMonth() {
      const newDate = new Date(this.currentCalendarDate)
      newDate.setMonth(newDate.getMonth() - 1)
      this.currentCalendarDate = newDate
    },
    nextMonth() {
      const newDate = new Date(this.currentCalendarDate)
      newDate.setMonth(newDate.getMonth() + 1)
      this.currentCalendarDate = newDate
    },
    getProjectTasks(project) {
      return this.sampleTasks.filter(task => 
        task.project.includes(project.name.split(' ')[0])
      )
    },
    getProjectBarStyle(project) {
      const startDate = new Date(project.startDate)
      const endDate = new Date(project.endDate)
      const ganttStart = new Date('2024-01-01')
      
      const startOffset = Math.max(0, (startDate - ganttStart) / (1000 * 60 * 60 * 24))
      const duration = (endDate - startDate) / (1000 * 60 * 60 * 24)
      
      let cellsPerDay = 1
      if (this.ganttZoom === 'month') cellsPerDay = 1/30
      else if (this.ganttZoom === 'week') cellsPerDay = 1/7
      
      return {
        left: (startOffset * cellsPerDay * this.ganttCellWidth) + 'px',
        width: (duration * cellsPerDay * this.ganttCellWidth) + 'px'
      }
    },
    getTaskBarStyle(task) {
      const taskStart = new Date(task.dueDate)
      taskStart.setDate(taskStart.getDate() - 7) // Assume 7 days before due date
      const taskEnd = new Date(task.dueDate)
      const ganttStart = new Date('2024-01-01')
      
      const startOffset = Math.max(0, (taskStart - ganttStart) / (1000 * 60 * 60 * 24))
      const duration = 7 // 7 days duration
      
      let cellsPerDay = 1
      if (this.ganttZoom === 'month') cellsPerDay = 1/30
      else if (this.ganttZoom === 'week') cellsPerDay = 1/7
      
      return {
        left: (startOffset * cellsPerDay * this.ganttCellWidth) + 'px',
        width: (duration * cellsPerDay * this.ganttCellWidth) + 'px',
        top: '30px'
      }
    },
    logout() {
      localStorage.removeItem('user')
      this.$router.push('/')
    }
  }
}
</script>

<style scoped lang="scss">
.dashboard-container {
  min-height: 100vh;
  background-color: #f8f9fa;
}

// Header del Dashboard
.dashboard-header {
  background: linear-gradient(135deg, $primary-color 0%, $secondary-color 100%);
  color: white;
  padding: 2rem 0;
  margin-bottom: 2rem;

  .header-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;

    .user-info h1 {
      margin: 0;
      font-size: 2rem;
      font-weight: 600;
    }

    .user-info p {
      margin: 0.5rem 0 0 0;
      opacity: 0.9;
    }
  }
}

// Métricas principales
.metrics-section {
  max-width: 1200px;
  margin: 0 auto 2rem auto;
  padding: 0 1rem;

  .metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
  }

  .metric-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    display: flex;
    align-items: center;
    gap: 1rem;
    transition: transform 0.2s ease;

    &:hover {
      transform: translateY(-2px);
    }

    .metric-icon {
      width: 60px;
      height: 60px;
      border-radius: 12px;
      background: linear-gradient(135deg, $primary-color, $secondary-color);
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-size: 1.5rem;
    }

    .metric-content h3 {
      margin: 0;
      font-size: 2rem;
      font-weight: 700;
      color: $primary-color;
    }

    .metric-content p {
      margin: 0.25rem 0 0 0;
      color: #6c757d;
      font-size: 0.9rem;
    }
  }
}

// Selector de vistas
.view-selector {
  max-width: 1200px;
  margin: 0 auto 2rem auto;
  padding: 0 1rem;

  .view-tabs {
    display: flex;
    background: white;
    border-radius: 12px;
    padding: 0.5rem;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    gap: 0.5rem;
    overflow-x: auto;

    .view-tab {
      padding: 0.75rem 1.5rem;
      border: none;
      background: transparent;
      border-radius: 8px;
      color: #6c757d;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s ease;
      white-space: nowrap;
      display: flex;
      align-items: center;
      gap: 0.5rem;

      &:hover {
        background: #f8f9fa;
        color: $primary-color;
      }

      &.active {
        background: $primary-color;
        color: white;
      }
    }
  }
}

// Contenido principal
.main-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem 2rem 1rem;
}

// Vista Overview
.overview-view {
  .projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 1.5rem;
    margin-top: 1.5rem;
  }

  .project-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease;

    &:hover {
      transform: translateY(-2px);
    }

    .project-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 1rem;

      h3 {
        margin: 0;
        color: $primary-color;
        font-size: 1.25rem;
      }

      .status-badge {
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;

        &.en-progreso {
          background: #e3f2fd;
          color: #1976d2;
        }

        &.planificación {
          background: #fff3e0;
          color: #f57c00;
        }

        &.completado {
          background: #e8f5e8;
          color: #388e3c;
        }

        &.iniciado {
          background: #f3e5f5;
          color: #7b1fa2;
        }

        &.crítica {
          background: #ffebee;
          color: #d32f2f;
        }
      }
    }

    .project-description {
      color: #6c757d;
      margin-bottom: 1rem;
      font-size: 0.9rem;
    }

    .project-progress {
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 1rem;

      .progress-bar {
        flex: 1;
        height: 8px;
        background: #e9ecef;
        border-radius: 4px;
        overflow: hidden;

        .progress-fill {
          height: 100%;
          background: linear-gradient(90deg, $primary-color, $secondary-color);
          transition: width 0.3s ease;
        }
      }

      .progress-text {
        font-weight: 600;
        color: $primary-color;
        font-size: 0.9rem;
      }
    }

    .project-details {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;

      .detail-item {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        color: #6c757d;
        font-size: 0.85rem;

        i {
          color: $primary-color;
        }
      }
    }
  }
}

// Vista de Tareas
.tasks-view {
  .tasks-container {
    margin-top: 1.5rem;
  }

  .task-columns {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
  }

  .task-column {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);

    h3 {
      margin: 0 0 1rem 0;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 1.1rem;
    }

    .task-list {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .task-item {
      padding: 1rem;
      border-radius: 8px;
      border-left: 4px solid;

      &.pending {
        background: #fff8e1;
        border-left-color: #ff9800;
      }

      &.in-progress {
        background: #e3f2fd;
        border-left-color: #2196f3;
      }

      &.completed {
        background: #e8f5e8;
        border-left-color: #4caf50;
      }

      h4 {
        margin: 0 0 0.5rem 0;
        font-size: 0.95rem;
        color: $primary-color;
      }

      p {
        margin: 0 0 0.5rem 0;
        color: #6c757d;
        font-size: 0.85rem;
      }

      .task-date {
        font-size: 0.8rem;
        color: #6c757d;
      }
    }
  }
}

// Vista de Calendario
.calendar-view {
  .calendar-container {
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    padding: 1.5rem;
    margin-top: 1.5rem;
  }

  .calendar-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;

    h3 {
      margin: 0;
      color: $primary-color;
      font-size: 1.5rem;
      font-weight: 600;
    }

    .nav-btn {
      background: $primary-color;
      color: white;
      border: none;
      border-radius: 8px;
      padding: 0.5rem 0.75rem;
      cursor: pointer;
      transition: background 0.2s ease;

      &:hover {
        background: darken($primary-color, 10%);
      }
    }
  }

  .calendar-grid {
    .calendar-weekdays {
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      gap: 1px;
      margin-bottom: 1px;

      .weekday {
        background: #f8f9fa;
        padding: 0.75rem;
        text-align: center;
        font-weight: 600;
        color: #495057;
        font-size: 0.9rem;
      }
    }

    .calendar-days {
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      gap: 1px;
      background: #dee2e6;
    }

    .calendar-day {
      background: white;
      min-height: 100px;
      padding: 0.5rem;
      position: relative;
      cursor: pointer;
      transition: background 0.2s ease;

      &:hover {
        background: #f8f9fa;
      }

      &.other-month {
        background: #f8f9fa;
        color: #adb5bd;
      }

      &.today {
        background: lighten($primary-color, 45%);
        
        .day-number {
          background: $primary-color;
          color: white;
          border-radius: 50%;
          width: 24px;
          height: 24px;
          display: flex;
          align-items: center;
          justify-content: center;
          font-weight: 600;
        }
      }

      &.has-events {
        border-left: 3px solid $primary-color;
      }

      .day-number {
        font-size: 0.9rem;
        font-weight: 500;
        margin-bottom: 0.25rem;
      }

      .day-events {
        display: flex;
        flex-direction: column;
        gap: 2px;
        margin-top: 0.25rem;

        .event-dot {
          width: 8px;
          height: 8px;
          border-radius: 50%;
          margin-right: 4px;

          &.deadline {
            background: #dc3545;
          }

          &.milestone {
            background: #28a745;
          }

          &.meeting {
            background: #007bff;
          }
        }

        .more-events {
          font-size: 0.7rem;
          color: #6c757d;
          margin-top: 2px;
        }
      }
    }
  }

  .calendar-legend {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-top: 1.5rem;
    padding-top: 1rem;
    border-top: 1px solid #dee2e6;

    .legend-item {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.9rem;
      color: #6c757d;

      .event-dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;

        &.deadline {
          background: #dc3545;
        }

        &.milestone {
          background: #28a745;
        }

        &.meeting {
          background: #007bff;
        }
      }
    }
  }
}

// Placeholders para vistas en desarrollo
.calendar-placeholder,
.gantt-placeholder {
  text-align: center;
  padding: 4rem 2rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  margin-top: 1.5rem;

  i {
    font-size: 4rem;
    color: #dee2e6;
    margin-bottom: 1rem;
  }

  p {
    color: #6c757d;
    margin: 0.5rem 0;
  }
}

// Vista de Gantt
.gantt-view {
  .gantt-container {
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    padding: 1.5rem;
    margin-top: 1.5rem;
  }

  .gantt-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;

    .gantt-controls {
      display: flex;
      gap: 0.5rem;

      .zoom-btn {
        padding: 0.5rem 1rem;
        border: 1px solid #dee2e6;
        background: white;
        border-radius: 6px;
        cursor: pointer;
        transition: all 0.2s ease;
        color: #6c757d;

        &:hover {
          background: #f8f9fa;
          border-color: $primary-color;
        }

        &.active {
          background: $primary-color;
          color: white;
          border-color: $primary-color;
        }
      }
    }
  }

  .gantt-chart {
    overflow-x: auto;
    border: 1px solid #dee2e6;
    border-radius: 8px;
  }

  .gantt-timeline {
    min-width: 800px;

    .timeline-header {
      display: flex;
      background: #f8f9fa;
      border-bottom: 2px solid #dee2e6;

      .project-column {
        width: 200px;
        padding: 1rem;
        font-weight: 600;
        color: $primary-color;
        border-right: 1px solid #dee2e6;
      }

      .dates-column {
        flex: 1;
        display: flex;

        .date-cell {
          padding: 1rem 0.5rem;
          text-align: center;
          border-right: 1px solid #dee2e6;
          font-size: 0.9rem;
          font-weight: 500;
          color: #495057;
        }
      }
    }

    .gantt-rows {
      .gantt-row {
        display: flex;
        border-bottom: 1px solid #dee2e6;
        min-height: 80px;

        &:hover {
          background: #f8f9fa;
        }

        .project-info {
          width: 200px;
          padding: 1rem;
          border-right: 1px solid #dee2e6;
          display: flex;
          flex-direction: column;
          justify-content: center;

          h4 {
            margin: 0 0 0.25rem 0;
            color: $primary-color;
            font-size: 0.95rem;
          }

          .project-duration {
            font-size: 0.8rem;
            color: #6c757d;
          }
        }

        .timeline-row {
          flex: 1;
          position: relative;
          padding: 1rem 0;

          .project-bar {
            position: absolute;
            height: 20px;
            background: linear-gradient(90deg, $primary-color, $secondary-color);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 0.8rem;
            font-weight: 600;
            overflow: hidden;
            top: 15px;

            .progress-overlay {
              position: absolute;
              left: 0;
              top: 0;
              height: 100%;
              background: rgba(255, 255, 255, 0.3);
              border-radius: 10px;
            }

            .project-label {
              position: relative;
              z-index: 2;
            }
          }

          .task-bar {
            position: absolute;
            height: 12px;
            background: #6c757d;
            border-radius: 6px;
            display: flex;
            align-items: center;
            padding: 0 0.5rem;

            .task-label {
              font-size: 0.7rem;
              color: white;
              white-space: nowrap;
              overflow: hidden;
              text-overflow: ellipsis;
            }
          }
        }
      }
    }
  }

  .gantt-legend {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid #dee2e6;

    .legend-item {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.9rem;
      color: #6c757d;

      .legend-bar {
        width: 20px;
        height: 12px;
        border-radius: 6px;

        &.project-bar-sample {
          background: linear-gradient(90deg, $primary-color, $secondary-color);
        }

        &.task-bar-sample {
          background: #6c757d;
        }

        &.progress-sample {
          background: rgba(255, 255, 255, 0.3);
          border: 1px solid $primary-color;
        }
      }
    }
  }
}

// Vista de Reportes
.reports-view {
  .reports-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 1.5rem;
    margin-top: 1.5rem;
  }

  .report-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);

    h3 {
      margin: 0 0 1rem 0;
      color: $primary-color;
    }

    .chart-placeholder {
      text-align: center;
      padding: 3rem 1rem;
      background: #f8f9fa;
      border-radius: 8px;

      i {
        font-size: 3rem;
        color: #dee2e6;
        margin-bottom: 1rem;
      }

      p {
        color: #6c757d;
        margin: 0;
      }
    }
  }
}

// Vista de Equipo
.team-view {
  .team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-top: 1.5rem;
  }

  .team-member-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    text-align: center;

    .member-avatar {
      width: 60px;
      height: 60px;
      border-radius: 50%;
      background: linear-gradient(135deg, $primary-color, $secondary-color);
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 1rem auto;
      color: white;
      font-size: 1.5rem;
    }

    h4 {
      margin: 0 0 0.5rem 0;
      color: $primary-color;
    }

    p {
      margin: 0 0 1rem 0;
      color: #6c757d;
      font-size: 0.9rem;
    }

    .member-projects {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      justify-content: center;

      .project-tag {
        padding: 0.25rem 0.5rem;
        background: #e9ecef;
        border-radius: 12px;
        font-size: 0.75rem;
        color: #495057;
      }
    }
  }
}

// Responsive
@media (max-width: 768px) {
  .dashboard-header .header-content {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }

  .metrics-grid {
    grid-template-columns: 1fr;
  }

  .view-tabs {
    justify-content: flex-start;
  }

  .projects-grid {
    grid-template-columns: 1fr;
  }

  .task-columns {
    grid-template-columns: 1fr;
  }

  .reports-grid {
    grid-template-columns: 1fr;
  }

  .team-grid {
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  }
}
</style>
