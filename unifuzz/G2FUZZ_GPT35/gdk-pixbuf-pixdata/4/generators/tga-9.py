import struct

def save_tga_monochrome(filename, width, height, data):
    with open(filename, 'wb') as f:
        # TGA header
        f.write(struct.pack('B', 0))  # ID length
        f.write(struct.pack('B', 0))  # Color map type
        f.write(struct.pack('B', 3))  # Image type (monochrome)
        f.write(struct.pack('<H', 0))  # Color map origin
        f.write(struct.pack('<H', 0))  # Color map length
        f.write(struct.pack('B', 0))  # Color map entry size
        f.write(struct.pack('<H', 0))  # X origin
        f.write(struct.pack('<H', 0))  # Y origin
        f.write(struct.pack('<H', width))  # Image width
        f.write(struct.pack('<H', height))  # Image height
        f.write(struct.pack('B', 8))  # Pixel depth
        f.write(struct.pack('B', 0))  # Image descriptor

        # Image data
        f.write(data)

# Generate monochrome image data
width = 100
height = 100
data = bytes([255 if x % width < width//2 else 0 for x in range(width*height)])

# Save monochrome image to a TGA file
filename = './tmp/monochrome_image.tga'
save_tga_monochrome(filename, width, height, data)