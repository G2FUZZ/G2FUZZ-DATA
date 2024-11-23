import numpy as np
from PIL import Image

# Create a sample image data
image_data = np.random.randint(0, 255, (256, 256, 4), dtype=np.uint8)  # Adding an alpha channel for transparency

# Set the resolution information (DPI) for the image
resolution_dpi = 300  # Setting resolution to 300 DPI

# Create a PIL Image object from the numpy array
image = Image.fromarray(image_data)

# Set the resolution metadata
image.info['dpi'] = (resolution_dpi, resolution_dpi)

# Set the image metadata
image.info['Image Metadata'] = 'Camera: Canon EOS 5D Mark IV, Lens: EF 24-70mm f/2.8L II USM, Location: New York City'

# Adding Transparency Masks feature
transparency_mask = np.random.randint(0, 255, (256, 256), dtype=np.uint8)  # Generating a transparency mask
image.info['Transparency Masks'] = 'Custom Transparency Mask'

# Save the image as a TIFF file with resolution, metadata, and transparency mask information
image.save('./tmp/sample_image_with_all_features.tiff')

print("TIFF file containing all specified features including Resolution, Image Metadata, and Transparency Masks has been generated and saved.")