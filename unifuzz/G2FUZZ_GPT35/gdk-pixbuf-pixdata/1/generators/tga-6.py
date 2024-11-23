import numpy as np

# Define image dimensions
width = 100
height = 100

# Create a monochrome image (black and white)
image = np.zeros((height, width), dtype=np.uint8)

# Save the image as a 'tga' file
with open('./tmp/monochrome_image.tga', 'wb') as f:
    f.write(b'\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    f.write(width.to_bytes(2, byteorder='little'))
    f.write(height.to_bytes(2, byteorder='little'))
    f.write(b'\x08')
    f.write(image.tobytes())