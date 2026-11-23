"""Genera el video corporativo del portal NODO a partir de imágenes propias.
Uso: python tools/generate_video.py  (requiere FFmpeg en el PATH)
"""
import pathlib, shutil, subprocess, tempfile

BASE = pathlib.Path(__file__).resolve().parents[1]
IMG = BASE / "assets" / "img"
OUT = BASE / "assets" / "video" / "nodo-startup.mp4"

CLIPS = [
    ("hero-equipo.webp", "NODO - Startup tecnologica de Bucaramanga"),
    ("codigo.webp", "Desarrollo web y aplicaciones a medida"),
    ("analitica.webp", "Datos, automatizacion e inteligencia"),
    ("servidores.webp", "Infraestructura, cloud y soporte 24/7"),
    ("equipo.webp", "Tecnologia hecha en Santander"),
]

# se explica la doble barra: FFmpeg necesita escapar ':' en filtros de Windows
FONT = "fontfile=C\\\\:/Windows/Fonts/segoeui.ttf"

def run(args, cwd):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-1200:])

with tempfile.TemporaryDirectory() as td:
    tmp = pathlib.Path(td)
    concat_lines = []
    for i, (image, caption) in enumerate(CLIPS, 1):
        src = tmp / f"img{i}.webp"
        shutil.copyfile(IMG / image, src)          # evita acentos en la ruta
        cap = tmp / f"cap{i}.txt"
        cap.write_text(caption, encoding="utf-8")
        clip = tmp / f"clip{i}.mp4"
        vf = (
            "scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=24,"
            f"drawtext={FONT}:textfile={cap.name}:expansion=none:fontcolor=white:fontsize=40:"
            "x=(w-text_w)/2:y=h-150:box=1:boxcolor=black@0.45:boxborderw=18,"
            "fade=t=in:st=0:d=0.4,fade=t=out:st=2.6:d=0.4,format=yuv420p"
        )
        run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-t", "3",
             "-i", src.name, "-vf", vf, "-an", "-c:v", "libx264", "-preset",
             "veryfast", "-crf", "23", "-pix_fmt", "yuv420p", clip.name], tmp)
        concat_lines.append(f"file 'clip{i}.mp4'")
        print("clip", i, "listo")

    listing = tmp / "lista.txt"
    listing.write_text("\n".join(concat_lines), encoding="utf-8")
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
         "-i", "lista.txt", "-c", "copy", "-movflags", "+faststart", str(OUT)], tmp)
    print("VIDEO:", OUT, f"{OUT.stat().st_size:,} bytes")
