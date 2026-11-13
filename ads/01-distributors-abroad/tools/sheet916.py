# Tile 9:16 stills (named <t>.jpg) into a labelled sheet: python3 sheet916.py <dir> <out.jpg> [cols] [tile_w]
import sys, glob, os
from PIL import Image, ImageDraw
d, out = sys.argv[1], sys.argv[2]; cols = int(sys.argv[3]) if len(sys.argv) > 3 else 7; tw = int(sys.argv[4]) if len(sys.argv) > 4 else 270
fs = sorted(glob.glob(os.path.join(d, '*.jpg')), key=lambda f: float(os.path.basename(f)[:-4])); th = tw * 16 // 9
rows = (len(fs) + cols - 1) // cols; S = Image.new('RGB', (cols * (tw + 6), rows * (th + 30)), '#111')
for i, f in enumerate(fs):
    im = Image.open(f).convert('RGB').resize((tw, th)); x, y = (i % cols) * (tw + 6), (i // cols) * (th + 30)
    S.paste(im, (x, y + 26)); ImageDraw.Draw(S).text((x + 4, y + 6), os.path.basename(f)[:-4] + 's', fill='#fff')
S.save(out, quality=88); print(out, len(fs))
