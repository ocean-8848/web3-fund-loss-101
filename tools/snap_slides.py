#!/usr/bin/env python3
"""Screenshot every page of one chapter's slides (end state of each line) and tile them into contact sheets.

  python3 tools/snap_slides.py <chapter id> <out dir> [first-last]

Builds slides/<id>/preview.html, renders each page with headless Chrome at 1920x1080 into <out dir>/p<NN>.png,
and writes <out dir>/sheet-<n>.png (3x3 pages each, page number + caption under every tile). Needs network (GSAP from cdnjs).
"""
import os, subprocess, sys, tempfile, json, re
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ch, out = sys.argv[1], os.path.abspath(sys.argv[2])
os.makedirs(out, exist_ok=True)
subprocess.run([sys.executable, os.path.join(ROOT, "tools", "make_slides.py"), "--only", ch], check=True)
prev = os.path.join(ROOT, "slides", ch, "preview.html")
nar = json.load(open(os.path.join(ROOT, "slides", ch, "narration.json"), encoding="utf-8"))
caps = [l for s in nar["scenes"] for l in s["lines"]]
pages = list(range(1, len(caps) + 1))
if len(sys.argv) > 3:
    a, b = map(int, sys.argv[3].split("-")); pages = [p for p in pages if a <= p <= b]


def snap(p):
    png = os.path.join(out, f"p{p:02d}.png")
    with tempfile.TemporaryDirectory() as ud:
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--user-data-dir={ud}",
                        "--window-size=1920,1080", "--virtual-time-budget=4000", f"--screenshot={png}",
                        f"file://{prev}?snap#{ch}/{p}"], capture_output=True, timeout=90)
    return png


with ThreadPoolExecutor(4) as ex:
    pngs = list(ex.map(snap, pages))
font = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", 20)
W, H, CAPH = 640, 360, 64
for n in range(0, len(pages), 9):
    chunk = list(zip(pages, pngs))[n:n + 9]
    sheet = Image.new("RGB", (W * 3, (H + CAPH) * ((len(chunk) + 2) // 3)), "white")
    d = ImageDraw.Draw(sheet)
    for i, (p, png) in enumerate(chunk):
        x, y = (i % 3) * W, (i // 3) * (H + CAPH)
        if os.path.exists(png):
            sheet.paste(Image.open(png).convert("RGB").resize((W, H)), (x, y))
        t = f"{p}. {caps[p - 1]}"
        d.text((x + 8, y + H + 6), t[:24], fill="black", font=font)
        d.text((x + 8, y + H + 32), t[24:48], fill="black", font=font)
    sheet.save(os.path.join(out, f"sheet-{n // 9 + 1}.png"))
print(f"{len(pages)} pages -> {out}/p*.png, sheet-*.png")
