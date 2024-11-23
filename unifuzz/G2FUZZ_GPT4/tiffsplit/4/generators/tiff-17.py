import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with white background
img = Image.new('RGB', (800, 400), color='white')  # Adjusted the canvas size to accommodate more text

# Initialize the drawing context
draw = ImageDraw.Draw(img)

# Define the text to be drawn, including the new feature description
text = """
6. Flexibility through Tags: The format uses a flexible, tag-based structure,
enabling TIFF to support a wide range of image types, resolutions, and color depths,
making it highly adaptable to various imaging needs.

7. BigTIFF Extension: For addressing the limitations of the original 32-bit TIFF format,
the BigTIFF extension allows TIFF files to exceed the 4 GB size limit and supports 64-bit
offsets, accommodating very large images and datasets.
"""

# Load a font
font = ImageFont.load_default()

# Position for the text
text_x, text_y = 10, 10

# Apply text onto the image using the correct variables for position
draw.text((text_x, text_y), text, fill="black", font=font)

# Save the image as TIFF
img.save('./tmp/extended_features.tiff')