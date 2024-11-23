import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with white background
img = Image.new('RGB', (800, 200), color = (255, 255, 255))
d = ImageDraw.Draw(img)

# Define the text and font (using a common, generic font)
text = "9. Standardization: The format is standardized by the Joint Photographic Experts Group (JPEG), ensuring consistent behavior across different platforms and devices."
try:
    # This tries to use a default font. Adjust the path as necessary.
    font = ImageFont.truetype("arial.ttf", 15)
except IOError:
    # If the specific font is not found, we default to a basic font.
    font = ImageFont.load_default()

# Add text to the image
d.text((10,10), text, fill=(0,0,0), font=font)

# Save the image
img_path = './tmp/standardization.jpg'
img.save(img_path)

print(f"Image saved at: {img_path}")