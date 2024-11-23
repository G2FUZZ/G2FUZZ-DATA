from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the ./tmp/day_to_night/ directory exists or create it
directory_path = './tmp/day_to_night/'
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

def draw_gradient(draw, width, height, start_color, end_color):
    """Draw a vertical gradient"""
    for i in range(height):
        ratio = i / height
        r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
        g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
        b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
        draw.line([(0, i), (width, i)], fill=(r, g, b))

def draw_moon_and_stars(draw, width, height):
    """Draw moon and stars on the image"""
    # Draw the moon
    draw.ellipse([width - 100, 50, width - 50, 100], fill="white")
    # Draw stars
    for _ in range(50):
        x = random.randint(0, width)
        y = random.randint(0, height // 2)
        draw.point([x, y], fill="white")

def draw_scene(hour, width=400, height=400):
    """Draw a scene representing a specific hour of the day"""
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)

    if 6 <= hour <= 18:
        # Daytime sky
        sky_start_color = (135, 206, 250)  # Light Sky Blue
        sky_end_color = (25, 25, 112)  # Midnight Blue
    else:
        # Nighttime sky
        sky_start_color = (25, 25, 112)  # Midnight Blue
        sky_end_color = (0, 0, 0)  # Black
        draw_moon_and_stars(draw, width, height)

    draw_gradient(draw, width, height, sky_start_color, sky_end_color)

    # Add a "timestamp"
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    try:
        font = ImageFont.truetype(font_path, 20)
    except IOError:
        font = None
    time_str = f"{hour:02d}:00"
    draw.text((10, height - 30), time_str, fill='white', font=font)

    # Save the image
    image.save(f'{directory_path}scene_{hour:02d}.jpg', 'JPEG', quality=95, progressive=True)

import random

# Generate images for each hour of the day
for hour in range(24):
    draw_scene(hour)