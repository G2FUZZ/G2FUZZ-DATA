from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate an image with an alpha channel
# Create a 256x256 image with 4 channels (RGBA)
width, height = 256, 256
channels = 4  # Red, Green, Blue, Alpha

# Create an array of bytes representing the image
# For the alpha channel, create a gradient effect from fully opaque to fully transparent
data = np.zeros((height, width, channels), dtype=np.uint8)

# Fill the R, G, B channels with a solid color, e.g., semi-bright green
data[..., :3] = [0, 128, 0]  # RGB

# Create a gradient for the alpha channel
for y in range(height):
    alpha_value = int((y / height) * 255)
    data[y, :, 3] = alpha_value

# Create the PIL image
img = Image.fromarray(data, mode='RGBA')

# Save the image
output_path = os.path.join(output_dir, 'image_with_alpha.tiff')
img.save(output_path, format='TIFF')

print(f"Image saved to {output_path}")