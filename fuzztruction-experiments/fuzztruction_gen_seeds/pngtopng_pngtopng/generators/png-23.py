import os
import numpy as np
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate horizontal gradient image
width, height = 256, 256
base_layer = np.zeros((height, width, 3), dtype=np.uint8)

# Create gradient for the base layer
for x in range(width):
    for y in range(height):
        base_layer[y, x] = [x, x, x]  # RGB channels

# Generate an additional layer with a different pattern (for demonstration)
# This will act as our "Multiple Layers" feature
overlay_layer = np.zeros((height, width, 3), dtype=np.uint8)

# Create an overlay pattern
for x in range(width):
    for y in range(height):
        overlay_layer[y, x] = [(255-x) // 2, (255-x) // 4, (255-x) // 4]  # Applying a different pattern

# Combine the layers
# Note: Since PNG does not natively support multiple image layers like PSD files,
# we simulate this by blending the layers together.
# For real multi-layer support, consider saving each layer as a separate file or using a format that supports layers.
combined_image_data = np.clip(base_layer + overlay_layer, 0, 255).astype(np.uint8)

# Save the combined image
img = Image.fromarray(combined_image_data, 'RGB')
img.save(f'./tmp/gradient_with_overlay.png', format='PNG', compress_level=9)

print("Image with 'Multiple Layers' saved as 'gradient_with_overlay.png'.")