def create_tga_with_metadata(file_path, width, height, metadata):
    # TGA Header for an uncompressed true-color image
    header = bytearray([
        0,  # ID length
        0,  # Color map type
        2,  # Image type (2 for uncompressed true-color image)
        0, 0, 0, 0, 0,  # Color map specification
        0, 0,  # X-origin
        0, 0,  # Y-origin
        width & 0xFF, (width >> 8) & 0xFF,  # Width
        height & 0xFF, (height >> 8) & 0xFF,  # Height
        24,  # Pixel depth
        0,  # Image descriptor
    ])

    # Image data (simple black image for demonstration)
    pixels = bytearray([0, 0, 0] * width * height)

    # Footer (Reference: TGA Specification 2.0)
    extension_area_offset = 0  # No extension area
    developer_area_offset = len(header) + len(pixels) + 18  # Offset to developer area
    signature = b"TRUEVISION-XFILE.\0"  # Signature + NULL terminator

    footer = bytearray([
        extension_area_offset & 0xFF, (extension_area_offset >> 8) & 0xFF,
        (extension_area_offset >> 16) & 0xFF, (extension_area_offset >> 24) & 0xFF,
        developer_area_offset & 0xFF, (developer_area_offset >> 8) & 0xFF,
        (developer_area_offset >> 16) & 0xFF, (developer_area_offset >> 24) & 0xFF,
        *signature
    ])

    # Developer area (just a simple metadata text for this example)
    developer_area = bytearray(metadata, 'ascii')
    developer_area_length = len(developer_area)
    developer_entries = 1  # Number of entries in the developer directory
    developer_directory = bytearray([
        developer_entries & 0xFF, (developer_entries >> 8) & 0xFF,
        0, 0,  # First entry ID
        developer_area_offset + 4 & 0xFF, (developer_area_offset + 4 >> 8) & 0xFF,
        (developer_area_offset + 4 >> 16) & 0xFF, (developer_area_offset + 4 >> 24) & 0xFF,
        developer_area_length & 0xFF, (developer_area_length >> 8) & 0xFF,
        (developer_area_length >> 16) & 0xFF, (developer_area_length >> 24) & 0xFF,
    ])

    with open(file_path, 'wb') as f:
        f.write(header)
        f.write(pixels)
        f.write(developer_directory)
        f.write(developer_area)
        f.write(footer)

# Example usage
create_tga_with_metadata('./tmp/example_with_metadata.tga', 100, 100, 'Example Metadata: This is a TGA file with metadata.')