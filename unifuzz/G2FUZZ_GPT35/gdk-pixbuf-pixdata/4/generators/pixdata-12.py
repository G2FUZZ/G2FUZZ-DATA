import numpy as np
import os

# Generate palette data
palette = np.random.randint(0, 256, size=(256, 3), dtype=np.uint8)

# Create directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save palette data to file
np.savetxt('./tmp/pixdata_palette.txt', palette, fmt='%d', delimiter=',', header='Palette: A color palette used to map pixel values to specific colors in indexed color images.')