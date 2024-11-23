from PIL import Image
import numpy as np
import os

# Ensure ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image with a gradient
width, height = 800, 600
image = Image.new('RGB', (width, height))
for x in range(width):
    for y in range(height):
        # Gradient from black to white
        value = int((x / width) * 255)
        image.putpixel((x, y), (value, value, value))

# Save the image with JPEG compression
image_path = './tmp/gradient_image.jpg'
image.save(image_path, 'JPEG', quality=85)  # Adjust quality for more or less compression

# Unfortunately, PIL (Python Imaging Library) does not support saving images in the 'Lossless JPEG' format directly.
# However, for the purpose of demonstrating an approach that might be taken if the feature were available,
# the following code block is a hypothetical example. 

# Hypothetical code to save the image in 'Lossless JPEG' format (this feature is not actually supported by PIL)
lossless_image_path = './tmp/gradient_image_lossless.jpg'
# image.save(lossless_image_path, 'JPEG', lossless=True)  # This is a hypothetical parameter

print(f"Image saved with standard compression to {image_path}")
# print(f"Image saved with lossless compression to {lossless_image_path}")  # This would be the print statement if lossless JPEG were supported

# Note: The actual implementation of saving an image in 'Lossless JPEG' format would require a library or an API
# that supports this feature, as the standard Python Imaging Library (PIL) does not support 'Lossless JPEG' natively.