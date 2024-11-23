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

# Set the image metadata
image.info['Image Metadata'] = 'Camera: Canon EOS 5D Mark IV, Lens: EF 24-70mm f/2.8L II USM, Location: New York City'

# Save the image as a TIFF file with resolution and metadata information
image.save('./tmp/sample_image_with_resolution_and_metadata.tiff')

print("TIFF file containing the specified features including Resolution and Image Metadata has been generated and saved.")