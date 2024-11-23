import numpy as np
import os

def write_tga(filename, data, width, height, origin_top_left=False):
    """
    Write data to a TGA file.
    
    :param filename: The name of the file.
    :param data: Pixel data.
    :param width: Image width.
    :param height: Image height.
    :param origin_top_left: Whether the origin is at the top-left.
    """
    header = bytearray(18)
    header[2] = 2  # Image type: uncompressed true-color image
    header[12] = width & 0xFF
    header[13] = (width >> 8) & 0xFF
    header[14] = height & 0xFF
    header[15] = (height >> 8) & 0xFF
    header[16] = 24  # Bits per pixel
    if origin_top_left:
        header[17] = 0x20  # Set the origin to top-left

    with open(filename, 'wb') as f:
        f.write(header)
        f.write(data)

def create_image(width, height, red_bottom_row=True):
    """
    Create a simple image with either a red bottom or top row.
    
    :param width: Image width.
    :param height: Image height.
    :param red_bottom_row: Whether the bottom row is red.
    :return: Image data.
    """
    image_data = np.zeros((height, width, 3), dtype=np.uint8)
    if red_bottom_row:
        image_data[-1, :, 0] = 255  # Set the bottom row to red
    else:
        image_data[0, :, 0] = 255  # Set the top row to red
    return image_data

def main():
    width, height = 100, 100
    output_dir = './tmp/'
    os.makedirs(output_dir, exist_ok=True)
    
    # Create and save an image with the bottom-left origin
    bl_image = create_image(width, height, red_bottom_row=True)
    bl_filename = os.path.join(output_dir, 'bottom_left_origin.tga')
    write_tga(bl_filename, bl_image.tobytes(), width, height)
    
    # Create and save an image with the top-left origin
    tl_image = create_image(width, height, red_bottom_row=False)
    tl_filename = os.path.join(output_dir, 'top_left_origin.tga')
    write_tga(tl_filename, tl_image.tobytes(), width, height, origin_top_left=True)
    
    print(f"Generated TGA files at: {output_dir}")

if __name__ == "__main__":
    main()