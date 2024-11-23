import os
from PIL import Image, ImageDraw, ImageFont

# Create the directory for saving files if it does not exist
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create an image with a white background
width, height = 640, 480
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Adding text to the image to represent the feature
text = """Device Independence: BMP files are designed to be device independent. They can render the same on any display device without depending on the device's resolution or color depth, making them suitable for use across different platforms and devices."""
try:
    # Try to use a default font
    font = ImageFont.truetype("arial.ttf", 15)
except IOError:
    # If specific font is not found, Pillow will fallback to a default font
    font = ImageFont.load_default()

# Text settings
text_width, text_height = draw.textsize(text, font=font)
text_x = (width - text_width) / 2
text_y = (height - text_height) / 2

# Apply text onto the image
draw.text((text_x, text_y), text, fill="black", font=font)

# Save the image as a BMP file
output_path = os.path.join(output_dir, "device_independence.bmp")
image.save(output_path, "BMP")

print(f"Image saved to {output_path}")