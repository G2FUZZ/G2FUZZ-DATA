from PIL import Image, TiffImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image for demonstration (e.g., 100x100 pixels, red)
width, height = 100, 100
color = (255, 0, 0, 255)  # Red color in RGBA format
image = Image.new("RGBA", (width, height), color)

# Choose compression - for demonstration, we use 'tiff_adobe_deflate' (ZIP compression)
compression = 'tiff_adobe_deflate'

# Prepare the info dictionary to include the compression
info = {
    "compression": compression,
    # Add other tags as needed here, but note the limitation regarding direct support for custom tags
}

# Save the image with specified compression
image.save('./tmp/geospatial_metadata_with_compression_and_sample_format.tif', "TIFF", **info)

print(f"Saved geospatial TIFF with Compression Algorithm Negotiation to ./tmp/geospatial_metadata_with_compression_and_sample_format.tif")