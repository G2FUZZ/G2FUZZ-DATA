from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image for demonstration (e.g., 100x100 pixels, red)
width, height = 100, 100
color = (255, 0, 0, 255)  # Red color in RGBA format
image = Image.new("RGBA", (width, height), color)

# The TIFF format allows for various types of metadata to be embedded within the file.
geospatial_tiff_file = './tmp/geospatial_metadata.tif'
image.save(geospatial_tiff_file, format='TIFF')

print(f"Saved geospatial TIFF to {geospatial_tiff_file}")