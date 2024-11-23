from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image for demonstration (e.g., 100x100 pixels, red)
width, height = 100, 100
color = (255, 0, 0, 255)  # Red color in RGBA format
image = Image.new("RGBA", (width, height), color)

# The TIFF format allows for various types of metadata to be embedded within the file.
# In addition, we're including the Compression Algorithm Negotiation
# For simplicity, we'll choose a compression method, but in a real scenario, this could be
# more dynamic, based on the desired optimization for file size or image quality.

# Choose compression - for demonstration, we use 'tiff_adobe_deflate' (ZIP compression)
# For Fax compression, you could use 'tiff_ccitt' which represents CCITT Group 3 or 4 fax compression
# Note: The actual negotiation or choice of compression would depend on further logic
compression = 'tiff_adobe_deflate'  # Choose appropriate compression based on requirements

geospatial_tiff_file_with_compression = './tmp/geospatial_metadata_with_compression.tif'
image.save(geospatial_tiff_file_with_compression, format='TIFF', compression=compression)

print(f"Saved geospatial TIFF with Compression Algorithm Negotiation to {geospatial_tiff_file_with_compression}")