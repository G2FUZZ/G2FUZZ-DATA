import struct

def create_ico_file(file_name):
    # ICO file header
    ico_header = bytearray.fromhex('000100010000000000200000000000002000000001000000060000000010000000')

    # ICO file directory entry
    icon_entry = bytearray.fromhex('000000000100010000000000000000000000000000000000')

    # Create a 16x16 transparent icon
    icon_data = bytearray.fromhex('1000000010000000010000000100000001000000010000000100000001000000'
                                  '0100000001000000010000000100000001000000010000000100000001000000'
                                  '01000000ffffffff00000000ffffffff00000000ffffffff00000000ffffffff')

    with open(file_name, 'wb') as file:
        # Write ICO file header
        file.write(ico_header)

        # Write ICO file directory entry
        file.write(icon_entry)

        # Write icon data
        file.write(icon_data)

# Create and save ICO file
file_name = './tmp/cross_platform_support.ico'
create_ico_file(file_name)
print(f'ICO file "{file_name}" created successfully.')