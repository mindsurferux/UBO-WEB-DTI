# Modelo de datos para Noticias (UBO TI App 1.8)

Este documento resume el **criterio funcional**, la **estructura actual** y una **propuesta de modelo de datos** para la sección de noticias, pensando en un futuro **CMS / backend**.

## 1. Contexto funcional

- Las noticias se consumen desde un **JSON** (`src/assets/noticias.json`), simulando un futuro CMS.
- Existen dos vistas principales:
  - `NewsView.vue` (listado + hero de noticias).
  - `NewsDetailView.vue` (detalle de una noticia).
- Hay un componente de tarjeta:
  - `Noticia.vue` (tarjeta en listado, con layout alternado por `orientation`).
- Las imágenes se sirven desde `public/img/noticias/` y se referencian vía ruta absoluta (`/img/noticias/...`), coherente con un despliegue estático.

Además, en `UBO Web DTI/Img/Noticias` y `UBO Web DTI/Textos/Noticias` existen **assets finales**:

- Imágenes por noticia:
  - `Noticia 1` → banner + foto vertical + imagen de resumen.
  - `Noticia 2` → banner + foto vertical + imagen de resumen.
  - `Noticia 4` → banner + foto vertical + imagen de resumen.
- Textos validados en `.docx`:
  - `Noticia 1 (titular).docx`
  - `Noticia 2.docx`
  - `Noticia 4.docx`
  - `Noticias (Reales).docx` (probable consolidado de contenido).

La arquitectura está pensada como un **mock de CMS**: todo se orquesta vía JSON para facilitar la futura migración a una base de datos / API.

---

## 2. Estructura actual de `noticias.json`

Archivo: `src/assets/noticias.json`

Cada noticia tiene actualmente los siguientes campos (ejemplo simplificado):

```jsonc
{
  "id": 1,
  "title": "Alerta global: 6.400 millones de correos de phishing se envían diariamente",
  "description": "Resumen corto...",
  "fullContent": "Texto largo con pseudo-markdown...",
  "author": "Equipo de Ciberseguridad DTI",
  "date": "15 de Marzo, 2024",
  "category": "Ciberseguridad",
  "tags": ["Phishing", "Ciberseguridad"],
  "image": "/img/noticias/noticia-phishing-global.webp",
  "orientation": "right",
  "buttonText": "Ver noticia"
}
```

### Uso de estos campos en la UI

1. **Listado (`NewsView.vue` + `Noticia.vue`)**
   - `NewsView.vue`:
     - `heroNews` = primera noticia de `newsItems`.
     - `otherNews` = resto de noticias.
     - `heroNews.image` se usa como **imagen hero horizontal**.
     - El texto hero principal tiene un **copy fijo** actualmente (no viene del JSON).
   - `Noticia.vue`:
     - `item.image` se usa como imagen de la tarjeta.
     - `item.orientation` controla la disposición (`left` / `right`).
     - `item.title`, `item.description`, `item.buttonText` para contenido y CTA.

2. **Detalle (`NewsDetailView.vue`)**
   - Busca la noticia por `id` en `noticias.json`.
   - Usa `news.image` como **banner principal** (horizontal, top de la página).
   - Usa `news.description` como párrafo introductorio.
   - Usa `news.fullContent` como contenido completo (renderizado como HTML simple).
   - Muestra meta-datos: `news.author`, `news.date`, `news.category`.
   - Sidebar:
     - Tiene una **imagen fija**, hardcodeada:
       ```vue
       <img src="/img/noticias/noticia-estrategia-nacional.webp" ... />
       ```
     - Esto ignora cualquier posible **foto vertical específica** por noticia.

---

## 3. Necesidades detectadas

1. **Noticias reales vs mock**
   - El JSON actual contiene 4 noticias de ciberseguridad (mock).
   - En UBO Web DTI hay 3 noticias reales (1, 2, 4) con texto+imágenes.
   - Es razonable **eliminar una noticia** (probablemente la actual `id:3`) al consolidar los contenidos reales.

2. **Gestión de múltiples imágenes por noticia**
   - Cada noticia real tiene, en la práctica, **al menos 2 tipos de imagen**:
     - Banner/resumen (horizontal) → para listado o hero.
     - Foto vertical → ideal para sidebar o imagen de detalle.
   - El modelo actual solo contempla **un campo `image`**.

3. **Separación de responsabilidades**
   - Hoy se reutiliza `image` para:
     - Tarjeta de listado.
     - Banner principal de detalle.
   - La imagen de sidebar está fija, no ligada a la noticia.
   - El texto hero en `NewsView.vue` no proviene del JSON.

4. **Pensando en un CMS / base de datos**
   - Se necesitará un modelo que permita:
     - Varios tamaños / roles de imagen por noticia (hero, detalle, vertical/sidebar, thumbnail).
     - Metadatos básicos (autor, fecha, categoría, tags).
     - Identificador estable (`id` + `slug`) para URL amigable.
     - Información de estado (borrador, publicado, archivado).

---

## 4. Propuesta de modelo de datos para Noticias

Propuesta de esquema (JSON) orientado a un futuro backend/CMS:

```jsonc
{
  "id": 1,                     // Entero interno, estable.
  "slug": "alerta-phishing-global", // Identificador URL-friendly.

  "title": "Alerta global: 6.400 millones de correos de phishing se envían diariamente",
  "subtitle": "Contexto y riesgos del phishing a nivel mundial", // Opcional.

  "summary": "Resumen corto que se muestra en la tarjeta y en el hero.",
  "fullContent": "...",      // HTML o markdown ya procesable.

  "category": "Ciberseguridad",
  "tags": ["Phishing", "Prevención"],

  "author": "Equipo de Ciberseguridad DTI",
  "authorId": null,           // Futuro vínculo a tabla de autores (opcional).

  "publishedAt": "2024-03-15", // Idealmente ISO 8601.
  "updatedAt": "2024-03-20",   // Opcional.

  "status": "published",     // draft | published | archived

  "images": {
    "list": "/img/noticias/noticia-1-list.webp",          // Para tarjetas (Noticia.vue).
    "hero": "/img/noticias/noticia-1-hero.webp",          // Para hero de NewsView.
    "detailBanner": "/img/noticias/noticia-1-banner.webp",// Banner principal en detalle.
    "detailSidebar": "/img/noticias/noticia-1-vertical.webp", // Foto vertical en sidebar.
    "thumbnail": "/img/noticias/noticia-1-thumb.webp"     // Opcional, para listados pequeños.
  },

  "layout": {
    "orientation": "left",      // Layout alternado en listado (left/right).
    "isHero": false              // Si esta noticia puede ser usada como hero.
  }
}
```

### Ventajas de este modelo

- **Claridad semántica**: cada imagen tiene un rol explícito (hero, detalle, sidebar).
- Facilita **cambio de diseño** sin reestructurar datos (solo se ajusta qué campo usa cada vista).
- Es **extensible**: se pueden agregar campos como `seoTitle`, `seoDescription`, `readingTime`, etc.
- Encaja bien con un CMS: cada noticia es un documento claro con metadatos, contenido y un objeto de imágenes.

---

## 5. Mapeo propuesto a la UI actual

### 5.1 Listado (`NewsView.vue` + `Noticia.vue`)

- `NewsView.vue`:
  - `heroNews`:
    - Imagen: `heroNews.images.hero`.
    - Título: `heroNews.title`.
    - Descripción del hero: usar `heroNews.summary` (en lugar de texto fijo).
  - `otherNews`:
    - Tarjetas usan:
      - `item.images.list` como imagen.
      - `item.title`, `item.summary`, `item.buttonText` (o derivar `buttonText` en vista).

- `Noticia.vue`:
  - Reemplazar `item.image` por `item.images.list`.
  - Mantener `item.orientation` para layout.

### 5.2 Detalle (`NewsDetailView.vue`)

- Banner principal:
  - Reemplazar `news.image` por `news.images.detailBanner`.

- Sidebar:
  - Reemplazar la imagen fija por `news.images.detailSidebar`.

- Contenido:
  - `news.summary` como párrafo intro (`lead-paragraph`).
  - `news.fullContent` como cuerpo principal (ya se procesa a HTML).

---

## 6. Relación con los assets de "UBO Web DTI"

Para cada noticia real disponible (1, 2 y 4), se puede hacer el siguiente mapeo base:

### Noticia 1

- Input (carpeta):
  - `Noticia 1 titular resumen.png`
  - `Noticia 1 titular banner.png`
  - `Noticia 1 foto vertical.png`

- Propuesta de asignación:
  - `images.list` → versión optimizada de `Noticia 1 titular resumen` → `/img/noticias/noticia-1-list.webp`.
  - `images.hero` → versión optimizada de `Noticia 1 titular banner` → `/img/noticias/noticia-1-hero.webp`.
  - `images.detailBanner` → puede reutilizar `hero` o tener variante dedicada.
  - `images.detailSidebar` → versión vertical de `Noticia 1 foto vertical` → `/img/noticias/noticia-1-vertical.webp`.

### Noticia 2

- Input:
  - `Noticia 2 resumen.png`
  - `Noticia 2 banner.png`
  - `Noticia 2 foto vertical.png`

- Misma lógica que Noticia 1, con nombres coherentes (`noticia-2-*`).

### Noticia 4

- Input:
  - `Noticia 4 resumen.png`
  - `Noticia 4  banner.png`
  - `Noticia 4 foto vertical.png`

- Misma lógica, con nombres `noticia-4-*`.

### Noticia que se elimina

- Dado que solo hay contenido real claro para 1, 2 y 4, la noticia mock actual `id:3` es una buena candidata a ser eliminada del JSON cuando se actualicen contenidos reales.

---

## 7. Pasos sugeridos para la implementación futura

> Nota: esta sección es una guía para etapas posteriores; no implica que ya se hayan hecho los cambios en código.

1. **Refactor de `noticias.json`**
   - Introducir estructura `images` y `layout` por noticia.
   - Agregar campos `summary`, `slug`, `status`, `publishedAt` (en ISO).
   - Eliminar o migrar la noticia que se decida retirar (probablemente la actual `id:3`).

2. **Actualización de imágenes**
   - Convertir todas las imágenes de `UBO Web DTI/Img/Noticias` a `.webp` optimizadas.
   - Guardarlas en `public/img/noticias/` con nombres consistentes (`noticia-1-hero.webp`, `noticia-1-vertical.webp`, etc.).
   - Actualizar rutas en `noticias.json` según el esquema `images`.

3. **Ajustes en las vistas**
   - `NewsView.vue`:
     - Usar `heroNews.images.hero` y `heroNews.summary`.
   - `Noticia.vue`:
     - Usar `item.images.list`.
   - `NewsDetailView.vue`:
     - Usar `news.images.detailBanner` y `news.images.detailSidebar`.

4. **Pensando en un backend real**
   - Este JSON podría mapearse 1:1 a una colección `news` en una base de datos (por ejemplo, Firestore, PostgreSQL, etc.).
   - La clave primaria podría ser `id` o `slug` según convenga.
   - El campo `status` permitiría manejar borradores y publicaciones programadas.

---

## 8. Resumen

- La sección de noticias ya está organizada alrededor de un **JSON pensado como mock de CMS**.
- Actualmente hay una sola imagen por noticia y una imagen fija en el detalle.
- Con las nuevas imágenes (banner + vertical) y textos reales en `.docx`, tiene sentido evolucionar hacia un modelo más rico con:
  - Múltiples roles de imagen por noticia (`list`, `hero`, `detailBanner`, `detailSidebar`).
  - Metadatos claros (`slug`, `status`, fechas en formato estándar).
- Este documento sirve como **referencia de diseño de datos** para futuras intervenciones y para la implementación de un backend real o un CMS.

---

## 9. Conversión de textos `.docx` a `.md` (referencia)

Para facilitar la integración de contenidos validados desde "UBO Web DTI" al proyecto, se creó un pequeño script de apoyo en Python:

- Script: `docx_to_md.py` (en la raíz del proyecto `ubo-tiapp-1.8`).
- Objetivo: convertir archivos `.docx` a `.md` usando `pandoc`.

### 9.1. Dependencias

- Sistema basado en Debian/Ubuntu (incluyendo WSL).
- Paquete `pandoc` instalado en el sistema:

  ```bash
  sudo apt-get update
  sudo apt-get install -y pandoc
  ```

### 9.2. Uso básico del script

Desde la carpeta del proyecto `ubo-tiapp-1.8`:

```bash
python3 docx_to_md.py input.docx [output.md]
```

- Si no se especifica `output.md`, el script genera un archivo `.md` con el mismo nombre que el `.docx` de origen, en la misma ruta.
- El script valida la existencia del archivo y muestra mensajes claros de error si `pandoc` no está disponible.

Ejemplo mínimo:

```bash
python3 docx_to_md.py \
  "/home/vandalit/CodigoWSL/UBO Web DTI/Textos/Consejos/Buenas Prácticas para evitar el Phishing.docx" \
  "docs/md_referencia/Consejos/buenas_practicas_phishing.md"
```

### 9.3. Flujo aplicado para "UBO Web DTI/Textos/Noticias"

Textos de origen (validados en `.docx`):

- `UBO Web DTI/Textos/Noticias/Noticia 1 (titular).docx`
- `UBO Web DTI/Textos/Noticias/Noticia 2.docx`
- `UBO Web DTI/Textos/Noticias/Noticia 4.docx`
- `UBO Web DTI/Textos/Noticias/Noticias (Reales).docx`

Salida de referencia en Markdown dentro del proyecto `ubo-tiapp-1.8`:

- `docs/md_referencia/Noticias/noticia_1.md`
- `docs/md_referencia/Noticias/noticia_2.md`
- `docs/md_referencia/Noticias/noticia_4.md`
- `docs/md_referencia/Noticias/noticias_reales.md`

Ejemplo de comando encadenado utilizado (una vez instalado `pandoc`):

```bash
mkdir -p docs/md_referencia/Noticias && \
python3 docx_to_md.py \
  "/home/vandalit/CodigoWSL/UBO Web DTI/Textos/Noticias/Noticia 1 (titular).docx" \
  "docs/md_referencia/Noticias/noticia_1.md" && \
python3 docx_to_md.py \
  "/home/vandalit/CodigoWSL/UBO Web DTI/Textos/Noticias/Noticia 2.docx" \
  "docs/md_referencia/Noticias/noticia_2.md" && \
python3 docx_to_md.py \
  "/home/vandalit/CodigoWSL/UBO Web DTI/Textos/Noticias/Noticia 4.docx" \
  "docs/md_referencia/Noticias/noticia_4.md" && \
python3 docx_to_md.py \
  "/home/vandalit/CodigoWSL/UBO Web DTI/Textos/Noticias/Noticias (Reales).docx" \
  "docs/md_referencia/Noticias/noticias_reales.md"
```

De forma análoga, se generó el Markdown de referencia para Consejos:

- Origen: `"UBO Web DTI/Textos/Consejos/Buenas Prácticas para evitar el Phishing.docx"`.
- Salida: `docs/md_referencia/Consejos/buenas_practicas_phishing.md`.

Estos `.md` sirven como **texto fuente consolidado** para poblar `noticias.json` (campos como `fullContent`, `summary`, `category`, etc.), manteniendo una referencia clara entre los archivos originales de diseño/comunicación y la implementación en el frontend.
