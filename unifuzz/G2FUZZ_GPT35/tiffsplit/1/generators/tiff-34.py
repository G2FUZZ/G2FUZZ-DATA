import numpy as np
from tifffile import TiffWriter

# Create a 100x100 RGBA image with random values
data = np.random.randint(0, 255, (100, 100, 4), dtype=np.uint8)

# Save the image with alpha channel as a TIFF file with compression, photometric interpretation, tiling, and ICC profile
with TiffWriter('./tmp/alpha_channel_complex.tiff') as tiff:
    tiff.save(data, compress='deflate', photometric='rgb', tile=(64, 64), extratags=[(34675, 's', 1, b'MyICCProfileData')])