# 📝 Notas Técnicas - Migración de Multimedia

## 🔧 Excepción: Background Login

### Problema Identificado

Durante la migración, se identificó que las **imágenes usadas en CSS dentro de componentes Vue** requieren un tratamiento especial.

### Contexto

El archivo `LoginView.vue` usa una imagen de fondo en su sección `<style scoped>`:

```scss
.background {
  background: url('/img/general/background-login.webp') center center / cover no-repeat;
}
```

### Error Generado

```
ERROR in ./src/views/LoginView.vue
Module not found: Error: Can't resolve '/img/general/background-login.webp'
```

### Causa Raíz

Webpack procesa las rutas en CSS de componentes Vue e intenta resolverlas como módulos. Las rutas absolutas que comienzan con `/` no funcionan correctamente porque:

1. Webpack intenta resolver la ruta como un módulo npm
2. No puede encontrar el archivo en `public/` durante el proceso de build
3. Las rutas absolutas en CSS de componentes necesitan ser relativas o usar alias

### Solución Implementada

**Mantener la imagen en `src/assets/img/`** con ruta relativa:

```scss
.background {
  background: url('../assets/img/img20.webp') center center / cover no-repeat;
}
```

### Alternativas Evaluadas

#### ❌ Opción 1: Usar alias `~@`
```scss
background: url('~@/../../public/img/general/background-login.webp');
```
**Problema:** Ruta muy larga y confusa.

#### ❌ Opción 2: Usar `require()`
```vue
<style>
.background {
  background-image: url(v-bind(backgroundImage));
}
</style>
<script>
export default {
  data() {
    return {
      backgroundImage: require('@/../../public/img/general/background-login.webp')
    }
  }
}
</script>
```
**Problema:** Requiere cambios mayores en el componente.

#### ✅ Opción 3: Mantener en assets (SELECCIONADA)
```scss
background: url('../assets/img/img20.webp') center center / cover no-repeat;
```
**Ventajas:**
- Solución simple y directa
- Sin cambios en la estructura del componente
- Webpack procesa correctamente
- Funciona con hot-reload

---

## 📋 Regla General

### Para imágenes en `<template>` → Usar `public/img/`

```vue
<template>
  <img src="/img/logos/logo-ubo-color.png" />
</template>
```

✅ **Funciona correctamente** porque Vue procesa el template en runtime.

### Para imágenes en `<style>` → Usar `src/assets/img/`

```vue
<style scoped>
.background {
  background: url('../assets/img/imagen.webp');
}
</style>
```

✅ **Funciona correctamente** porque webpack resuelve la ruta relativa correctamente.

---

## 🎯 Resumen de la Excepción

| Aspecto | Detalle |
|---------|---------|
| **Archivo afectado** | `src/views/LoginView.vue` |
| **Imagen** | `img20.webp` (background login) |
| **Ubicación original** | `src/assets/img/img20.webp` |
| **Ubicación final** | `src/assets/img/img20.webp` (sin cambios) |
| **Motivo** | CSS en componentes Vue requiere rutas relativas |
| **Impacto en convención** | Mínimo - solo 1 imagen de 32 |

---

## 📚 Referencias

### Documentación Oficial Vue.js
- [Asset Handling in Vue CLI](https://cli.vuejs.org/guide/html-and-static-assets.html#static-assets-handling)
- Las rutas en CSS son procesadas por `css-loader` y `file-loader`

### Documentación Webpack
- [file-loader](https://v4.webpack.js.org/loaders/file-loader/)
- Las rutas relativas en CSS se resuelven basándose en la ubicación del archivo

---

## 💡 Lecciones Aprendidas

1. **Templates vs CSS:** Diferentes contextos de procesamiento
2. **Public vs Assets:** 
   - `public/` → Para recursos estáticos accesibles directamente
   - `src/assets/` → Para recursos procesados por webpack
3. **Rutas en CSS:** Siempre usar rutas relativas en componentes Vue

---

## 🔍 Cómo Identificar Situaciones Similares

Buscar usos de `url()` en archivos Vue:

```bash
# PowerShell
Get-ChildItem src -Recurse -Include *.vue | Select-String "url\(" | Select-Object Path, Line
```

Si encuentras rutas absolutas a `/img/` en CSS, considerar moverlas a `assets/`.

---

## ✅ Estado Actual

- ✅ Error resuelto
- ✅ Documentación actualizada
- ✅ Convención general intacta (31 de 32 imágenes en `public/`)
- ✅ Build exitoso

---

**Fecha de resolución:** 07-10-2025  
**Documentado por:** Sistema automatizado
