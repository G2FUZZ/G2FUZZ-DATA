from PIL import Image, ImageDraw, ImagePalette

def create_indexed_image_with_compression_demo():
    # Image dimensions
    width, height = 800, 600
    
    # Create a new image with a white background in mode 'P' for palette-based images
    image = Image.new('P', (width, height), 'white')
    
    # Define a palette: each entry consists of three bytes for R, G, and B
    palette = [
        255, 255, 255,  # white
        255, 0, 0,      # red
        0, 255, 0,      # green
        0, 0, 255,      # blue
        255, 255, 0,    # yellow
        0, 0, 0,        # black
    ] + [0, 0, 0] * (256 - 6)  # Fill the rest of the 256 color palette with black
    
    # Assign palette to the image
    image.putpalette(palette)
    
    # Use ImageDraw to fill rectangles with the colors from the palette
    draw = ImageDraw.Draw(image)
    colors = [1, 2, 3, 4, 5]  # Palette indices for our defined colors (0 is white, already the background)
    rectangle_width = width // len(colors)
    
    for i, color_index in enumerate(colors):
        draw.rectangle([i * rectangle_width, 0, (i + 1) * rectangle_width, height], fill=color_index)
    
    # Save the image using PNG format which will automatically use the palette
    output_path = './tmp/indexed_lossless_compression_demo.png'
    image.save(output_path, 'PNG')

# Ensure the ./tmp/ folder exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

create_indexed_image_with_compression_demo()