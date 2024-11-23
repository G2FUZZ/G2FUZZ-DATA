import os
import numpy as np

def create_rle_tga(image_data, file_path):
    """
    Create a TGA file with RLE compression.

    Parameters:
    - image_data: A numpy array with shape (height, width, 3) representing the image.
    - file_path: The path to save the TGA file.
    """
    height, width, depth = image_data.shape
    assert depth == 3, "Image data must have 3 channels."

    # TGA Header for RLE compressed, 24-bit image
    header = bytearray([
        0,  # ID length
        0,  # Color map type
        10,  # Image type: RLE Truecolor
        0, 0, 0, 0, 0,  # Color map specification
        0, 0, 0, 0,  # X and Y origin
        width & 0xFF, (width >> 8) & 0xFF,  # Width
        height & 0xFF, (height >> 8) & 0xFF,  # Height
        24,  # Pixel depth
        0  # Image descriptor
    ])

    # Convert image data to BGR format expected by TGA
    bgr_data = image_data[:, :, ::-1]

    # RLE Compress
    compressed_data = bytearray()
    for row in bgr_data:
        i = 0
        while i < len(row):
            count = 1
            while i + count < len(row) and count < 128 and np.array_equal(row[i], row[i + count]):
                count += 1
            if count > 1:
                compressed_data.append(count - 1 | 0x80)  # Set RLE flag
                compressed_data.extend(row[i].astype(np.uint8).tobytes())  # Convert numpy array to bytes
            else:
                # Find next non-repeating pixel or end of row
                start = i
                while count < 128 and i + count < len(row) and (count == 1 or not np.array_equal(row[i + count - 1], row[i + count])):
                    count += 1
                compressed_data.append(count - 1)  # Raw packet flag
                # Convert numpy array slice to bytes and extend compressed_data
                compressed_data.extend(row[start:start + count].astype(np.uint8).flatten().tobytes())

            i += count

    with open(file_path, 'wb') as f:
        f.write(header)
        f.write(compressed_data)

# Example usage
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a sample image data (green square)
image_height, image_width = 100, 100
green_color = np.array([0, 255, 0], dtype=np.uint8)
image_data = np.tile(green_color, (image_height, image_width, 1))

create_rle_tga(image_data, './tmp/green_square_rle.tga')