import struct
import os

def create_rle_tga(image_data, width, height, file_path):
    # TGA Header for 24-bit image with RLE compression
    header = bytearray([
        0,  # ID length
        0,  # Color map type
        10,  # Image type: RLE Truecolor
        0, 0, 0, 0,  # Color map specification
        0, 0, 0, 0,  # X-origin & Y-origin
        width & 0xFF, (width >> 8) & 0xFF,  # Width
        height & 0xFF, (height >> 8) & 0xFF,  # Height
        24,  # Pixel depth
        0  # Image descriptor
    ])

    with open(file_path, 'wb') as f:
        f.write(header)  # Write the header

        # Process the image data with RLE compression
        pixel_count = len(image_data)
        i = 0
        while i < pixel_count:
            # Look ahead to find runs of the same pixel
            run_length = 1
            while (i + run_length < pixel_count) and (run_length < 128) and (image_data[i] == image_data[i + run_length]):
                run_length += 1

            if run_length > 1:
                # Write a RLE packet
                f.write(struct.pack('B', 0x80 | (run_length - 1)))  # RLE packet header
                f.write(image_data[i])  # Pixel data
                i += run_length
            else:
                # Write a raw packet
                raw_start = i
                i += 1
                while (i < pixel_count) and ((i - raw_start) < 128) and ((i + 1 == pixel_count) or (image_data[i] != image_data[i + 1])):
                    i += 1
                
                f.write(struct.pack('B', (i - raw_start) - 1))  # Raw packet header
                f.write(b"".join(image_data[raw_start:i]))  # Pixel data

def generate_gradient_image(width, height):
    # Creates a simple image with a blue and red horizontal gradient
    image_data = []
    for y in range(height):
        for x in range(width):
            red = x % 256
            green = 0
            blue = (width - x) % 256
            image_data.append(struct.pack('BBB', blue, green, red))
    return image_data

# Define image dimensions
width, height = 100, 100

# Generate image data
image_data = generate_gradient_image(width, height)

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create and save the TGA file
create_rle_tga(image_data, width, height, './tmp/gradient_rle.tga')