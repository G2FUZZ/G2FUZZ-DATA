from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define image size and color depth
width, height = 4000, 4000
color = (255, 0, 0)  # A bright red color

# Create a new image with a high color depth (RGB)
image = Image.new("RGB", (width, height), color)

# Save the image to a BMP file
file_path = './tmp/large_image.bmp'
image.save(file_path, "BMP")

print(f"Image saved to {file_path}")