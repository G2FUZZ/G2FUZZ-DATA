import os
import datetime

def create_ras_file_with_metadata(filename, width, height, metadata):
    # RAS file header consists of 32 bytes
    # Magic (4 bytes), Width (4 bytes), Height (4 bytes),
    # Depth (4 bytes), Length (4 bytes), Type (4 bytes),
    # MapType (4 bytes), MapLength (4 bytes)
    magic = b'\x59\xA6\x6A\x95'  # RAS magic number
    depth = 24  # Assuming 24 bits per pixel (RGB)
    length = width * height * 3  # Image data size
    header = magic + width.to_bytes(4, byteorder='big') + height.to_bytes(4, byteorder='big') \
             + depth.to_bytes(4, byteorder='big') + length.to_bytes(4, byteorder='big') \
             + (0).to_bytes(4, byteorder='big')*3  # Type, MapType, and MapLength set to 0
    
    # Simulating image data: filling with black pixels
    image_data = b'\x00' * length
    
    # Metadata as bytes
    metadata_bytes = metadata.encode('utf-8')
    
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Write the header, image data, and metadata to file
    with open(f'./tmp/{filename}', 'wb') as file:
        file.write(header)
        file.write(image_data)
        # Write metadata at the end of the file
        file.write(b'\nMetadata:\n')
        file.write(metadata_bytes)

# Example metadata
metadata = "Creator: John Doe\nCreation Date: {}\nDescription: Just a simple RAS file.".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# Creating a simple 100x100 RAS file with metadata
create_ras_file_with_metadata('example.ras', 100, 100, metadata)