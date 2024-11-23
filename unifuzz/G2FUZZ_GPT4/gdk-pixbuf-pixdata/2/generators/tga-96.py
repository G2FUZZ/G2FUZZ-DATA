import os
import numpy as np

def save_tga(filename, image_data, color_mode, compress=False):
    """
    Save an image as a TGA file with specified color mode and optional RLE compression.
    color_mode: 'grayscale', 'rgb', or 'rgba'
    """
    if color_mode == 'grayscale':
        bit_depth = 1
        image_type = 3  # Uncompressed black-and-white image.
    elif color_mode == 'rgb':
        bit_depth = 3
    elif color_mode == 'rgba':
        bit_depth = 4
    else:
        raise ValueError("Unsupported color mode.")

    if compress:
        image_type = 10 if bit_depth in [3, 4] else 11  # RLE True-color or Black-and-White image.
        pixel_data = rle_compress(image_data, bit_depth)
    else:
        image_type = 2 if bit_depth in [3, 4] else 3  # Uncompressed true-color or black-and-white image.
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
    Compress image data using RLE for TGA files, optimized for different bit depths.
    """
    max_packet_size = 128
    
    if bit_depth == 1:
        bytes_per_pixel = 1
    elif bit_depth in [3, 4]:
        bytes_per_pixel = bit_depth
    else:
        raise ValueError("Unsupported bit depth for RLE compression.")

    flat_image = image_data.flatten()
    compressed_stream = bytearray()
    
    i = 0
    while i < len(flat_image):
        run_length = 1
        while i + run_length * bytes_per_pixel < len(flat_image) and run_length < max_packet_size:
            if np.array_equal(flat_image[i:i+bytes_per_pixel], flat_image[i+run_length*bytes_per_pixel:i+(run_length+1)*bytes_per_pixel]):
                run_length += 1
            else:
                break
        
        if run_length >= 2:
            compressed_stream.append(0x80 | (run_length - 1))
            compressed_stream.extend(flat_image[i:i+bytes_per_pixel])
            i += run_length * bytes_per_pixel
        else:
            raw_start = i
            i += bytes_per_pixel
            while i < len(flat_image) and (i - raw_start) < (max_packet_size - 1) * bytes_per_pixel and (i + bytes_per_pixel >= len(flat_image) or not np.array_equal(flat_image[i:i+bytes_per_pixel], flat_image[i+bytes_per_pixel:i+2*bytes_per_pixel])):
                i += bytes_per_pixel
            raw_length = (i - raw_start) // bytes_per_pixel
            compressed_stream.append(raw_length - 1)
            compressed_stream.extend(flat_image[raw_start:i])

    return compressed_stream

def generate_complex_image(width, height, color_mode):
    """
    Generate a complex image for demonstration, supporting different color modes.
    """
    x = np.linspace(0, 1, num=width)
    y = np.linspace(0, 1, num=height)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(2 * np.pi * (2 * X + Y)) * 127 + 128

    if color_mode == 'grayscale':
        return Z.astype(np.uint8)
    elif color_mode == 'rgb' or color_mode == 'rgba':
        image = np.stack((Z, Z, Z), axis=-1).astype(np.uint8)
        if color_mode == 'rgba':
            alpha_channel = np.full((height, width, 1), 255, dtype=np.uint8)  # Full opacity
            image = np.concatenate((image, alpha_channel), axis=-1)
        return image

def main():
    os.makedirs('./tmp/', exist_ok=True)

    # Generate and save images in different color modes with and without RLE compression
    for color_mode in ['grayscale', 'rgb', 'rgba']:
        image = generate_complex_image(256, 256, color_mode)
        save_tga(f'./tmp/complex_image_{color_mode}_rle.tga', image, color_mode, compress=True)
        save_tga(f'./tmp/complex_image_{color_mode}.tga', image, color_mode, compress=False)

if __name__ == '__main__':
    main()