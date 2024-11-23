import os

def create_bmp(filename, width, height):
    # Ensure the tmp directory exists
    os.makedirs('./tmp/', exist_ok=True)
    filepath = os.path.join('./tmp/', filename)

    with open(filepath, 'wb') as f:
        # BMP Header
        f.write(b'BM')  # Signature
        filesize = 54 + 3 * width * height  # Header (54 bytes) + pixel data
        f.write(filesize.to_bytes(4, byteorder='little'))  # File size
        f.write((0).to_bytes(4, byteorder='little'))  # Reserved
        f.write((54).to_bytes(4, byteorder='little'))  # Data offset

        # DIB Header
        f.write((40).to_bytes(4, byteorder='little'))  # DIB Header size
        f.write(width.to_bytes(4, byteorder='little'))  # Width
        f.write(height.to_bytes(4, byteorder='little'))  # Height
        f.write((1).to_bytes(2, byteorder='little'))  # Planes
        f.write((24).to_bytes(2, byteorder='little'))  # Bits per pixel
        f.write((0).to_bytes(4, byteorder='little'))  # Compression
        f.write((0).to_bytes(4, byteorder='little'))  # Image size (can be 0 for BI_RGB)
        f.write((0).to_bytes(4, byteorder='little'))  # Horizontal resolution
        f.write((0).to_bytes(4, byteorder='little'))  # Vertical resolution
        f.write((0).to_bytes(4, byteorder='little'))  # Colors in color table
        f.write((0).to_bytes(4, byteorder='little'))  # Important color count

        # Pixel Array (Image Data)
        for row in reversed(range(height)):  # Bottom to top
            for col in range(width):  # Left to right
                # Gradient effect from blue to green to red
                blue = (255 * col) // width
                green = (255 * row) // height
                red = (255 * (col + row)) // (width + height)
                f.write(bytes([blue, green, red]))
            # Padding for 4-byte alignment
            padding = (4 - (3 * width) % 4) % 4
            f.write((0).to_bytes(padding, byteorder='little'))

create_bmp('gradient.bmp', 200, 200)  # Example usage