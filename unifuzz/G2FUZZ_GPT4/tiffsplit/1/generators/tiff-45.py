from PIL import Image, TiffTags, TiffImagePlugin
import os

# Ensure tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Helper function to generate resolution info
def generate_res_info(dpi):
    # Convert DPI to TIFF resolution unit (pixels per inch to pixels per centimeter)
    res = dpi * 2.54 / 10
    return (int(res), int(res))

# Create a simple image with updated dimensions and DPI
image = Image.new('RGB', (200, 200), color='blue')  # Updated dimensions
image_res = generate_res_info(300)  # 300 DPI

# Prepare metadata with more complex structures and information
info = TiffImagePlugin.ImageFileDirectory_v2()

# Adding more metadata fields with updated structure
info[282] = image_res  # XResolution tag number is 282, now using the helper function
info[283] = image_res  # YResolution tag number is 283, now using the helper function
info[296] = 2  # ResolutionUnit tag number is 296, 2 stands for inches
info[270] = 'Copyright 2023, Example Corp. with Enhanced Metadata'  # Updated description
info[315] = "Python PIL"  # Artist tag number is 315
info[305] = "Pillow"  # Software tag number is 305

# Save the TIFF with updated metadata
image.save('./tmp/enhanced_example_with_metadata.tif', tiffinfo=info, dpi=[image_res, image_res])