#!/usr/bin/env python3
"""Render a .pptx to per-slide PNGs: pptx -> pdf (LibreOffice) -> png (PyMuPDF)."""
import glob
import os
import subprocess
import sys

import pymupdf

SKILL = "/root/.claude/skills/synced/9e2455ea-3929-4bb4-9f44-24688b11eb7b_26e77000-58ba-47d7-9a38-02aecd2190f1/pptx"
deck = os.path.abspath(sys.argv[1])
out_dir = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.path.join(os.path.dirname(deck), "render")
dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 110
os.makedirs(out_dir, exist_ok=True)
for f in glob.glob(os.path.join(out_dir, "slide-*.png")):
    os.remove(f)
subprocess.run([sys.executable, os.path.join(SKILL, "scripts/office/soffice.py"), "--headless",
                "--convert-to", "pdf", "--outdir", out_dir, deck], check=True,
               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
pdf = os.path.join(out_dir, os.path.splitext(os.path.basename(deck))[0] + ".pdf")
doc = pymupdf.open(pdf)
zoom = dpi / 72.0
for i, page in enumerate(doc, start=1):
    pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom))
    pix.save(os.path.join(out_dir, f"slide-{i:02d}.png"))
print(f"{len(doc)} slides rendered to {out_dir}")
for f in sorted(glob.glob(os.path.join(out_dir, "slide-*.png"))):
    print(f)
