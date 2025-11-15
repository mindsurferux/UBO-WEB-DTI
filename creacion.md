### **1. Prerrequisitos**

Antes de comenzar, asegúrate de tener instalados los siguientes elementos en tu sistema:

- **Node.js y npm**: Puedes descargarlos desde https://nodejs.org/.

- **Vue CLI**: Si no lo tienes instalado, puedes hacerlo ejecutando:

  ```bash
  npm install -g @vue/cli
  ```

  Verifica la instalación con:

  ```bash
  vue --version
  ```

### **2. Crear el Proyecto con Vue CLI**

Abre una terminal y navega hasta el directorio donde deseas crear tu proyecto. Luego, ejecuta el siguiente comando para iniciar la creación del proyecto:

```bash
vue create mi-proyecto
```

**Nota:** Reemplaza `mi-proyecto` por el nombre que desees para tu proyecto.

### **3. Configuración del Proyecto**

Después de ejecutar el comando anterior, Vue CLI te presentará opciones para configurar tu proyecto. Sigue estos pasos:

1. **Seleccionar Preset Personalizado:**

   Cuando te pregunte si deseas usar un preset predeterminado o personalizar la configuración, selecciona:

   ```bash
   ❯ Manually select features
   ```

2. **Seleccionar las Características Necesarias:**

   A continuación, selecciona las siguientes características usando las teclas de flecha y la barra espaciadora:

   - **Choose Vue version**
   - **Babel**
   - **Router**
   - **Vuex**
   - **CSS Pre-processors**
   - **Linter / Formatter**

   Presiona `Enter` después de seleccionar las opciones.

3. **Seleccionar la Versión de Vue:**

   Cuando te pregunte por la versión de Vue, selecciona **Vue 3**.

4. **Configuración de Vue Router:**

   - **¿Usar History mode para el router?** Selecciona **Yes** o **No** según tu preferencia. Generalmente, **Yes** es recomendado para aplicaciones que necesitan URLs limpias.

5. **Configuración de Vuex:**

   Vuex se configurará automáticamente como parte de las características seleccionadas.

6. **Seleccionar el Preprocesador CSS:**

   Selecciona **Sass/SCSS (with dart-sass)** para utilizar SASS como preprocesador CSS.

7. **Configurar Linter / Formatter:**

   Configura según tus preferencias. Por ejemplo:

   - **Linter / Formatter:** ESLint with error prevention only
   - **Dónde guardar los archivos de configuración:** En el proyecto
   - **Formato de código:** Prettier
   - **¿Quieres que se ejecute ESLint al hacer commit?** Selecciona **Yes**.

8. **Guardar esta configuración como un preset (opcional):**

   Puedes optar por guardar esta configuración para futuros proyectos o no. Selecciona **No** si prefieres no guardarla.

### **4. Instalar Bootstrap**

Una vez creado el proyecto, navega al directorio del proyecto e instala Bootstrap y sus dependencias:

```bash
cd mi-proyecto
npm install bootstrap@5.3.0
```

**Nota:** Asegúrate de verificar la versión más reciente de Bootstrap en https://getbootstrap.com/ y ajusta el comando si es necesario.

### **5. Configurar Bootstrap en el Proyecto**

Para integrar Bootstrap con SASS en tu proyecto Vue, sigue estos pasos:

1. **Importar Bootstrap en el Proyecto:**

   Abre el archivo principal de estilos. Si estás utilizando SASS, probablemente sea `src/assets/styles.scss`. Si no existe, créalo.

   ```scss
   /* src/assets/styles.scss */
   
   // Importar variables de Bootstrap si deseas personalizarlas
   @import "~bootstrap/scss/bootstrap";
   ```

2. **Importar el Archivo de Estilos en tu Proyecto:**

   Abre el archivo `main.js` (o `main.ts` si usas TypeScript) y añade la importación del archivo de estilos:

   ```javascript
   // src/main.js
   
   import { createApp } from 'vue';
   import App from './App.vue';
   import router from './router';
   import store from './store';
   import './assets/styles.scss'; // Importar los estilos
   
   createApp(App)
     .use(store)
     .use(router)
     .mount('#app');
   ```

3. **Verificar la Integración:**

   Puedes verificar que Bootstrap está funcionando agregando alguna clase de Bootstrap a un componente. Por ejemplo, en `App.vue`:

   ```vue
   <template>
     <div id="app">
       <nav class="navbar navbar-expand-lg navbar-light bg-light">
         <a class="navbar-brand" href="#">Mi Proyecto Vue</a>
       </nav>
       <router-view/>
     </div>
   </template>
   
   <script>
   export default {
     name: 'App',
   };
   </script>
   
   <style scoped>
   /* Tus estilos personalizados */
   </style>
   ```

### **6. Ejecutar el Proyecto**

Finalmente, inicia el servidor de desarrollo para ver tu proyecto en acción:

```bash
npm run serve
```

Abre tu navegador y navega a http://localhost:8080 (o el puerto que indique la terminal) para ver tu aplicación Vue 3 con Vue Router, Vuex, SASS y Bootstrap integrados.

### **Resumen de Comandos**

Para resumir, aquí están los comandos principales que ejecutaste:

```bash
# Instalar Vue CLI globalmente (si no lo tienes)
npm install -g @vue/cli

# Crear el proyecto
vue create mi-proyecto

# Navegar al directorio del proyecto
cd mi-proyecto

# Instalar Bootstrap
npm install bootstrap@5.3.0

# Ejecutar el servidor de desarrollo
npm run serve
```