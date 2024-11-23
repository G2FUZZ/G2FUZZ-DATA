import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create a simple TGA file with a footer
def create_tga_with_footer(file_path):
    width, height = 100, 100  # Image dimensions
    header = bytearray([
        0,    # ID length
        0,    # Color map type
        2,    # Image type (uncompressed, true-color image)
        0, 0, 0, 0, 0, 0,  # Color map specification (5 bytes)
        0, 0,  # X-origin (2 bytes)
        0, 0,  # Y-origin (2 bytes)
        width & 0xFF, (width >> 8) & 0xFF,  # Width (2 bytes)
        height & 0xFF, (height >> 8) & 0xFF,  # Height (2 bytes)
        24,   # Pixel depth (24 bits or 3 bytes per pixel for RGB)
        0     # Image descriptor (bits 3-0 give the alpha channel depth, bits 5-4 give direction)
    ])

    # Image data (simple blue color for the entire image)
    pixels = [255, 0, 0] * width * height  # Blue pixel (B, G, R) format

    # Footer
    # For simplicity, we're setting the extension area and developer directory offsets to 0
    # indicating that they are not used in this example.
    footer = bytearray([
        0, 0, 0, 0,  # Extension area offset (not used)
        0, 0, 0, 0,  # Developer directory offset (not used)
    ]) + b"TRUEVISION-XFILE.\x00"  # Signature + final period and null byte

    # Write the TGA file
    with open(file_path, 'wb') as f:
        f.write(header)  # Write the header
        f.write(bytearray(pixels))  # Write the pixel data
        f.write(footer)  # Append the footer

create_tga_with_footer('./tmp/simple_with_footer.tga')