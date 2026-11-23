# web-tecnoligia

## NODO · Portal Web Interactivo para el Sector Productivo de Bucaramanga

Proyecto final integrador — 30% corte 3 · Diseño Web Avanzado · Grupo B191 · UTS

**Caso seleccionado:** Tecnología — startup tecnológica bumanguesa.  
**Integrantes:** Dayron Camilo Diaz · Santiago Alejandro Figueroa · Andres Felipe Contreras Rodriguez · Kevin Andrey Florez Ramírez.

> La marca NODO, los datos de contacto y los proyectos del portafolio son ficticios y fueron creados con criterios de realismo profesional para el proyecto académico.

---

## 1. URL pública funcional (entregable obligatorio)

**Estado:** ⏳ Pendiente de publicar con la cuenta del grupo. No se acepta `localhost` como entrega.

Cuando publiques, reemplaza esta línea por la URL real:

```
URL_PUBLICA=https://TU-SITIO.netlify.app
```

### Publicar en 3 minutos (Netlify Drop, recomendado)

1. Comprime la carpeta `Portal_NODO_Tecnologia_Bucaramanga` en un `.zip`.
2. Entra a <https://app.netlify.com/drop> e inicia sesión con un correo del grupo.
3. Arrastra el `.zip` a la zona de carga.
4. Copia la URL que muestra Netlify (p. ej. `https://nodo-bucaramanga.netlify.app`).
5. Pégala en la sección 1 de este README y en el documento técnico (sección 12).

**Alternativas:** Vercel, GitHub Pages, Firebase Hosting, Render o InfinityFree.  
El proyecto es 100% estático: no necesita base de datos ni variables de entorno.

---

## 2. Ejecutar en local

```bash
cd Portal_NODO_Tecnologia_Bucaramanga
python -m http.server 8765
```

Abre <http://127.0.0.1:8765/index.html>.  
> Es importante usar un servidor local (no abrir el HTML con doble clic) para que `fetch()` pueda leer los archivos JSON.

---

## 3. Estructura del proyecto

```
Portal_NODO_Tecnologia_Bucaramanga/
├── index.html                  Página principal (banner, nosotros, servicios, clima, portafolio)
├── servicios.html              Catálogo dinámico + filtros + planes
├── contacto.html               Formulario avanzado + validaciones + mapa
├── multimedia.html             Video institucional + galería + lightbox
├── assets/
│   ├── css/                    styles.css + Bootstrap 5.3.3 local
│   ├── js/                     classes.js (POO) + app.js + jQuery/Bootstrap locales
│   ├── data/                   servicios.json + empresa.json
│   ├── img/                    14 fotografías WebP optimizadas
│   ├── fonts/                  Manrope y Space Grotesk (woff2 embebidas)
│   ├── icons/                  sprite.svg + favicon.svg
│   └── video/                  nodo-startup.mp4 + nodo-es.vtt
├── docs/
│   ├── Documento_Tecnico_IEEE_NODO.pdf
│   ├── GUION_VIDEO_EXPOSICION.md
│   └── evidencia/              Capturas reales desktop / tablet / móvil
└── tools/                      Generadores de páginas, video, evidencia y PDF
```

---

## 4. Cumplimiento de requerimientos del PDF

| Requerimiento | Dónde está |
|---|---|
| HTML5 semántico | `header`, `nav`, `main`, `section`, `article`, `figure`, `footer` en las 4 páginas |
| Banner principal adaptable | Carrusel Bootstrap en `#inicio` (3 diapositivas WebP) |
| Navegación responsive | `navbar-expand-lg` + `navbar-toggler` + media queries |
| Iconografía y tipografía personalizada | `assets/icons/sprite.svg`, fuentes woff2 locales |
| Multimedia optimizada | WebP con `loading="lazy"`, MP4 H.264, WebVTT |
| Productos/servicios dinámicos | `assets/data/servicios.json` → `CatalogoServicios` |
| CSS Grid, Flexbox, media queries | `assets/css/styles.css` (breakpoints 1200/992/768/576) |
| Efectos fade, slide, hover | `.reveal`, `@keyframes`, transiciones y carrusel |
| Formularios con todos los campos | `contacto.html` (texto, correo, teléfono, select, checkbox, textarea, archivo) |
| Validaciones y mensajes dinámicos | `ValidadorFormulario` en `assets/js/classes.js` |
| JavaScript + jQuery + DOM | `app.js` y `classes.js` |
| Programación Orientada a Objetos | 9 clases ES6 en `classes.js` |
| Framework CSS | Bootstrap 5.3.3 alojado localmente |
| API pública externa | Open-Meteo (clima de Bucaramanga) en `ClimaService` |
| JSON | `servicios.json`, `empresa.json` y `localStorage` de solicitudes |
| Pseudoelementos `::before` / `::after` | Marco de video, tarjetas, etiquetas y galería |
| Documento técnico IEEE | `docs/Documento_Tecnico_IEEE_NODO.pdf` (13 páginas) |
| Evidencia responsive | `docs/evidencia/` (6 capturas reales) |
| Guion de video exposición | `docs/GUION_VIDEO_EXPOSICION.md` (máx. 10 minutos) |
| URL pública | ⏳ Paso 1 de este README |

---

## 5. Créditos de recursos externos

- **Fotografías:** Unsplash (<https://unsplash.com/license>). Descargadas y convertidas a WebP; incluidas en `assets/img/`.
- **Video:** montaje original generado con FFmpeg a partir de esas imágenes (`tools/generate_video.py`).
- **Fuentes:** Manrope y Space Grotesk — Google Fonts, SIL Open Font License.
- **API:** Open-Meteo (<https://open-meteo.com/>), uso público sin clave.
- **Mapa:** OpenStreetMap (<https://www.openstreetmap.org/>).
- **Librerías:** Bootstrap 5.3.3 (MIT), jQuery 3.7.1 (MIT).

---

## 6. Exposición

El guion para la video exposición (máximo 10 minutos) está en [`docs/GUION_VIDEO_EXPOSICION.md`](docs/GUION_VIDEO_EXPOSICION.md).  
Incluye qué mostrar en pantalla, qué explicar y qué código abrir en cada minuto, además del apartado de trabajo colaborativo.
