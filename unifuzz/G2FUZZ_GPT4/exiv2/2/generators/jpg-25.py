from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

def create_radial_gradient(width, height):
    """
    Create a radial gradient image from the center outwards.
    """
    center_x, center_y = width / 2, height / 2
    max_distance = np.sqrt(center_x**2 + center_y**2)
    
    image = Image.new('RGB', (width, height))
    for x in range(width):
        for y in range(height):
            distance = np.sqrt((center_x - x)**2 + (center_y - y)**2)
            value = int((1 - distance / max_distance) * 255)
            image.putpixel((x, y), (value, value, value))
    return image

def add_text_overlay(image, text, position, font_size=30, font_color=(255, 0, 0)):
    """
    Add a text overlay to an existing image.
    """
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
        print("Default font loaded because Arial was not found.")
    
    draw.text(position, text, font_color, font=font)
    return image

# Ensure ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Parameters
width, height = 800, 600
text = "Hello, World!"
text_position = (50, height - 50)  # Position at the bottom-left

# Create a radial gradient background
image = create_radial_gradient(width, height)

# Add text overlay to the image
image_with_text = add_text_overlay(image, text, text_position)

# Save the image with JPEG compression
image_path = './tmp/complex_gradient_image.jpg'
image_with_text.save(image_path, 'JPEG', quality=85)  # Adjust quality for more or less compression

print(f"Image saved to {image_path}")