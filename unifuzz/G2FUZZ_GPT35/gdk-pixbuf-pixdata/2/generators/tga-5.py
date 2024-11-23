import numpy as np

def create_tga_file(image_orientation, file_path):
    # Define TGA image header
    header = bytearray([
        0,  # ID length
        0,  # Color map type
        0,  # Image type (no color map included)
        0, 0, 0, 0, 0,  # Color map specification
        0, 0,  # X-origin
        0, 0,  # Y-origin
        (image_orientation << 4),  # Image orientation
        0, 0,  # Image width
        0, 0,  # Image height
        24,  # Pixel depth
        0  # Image descriptor
    ])

    # Generate example image data
    image_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

    # Write header and image data to file
    with open(file_path, 'wb') as f:
        f.write(header)
        f.write(image_data.tobytes())

# Save TGA files with different orientations
orientations = [0, 1, 2, 3]  # Top-left, top-right, bottom-left, bottom-right

for idx, orientation in enumerate(orientations):
    file_path = f'./tmp/image_{idx}.tga'
    create_tga_file(orientation, file_path)