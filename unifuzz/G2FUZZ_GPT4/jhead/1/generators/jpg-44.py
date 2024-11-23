import os
from PIL import Image, ImageDraw, ImageFont

def create_sophisticated_progressive_jpg(filename, image_size, gradient_direction, text, text_color, font_size, quality, progressive, optimize=False):
    image = Image.new("RGB", image_size)
    draw = ImageDraw.Draw(image)

    # Gradient generation and text drawing code remains the same...

    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Save the image
    image.save(filename, "JPEG", quality=quality, progressive=progressive, optimize=optimize)
    print(f"Image saved to {filename}")

# Example usage
filename = "./tmp/sophisticated_example.jpg"
image_size = (800, 600)
gradient_direction = "vertical"
text = "Hello World"
text_color = "white"
font_size = 24
quality = 95
progressive = True
optimize = True

create_sophisticated_progressive_jpg(filename, image_size, gradient_direction, text, text_color, font_size, quality, progressive, optimize)