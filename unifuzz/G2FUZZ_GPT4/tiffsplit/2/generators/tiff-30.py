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

# Save the image as a TIFF file with Planar Configuration
tiff_path = './tmp/sample_scanned_document_with_planar_configuration.tiff'

# Note on Planar Configuration:
# The PIL library does not directly expose an interface to set the Planar Configuration at the time of saving a TIFF.
# However, for demonstration, we will save it normally and acknowledge that the desired configuration
# would typically be handled by specifying additional parameters or using a lower-level library that allows
# direct manipulation of TIFF tags if necessary.

# For this example, we save without explicit planar configuration, acknowledging the limitation.
img.save(tiff_path, "TIFF")

print(f"TIFF file saved at: {tiff_path}")

# Following this, to actually apply a planar configuration, one would likely need to use a more specialized
# library or tool that allows for direct manipulation of TIFF metadata and structure, such as libtiff or
# a similar library capable of dealing with such specifics.