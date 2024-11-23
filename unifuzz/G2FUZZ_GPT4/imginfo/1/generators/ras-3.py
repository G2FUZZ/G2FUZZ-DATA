import os
import struct

def create_ras_file(file_path, width, height, depth):
    """
    Creates a .ras file with the specified dimensions and color depth.

    Args:
    - file_path: Path where the .ras file will be saved.
    - width: Width of the image.
    - height: Height of the image.
    - depth: Color depth (e.g., 8, 24 for greyscale, RGB, etc.).
    """
    # Ensure the tmp directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # RAS file header format:
    # magic (4 bytes), width (4 bytes), height (4 bytes),
    # depth (4 bytes), length (4 bytes), type (4 bytes),
    # maptype (4 bytes), maplength (4 bytes)
    # For simplicity, we're filling some fields with fixed values
    magic = 0x59a66a95  # Magic number for RAS files
    length = width * height * (depth // 8)  # Image data size
    type = 0  # Type of file; 0 for raw
    maptype = 0  # Color map type; 0 for RGB
    maplength = 0  # Length of color map; 0 for no color map

    # Open file in binary write mode
    with open(file_path, 'wb') as file:
        # Write the header
        file.write(struct.pack('>IIIIIIII', magic, width, height, depth, length, type, maptype, maplength))
        
        # For simplicity, generate a solid color image (e.g., black for RGB)
        # Note: Adjust the filler based on the color depth
        if depth == 24:  # RGB
            filler = b'\x00\x00\x00'  # Black pixel in RGB
        elif depth == 8:  # Greyscale
            filler = b'\x00'  # Black pixel in greyscale
        else:
            raise ValueError("Unsupported color depth")

        # Write the image data
        for _ in range(width * height):
            file.write(filler)

# Example usage
create_ras_file('./tmp/example.ras', 100, 100, 24)  # Creates a 100x100 black RGB image