import numpy as np
from PIL import Image
from tifffile import TiffWriter

# Create multiple images to store in the TIFF file
image1 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)
image2 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)

# Save the images as TIFF with multiple pages, geospatial metadata, digital signatures, and image editing capabilities
with TiffWriter("./tmp/multiple_pages_with_geospatial_and_digital_signatures_and_editing_capabilities.tiff") as tiff:
    tiff.save(image1, software='MyGISApp', metadata={'coordinate_system': 'WGS84', 'digital_signatures': 'Signature1', 'image_editing_capabilities': 'Adjustment Layers, Masks, Filters'})
    tiff.save(image2, software='MyGISApp', metadata={'coordinate_system': 'WGS84', 'digital_signatures': 'Signature2', 'image_editing_capabilities': 'Adjustment Layers, Masks, Filters'})