import os
import struct

def write_tga(width, height, color_depth, data, filename):
    header = bytearray(18)
    header[2] = 2  # Truecolor image type
    header[12] = width & 0xFF
    header[13] = (width >> 8) & 0xFF
    header[14] = height & 0xFF
    header[15] = (height >> 8) & 0xFF
    header[16] = color_depth  # Color depth

    with open(filename, 'wb') as file:
        file.write(header)
        file.write(data)

def generate_tga_files():
    os.makedirs('./tmp/', exist_ok=True)

    # 8-bit example (palette-based, simple gradient for demonstration)
    width, height = 100, 100
    palette = [struct.pack('BBB', i, i, i) for i in range(256)]  # Grayscale palette
    data = bytes([i % 256 for i in range(width * height)])
    write_tga(width, height, 8, b''.join(palette) + data, './tmp/8bit.tga')

    # 24-bit example (RGB)
    data = bytearray()
    for y in range(height):
        for x in range(width):
            data.extend([x % 256, y % 256, (x + y) % 256])  # Simple gradient
    write_tga(width, height, 24, data, './tmp/24bit.tga')

    # 32-bit example (RGBA)
    data = bytearray()
    for y in range(height):
        for x in range(width):
            data.extend([x % 256, y % 256, (x + y) % 256, 255])  # Simple gradient with full alpha
    write_tga(width, height, 32, data, './tmp/32bit.tga')

if __name__ == "__main__":
    generate_tga_files()