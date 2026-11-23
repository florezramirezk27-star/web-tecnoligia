"""Captura evidencia responsive con Chrome headless.
Requiere el servidor local activo: python -m http.server 8765
Uso: python tools/capture_evidence.py
"""
import pathlib, subprocess

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE = "http://127.0.0.1:8765/"
OUT = pathlib.Path(__file__).resolve().parents[1] / "docs" / "evidencia"
OUT.mkdir(parents=True, exist_ok=True)

CAPTURAS = [
    ("index.html",        "index-desktop.png",  1440, 1000),
    ("index.html",        "index-tablet.png",    820, 1180),
    ("index.html",        "index-mobile.png",    390,  844),
    ("servicios.html",    "servicios-desktop.png", 1440, 1000),
    ("contacto.html",     "contacto-mobile.png",   390,  844),
    ("multimedia.html",   "multimedia-desktop.png", 1440, 1000),
]

for pagina, nombre, ancho, alto in CAPTURAS:
    destino = OUT / nombre
    subprocess.run([
        CHROME, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
        "--no-first-run", "--virtual-time-budget=8000",
        f"--window-size={ancho},{alto}", f"--screenshot={destino}", BASE + pagina
    ], capture_output=True, text=True)
    print(f"{nombre:28s} {ancho}x{alto}  {destino.stat().st_size:,} bytes")
