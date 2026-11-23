/* ==========================================================================
   NODO · Clases ES6 (Programación Orientada a Objetos)
   ========================================================================== */

/** Configuración del sitio: consume JSON local y lo inyecta en el DOM. */
class Configuracion {
  constructor(url) {
    this.url = url;
    this.datos = {
      nombre: 'NODO',
      telefono: '+57 7 612 4820',
      email: 'hola@nodotecnologia.co',
      direccion: 'Cra. 15 # 36-24, Centro, Bucaramanga',
      horario: 'Lunes a viernes, 8:00 a. m. — 6:00 p. m. (UTC-5)',
      ubicacion: 'Bucaramanga, Santander, Colombia',
      integrantes: [
        'Dayron Camilo Diaz',
        'Santiago Alejandro Figueroa',
        'Andres Felipe Contreras Rodriguez',
        'Kevin Andrey Florez Ramírez'
      ],
      videoExposicion: '',
      anio: new Date().getFullYear()
    };
  }

  async cargar() {
    try {
      const respuesta = await fetch(this.url);
      if (!respuesta.ok) throw new Error('No se pudo leer empresa.json');
      this.datos = Object.assign(this.datos, await respuesta.json());
    } catch (error) {
      console.info('NODO: usando configuración de respaldo (JSON local).', error.message);
    }
    this.aplicar();
    return this.datos;
  }

  aplicar() {
    document.querySelectorAll('[data-config]').forEach(elemento => {
      const clave = elemento.dataset.config;
      if (this.datos[clave] === undefined) return;
      elemento.textContent = this.datos[clave];

      if (elemento.tagName === 'A') {
        if (clave === 'email') elemento.href = `mailto:${this.datos.email}`;
        if (clave === 'telefono') elemento.href = `tel:${this.datos.telefono.replace(/\s/g, '')}`;
        if (clave === 'whatsapp') elemento.href = `https://wa.me/${this.datos.whatsapp.replace(/\D/g, '')}`;
      }
    });

    const lista = document.getElementById('integrantes-list');
    if (lista && Array.isArray(this.datos.integrantes)) {
      lista.innerHTML = this.datos.integrantes.map(nombre => `<span>${nombre}</span>`).join('');
    }

    const anio = document.getElementById('anio');
    if (anio) anio.textContent = this.datos.anio;

    const video = document.getElementById('video-exposicion');
    if (video) {
      if (this.datos.videoExposicion) {
        video.href = this.datos.videoExposicion;
        video.classList.remove('d-none');
      } else {
        video.classList.add('d-none');
      }
    }
  }
}

/** Modelo de un servicio del catálogo. */
class Servicio {
  constructor(datos) {
    Object.assign(this, datos);
  }

  get iconoSVG() {
    return `<svg class="icono" aria-hidden="true"><use href="#${this.icono}"></use></svg>`;
  }

  get etiquetasHTML() {
    const etiquetas = (this.etiquetas || []).map(t => `<span class="tag">${t}</span>`).join('');
    return etiquetas + `<span class="tag destacado">${this.duracion}</span>`;
  }

  tarjeta(indice = 0) {
    return `
      <article class="card-nodo servicio-card reveal reveal-retraso-${(indice % 3) + 1}"
               data-categoria="${this.categoria}" data-servicio="${this.id}">
        <img class="servicio-img" src="${this.imagen}"
             alt="Representación visual del servicio ${this.nombre}" loading="lazy" width="900" height="600">
        <div class="icono-caja">${this.iconoSVG}</div>
        <h3>${this.nombre}</h3>
        <p>${this.descripcion}</p>
        <div class="tags">${this.etiquetasHTML}</div>
        <a class="card-enlace" href="contacto.html?servicio=${this.id}">
          Solicitar este servicio
          <svg class="icono" aria-hidden="true"><use href="#i-arrow-right"></use></svg>
        </a>
      </article>`;
  }
}

/** Catálogo: carga JSON, renderiza tarjetas y aplica filtros con jQuery. */
class CatalogoServicios {
  constructor(contenedor, url, opciones = {}) {
    this.contenedor = contenedor;
    this.url = url;
    this.limite = opciones.limite || 0;
    this.servicios = [];
  }

  async cargar() {
    $(this.contenedor).addClass('cargando');
    try {
      const respuesta = await fetch(this.url);
      if (!respuesta.ok) throw new Error('HTTP ' + respuesta.status);
      const datos = await respuesta.json();
      this.servicios = datos.map(item => new Servicio(item));
    } catch (error) {
      console.info('NODO: catálogo usando datos de respaldo.', error.message);
      this.servicios = CatalogoServicios.respaldo().map(item => new Servicio(item));
    }

    if (this.limite) this.servicios = this.servicios.filter(s => s.destacado).slice(0, this.limite);

    this.renderizar();
    $(this.contenedor).removeClass('cargando');
    return this.servicios;
  }

  renderizar() {
    const html = this.servicios.map((servicio, i) => servicio.tarjeta(i)).join('');
    $(this.contenedor).html(html);
    document.dispatchEvent(new CustomEvent('nodo:contenido', { detail: this.contenedor }));
  }

  filtrar(categoria) {
    $(this.contenedor).children('.servicio-card').each(function () {
      const mostrar = categoria === 'todos' || $(this).attr('data-categoria') === categoria;
      if (mostrar) {
        $(this).removeClass('oculto').stop(true, true).fadeIn(220);
      } else {
        $(this).stop(true, true).fadeOut(180, () => $(this).addClass('oculto'));
      }
    });
  }

  vincularFiltros() {
    const self = this;
    $('[data-filtro]').on('click', function () {
      $('[data-filtro]').removeClass('activo');
      $(this).addClass('activo');
      self.filtrar($(this).attr('data-filtro'));
    });
  }

  static respaldo() {
    return [
      { id: 'desarrollo-web', nombre: 'Desarrollo web a medida', categoria: 'Desarrollo', descripcion: 'Sitios corporativos y aplicaciones web responsivas.', icono: 'i-code', imagen: 'assets/img/codigo.webp', etiquetas: ['HTML5', 'JavaScript'], duracion: '4 a 8 semanas', destacado: true },
      { id: 'inteligencia-datos', nombre: 'Analítica e inteligencia de datos', categoria: 'Datos', descripcion: 'Dashboards y reportes automáticos para decidir mejor.', icono: 'i-chart', imagen: 'assets/img/analitica.webp', etiquetas: ['JSON', 'SQL'], duracion: '3 a 6 semanas', destacado: true },
      { id: 'cloud-devops', nombre: 'Cloud y DevOps', categoria: 'Infraestructura', descripcion: 'Despliegue, monitoreo y escalabilidad en la nube.', icono: 'i-cloud', imagen: 'assets/img/servidores.webp', etiquetas: ['Docker', 'CI/CD'], duracion: '2 a 4 semanas', destacado: true }
    ];
  }
}

/** Consumo de la API pública Open-Meteo para el clima de Bucaramanga. */
class ClimaService {
  constructor(contenedor, latitud, longitud) {
    this.contenedor = contenedor;
    this.latitud = latitud;
    this.longitud = longitud;
  }

  get url() {
    return `https://api.open-meteo.com/v1/forecast?latitude=${this.latitud}&longitude=${this.longitud}` +
           `&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m` +
           `&timezone=America%2FBogota`;
  }

  async obtener() {
    try {
      const respuesta = await fetch(this.url);
      if (!respuesta.ok) throw new Error('HTTP ' + respuesta.status);
      const datos = await respuesta.json();
      this.datos = datos.current;
      this.renderizar();
    } catch (error) {
      console.info('NODO: API del clima no disponible, se muestra estado de respaldo.', error.message);
      $(this.contenedor).html(`
        <div class="clima-estado error">
          <svg class="icono" aria-hidden="true"><use href="#i-cloud"></use></svg>
          No fue posible consultar el clima en este momento. Intente recargar la página.
        </div>`);
    }
  }

  describir(codigo) {
    if (codigo === 0) return { texto: 'Cielo despejado', icono: 'i-sun' };
    if ([1, 2].includes(codigo)) return { texto: 'Parcialmente nublado', icono: 'i-cloud-sun' };
    if (codigo === 3) return { texto: 'Nublado', icono: 'i-cloud' };
    if ([45, 48].includes(codigo)) return { texto: 'Niebla', icono: 'i-cloud' };
    if ([51, 53, 55, 56, 57].includes(codigo)) return { texto: 'Llovizna', icono: 'i-cloud-rain' };
    if ([61, 63, 65, 66, 67].includes(codigo)) return { texto: 'Lluvia', icono: 'i-cloud-rain' };
    if ([80, 81, 82].includes(codigo)) return { texto: 'Aguaceros', icono: 'i-cloud-rain' };
    if ([95, 96, 99].includes(codigo)) return { texto: 'Tormenta eléctrica', icono: 'i-storm' };
    return { texto: 'Condiciones variables', icono: 'i-cloud-sun' };
  }

  renderizar() {
    const clima = this.describir(this.datos.weather_code);
    const hora = (this.datos.time || '').slice(11, 16) || 'ahora';
    $(this.contenedor).html(`
      <div class="clima-main">
        <div class="clima-temp">${Math.round(this.datos.temperature_2m)}<span style="font-size:1.7rem">°C</span></div>
        <div class="clima-icono">
          <svg class="icono" aria-hidden="true"><use href="#${clima.icono}"></use></svg>
        </div>
        <div>
          <div class="clima-desc">${clima.texto}</div>
          <div class="clima-lugar">Actualizado a las ${hora}</div>
        </div>
      </div>
      <div class="clima-meta">
        <div>Humedad<strong>${this.datos.relative_humidity_2m}%</strong></div>
        <div>Viento<strong>${this.datos.wind_speed_10m} km/h</strong></div>
        <div>Fuente<strong>Open-Meteo API</strong></div>
      </div>`);
  }
}

/** Persistencia de solicitudes en localStorage usando JSON. */
class AlmacenamientoContactos {
  constructor(clave = 'nodo_solicitudes') {
    this.clave = clave;
  }

  leer() {
    try {
      return JSON.parse(localStorage.getItem(this.clave)) || [];
    } catch (error) {
      return [];
    }
  }

  guardar(registro) {
    const registros = this.leer();
    registros.push(registro);
    localStorage.setItem(this.clave, JSON.stringify(registros));
    return registros.length;
  }

  total() {
    return this.leer().length;
  }
}

/** Validación avanzada del formulario de contacto. */
class ValidadorFormulario {
  constructor(selector) {
    this.form = $(selector);
    this.almacen = new AlmacenamientoContactos();
  }

  iniciar() {
    const self = this;

    this.form.on('submit', function (evento) {
      evento.preventDefault();
      self.enviar();
    });

    this.form.find('input, select, textarea').not('[type="checkbox"]').on('blur', function () {
      self.validarCampo($(this));
    });

    this.form.find('[type="checkbox"]').on('change', function () {
      self.validarCampo($(this));
    });

    this.form.find('input[type="file"]').on('change', function () {
      self.validarArchivo($(this));
      self.mostrarNombreArchivo(this);
    });

    $('#limpiar-form').on('click', function () {
      self.limpiar();
    });

    const parametros = new URLSearchParams(window.location.search);
    const servicio = parametros.get('servicio');
    if (servicio) {
      const nombres = {
        'desarrollo-web': 'Desarrollo web a medida',
        'apps-moviles': 'Aplicaciones móviles',
        'inteligencia-datos': 'Analítica e inteligencia de datos',
        'automatizacion': 'Automatización e IoT',
        'cloud-devops': 'Cloud y DevOps',
        'soporte-seguridad': 'Soporte y seguridad'
      };
      if (nombres[servicio]) {
        this.form.find('[name="tipo"]').val(servicio);
        this.form.find('[name="asunto"]').val(`Información sobre ${nombres[servicio]}`);
      }
    }

    this.actualizarContador();
    return this;
  }

  errorPara(campo, mensaje) {
    const contenedor = campo.closest('.form-field, .form-check-nodo');
    const error = contenedor.find('.mensaje-campo');
    error.text(mensaje).addClass('visible');
    campo.addClass('is-invalid').removeClass('is-valid');
    return false;
  }

  correcto(campo) {
    const contenedor = campo.closest('.form-field, .form-check-nodo');
    contenedor.find('.mensaje-campo').removeClass('visible');
    campo.removeClass('is-invalid').addClass('is-valid');
    return true;
  }

  validarCampo(campo) {
    const nombre = campo.attr('name');
    const valor = (campo.val() || '').trim();

    switch (nombre) {
      case 'nombre':
        return valor.length >= 3 ? this.correcto(campo) : this.errorPara(campo, 'Escribe tu nombre completo (mínimo 3 caracteres).');
      case 'email':
        return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(valor) ? this.correcto(campo) : this.errorPara(campo, 'Ingresa un correo electrónico válido.');
      case 'telefono': {
        const digitos = valor.replace(/\D/g, '');
        return digitos.length >= 7 && digitos.length <= 15 ? this.correcto(campo) : this.errorPara(campo, 'Ingresa un teléfono válido (7 a 15 dígitos).');
      }
      case 'empresa':
        return valor.length === 0 || valor.length >= 2 ? this.correcto(campo) : this.errorPara(campo, 'La empresa debe tener al menos 2 caracteres.');
      case 'tipo':
        return valor !== '' ? this.correcto(campo) : this.errorPara(campo, 'Selecciona el tipo de solicitud.');
      case 'asunto':
        return valor.length >= 5 ? this.correcto(campo) : this.errorPara(campo, 'El asunto debe tener al menos 5 caracteres.');
      case 'mensaje':
        return valor.length >= 20 ? this.correcto(campo) : this.errorPara(campo, 'Cuéntanos un poco más: mínimo 20 caracteres.');
      case 'terminos':
        return campo.is(':checked') ? this.correcto(campo) : this.errorPara(campo, 'Debes aceptar el tratamiento de tus datos.');
      default:
        return true;
    }
  }

  validarArchivo(campo) {
    const archivo = campo[0].files[0];
    if (!archivo) return true;
    const permitidos = ['application/pdf', 'image/png', 'image/jpeg', 'image/webp'];
    if (!permitidos.includes(archivo.type)) {
      return this.errorPara(campo, 'Solo se permiten archivos PDF, PNG, JPG o WEBP.');
    }
    if (archivo.size > 5 * 1024 * 1024) {
      return this.errorPara(campo, 'El archivo no debe superar los 5 MB.');
    }
    return this.correcto(campo);
  }

  mostrarNombreArchivo(input) {
    const caja = $(input).closest('.form-field').find('.archivo-preview');
    if (input.files.length) {
      caja.find('span').text(input.files[0].name + ' · ' + Math.round(input.files[0].size / 1024) + ' KB');
      caja.addClass('visible');
    } else {
      caja.removeClass('visible');
    }
  }

  validarTodo() {
    let valido = true;
    this.form.find('input[name], select[name], textarea[name]').each((i, elemento) => {
      const campo = $(elemento);
      if (campo.attr('type') === 'file') {
        if (!this.validarArchivo(campo)) valido = false;
      } else if (!this.validarCampo(campo)) {
        valido = false;
      }
    });
    return valido;
  }

  mensaje(texto, tipo) {
    $('#alerta-formulario')
      .attr('class', `alerta-dinamica ${tipo}`)
      .attr('role', 'alert')
      .html(`<svg class="icono" aria-hidden="true"><use href="#${tipo === 'exito' ? 'i-check' : 'i-shield'}"></use></svg><span>${texto}</span>`)
      .hide()
      .slideDown(280);
  }

  enviar() {
    if (!this.validarTodo()) {
      this.mensaje('Revisa los campos marcados en rojo antes de enviar tu solicitud.', 'error');
      this.form.find('.is-invalid').first().trigger('focus');
      return;
    }

    const datos = {};
    this.form.serializeArray().forEach(item => { datos[item.name] = item.value; });
    datos.fecha = new Date().toISOString();

    try {
      this.almacen.guardar(datos);
      this.mensaje('¡Listo! Recibimos tu solicitud. Te contactaremos en un plazo máximo de 24 horas hábiles.', 'exito');
      this.limpiar(false);
      this.actualizarContador();
    } catch (error) {
      this.mensaje('No se pudo guardar la solicitud en este navegador. Inténtalo nuevamente.', 'error');
    }
  }

  limpiar(mostrarMensaje = true) {
    this.form[0].reset();
    this.form.find('.is-valid, .is-invalid').removeClass('is-valid is-invalid');
    this.form.find('.mensaje-campo').removeClass('visible');
    this.form.find('.archivo-preview').removeClass('visible');
    if (mostrarMensaje) {
      this.mensaje('El formulario se ha limpiado correctamente.', 'informacion');
    }
  }

  actualizarContador() {
    $('#contador-solicitudes').text(this.almacen.total());
  }
}

/** Galería con lightbox usando jQuery + Bootstrap Modal. */
class Galeria {
  constructor(selector) {
    this.selector = selector;
  }

  iniciar() {
    const self = this;
    $(this.selector).on('click', function () {
      const imagen = $(this).find('img').attr('src');
      const titulo = $(this).attr('data-titulo') || '';
      const descripcion = $(this).attr('data-descripcion') || '';
      self.mostrar(imagen, titulo, descripcion);
    });
    return this;
  }

  mostrar(imagen, titulo, descripcion) {
    $('#lightbox-imagen').attr('src', imagen).attr('alt', titulo);
    $('#lightbox-titulo').text(titulo);
    $('#lightbox-descripcion').text(descripcion);
    $('#lightboxModal').modal('show');
  }
}

/** Reproductor de video con controles propios (DOM + POO). */
class ReproductorVideo {
  constructor(videoId) {
    this.video = document.getElementById(videoId);
    this.overlay = document.getElementById('video-overlay');
    this.barra = document.getElementById('barra-progreso');
    this.botonPlay = document.getElementById('btn-play-video');
    this.botonSonido = document.getElementById('btn-sonido');
  }

  iniciar() {
    if (!this.video) return this;

    this.overlay?.addEventListener('click', () => this.reproducir());
    this.botonPlay?.addEventListener('click', () => this.alternar());
    this.botonSonido?.addEventListener('click', () => {
      this.video.muted = !this.video.muted;
      this.botonSonido.innerHTML = this.video.muted
        ? '<svg class="icono"><use href="#i-x"></use></svg> Activar sonido'
        : '<svg class="icono"><use href="#i-check"></use></svg> Sonido activo';
    });

    this.video.addEventListener('timeupdate', () => {
      const porcentaje = (this.video.currentTime / this.video.duration) * 100 || 0;
      if (this.barra) this.barra.style.width = porcentaje + '%';
    });

    this.video.addEventListener('click', () => this.alternar());
    this.video.addEventListener('ended', () => this.overlay?.classList.remove('oculto'));

    this.barra?.parentElement.addEventListener('click', evento => {
      const rect = evento.currentTarget.getBoundingClientRect();
      this.video.currentTime = ((evento.clientX - rect.left) / rect.width) * this.video.duration;
    });

    return this;
  }

  reproducir() {
    this.video.play();
    this.overlay?.classList.add('oculto');
    if (this.botonPlay) this.botonPlay.textContent = 'Pausar video';
  }

  alternar() {
    if (this.video.paused) this.reproducir();
    else {
      this.video.pause();
      this.overlay?.classList.remove('oculto');
      if (this.botonPlay) this.botonPlay.textContent = 'Reproducir video';
    }
  }
}

/** Animaciones de entrada al hacer scroll (IntersectionObserver). */
class RevealOnScroll {
  constructor() {
    this.observador = new IntersectionObserver((entradas) => {
      entradas.forEach(entrada => {
        if (entrada.isIntersecting) {
          entrada.target.classList.add('visible');
          this.observador.unobserve(entrada.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    document.addEventListener('nodo:contenido', () => this.observarNuevos());
  }

  observarNuevos() {
    document.querySelectorAll('.reveal:not(.visible)').forEach(elemento => this.observador.observe(elemento));
  }

  iniciar() {
    this.observarNuevos();
    return this;
  }
}
