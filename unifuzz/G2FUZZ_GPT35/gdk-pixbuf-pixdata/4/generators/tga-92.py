import struct

# Function to create a TGA file with extended metadata and image data
def create_complex_tga_file(file_name, width, height, color_map, developer_data, image_data):
    header = bytearray([0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, (width % 256), (width // 256), (height % 256), (height // 256), 24, 32])

    # Color map data (not fully implemented in this example)
    color_map_data = bytearray(color_map)

    # Developer-specific data
    developer_data_length = len(developer_data)
    developer_data_field = bytearray(developer_data_length.to_bytes(2, byteorder='little'))
    developer_data_field += bytearray(developer_data, 'utf-8')

    # Image data
    image_data_field = bytearray(image_data)

    with open(file_name, 'wb') as file:
        file.write(header)
        file.write(color_map_data)
        file.write(developer_data_field)
        file.write(image_data_field)

# Create a TGA file with extended metadata and image data
file_name = './tmp/complex_metadata_example.tga'
width = 200
height = 200
color_map = []  # Color map not fully implemented in this example
developer_data = "This is developer-specific data for the TGA file."
image_data = b'\x00\xFF\x00' * (width * height)  # Example: Green image

create_complex_tga_file(file_name, width, height, color_map, developer_data, image_data)