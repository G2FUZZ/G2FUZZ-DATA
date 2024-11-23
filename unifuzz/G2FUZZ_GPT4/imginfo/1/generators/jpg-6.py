from PIL import Image, ImageDraw, ImageFont
import os

# Ensuring the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Text to be added to the image
text = """
6. Compatibility: JPG is widely supported across almost all image viewing and editing software, web browsers, and digital cameras, making it one of the most compatible image formats available.
"""

# Image size
img_width = 800
img_height = 200

# Create a new image with white background
image = Image.new("RGB", (img_width, img_height), "white")
draw = ImageDraw.Draw(image)

# Load a font
try:
    font = ImageFont.truetype("arial.ttf", size=15)
except IOError:
    font = ImageFont.load_default()

# Calculate text width and height
text_width, text_height = draw.textsize(text, font=font)

# Calculate x, y position of the text
x = (img_width - text_width) / 2
y = (img_height - text_height) / 2

# Add text to image
draw.text((x, y), text, fill="black", font=font)

# Save the image
file_path = os.path.join(output_dir, "compatibility.jpg")
image.save(file_path)

print(f"Image saved to {file_path}")