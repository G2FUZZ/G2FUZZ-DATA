import numpy as np

def create_tga_file(pixel_format, filename):
    if pixel_format == 'grayscale':
        image_data = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
    elif pixel_format == 'RGB':
        image_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
    elif pixel_format == 'RGBA':
        image_data = np.random.randint(0, 256, (100, 100, 4), dtype=np.uint8)
    
    with open(filename, 'wb') as f:
        f.write(b'\x00')  # ID Length
        f.write(b'\x00')  # Color Map Type
        f.write(b'\x02')  # Image Type (Uncompressed Truecolor)
        f.write(b'\x00\x00')  # Color Map Specification
        f.write(b'\x00\x00')
        f.write(b'\x00')  # Color Map Depth
        f.write(b'\x00\x00')  # X-origin
        f.write(b'\x00\x00')  # Y-origin
        f.write(b'\x64\x00')  # Width (100)
        f.write(b'\x64\x00')  # Height (100)
        f.write(b'\x08')  # Pixel Depth (8 bits per channel)
        f.write(b'\x20')  # Image Descriptor (Top-left origin)
        
        if pixel_format == 'grayscale':
            f.write(image_data.tobytes())
        else:
            f.write(image_data.transpose(1, 0, 2).tobytes())

# Create grayscale TGA file
create_tga_file('grayscale', './tmp/grayscale.tga')

# Create RGB TGA file
create_tga_file('RGB', './tmp/RGB.tga')

# Create RGBA TGA file
create_tga_file('RGBA', './tmp/RGBA.tga')