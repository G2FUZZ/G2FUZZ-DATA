from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define image size and color (example color in RGB)
image_size = (100, 100)  # 100x100 pixels
color_rgb = (255, 0, 0)  # Red color

# Generate an 8-bit (grayscale) image
image_8bit = Image.new('L', image_size, color=255)  # 'L' mode for 8-bit pixels, grayscale
image_8bit.save('./tmp/image_8bit.png')

# Generate a 24-bit (true color) image
image_24bit = Image.new('RGB', image_size, color=color_rgb)  # 'RGB' mode for 24-bit
image_24bit.save('./tmp/image_24bit.png')

# Generate a 32-bit (true color with alpha) image
color_rgba = (255, 0, 0, 128)  # Red color with 50% opacity
image_32bit = Image.new('RGBA', image_size, color=color_rgba)  # 'RGBA' for 32-bit
image_32bit.save('./tmp/image_32bit.png')