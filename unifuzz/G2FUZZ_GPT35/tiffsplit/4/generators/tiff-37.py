import numpy as np
from PIL import Image, ImageSequence

# Define bit depth (e.g., 16-bit per channel for higher precision)
bit_depth = 16

# Generate multiple image layers with different patterns
image_data_layer1 = np.random.randint(0, 2**bit_depth, size=(256, 256), dtype=np.uint16)
image_data_layer2 = np.random.randint(0, 2**bit_depth, size=(256, 256), dtype=np.uint16)

# Create images from the layers
image_layer1 = Image.fromarray(image_data_layer1)
image_layer2 = Image.fromarray(image_data_layer2)

# Add metadata to the images
image_layer1.info['Description'] = 'First Image Layer'
image_layer2.info['Description'] = 'Second Image Layer'

# Create a multi-layer TIFF file
multi_layer_image = Image.new('RGB', (256, 256))
multi_layer_image.putdata(image_layer1.getdata())
multi_layer_image.putdata(image_layer2.getdata())

# Save the multi-layer TIFF file with metadata
multi_layer_image.save('./tmp/multi_layer_tiff_example.tiff')