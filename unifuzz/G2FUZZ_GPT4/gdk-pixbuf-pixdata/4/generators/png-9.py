import os
import zlib
from PIL import Image
import numpy as np

def create_png_with_text(text, file_path):
    # Create an image with PIL
    img_size = (200, 100)  # Width, height
    image = Image.new('RGB', img_size, color = (73, 109, 137))
    
    # Convert the image to bytes
    img_bytes = image.tobytes()
    
    # Create a PNG file manually to understand CRC
    width, height = img_size
    
    # PNG file signature
    png_signature = b'\x89PNG\r\n\x1a\n'
    
    # IHDR chunk
    ihdr_chunk = b'IHDR' + (width).to_bytes(4, byteorder='big') + (height).to_bytes(4, byteorder='big') + b'\x08\x06\x00\x00\x00'
    ihdr_data_length = len(ihdr_chunk).to_bytes(4, byteorder='big')
    ihdr_crc = zlib.crc32(ihdr_chunk).to_bytes(4, byteorder='big')
    ihdr_chunk_full = ihdr_data_length + ihdr_chunk + ihdr_crc
    
    # IDAT chunk
    idat_chunk = b'IDAT'
    img_data = zlib.compress(img_bytes)
    idat_chunk += img_data
    idat_data_length = len(img_data).to_bytes(4, byteorder='big')
    idat_crc = zlib.crc32(idat_chunk).to_bytes(4, byteorder='big')
    idat_chunk_full = idat_data_length + idat_chunk + idat_crc
    
    # IEND chunk
    iend_chunk = b'IEND'
    iend_data_length = (0).to_bytes(4, byteorder='big')
    iend_crc = zlib.crc32(iend_chunk).to_bytes(4, byteorder='big')
    iend_chunk_full = iend_data_length + iend_chunk + iend_crc
    
    # Combine all chunks
    png_data = png_signature + ihdr_chunk_full + idat_chunk_full + iend_chunk_full
    
    # Save to file
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as f:
        f.write(png_data)

# Create a PNG file with CRC for robust error detection
create_png_with_text("Robust Error Detection: PNG files include a CRC (Cyclic Redundancy Check) for each chunk of data, ensuring high integrity of the data and robust error detection capabilities.", "./tmp/robust_error_detection.png")