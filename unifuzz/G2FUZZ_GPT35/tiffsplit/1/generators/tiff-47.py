import numpy as np
from PIL import Image
from tifffile import TiffWriter

# Create multiple images with alpha channel to store in the TIFF file
image1 = np.random.randint(0, 255, size=(100, 100, 4), dtype=np.uint8)
image2 = np.random.randint(0, 255, size=(100, 100, 4), dtype=np.uint8)

# Save the images as TIFF with multiple layers, alpha channel, tiled storage, and custom tags
metadata1 = {'coordinate_system': 'WGS84', 'Author': 'John Doe'}
metadata2 = {'coordinate_system': 'WGS84', 'Author': 'Jane Smith'}

with TiffWriter("./tmp/extended_tiff_file.tiff") as tiff:
    tiff.save(image1, description='First Image', software='MyGISApp', metadata=metadata1, compress='jpeg', photometric='minisblack', resolution=(300.0, 300.0), tile=(64, 64))
    tiff.save(image2, description='Second Image', software='MyGISApp', metadata=metadata2, compress='deflate', photometric='minisblack', resolution=(300.0, 300.0), tile=(64, 64))