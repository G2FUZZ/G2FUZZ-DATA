import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Settings for the image
image_width = 800
image_height = 200
background_color = (255, 255, 255)
text_color = (0, 0, 0)
font_size = 20
text = ("7. Wide Software Compatibility: JPG is one of the most widely supported image formats, compatible with virtually all "
        "image viewing and editing software, as well as web browsers.")

# Create a blank image and get a drawing context
image = Image.new('RGB', (image_width, image_height), background_color)
draw = ImageDraw.Draw(image)

# Load a font
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    font = ImageFont.load_default()

# Calculate text size and position
text_width, text_height = draw.textsize(text, font=font)
text_x = (image_width - text_width) / 2
text_y = (image_height - text_height) / 2

# Draw the text onto the image
draw.text((text_x, text_y), text, fill=text_color, font=font)

# Save the image
image.save(os.path.join(output_dir, 'feature_7.jpg'))