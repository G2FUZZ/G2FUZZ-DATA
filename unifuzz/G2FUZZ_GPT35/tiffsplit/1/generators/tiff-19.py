import numpy as np
from PIL import Image
from tifffile import TiffWriter

# Create a random image data with 8-bit depth
data = np.random.randint(0, 256, (256, 256), dtype=np.uint8)
image = Image.fromarray(data)

# Add transparency to the image by creating an alpha channel with random values
alpha = np.random.randint(0, 256, (256, 256), dtype=np.uint8)
data_with_transparency = np.dstack((data, alpha))
image_with_transparency = Image.fromarray(data_with_transparency)

# Save the image as a TIFF file with transparency, extensibility, and compatibility feature
with TiffWriter("./tmp/8bit_depth_with_transparency_and_extensibility_and_compatibility.tiff") as tif:
    tif.save(data_with_transparency, software='MyCustomSoftware', description='Example TIFF with Extensibility and Compatibility: TIFF files are widely supported by various image editing and viewing software, ensuring interoperability across different platforms and applications.')