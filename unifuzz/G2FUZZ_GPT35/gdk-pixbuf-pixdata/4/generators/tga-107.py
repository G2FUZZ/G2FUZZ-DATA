import numpy as np
import struct

def create_image_layer(width, height, pixel_depth):
    return np.random.randint(0, 256, (width * height, pixel_depth // 8))

def run_length_encode(layer):
    encoded_data = []
    current_count = 1
    current_value = layer[0]

    for i in range(1, len(layer)):
        if np.array_equal(layer[i], current_value):
            current_count += 1
        else:
            encoded_data.append((current_count, current_value))
            current_count = 1
            current_value = layer[i]

    encoded_data.append((current_count, current_value))

    return encoded_data

def save_tga_file_extended(filename, width, height, layers):
    with open(f'./tmp/{filename}', 'wb') as f:
        # TGA header
        f.write(struct.pack('B', 0))  # ID length
        f.write(struct.pack('B', 0))  # No color map
        f.write(struct.pack('B', 10))  # Image type (RLE compressed true-color image with alpha channel)
        f.write(struct.pack('<H', 0))  # Color map origin
        f.write(struct.pack('<H', 0))  # Color map length
        f.write(struct.pack('B', 0))  # Color map entry size
        f.write(struct.pack('<H', 0))  # X-origin
        f.write(struct.pack('<H', 0))  # Y-origin
        f.write(struct.pack('<H', width))  # Image width
        f.write(struct.pack('<H', height))  # Image height
        f.write(struct.pack('B', 32))  # Pixel depth
        f.write(struct.pack('B', 8))  # Image descriptor

        # Save each image layer
        for layer in layers:
            encoded_data = run_length_encode(layer)

            for count, value in encoded_data:
                if count > 128:
                    f.write(struct.pack('B', 128 + (count - 1)))
                    f.write(struct.pack('B', *value))
                else:
                    f.write(struct.pack('B', count - 1))
                    for v in value:
                        f.write(struct.pack('B', v))

# Generate sample data
width = 10
height = 10
num_layers = 3
layers = [create_image_layer(width, height, 24), create_image_layer(width, height, 32), create_image_layer(width, height, 16)]

# Save TGA file with multiple image layers
save_tga_file_extended('extended_complex_sample.tga', width, height, layers)