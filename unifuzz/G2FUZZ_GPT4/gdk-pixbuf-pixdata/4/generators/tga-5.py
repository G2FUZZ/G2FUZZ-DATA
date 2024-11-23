import os

def create_tga_file(filename, width, height, color_depth, color):
    # TGA Header for uncompressed true-color image
    header = bytearray([
        0,  # ID length
        0,  # Color map type
        2,  # Image type (2 for uncompressed true-color image)
        0, 0, 0, 0, 0,  # Color map specification
        0, 0,  # X-origin (low-high)
        0, 0,  # Y-origin (low-high)
        width & 0xFF, (width >> 8) & 0xFF,  # Width (low-high)
        height & 0xFF, (height >> 8) & 0xFF,  # Height (low-high)
        color_depth,  # Pixel depth
        0  # Image descriptor
    ])

    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Open file for writing in binary mode
    with open(filename, 'wb') as f:
        f.write(header)  # Write the header to the file
        # Correctly create pixel data by repeating the color for each pixel
        pixel_data = bytearray()
        for _ in range(width * height):
            pixel_data.extend(color)  # Extend the bytearray with the color for each pixel
        f.write(pixel_data)  # Write the pixel data to the file

# Example usage
create_tga_file('./tmp/example.tga', 100, 100, 24, [0, 0, 255])  # Create a 100x100 blue image