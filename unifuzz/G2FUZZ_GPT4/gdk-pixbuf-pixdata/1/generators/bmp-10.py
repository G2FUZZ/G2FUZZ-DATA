from PIL import Image
from PIL import PngImagePlugin
import datetime
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a new image with a solid color (e.g., red)
image = Image.new('RGB', (100, 100), 'red')

# Add basic metadata
meta = PngImagePlugin.PngInfo()
meta.add_text("Author", "John Doe")
meta.add_text("Software", "Pillow")
meta.add_text("Creation Time", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Saving the image as BMP does not support the standard metadata fields as PNG or JPEG
# This is a workaround to include some basic info in the filename or consider another way to store metadata
filename = 'image_with_metadata.bmp'
filepath = os.path.join(output_dir, filename)

# Save the image
image.save(filepath)

print(f"Image saved at {filepath}")