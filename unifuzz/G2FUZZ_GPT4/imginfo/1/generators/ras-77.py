import os
import struct

def create_gradient_ras_file(file_path, width, height, depth, direction='horizontal'):
    """
    Creates a .ras file with a gradient based on the specified dimensions and color depth.

    Args:
    - file_path: Path where the .ras file will be saved.
    - width: Width of the image.
    - height: Height of the image.
    - depth: Color depth (e.g., 8 for greyscale, 24 for RGB).
    - direction: Gradient direction ('horizontal' or 'vertical').
    """
    # Ensure the tmp directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # RAS file header format
    magic = 0x59a66a95  # Magic number for RAS files
    length = width * height * (depth // 8)  # Image data size
    type = 0  # Type of file; 0 for raw
    maptype = 0  # Color map type; 0 for RGB
    maplength = 0  # Length of color map; 0 for no color map

    with open(file_path, 'wb') as file:
        # Write the header
        file.write(struct.pack('>IIIIIIII', magic, width, height, depth, length, type, maptype, maplength))
        
        # Determine how to create the gradient
        if depth == 24:  # RGB
            for i in range(height):
                for j in range(width):
                    if direction == 'horizontal':
                        # Horizontal gradient - color changes along x-axis
                        ratio = j / width
                    else:
                        # Vertical gradient - color changes along y-axis
                        ratio = i / height
                    # Generate pixel color based on position
                    # Example: simple RGB gradient
                    r = int(ratio * 255)
                    g = int((1 - ratio) * 255)
                    b = int((ratio * 255) % 256)  # Simple way to create a varying color
                    pixel = struct.pack('BBB', r, g, b)
                    file.write(pixel)
        elif depth == 8:  # Greyscale
            for i in range(height):
                for j in range(width):
                    if direction == 'horizontal':
                        # Horizontal gradient - intensity changes along x-axis
                        ratio = j / width
                    else:
                        # Vertical gradient - intensity changes along y-axis
                        ratio = i / height
                    # Generate pixel intensity based on position
                    intensity = int(ratio * 255)
                    pixel = struct.pack('B', intensity)
                    file.write(pixel)
        else:
            raise ValueError("Unsupported color depth")

# Example usage
create_gradient_ras_file('./tmp/gradient_horizontal.ras', 100, 100, 24, 'horizontal')  # Creates a 100x100 horizontal RGB gradient
create_gradient_ras_file('./tmp/gradient_vertical.ras', 100, 100, 24, 'vertical')  # Creates a 100x100 vertical RGB gradient
create_gradient_ras_file('./tmp/gradient_greyscale_horizontal.ras', 100, 100, 8, 'horizontal')  # Creates a 100x100 horizontal greyscale gradient