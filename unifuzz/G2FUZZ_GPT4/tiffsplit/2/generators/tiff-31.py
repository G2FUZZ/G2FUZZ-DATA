import numpy as np
from PIL import Image, ImagePalette
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an example indexed image with a color map using numpy
# For simplicity, we're creating an image with values from 0 to 255, which will directly map to colors in the palette.
# In practice, your palette and image data might be more complex and not directly correlate.
image_data_indexed = np.random.randint(0, 256, (100, 100), dtype=np.uint8)

# Generate a color palette
# Here, we're creating a simple grayscale palette, but you could define any RGB colors in your palette.
palette = []
for i in range(256):
    palette.extend([i, i, i])  # Grayscale color, R=G=B=i

# Create an indexed image
image_indexed = Image.fromarray(image_data_indexed, mode='P')  # Create an image in "P" mode (palettized)

# Assign the color palette to the image
image_indexed.putpalette(palette)

# Save the indexed image with a color map in TIFF format
image_indexed.save('./tmp/example_indexed_color_map.tiff')

# Optionally, you can still save the image with various compression methods
# Saving with LZW compression
image_indexed.save('./tmp/example_indexed_color_map_lzw.tiff', compression='tiff_lzw')

# Saving with ZIP (Deflate) compression
image_indexed.save('./tmp/example_indexed_color_map_zip.tiff', compression='tiff_deflate')

# Saving with PackBits compression
image_indexed.save('./tmp/example_indexed_color_map_packbits.tiff', compression='tiff_packbits')