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
d.text((10, 10), "This is a sample scanned document.", fill=(0, 0, 0), font=font)

# Add a description of Sample Format feature
d.text((10, 50), "Sample Format: TIFF supports unsigned int, signed int, float, and undefined formats.", fill=(0, 0, 0), font=font)

# Add a description of Halftone Hints feature
d.text((10, 100), "7. Halftone Hints: TIFF files can contain halftone hints, which provide information about the halftoning screens used when converting continuous-tone images into halftone images for printing.", fill=(0, 0, 0), font=font)

# Add a description of SubIFDs feature
d.text((10, 250), "12. SubIFDs: TIFF files can include SubIFDs (Sub Image File Directories) for storing additional images within the same file, such as thumbnails or alternative image representations, in a structured manner.", fill=(0, 0, 0), font=font)

# Save the image as a TIFF file with additional metadata to simulate the "SubIFDs" feature
tiff_path = './tmp/sample_scanned_document_with_subifds.tiff'
# Creating a second image (e.g., a thumbnail) to store in SubIFDs
thumb_img = img.resize((200, 150))
# PIL does not support writing SubIFDs directly, so we simulate it by saving a second image.
# In a real scenario, specialized libraries or modifications to the file are required to embed SubIFDs.
thumb_path = './tmp/thumbnail.tiff'
thumb_img.save(thumb_path, "TIFF")

img.save(tiff_path, "TIFF")

print(f"TIFF file with 'SubIFDs' feature simulated by including a separate thumbnail file saved at: {tiff_path}")
print(f"Thumbnail (simulated SubIFD) saved at: {thumb_path}")

# Note on OCR, Halftone Hints, and SubIFDs:
# The "Halftone Hints" and "SubIFDs" features described here are simulated by adding text to the image.
# Actual halftone hints and SubIFDs would be part of the metadata or specific configurations within a TIFF file.
# This script does not embed real halftone hints or SubIFDs but simulates the inclusion of such features through descriptive text and a separate thumbnail image.