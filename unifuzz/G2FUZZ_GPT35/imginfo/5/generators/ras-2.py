import numpy as np
import rasterio

# Define the compression options
compression_options = {
    'COMPRESS': 'RLE',  # Use RLE compression
}

# Create sample data
data = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)

# Create a new 'ras' file with RLE compression
with rasterio.open('./tmp/compressed_ras.ras', 'w', driver='ENVI', width=100, height=100, count=1, dtype=np.uint8, **compression_options) as dst:
    dst.write(data, 1)

print("Compressed 'ras' file saved successfully.")