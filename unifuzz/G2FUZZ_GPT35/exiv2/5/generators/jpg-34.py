import numpy as np
from PIL import Image

# Creating a sample image (you can replace this with your own image generation logic)
image_data = np.random.randint(0, 255, size=(256, 256, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Adding embedded thumbnail data
thumbnail_data = np.random.randint(0, 255, size=(64, 64, 3), dtype=np.uint8)
thumbnail_image = Image.fromarray(thumbnail_data)
thumbnail_bytes = thumbnail_image.tobytes()

# Generate a sample complex JPEG file with embedded thumbnail
file_path = './tmp/compressed_image_with_thumbnail.jpg'
with open(file_path, 'wb') as file:
    file.write(b'\xFF\xD8')  # SOI (Start of Image)

    # APP0 marker segment (JFIF header)
    file.write(b'\xFF\xE0')
    file.write(b'\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00')

    # APP1 marker segment (custom metadata)
    file.write(b'\xFF\xE1')
    metadata_length = len(thumbnail_bytes) + 2
    metadata = b'Thumbnail Data'
    file.write(metadata_length.to_bytes(2, byteorder='big'))
    file.write(metadata)
    file.write(thumbnail_bytes)

    # Image data segment (fake image data)
    file.write(b'\xFF\xDB')  # DQT marker
    file.write(b'\x00\x43')  # Segment length
    file.write(b'\x00')  # Precision and destination identifier
    for j in range(64):
        file.write(j.to_bytes(1, byteorder='big'))

    file.write(b'\xFF\xD9')  # EOI (End of Image)