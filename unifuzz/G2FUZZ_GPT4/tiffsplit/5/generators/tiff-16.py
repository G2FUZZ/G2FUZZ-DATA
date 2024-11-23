from PIL import Image, PngImagePlugin
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define image size and color depth
width, height = 256, 256
color_depth = 16

# Create an array of shape (height, width, 3) for RGB, 16 bit depth
image_data = np.zeros((height, width, 3), dtype=np.uint16)

# Generate a gradient for each channel
for y in range(height):
    for x in range(width):
        image_data[y, x, 0] = (x * 65535) // width  # Red channel gradient
        image_data[y, x, 1] = (y * 65535) // height  # Green channel gradient
        image_data[y, x, 2] = ((x + y) * 65535) // (width + height)  # Blue channel mix

# Convert the numpy array to a PIL image
image = Image.fromarray(image_data, mode='I;16')

# Prepare DRM metadata
drm_info = {
    "Copyright": "Copyright 2023, Example Corp",
    "UsageRights": "No redistribution or reproduction allowed without permission.",
    "Contact": "copyright@example.com"
}

# Embedding DRM information in the PNG's metadata
info = PngImagePlugin.PngInfo()
for key, value in drm_info.items():
    info.add_text(key, value)

# Save the image as a PNG file with metadata
file_path = './tmp/high_color_depth_with_drm.png'
image.save(file_path, format='PNG', pnginfo=info)

print(f"Image saved to {file_path} with DRM metadata")