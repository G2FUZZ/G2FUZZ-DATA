import os
import numpy as np

def save_tga(filename, image_data, bit_depth):
    """
    Save an image as a TGA file with specified bit depth.
    """
    header = bytearray(18)
    header[2] = 2  # Image type: uncompressed true-color image.
    header[12:14] = (image_data.shape[1] & 0xFF, image_data.shape[1] >> 8 & 0xFF)  # Image width.
    header[14:16] = (image_data.shape[0] & 0xFF, image_data.shape[0] >> 8 & 0xFF)  # Image height.
    header[16] = bit_depth * 8  # Color depth per pixel.
    header[17] = 0x20  # Image descriptor (top-left origin).

    with open(filename, 'wb') as f:
        f.write(header)
        image_data.tofile(f)

def generate_color_gradient(width, height, with_alpha=False):
    """
    Generate a simple color gradient image.
    """
    # Create a gradient for each color channel
    x = np.linspace(0, 255, num=width, dtype=np.uint8)
    gradient = np.tile(x, (height, 1))

    if with_alpha:
        # Add an alpha channel filled with 255
        alpha_channel = np.full((height, width), 255, dtype=np.uint8)
        return np.dstack((gradient, gradient, gradient, alpha_channel))
    else:
        return np.dstack((gradient, gradient, gradient))

def main():
    os.makedirs('./tmp/', exist_ok=True)

    # Generate and save 8-bit grayscale image
    grayscale_image = generate_color_gradient(100, 100).mean(axis=2).astype(np.uint8)
    save_tga('./tmp/grayscale_8bit.tga', grayscale_image, 1)

    # Generate and save 16-bit image (5 bits for R, G, B, and 1 bit for unused)
    rgb_16bit_image = np.dstack((grayscale_image // 8, grayscale_image // 8, grayscale_image // 8, np.zeros_like(grayscale_image)))
    save_tga('./tmp/rgb_16bit.tga', rgb_16bit_image, 2)

    # Generate and save 24-bit RGB image
    rgb_24bit_image = generate_color_gradient(100, 100)
    save_tga('./tmp/rgb_24bit.tga', rgb_24bit_image, 3)

    # Generate and save 32-bit RGBA image
    rgba_32bit_image = generate_color_gradient(100, 100, with_alpha=True)
    save_tga('./tmp/rgba_32bit.tga', rgba_32bit_image, 4)

if __name__ == '__main__':
    main()