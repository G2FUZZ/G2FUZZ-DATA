import numpy as np
from PIL import Image
from tifffile import TiffWriter

# Create multiple images to store in the TIFF file
image1 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)
image2 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)

# Save the images as TIFF with multiple pages and custom tags
with TiffWriter("./tmp/multiple_pages_custom_tags.tiff") as tiff:
    tiff.save(image1, software='MyCustomSoftware', description='First Image')
    tiff.save(image2, software='MyCustomSoftware', description='Second Image')