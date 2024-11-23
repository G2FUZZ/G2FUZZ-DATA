import numpy as np
from PIL import Image

# Create an image with intricate color gradients and patterns
width, height = 1000, 800
image = np.zeros((height, width, 3), dtype=np.uint8)  # Changed to 3 channels (RGB) instead of 4 (RGBA)
for y in range(height):
    for x in range(width):
        r = int(255 * np.sin(x / width * np.pi))
        g = int(255 * np.cos(y / height * np.pi))
        b = int(255 * np.sin((x+y) / (width+height) * np.pi))
        image[y, x] = [r, g, b]

# Save the image as a jpg file without alpha channel
file_path = './tmp/intricate_color_gradients.jpg'
Image.fromarray(image).convert('RGB').save(file_path)  # Convert image to RGB mode before saving
print(f"Image with intricate color gradients saved at: {file_path}")