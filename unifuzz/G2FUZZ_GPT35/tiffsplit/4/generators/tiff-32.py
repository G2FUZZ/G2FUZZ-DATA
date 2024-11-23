import numpy as np
from PIL import Image

# Create a sample image data for multiple layers
image_data_layer1 = np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)
image_data_layer2 = np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)

# Set the resolution information (DPI) for the image
resolution_dpi = 300  # Setting resolution to 300 DPI

# Create PIL Image objects from the numpy arrays for each layer
image_layer1 = Image.fromarray(image_data_layer1)
image_layer2 = Image.fromarray(image_data_layer2)

# Create a new image with layers
multi_layer_image = Image.new('RGBA', (256, 256))
multi_layer_image.paste(image_layer1, (0, 0))

# Create a mask image from image_layer2
mask_image = Image.new('L', (256, 256))
mask_image.paste(image_layer2, (0, 0))

# Paste image_layer2 onto multi_layer_image with the mask
multi_layer_image.paste(image_layer2, (0, 0), mask=mask_image)

# Set the resolution metadata
multi_layer_image.info['dpi'] = (resolution_dpi, resolution_dpi)

# Set the image metadata
multi_layer_image.info['Image Metadata'] = 'Camera: Canon EOS 5D Mark IV, Lens: EF 24-70mm f/2.8L II USM, Location: New York City'

# Save the multi-layer image as a compressed TIFF file with resolution and metadata information
multi_layer_image.save('./tmp/sample_multi_layer_image.tiff', compression='tiff_adobe_deflate')

print("Multi-layer TIFF file containing complex file structures, resolution, and image metadata has been generated and saved.")