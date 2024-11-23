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

# Text for the existing and new feature
text_1 = ("7. Wide Software Compatibility: JPG is one of the most widely supported image formats, compatible with virtually all "
          "image viewing and editing software, as well as web browsers.")
text_2 = ("10. Security Features: JPEG files can incorporate various security features, including watermarking and steganography, "
          "enabling the embedding of hidden information or copyright notices directly within the image data in a non-intrusive manner.")

# Create a blank image and get a drawing context
image = Image.new('RGB', (image_width, image_height), background_color)
draw = ImageDraw.Draw(image)

# Load a font
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    font = ImageFont.load_default()

# Function to draw text
def draw_text(draw, text, position_y, font, max_width):
    text_width, text_height = draw.textsize(text, font=font)
    text_x = (max_width - text_width) / 2
    draw.text((text_x, position_y), text, fill=text_color, font=font)
    return position_y + text_height + 20  # Return new Y position, add a little space between texts

# Draw the texts
y_position = 10  # Start a little bit from the top
y_position = draw_text(draw, text_1, y_position, font, image_width)
draw_text(draw, text_2, y_position, font, image_width)  # No need to catch the returned y_position as it's the last text

# Save the image
image.save(os.path.join(output_dir, 'feature_combined.jpg'))