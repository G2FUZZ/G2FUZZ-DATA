import os
from PIL import Image

# Create the directory for storing the output if it doesn't exist
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Image specifications
width, height = 640, 480  # Size in pixels
color = (255, 255, 255)  # White background

# Creating a new image with RGB mode and white background
image = Image.new("RGB", (width, height), color)

# Specifying resolution in pixels per meter (ppm)
# For example, let's use 3780 ppm which is approximately 96 dpi (dots per inch)
# Since 1 inch = 0.0254 meters, 96 dpi = 96/0.0254 dots per meter = ~3779.527559 pixels per meter
pixels_per_meter = (3780, 3780)

# Setting the resolution for the image
image.info['dpi'] = (pixels_per_meter[0] * 0.0254, pixels_per_meter[1] * 0.0254)

# Save the image as BMP with the specified resolution
image.save(os.path.join(output_dir, "image_with_resolution.bmp"), "BMP", dpi=pixels_per_meter)

print("Image saved successfully.")