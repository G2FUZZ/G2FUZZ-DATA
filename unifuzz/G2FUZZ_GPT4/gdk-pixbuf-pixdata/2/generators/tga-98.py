import os
import struct

def create_tga(width, height, color_depth, alpha=False, pattern=None):
    """
    Create a TGA file with more complex features including True Color and optional alpha channel.

    :param width: Width of the image
    :param height: Height of the image
    :param color_depth: Color depth (24 for RGB, 32 for RGBA)
    :param alpha: Include alpha channel (True/False)
    :param pattern: Function to generate pattern data (takes width, height, alpha)
    """
    header = bytearray([
        0,  # ID length
        0,  # Color map type (0 = no colormap)
        2,  # Image type (2 = True Color)
        0, 0, 0, 0, 0,  # Color map specification (not used)
        0, 0,  # X-origin of the image (low-byte, high-byte)
        0, 0,  # Y-origin of the image (low-byte, high-byte)
        width & 0xFF, (width >> 8) & 0xFF,  # Width of the image (low-byte, high-byte)
        height & 0xFF, (height >> 8) & 0xFF,  # Height of the image (low-byte, high-byte)
        color_depth,  # Pixel depth (24 for RGB, 32 for RGBA)
        32 if alpha else 0,  # Image descriptor (bit 5: 0 = origin lower left, 1 = origin upper left)
    ])

    # Generate image data
    if pattern:
        image_data = pattern(width, height, alpha)
    else:
        # Default pattern: solid color (red or red with alpha)
        if alpha:
            image_data = bytearray([(i % width) * 255 // width, 0, 0, 255] for i in range(width * height))
        else:
            image_data = bytearray([(i % width) * 255 // width, 0, 0] for i in range(width * height))

    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)

    # Write the TGA file
    filename = f'./tmp/complex_image{"_alpha" if alpha else ""}.tga'
    with open(filename, 'wb') as file:
        file.write(header)
        file.write(image_data)

def checkerboard_pattern(width, height, alpha=False):
    """
    Generate a checkerboard pattern.

    :param width: Width of the image
    :param height: Height of the image
    :param alpha: Include alpha channel (True/False)
    :return: Generated image data
    """
    image_data = bytearray()
    for y in range(height):
        for x in range(width):
            # Checkerboard pattern
            if (x // 10) % 2 == (y // 10) % 2:
                pixel = [0xFF, 0xFF, 0xFF]  # White
            else:
                pixel = [0, 0, 0]  # Black
            if alpha:
                pixel.append(0xFF)  # Full opacity
            image_data += bytearray(pixel)
    return image_data

# Example usage
create_tga(100, 100, 24, pattern=checkerboard_pattern)  # RGB checkerboard
create_tga(100, 100, 32, alpha=True, pattern=checkerboard_pattern)  # RGBA checkerboard