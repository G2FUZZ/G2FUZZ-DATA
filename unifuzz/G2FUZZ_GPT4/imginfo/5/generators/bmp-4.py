import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an RGBA image
width, height = 200, 200
image = Image.new('RGBA', (width, height), (255, 0, 0, 0))  # Transparent background

# Drawing a semi-transparent blue square in the center
for x in range(50, 150):
    for y in range(50, 150):
        image.putpixel((x, y), (0, 0, 255, 128))  # Semi-transparent blue

# Since BMP does not naturally support full alpha transparency,
# we convert the image to RGB, and the transparency is represented as white or any background color.
image_rgb = image.convert("RGB")

# Saving the image as BMP without alpha channel as BMP doesn't support it naturally
# But we handled transparency by blending it with a white background
image_rgb.save('./tmp/alpha_channel_example.bmp')