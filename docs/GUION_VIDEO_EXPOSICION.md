# Guion · Video de exposición (máximo 10 minutos)

**Proyecto:** NODO · Startup tecnológica de Bucaramanga  
**Grupo:** B191 · Diseño Web Avanzado · UTS  
**Formato sugerido:** pantalla compartida + voz en off de los integrantes, 9:30 min.

> Regla de oro: mostrar el sitio funcionando, abrir el código, explicar la técnica y demostrar el responsive. No leer el documento técnico en voz alta.

| Tiempo | En pantalla | Qué decir / hacer |
|---|---|---|
| 00:00 – 00:40 | Presentación: nombre del proyecto, sector y los 4 integrantes. | "Somos el grupo B191. Elegimos el sector tecnología y creamos NODO, una startup bumanguesa de soluciones digitales. Hoy mostraremos el portal, su arquitectura y el trabajo colaborativo." |
| 00:40 – 01:40 | `index.html` en escritorio. Recargar y mostrar el carrusel. | Presentar el negocio, el banner adaptable, la navegación y la tipografía. Mencionar HTML5 semántico: `header`, `nav`, `main`, `section`, `footer`. |
| 01:40 – 02:40 | Sección "Servicios destacados" y archivo `assets/data/servicios.json`. | "Estas tres tarjetas no están escritas en el HTML: se cargan desde JSON con `fetch` y se convierten en objetos `Servicio`." Abrir el JSON y una tarjeta generada. |
| 02:40 – 03:40 | Widget del clima en vivo. | Explicar la API pública Open-Meteo, las coordenadas de Bucaramanga y el manejo de errores. Mostrar `ClimaService` en `classes.js`. |
| 03:40 – 04:40 | `servicios.html`: filtros **Todos / Desarrollo / Datos / Infraestructura**. | Explicar `CatalogoServicios.filtrar()`, el uso de jQuery para animar las tarjetas y CSS Grid para la maquetación. Mencionar fade, slide y hover. |
| 04:40 – 05:50 | `contacto.html`: llenar el formulario sin datos, mostrar errores, corregir y enviar. | Recorrer campo por campo: texto, correo, teléfono, select, checkbox, textarea y archivo. Mostrar validación de 5 MB y mensajes dinámicos. Abrir `ValidadorFormulario`. |
| 05:50 – 06:30 | Consola → `localStorage` → `nodo_solicitudes`. | "La solicitud se guarda como JSON en el navegador. Es nuestro mecanismo de almacenamiento sin backend." Mostrar el contador en pantalla. |
| 06:30 – 07:20 | `multimedia.html`: reproducir el video y abrir la galería (lightbox). | Destacar WebP, `loading="lazy"`, subtítulos VTT, controles propios y los pseudoelementos `::before`/`::after` del marco. |
| 07:20 – 08:20 | `assets/js/classes.js` completo (scroll por las clases). | Explicar POO: `Servicio`, `CatalogoServicios`, `ClimaService`, `ValidadorFormulario`, `Galeria`, `ReproductorVideo`, `RevealOnScroll`. "Cada clase encapsula estado y métodos." |
| 08:20 – 09:10 | Demo responsive con DevTools: 1440 px → 820 px → 390 px. | Mostrar el menú colapsado, el cambio de columnas y el video adaptable. Mencionar media queries 1200/992/768/576. Usar las capturas de `docs/evidencia/` si falla la conexión. |
| 09:10 – 09:40 | URL pública en el navegador + carpeta del proyecto + PDF. | "El sitio está publicado en [PEGAR URL]. Entregamos carpeta, documento IEEE, evidencia y este video." |
| 09:40 – 10:00 | Cierre: integrantes en el pie del sitio. | Breve conclusión y agradecimiento. cada integrante dice una frase sobre lo que aportó. |

## Checklist antes de grabar

- [ ] URL pública funcionando y verificada desde otro navegador o celular.
- [ ] Servidor o hosting activo durante la grabación.
- [ ] Pestañas abiertas: sitio, `classes.js`, `servicios.json`, DevTools.
- [ ] Formulario probado con un correo electrónico válido y un archivo PDF pequeño.
- [ ] Consola del navegador sin errores rojos.
- [ ] Video ≤ 10 minutos y con audio claro.
- [ ] Enlace del video pegado en `assets/data/empresa.json` (`videoExposicion`) y en el README.

## Código que conviene tener a la mano

```js
// POO: crear un servicio y renderizarlo
const servicio = new Servicio(datosJSON);
catalogo.renderizar();

// API pública
new ClimaService('#clima-widget', 7.1193, -73.1227).obtener();

// Validación
new ValidadorFormulario('#contacto-form').iniciar();

// jQuery + DOM
$('#servicios-grid').html(html).hide().fadeIn(300);
```

> Nota: se permiten pequeños ajustes de redacción al grabar; lo importante es cubrir los cinco puntos exigidos: funcionamiento del sitio, explicación técnica, código desarrollado, diseño responsive y trabajo colaborativo.
