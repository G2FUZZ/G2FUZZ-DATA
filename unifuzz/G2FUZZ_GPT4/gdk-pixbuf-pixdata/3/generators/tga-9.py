import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Text to be drawn
text = """
9. **Versatility in Application**: Due to their high quality and support for transparency, TGA files are widely used in various industries, including video game development, professional video editing, and graphic design.
"""

# Create a new blank image with a white background
image = Image.new('RGBA', (800, 400), (255, 255, 255, 255))

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Define a font (default PIL font, might not support bold or markdown formatting)
try:
    # Trying to use a nicer font if available
    font = ImageFont.truetype("arial.ttf", 16)
except IOError:
    # Fallback to the default PIL font if the above font is not available
    font = ImageFont.load_default()

# Draw the text onto the image
draw.multiline_text((10, 10), text, fill=(0, 0, 0), font=font)

# Save the image as a TGA file
image.save('./tmp/versatility_in_application.tga')