from PIL import Image, ImageDraw

# Create an image with solid colors
def create_image_with_compression_demo():
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
    
    # Save the image using PNG format
    output_path = './tmp/lossless_compression_demo.png'
    image.save(output_path, 'PNG')

# Ensure the ./tmp/ folder exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

create_image_with_compression_demo()