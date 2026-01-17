import os
import argparse
from PIL import Image

def process_png(in_path: str, out_path: str, threshold: int) -> None:
    """
    Keep only black (or near-black if threshold > 0) pixels; everything else becomes transparent.
    threshold:
      - 0  => only exact #000000
      - >0 => keep pixels where R,G,B <= threshold
    """
    im = Image.open(in_path).convert("RGBA")
    pixels = im.load()
    w, h = im.size

    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]

            # Ignore fully transparent pixels already
            if a == 0:
                continue

            is_black = (r == 0 and g == 0 and b == 0) if threshold == 0 else (r <= threshold and g <= threshold and b <= threshold)

            if is_black:
                # Force pure black, fully opaque
                pixels[x, y] = (0, 0, 0, 255)
            else:
                # Transparent
                pixels[x, y] = (0, 0, 0, 0)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    im.save(out_path, "PNG")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="in_dir", required=True, help="Input folder containing PNGs")
    parser.add_argument("--out", dest="out_dir", required=True, help="Output folder")
    parser.add_argument("--threshold", type=int, default=0, help="0 = exact black only; higher keeps near-black too (e.g. 20)")
    args = parser.parse_args()

    in_dir = os.path.abspath(args.in_dir)
    out_dir = os.path.abspath(args.out_dir)

    if not os.path.isdir(in_dir):
        raise SystemExit(f"Input folder not found: {in_dir}")

    for root, _, files in os.walk(in_dir):
        for name in files:
            if not name.lower().endswith(".png"):
                continue

            in_path = os.path.join(root, name)
            rel_dir = os.path.relpath(root, in_dir)

            base, ext = os.path.splitext(name)
            out_name = f"{base}_Black{ext}"

            out_path = os.path.join(out_dir, rel_dir, out_name)
            process_png(in_path, out_path, args.threshold)

    print(f"Done. Wrote results to: {out_dir}")

if __name__ == "__main__":
    main()