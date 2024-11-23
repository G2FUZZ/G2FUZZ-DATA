import numpy as np
from PIL import Image
import os

# Ensure ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple gradient image for demonstration
width, height = 256, 256
array = np.zeros((height, width, 3), dtype=np.uint8)

# Generate gradient
for y in range(height):
    for x in range(width):
        array[y, x] = [x, y, (x+y)//2]

# Convert array to an image
image = Image.fromarray(array)

# Save the original image
image.save('./tmp/gradient.jpg', quality=95)  # High quality to see the effect of manual "compression"

# Huffman coding demonstration (conceptual, not actual implementation)
# Here, we simply demonstrate the concept by reducing the image quality, which isn't Huffman coding but demonstrates data reduction
image.save('./tmp/gradient_compressed.jpg', quality=10)  # Lower quality to simulate "compression"

print("Images saved in ./tmp/: 'gradient.jpg' (less compression) and 'gradient_compressed.jpg' (more compression)")