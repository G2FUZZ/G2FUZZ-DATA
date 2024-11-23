import os

def write_tga_footer(file_path, extension_area_offset=0, developer_area_offset=0):
    # TGA Footer format:
    # - Extension Area Offset (4 bytes)
    # - Developer Directory Offset (4 bytes)
    # - Signature "TRUEVISION-XFILE." (18 bytes including NULL terminator)
    with open(file_path, 'ab') as f:
        # Extension Area Offset (4 bytes, little endian)
        f.write(extension_area_offset.to_bytes(4, byteorder='little'))
        # Developer Area Offset (4 bytes, little endian)
        f.write(developer_area_offset.to_bytes(4, byteorder='little'))
        # Signature + NULL terminator
        f.write(b'TRUEVISION-XFILE.\x00')

def create_basic_tga_with_footer(directory, filename):
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)
    
    file_path = os.path.join(directory, filename)

    # TGA Header for a minimal file (uncompressed, no colormap, no image data)
    # This is just an example; adjust header and image data as necessary
    header = bytes([
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # Image ID (0) + Color map (0) + Image type (0)
        0, 0, 0, 0,  # Color map spec
        0, 0, 0, 0,  # X-origin + Y-origin
        0, 0,  # Width (little endian)
        0, 0,  # Height (little endian)
        0,  # Pixel depth
        0   # Image Descriptor
    ])

    # Write header to file
    with open(file_path, 'wb') as f:
        f.write(header)
    
    # Optionally: add image data here

    # Add footer
    write_tga_footer(file_path)

# Example usage
create_basic_tga_with_footer('./tmp/', 'example.tga')