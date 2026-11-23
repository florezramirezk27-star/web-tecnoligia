/* ==========================================================================
   NODO · Inicialización general (jQuery + clases)
   ========================================================================== */
(function ($, window, document) {
  'use strict';

  $(function () {
    const pagina = document.body.dataset.page || 'inicio';

    /* Configuración JSON -> DOM (POO + JSON + manipulación) */
    new Configuracion('assets/data/empresa.json').cargar();

    /* Animaciones reveal */
    new RevealOnScroll().iniciar();

    /* Cabecera que cambia al desplazarse y botón volver arriba */
    $(window).on('scroll', function () {
      const scroll = $(this).scrollTop();
      $('.site-header').toggleClass('is-scrolled', scroll > 40);
      $('#back-to-top').toggleClass('visible', scroll > 500);
    });

    $('#back-to-top').on('click', function () {
      $('html, body').animate({ scrollTop: 0 }, 500);
    });

    /* Cierre del menú responsive y resaltado del enlace activo */
    $('.navbar-collapse .nav-link').on('click', function () {
      $('.navbar-collapse').removeClass('show');
    });

    const archivo = window.location.pathname.split('/').pop() || 'index.html';
    $('.navbar-collapse .nav-link').each(function () {
      const destino = $(this).attr('href');
      if (destino === archivo || (archivo === '' && destino === 'index.html')) {
        $(this).addClass('active').attr('aria-current', 'page');
      }
    });

    /* Desplazamiento suave con compensación de la cabecera fija */
    $('a[href^="#"]').not('[data-bs-toggle]').on('click', function (evento) {
      const id = $(this).attr('href');
      if (id.length <= 1) return;
      const destino = $(id);
      if (!destino.length) return;
      evento.preventDefault();
      $('html, body').animate({ scrollTop: destino.offset().top - 72 }, 550);
    });

    /* Carrusel: pausa al pasar el mouse (mejora de usabilidad) */
    const carrusel = document.getElementById('heroCarousel');
    if (carrusel && window.bootstrap) {
      const instancia = bootstrap.Carousel.getOrCreateInstance(carrusel, { interval: 6500, ride: 'carousel' });
      carrusel.addEventListener('mouseenter', () => instancia.pause());
      carrusel.addEventListener('mouseleave', () => instancia.cycle());
    }

    /* ---- Funcionalidad específica por página ---- */
    switch (pagina) {
      case 'inicio':
        new CatalogoServicios('#servicios-destacados', 'assets/data/servicios.json', { limite: 3 }).cargar();
        new ClimaService('#clima-widget', 7.1193, -73.1227).obtener();
        break;

      case 'servicios': {
        const catalogo = new CatalogoServicios('#servicios-grid', 'assets/data/servicios.json');
        catalogo.vincularFiltros();
        catalogo.cargar();
        break;
      }

      case 'contacto':
        new ValidadorFormulario('#contacto-form').iniciar();
        break;

      case 'multimedia':
        new Galeria('[data-galeria]').iniciar();
        new ReproductorVideo('video-nodo').iniciar();
        break;
    }
  });
})(jQuery, window, document);
