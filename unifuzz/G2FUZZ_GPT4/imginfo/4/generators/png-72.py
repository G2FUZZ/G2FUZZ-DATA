import os
from PIL import Image, ImageDraw, ImageFont, PngImagePlugin

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Function to create a gradient
def make_gradient(width, height, left_color, right_color):
    base = Image.new('RGB', (width, height), left_color)
    top = Image.new('RGB', (width, height), right_color)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        for x in range(width):
            mask_data.append(int(255 * (x / width)))
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

# Create an image with a gradient background
img = make_gradient(200, 200, 'darkblue', 'cyan')

# Draw some custom shapes
draw = ImageDraw.Draw(img)
draw.rectangle([10, 10, 190, 60], fill="darkred", outline="black")
draw.ellipse([150, 120, 190, 160], fill="yellow", outline="black")
draw.polygon([(50, 180), (100, 100), (150, 180)], fill="green", outline="black")

# Add text
try:
    font = ImageFont.truetype("arial.ttf", 15)
except IOError:
    font = ImageFont.load_default()
draw.text((10, 70), "Hello, PIL!", fill="white", font=font)

# Prepare metadata
metadata = PngImagePlugin.PngInfo()
metadata.add_text("Copyright", "Copyright © 2023 by My Company")
metadata.add_text("Author", "John Doe")
metadata.add_text("Description", "This is a complex image with metadata, custom shapes, and gradients.")

# Save the image with metadata
# Omitting the ICC profile embedding for simplicity and to avoid the FileNotFoundError
img.save('./tmp/complex_sample_with_metadata.png', "PNG", pnginfo=metadata)

print("Image saved with custom shapes, gradients, and embedded metadata.")