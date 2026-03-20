from PIL import Image
import numpy as np
import os

folder = "outputs"

for filename in os.listdir(folder):
    if filename.endswith(".png"):
        path = os.path.join(folder, filename)
        img = Image.open(path).convert("RGB")
        data = np.array(img)

        # Treat anything > 240 in all channels as "white"
        mask = ~((data[:,:,0] > 240) & (data[:,:,1] > 240) & (data[:,:,2] > 240))

        rows = np.any(mask, axis=1)
        cols = np.any(mask, axis=0)
        top, bottom = np.where(rows)[0][[0, -1]]
        left, right = np.where(cols)[0][[0, -1]]

        cropped = img.crop((left, top, right+1, bottom+1))
        cropped.save(path)
        print(f"Cropped: {filename}  {img.size} → {cropped.size}")

print("Done.")
