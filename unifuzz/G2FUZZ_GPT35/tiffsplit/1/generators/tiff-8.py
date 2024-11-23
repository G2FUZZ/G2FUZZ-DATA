import numpy as np
from PIL import Image

# Create a simple black and white image
data = np.zeros((100, 100), dtype=np.uint8)
data[25:75, 25:75] = 255  # Add a white square in the middle

# Set some example tags
tags = {
    256: 100,  # Image width
    257: 100,  # Image height
    258: 8,    # Bits per sample
    259: 1,    # Compression (1 = no compression)
    262: 0,    # Photometric interpretation (0 = white is zero)
    274: 1,    # Orientation
    277: 1,    # Samples per pixel
    282: (72, 1),  # X resolution
    283: (72, 1),  # Y resolution
}

# Create a new image with the specified tags
img = Image.fromarray(data)
img.save("./tmp/example.tiff", tiffinfo=tags)