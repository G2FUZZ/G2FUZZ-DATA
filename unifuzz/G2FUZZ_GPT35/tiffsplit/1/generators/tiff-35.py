import numpy as np
from tifffile import TiffWriter

# Create multiple images to store in the TIFF file
image1 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)
image2 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)

# Define ICC profile data (example data, replace with actual ICC profile data)
icc_profile_data = b'MyICCProfileData'

# Define custom resolution tags (example data, replace with actual resolution values)
resolution_tags = [(282, 'I', 2, 300), (283, 'I', 2, 300)]  # XResolution, YResolution

# Save the images as TIFF with multiple layers, tiled organization, Deflate compression, and custom resolution tags
with TiffWriter("./tmp/complex_tiff_file.tiff") as tiff:
    tiff.save(image1, compress='deflate', photometric='rgb', tile=(64, 64), extratags=[(34675, 's', 1, icc_profile_data)] + resolution_tags)
    tiff.save(image2, compress='deflate', photometric='rgb', tile=(64, 64), extratags=[(34675, 's', 1, icc_profile_data)] + resolution_tags)