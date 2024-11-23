import struct

# Function to create ICO file header
def create_ico_header(num_images):
    reserved = 0
    type = 1
    num_images = num_images

    # Create ICO header
    ico_header = struct.pack('<H', reserved)
    ico_header += struct.pack('<H', type)
    ico_header += struct.pack('<H', num_images)

    return ico_header

# Function to create ICO file with the given icon data
def create_ico_file(icon_data, file_name):
    ico_header = create_ico_header(1)

    with open(file_name, 'wb') as f:
        f.write(ico_header)
        f.write(icon_data)

# Create an example icon data (16x16 pixels)
icon_data = bytes.fromhex('00000000010000001000180000000001040001F00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

# Save the icon data to an ICO file
create_ico_file(icon_data, './tmp/example_icon.ico')