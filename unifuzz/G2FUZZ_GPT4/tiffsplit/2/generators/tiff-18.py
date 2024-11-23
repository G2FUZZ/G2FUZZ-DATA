import numpy as np
from PIL import Image, TiffImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an example image using numpy
image_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# Create and save the TIFF file with LZW compression
image = Image.fromarray(image_data)

# Defining rich text description
rich_text_description = "This is an example of TIFF with Rich Text Descriptions. Here you can include extensive annotations or metadata about the image content in a standardized format."

# Create an IFD (Image File Directory) object for TIFF tags
ifd = TiffImagePlugin.ImageFileDirectory_v2()

# Set the ImageDescription tag (tag number 270) with the rich text description
ifd[270] = rich_text_description

# Save with LZW compression and rich text description
# Note: The 'compression' parameter's value 'tiff_lzw' is corrected to 'lzw' which is the valid argument value for LZW compression.
image.save('./tmp/example_lzw_rich_text.tiff', compression='lzw', tiffinfo=ifd)

# Note: The TIFFTAG_IMAGEDESCRIPTION tag (270) is used to store the description. 
# While this example uses plain text for simplicity, incorporating rich text formatting 
# (such as HTML or Markdown) depends on the support of the application reading the TIFF files.