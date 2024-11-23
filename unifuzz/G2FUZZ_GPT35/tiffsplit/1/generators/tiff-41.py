import numpy as np
from tifffile import TiffWriter

# Create multiple pages of 100x100 RGBA images with random values
num_pages = 3
data = [np.random.randint(0, 255, (100, 100, 4), dtype=np.uint8) for _ in range(num_pages)]

# Save the images as multiple pages in a single TIFF file with custom metadata
with TiffWriter('./tmp/multi_page_complex.tiff') as tiff:
    for i, page_data in enumerate(data):
        metadata = {'PageNumber': i+1, 'Description': f'Page {i+1}'}
        tiff.save(page_data, description=f'Page {i+1}', extratags=[(33432, 's', len(metadata), str(metadata).encode())])