from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Image settings
image_width, image_height = 800, 200
background_color = (255, 255, 255)
font_color = (0, 0, 0)
font_path = "arial.ttf"  # Adjust the font path as needed
font_size = 20

# Initialize a new image with a white background
image = Image.new("RGB", (image_width, image_height), color=background_color)
draw = ImageDraw.Draw(image)

# Load a font
try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    font = ImageFont.load_default()

# Text to be drawn
text = "8. Widespread Compatibility: JPG is one of the most widely supported image formats, compatible with virtually all image viewing and editing software, as well as web browsers."

# Calculate text width and height to position it on the center
text_width, text_height = draw.textsize(text, font=font)
x = (image_width - text_width) / 2
y = (image_height - text_height) / 2

# Draw the text onto the image
draw.text((x, y), text, fill=font_color, font=font)

# Save the image
output_path = os.path.join(output_dir, "widespread_compatibility.jpg")
image.save(output_path)

print(f"Image saved to {output_path}")