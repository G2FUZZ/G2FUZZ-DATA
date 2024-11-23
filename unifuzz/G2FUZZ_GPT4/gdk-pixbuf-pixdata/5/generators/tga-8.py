import os

def create_tga_file(filepath, width, height, color_data):
    # TGA Header for an uncompressed true-color image
    header = bytearray([
        0,  # ID length
        0,  # Color map type
        2,  # Image type (2 for uncompressed true-color image)
        0, 0, 0, 0, 0,  # Color map specification
        0, 0,  # X-origin (2 bytes)
        0, 0,  # Y-origin (2 bytes)
        width & 0xFF, (width >> 8) & 0xFF,  # Width
        height & 0xFF, (height >> 8) & 0xFF,  # Height
        24,  # Pixel depth (24 bits/3 bytes per pixel for true color)
        0  # Image descriptor
    ])

    # Ensure the directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Write the TGA file
    with open(filepath, 'wb') as file:
        file.write(header)  # Write the header
        for row in range(height):  # Write the pixel data
            for col in range(width):
                file.write(color_data[row][col])

# Example usage
width, height = 100, 100  # Dimensions of the image

# Create a simple pattern: alternating red and blue
color_data = [
    [b'\xFF\x00\x00' if (row + col) % 2 == 0 else b'\x00\x00\xFF' for col in range(width)]
    for row in range(height)
]

create_tga_file('./tmp/cross_platform_compatibility.tga', width, height, color_data)