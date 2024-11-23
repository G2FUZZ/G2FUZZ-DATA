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

# Save the image as a TIFF file
tiff_path = './tmp/sample_scanned_document.tiff'
img.save(tiff_path, "TIFF")

print(f"TIFF file saved at: {tiff_path}")

# Note on OCR:
# Applying OCR to the TIFF file to embed text layers or annotations is typically done with OCR tools like Tesseract.
# This process involves reading the image, performing OCR, and then using the OCR output in a meaningful way.
# Embedding the OCR results directly back into the TIFF as a text layer or annotation is non-standard and would
# require a specific approach depending on the use case and software ecosystem.