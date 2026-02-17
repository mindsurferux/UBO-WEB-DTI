# Mapeo de Multimedia - Proyecto UBO TI App

**Fecha de creación:** 2025-10-07  
**Propósito:** Registro de todas las rutas de imágenes antes de la reorganización

---

## 📁 Estructura Actual

### src/assets/img/ (Imágenes importadas)
Ubicación física: `c:\Users\vanda\Documents\Codigo\UBO-TI-py\ubo-tiapp-1.8\src\assets\img\`

| Archivo | Tamaño | Uso Actual | Componente/Vista |
|---------|--------|------------|------------------|
| Marca-UBO.png | 9094 bytes | Logo navbar | `src/components/Navbar.vue` línea 6 |
| Marca-UBO.webp | 8578 bytes | Logo login | `src/views/LoginView.vue` línea 18 |
| img01.webp | 1049136 bytes | Hero principal | `src/views/HomeView.vue` línea 14 |
| img02.webp | 590356 bytes | Banner nosotros | `src/views/AboutView.vue` línea 12 |
| img03.webp | 610024 bytes | Banner servicios | `src/views/ServicesView.vue` línea 12 |
| img10.webp | 417580 bytes | Banner ciberseguridad | `src/views/CybersecurityView.vue` línea 12 |
| img10.webp | 417580 bytes | Banner consejos | `src/views/ConsejosView.vue` línea 12 |
| img20.webp | 241396 bytes | Background login | `src/views/LoginView.vue` línea 199 (CSS) |
| pc-01.png | 1788439 bytes | Sin uso detectado | - |
| pc-02.png | 1817304 bytes | Sin uso detectado | - |

**Referencias encontradas:**
```
src/components/Navbar.vue:6         → ../assets/img/Marca-UBO.png
src/views/LoginView.vue:18          → ../assets/img/Marca-UBO.webp
src/views/LoginView.vue:199         → ../assets/img/img20.webp (CSS background)
src/views/HomeView.vue:14           → ../assets/img/img01.webp
src/views/AboutView.vue:12          → ../assets/img/img02.webp
src/views/ServicesView.vue:12       → ../assets/img/img03.webp
src/views/CybersecurityView.vue:12  → ../assets/img/img10.webp
src/views/ConsejosView.vue:12       → ../assets/img/img10.webp
```

---

### public/img/ (Imágenes públicas)
Ubicación física: `c:\Users\vanda\Documents\Codigo\UBO-TI-py\ubo-tiapp-1.8\public\img\`

#### Servicios (services.json)
| Archivo | Tamaño | Servicio | Línea JSON |
|---------|--------|----------|------------|
| img04.webp | 489162 bytes | Seguimiento Proyectos TI | services.json:4 |
| img05.webp | 526224 bytes | Mesa de Ayuda TI | services.json:12 |
| img06.webp | 523740 bytes | Consultoría TI | services.json:20 |
| img07.webp | 472904 bytes | Conectividad WI-FI UBO | services.json:28 |
| img08.webp | 272196 bytes | Software y Aplicaciones | services.json:36 |
| img09.webp | 350450 bytes | Base de Conocimiento | services.json:44 |

#### Ciberseguridad (cybersecurity.json)
| Archivo | Tamaño | Item | Línea JSON |
|---------|--------|------|------------|
| img11.webp | 364784 bytes | Registrar Incidente | cybersecurity.json:4 |
| img12.webp | 371456 bytes | Políticas de contraseñas | cybersecurity.json:12 |
| img13.webp | 357260 bytes | Programa de Concientización | cybersecurity.json:20 |
| img14.webp | 708406 bytes | Antivirus Corporativo | cybersecurity.json:28 |
| img15.webp | 374936 bytes | Reportes | cybersecurity.json:36 |

#### Noticias (noticias.json)
| Archivo | Tamaño | Noticia | Línea JSON |
|---------|--------|---------|------------|
| img16.webp | 209710 bytes | Noticia ID:1 - Phishing global | noticias.json:11 |
| img17.webp | 641046 bytes | Noticia ID:2 - Suplantación | noticias.json:24 |
| img18.webp | 170090 bytes | Noticia ID:3 - Estrategia nacional | noticias.json:37 |
| img19.webp | 291924 bytes | Noticia ID:4 - Asesoría gratuita | noticias.json:50 |

**Uso adicional de img18.webp:**
```
src/views/NewsDetailView.vue:45 → /img/img18.webp (imagen sidebar)
```

#### Consejos (consejos.json)
| Archivo | Tamaño | Consejo | Línea JSON |
|---------|--------|---------|------------|
| img16.webp | 209710 bytes | Consejo ID:1 - Ofertas buenas | consejos.json:6 |
| img17.webp | 641046 bytes | Consejo ID:2 - Mensajes urgentes | consejos.json:13 |
| img18.webp | 170090 bytes | Consejo ID:3 - Info sensible | consejos.json:20 |
| img19.webp | 291924 bytes | Consejo ID:4 - Verificar URL | consejos.json:27 |
| img20.webp | 241396 bytes | Consejo ID:5 - Software actualizado | consejos.json:34 |

#### Usuarios (equipo.json)
| Archivo | Tamaño | Usuario | Línea JSON |
|---------|--------|---------|------------|
| user-placeholder.webp | 5296 bytes | Todos (placeholder) | equipo.json:6,16,26,36,46,56,66 |
| user01.webp | 329820 bytes | Sin uso actual | - |
| user02.webp | 359990 bytes | Sin uso actual | - |
| user03.webp | 224426 bytes | Sin uso actual | - |

---

## 🔍 Análisis de Uso

### Imágenes Compartidas (Usadas múltiples veces)
- **img16.webp**: noticias.json (id:1) + consejos.json (id:1)
- **img17.webp**: noticias.json (id:2) + consejos.json (id:2)
- **img18.webp**: noticias.json (id:3) + consejos.json (id:3) + NewsDetailView.vue (sidebar)
- **img19.webp**: noticias.json (id:4) + consejos.json (id:4)
- **img20.webp**: consejos.json (id:5) + LoginView.vue (background)
- **img10.webp**: CybersecurityView.vue + ConsejosView.vue

### Imágenes Sin Uso Detectado
- `src/assets/img/pc-01.png`
- `src/assets/img/pc-02.png`
- `public/img/user01.webp`
- `public/img/user02.webp`
- `public/img/user03.webp`

---

## 📋 Resumen de Referencias por Archivo

### Archivos JSON (5)
1. **services.json** → 6 imágenes (img04 - img09)
2. **cybersecurity.json** → 5 imágenes (img11 - img15)
3. **noticias.json** → 4 imágenes (img16 - img19)
4. **consejos.json** → 5 imágenes (img16 - img20)
5. **equipo.json** → 1 imagen (user-placeholder.webp)

### Componentes Vue (8)
1. **Navbar.vue** → 1 imagen (Marca-UBO.png)
2. **LoginView.vue** → 2 imágenes (Marca-UBO.webp, img20.webp)
3. **HomeView.vue** → 1 imagen (img01.webp)
4. **AboutView.vue** → 1 imagen (img02.webp)
5. **ServicesView.vue** → 1 imagen (img03.webp)
6. **CybersecurityView.vue** → 1 imagen (img10.webp)
7. **ConsejosView.vue** → 1 imagen (img10.webp)
8. **NewsDetailView.vue** → 1 imagen (img18.webp)

---

## 🎯 Nueva Estructura Propuesta

```
public/img/
├── banners/
│   ├── banner-home-proyectos.webp (img01)
│   ├── banner-nosotros.webp (img02)
│   ├── banner-servicios.webp (img03)
│   └── banner-ciberseguridad.webp (img10)
│
├── servicios/
│   ├── servicio-seguimiento-proyectos.webp (img04)
│   ├── servicio-mesa-ayuda.webp (img05)
│   ├── servicio-consultoria.webp (img06)
│   ├── servicio-wifi.webp (img07)
│   ├── servicio-software.webp (img08)
│   └── servicio-base-conocimiento.webp (img09)
│
├── ciberseguridad/
│   ├── ciber-registrar-incidente.webp (img11)
│   ├── ciber-politicas-password.webp (img12)
│   ├── ciber-concientizacion.webp (img13)
│   ├── ciber-antivirus.webp (img14)
│   └── ciber-reportes.webp (img15)
│
├── noticias/
│   ├── noticia-phishing-global.webp (img16)
│   ├── noticia-suplantacion.webp (img17)
│   ├── noticia-estrategia-nacional.webp (img18)
│   └── noticia-asesoria-gratuita.webp (img19)
│
├── consejos/
│   ├── consejo-ofertas-buenas.webp (img16 - clonar de noticias)
│   ├── consejo-mensajes-urgentes.webp (img17 - clonar de noticias)
│   ├── consejo-info-sensible.webp (img18 - clonar de noticias)
│   ├── consejo-verificar-url.webp (img19 - clonar de noticias)
│   └── consejo-software-actualizado.webp (img20)
│
├── usuarios/
│   ├── user-placeholder.webp (existente)
│   ├── user01.webp (existente)
│   ├── user02.webp (existente)
│   └── user03.webp (existente)
│
├── logos/
│   ├── logo-ubo-color.png (Marca-UBO.png)
│   └── logo-ubo-color.webp (Marca-UBO.webp)
│
└── general/
    ├── background-login.webp (img20)
    ├── pc-01.png (sin uso)
    └── pc-02.png (sin uso)
```

---

## ✅ Checklist de Migración

- [ ] Crear directorios en public/img/
- [ ] Mover imágenes de src/assets/img/ a public/img/
- [ ] Renombrar imágenes según convención
- [ ] Actualizar services.json (6 referencias)
- [ ] Actualizar cybersecurity.json (5 referencias)
- [ ] Actualizar noticias.json (4 referencias)
- [ ] Actualizar consejos.json (5 referencias)
- [ ] Actualizar equipo.json (1 referencia)
- [ ] Actualizar Navbar.vue
- [ ] Actualizar LoginView.vue (2 referencias)
- [ ] Actualizar HomeView.vue
- [ ] Actualizar AboutView.vue
- [ ] Actualizar ServicesView.vue
- [ ] Actualizar CybersecurityView.vue
- [ ] Actualizar ConsejosView.vue
- [ ] Actualizar NewsDetailView.vue
- [ ] Verificar rutas rotas
- [ ] Probar aplicación

---

## 📝 Notas Importantes

1. **Imágenes compartidas**: Varias imágenes se usan en múltiples módulos (noticias y consejos)
2. **img20.webp**: Usado tanto en CSS (background) como en JSON (consejos)
3. **img10.webp**: Compartido entre CybersecurityView y ConsejosView
4. **Placeholders**: user-placeholder se usa para todos los miembros del equipo
5. **Archivos sin uso**: pc-01.png, pc-02.png, user01-03.webp no tienen referencias activas

---

**Fin del documento**
