import numpy as np
import struct

# Generate random image data
image_data = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)

# Additional metadata for the image
metadata = {
    'width': 100,
    'height': 100,
    'channels': 3,
    'created_by': 'Your Name',
    'date_created': '2022-12-31'
}

# Additional layers for the image
num_layers = 2
layer_data = [np.random.randint(0, 255, size=(100, 100), dtype=np.uint8) for _ in range(num_layers)]

# Pack metadata into a binary string
metadata_str = '\n'.join([f"{key}: {value}" for key, value in metadata.items()])
metadata_bytes = metadata_str.encode()

# Save image data, metadata, and layers to a '.pgx' file
file_path = './tmp/complex_image_data_with_layers.pgx'
with open(file_path, 'wb') as file:
    # Write metadata length as 4-byte integer followed by metadata
    file.write(struct.pack('I', len(metadata_bytes)))
    file.write(metadata_bytes)
    
    # Write number of layers as a 4-byte integer
    file.write(struct.pack('I', num_layers))
    
    # Write image data
    file.write(image_data.tobytes())
    
    # Write each layer
    for layer in layer_data:
        file.write(layer.tobytes())

print(f"Complex Image data with layers saved to '{file_path}' successfully.")