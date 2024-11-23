import numpy as np
from tifffile import TiffWriter

# Create multiple images to store in the TIFF file
image1 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)
image2 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)

# Define ICC profile data (example data, replace with actual ICC profile data)
icc_profile_data = b'MyICCProfileData'

# Save the images as TIFF with multiple layers, tiled organization, and Deflate compression
with TiffWriter("./tmp/complex_tiff_file.tiff") as tiff:
    tiff.save(image1, compress='deflate', photometric='rgb', tile=(64, 64), extratags=[(34675, 's', 1, icc_profile_data)])
    tiff.save(image2, compress='deflate', photometric='rgb', tile=(64, 64), extratags=[(34675, 's', 1, icc_profile_data)])