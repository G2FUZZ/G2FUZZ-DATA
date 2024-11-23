import struct
import os

def create_rle_tga(image_data, width, height, file_path, pixel_depth=24, developer_area=None):
    """
    Generate a TGA file with RLE compression. Supports 24-bit and 32-bit images.
    Optionally includes a developer area if provided.

    Parameters:
    - image_data: List of pixel data tuples (RGB or RGBA depending on pixel_depth).
    - width: Image width.
    - height: Image height.
    - file_path: Path to save the TGA file.
    - pixel_depth: Depth of each pixel (24 or 32 bits).
    - developer_area: Optional tuple of (tag, data) pairs for developer area entries.
    """
    # TGA Header for RLE compressed image
    header = bytearray([
        0,  # ID length
        0,  # Color map type
        10,  # Image type: RLE Truecolor
        0, 0, 0, 0,  # Color map specification
        0, 0, 0, 0,  # X-origin & Y-origin
        width & 0xFF, (width >> 8) & 0xFF,  # Width
        height & 0xFF, (height >> 8) & 0xFF,  # Height
        pixel_depth,  # Pixel depth (24 or 32)
        0  # Image descriptor (bit 5 should be set for top-left origin, if desired)
    ])

    # Developer area (optional)
    developer_entries = []
    if developer_area:
        for tag, data in developer_area:
            entry = struct.pack('HH', tag, len(data)) + data
            developer_entries.append(entry)

    developer_directory = b"".join(developer_entries)
    developer_directory_offset = len(header) + sum(len(d) for d in image_data) + len(developer_directory)
    developer_directory_header = struct.pack('II', developer_directory_offset, len(developer_area)) if developer_area else b'\x00' * 8

    # Footer (optional, but recommended for TGA 2.0)
    # "TRUEVISION-XFILE" signature indicates the presence of a footer.
    footer = b'TRUEVISION-XFILE.\x00'
    # Offsets for the extension area and developer directory (set to zero if not used)
    extension_area_offset = 0
    # Correcting the footer structure with the right format and arguments
    footer_struct = struct.pack('III18s', extension_area_offset, developer_directory_offset, 0, footer)

    with open(file_path, 'wb') as f:
        f.write(header)  # Write the header

        # RLE Compression and Writing Pixel Data
        pixel_count = len(image_data)
        i = 0
        while i < pixel_count:
            run_length = 1
            while (i + run_length < pixel_count) and (run_length < 128) and (image_data[i] == image_data[i + run_length]):
                run_length += 1

            if run_length > 1:
                # RLE Packet
                f.write(struct.pack('B', 0x80 | (run_length - 1)))
                f.write(image_data[i])
                i += run_length
            else:
                # Raw Packet
                raw_start = i
                i += 1
                while (i < pixel_count) and ((i - raw_start) < 128) and ((i + 1 == pixel_count) or (image_data[i] != image_data[i + 1])):
                    i += 1
                
                f.write(struct.pack('B', (i - raw_start) - 1))
                f.write(b"".join(image_data[raw_start:i]))

        if developer_area:
            f.write(developer_directory)  # Write the developer directory
            f.write(developer_directory_header)  # Write the developer directory header

        f.write(footer_struct)  # Write the footer

def generate_gradient_image(width, height, include_alpha=False):
    """
    Creates a simple image with a blue-to-red horizontal gradient.
    Optionally includes an alpha channel for 32-bit images.
    """
    image_data = []
    for y in range(height):
        for x in range(width):
            red = x % 256
            green = 0
            blue = (width - x) % 256
            alpha = (x + y) % 256  # Example alpha value
            if include_alpha:
                image_data.append(struct.pack('BBBB', blue, green, red, alpha))
            else:
                image_data.append(struct.pack('BBB', blue, green, red))
    return image_data

# Example usage:
width, height = 100, 100
image_data = generate_gradient_image(width, height, include_alpha=True)  # Corrected function call

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Example developer area data
developer_data = [(1, b"ExampleDeveloperData")]

# Create and save the TGA file with 32-bit depth and developer area
create_rle_tga(image_data, width, height, './tmp/gradient_rle_32bit.tga', pixel_depth=32, developer_area=developer_data)