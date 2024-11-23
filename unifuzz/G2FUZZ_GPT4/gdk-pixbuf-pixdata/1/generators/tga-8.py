import os

def create_tga_file(file_path, width, height, color_depth):
    # Ensure the tmp directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # TGA Header for an uncompressed true-color image
    header = bytearray([
        0,  # ID length
        0,  # Color map type
        2,  # Image type (2 for uncompressed true-color image)
        0, 0, 0, 0, 0,  # Color map specification (5 bytes)
        0, 0,  # X-origin (2 bytes)
        0, 0,  # Y-origin (2 bytes)
        width & 0xFF, (width >> 8) & 0xFF,  # Width (2 bytes)
        height & 0xFF, (height >> 8) & 0xFF,  # Height (2 bytes)
        color_depth,  # Pixel depth (e.g., 24 for 24-bit)
        0  # Image descriptor (bits 3-0 give the alpha channel depth, bits 5-4 give direction)
    ])
    
    # Simple image data (e.g., a blue image)
    # Note: TGA format specifies pixel data in BGR format
    pixel_data = bytearray([255, 0, 0] * width * height)  # Blue image
    
    # Write the file
    with open(file_path, 'wb') as f:
        f.write(header)
        f.write(pixel_data)  # Corrected the variable name here

# Parameters for the image
width = 100  # Width of the image
height = 100  # Height of the image
color_depth = 24  # Color depth (24 for RGB)

# Generate and save the TGA file
create_tga_file('./tmp/sample.tga', width, height, color_depth)