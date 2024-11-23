import numpy as np
from PIL import Image

# Define resolution parameters
resolutions = [(1920, 1080), (1280, 720), (800, 600)]

# Define chroma subsampling ratios (possible values: '4:4:4', '4:2:2', '4:2:0')
subsampling_ratios = ['4:4:4', '4:2:2', '4:2:0']

# Create and save jpg files with different resolutions and chroma subsampling
for idx, resolution in enumerate(resolutions):
    for subsampling_ratio in subsampling_ratios:
        img = np.random.randint(0, 256, (resolution[1], resolution[0], 3), dtype=np.uint8)
        img = Image.fromarray(img)
        img.save(f"./tmp/image_{idx}_subsampling_{subsampling_ratio}.jpg", subsampling=subsampling_ratio)