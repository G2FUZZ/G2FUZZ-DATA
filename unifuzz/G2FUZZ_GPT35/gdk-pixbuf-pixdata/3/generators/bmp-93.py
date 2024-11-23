import numpy as np
from PIL import Image

# Create a 100x100 RGB image with a custom color palette
palette = np.array([[255, 0, 0], [0, 255, 0], [0, 0, 255]], dtype=np.uint8)
image_rgb_custom = np.random.randint(0, 3, (100, 100), dtype=np.uint8)
image_rgb_custom = Image.fromarray(palette[image_rgb_custom], 'RGB')
image_rgb_custom.save('./tmp/rgb_custom_image.bmp')

# Create a 100x100 image with multiple layers (RGB and grayscale)
image_layers = np.zeros((100, 100, 4), dtype=np.uint8)
image_layers[:, :, :3] = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)  # RGB layer
image_layers[:, :, 3] = np.random.randint(0, 256, (100, 100), dtype=np.uint8)  # Alpha (grayscale) layer
image_layers = Image.fromarray(image_layers, 'RGBA')
image_layers.save('./tmp/layers_image.bmp')