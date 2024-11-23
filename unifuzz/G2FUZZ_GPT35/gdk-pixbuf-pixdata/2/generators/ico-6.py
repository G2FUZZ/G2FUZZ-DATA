import io
import struct

def create_ico_file():
    # ICO file header
    ico_header = struct.pack('<HHH', 0, 1, 1)  # Reserved, Type, Number of Images

    # ICO image directory
    image_directory = struct.pack('<BBBBHHII', 32, 32, 0, 0, 1, 24, 0, 0)  # Width, Height, Color Count, Reserved, Planes, Bit Count, Bytes In Res, Image Offset

    # Create ICO file content by concatenating header and image directory
    ico_content = ico_header + image_directory

    # Save the ICO content to a file
    with open('./tmp/platform_independence.ico', 'wb') as file:
        file.write(ico_content)

create_ico_file()