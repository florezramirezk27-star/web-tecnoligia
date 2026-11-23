"""Genera las 4 páginas HTML del portal desde una plantilla común.
Uso: python tools/generate_pages.py
"""
import pathlib, re

BASE = pathlib.Path(__file__).resolve().parents[1]
sprite = (BASE / "assets/icons/sprite.svg").read_text(encoding="utf-8")
simbolos = re.search(r"<svg[^>]*>(.*?)</svg>", sprite, re.S).group(1).strip()

HEAD = """<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="__DESCRIPTION__">
  <meta name="theme-color" content="#0b1220">
  <meta property="og:type" content="website">
  <meta property="og:title" content="NODO | Startup tecnológica de Bucaramanga">
  <meta property="og:description" content="__DESCRIPTION__">
  <meta property="og:image" content="assets/img/hero-equipo.webp">
  <title>__TITLE__</title>
  <link rel="icon" type="image/svg+xml" href="assets/icons/favicon.svg">
  <link rel="preload" href="assets/fonts/SpaceGrotesk-700.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="assets/css/vendor/bootstrap.min.css">
  <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body data-page="__PAGE__">
  <a class="skip-link" href="#contenido">Saltar al contenido principal</a>
  <svg class="sprite" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">__SPRITE__</svg>
"""

NAV = """
  <header class="site-header">
    <nav class="navbar navbar-expand-lg navbar-nodo container" aria-label="Navegación principal">
      <a class="logo-marca" href="index.html" aria-label="NODO, inicio">
        <span class="logo-simbolo"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#i-logo"></use></svg></span>
        <span>NODO<small>Tech · Bucaramanga</small></span>
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navNodo"
              aria-controls="navNodo" aria-expanded="false" aria-label="Abrir menú de navegación">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navNodo">
        <ul class="navbar-nav ms-auto align-items-lg-center">
          <li class="nav-item"><a class="nav-link __A_INICIO__" data-nav="inicio" href="index.html#inicio">Inicio</a></li>
          <li class="nav-item"><a class="nav-link __A_NOSOTROS__" data-nav="nosotros" href="index.html#nosotros">Nosotros</a></li>
          <li class="nav-item"><a class="nav-link __A_SERVICIOS__" data-nav="servicios" href="servicios.html">Servicios</a></li>
          <li class="nav-item"><a class="nav-link __A_MULTIMEDIA__" data-nav="multimedia" href="multimedia.html">Multimedia</a></li>
          <li class="nav-item"><a class="nav-link __A_CONTACTO__" data-nav="contacto" href="contacto.html">Contacto</a></li>
        </ul>
        <a class="btn-nodo nav-cta" href="contacto.html">
          Hablemos <svg class="icono" aria-hidden="true"><use href="#i-arrow-right"></use></svg>
        </a>
      </div>
    </nav>
  </header>
"""

FOOTER = """
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a class="logo-marca logotipo-pequeno" href="index.html">
            <span class="logo-simbolo"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#i-logo"></use></svg></span>
            <span>NODO<small>Tech · Bucaramanga</small></span>
          </a>
          <p class="mt-3" data-config="descripcion">Startup tecnológica de Bucaramanga.</p>
          <div class="social-links">
            <a href="https://www.linkedin.com/" target="_blank" rel="noopener" aria-label="LinkedIn"><svg class="icono"><use href="#i-linkedin"></use></svg></a>
            <a href="https://github.com/" target="_blank" rel="noopener" aria-label="GitHub"><svg class="icono"><use href="#i-github"></use></svg></a>
            <a href="https://www.instagram.com/" target="_blank" rel="noopener" aria-label="Instagram"><svg class="icono"><use href="#i-instagram"></use></svg></a>
          </div>
        </div>
        <div>
          <h5>Navegación</h5>
          <ul>
            <li><a href="index.html">Inicio</a></li>
            <li><a href="index.html#nosotros">Nosotros</a></li>
            <li><a href="servicios.html">Servicios</a></li>
            <li><a href="multimedia.html">Multimedia</a></li>
            <li><a href="contacto.html">Contacto</a></li>
          </ul>
        </div>
        <div>
          <h5>Servicios</h5>
          <ul>
            <li><a href="servicios.html">Desarrollo web</a></li>
            <li><a href="servicios.html">Datos e IA</a></li>
            <li><a href="servicios.html">Cloud y DevOps</a></li>
            <li><a href="servicios.html">Soporte y seguridad</a></li>
          </ul>
        </div>
        <div>
          <h5>Contacto</h5>
          <address>
            <svg class="icono" aria-hidden="true"><use href="#i-pin"></use></svg>
            <span data-config="direccion">Cra. 15 # 36-24, Bucaramanga</span><br>
            <svg class="icono" aria-hidden="true"><use href="#i-phone"></use></svg>
            <a data-config="telefono" href="tel:+576124820">+57 7 612 4820</a><br>
            <svg class="icono" aria-hidden="true"><use href="#i-mail"></use></svg>
            <a data-config="email" href="mailto:hola@nodotecnologia.co">hola@nodotecnologia.co</a><br>
            <svg class="icono" aria-hidden="true"><use href="#i-clock"></use></svg>
            <span data-config="horario">Lunes a viernes, 8:00 a. m. — 6:00 p. m.</span>
          </address>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© <span id="anio">2026</span> NODO · Proyecto académico · Diseño Web Avanzado UTS</span>
        <div class="integrantes" id="integrantes-list" aria-label="Integrantes del grupo"></div>
        <a id="video-exposicion" class="d-none" href="#" target="_blank" rel="noopener">Ver video exposición</a>
      </div>
    </div>
  </footer>

  <button id="back-to-top" class="back-to-top" type="button" aria-label="Volver al inicio de la página">
    <svg class="icono" aria-hidden="true"><use href="#i-arrow-up"></use></svg>
  </button>

  <div class="modal fade modal-lightbox" id="lightboxModal" tabindex="-1" aria-labelledby="lightbox-titulo" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <button type="button" class="btn-close ms-auto" data-bs-dismiss="modal" aria-label="Cerrar galería"></button>
        <img id="lightbox-imagen" class="lightbox-body" src="" alt="">
        <div class="lightbox-pie">
          <h3 id="lightbox-titulo" class="h5 mb-1"></h3>
          <p id="lightbox-descripcion" class="mb-0 small"></p>
        </div>
      </div>
    </div>
  </div>

  <script src="assets/js/vendor/jquery-3.7.1.min.js"></script>
  <script src="assets/js/vendor/bootstrap.bundle.min.js"></script>
  <script src="assets/js/classes.js"></script>
  <script src="assets/js/app.js"></script>
</body>
</html>
"""

CTA = """
  <section class="section section-soft">
    <div class="container">
      <div class="cta-band reveal">
        <div class="row align-items-center">
          <div class="col-lg-8">
            <h2>¿Tu idea necesita un aliado tecnológico?</h2>
            <p>Cuéntanos qué quieres construir. Respondemos con una propuesta clara en menos de 24 horas hábiles.</p>
          </div>
          <div class="col-lg-4 text-lg-end">
            <a class="btn-nodo" href="contacto.html">Iniciar un proyecto <svg class="icono"><use href="#i-arrow-right"></use></svg></a>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

# ==========================================================================
# PÁGINA: INICIO
# ==========================================================================
INDEX = """
  <main id="contenido">
    <section id="inicio" class="hero" aria-label="Banner principal">
      <div id="heroCarousel" class="carousel slide hero-carousel" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <div class="hero-slide" style="background-image:url('assets/img/hero-equipo.webp')"></div>
          </div>
          <div class="carousel-item">
            <div class="hero-slide slide-2" style="background-image:url('assets/img/hero-oficina.webp')"></div>
          </div>
          <div class="carousel-item">
            <div class="hero-slide slide-3" style="background-image:url('assets/img/ciudad.webp')"></div>
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#heroCarousel" data-bs-slide="prev" aria-label="Diapositiva anterior">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#heroCarousel" data-bs-slide="next" aria-label="Diapositiva siguiente">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
        </button>
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#heroCarousel" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Ir a la diapositiva 1"></button>
          <button type="button" data-bs-target="#heroCarousel" data-bs-slide-to="1" aria-label="Ir a la diapositiva 2"></button>
          <button type="button" data-bs-target="#heroCarousel" data-bs-slide-to="2" aria-label="Ir a la diapositiva 3"></button>
        </div>
      </div>

      <div class="container">
        <div class="row align-items-center">
          <div class="col-xl-7 col-lg-8">
            <div class="hero-content">
              <span class="hero-badge"><span class="punto"></span> Startup bumanguesa · Santander, Colombia</span>
              <h1 class="hero-title">Tecnología que conecta a Bucaramanga con el <span class="resaltado">futuro</span>.</h1>
              <p class="hero-lead">Diseñamos y construimos soluciones digitales reales para empresas de nuestra región: desarrollo web, analítica de datos, automatización e infraestructura en la nube.</p>
              <div class="hero-actions">
                <a class="btn-nodo" href="servicios.html">Explorar servicios <svg class="icono"><use href="#i-arrow-right"></use></svg></a>
                <a class="btn-outline-nodo" href="contacto.html">Agendar una conversación</a>
              </div>
              <div class="hero-stats" aria-label="Cifras del equipo">
                <div><div class="stat-numero">40+</div><div class="stat-texto">Proyectos</div></div>
                <div><div class="stat-numero">15</div><div class="stat-texto">Aliados</div></div>
                <div><div class="stat-numero">99,9%</div><div class="stat-texto">Disponibilidad</div></div>
              </div>
            </div>
          </div>
          <div class="col-xl-5 d-none d-xl-block">
            <div class="hero-mockup" aria-hidden="true">
              <div class="code-window">
                <div class="barra"><i style="background:#ff5f57"></i><i style="background:#febc2e"></i><i style="background:#28c840"></i><span>nodo/soluciones.js</span></div>
                <pre><span class="c4">// tecnología local, alcance global</span>
<span class="c1">class</span> <span class="c2">Solucion</span> {
  <span class="c1">constructor</span>(ciudad) {
    <span class="c3">this</span>.ciudad = ciudad;
  }
  <span class="c2">conectar</span>() {
    <span class="c1">return</span> <span class="c3">this</span>.ciudad + <span class="c2">' → futuro'</span>;
  }
}
<span class="c1">const</span> nodo = <span class="c1">new</span> <span class="c2">Solucion</span>(<span class="c2">'Bucaramanga'</span>);
nodo.<span class="c2">conectar</span>();</pre>
              </div>
              <div class="hero-chip">
                <span class="chip-icon"><svg class="icono"><use href="#i-bolt"></use></svg></span>
                <span><strong>Equipo activo</strong><span>Desplegando soluciones 24/7</span></span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="nosotros" class="section section-light">
      <div class="container">
        <div class="grid-2">
          <div class="sobre-imagen reveal">
            <img class="imagen-redondeada" src="assets/img/equipo.webp" alt="Equipo de NODO colaborando en una solución tecnológica" loading="lazy" width="900" height="600">
            <div class="etiqueta-flotante"><strong>4</strong><span>integrantes · una misma visión</span></div>
          </div>
          <div class="reveal reveal-retraso-1">
            <span class="eyebrow">Quiénes somos</span>
            <h2>Una startup hecha en Santander, con mentalidad global.</h2>
            <p>Nacimos en Bucaramanga para acortar la distancia entre las ideas de los emprendedores locales y las herramientas tecnológicas que necesitan para crecer. Trabajamos con metodologías ágiles, código limpio y comunicación transparente.</p>
            <ul class="lista-features">
              <li><svg class="icono"><use href="#i-check"></use></svg> Equipo multidisciplinar de desarrollo, datos y diseño.</li>
              <li><svg class="icono"><use href="#i-check"></use></svg> Soluciones escalables, documentadas y fáciles de mantener.</li>
              <li><svg class="icono"><use href="#i-check"></use></svg> Acompañamiento cercano desde el primer boceto hasta el despliegue.</li>
            </ul>
            <a class="btn-ghost" href="multimedia.html">Conoce nuestro trabajo <svg class="icono"><use href="#i-arrow-right"></use></svg></a>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-soft">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow">Lo que hacemos</span>
          <h2>Servicios diseñados para impulsar tu operación</h2>
          <p>Seleccionamos las tecnologías adecuadas para cada reto, sin modas innecesarias y con foco en resultados medibles.</p>
        </div>
        <div id="servicios-destacados" class="grid-3" aria-live="polite">
          <div class="card-nodo"><p>Cargando servicios desde JSON…</p></div>
        </div>
        <div class="text-center mt-7 reveal">
          <a class="btn-nodo" href="servicios.html">Ver todos los servicios <svg class="icono"><use href="#i-arrow-right"></use></svg></a>
        </div>
      </div>
    </section>

    <section class="section section-dark">
      <div class="container">
        <div class="section-head centrado reveal">
          <span class="eyebrow">Metodología</span>
          <h2>Cuatro pasos, cero sorpresas</h2>
          <p>Un proceso claro que mantiene a tu equipo informado en cada etapa del proyecto.</p>
        </div>
        <div class="proceso">
          <article class="paso reveal"><h3>Descubrimiento</h3><p>Entendemos tu negocio, tus usuarios y el problema que hay que resolver.</p></article>
          <article class="paso reveal reveal-retraso-1"><h3>Diseño</h3><p>Prototipamos la experiencia y definimos la arquitectura de la solución.</p></article>
          <article class="paso reveal reveal-retraso-2"><h3>Construcción</h3><p>Desarrollamos por iteraciones con revisiones y entregas frecuentes.</p></article>
          <article class="paso reveal reveal-retraso-3"><h3>Lanzamiento</h3><p>Desplegamos, medimos resultados y acompañamos la evolución del producto.</p></article>
        </div>
      </div>
    </section>

    <section class="section section-soft">
      <div class="container">
        <div class="grid-2">
          <div class="reveal">
            <span class="eyebrow">Datos en tiempo real</span>
            <h2>El clima de Bucaramanga, integrado desde una API pública.</h2>
            <p>En NODO creamos interfaces que conversan con el mundo. Este widget consume la API abierta <strong>Open-Meteo</strong> y muestra las condiciones actuales de nuestra ciudad usando JavaScript y JSON.</p>
            <ul class="lista-features">
              <li><svg class="icono"><use href="#i-check"></use></svg> Consulta en vivo sin claves de acceso.</li>
              <li><svg class="icono"><use href="#i-check"></use></svg> Manejo de errores y estado de respaldo.</li>
              <li><svg class="icono"><use href="#i-check"></use></svg> Interfaz responsiva para cualquier dispositivo.</li>
            </ul>
          </div>
          <div class="reveal reveal-retraso-1">
            <div id="clima-widget" class="clima-wrap" aria-live="polite">
              <div class="clima-main"><div class="clima-temp">--°</div><div><div class="clima-desc">Consultando datos…</div><div class="clima-lugar">Bucaramanga, Santander</div></div></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-light">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow">Portafolio</span>
          <h2>Proyectos que ya están generando valor</h2>
          <p>Una muestra de cómo aplicamos tecnología a retos concretos de empresas de la región.</p>
        </div>
        <div class="grid-3">
          <article class="proyecto-card reveal">
            <img src="assets/img/diseno.webp" alt="Diseño de interfaz para proyecto de comercio digital" loading="lazy" width="900" height="600">
            <div class="proyecto-info"><span>E-Commerce</span><h3>Planeta Digital</h3></div>
          </article>
          <article class="proyecto-card reveal reveal-retraso-1">
            <img src="assets/img/analitica.webp" alt="Tablero de analítica de datos" loading="lazy" width="900" height="600">
            <div class="proyecto-info"><span>Analítica</span><h3>Reportes Clínica Andina</h3></div>
          </article>
          <article class="proyecto-card reveal reveal-retraso-2">
            <img src="assets/img/circuito.webp" alt="Componentes electrónicos de solución IoT" loading="lazy" width="900" height="600">
            <div class="proyecto-info"><span>IoT</span><h3>Santander Conectado</h3></div>
          </article>
        </div>
      </div>
    </section>

    <section class="section section-soft">
      <div class="container">
        <div class="section-head centrado reveal">
          <span class="eyebrow">Testimonios</span>
          <h2>La confianza se construye con resultados</h2>
        </div>
        <div class="grid-3">
          <blockquote class="testimonio reveal">
            <div class="estrellas" aria-label="5 de 5 estrellas">★★★★★</div>
            <p>Entendieron nuestro negocio desde el primer día. La plataforma quedó lista antes de lo previsto y el equipo la usa sin capacitación adicional.</p>
            <footer class="autor"><span class="avatar">LM</span><span><strong>Laura Mendoza</strong><small>Gerente comercial · distribuidora regional</small></span></footer>
          </blockquote>
          <blockquote class="testimonio reveal reveal-retraso-1">
            <div class="estrellas" aria-label="5 de 5 estrellas">★★★★★</div>
            <p>Por fin tenemos un tablero que muestra la operación en tiempo real. Tomamos decisiones en minutos en lugar de esperar reportes manuales.</p>
            <footer class="autor"><span class="avatar">JC</span><span><strong>Javier Cárdenas</strong><small>Operaciones · empresa de logística</small></span></footer>
          </blockquote>
          <blockquote class="testimonio reveal reveal-retraso-2">
            <div class="estrellas" aria-label="5 de 5 estrellas">★★★★★</div>
            <p>La atención es cercana y técnica a la vez. Cada entrega viene documentada, algo que valoramos mucho en nuestro equipo de sistemas.</p>
            <footer class="autor"><span class="avatar">PR</span><span><strong>Paula Rodríguez</strong><small>Líder de tecnología · clínica regional</small></span></footer>
          </blockquote>
        </div>
      </div>
    </section>
""" + CTA + """
  </main>
"""

# ==========================================================================
# PÁGINA: SERVICIOS
# ==========================================================================
SERVICIOS = """
  <main id="contenido">
    <section class="page-hero">
      <div class="container">
        <nav class="migas" aria-label="Ruta de navegación">
          <a href="index.html">Inicio</a><svg class="icono"><use href="#i-chevron-right"></use></svg><span>Servicios</span>
        </nav>
        <h1>Soluciones tecnológicas para tu negocio</h1>
        <p>Construimos herramientas digitales que resuelven problemas reales: desde una página web hasta una arquitectura de datos completa.</p>
      </div>
    </section>

    <div class="container contenido-interior">
      <section class="section" style="padding-top:20px">
        <div class="section-head reveal">
          <span class="eyebrow">Catálogo dinámico</span>
          <h2>Nuestros servicios</h2>
          <p>La información de esta sección se carga dinámicamente desde un archivo JSON y se renderiza con JavaScript orientado a objetos.</p>
        </div>

        <div class="filter-bar reveal" role="group" aria-label="Filtrar servicios por categoría">
          <button type="button" class="filter-btn activo" data-filtro="todos">Todos</button>
          <button type="button" class="filter-btn" data-filtro="Desarrollo">Desarrollo</button>
          <button type="button" class="filter-btn" data-filtro="Datos">Datos e IA</button>
          <button type="button" class="filter-btn" data-filtro="Infraestructura">Infraestructura</button>
        </div>

        <div id="servicios-grid" aria-live="polite">
          <div class="card-nodo"><p>Cargando catálogo desde JSON…</p></div>
        </div>
      </section>
    </div>

    <section class="section section-light">
      <div class="container">
        <div class="section-head centrado reveal">
          <span class="eyebrow">Estándar de calidad</span>
          <h2>Cada proyecto incluye</h2>
        </div>
        <ul class="incluye-lista">
          <li class="reveal"><svg class="icono"><use href="#i-check"></use></svg> Diseño responsivo probado en móvil, tablet y escritorio.</li>
          <li class="reveal"><svg class="icono"><use href="#i-check"></use></svg> Código semántico, documentado y versionado.</li>
          <li class="reveal"><svg class="icono"><use href="#i-check"></use></svg> Formularios validados y manejo de errores.</li>
          <li class="reveal"><svg class="icono"><use href="#i-check"></use></svg> Integración con APIs y datos en formato JSON.</li>
          <li class="reveal"><svg class="icono"><use href="#i-check"></use></svg> Despliegue en hosting y URL pública funcional.</li>
          <li class="reveal"><svg class="icono"><use href="#i-check"></use></svg> Capacitación breve para tu equipo.</li>
        </ul>
      </div>
    </section>

    <section class="section section-soft">
      <div class="container">
        <div class="section-head centrado reveal">
          <span class="eyebrow">Planes</span>
          <h2>Elige el punto de partida</h2>
          <p>Precios de referencia en pesos colombianos. Cada propuesta se ajusta al alcance real del proyecto.</p>
        </div>
        <div class="planes-grid">
          <article class="plan-card reveal">
            <h3>Lanzamiento</h3>
            <p class="text-muted small">Para validar una idea o presencia digital.</p>
            <div class="precio">$1.8M <small>/ proyecto</small></div>
            <ul>
              <li><svg class="icono"><use href="#i-check"></use></svg> Sitio web de hasta 5 secciones</li>
              <li><svg class="icono"><use href="#i-check"></use></svg> Diseño responsivo</li>
              <li><svg class="icono"><use href="#i-check"></use></svg> Formulario de contacto</li>
              <li><svg class="icono"><use href="#i-check"></use></svg> Publicación en hosting</li>
            </ul>
            <a class="btn-ghost w-100" href="contacto.html">Solicitar propuesta</a>
          </article>
          <article class="plan-card destacado-plan reveal reveal-retraso-1">
            <span class="plan-tag">Más elegido</span>
            <h3>Crecimiento</h3>
            <p class="text-muted small">Para empresas que necesitan operar mejor.</p>
            <div class="precio">$4.5M <small>/ proyecto</small></div>
            <ul>
              <li><svg class="icono"><use href="#i-check"></use></svg> Todo lo de Lanzamiento</li>
              <li><svg class="icono"><use href="#i-check"></use></svg> Dashboard con datos en vivo</li>
              <li><svg class="icono"><use href="#i-check"></use></svg> Integración con APIs</li>
              <li><svg class="icono"><use href="#i-check"></use></svg> 30 días de soporte</li>
            </ul>
            <a class="btn-nodo w-100" href="contacto.html">Solicitar propuesta</a>
          </article>
          <article class="plan-card reveal reveal-retraso-2">
            <h3>Escala</h3>
            <p class="text-muted small">Para operaciones críticas y continuas.</p>
            <div class="precio">$2.9M <small>/ mes</small></div>
            <ul>
              <li><svg class="icono"><use href="#i-check"></use></svg> Desarrollo dedicado por sprints</li>
              <li><svg class="icono"><use href="#i-check"></use></svg> Infraestructura cloud monitorizada</li>
              <li><svg class="icono"><use href="#i-check"></use></svg> SLA y soporte prioritario</li>
              <li><svg class="icono"><use href="#i-check"></use></svg> Revisión de seguridad mensual</li>
            </ul>
            <a class="btn-ghost w-100" href="contacto.html">Hablar con el equipo</a>
          </article>
        </div>
      </div>
    </section>
""" + CTA + """
  </main>
"""

# ==========================================================================
# PÁGINA: CONTACTO
# ==========================================================================
CONTACTO = """
  <main id="contenido">
    <section class="page-hero">
      <div class="container">
        <nav class="migas" aria-label="Ruta de navegación">
          <a href="index.html">Inicio</a><svg class="icono"><use href="#i-chevron-right"></use></svg><span>Contacto</span>
        </nav>
        <h1>Hablemos de tu próximo proyecto</h1>
        <p>Completa el formulario con tus datos. Nos pondremos en contacto contigo en un plazo máximo de 24 horas hábiles.</p>
      </div>
    </section>

    <div class="container contenido-interior">
      <section class="section" style="padding-top:20px">
        <div class="row g-4">
          <div class="col-lg-7">
            <div id="alerta-formulario" role="status" aria-live="polite"></div>
            <form id="contacto-form" class="form-nodo" novalidate>
              <div class="row g-3">
                <div class="col-md-6">
                  <div class="form-field">
                    <label for="nombre">Nombre completo <span class="obligatorio">*</span></label>
                    <input class="form-control-nodo" type="text" id="nombre" name="nombre" placeholder="Ej. María Rodríguez" autocomplete="name">
                    <small class="mensaje-campo"></small>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-field">
                    <label for="email">Correo electrónico <span class="obligatorio">*</span></label>
                    <input class="form-control-nodo" type="email" id="email" name="email" placeholder="nombre@empresa.com" autocomplete="email">
                    <small class="mensaje-campo"></small>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-field">
                    <label for="telefono">Teléfono <span class="obligatorio">*</span></label>
                    <input class="form-control-nodo" type="tel" id="telefono" name="telefono" placeholder="+57 300 123 4567" autocomplete="tel">
                    <small class="mensaje-campo"></small>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-field">
                    <label for="empresa">Empresa (opcional)</label>
                    <input class="form-control-nodo" type="text" id="empresa" name="empresa" placeholder="Nombre de tu organización" autocomplete="organization">
                    <small class="mensaje-campo"></small>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-field">
                    <label for="tipo">Tipo de solicitud <span class="obligatorio">*</span></label>
                    <select class="form-select-nodo" id="tipo" name="tipo">
                      <option value="">Selecciona una opción</option>
                      <option value="desarrollo-web">Desarrollo web</option>
                      <option value="apps-moviles">Aplicaciones móviles</option>
                      <option value="inteligencia-datos">Datos e inteligencia</option>
                      <option value="automatizacion">Automatización e IoT</option>
                      <option value="cloud-devops">Cloud y DevOps</option>
                      <option value="soporte-seguridad">Soporte y seguridad</option>
                      <option value="otro">Otro</option>
                    </select>
                    <small class="mensaje-campo"></small>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-field">
                    <label for="asunto">Asunto <span class="obligatorio">*</span></label>
                    <input class="form-control-nodo" type="text" id="asunto" name="asunto" placeholder="¿En qué podemos ayudarte?">
                    <small class="mensaje-campo"></small>
                  </div>
                </div>
                <div class="col-12">
                  <div class="form-field">
                    <label for="mensaje">Mensaje <span class="obligatorio">*</span></label>
                    <textarea class="form-control-nodo" id="mensaje" name="mensaje" placeholder="Cuéntanos sobre tu idea, tus necesidades y el resultado que esperas (mínimo 20 caracteres)."></textarea>
                    <small class="mensaje-campo"></small>
                  </div>
                </div>
                <div class="col-12">
                  <div class="form-field">
                    <label for="archivo">Adjuntar archivo (opcional)</label>
                    <input class="form-control-nodo" type="file" id="archivo" name="archivo" accept=".pdf,.png,.jpg,.jpeg,.webp" aria-describedby="archivo-ayuda">
                    <div id="archivo-ayuda" class="archivo-preview"><svg class="icono"><use href="#i-file"></use></svg><span></span></div>
                    <small class="mensaje-campo"></small>
                    <small class="text-muted d-block mt-1" style="font-size:.75rem">PDF, PNG, JPG o WEBP · máximo 5 MB</small>
                  </div>
                </div>
                <div class="col-12">
                  <div class="form-check-nodo">
                    <input type="checkbox" id="terminos" name="terminos">
                    <div>
                      <label for="terminos">Acepto el tratamiento de mis datos personales para ser contactado por NODO. <span class="obligatorio">*</span></label>
                      <small class="mensaje-campo"></small>
                    </div>
                  </div>
                  <div class="form-check-nodo">
                    <input type="checkbox" id="novedades" name="novedades">
                    <label for="novedades">Quiero recibir novedades y consejos tecnológicos por correo.</label>
                  </div>
                </div>
              </div>
              <div class="d-flex flex-wrap gap-2 mt-3">
                <button class="btn-nodo" type="submit"><svg class="icono"><use href="#i-send"></use></svg> Enviar solicitud</button>
                <button class="btn-ghost" type="button" id="limpiar-form">Limpiar formulario</button>
              </div>
              <p class="contador-local">Solicitudes guardadas en este navegador: <strong id="contador-solicitudes">0</strong> (almacenamiento JSON en localStorage)</p>
            </form>
          </div>

          <div class="col-lg-5">
            <h2 class="h4 mb-4">Datos de contacto</h2>
            <div class="contact-card reveal">
              <div class="icono-caja"><svg class="icono"><use href="#i-pin"></use></svg></div>
              <div><h3>Ubicación</h3><p data-config="direccion">Cra. 15 # 36-24, Centro, Bucaramanga</p><p data-config="ubicacion">Bucaramanga, Santander, Colombia</p></div>
            </div>
            <div class="contact-card reveal reveal-retraso-1">
              <div class="icono-caja"><svg class="icono"><use href="#i-mail"></use></svg></div>
              <div><h3>Correo</h3><p><a data-config="email" href="mailto:hola@nodotecnologia.co">hola@nodotecnologia.co</a></p></div>
            </div>
            <div class="contact-card reveal reveal-retraso-2">
              <div class="icono-caja"><svg class="icono"><use href="#i-phone"></use></svg></div>
              <div><h3>Teléfono y WhatsApp</h3><p><a data-config="telefono" href="tel:+576124820">+57 7 612 4820</a></p><p><a data-config="whatsapp" href="#">+57 300 555 0142</a></p></div>
            </div>
            <div class="contact-card reveal">
              <div class="icono-caja"><svg class="icono"><use href="#i-clock"></use></svg></div>
              <div><h3>Horario de atención</h3><p data-config="horario">Lunes a viernes, 8:00 a. m. — 6:00 p. m.</p></div>
            </div>
            <iframe class="mapa mt-4 reveal" title="Mapa de ubicación de NODO en Bucaramanga"
              src="https://www.openstreetmap.org/export/embed.html?bbox=-73.1350%2C7.1090%2C-73.1100%2C7.1300&amp;layer=mapnik&amp;marker=7.1193%2C-73.1227"
              loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            <p class="small text-muted mt-2"><a href="https://www.openstreetmap.org/?mlat=7.1193&amp;mlon=-73.1227#map=15/7.1193/-73.1227" target="_blank" rel="noopener">Abrir mapa en OpenStreetMap</a></p>
          </div>
        </div>
      </section>
    </div>
""" + CTA + """
  </main>
"""

# ==========================================================================
# PÁGINA: MULTIMEDIA
# ==========================================================================
MULTIMEDIA = """
  <main id="contenido">
    <section class="page-hero">
      <div class="container">
        <nav class="migas" aria-label="Ruta de navegación">
          <a href="index.html">Inicio</a><svg class="icono"><use href="#i-chevron-right"></use></svg><span>Multimedia</span>
        </nav>
        <h1>Multimedia</h1>
        <p>Conoce el detrás de cámaras de NODO: nuestro equipo, nuestra forma de trabajar y el video institucional del proyecto.</p>
      </div>
    </section>

    <div class="container contenido-interior">
      <section class="section" style="padding-top:20px">
        <div class="video-seccion reveal">
          <div class="row align-items-center mb-4">
            <div class="col-lg-8">
              <span class="eyebrow">Video institucional</span>
              <h2>NODO en 15 segundos</h2>
            </div>
            <div class="col-lg-4 text-lg-end">
              <span class="badge rounded-pill" style="background:rgba(255,255,255,.12);color:#fff">MP4 · 1280 × 720 · optimizado</span>
            </div>
          </div>

          <div class="video-marco">
            <video id="video-nodo" poster="assets/img/video-poster.webp" preload="metadata" playsinline>
              <source src="assets/video/nodo-startup.mp4" type="video/mp4">
              <track kind="captions" src="assets/video/nodo-es.vtt" srclang="es" label="Español" default>
              Tu navegador no admite el elemento video. Puedes <a href="assets/video/nodo-startup.mp4">descargar el video</a>.
            </video>
            <div id="video-overlay" class="video-overlay" role="button" tabindex="0" aria-label="Reproducir video institucional">
              <div class="boton-play"><svg class="icono"><use href="#i-play"></use></svg></div>
            </div>
          </div>

          <div class="video-controles">
            <button id="btn-play-video" type="button">Reproducir video</button>
            <div class="barra-progreso" title="Progreso del video"><span id="barra-progreso"></span></div>
            <button id="btn-sonido" type="button"><svg class="icono"><use href="#i-x"></use></svg> Activar sonido</button>
          </div>

          <div class="media-nota">
            <svg class="icono"><use href="#i-bolt"></use></svg>
            <p><strong>Recurso optimizado:</strong> video H.264 con carga diferida y subtítulos WebVTT en español. La imagen de portada y las fotografías se sirven en formato WebP.</p>
          </div>
        </div>
      </section>

      <section class="section section-light">
        <div class="container">
          <div class="section-head reveal">
            <span class="eyebrow">Galería</span>
            <h2>Momentos de nuestro equipo</h2>
            <p>Imágenes optimizadas con atributos <code>loading="lazy"</code>, dimensiones explícitas y efectos con pseudoelementos <code>::before</code> y <code>::after</code>.</p>
          </div>
          <div class="galeria-grid">
            <button class="galeria-item reveal" type="button" data-galeria
              data-titulo="Trabajo colaborativo"
              data-descripcion="Sesión de planeación del equipo NODO en Bucaramanga.">
              <img src="assets/img/equipo.webp" alt="Equipo colaborando alrededor de una mesa" loading="lazy" width="900" height="675">
              <span class="zoom-signo"><svg class="icono"><use href="#i-zoom"></use></svg></span>
            </button>
            <button class="galeria-item reveal reveal-retraso-1" type="button" data-galeria
              data-titulo="Código en acción"
              data-descripcion="Desarrollo de soluciones web con JavaScript orientado a objetos.">
              <img src="assets/img/codigo.webp" alt="Pantalla con código fuente" loading="lazy" width="900" height="675">
              <span class="zoom-signo"><svg class="icono"><use href="#i-zoom"></use></svg></span>
            </button>
            <button class="galeria-item reveal reveal-retraso-2" type="button" data-galeria
              data-titulo="Datos que hablan"
              data-descripcion="Construcción de tableros de analítica para clientes de la región.">
              <img src="assets/img/analitica.webp" alt="Tablero de analítica de datos" loading="lazy" width="900" height="675">
              <span class="zoom-signo"><svg class="icono"><use href="#i-zoom"></use></svg></span>
            </button>
            <button class="galeria-item reveal" type="button" data-galeria
              data-titulo="Infraestructura confiable"
              data-descripcion="Monitoreo y operación de servicios en la nube.">
              <img src="assets/img/servidores.webp" alt="Servidores en centro de datos" loading="lazy" width="900" height="675">
              <span class="zoom-signo"><svg class="icono"><use href="#i-zoom"></use></svg></span>
            </button>
            <button class="galeria-item reveal reveal-retraso-1" type="button" data-galeria
              data-titulo="Automatización e IoT"
              data-descripcion="Prototipos conectados que mejoran procesos productivos.">
              <img src="assets/img/circuito.webp" alt="Circuito electrónico" loading="lazy" width="900" height="675">
              <span class="zoom-signo"><svg class="icono"><use href="#i-zoom"></use></svg></span>
            </button>
            <button class="galeria-item reveal reveal-retraso-2" type="button" data-galeria
              data-titulo="Diseño con intención"
              data-descripcion="Cada interfaz se prueba en móvil, tablet y escritorio.">
              <img src="assets/img/diseno.webp" alt="Espacio de trabajo de diseño" loading="lazy" width="900" height="675">
              <span class="zoom-signo"><svg class="icono"><use href="#i-zoom"></use></svg></span>
            </button>
          </div>
        </div>
      </section>
""" + CTA + """
  </main>
"""


def layout(titulo, descripcion, pagina, active, contenido):
    html = (HEAD + NAV + contenido + FOOTER)
    reemplazos = {
        "__TITLE__": titulo,
        "__DESCRIPTION__": descripcion,
        "__PAGE__": pagina,
        "__SPRITE__": simbolos,
        "__A_INICIO__": "active" if active == "inicio" else "",
        "__A_NOSOTROS__": "active" if active == "nosotros" else "",
        "__A_SERVICIOS__": "active" if active == "servicios" else "",
        "__A_MULTIMEDIA__": "active" if active == "multimedia" else "",
        "__A_CONTACTO__": "active" if active == "contacto" else "",
    }
    for clave, valor in reemplazos.items():
        html = html.replace(clave, valor)
    return html

PAGINAS = {
    "index.html": layout(
        "NODO | Startup tecnológica de Bucaramanga",
        "NODO es una startup tecnológica de Bucaramanga especializada en desarrollo web, analítica de datos, automatización e infraestructura cloud.",
        "inicio", "inicio", INDEX),
    "servicios.html": layout(
        "Servicios | NODO Tecnología Bucaramanga",
        "Conoce los servicios tecnológicos de NODO: desarrollo web, aplicaciones móviles, analítica de datos, IoT, cloud y soporte.",
        "servicios", "servicios", SERVICIOS),
    "contacto.html": layout(
        "Contacto | NODO Tecnología Bucaramanga",
        "Contacta con NODO, startup tecnológica en Bucaramanga. Cuéntanos tu proyecto y te responderemos en 24 horas hábiles.",
        "contacto", "contacto", CONTACTO),
    "multimedia.html": layout(
        "Multimedia | NODO Tecnología Bucaramanga",
        "Video institucional y galería multimedia de NODO, startup tecnológica de Bucaramanga.",
        "multimedia", "multimedia", MULTIMEDIA),
}

for nombre, contenido in PAGINAS.items():
    (BASE / nombre).write_text(contenido, encoding="utf-8")
    print("Generado:", nombre, f"{len(contenido):,} chars")
