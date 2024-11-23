from PIL import Image, ImageDraw, ImageFont
import os

# Ensure tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Create a new image with white background
img = Image.new('RGB', (800, 600), color=(255, 255, 255))

# Initialize ImageDraw
d = ImageDraw.Draw(img)

# Optionally, add some text to simulate a scanned document
# In a real scenario, you would have an actual document image
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font = ImageFont.truetype(font_path, 30)
d.text((10,10), "This is a sample scanned document.", fill=(0,0,0), font=font)

# Add a description of Sample Format feature
d.text((10, 50), "Sample Format: TIFF supports unsigned int, signed int, float, and undefined formats.", fill=(0,0,0), font=font)

# Add a description of Halftone Hints feature
d.text((10, 100), "7. Halftone Hints: TIFF files can contain halftone hints, which provide information about the halftoning screens used when converting continuous-tone images into halftone images for printing.", fill=(0,0,0), font=font)

# Save the image as a TIFF file with additional metadata to simulate the "Halftone Hints" feature
tiff_path = './tmp/sample_scanned_document_with_halftone_hints.tiff'
img.save(tiff_path, "TIFF")

print(f"TIFF file with 'Halftone Hints' feature saved at: {tiff_path}")

# Note on OCR and Halftone Hints:
# The "Halftone Hints" feature described here is simulated by adding text to the image.
# Actual halftone hints would be part of the metadata or specific configurations within a TIFF file.
# This script does not embed real halftone hints but simulates the inclusion of such a feature through descriptive text.