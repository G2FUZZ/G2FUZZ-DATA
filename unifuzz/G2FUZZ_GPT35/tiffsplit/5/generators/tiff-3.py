import numpy as np
from PIL import Image

# Create a blank white image
width, height = 200, 200
white_image = Image.new('RGB', (width, height), 'white')

# Add layers to the image
num_layers = 3
for i in range(num_layers):
    layer = Image.new('RGB', (width, height), (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256)))
    white_image.paste(layer, (0, 0))

# Save the image as a TIFF file
output_path = './tmp/multi_layer_image.tiff'
white_image.save(output_path)