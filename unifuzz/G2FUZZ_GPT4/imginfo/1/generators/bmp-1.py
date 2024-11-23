from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a simple colored BMP file
def generate_simple_color_bmp(width, height, color, filename):
    image = Image.new("RGB", (width, height), color)
    image.save(filename)

# Function to generate a gradient BMP file
def generate_gradient_bmp(width, height, filename):
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    for i in range(width):
        gradient_color = int(255 * (i / width))
        draw.line((i, 0, i, height), fill=(gradient_color, gradient_color, gradient_color))
    
    image.save(filename)

# Function to generate a pattern BMP file
def generate_pattern_bmp(width, height, filename):
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    for y in range(0, height, 40):
        for x in range(0, width, 40):
            draw.rectangle([x, y, x+20, y+20], fill="blue")
            draw.rectangle([x+20, y+20, x+40, y+40], fill="blue")

    image.save(filename)

# Generating and saving BMP files
generate_simple_color_bmp(100, 100, "red", "./tmp/simple_color.bmp")
generate_gradient_bmp(256, 100, "./tmp/gradient.bmp")
generate_pattern_bmp(200, 200, "./tmp/pattern.bmp")

print("BMP files generated successfully.")