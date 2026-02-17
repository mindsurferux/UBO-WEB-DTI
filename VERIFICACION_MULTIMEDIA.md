# 🔍 Guía de Verificación - Nueva Convención Multimedia

## ✅ Checklist de Verificación Post-Migración

### 1️⃣ Verificar que el servidor inicia sin errores

```bash
npm run serve
```

**Esperado:** Servidor inicia en `http://localhost:8080` sin errores de compilación.

---

### 2️⃣ Páginas a Probar Visualmente

Abre cada una de estas rutas y verifica que las imágenes carguen correctamente:

#### **Página Principal** 
- **URL:** `http://localhost:8080/`
- **Verificar:** 
  - ✅ Logo UBO en navbar
  - ✅ Banner hero de proyectos TI
  - ✅ Slider de texto funciona (3 slides)

#### **Nosotros**
- **URL:** `http://localhost:8080/about`
- **Verificar:**
  - ✅ Banner de equipo

#### **Servicios**
- **URL:** `http://localhost:8080/services`
- **Verificar:**
  - ✅ Banner de servicios
  - ✅ 6 cards con imágenes:
    - Seguimiento Proyectos TI
    - Mesa de Ayuda TI
    - Consultoría TI
    - Conectividad WI-FI
    - Software y Aplicaciones
    - Base de Conocimiento

#### **Ciberseguridad**
- **URL:** `http://localhost:8080/cybersecurity`
- **Verificar:**
  - ✅ Banner de ciberseguridad
  - ✅ 5 cards con imágenes:
    - Registrar Incidente
    - Políticas de contraseñas
    - Programa de Concientización
    - Antivirus Corporativo
    - Reportes

#### **Consejos**
- **URL:** `http://localhost:8080/consejos`
- **Verificar:**
  - ✅ Banner de ciberseguridad
  - ✅ 5 cards de consejos con imágenes diferentes

#### **Noticias**
- **URL:** `http://localhost:8080/news`
- **Verificar:**
  - ✅ 4 noticias con imágenes

#### **Detalle de Noticia**
- **URL:** `http://localhost:8080/news/1` (cualquier ID del 1-4)
- **Verificar:**
  - ✅ Imagen de banner de la noticia
  - ✅ Imagen adicional en sidebar

#### **Login**
- **URL:** `http://localhost:8080/login`
- **Verificar:**
  - ✅ Logo UBO en navbar
  - ✅ Logo UBO en caja izquierda
  - ✅ Background con imagen de fondo

---

### 3️⃣ Verificar Consola del Navegador

Abre DevTools (F12) → Pestaña Console

**Esperado:** 
- ❌ Sin errores 404 de imágenes
- ❌ Sin warnings de rutas no encontradas
- ✅ Todas las imágenes con status 200

---

### 4️⃣ Verificar Network (Red)

Abre DevTools (F12) → Pestaña Network → Filtra por "Img"

**Esperado:**
- ✅ Todas las imágenes cargando desde `/img/[categoria]/`
- ✅ Status 200 en todas las imágenes
- ❌ Ninguna imagen con status 404

---

## 🗂️ Estructura de Rutas por Módulo

### Banners
```
/img/banners/banner-home-proyectos.webp
/img/banners/banner-nosotros.webp
/img/banners/banner-servicios.webp
/img/banners/banner-ciberseguridad.webp
```

### Servicios
```
/img/servicios/servicio-seguimiento-proyectos.webp
/img/servicios/servicio-mesa-ayuda.webp
/img/servicios/servicio-consultoria.webp
/img/servicios/servicio-wifi.webp
/img/servicios/servicio-software.webp
/img/servicios/servicio-base-conocimiento.webp
```

### Ciberseguridad
```
/img/ciberseguridad/ciber-registrar-incidente.webp
/img/ciberseguridad/ciber-politicas-password.webp
/img/ciberseguridad/ciber-concientizacion.webp
/img/ciberseguridad/ciber-antivirus.webp
/img/ciberseguridad/ciber-reportes.webp
```

### Noticias
```
/img/noticias/noticia-phishing-global.webp
/img/noticias/noticia-suplantacion.webp
/img/noticias/noticia-estrategia-nacional.webp
/img/noticias/noticia-asesoria-gratuita.webp
```

### Consejos
```
/img/consejos/consejo-ofertas-buenas.webp
/img/consejos/consejo-mensajes-urgentes.webp
/img/consejos/consejo-info-sensible.webp
/img/consejos/consejo-verificar-url.webp
/img/consejos/consejo-software-actualizado.webp
```

### Usuarios
```
/img/usuarios/user-placeholder.webp
/img/usuarios/user01.webp
/img/usuarios/user02.webp
/img/usuarios/user03.webp
```

### Logos
```
/img/logos/logo-ubo-color.png
/img/logos/logo-ubo-color.webp
```

### General
```
/img/general/pc-01.png
/img/general/pc-02.png
```

**Excepción:** El background de login (`img20.webp`) permanece en `src/assets/img/` porque se usa en CSS.

---

## 🚨 Problemas Comunes y Soluciones

### ❌ Imágenes no cargan (404)

**Causa:** El servidor de desarrollo no detectó los cambios.

**Solución:**
```bash
# Detener el servidor (Ctrl+C)
# Limpiar caché
npm run build
# Reiniciar
npm run serve
```

### ❌ Algunas imágenes muestran las antiguas

**Causa:** Caché del navegador.

**Solución:**
- Ctrl + Shift + R (hard refresh)
- O en DevTools: clic derecho en Refresh → Empty Cache and Hard Reload

### ❌ Errores de compilación

**Causa:** Alguna ruta no fue actualizada correctamente.

**Solución:**
Busca referencias antiguas:
```bash
# Desde PowerShell en la raíz del proyecto
Get-ChildItem -Recurse -Include *.vue,*.js,*.json | Select-String "img0[1-9]\.webp|img1[0-9]\.webp"
```

---

## 📋 Tabla de Verificación Rápida

Marca cada item al verificarlo:

| Módulo | Imágenes | Estado |
|--------|----------|--------|
| Navbar | Logo | ⬜ |
| Home | Banner hero | ⬜ |
| About | Banner nosotros | ⬜ |
| Services | Banner + 6 cards | ⬜ |
| Cybersecurity | Banner + 5 cards | ⬜ |
| Consejos | Banner + 5 cards | ⬜ |
| News | 4 noticias | ⬜ |
| NewsDetail | Banner + sidebar | ⬜ |
| Login | Logo + background | ⬜ |

---

## 🎯 Si TODO está ✅

### Puedes proceder a limpiar archivos antiguos:

```bash
# SOLO DESPUÉS DE VERIFICAR QUE TODO FUNCIONA

# Eliminar imágenes antiguas de public/img raíz
Remove-Item public\img\img04.webp
Remove-Item public\img\img05.webp
Remove-Item public\img\img06.webp
Remove-Item public\img\img07.webp
Remove-Item public\img\img08.webp
Remove-Item public\img\img09.webp
Remove-Item public\img\img11.webp
Remove-Item public\img\img12.webp
Remove-Item public\img\img13.webp
Remove-Item public\img\img14.webp
Remove-Item public\img\img15.webp
Remove-Item public\img\img16.webp
Remove-Item public\img\img17.webp
Remove-Item public\img\img18.webp
Remove-Item public\img\img19.webp
Remove-Item public\img\user-placeholder.webp
Remove-Item public\img\user01.webp
Remove-Item public\img\user02.webp
Remove-Item public\img\user03.webp

# Eliminar imágenes antiguas de src/assets/img
Remove-Item src\assets\img\img01.webp
Remove-Item src\assets\img\img02.webp
Remove-Item src\assets\img\img03.webp
Remove-Item src\assets\img\img10.webp
Remove-Item src\assets\img\img20.webp
Remove-Item src\assets\img\Marca-UBO.png
Remove-Item src\assets\img\Marca-UBO.webp
Remove-Item src\assets\img\pc-01.png
Remove-Item src\assets\img\pc-02.png
```

---

## 📞 Soporte

Si encuentras algún problema:
1. Revisa **MULTIMEDIA_MAPPING.md** para ver el mapeo original
2. Revisa **MIGRACION_COMPLETADA.md** para ver los cambios realizados
3. Verifica que copiaste las imágenes y no las moviste

---

**Última actualización:** 07-10-2025
