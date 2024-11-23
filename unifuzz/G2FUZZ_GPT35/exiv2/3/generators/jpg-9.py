import numpy as np
from PIL import Image

# Define resolution parameters
resolutions = [(1920, 1080), (1280, 720), (800, 600)]

# Create and save jpg files with different resolutions
for idx, resolution in enumerate(resolutions):
    img = np.random.randint(0, 256, (resolution[1], resolution[0], 3), dtype=np.uint8)
    img = Image.fromarray(img)
    img.save(f"./tmp/image_{idx}.jpg")