from PIL import Image
import numpy as np
import os

folder = "outputs"

for filename in sorted(os.listdir(folder)):
    if not filename.endswith(".png"):
        continue

    path = os.path.join(folder, filename)
    img  = Image.open(path).convert("RGB")
    data = np.array(img)

    # Sample the corner pixel — that IS the border color
    corner = data[0, 0]          # top-left pixel
    r, g, b = int(corner[0]), int(corner[1]), int(corner[2])

    # Mask: pixels that are NOT the border color (tolerance = 15)
    tol  = 15
    mask = ~(
        (np.abs(data[:,:,0].astype(int) - r) < tol) &
        (np.abs(data[:,:,1].astype(int) - g) < tol) &
        (np.abs(data[:,:,2].astype(int) - b) < tol)
    )

    rows = np.any(mask, axis=1)
    cols = np.any(mask, axis=0)

    if not rows.any() or not cols.any():
        print(f"  SKIP (nothing to crop): {filename}")
        continue

    top,    bottom = np.where(rows)[0][[0, -1]]
    left,   right  = np.where(cols)[0][[0, -1]]

    # Add 2px padding so we don't clip the content edge
    top    = max(top    - 2, 0)
    left   = max(left   - 2, 0)
    bottom = min(bottom + 2, data.shape[0] - 1)
    right  = min(right  + 2, data.shape[1] - 1)

    cropped = img.crop((left, top, right + 1, bottom + 1))
    cropped.save(path)
    print(f"  OK  {filename}:  {img.size}  →  {cropped.size}   (border RGB {r},{g},{b})")

print("\nDone.")
