import struct

# Function to create ICO file header
def create_ico_header(num_images):
    reserved = 0
    type = 1
    num_images = min(num_images, 255)  # Limit to 255 images
    return struct.pack('<HHH', reserved, type, num_images)

# Function to create ICONDIR entry for each image
def create_icon_dir_entry(width, height, size, offset):
    width = min(width, 255)
    height = min(height, 255)
    return struct.pack('<BBBBHHII', width, height, 0, 0, 1, 0, size, offset)

# Function to create an ICO file with given image data
def create_ico_file(images):
    num_images = len(images)
    header = create_ico_header(num_images)
    icondir_entries = []
    image_data = b''
    offset = 6 + 16 * num_images

    for image in images:
        width, height = image.size
        size = len(image.data)
        icondir_entries.append(create_icon_dir_entry(width, height, size, offset))
        image_data += image.data
        offset += size

    ico_data = header + b''.join(icondir_entries) + image_data

    with open('./tmp/cross_platform_support.ico', 'wb') as f:
        f.write(ico_data)

# Define image class to hold size and data
class Image:
    def __init__(self, size, data):
        self.size = size
        self.data = data

# Generate ICO file with one image
image_data = b'\x00\x00\x00\x00'  # Placeholder image data
image_size = (16, 16)  # Image size (width, height)
image = Image(image_size, image_data)
create_ico_file([image])