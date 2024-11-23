import numpy as np
import os
import json
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a layered image data structure
def generate_layered_image_data(layers_info, width=256, height=256):
    layers_data = []
    for layer_info in layers_info:
        bit_depth = layer_info['bit_depth']
        max_val = 2**bit_depth - 1
        alpha_channel = layer_info.get('alpha_channel', False)
        
        # Generate a gradient image for this layer
        gradient = np.tile(np.linspace(0, max_val, width, dtype=np.uint16), (height, 1))
        if alpha_channel:
            # If the layer includes an alpha channel, we add it as a fully opaque channel
            alpha = np.full((height, width), max_val, dtype=np.uint16)
            layer_data = np.stack([gradient, alpha], axis=-1)
        else:
            layer_data = gradient
        
        layers_data.append(layer_data)
    
    return layers_data

# Function to save layers data to a pixdata file
def save_pixdata_file(filename, layers_data, metadata):
    with open(filename, 'wb') as f:
        # Write metadata as JSON, followed by a separator
        metadata_str = json.dumps(metadata)
        f.write(metadata_str.encode('utf-8'))
        f.write(b'\n---\n')  # Separator between metadata and image data
        
        # Write each layer's data
        for layer_data in layers_data:
            np.save(f, layer_data)

# Define layers with bit depth and optional alpha channel
layers_info = [
    {'bit_depth': 8, 'alpha_channel': False},
    {'bit_depth': 16, 'alpha_channel': True},
    {'bit_depth': 24, 'alpha_channel': False}  # 24-bit will be treated as 16-bit with RGB channels but without alpha for simplicity
]

# Generate the layered image data
layers_data = generate_layered_image_data(layers_info)

# Metadata for the pixdata file
metadata = {
    'description': 'Example layered image file',
    'layers': len(layers_info),
    'width': 256,
    'height': 256,
    'layers_info': layers_info
}

# Save the pixdata file
save_pixdata_file('./tmp/complex_image.pixdata', layers_data, metadata)
print("Saved complex_image.pixdata")