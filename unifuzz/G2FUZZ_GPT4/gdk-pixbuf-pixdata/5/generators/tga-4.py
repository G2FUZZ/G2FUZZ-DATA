import os

def create_palette_based_tga(filename, width, height, palette, data):
    header = bytes([
        0,  # ID length
        1,  # Color map type (1 = has palette)
        1,  # Image type (1 = palette-based)
        0, 0,  # Color map origin
        len(palette), 0,  # Color map length
        24,  # Color map depth (24 bits)
        0, 0, 0, 0,  # X and Y origin
        width & 0xFF, (width >> 8) & 0xFF,  # Width
        height & 0xFF, (height >> 8) & 0xFF,  # Height
        24,  # Pixel depth
        0,  # Image descriptor
    ])

    # Convert palette to bytes
    palette_bytes = b''.join([b''.join([bytes([component]) for component in color]) for color in palette])

    # Convert data to bytes
    data_bytes = bytes(data)

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Write the file
    with open(filename, 'wb') as f:
        f.write(header)
        f.write(palette_bytes)
        f.write(data_bytes)

# Example usage
filename = './tmp/palette_based_image.tga'
width = 4
height = 4
palette = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255)]  # Red, Green, Blue, White
data = [
    0, 1, 2, 3,  # First row: Red, Green, Blue, White
    1, 2, 3, 0,  # Second row: Green, Blue, White, Red
    2, 3, 0, 1,  # Third row: Blue, White, Red, Green
    3, 0, 1, 2   # Fourth row: White, Red, Green, Blue
]

create_palette_based_tga(filename, width, height, palette, data)