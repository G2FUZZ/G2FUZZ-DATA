import numpy as np
from PIL import Image
from tifffile import TiffWriter

# Create multiple images to store in the TIFF file
image1 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)
image2 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)

# Save the images as TIFF with multiple pages, geospatial metadata, image compression
with TiffWriter("./tmp/extended_tiff_file.tiff") as tiff:
    tiff.save(image1, description='First Image', software='MyGISApp', metadata={'coordinate_system': 'WGS84'}, compress='jpeg', photometric='minisblack', resolution=(300.0, 300.0))
    tiff.save(image2, description='Second Image', software='MyGISApp', metadata={'coordinate_system': 'WGS84'}, compress='deflate', photometric='miniswhite', resolution=(300.0, 300.0))