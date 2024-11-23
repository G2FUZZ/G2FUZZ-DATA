import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_complex_jpg(filename, text="PIL Demo", blur=False, font_path=None):
    # Create a new image with RGB mode
    image = Image.new("RGB", (800, 600))
    
    # Initialize the drawing context
    draw = ImageDraw.Draw(image)

    # (The rest of the image manipulation code remains unchanged...)

    # Ensure the ./tmp/ directory exists or create it
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the image with progressive option
    image.save(filename, "JPEG", quality=95, progressive=True)

# Filepath to save the image
filepath = './tmp/complex_image.jpg'

# Create and save a complex JPEG
create_complex_jpg(filepath, text="Hello, World!", blur=True)

print(f"Complex JPEG saved to {filepath}")