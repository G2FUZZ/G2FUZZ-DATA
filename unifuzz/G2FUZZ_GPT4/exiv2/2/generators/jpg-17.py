from PIL import Image, ImageFile
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

# Define custom quantization tables
# These tables are just an example and need to be adjusted based on the specific needs
# Note: The values in these tables should be carefully chosen based on the application's requirements.
#       Incorrect values can severely affect the image quality.
luminance_q_table = np.array([
    16, 11, 10, 16, 24, 40, 51, 61,
    12, 12, 14, 19, 26, 58, 60, 55,
    14, 13, 16, 24, 40, 57, 69, 56,
    14, 17, 22, 29, 51, 87, 80, 62,
    18, 22, 37, 56, 68, 109, 103, 77,
    24, 35, 55, 64, 81, 104, 113, 92,
    49, 64, 78, 87, 103, 121, 120, 101,
    72, 92, 95, 98, 112, 100, 103, 99
], dtype=np.uint8).reshape((8, 8))

chrominance_q_table = np.array([
    17, 18, 24, 47, 99, 99, 99, 99,
    18, 21, 26, 66, 99, 99, 99, 99,
    24, 26, 56, 99, 99, 99, 99, 99,
    47, 66, 99, 99, 99, 99, 99, 99,
    99, 99, 99, 99, 99, 99, 99, 99,
    99, 99, 99, 99, 99, 99, 99, 99,
    99, 99, 99, 99, 99, 99, 99, 99,
    99, 99, 99, 99, 99, 99, 99, 99
], dtype=np.uint8).reshape((8, 8))

# Apply custom quantization tables
ImageFile.MAXBLOCK = width * height  # May be necessary for large images

# Set custom quantization tables
image.encoderinfo = {
    "quality": 85,
    "qtables": [luminance_q_table, chrominance_q_table]
}

# Save the image with custom quantization tables
custom_q_table_image_path = './tmp/gradient_image_custom_q_table.jpg'
image.save(custom_q_table_image_path, 'JPEG')

print(f"Image saved with standard compression to {image_path}")
print(f"Image saved with custom quantization tables to {custom_q_table_image_path}")