import numpy as np

# Create a 32x32 transparent image with an alpha channel
image = np.zeros((32, 32, 4), dtype=np.uint8)
image[:, :, 3] = 128  # Set alpha channel to 128 (50% opacity)

# Save the image as a TGA file
with open('./tmp/transparent_image.tga', 'wb') as f:
    # Write header
    header = bytearray([0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 0, 32, 0])
    f.write(header)
    
    # Write image data
    f.write(image.tobytes())