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

# Save the image as a TIFF file with additional metadata to simulate the "Sample Format" feature
# Note: The PIL library does not support direct embedding of arbitrary metadata in TIFF tags related to sample formats.
# However, we can simulate adding a feature description through image content or comments.
tiff_path = './tmp/sample_scanned_document_with_feature.tiff'
img.save(tiff_path, "TIFF")

print(f"TIFF file with 'Sample Format' feature saved at: {tiff_path}")

# Note on OCR and Sample Format:
# The "Sample Format" feature described here is simulated by adding text to the image.
# In practical terms, handling different sample formats (e.g., for scientific imaging or complex document management systems)
# would involve more nuanced data management and possibly different software libraries or systems tailored to those needs.