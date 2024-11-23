from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Text to be added
text = """
8. Compatibility: BMP format is widely supported across various operating systems and software applications, making it a versatile choice for storing and exchanging bitmapped images.
"""

# Create an image with white background
img = Image.new('RGB', (800, 200), color = (255, 255, 255))

# Initialize the drawing context
draw = ImageDraw.Draw(img)

# Define the font and size, use a built-in font
font = ImageFont.load_default()

# Starting position of the message
(x, y) = (10, 10)

# Add text to image
draw.text((x, y), text, fill=(0, 0, 0), font=font)

# Save the image to a BMP file
file_path = os.path.join(output_dir, 'compatibility.bmp')
img.save(file_path)

print(f"Image saved to {file_path}")