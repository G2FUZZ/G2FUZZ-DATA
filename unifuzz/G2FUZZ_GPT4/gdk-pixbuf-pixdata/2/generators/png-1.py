import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Image size and background color
img_size = (600, 200)
background_color = 'white'

# Create a new image with a white background
image = Image.new('RGB', img_size, background_color)

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Define the text to be drawn and font properties
text = """
Lossless Compression: PNG uses a lossless compression algorithm,
meaning that it compresses image data without losing any information.
This allows for high-quality images that are fully restorable to their original form.
"""
font_size = 14
try:
    # This will work on many systems. Adjust the path if you have a specific font in mind
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    # Fallback to a default font if the preferred font is not available
    font = ImageFont.load_default()

# Text position
text_position = (10, 10)

# Drawing the text on the image
draw.multiline_text(text_position, text, fill="black", font=font)

# Save the image
output_file_path = os.path.join(output_dir, 'lossless_compression_demo.png')
image.save(output_file_path, 'PNG')

print(f"Image saved to {output_file_path}")