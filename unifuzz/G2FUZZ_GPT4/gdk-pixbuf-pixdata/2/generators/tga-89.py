import os
import numpy as np

def save_tga(filename, image_data, bit_depth, compress=False):
    """
    Save an image as a TGA file with specified bit depth and optional RLE compression.
    """
    if compress:
        image_type = 10  # RLE True-color image.
        pixel_data = rle_compress(image_data, bit_depth)
    else:
        image_type = 2  # Uncompressed true-color image.
        pixel_data = image_data.tobytes()

    header = bytearray(18)
    header[2] = image_type
    header[12:14] = (image_data.shape[1] & 0xFF, image_data.shape[1] >> 8 & 0xFF)  # Image width.
    header[14:16] = (image_data.shape[0] & 0xFF, image_data.shape[0] >> 8 & 0xFF)  # Image height.
    header[16] = bit_depth * 8  # Color depth per pixel.
    header[17] = 0x20  # Image descriptor (top-left origin).

    with open(filename, 'wb') as f:
        f.write(header)
        f.write(pixel_data)

def rle_compress(image_data, bit_depth):
    """
    Compress image data using RLE for TGA files.
    """
    max_packet_size = 128
    if bit_depth == 1 or bit_depth == 2:
        raise ValueError("RLE compression is not supported for bit depths less than 3.")
    
    bytes_per_pixel = bit_depth
    flat_image = image_data.flatten()  # Corrected line
    compressed_stream = bytearray()
    
    i = 0
    while i < len(flat_image):
        # Check for a run
        run_length = 1
        while i + run_length < len(flat_image) and run_length < max_packet_size and flat_image[i] == flat_image[i + run_length]:
            run_length += 1
        
        if run_length >= 2:
            # Write a RLE packet
            compressed_stream.append(0x80 | (run_length - 1))  # Packet header
            compressed_stream.extend(flat_image[i:i+bytes_per_pixel])  # Pixel data
            i += run_length
        else:
            # Write a raw packet
            raw_start = i
            i += 1
            while i < len(flat_image) and (i - raw_start) < (max_packet_size - 1) and (i + 1 >= len(flat_image) or flat_image[i] != flat_image[i + 1]):
                i += 1
            raw_length = i - raw_start
            compressed_stream.append(raw_length - 1)  # Packet header
            compressed_stream.extend(flat_image[raw_start:i])  # Pixel data

    return compressed_stream

def generate_complex_image(width, height):
    """
    Generate a more complex image for demonstration.
    """
    x = np.linspace(0, 1, num=width)
    y = np.linspace(0, 1, num=height)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(2 * np.pi * (2 * X + Y)) * 127 + 128
    return np.stack((Z, Z, Z), axis=-1).astype(np.uint8)

def main():
    os.makedirs('./tmp/', exist_ok=True)

    # Generate and save 24-bit RGB image with RLE compression
    complex_image = generate_complex_image(256, 256)
    save_tga('./tmp/complex_image_rle_24bit.tga', complex_image, 3, compress=True)

    # Generate and save 24-bit RGB image without RLE compression
    save_tga('./tmp/complex_image_24bit.tga', complex_image, 3, compress=False)

if __name__ == '__main__':
    main()