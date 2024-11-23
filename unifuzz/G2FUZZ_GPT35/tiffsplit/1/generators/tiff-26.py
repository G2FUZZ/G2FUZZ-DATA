import numpy as np
from PIL import Image
from tifffile import TiffWriter

# Create multiple images to store in the TIFF file
image1 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)
image2 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)

# Define ICC profile data (example data, replace with actual ICC profile data)
icc_profile_data = b'MyICCProfileData'

# Define OCR text data
ocr_text = "Sample OCR text for searchable and selectable text within scanned documents."

# Save the images as TIFF with multiple pages, geospatial metadata, ICC profile, and OCR text
with TiffWriter("./tmp/multiple_pages_with_geospatial_icc_ocr.tiff") as tiff:
    tiff.save(image1, software='MyGISApp', metadata={'coordinate_system': 'WGS84'}, extratags=[(34675, 's', 1, icc_profile_data)], description=ocr_text)
    tiff.save(image2, software='MyGISApp', metadata={'coordinate_system': 'WGS84'}, extratags=[(34675, 's', 1, icc_profile_data)], description=ocr_text)