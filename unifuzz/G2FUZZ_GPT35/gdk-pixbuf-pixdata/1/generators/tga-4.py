import struct

def create_tga_file(width, height, color_map_type, image_type, file_path):
    # Define TGA header
    tga_header = bytearray([0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, width & 0xFF, (width >> 8) & 0xFF, height & 0xFF, (height >> 8) & 0xFF, 24, 0])
    
    # Write TGA header to file
    with open(file_path, 'wb') as f:
        f.write(tga_header)
    
    print(f"TGA file with metadata created at {file_path}")

# Define metadata
width = 640
height = 480
color_map_type = 0
image_type = 2
file_path = "./tmp/metadata_example.tga"

# Create TGA file with metadata
create_tga_file(width, height, color_map_type, image_type, file_path)