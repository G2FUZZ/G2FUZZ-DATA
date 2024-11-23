import struct

def create_ico(color_depth, output_file):
    # ICO header
    ico_header = struct.pack("<HHH", 0, 1, 1)  # Reserved, Type, Count

    # ICO image directory
    if color_depth == "monochrome":
        width, height = 32, 32
        color_palette = b"\x00\x00\x00\x00\xFF\xFF\xFF\x00"  # Black and White
    elif color_depth == "truecolor":
        width, height = 64, 64
        color_palette = b"\xFF\x00\x00\x00\xFF\xFF\xFF\x00"  # Red and White
    else:
        print("Unsupported color depth.")
        return

    image_directory = struct.pack("<BBBBHHII", width, height, 0, 0, 1, 0, len(ico_header) + len(color_palette), len(color_palette))

    # Write ICO file
    with open(output_file, "wb") as file:
        file.write(ico_header)
        file.write(image_directory)
        file.write(color_palette)

# Create ICO files
create_ico("monochrome", "./tmp/monochrome.ico")
create_ico("truecolor", "./tmp/truecolor.ico")