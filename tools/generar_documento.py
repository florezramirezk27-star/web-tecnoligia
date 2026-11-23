"""Genera el Documento Técnico PDF (norma IEEE) del proyecto NODO.
Uso: python tools/generar_documento.py
"""
import pathlib
from fpdf import FPDF

BASE = pathlib.Path(__file__).resolve().parents[1]
SALIDA = BASE / "docs" / "Documento_Tecnico_IEEE_NODO.pdf"
EVID = BASE / "docs" / "evidencia"

AZUL = (11, 18, 32)
PRIMARIO = (91, 75, 255)
VERDE = (0, 150, 130)
GRIS = (90, 100, 115)
CLARO = (238, 241, 248)


def limpio(texto):
    reemplazos = {
        "—": "-", "–": "-", "→": "->", "“": '"', "”": '"',
        "’": "'", "·": ".", "…": "...", "✓": "x", "°": " grados",
    }
    for a, b in reemplazos.items():
        texto = texto.replace(a, b)
    return texto.encode("latin-1", "replace").decode("latin-1")


class DocumentoIEEE(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=True, margin=20)
        self.set_margins(20, 20, 20)
        self.set_title("Documento Tecnico - Portal NODO")
        self.set_author("Grupo B191 - Diseno Web Avanzado - UTS")
        self.set_subject("Proyecto final integrador 30% corte 3")

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Times", "", 8.5)
        self.set_text_color(*GRIS)
        self.cell(120, 5, limpio("Proyecto Final Integrador - Portal Web NODO"), align="L")
        self.cell(0, 5, limpio("UTS - B191"), align="R")
        self.ln(6)
        self.set_draw_color(210, 214, 225)
        self.line(20, self.get_y(), 190, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-14)
        self.set_font("Times", "I", 9)
        self.set_text_color(*GRIS)
        self.cell(0, 8, f"Pagina {self.page_no()}", align="C")

    # ---- helpers ----
    def titulo1(self, texto):
        self.ln(2)
        self.set_font("Times", "B", 14)
        self.set_text_color(*AZUL)
        self.multi_cell(0, 7, limpio(texto))
        self.set_draw_color(*PRIMARIO)
        self.set_line_width(0.6)
        y = self.get_y()
        self.line(20, y, 190, y)
        self.ln(4)

    def titulo2(self, texto):
        self.ln(2)
        self.set_font("Times", "B", 11.5)
        self.set_text_color(*PRIMARIO)
        self.multi_cell(0, 6, limpio(texto))
        self.ln(1)

    def parrafo(self, texto, justificado=True):
        self.set_font("Times", "", 11)
        self.set_text_color(35, 40, 50)
        self.multi_cell(0, 5.8, limpio(texto), align="J" if justificado else "L")
        self.ln(2)

    def lista(self, elementos):
        self.set_font("Times", "", 11)
        self.set_text_color(35, 40, 50)
        for elemento in elementos:
            self.set_x(20)
            self.cell(6, 5.8, "")
            self.multi_cell(164, 5.8, limpio("- " + elemento))
        self.ln(2)

    def codigo(self, texto):
        self.set_font("Courier", "", 8)
        self.set_fill_color(245, 246, 250)
        self.set_text_color(40, 45, 60)
        self.multi_cell(0, 4.2, limpio(texto), fill=True)
        self.ln(3)

    def tabla(self, cabeceras, filas, anchos):
        self.set_font("Times", "B", 9.5)
        self.set_fill_color(*PRIMARIO)
        self.set_text_color(255, 255, 255)
        for cab, ancho in zip(cabeceras, anchos):
            self.cell(ancho, 8, limpio(cab), border=1, align="C", fill=True)
        self.ln()
        self.set_font("Times", "", 9.5)
        self.set_text_color(35, 40, 50)
        for i, fila in enumerate(filas):
            if i % 2 == 0:
                self.set_fill_color(244, 246, 251)
            else:
                self.set_fill_color(255, 255, 255)
            for valor, ancho in zip(fila, anchos):
                self.cell(ancho, 7.5, limpio(str(valor)), border=1, fill=True)
            self.ln()
        self.ln(3)

    def nota(self, texto):
        self.set_fill_color(232, 250, 246)
        self.set_text_color(5, 105, 90)
        self.set_font("Times", "I", 10)
        self.multi_cell(0, 5.5, limpio(texto), fill=True)
        self.ln(3)

    def imagen(self, nombre, ancho, titulo):
        ruta = EVID / nombre
        if not ruta.exists():
            return
        from PIL import Image
        with Image.open(ruta) as img:
            alto = ancho * img.height / img.width
        if self.get_y() + alto + 12 > 270:
            self.add_page()
        x = (210 - ancho) / 2
        self.image(str(ruta), x=x, w=ancho)
        self.set_font("Times", "I", 9)
        self.set_text_color(*GRIS)
        self.cell(0, 5, limpio(titulo), align="C")
        self.ln(8)


doc = DocumentoIEEE()

# ============================ PORTADA ============================
doc.add_page()
doc.ln(12)
doc.set_font("Times", "B", 12)
doc.set_text_color(*PRIMARIO)
doc.cell(0, 7, limpio("UNIVERSITARIA TECNOLOGICA DE SANTANDER"), align="C")
doc.ln(12)
doc.set_font("Times", "B", 22)
doc.set_text_color(*AZUL)
doc.multi_cell(0, 10, limpio("DOCUMENTO TECNICO DEL PROYECTO"), align="C")
doc.ln(3)
doc.set_font("Times", "B", 17)
doc.set_text_color(*PRIMARIO)
doc.multi_cell(0, 9, limpio("Portal Web Interactivo para el Sector\nProductivo de Bucaramanga"), align="C")
doc.ln(4)
doc.set_font("Times", "I", 13)
doc.set_text_color(*GRIS)
doc.multi_cell(0, 7, limpio("Caso: NODO - Startup tecnologica bumanguesa"), align="C")
doc.ln(14)

doc.set_font("Times", "", 11)
doc.set_text_color(35, 40, 50)
datos = [
    ("Asignatura", "Diseno Web Avanzado"),
    ("Grupo", "B191"),
    ("Programa", "Tecnologia en Desarrollo de Sistemas Informaticos"),
    ("Docente", "Gustavo Paramio"),
    ("Periodo", "Corte 3 - Proyecto final integrador (30%)"),
    ("Fecha de entrega", "30 de noviembre de 2026"),
]
for etiqueta, valor in datos:
    doc.set_font("Times", "B", 11)
    doc.cell(45, 7, limpio(etiqueta + ":"))
    doc.set_font("Times", "", 11)
    doc.cell(0, 7, limpio(valor))
    doc.ln()

doc.ln(9)
doc.set_font("Times", "B", 12)
doc.set_text_color(*AZUL)
doc.cell(0, 7, limpio("INTEGRANTES DEL GRUPO"), align="C")
doc.ln(9)
integrantes = [
    "1. Dayron Camilo Diaz",
    "2. Santiago Alejandro Figueroa",
    "3. Andres Felipe Contreras Rodriguez",
    "4. Kevin Andrey Florez Ramirez",
]
doc.set_font("Times", "", 11)
for integrante in integrantes:
    doc.cell(0, 7, limpio(integrante), align="C")
    doc.ln()

doc.ln(12)
doc.set_font("Times", "I", 10)
doc.set_text_color(*GRIS)
doc.multi_cell(0, 5.5, limpio("Entregable: Documento Tecnico bajo norma IEEE. El portal es un proyecto academico con marca y datos de contacto ficticios, construido con criterios de realismo profesional."), align="C")

# ============================ CONTENIDO ============================
doc.add_page()
doc.titulo1("1. Introduccion")
doc.parrafo("El presente documento describe el diseno, desarrollo y despliegue de NODO, un portal web interactivo orientado al subsector tecnologico de Bucaramanga. El proyecto se enmarca en la actividad 'Portal Web Interactivo para el Sector Productivo de Bucaramanga' y cumple con los requerimientos de HTML5 semantico, multimedia optimizada, formularios validados, programacion orientada a objetos, consumo de API publica, uso de JSON y publicacion en hosting gratuito.")
doc.parrafo("NODO se presenta como una startup local dedicada al desarrollo web, la analitica de datos, la automatizacion y la infraestructura cloud. La marca, los datos de contacto y los proyectos del portafolio son ficticios y se usan con fines demostrativos, manteniendo un enfoque realista y coherente con la realidad economica de Santander.")

doc.titulo1("2. Integrantes del grupo")
doc.tabla(["#", "Nombre completo", "Rol principal en el proyecto"], [
    ["1", "Dayron Camilo Diaz", "Arquitectura y desarrollo frontend"],
    ["2", "Santiago Alejandro Figueroa", "Diseno visual, maquetacion y multimedia"],
    ["3", "Andres Felipe Contreras Rodriguez", "Logica JavaScript, API y formularios"],
    ["4", "Kevin Andrey Florez Ramirez", "Documentacion, pruebas y despliegue"],
], [12, 68, 90])

doc.titulo1("3. Sector productivo seleccionado")
doc.titulo2("3.1 Caso de aplicacion")
doc.parrafo("Sector seleccionado: tecnologia. Caso de aplicacion: portal web para una startup tecnologica bumanguesa. El tema es diferente a los casos de gastronomia, turismo, salud, educacion, calzado, moda, cafe, hoteleria, transporte, deportes, cultura, agricultura, veterinaria, comercio y bienestar, evitando la repeticion de tematicas entre grupos.")
doc.titulo2("3.2 Justificacion")
doc.parrafo("Bucaramanga cuenta con un ecosistema creciente de empresas de software, servicios digitales y emprendimientos tecnologicos. Un portal para una startup permite demostrar de forma natural todos los requerimientos tecnicos: catalogo dinamico, integracion con APIs, paneles de datos, formularios avanzados y multimedia, sin forzar los contenidos.")

doc.titulo1("4. Objetivo del sitio")
doc.titulo2("4.1 Objetivo general")
doc.parrafo("Desarrollar un portal web avanzado, adaptable e interactivo orientado al subsector tecnologico de Bucaramanga, aplicando tecnologias modernas de diseno y desarrollo web y publicandolo en una URL publica funcional.")
doc.titulo2("4.2 Objetivos especificos")
doc.lista([
    "Implementar HTML5 semantico para estructurar correctamente el contenido.",
    "Integrar multimedia optimizada para distintos dispositivos.",
    "Disenar formularios interactivos con validaciones.",
    "Utilizar JavaScript, jQuery y manipulacion del DOM.",
    "Implementar programacion orientada a objetos con JavaScript.",
    "Aplicar Responsive Web Design mediante Flexbox, Grid y Media Queries.",
    "Utilizar el framework CSS Bootstrap 5.3.3.",
    "Consumir la API publica Open-Meteo para mostrar el clima de Bucaramanga.",
    "Utilizar JSON para el intercambio de informacion y el almacenamiento local.",
    "Publicar el proyecto en un hosting gratuito accesible por Internet.",
])

doc.titulo1("5. Mapa de navegacion")
doc.parrafo("El portal esta compuesto por cuatro paginas HTML conectadas por una navegacion responsive comun, con secciones ancladas en la pagina principal y un pie de pagina global.")
doc.codigo(
    "index.html (Inicio)\n"
    " |-- #inicio ......... Banner principal (carrusel adaptable)\n"
    " |-- #nosotros ....... Presentacion del negocio y equipo\n"
    " |-- #servicios ...... Servicios destacados (cargados desde JSON)\n"
    " |-- #proceso ........ Metodologia de trabajo\n"
    " |-- #clima .......... Widget de API publica Open-Meteo\n"
    " |-- #portafolio ..... Proyectos destacados\n"
    " |-- #testimonios .... Testimonios de clientes\n"
    " |\n"
    " +-- servicios.html .. Catalogo dinamico + filtros + planes\n"
    " +-- contacto.html ... Formulario avanzado + datos + mapa OSM\n"
    " +-- multimedia.html . Video institucional + galeria con lightbox\n"
    "\n"
    "pie de pagina comun: navegacion, contacto, integrantes y creditos"
)

doc.titulo1("6. Estructura de carpetas y paginas")
doc.codigo(
    "Portal_NODO_Tecnologia_Bucaramanga/\n"
    "|-- index.html | servicios.html | contacto.html | multimedia.html\n"
    "|-- assets/\n"
    "|   |-- css/ ........ styles.css + vendor/bootstrap.min.css\n"
    "|   |-- js/ ......... classes.js + app.js + vendor/ (jQuery, Bootstrap)\n"
    "|   |-- data/ ....... servicios.json + empresa.json\n"
    "|   |-- img/ ........ fotografias WebP optimizadas\n"
    "|   |-- fonts/ ...... woff2 embebidas (Manrope, Space Grotesk)\n"
    "|   |-- icons/ ...... sprite.svg + favicon.svg (iconos vectoriales)\n"
    "|   `-- video/ ...... nodo-startup.mp4 + nodo-es.vtt\n"
    "|-- docs/ ........... este documento y evidencia responsive\n"
    "`-- tools/ .......... generadores de paginas, video y evidencia"
)
doc.titulo2("6.1 Descripcion de paginas")
doc.tabla(["Pagina", "Contenido principal", "Tecnologia destacada"], [
    ["index.html", "Presentacion, banner, servicios, clima, portafolio", "Carrusel Bootstrap, API, IntersectionObserver"],
    ["servicios.html", "6 servicios, filtros por categoria, planes", "JSON + POO + CSS Grid + jQuery"],
    ["contacto.html", "Formulario con 10 campos, mapa y datos", "Validacion JS/jQuery + localStorage JSON"],
    ["multimedia.html", "Video MP4, subtitulos VTT, galeria", "Pseudoelementos + lightbox + controls"],
], [30, 70, 70])

doc.titulo1("7. Tecnologias utilizadas")
doc.tabla(["Tecnologia", "Uso en el proyecto", "Evidencia"], [
    ["HTML5 semantico", "header, nav, main, section, article, footer, figure", "4 paginas HTML"],
    ["CSS3 / Bootstrap 5.3.3", "Grid, Flexbox, media queries, componentes", "styles.css + vendor"],
    ["JavaScript ES6", "Clases, DOM, eventos, fetch", "classes.js"],
    ["jQuery 3.7.1", "Filtros, animaciones, lightbox, mensajes", "app.js + classes.js"],
    ["JSON", "servicios.json, empresa.json, localStorage", "assets/data/"],
    ["API publica", "Clima actual de Bucaramanga (Open-Meteo)", "ClimaService"],
    ["Fuentes embebidas", "Manrope y Space Grotesk en woff2 local", "assets/fonts/"],
    ["Iconos vectoriales", "Sprite SVG reutilizable en todas las paginas", "assets/icons/"],
    ["Multimedia", "WebP, MP4 H.264, WebVTT", "assets/img, assets/video"],
], [42, 80, 48])

doc.add_page()
doc.titulo1("8. Explicacion tecnica")
doc.titulo2("8.1 DOM (Document Object Model)")
doc.parrafo("El DOM es la representacion en arbol de los elementos HTML. Desde JavaScript se accede a el con document.querySelector / querySelectorAll y se modifica su contenido, estilos y atributos. En el proyecto se usa directamente para inyectar la configuracion de empresa, observar animaciones y actualizar el reproductor de video; con jQuery se usa una capa simplificadora para los filtros y el lightbox.")
doc.codigo(
    "document.querySelectorAll('[data-config]').forEach(elemento => {\n"
    "    elemento.textContent = this.datos[elemento.dataset.config];\n"
    "});"
)
doc.titulo2("8.2 API publica")
doc.parrafo("Se integra la API abierta Open-Meteo (sin clave de acceso) mediante fetch. Se consultan temperatura, humedad, codigo climatico y velocidad del viento para las coordenadas de Bucaramanga (7.1193, -73.1227) en la zona horaria America/Bogota. La clase ClimaService transforma los codigos WMO en texto e iconos y controla el estado de error si la respuesta falla.")
doc.codigo(
    "https://api.open-meteo.com/v1/forecast?latitude=7.1193&longitude=-73.1227\n"
    "  &current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m\n"
    "  &timezone=America%2FBogota"
)
doc.titulo2("8.3 JSON")
doc.parrafo("JSON se emplea en tres niveles: (1) servicios.json alimenta el catalogo de productos/servicios cargado dinamicamente; (2) empresa.json centraliza los datos del negocio y los integrantes, que se inyectan en el DOM; (3) localStorage guarda cada solicitud del formulario como un arreglo de objetos JSON, permitiendo consultar el numero de registros almacenados.")
doc.codigo(
    "// assets/data/servicios.json\n"
    "{\n"
    "  \"id\": \"desarrollo-web\",\n"
    "  \"nombre\": \"Desarrollo web a medida\",\n"
    "  \"categoria\": \"Desarrollo\",\n"
    "  \"etiquetas\": [\"HTML5\", \"JavaScript\"]\n"
    "}"
)
doc.titulo2("8.4 Programacion orientada a objetos (POO)")
doc.parrafo("La logica se organiza en clases ES6 con responsabilidades unicas: Configuracion (datos del sitio), Servicio (modelo de servicio), CatalogoServicios (carga, renderizado y filtros), ClimaService (API), AlmacenamientoContactos (persistencia), ValidadorFormulario (validaciones), Galeria (lightbox), ReproductorVideo (controles) y RevealOnScroll (animaciones). Cada clase expone metodos y encapsula su estado, cumpliendo con el requerimiento de POO.")
doc.codigo(
    "class Servicio {\n"
    "    constructor(datos) { Object.assign(this, datos); }\n"
    "    tarjeta(indice) { return `<article class=\"servicio-card\">...</article>`; }\n"
    "}\n"
    "const catalogo = new CatalogoServicios('#servicios-grid', 'assets/data/servicios.json');\n"
    "catalogo.cargar();"
)

doc.titulo1("9. Formularios y validaciones")
doc.parrafo("El formulario de contacto incluye los tipos de campo exigidos: texto, correo, telefono, select, checkbox, textarea y archivos. Las validaciones se ejecutan al perder el foco y antes del envio, con mensajes dinamicos por campo y un resumen general. El archivo debe ser PDF, PNG, JPG o WEBP y no superar 5 MB.")
doc.tabla(["Campo", "Tipo", "Regla principal"], [
    ["nombre", "text", "Minimo 3 caracteres"],
    ["email", "email", "Formato correo valido"],
    ["telefono", "tel", "7 a 15 digitos"],
    ["empresa", "text", "Opcional, minimo 2 caracteres"],
    ["tipo", "select", "Obligatorio"],
    ["asunto", "text", "Minimo 5 caracteres"],
    ["mensaje", "textarea", "Minimo 20 caracteres"],
    ["archivo", "file", "PDF/PNG/JPG/WEBP, max. 5 MB"],
    ["terminos", "checkbox", "Aceptacion obligatoria"],
    ["novedades", "checkbox", "Suscripcion opcional"],
], [35, 30, 105])

doc.titulo1("10. Diseno responsive y evidencia")
doc.parrafo("Se aplico Responsive Web Design con Bootstrap 5, CSS Grid, Flexbox y media queries explicitas en 1200 px, 992 px, 768 px y 576 px. La navegacion se colapsa en un menu en tablet y movil; las cuadriculas pasan de 3 a 2 y luego a 1 columna; el mockup del hero se oculta en pantallas medianas; y los botones y estadisticas se reorganizan en movil.")
doc.tabla(["Dispositivo", "Ancho de prueba", "Comportamiento verificado"], [
    ["Escritorio", "1440 px", "3 columnas, hero con mockup y carrusel"],
    ["Tablet", "820 px", "Menu colapsado, 2 columnas, sin mockup"],
    ["Movil", "390 px", "1 columna, botones apilados, video adaptable"],
], [38, 32, 100])
doc.imagen("index-desktop.png", 170, "Figura 1. Vista de escritorio (1440 px).")
doc.imagen("index-tablet.png", 120, "Figura 2. Vista de tablet (820 px).")
doc.imagen("index-mobile.png", 85, "Figura 3. Vista de movil (390 px).")
doc.imagen("servicios-desktop.png", 170, "Figura 4. Catalogo dinamico de servicios en escritorio.")
doc.imagen("contacto-mobile.png", 85, "Figura 5. Formulario de contacto en movil.")

doc.add_page()
doc.titulo1("11. Multimedia optimizada")
doc.lista([
    "14 fotografias en formato WebP con anchos adaptados (600-1600 px) y compresion entre q78 y q82.",
    "Atributos loading='lazy' y dimensiones width/height para evitar desplazamientos de layout.",
    "Video institucional MP4 H.264 de 15 segundos, 1280x720, generado a partir de imagenes propias del proyecto.",
    "Subtitulos WebVTT en espanol (nodo-es.vtt) y poster optimizado.",
    "Pseudoelementos ::before y ::after en el marco del video, tarjetas, etiquetas y galeria.",
    "Iconos vectoriales SVG reutilizados mediante un sprite comun.",
])

doc.titulo1("12. Publicacion web")
doc.parrafo("El proyecto queda preparado para publicacion en un hosting gratuito (Netlify, Vercel, GitHub Pages u otro). Todo el codigo, incluidas las librerias y tipografias, esta incluido en la carpeta para que no dependa de CDN externos. El paso final consiste en subir la carpeta y copiar la URL publica en el archivo README.md y en este documento.")
doc.nota("Estado: URL publica pendiente de generar con la cuenta del grupo. El sitio funciona correctamente en servidor local y no se acepta localhost como entrega final, por lo que debe publicarse antes del 30 de noviembre de 2026.")
doc.codigo(
    "# Publicacion sugerida con Netlify Drop\n"
    "1. Comprimir la carpeta Portal_NODO_Tecnologia_Bucaramanga en ZIP.\n"
    "2. Ingresar a https://app.netlify.com/drop e iniciar sesion.\n"
    "3. Arrastrar el ZIP y esperar el despliegue.\n"
    "4. Copiar la URL (https://<sitio>.netlify.app) en README.md."
)

doc.titulo1("13. Cumplimiento de requerimientos")
doc.tabla(["Requerimiento del PDF", "Estado"], [
    ["Grupo de 4 integrantes y tema unico (tecnologia)", "Cumplido"],
    ["HTML5 semantico y multimedia optimizada", "Cumplido"],
    ["Formularios avanzados y validaciones", "Cumplido"],
    ["Diseno responsive (Grid, Flexbox, media queries)", "Cumplido"],
    ["DOM y POO con JavaScript", "Cumplido"],
    ["Integracion API y JSON", "Cumplido"],
    ["Framework CSS (Bootstrap 5.3.3)", "Cumplido"],
    ["jQuery y manipulacion del DOM", "Cumplido"],
    ["Fuentes embebidas e iconos vectoriales", "Cumplido"],
    ["Paginas Principal, Servicios, Contacto y Multimedia", "Cumplido"],
    ["Carpeta con HTML, CSS, JS, JSON, imagenes y multimedia", "Cumplido"],
    ["Documento tecnico IEEE y guion de video exposicion", "Cumplido"],
    ["URL publica funcional", "Pendiente de publicacion"],
], [132, 38])

doc.titulo1("14. Conclusiones")
doc.parrafo("El portal NODO integra de forma coherente todos los requerimientos academicos: contenido semantico, diseno adaptable, interactividad con JavaScript y jQuery, arquitectura orientada a objetos, datos en JSON, consumo de una API real y multimedia optimizada. La evidencia responsive demuestra que la experiencia se mantiene usable en escritorio, tablet y movil.")
doc.parrafo("La unica actividad externa al desarrollo es la publicacion final, que requiere la cuenta de hosting del grupo. Una vez obtenida la URL, el proyecto queda listo para la entrega y la exposicion de maximo 10 minutos.")

doc.titulo1("15. Referencias")
doc.lista([
    "MDN Web Docs. Document Object Model (DOM). https://developer.mozilla.org/",
    "Open-Meteo. Weather Forecast API. https://open-meteo.com/",
    "Bootstrap Team. Bootstrap 5.3 Documentacion. https://getbootstrap.com/",
    "jQuery Foundation. jQuery 3.7 Documentacion. https://jquery.com/",
    "Google Fonts. Manrope y Space Grotesk (SIL Open Font License). https://fonts.google.com/",
    "Unsplash. Fotografias con licencia Unsplash. https://unsplash.com/license",
    "OpenStreetMap. Mapa embebido de Bucaramanga. https://www.openstreetmap.org/",
])

doc.output(str(SALIDA))
print("PDF generado:", SALIDA, f"{SALIDA.stat().st_size:,} bytes", "paginas:", doc.page_no())
