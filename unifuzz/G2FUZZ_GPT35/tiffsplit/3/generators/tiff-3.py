import numpy as np
from PIL import Image

# Create a 3-layer image
width, height = 256, 256
num_layers = 3

for layer_num in range(num_layers):
    # Generate a random image for each layer
    image_data = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
    image = Image.fromarray(image_data, 'RGB')
    
    # Save each layer as a separate TIFF file
    image.save(f'./tmp/layer_{layer_num + 1}.tiff')