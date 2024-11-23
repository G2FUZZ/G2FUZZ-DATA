import numpy as np

# Define image dimensions
width = 256
height = 256

# Create image data
image_data = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)

# Set origin location
origin_top_left = True

# Define TGA header
header = bytearray([
    0,  # ID length
    0,  # Color map type
    2,  # Image type (truecolor)
    0, 0, 0, 0, 0,  # Color map specification
    0, 0,  # X-origin
    width % 256, width // 256,  # Image width
    height % 256, height // 256,  # Image height
    24,  # Pixel depth
    32  # Image descriptor
])

# Set origin location in the header
if len(header) > 17:
    if origin_top_left:
        header[17] = 0
    else:
        header[17] = 1
else:
    print("Error: Index 17 is out of range in the header.")

# Write data to TGA file
filename = "./tmp/generated_image.tga"
with open(filename, 'wb') as f:
    f.write(header)
    f.write(image_data)

print(f"TGA file generated with origin location at {'top-left' if origin_top_left else 'bottom-left'} saved as '{filename}'")