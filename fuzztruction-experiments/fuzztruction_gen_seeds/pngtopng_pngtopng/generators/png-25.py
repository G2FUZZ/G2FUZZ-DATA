from PIL import Image, ImageDraw
import os

# Create an image with solid colors and save it as a palette-based image with lossy compression
def create_image_with_palette_and_lossy_compression_demo():
    # Image dimensions
    width, height = 800, 600
    
    # Create a new image with a white background
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    
    # Create rectangles of solid colors
    colors = ['red', 'green', 'blue', 'yellow', 'black']
    rectangle_width = width // len(colors)
    for i, color in enumerate(colors):
        draw.rectangle([i * rectangle_width, 0, (i + 1) * rectangle_width, height], fill=color)
    
    # Convert the image to use a palette (8-bit color)
    image = image.convert('P', palette=Image.ADAPTIVE, colors=256)
    
    # Before saving, apply a lossy compression technique
    # This example uses PIL's 'optimize' and 'save_all' parameters for demonstration,
    # which are not truly lossy but can help reduce file size in some cases.
    # For actual lossy compression, consider using an external tool or library that supports PNG lossy compression.
    output_path = './tmp/palette_lossy_compression_demo.png'
    image.save(output_path, 'PNG', optimize=True, save_all=True)

# Ensure the ./tmp/ folder exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

create_image_with_palette_and_lossy_compression_demo()