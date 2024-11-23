from PIL import Image, ImageDraw, ImageFont, TiffTags, TiffImagePlugin
import os
from datetime import datetime

# Ensure tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Create a new image with white background
img = Image.new('RGB', (800, 600), color=(255, 255, 255))

# Initialize ImageDraw
d = ImageDraw.Draw(img)

# Optionally, add some text to simulate a scanned document
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font = ImageFont.truetype(font_path, 30)
d.text((10,10), "This is a sample scanned document.", fill=(0,0,0), font=font)

# Save the image as a TIFF file
tiff_path = './tmp/sample_scanned_document_with_datetime_tags.tiff'

# Current datetime in "YYYY:MM:DD HH:MM:SS" format for TIFF DateTime tag
current_datetime = datetime.now().strftime("%Y:%m:%d %H:%M:%S")

# Prepare TIFF tags
# Note: The TIFF standard tag for DateTime is 306
info = TiffImagePlugin.ImageFileDirectory_v2()
info[306] = current_datetime  # DateTime tag

# Save the image with additional tags
img.save(tiff_path, "TIFF", tiffinfo=info)

print(f"TIFF file with DateTime tags saved at: {tiff_path}")