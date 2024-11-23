from PIL import Image

def create_rle_bmp(filename, mode, size, color):
    # Create a new image with the specified mode and size
    # Modes can be 'P' for 8-bit or 'L' for 4-bit in this context
    # Size is a tuple (width, height), and color is the fill color
    img = Image.new(mode, size, color)
    
    # Save the image with RLE compression
    # RLE compression is specified with the 'BMP RLE' format for Pillow
    img.save(filename, format='BMP', bits=4 if mode == 'L' else 8, compression='BMP RLE')
    
# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create an 8-bit RLE compressed BMP file
create_rle_bmp('./tmp/8bit_rle_compressed.bmp', 'P', (100, 100), 'blue')

# Create a 4-bit RLE compressed BMP file by using a grayscale color
create_rle_bmp('./tmp/4bit_rle_compressed.bmp', 'L', (100, 100), 128)