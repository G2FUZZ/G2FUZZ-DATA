import struct

def create_ico_file(file_path, images):
    ico_header = struct.pack(
        "<HHH",
        0,  # Reserved, must be 0
        1,  # Type 1 for ICO files
        len(images)  # Number of images in the file
    )

    with open(file_path, "wb") as f:
        f.write(ico_header)

        image_offset = len(images) * 16 + 6  # Size of header + image directory entries
        for image_data in images:
            width, height, data = image_data
            image_directory = struct.pack(
                "<BBBBHHII",
                width if width <= 255 else 0,  # Width
                height if height <= 255 else 0,  # Height
                0,  # Color count
                0,  # Reserved, must be 0
                1,  # Color planes
                32,  # Bits per pixel
                len(data),  # Image data size
                image_offset  # Offset of image data in the file
            )
            f.write(image_directory)
            image_offset += len(data)

        for width, height, data in images:
            f.write(data)

# Generate ICO files with different images representing various states
images = [
    (32, 32, b"\x00\x00\xFF\xFF" * 32 * 32),  # Example: Blue square icon
    (64, 64, b"\xFF\x00\x00\xFF" * 64 * 64),  # Example: Red square icon
]

file_path = "./tmp/example.ico"
create_ico_file(file_path, images)