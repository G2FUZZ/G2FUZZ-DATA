import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with white background
img = Image.new('RGB', (800, 400), color='white')  # Adjust height to accommodate additional text

# Initialize the drawing context
draw = ImageDraw.Draw(img)

# Define the text to be drawn including the new feature
text = """
6. Flexibility through Tags: The format uses a flexible, tag-based structure,
enabling TIFF to support a wide range of image types, resolutions, and color depths,
making it highly adaptable to various imaging needs.

9. Spot Colors Support: TIFF files can support spot colors, used in printing to ensure accurate reproduction of specific colors that cannot be achieved through the standard CMYK color process alone.
"""

# Load a font
font = ImageFont.load_default()

# Position for the text
text_x, text_y = 10, 10

# Apply text onto the image using the correct variables for position
draw.text((text_x, text_y), text, fill="black", font=font)

# Save the image as TIFF with a new name to reflect the added feature
img.save('./tmp/flexibility_spot_colors_support.tiff')