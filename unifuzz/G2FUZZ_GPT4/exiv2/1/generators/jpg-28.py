import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Settings for the image
image_width = 800
image_height = 400  # Increased height to accommodate additional text
background_color = (255, 255, 255)
text_color = (0, 0, 0)
font_size = 20

# Text for the features
texts = [
    "7. Wide Software Compatibility: JPG is one of the most widely supported image formats, compatible with virtually all "
    "image viewing and editing software, as well as web browsers.",
    "8. JPEG 2000: Another distinct but related standard, JPEG 2000 offers both lossless and lossy compression, superior "
    "compression efficiency, and additional features like progressive decoding and region-of-interest coding. It is used in "
    "various professional fields, though it has not replaced the original JPEG in most web and consumer applications."
]

# Create a blank image and get a drawing context
image = Image.new('RGB', (image_width, image_height), background_color)
draw = ImageDraw.Draw(image)

# Load a font
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    font = ImageFont.load_default()

# Initialize the starting Y position of the text
text_y = 10  # Start a little from the top

# Loop through each text to calculate text size, position, and draw it
for text in texts:
    text_width, text_height = draw.textsize(text, font=font)
    text_x = (image_width - text_width) / 2
    
    # Draw the text onto the image and update Y position for the next text
    draw.text((text_x, text_y), text, fill=text_color, font=font)
    text_y += text_height + 10  # Add a small padding between the texts

# Save the image
image.save(os.path.join(output_dir, 'features.jpg'))