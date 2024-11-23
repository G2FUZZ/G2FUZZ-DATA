import numpy as np
from PIL import Image

# Create a sample image data
image_data = np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)

# Set the resolution information (DPI) for the image
resolution_dpi = 300  # Setting resolution to 300 DPI

# Create a PIL Image object from the numpy array
image = Image.fromarray(image_data)

# Set the resolution metadata
image.info['dpi'] = (resolution_dpi, resolution_dpi)

# Save the image as a TIFF file with resolution information
image.save('./tmp/sample_image_with_resolution.tiff')

print("TIFF file containing the specified feature including Resolution has been generated and saved.")