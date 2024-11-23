import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
os.makedirs("./tmp/", exist_ok=True)

# Create a simple image with a gradient to demonstrate interlacing
width, height = 800, 600
image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)

# Draw a vertical gradient
for i in range(height):
    intensity = int(255 * (i / height))
    draw.line([(0, i), (width, i)], fill=(intensity, intensity, intensity))

# Save the image with Adam7 interlacing
image.save("./tmp/interlaced_image.png", "PNG", interlace=True)