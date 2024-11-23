from PIL import Image, ImageDraw, ImageFont
import os
import random

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_gradient_image(width, height):
    """Generate a simple gradient image"""
    image = Image.new("RGB", (width, height), "#FFFFFF")
    for x in range(width):
        for y in range(height):
            image.putpixel((x, y), (x % 256, y % 256, (x + y) % 256))
    return image

def generate_solid_color_image(width, height, color):
    """Generate a solid color image"""
    return Image.new("RGB", (width, height), color)

def generate_random_pixels_image(width, height):
    """Generate an image with random pixels"""
    image = Image.new("RGB", (width, height), "#FFFFFF")
    for x in range(width):
        for y in range(height):
            image.putpixel((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    return image

def add_shapes_and_text_to_image(image):
    """Add circles, lines, and text overlays to an image"""
    draw = ImageDraw.Draw(image)
    # Draw circles
    for _ in range(10):
        x0 = random.randint(0, image.width // 2)
        y0 = random.randint(0, image.height // 2)
        x1 = x0 + random.randint(10, 100)
        y1 = y0 + random.randint(10, 100)
        draw.ellipse([x0, y0, x1, y1], outline="blue", width=2)
    # Draw lines
    for _ in range(10):
        x0 = random.randint(0, image.width)
        y0 = random.randint(0, image.height)
        x1 = random.randint(0, image.width)
        y1 = random.randint(0, image.height)
        draw.line([x0, y0, x1, y1], fill="red", width=2)
    # Add text overlays
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()
    draw.text((10, 10), "Demo Image", fill="green", font=font)

# Generate images
gradient_image = generate_gradient_image(256, 256)
solid_color_image = generate_solid_color_image(256, 256, "#FF5733")
random_pixels_image = generate_random_pixels_image(256, 256)

# Modify images by adding shapes and text
add_shapes_and_text_to_image(gradient_image)
add_shapes_and_text_to_image(solid_color_image)
add_shapes_and_text_to_image(random_pixels_image)

# Save images with custom compression quality (lower quality = smaller file size)
gradient_image.save('./tmp/gradient_with_shapes.jpg', quality=90)
solid_color_image.save('./tmp/solid_color_with_text.jpg', quality=95)
random_pixels_image.save('./tmp/random_pixels_with_shapes.jpg', quality=85)