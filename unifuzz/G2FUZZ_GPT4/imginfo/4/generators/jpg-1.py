import numpy as np
import os
from PIL import Image  # Import the Image module from PIL

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generating a gradient image
width, height = 256, 256
gradient = np.zeros((height, width, 3), dtype=np.uint8)

# Creating a horizontal gradient for demonstration
for x in range(width):
    for y in range(height):
        gradient[y, x] = [x, x, x]  # Setting the pixel value to create a grayscale gradient

# Save the generated image with JPEG compression
file_path = os.path.join(output_dir, 'gradient_lossy_compression.jpg')

# Convert the numpy array to a PIL Image and save it with the specified quality
image = Image.fromarray(gradient)
image.save(file_path, 'JPEG', quality=25)  # Adjust the quality for more or less compression

print(f'Gradient image saved with lossy compression at {file_path}')