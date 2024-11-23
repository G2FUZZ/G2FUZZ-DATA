from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

# Ensure tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Create a new image with white background
# For Multi-spectral/Hyperspectral, assume we're storing 4 channels (RGBA) for simplicity. Real applications may have more.
channels = 4  # Simulate multi-spectral data (e.g., RGB + Near-Infrared)
width, height = 800, 600
img = np.zeros((height, width, channels), dtype=np.uint8)
img.fill(255)  # Fill the image with white pixels

# Convert numpy array to PIL Image
img = Image.fromarray(img)

# Initialize ImageDraw
d = ImageDraw.Draw(img)

# Optionally, add some text to simulate a scanned document
# In a real scenario, you would have an actual document image
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font = ImageFont.truetype(font_path, 30)
d.text((10,10), "This is a sample scanned document with Multi-spectral and Hyperspectral Data Storage.", fill=(0,0,0,255), font=font)

# Save the image as a TIFF file
tiff_path = './tmp/sample_multispectral_document.tiff'
img.save(tiff_path, "TIFF")

print(f"TIFF file saved at: {tiff_path}")

# Note on OCR and Multi-spectral/Hyperspectral Data:
# Applying OCR to the TIFF file to embed text layers or annotations is typically done with OCR tools like Tesseract.
# For Multi-spectral and Hyperspectral data, the process involves capturing images across various wavelengths beyond
# visible light and potentially using specialized software for analysis. This example simplifies the concept by using
# an RGBA image to simulate additional channels.