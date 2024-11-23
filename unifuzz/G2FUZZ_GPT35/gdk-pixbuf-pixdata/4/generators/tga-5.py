import struct

# Function to create a TGA file with metadata
def create_tga_file(file_name, width, height, color_map, developer_data):
    header = bytearray([0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, (width % 256), (width // 256), (height % 256), (height // 256), 24, 32])

    # Color map data (not implemented in this example)
    color_map_data = bytearray(color_map)

    # Developer-specific data
    developer_data_length = len(developer_data)
    developer_data_field = bytearray(developer_data_length.to_bytes(2, byteorder='little'))
    developer_data_field += bytearray(developer_data, 'utf-8')

    with open(file_name, 'wb') as file:
        file.write(header)
        file.write(color_map_data)
        file.write(developer_data_field)

# Create a TGA file with metadata
file_name = './tmp/metadata_example.tga'
width = 100
height = 100
color_map = []  # Color map not implemented in this example
developer_data = "This is developer-specific data for the TGA file."

create_tga_file(file_name, width, height, color_map, developer_data)