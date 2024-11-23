import struct

# Function to create a BMP file with metadata
def create_bmp_with_metadata(width, height, resolution, color_profile):
    # BMP file header
    file_type = b'BM'
    file_size = 54 + width * height * 3
    reserved1 = 0
    reserved2 = 0
    offset = 54

    # DIB header
    dib_header_size = 40
    image_width = width
    image_height = height
    planes = 1
    bits_per_pixel = 24
    compression = 0
    image_size = 0
    x_resolution = resolution
    y_resolution = resolution
    colors = 0
    important_colors = 0

    # Create BMP file
    with open(f'./tmp/metadata_example.bmp', 'wb') as bmp_file:
        # Write BMP file header
        bmp_file.write(file_type)
        bmp_file.write(struct.pack('<I', file_size))
        bmp_file.write(struct.pack('<H', reserved1))
        bmp_file.write(struct.pack('<H', reserved2))
        bmp_file.write(struct.pack('<I', offset))

        # Write DIB header
        bmp_file.write(struct.pack('<I', dib_header_size))
        bmp_file.write(struct.pack('<I', image_width))
        bmp_file.write(struct.pack('<I', image_height))
        bmp_file.write(struct.pack('<H', planes))
        bmp_file.write(struct.pack('<H', bits_per_pixel))
        bmp_file.write(struct.pack('<I', compression))
        bmp_file.write(struct.pack('<I', image_size))
        bmp_file.write(struct.pack('<I', x_resolution))
        bmp_file.write(struct.pack('<I', y_resolution))
        bmp_file.write(struct.pack('<I', colors))
        bmp_file.write(struct.pack('<I', important_colors))

        # Add metadata (color profile) at the end of the BMP file
        bmp_file.write(color_profile)

# Define metadata (color profile)
color_profile = b'Metadata: Color profile - sRGB'

# Generate BMP file with metadata
create_bmp_with_metadata(200, 200, 300, color_profile)