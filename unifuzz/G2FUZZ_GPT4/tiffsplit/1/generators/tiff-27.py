from PIL import Image, ImageEnhance
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate an RGB image with JPEG Compression, Subsampling (chroma subsampling), and Planar Configuration
rgb_image_subsampling = Image.new("RGB", (100, 100), (255, 255, 0))  # Yellow square
# When saving as JPEG with subsampling, specify subsampling as '4:2:0' (or another desired ratio)
# For TIFF with JPEG compression, the PIL library may not directly support setting subsampling via the save method's parameters.
# As a workaround, we first save the image as JPEG with subsampling and then read and save it as TIFF.
jpeg_temp_path = './tmp/temp_subsampling.jpg'
tiff_output_path = './tmp/rgb_image_subsampling.tiff'
# Save as JPEG with subsampling
rgb_image_subsampling.save(jpeg_temp_path, quality=95, subsampling=0)  # '0' corresponds to '4:2:0'
# Read the JPEG image
jpeg_image_with_subsampling = Image.open(jpeg_temp_path)

# Enhancing the image for HDR-like quality
# Note: True HDR support in TIFF files depends on the use of specific HDR formats that can store extended dynamic range data.
# This step enhances the contrast to simulate an HDR effect for demonstration purposes, as true HDR requires capturing or converting to an HDR format.
enhancer = ImageEnhance.Contrast(jpeg_image_with_subsampling)
hdr_image = enhancer.enhance(2.0)  # Increase contrast to simulate HDR effect

# Save the image as TIFF with Deflate Compression and Planar Configuration
hdr_image.save(tiff_output_path, compression="tiff_deflate", tiffinfo={317: 2})

# Clean up the temporary JPEG file
os.remove(jpeg_temp_path)