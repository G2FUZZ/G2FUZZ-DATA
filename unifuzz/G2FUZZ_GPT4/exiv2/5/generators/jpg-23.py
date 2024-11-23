from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a new blank image
image = Image.new('RGB', (800, 300), color = (255, 255, 255))  # Increased height to accommodate additional text

# Initialize ImageDraw
draw = ImageDraw.Draw(image)

# Define the text to be drawn, now including Error Resilience feature
text = """
6. Wide Compatibility: JPG is one of the most widely supported image formats, compatible with virtually all image viewing and editing software, as well as web browsers.

3. Error Resilience: While not robust against file corruption, certain encoding strategies can make JPG files more resilient to errors, allowing partial image display even if the file is slightly damaged.
"""

# Load a font
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # This path is an example; it might differ
try:
    font = ImageFont.truetype(font_path, 20)
except IOError:
    font = ImageFont.load_default()

# Drawing text on the image
draw.text((10, 10), text, fill=(0, 0, 0), font=font)

# Save the image
file_path = os.path.join(output_dir, 'features_6_and_3.jpg')  # Corrected variable name here
image.save(file_path)

print(f"Image saved to {file_path}")