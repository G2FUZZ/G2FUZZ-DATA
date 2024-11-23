import os
import numpy as np
import rasterio
from rasterio.transform import from_origin

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp', exist_ok=True)

# Define the data and geospatial parameters
width = 300  # Width of the raster
height = 300  # Height of the raster

# Generate random pixel values for three bands (Red, Green, Blue)
data_red = np.random.randint(0, 255, (height, width)).astype(np.uint8)
data_green = np.random.randint(0, 255, (height, width)).astype(np.uint8)
data_blue = np.random.randint(0, 255, (height, width)).astype(np.uint8)

transform = from_origin(145.0, -37.0, 0.01, 0.01)  # Define the geotransform

# Define the CRS (Coordinate Reference System) as WGS84
crs = 'EPSG:4326'

# Create the GeoTIFF with three bands
with rasterio.open('./tmp/complex_geospatial_data.tif', 'w', driver='GTiff',
                   width=width, height=height,
                   count=3,  # Number of bands
                   dtype=str(data_red.dtype),
                   crs=crs,
                   transform=transform,
                   compress='lzw') as dst:  # Use LZW compression
    dst.write(data_red, 1)  # Write the red band data
    dst.write(data_green, 2)  # Write the green band data
    dst.write(data_blue, 3)  # Write the blue band data

print("Complex GeoTIFF file created successfully at './tmp/complex_geospatial_data.tif'")