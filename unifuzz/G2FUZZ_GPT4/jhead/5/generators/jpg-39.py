from PIL import Image, ImageDraw
import os
import math

def create_horizontal_gradient_image(width, height, filename, quality=95):
    """
    Create a simple horizontal gradient image.
    """
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)
    for i in range(width):
        color = int(255 * (i / width))
        draw.line((i, 0, i, height), fill=(color, color, color))
    save_image(image, 'horizontal', filename, quality)

def create_vertical_gradient_image(width, height, filename, quality=95):
    """
    Create a simple vertical gradient image.
    """
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)
    for i in range(height):
        color = int(255 * (i / height))
        draw.line((0, i, width, i), fill=(color, color, color))
    save_image(image, 'vertical', filename, quality)

def create_radial_gradient_image(width, height, filename, quality=95):
    """
    Create a radial gradient image.
    """
    image = Image.new("RGB", (width, height))
    centerX, centerY = width / 2, height / 2
    for x in range(width):
        for y in range(height):
            distanceToCenter = math.sqrt((x - centerX) ** 2 + (y - centerY) ** 2)
            distanceToCenter = distanceToCenter / (math.sqrt(2) * width / 2)
            color = int(255 * (1 - min(1, distanceToCenter)))
            image.putpixel((x, y), (color, color, color))
    save_image(image, 'radial', filename, quality)

def save_image(image, gradient_type, filename, quality):
    """
    Save the image in a structured directory based on gradient type.
    """
    path = f'./tmp/{gradient_type}/'
    os.makedirs(path, exist_ok=True)
    image.save(f'{path}{filename}.jpg', 'JPEG', quality=quality)

# Example usage:
create_horizontal_gradient_image(500, 300, 'gradient_horizontal_high_quality', quality=95)
create_vertical_gradient_image(500, 300, 'gradient_vertical_high_quality', quality=95)
create_radial_gradient_image(500, 300, 'gradient_radial_high_quality', quality=95)