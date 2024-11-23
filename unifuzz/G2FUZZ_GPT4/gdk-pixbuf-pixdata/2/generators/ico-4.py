import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_transparent_ico(size=(256, 256), filename='./tmp/transparent_icon.ico'):
    """
    Create an ICO file with transparency support.

    Args:
    - size: a tuple for the icon size, default is (256, 256)
    - filename: the path to save the .ico file
    """
    # Create an image with transparency (RGBA)
    img = Image.new('RGBA', size, color=(0, 0, 0, 0))
    
    # Draw a simple shape that demonstrates transparency
    draw = ImageDraw.Draw(img)
    # Draw a semi-transparent rectangle
    draw.rectangle([size[0]//4, size[1]//4, 3*size[0]//4, 3*size[1]//4], fill=(255, 0, 0, 128))
    # Draw a less transparent circle
    draw.ellipse([size[0]//3, size[1]//3, 2*size[0]//3, 2*size[1]//3], fill=(0, 255, 0, 192))

    # Save the image as an icon file with transparency
    img.save(filename)

create_transparent_ico()