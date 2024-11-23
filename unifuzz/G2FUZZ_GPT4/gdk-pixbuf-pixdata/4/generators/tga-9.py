import os
import struct

def create_tga_header(width, height, bpp, image_type):
    # TGA Header
    # idlength (1 byte): length of ID field that follows 18 byte header (0)
    # colormaptype (1 byte): no color map included (0)
    # datatypecode (1 byte): uncompressed true-color image (2)
    # colormaporigin (2 bytes): not used
    # colormaplength (2 bytes): not used
    # colormapdepth (1 byte): not used
    # x_origin (2 bytes): not used
    # y_origin (2 bytes): not used
    # width (2 bytes): width of the image
    # height (2 bytes): height of the image
    # bitsperpixel (1 byte): image pixel size
    # imagedescriptor (1 byte): image descriptor byte (0)
    header = struct.pack('<BBBHHBHHHHBB',
                         0, 0, image_type,
                         0, 0, 0,
                         0, 0,
                         width, height,
                         bpp, 0)
    return header

def create_dummy_image_data(width, height, bpp):
    # Create dummy data for demonstration, simple gradient effect
    data = []
    max_val = 255
    for y in range(height):
        for x in range(width):
            # Simple gradient: R, G, and B change with x and y to create a gradient effect
            r = (x / width) * max_val
            g = (y / height) * max_val
            b = ((x + y) / (width + height)) * max_val
            if bpp == 32:  # If 32 bits per pixel, add an alpha value
                a = max_val
                data.extend([int(b), int(g), int(r), int(a)])
            else:  # Else, assume 24 bpp
                data.extend([int(b), int(g), int(r)])
    return bytearray(data)

def save_tga(file_path, width, height, bpp, image_type):
    header = create_tga_header(width, height, bpp, image_type)
    data = create_dummy_image_data(width, height, bpp)
    with open(file_path, 'wb') as f:
        f.write(header)
        f.write(data)
        
def save_multiple_images_in_one_tga(directory, images_info):
    os.makedirs(directory, exist_ok=True)
    for idx, info in enumerate(images_info):
        file_path = os.path.join(directory, f'image_{idx}.tga')
        width, height, bpp, image_type = info
        save_tga(file_path, width, height, bpp, image_type)
    # Note: TGA doesn't natively support multiple images in one file in a standard way.
    # This will create separate TGA files for demonstration purposes.
    print(f"Saved {len(images_info)} images in '{directory}'")

# Example usage
images_info = [
    # width, height, bits per pixel, image type (2 for uncompressed true-color image)
    (100, 100, 24, 2),
    (200, 150, 32, 2)  # Including alpha channel
]
save_multiple_images_in_one_tga('./tmp/', images_info)