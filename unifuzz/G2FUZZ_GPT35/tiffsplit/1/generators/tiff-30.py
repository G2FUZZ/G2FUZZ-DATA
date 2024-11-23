import numpy as np
from PIL import Image
from tifffile import TiffWriter

# Create multiple images with transparency to store in the TIFF file
image1 = np.random.randint(0, 255, size=(100, 100, 4), dtype=np.uint8)  # RGBA image
image1[:, :, 3] = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)  # Set transparency values

image2 = np.random.randint(0, 255, size=(100, 100, 4), dtype=np.uint8)  # RGBA image
image2[:, :, 3] = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)  # Set transparency values

# Define ICC profile data (example data, replace with actual ICC profile data)
icc_profile_data = b'MyICCProfileData'

# Define resolution information
resolution_dpi = (300, 300)  # DPI (dots per inch) values

# Tiled storage configuration
tile_size = (64, 64)  # Tiled storage size

# Save the images as TIFF with multiple layers, transparency, geospatial metadata, ICC profile, and resolution information
with TiffWriter("./tmp/multiple_layers_with_transparency_and_geospatial_icc_resolution.tiff") as tiff:
    tiff.tile = tile_size  # Set the tile size
    tiff.save(image1, software='MyGISApp', metadata={'coordinate_system': 'WGS84'}, extratags=[(34675, 's', 1, icc_profile_data)], resolution=resolution_dpi)
    tiff.save(image2, software='MyGISApp', metadata={'coordinate_system': 'WGS84'}, extratags=[(34675, 's', 1, icc_profile_data)], resolution=resolution_dpi)