import numpy as np
from PIL import Image

# Create multiple images to store in the TIFF file
image1 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)
image2 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)

# Save the images as TIFF with multiple pages
with Image.new("L", (100, 100)) as tiff:
    tiff.save("./tmp/multiple_pages.tiff", compression="tiff_adobe_deflate", save_all=True, append_images=[Image.fromarray(image1), Image.fromarray(image2)])