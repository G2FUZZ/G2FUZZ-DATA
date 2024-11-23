import os
import struct
from PIL import Image

def rle_encode(data):
    """Run-length encode the input data"""
    encoding = []
    prev_char = data[0]
    count = 1
    for char in data[1:]:
        if char == prev_char:
            count += 1
        else:
            encoding.append((count, prev_char))
            count = 1
            prev_char = char
    encoding.append((count, prev_char))
    return encoding

def save_pixdata(image, filename):
    """Save an image in a custom pixdata format with RLE compression"""
    # Convert the image to grayscale for simplicity
    grayscale = image.convert("L")
    width, height = grayscale.size
    
    # Extract raw pixels
    pixels = list(grayscale.getdata())
    
    # Compress the pixel data
    compressed_pixels = rle_encode(pixels)
    
    # Create the file header
    # Format: [width (4 bytes), height (4 bytes), number of RLE entries (4 bytes)]
    header = struct.pack("III", width, height, len(compressed_pixels))
    
    # Write the header and compressed pixel data to the file
    with open(filename, 'wb') as f:
        f.write(header)
        for count, value in compressed_pixels:
            # Each RLE entry: [run-length (4 bytes), pixel value (1 byte)]
            entry = struct.pack("IB", count, value)
            f.write(entry)

try:
    # Example usage
    image = Image.open('./tmp/striped_image.png')
    save_pixdata(image, './tmp/striped_image.pixdata')
    print("Pixdata file saved.")
except FileNotFoundError:
    print("FileNotFoundError: The specified file was not found.")
    print("Current working directory:", os.getcwd())
    print("Please check the file path or consider using an absolute path.")