import numpy as np
from PIL import Image
from tifffile import TiffWriter

# Create different images with varied resolutions and color channels
image1 = np.random.randint(0, 255, size=(200, 200), dtype=np.uint8)  # Random image data
image2 = np.random.randint(0, 255, size=(150, 150, 3), dtype=np.uint8)  # Random color image data

# Define ICC profile data for both images (example data, replace with actual ICC profile data)
icc_profile_data = b'MyICCProfileData'

# Save the images as TIFF with multiple pages, geospatial metadata, and ICC profile
with TiffWriter("./tmp/multiple_pages_with_geospatial_and_icc_profiles.tiff") as tiff:
    tiff.save(image1, software='MyGISApp', metadata={'coordinate_system': 'WGS84'}, extratags=[(34675, 's', 1, icc_profile_data)])
    tiff.save(image2, software='MyGISApp', metadata={'coordinate_system': 'WGS84'}, extratags=[(34675, 's', 1, icc_profile_data)])