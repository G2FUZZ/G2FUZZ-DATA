import struct

def create_ico_file_with_features(file_name, images_data):
    # ICO Header
    ico_header = struct.pack('<HHH', 0, 1, len(images_data))  # Reserved, Type, Number of Images
    
    ico_data = b''
    offset = len(ico_header) + len(images_data) * 16
    
    for image in images_data:
        # Ensure values are within the valid range
        width = min(image['width'], 255)
        height = min(image['height'], 255)
        color_count = min(image['color_count'], 255)
        reserved = min(image['reserved'], 255)
        
        # ICO Image Directory
        image_data = struct.pack('<BBBBHHII', width, height, color_count, reserved,
                                 image['planes'], image['bit_count'], image['image_size'], offset)
        ico_data += image_data
        offset += image['image_size']
    
    # Write ICO file
    with open(file_name, 'wb') as f:
        f.write(ico_header)
        f.write(ico_data)
        for image in images_data:
            f.write(image['image_bytes'])

# Create ICO files with multiple image sizes and color depths
images_data = [
    {'width': 16, 'height': 16, 'color_count': 256, 'reserved': 0, 'planes': 1, 'bit_count': 8,
     'image_size': 40, 'image_bytes': b'\x01\x00\x01\x00\x20\x00\x20\x20\x00\x00\x00\x00\x00\x00\x00\x00'},
    {'width': 32, 'height': 32, 'color_count': 256, 'reserved': 0, 'planes': 1, 'bit_count': 8,
     'image_size': 40, 'image_bytes': b'\x02\x00\x02\x00\x20\x00\x20\x20\x00\x00\x00\x00\x00\x00\x00\x00'}
]

create_ico_file_with_features('./tmp/multi_size_icon.ico', images_data)