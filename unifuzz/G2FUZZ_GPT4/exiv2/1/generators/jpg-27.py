import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Settings for the image
image_width = 800
image_height = 400  # Updated height to accommodate more text
background_color = (255, 255, 255)
text_color = (0, 0, 0)
font_size = 20
text = ("7. Wide Software Compatibility: JPG is one of the most widely supported image formats, compatible with virtually all "
        "image viewing and editing software, as well as web browsers.\n\n"
        "8. JPEG-LS: A related but separate standard from traditional JPEG, JPEG-LS provides lossless (and near-lossless) "
        "compression, aimed at medical imaging, satellite imagery, and other fields where image accuracy is critical and "
        "cannot be compromised.")

# Create a blank image and get a drawing context
image = Image.new('RGB', (image_width, image_height), background_color)
draw = ImageDraw.Draw(image)

# Load a font
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    font = ImageFont.load_default()

# Calculate text size and position, considering multiline text
text_width, text_height = draw.textsize(text, font=font)
text_x = (image_width - text_width) / 2
text_y = (image_height - text_height) / 2

# Adjust for multiline text
x, y = 10, 10  # Starting position

# Draw the updated text onto the image
draw.multiline_text((x, y), text, fill=text_color, font=font, align="left")

# Save the image
image.save(os.path.join(output_dir, 'feature_8.jpg'))