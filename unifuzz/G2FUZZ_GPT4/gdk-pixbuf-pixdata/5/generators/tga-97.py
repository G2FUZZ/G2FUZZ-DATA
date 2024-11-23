import struct
import os

def write_footer(f):
    # TGA Footer
    footer = struct.pack('IIIB', 0, 0, 0, ord('T')) + b'RUEVISION-XFILE.\0'
    f.write(footer)

def create_tga_header(width, height, image_type, color_map_type=0, color_map_length=0, color_map_entry_size=0):
    # TGA Header
    header = struct.pack(
        'BBBHHBHHHHBB',
        0,  # ID Length
        color_map_type,  # Color Map Type (0 or 1)
        image_type,  # Image Type (2 for uncompressed true-color image, 10 for RLE true-color)
        0, color_map_length,  # Color Map Specification
        color_map_entry_size,
        0, 0,  # X-origin & Y-origin
        width, height,  # Width & Height
        24,  # Pixel Depth
        0   # Image Descriptor
    )
    return header

def compress_rle(image_data):
    compressed_data = bytearray()
    pixel_count = len(image_data)
    i = 0
    while i < pixel_count:
        # Look ahead to find runs of the same pixel
        run_length = 1
        while (i + run_length < pixel_count) and (run_length < 128) and (image_data[i] == image_data[i + run_length]):
            run_length += 1

        if run_length > 1:
            # Write a RLE packet
            compressed_data.append(0x80 | (run_length - 1))  # RLE packet header
            compressed_data += image_data[i]  # Pixel data
            i += run_length
        else:
            # Write a raw packet
            raw_start = i
            i += 1
            while (i < pixel_count) and ((i - raw_start) < 128) and ((i + 1 == pixel_count) or (image_data[i] != image_data[i + 1])):
                i += 1
            
            compressed_data.append((i - raw_start) - 1)  # Raw packet header
            compressed_data += b"".join(image_data[raw_start:i])  # Pixel data
    return compressed_data

def create_tga(image_data, width, height, file_path, image_type=2, color_map=None):
    color_map_type = 1 if color_map else 0
    color_map_length = len(color_map) if color_map else 0
    color_map_entry_size = 24 if color_map else 0  # Assuming 24-bit color map entries

    header = create_tga_header(width, height, image_type, color_map_type, color_map_length, color_map_entry_size)

    with open(file_path, 'wb') as f:
        f.write(header)  # Write the header

        if color_map:
            # Write the color map
            for color in color_map:
                f.write(struct.pack('BBB', *color))

        if image_type == 10:  # RLE Compression
            compressed_data = compress_rle(image_data)
            f.write(compressed_data)
        else:
            # Uncompressed data
            f.write(b"".join(image_data))

        write_footer(f)  # Write the footer

def generate_checkerboard_image(width, height, pattern_size):
    # Generates a checkerboard pattern
    image_data = []
    color_map = [(255, 255, 255), (0, 0, 0)]  # White and Black
    for y in range(height):
        for x in range(width):
            if (x // pattern_size) % 2 == (y // pattern_size) % 2:
                index = 0  # White
            else:
                index = 1  # Black
            image_data.append(struct.pack('B', index))
    return image_data, color_map

# Define image dimensions
width, height, pattern_size = 100, 100, 10

# Generate checkerboard image data
image_data, color_map = generate_checkerboard_image(width, height, pattern_size)

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create and save the TGA file with a color map and uncompressed image data
create_tga(image_data, width, height, './tmp/checkerboard_uncompressed.tga', image_type=1, color_map=color_map)

# Create and save the TGA file with a color map and RLE compressed image data
create_tga(image_data, width, height, './tmp/checkerboard_rle.tga', image_type=9, color_map=color_map)