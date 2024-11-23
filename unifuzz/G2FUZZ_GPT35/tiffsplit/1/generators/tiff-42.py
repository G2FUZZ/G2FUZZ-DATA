import numpy as np
from PIL import Image

# Create a multi-layered image with different patterns
layer1 = np.zeros((100, 100), dtype=np.uint8)
layer1[10:30, 10:30] = 255  # Add a white square in the top-left corner

layer2 = np.zeros((100, 100), dtype=np.uint8)
layer2[40:60, 40:60] = 255  # Add a white square in the middle

layer3 = np.zeros((100, 100), dtype=np.uint8)
layer3[70:90, 70:90] = 255  # Add a white square in the bottom-right corner

# Set additional metadata tags for each layer
tags_layer1 = {
    37724: b"Layer 1 Metadata"
}

tags_layer2 = {
    37724: b"Layer 2 Metadata"
}

tags_layer3 = {
    37724: b"Layer 3 Metadata"
}

# Combine tag dictionaries into a single dictionary
combined_tags = {**tags_layer1, **tags_layer2, **tags_layer3}

# Create a new multi-layered image with specified tags for each layer
img = Image.new('RGBA', (100, 100))
img.paste(Image.fromarray(layer1), (0, 0))
img.paste(Image.fromarray(layer2), (0, 0), mask=Image.fromarray(layer2))
img.paste(Image.fromarray(layer3), (0, 0), mask=Image.fromarray(layer3))

# Save the multi-layered image with additional metadata
img.save("./tmp/multi_layer_image.tiff", tiffinfo=combined_tags)