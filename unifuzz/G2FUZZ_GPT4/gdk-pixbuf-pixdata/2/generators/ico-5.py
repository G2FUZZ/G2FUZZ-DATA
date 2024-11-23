from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_icon(size, filename):
    # Create an image with transparent background
    image = Image.new("RGBA", (size, size), (255, 255, 255, 0))

    # Draw a shape to demonstrate the adaptiveness
    draw = ImageDraw.Draw(image)
    padding = size // 10
    corner_radius = size // 5
    draw.ellipse([padding, padding, size-padding, size-padding], fill=(255, 0, 0, 255), outline=None)
    draw.rounded_rectangle([padding, padding, size-padding, size-padding], fill=None, outline=(0, 0, 0, 255), width=size//20, radius=corner_radius)

    # Save the icon with multiple sizes
    image.save(filename, format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])

create_icon(256, './tmp/adaptive_icon.ico')