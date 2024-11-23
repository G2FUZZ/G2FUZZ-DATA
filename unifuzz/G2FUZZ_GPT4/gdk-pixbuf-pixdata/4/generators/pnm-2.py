import os

def create_pbm_image(filename, width, height):
    """
    Create a simple PBM (Portable BitMap) image, which is a subset of the PNM format family.
    This function generates an image with a simple pattern.
    """
    with open(filename, 'wb') as f:
        # PBM header
        f.write(b'P4\n')  # P4 means binary PBM
        f.write(f'{width} {height}\n'.encode())

        # Image data: simple pattern (checkerboard)
        for y in range(height):
            row = bytearray()
            for x in range(width):
                if (x//10 + y//10) % 2 == 0:
                    row.append(0x00)  # Black pixel
                else:
                    row.append(0xFF)  # White pixel, though in PBM 0 is black and 1 is white
            f.write(row[:width // 8])

def create_pgm_image(filename, width, height):
    """
    Create a simple PGM (Portable GrayMap) image, which is another format in the PNM family.
    This function generates a gradient image.
    """
    with open(filename, 'wb') as f:
        # PGM header
        f.write(b'P5\n')  # P5 means binary PGM
        f.write(f'{width} {height}\n255\n'.encode())

        # Image data: vertical gradient
        for y in range(height):
            for x in range(width):
                value = int(x / width * 255)
                f.write(value.to_bytes(1, byteorder='big'))

def create_ppm_image(filename, width, height):
    """
    Create a simple PPM (Portable PixMap) image, which is the most general format in the PNM family.
    This function generates an RGB gradient image.
    """
    with open(filename, 'wb') as f:
        # PPM header
        f.write(b'P6\n')  # P6 means binary PPM
        f.write(f'{width} {height}\n255\n'.encode())

        # Image data: RGB gradient
        for y in range(height):
            for x in range(width):
                f.write(bytes([
                    int(x / width * 255),  # Red
                    int(y / height * 255),  # Green
                    int((x+y) / (width+height) * 255)  # Blue
                ]))

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create PNM images
create_pbm_image('./tmp/simple_pattern.pbm', 80, 80)  # PBM example
create_pgm_image('./tmp/gradient.pgm', 80, 80)        # PGM example
create_ppm_image('./tmp/rgb_gradient.ppm', 80, 80)    # PPM example