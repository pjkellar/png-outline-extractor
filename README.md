# PNG Outline Extractor

**PNG Outline Extractor** is a small Dockerized CLI tool that batch-processes PNG images and exports **outline-only** versions by removing color fills and keeping only the **black/dark line work**.

Perfect for turning artwork into **line art**, **coloring-book style images**, or clean **stroke-only overlays**.

---

## ✅ What it does

For every `.png` file found in an input folder (recursively), it:

- keeps only the black/dark outline pixels
- removes all other colors
- outputs a **transparent PNG**
- preserves folder structure
- keeps the original filename, but appends: `_Black`

Example:

```code
input/cupcake.png -> output/cupcake_Black.png
```

---

## 📦 Requirements

You only need:

- **Docker**

No local Python install required.

---
## 📁 Recommended repo structure

```code
png-outline-extractor/
Dockerfile
requirements.txt
outline_only.py
README.md
input/
.gitkeep
output/
.gitkeep
```

---

## 🚀 Build the Docker image

From the repo root:

```bash
docker build -t png-outline-extractor .
```

▶️ Run it

Basic usage

This will read PNGs from ./input and write to ./output:

```bash
docker run --rm \
  -v "$(pwd)/input:/in" \
  -v "$(pwd)/output:/out" \
  png-outline-extractor --in /in --out /out
```
---
🎭 Threshold Settings

Outlines in images often aren’t pure black — they may contain dark grays due to anti-aliasing.

Use `--threshold` to control how “dark” a pixel must be to count as outline.
  
```code
--threshold 0 = only exact #000000
--threshold 40 = keeps most dark outlines
--threshold 60 = recommended for smoother outlines
--threshold 80 = more aggressive (keeps more dark pixels)
```

Example:
```bash
docker run --rm \
  -v "$(pwd)/input:/in" \
  -v "$(pwd)/output:/out" \
  png-outline-extractor --in /in --out /out --threshold 60
```
---

🧠 Notes
  • Output is always PNG so transparency is preserved.
  • The script traverses folders recursively.
  • Output folder structure matches the input folder structure.

---

🏷️ Suggested GitHub Topics

python docker png image-processing outline line-art pillow cli batch-processing transparency