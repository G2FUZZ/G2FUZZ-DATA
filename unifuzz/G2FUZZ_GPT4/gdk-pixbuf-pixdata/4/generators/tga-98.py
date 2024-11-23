import os
import struct

def create_tga(path, width, height, pixels, color_map=None, use_rle_compression=False):
    if color_map is not None:
        image_type = 9 if use_rle_compression else 1  # Color-mapped image (RLE compressed or not)
        color_map_type = 1  # Has a color map
        color_map_entry_size = 24  # 24 bits per color map entry
        color_map_data = b''.join(struct.pack('BBB', *color) for color in color_map)
        color_map_length = len(color_map)
        pixel_data = b''.join(struct.pack('B', idx) for idx in pixels)
    else:
        image_type = 10 if use_rle_compression else 2  # True color image (RLE compressed or not)
        color_map_type = 0  # No color map
        color_map_entry_size = 0
        color_map_length = 0
        color_map_data = b''
        pixel_data = b''.join(struct.pack('BBB', *pixel) for pixel in pixels)

    header = struct.pack(
        '<BBBHHBHHHHBB',
        0,  # ID length
        color_map_type,
        image_type,
        0,  # Color map origin
        color_map_length,
        color_map_entry_size,
        0, 0,  # X-origin, Y-origin
        width, height,
        24,  # Pixel depth
        0,  # Image descriptor
    )

    if use_rle_compression:
        pixel_data = rle_compress(pixel_data, is_mapped=bool(color_map))

    # Optional TGA footer (useful for TGA 2.0 readers)
    footer = b'TRUEVISION-XFILE.\x00'  # 26 bytes

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Write the file
    with open(path, 'wb') as f:
        f.write(header)
        f.write(color_map_data)
        f.write(pixel_data)
        # Write an empty developer area and extension area
        f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00')
        # Write the footer
        f.write(footer)

def rle_compress(data, is_mapped=True):
    compressed_data = bytearray()
    i = 0
    while i < len(data):
        # Find run length
        run_length = 1
        while i + run_length < len(data) and run_length < 128:
            if data[i:i+3] == data[i+run_length:i+run_length+3] and not is_mapped:
                run_length += 1
            elif data[i] == data[i+run_length] and is_mapped:
                run_length += 1
            else:
                break
        if run_length > 1:
            # Write run length packet
            compressed_data.append(128 + run_length - 1)
            compressed_data.extend(data[i:i+(1 if is_mapped else 3)])
        else:
            # Write raw packet
            start = i
            i += 1
            while i < len(data) and run_length < 128 and (i + 3 >= len(data) or data[i:i+3] != data[i+3:i+6] or is_mapped and data[i] != data[i+1]):
                i += 1
                run_length += 1
            compressed_data.append(run_length - 1)
            compressed_data.extend(data[start:i])
        i += run_length
    return bytes(compressed_data)

# Example usage (true color image)
pixels = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
] * 64  # 8x8 image

create_tga('./tmp/true_color_image.tga', 8, 8, pixels, use_rle_compression=True)