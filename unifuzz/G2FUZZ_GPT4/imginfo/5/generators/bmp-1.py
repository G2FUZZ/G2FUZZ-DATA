import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create a solid color BMP file
def create_solid_color_bmp(width, height, color, file_name):
    # Create an image with the specified color
    image = Image.new("RGB", (width, height), color)
    # Save the image in BMP format
    image.save(f'./tmp/{file_name}.bmp')

# Function to create a gradient BMP file
def create_gradient_bmp(width, height, file_name):
    # Create a new image with a white background
    image = Image.new("RGB", (width, height), "white")
    pixels = image.load()

    for x in range(width):
        for y in range(height):
            # Calculate the RGB values based on the position to create a gradient
            r = int((x / width) * 255)
            g = int((y / height) * 255)
            b = 125  # Constant value for a color aspect
            pixels[x, y] = (r, g, b)

    # Save the image in BMP format
    image.save(f'./tmp/{file_name}.bmp')

# Create a solid color BMP file
create_solid_color_bmp(100, 100, 'blue', 'solid_blue')

# Create a gradient BMP file
create_gradient_bmp(100, 100, 'gradient')

print("BMP files generated successfully.")