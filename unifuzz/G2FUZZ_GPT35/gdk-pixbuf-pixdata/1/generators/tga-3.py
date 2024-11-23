import numpy as np

# Define image size
width = 100
height = 100

# Create alpha channel data
alpha_channel = np.random.randint(0, 256, (height, width), dtype=np.uint8)

# Save alpha channel to a TGA file
with open('./tmp/alpha_channel.tga', 'wb') as f:
    # Write TGA header
    f.write(bytearray([0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, width % 256, width // 256, height % 256, height // 256, 32, 8]))

    # Write alpha channel data
    f.write(alpha_channel.tobytes())