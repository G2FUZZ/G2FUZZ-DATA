import numpy as np
from PIL import Image
from tifffile import TiffWriter

# Create multiple images to store in the TIFF file
image1 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)
image2 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)

# Define ICC profile data (example data, replace with actual ICC profile data)
icc_profile_data = b'MyICCProfileData'

# Define resolution information
resolution_dpi = (300, 300)  # DPI (dots per inch) values

# Additional image with a different compression mode
image3 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)

# Save the images as TIFF with multiple pages, geospatial metadata, ICC profile, and resolution information
with TiffWriter("./tmp/multiple_pages_with_geospatial_icc_and_resolution.tiff") as tiff:
    tiff.save(image1, software='MyGISApp', metadata={'coordinate_system': 'WGS84'}, extratags=[(34675, 's', 1, icc_profile_data)], resolution=resolution_dpi)
    tiff.save(image2, software='MyGISApp', metadata={'coordinate_system': 'WGS84'}, extratags=[(34675, 's', 1, icc_profile_data)], resolution=resolution_dpi)
    
    # Save the third image with compression method 'deflate'
    tiff.save(image3, compression='deflate', software='MyGISApp', metadata={'coordinate_system': 'WGS84'}, extratags=[(34675, 's', 1, icc_profile_data)], resolution=resolution_dpi)