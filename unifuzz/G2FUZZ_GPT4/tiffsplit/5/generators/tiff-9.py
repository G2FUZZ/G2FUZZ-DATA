import os
import numpy as np
import rasterio
from rasterio.transform import from_origin

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp', exist_ok=True)

# Define the data and geospatial parameters
width = 300  # Width of the raster
height = 300  # Height of the raster
data = np.random.randint(0, 255, (height, width)).astype(np.uint8)  # Generate random pixel values

transform = from_origin(145.0, -37.0, 0.01, 0.01)  # Define the geotransform (top-left x, top-left y, x pixel size, y pixel size)

# Define the CRS (Coordinate Reference System) as WGS84
crs = 'EPSG:4326'

# Create the GeoTIFF
with rasterio.open('./tmp/geospatial_data.tif', 'w', driver='GTiff',
                   width=width, height=height,
                   count=1, dtype=str(data.dtype),
                   crs=crs,
                   transform=transform) as dst:
    dst.write(data, 1)  # Write the data to the first band

print("GeoTIFF file created successfully at './tmp/geospatial_data.tif'")