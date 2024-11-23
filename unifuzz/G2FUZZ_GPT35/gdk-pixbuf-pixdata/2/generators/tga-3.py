import struct

def create_tga_file(filename, width, height, data, compressed=False):
    # TGA header
    tga_header = bytearray([0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, (width % 256), (width // 256), (height % 256), (height // 256), 24, 0])

    # Run-Length Encoding (RLE) compression
    if compressed:
        compressed_data = bytearray()
        count = 1
        for i in range(1, len(data)):
            if data[i] == data[i-1]:
                count += 1
                if count == 128:  # maximum run-length of 128
                    compressed_data.extend([127, data[i]])
                    count = 1
            else:
                compressed_data.extend([count - 1, data[i-1]])
                count = 1
        compressed_data.extend([count - 1, data[-1]])

        tga_data = compressed_data
    else:
        tga_data = data

    with open(filename, 'wb') as f:
        f.write(tga_header)
        f.write(tga_data)

# Generate some random pixel data
import random
pixel_data = bytearray([random.randint(0, 255) for _ in range(256 * 256)])

# Save uncompressed TGA file
create_tga_file('./tmp/uncompressed.tga', 256, 256, pixel_data, compressed=False)

# Save compressed TGA file
create_tga_file('./tmp/compressed.tga', 256, 256, pixel_data, compressed=True)