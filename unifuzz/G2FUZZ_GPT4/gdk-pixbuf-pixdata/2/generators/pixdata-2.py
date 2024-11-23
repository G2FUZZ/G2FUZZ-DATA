from PIL import Image
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define image properties
width, height = 100, 100  # Size of the image
color_depth = 8  # 8-bit color depth

# Create a new image with 8-bit color depth (256 colors)
# Here, 'P' mode is used for paletted images, which can be used to simulate 8-bit color depth
image = Image.new('P', (width, height))

# Create a gradient effect for demonstration
for x in range(width):
    for y in range(height):
        # Calculate a color index in range 0-255
        color_index = (x + y) % 256
        image.putpixel((x, y), color_index)

# Define a color palette (optional, for better visualization of the 8-bit color depth)
# This creates a grayscale palette but you can customize it to demonstrate various colors
palette = []
for i in range(256):
    palette.extend([i, i, i])  # Grayscale values
image.putpalette(palette)

# Save the image
file_path = os.path.join(output_dir, '8bit_color_depth_image.png')
image.save(file_path)

print(f'Image with 8-bit color depth saved to {file_path}')