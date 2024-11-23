import numpy as np
from PIL import Image

# Create a colorful image with multiple layers
data = np.zeros((200, 200, 3), dtype=np.uint8)
data[:100, :100, 0] = 255  # Red square in the top-left
data[100:, :100, 1] = 255  # Green square in the bottom-left
data[:100, 100:, 2] = 255  # Blue square in the top-right

# Set more detailed tags for the TIFF image
tags = {
    256: 200,   # Image width
    257: 200,   # Image height
    258: 8,     # Bits per sample
    259: 1,     # Compression (1 = no compression)
    262: 2,     # Photometric interpretation (2 = RGB)
    274: 1,     # Orientation
    277: 3,     # Samples per pixel (RGB)
    282: (300, 1),  # X resolution
    283: (300, 1),  # Y resolution
    37724: b"Layer Support",  # Custom tag for Layer Support feature
    37725: b"Advanced Color Channels",  # Custom tag for Advanced Color Channels
    40001: b"Layer 1",  # Custom tag for Layer 1
    40002: b"Layer 2",  # Custom tag for Layer 2
    40003: b"Layer 3"   # Custom tag for Layer 3
}

# Create a new image with the specified tags
img = Image.fromarray(data)
img.save("./tmp/complex_example.tiff", tiffinfo=tags)