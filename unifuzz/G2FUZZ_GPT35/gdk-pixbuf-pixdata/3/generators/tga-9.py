import os

# Function to generate a TGA file with extension area
def generate_tga_with_extension(extension_data, output_file):
    # TGA file header
    tga_header = bytearray([
        0, 0, 2,             # ID length, color map type, image type
        0, 0, 0, 0, 0,      # Color map specification
        0, 0,               # X-origin
        0, 0,               # Y-origin
        0, 0,               # Width
        0, 0,               # Height
        24,                 # Pixel depth
        32,                 # Image descriptor
    ])

    # Extension area header
    extension_area_header = bytearray([
        0, 0, 0, 0, 0, 0,   # Extension size
        0, 0, 0, 0, 0,      # Developer directory offset
        0, 0,               # Tags offset
    ])

    # Extension area data
    extension_data_bytes = extension_data.encode('utf-8')

    # Update extension area header with extension size
    extension_area_header[0] = len(extension_data_bytes) // 256
    extension_area_header[1] = len(extension_data_bytes) % 256

    # Write TGA file
    with open(output_file, 'wb') as f:
        f.write(tga_header)
        f.write(extension_area_header)
        f.write(extension_data_bytes)

# Generate and save TGA file with extension area
extension_data = "Additional information or custom data"
output_file = "./tmp/generated_tga_with_extension.tga"
generate_tga_with_extension(extension_data, output_file)