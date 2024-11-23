import numpy as np
from PIL import Image

# Create a simple image with progressive loading feature
width, height = 200, 200
image = np.zeros((height, width, 3), dtype=np.uint8)

# Add some color to the image
image[:, :width//2] = [255, 0, 0]  # Red
image[:, width//2:] = [0, 0, 255]  # Blue

# Save the image as a JPEG file with progressive loading
file_path = "./tmp/progressive_loading.jpg"
img = Image.fromarray(image)
img.save(file_path, format='JPEG', quality=95, optimize=True, progressive=True)

print(f"Image saved with progressive loading feature at: {file_path}")