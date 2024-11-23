from PIL import Image, ImageDraw, ImagePalette

def create_stereoscopic_image_demo():
    # Image dimensions
    width, height = 800, 600
    
    # Create two new images with a white background in mode 'P' for palette-based images
    left_image = Image.new('P', (width, height), 'white')
    right_image = Image.new('P', (width, height), 'white')
    
    # Define a palette: each entry consists of three bytes for R, G, and B
    palette = [
        255, 255, 255,  # white
        255, 0, 0,      # red
        0, 255, 0,      # green
        0, 0, 255,      # blue
        255, 255, 0,    # yellow
        0, 0, 0,        # black
    ] + [0, 0, 0] * (256 - 6)  # Fill the rest of the 256 color palette with black
    
    # Assign palette to both images
    left_image.putpalette(palette)
    right_image.putpalette(palette)
    
    # Use ImageDraw to fill rectangles with the colors from the palette
    def draw_rectangles(image, offset=0):
        draw = ImageDraw.Draw(image)
        colors = [1, 2, 3, 4, 5]  # Palette indices for our defined colors (0 is white, already the background)
        rectangle_width = width // len(colors)
        
        for i, color_index in enumerate(colors):
            draw.rectangle([i * rectangle_width + offset, 0, (i + 1) * rectangle_width + offset, height], fill=color_index)
    
    # Draw the rectangles on both images with a slight horizontal offset to create the stereoscopic effect
    draw_rectangles(left_image, -10)
    draw_rectangles(right_image, 10)
    
    # Combine the two images into one stereoscopic image (side by side)
    stereoscopic_width = width * 2
    stereoscopic_image = Image.new('P', (stereoscopic_width, height), 'white')
    stereoscopic_image.paste(left_image, (0, 0))
    stereoscopic_image.paste(right_image, (width, 0))
    stereoscopic_image.putpalette(palette)
    
    # Save the stereoscopic image using PNG format
    output_path = './tmp/stereoscopic_demo.png'
    stereoscopic_image.save(output_path, 'PNG')

# Ensure the ./tmp/ folder exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

create_stereoscopic_image_demo()