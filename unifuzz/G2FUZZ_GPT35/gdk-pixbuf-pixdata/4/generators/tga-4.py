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

def save_tga_file(filename, width, height, data):
    with open(filename, 'wb') as f:
        # TGA header
        f.write(struct.pack('B', 0))  # ID length
        f.write(struct.pack('B', 0))  # Color map type
        f.write(struct.pack('B', 10))  # Image type (RLE compressed true-color image)
        f.write(struct.pack('<H', 0))  # Color map origin
        f.write(struct.pack('<H', 0))  # Color map length
        f.write(struct.pack('B', 0))  # Color map entry size
        f.write(struct.pack('<H', 0))  # X-origin
        f.write(struct.pack('<H', 0))  # Y-origin
        f.write(struct.pack('<H', width))  # Image width
        f.write(struct.pack('<H', height))  # Image height
        f.write(struct.pack('B', 24))  # Pixel depth
        f.write(struct.pack('B', 32))  # Image descriptor

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

# Save TGA file with run-length encoding
save_tga_file('./tmp/sample.tga', width, height, data)