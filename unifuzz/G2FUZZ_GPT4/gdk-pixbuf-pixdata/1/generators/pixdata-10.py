import os
import struct

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_pixdata_file(filename, pixels, endianess='little'):
    """
    Creates a pixdata file with specified endianness.
    
    :param filename: The name of the file to save the pixel data.
    :param pixels: A list of pixel values represented as tuples of RGBA.
    :param endianess: The byte order ('little' or 'big').
    """
    # Determine the format string for struct.pack based on endianness
    format_string = '<I' if endianess == 'little' else '>I'
    
    with open(filename, 'wb') as file:
        for pixel in pixels:
            # Pack each pixel as a 32-bit unsigned integer
            data = struct.pack(format_string, 
                               (pixel[0] << 24) +  # Red
                               (pixel[1] << 16) +  # Green
                               (pixel[2] << 8) +   # Blue
                               pixel[3])           # Alpha
            file.write(data)

# Pixel data for a 2x2 image [(R, G, B, A), ...]
pixels = [(255, 0, 0, 255), (0, 255, 0, 255), 
          (0, 0, 255, 255), (255, 255, 0, 255)]

# Create pixdata files with different endianness
create_pixdata_file('./tmp/pixdata_little_endian.bin', pixels, 'little')
create_pixdata_file('./tmp/pixdata_big_endian.bin', pixels, 'big')

print('Pixdata files with specified endianness have been created.')