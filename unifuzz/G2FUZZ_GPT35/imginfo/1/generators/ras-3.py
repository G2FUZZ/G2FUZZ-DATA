import numpy as np
import rasterio
from rasterio import crs

# Create a sample raster array
data = np.random.randint(0, 255, size=(100, 100)).astype(np.uint8)

# Define metadata for the raster file
meta = {
    'count': 1,
    'crs': crs.CRS.from_epsg(4326),
    'dtype': 'uint8',
    'driver': 'GTiff',
    'height': data.shape[0],
    'width': data.shape[1],
    'transform': rasterio.transform.from_origin(0, 0, 1, 1),
    'compress': 'RLE'  # RLE compression
}

# Save the raster file as 'example_ras_rle.tif'
with rasterio.open('./tmp/example_ras_rle.tif', 'w', **meta) as dst:
    dst.write(data, 1)