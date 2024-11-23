import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image with transparency
width, height = 400, 400
image = Image.new('RGBA', (width, height), (255, 255, 255, 0))

draw = ImageDraw.Draw(image)

# Function to draw a vertical gradient
def draw_vertical_gradient(draw, rect, top_color, bottom_color):
    (left, top, right, bottom) = rect
    for i, color in enumerate(range(top, bottom)):
        r, g, b = [top_color[j] + (bottom_color[j] - top_color[j]) * i / (bottom - top) for j in range(3)]
        draw.line([(left, top + i), (right, top + i)], fill=(int(r), int(g), int(b)), width=1)

# Draw a background gradient
draw_vertical_gradient(draw, (0, 0, width, height), (69, 117, 180), (215, 48, 39))

# Draw a semi-transparent polygon
draw.polygon([(100, 100), (300, 100), (350, 200), (50, 200)], fill=(0, 255, 0, 128))

# Draw a circle with a border
draw.ellipse((100, 220, 300, 350), fill=(255, 255, 0, 128), outline='blue', width=5)

# Add text with a custom font
try:
    font = ImageFont.truetype("arial.ttf", 24)  # Adjust path as necessary
except IOError:
    font = ImageFont.load_default()
draw.text((10, 10), "Complex PNG", fill="white", font=font)

# Add text with different sizes
for i in range(10, 30, 10):
    try:
        font = ImageFont.truetype("arial.ttf", i)
    except IOError:
        font = ImageFont.load_default()
    draw.text((10, 350 - i*2), f"Size {i}", fill="black", font=font)

# Save the image
image.save('./tmp/complex_image.png')