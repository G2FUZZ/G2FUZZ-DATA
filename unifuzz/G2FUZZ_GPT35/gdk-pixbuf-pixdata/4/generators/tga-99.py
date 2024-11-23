import numpy as np
import struct

def run_length_encode(data):
    encoded_data = []
    current_value = data[0]
    count = 1

    for i in range(1, len(data)):
        if data[i] == current_value:
            count += 1
        else:
            encoded_data.append((count, current_value))
            current_value = data[i]
            count = 1

    encoded_data.append((count, current_value))
    return encoded_data

def save_tga_file(filename, width, height, data, color_map=None, alpha_channel=None):
    with open(filename, 'wb') as f:
        # TGA header
        f.write(struct.pack('B', 0))  # ID length
        f.write(struct.pack('B', 1 if color_map else 0))  # Color map type
        if alpha_channel is not None and alpha_channel.any():
            f.write(struct.pack('B', 10))  # Image type (RLE compressed true-color image with alpha channel)
            pixel_depth = 32
            image_descriptor = 8
        else:
            f.write(struct.pack('B', 2))  # Image type (RLE compressed true-color image without alpha channel)
            pixel_depth = 24
            image_descriptor = 0
        f.write(struct.pack('<H', 0))  # Color map origin
        f.write(struct.pack('<H', 0))  # Color map length
        f.write(struct.pack('B', 0))  # Color map entry size
        f.write(struct.pack('<H', 0))  # X-origin
        f.write(struct.pack('<H', 0))  # Y-origin
        f.write(struct.pack('<H', width))  # Image width
        f.write(struct.pack('<H', height))  # Image height
        f.write(struct.pack('B', pixel_depth))  # Pixel depth
        f.write(struct.pack('B', image_descriptor))  # Image descriptor

        # Color map data
        if color_map:
            for color in color_map:
                f.write(struct.pack('BBB', *color))

        # Alpha channel data
        if alpha_channel is not None and alpha_channel.any():
            f.write(alpha_channel.tobytes())

        # Run-length encode data
        encoded_data = run_length_encode(data)

        for count, value in encoded_data:
            if count > 128:
                f.write(struct.pack('B', 128 + (count - 1)))
                f.write(struct.pack('B', value))
            else:
                f.write(struct.pack('B', count - 1))
                f.write(struct.pack('B', value))

# Generate sample data
width = 10
height = 10
data = np.random.randint(0, 256, (width * height))

# Generate color map
color_map = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Generate alpha channel
alpha_channel = np.random.randint(0, 256, (width * height))

# Save TGA file with run-length encoding, color map, and alpha channel
save_tga_file('./tmp/extended_sample.tga', width, height, data, color_map, alpha_channel)