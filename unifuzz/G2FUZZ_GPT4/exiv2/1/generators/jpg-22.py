import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Settings for the image
image_width = 800
image_height = 200 * 2  # Increased the height to accommodate two features
background_color = (255, 255, 255)
text_color = (0, 0, 0)
font_size = 20
texts = [
    "7. Wide Software Compatibility: JPG is one of the most widely supported image formats, compatible with virtually all image viewing and editing software, as well as web browsers.",
    "2. 8-bit and 12-bit Color Modes: JPEG supports both 8-bit and 12-bit color modes per channel, allowing for variations in color depth. This means that the format can accommodate standard 24-bit RGB images (8 bits per channel) as well as 36-bit high color (12 bits per channel), providing flexibility in balancing file size and color fidelity."
]

# Create a blank image and get a drawing context
image = Image.new('RGB', (image_width, image_height), background_color)
draw = ImageDraw.Draw(image)

# Load a font
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    font = ImageFont.load_default()

# Calculate text positions and draw them
for i, text in enumerate(texts):
    text_width, text_height = draw.textsize(text, font=font)
    text_x = (image_width - text_width) / 2
    text_y = (image_height / len(texts) - text_height) / 2 + (image_height / len(texts)) * i

    # Draw the text onto the image
    draw.text((text_x, text_y), text, fill=text_color, font=font)

# Save the image
image.save(os.path.join(output_dir, 'features.jpg'))