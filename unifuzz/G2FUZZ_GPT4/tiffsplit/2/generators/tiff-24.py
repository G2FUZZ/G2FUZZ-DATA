import numpy as np
from PIL import Image, TiffImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an example image using numpy
image_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# Create and save the TIFF file with LZW compression
image = Image.fromarray(image_data)

# Defining rich text description with HDR support
rich_text_description = """
This is an example of TIFF with Rich Text Descriptions. Here you can include extensive annotations or metadata about the image content in a standardized format.
10. HDR Support: High Dynamic Range (HDR) imaging is supported in TIFF, allowing for a greater range of luminosity than what is possible with standard digital imaging techniques.
"""

# Create an IFD (Image File Directory) object for TIFF tags
ifd = TiffImagePlugin.ImageFileDirectory_v2()

# Set the ImageDescription tag (tag number 270) with the rich text description
ifd[270] = rich_text_description

# Save with LZW compression and rich text description
image.save('./tmp/example_lzw_rich_text_hdr.tiff', compression='lzw', tiffinfo=ifd)