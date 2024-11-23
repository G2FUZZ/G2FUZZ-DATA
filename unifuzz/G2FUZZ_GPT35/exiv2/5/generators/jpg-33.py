import numpy as np
from PIL import Image

# Creating a sample image (you can replace this with your own image generation logic)
image_data = np.random.randint(0, 255, size=(256, 256, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Adding embedded thumbnail data
thumbnail_data = np.random.randint(0, 255, size=(64, 64, 3), dtype=np.uint8)
thumbnail_image = Image.fromarray(thumbnail_data)
thumbnail_bytes = thumbnail_image.tobytes()

# Save the image in JPEG format with DCT compression, Chroma subsampling, Progressive display, and Embedded thumbnails
file_path = './tmp/compressed_image_with_thumbnail.jpg'
with open(file_path, 'wb') as file:
    file.write(b'\xFF\xD8')  # SOI (Start of Image)

    # APP0 marker segment (JFIF header)
    file.write(b'\xFF\xE0')
    file.write(b'\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00')

    # APP1 marker segment (custom metadata)
    file.write(b'\xFF\xE1')
    metadata_length = 30
    metadata = b'Custom Metadata: Hello, World!'
    file.write(metadata_length.to_bytes(2, byteorder='big'))
    file.write(metadata)

    # Multiple image data segments (fake image data)
    for i in range(3):
        file.write(b'\xFF\xDB')  # DQT marker
        file.write(b'\x00\x43')  # Segment length
        file.write(b'\x00')  # Precision and destination identifier
        for j in range(64):
            file.write(j.to_bytes(1, byteorder='big'))

    file.write(b'\xFF\xD9')  # EOI (End of Image)