from PIL import Image
import numpy as np
import os
import rasterio
from rasterio.transform import from_origin

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate an image with an indexed color (using a color map) and an additional layer for floating point data
width, height = 256, 256

# Create an array of bytes representing the image indices for the indexed color layer
data = np.zeros((height, width), dtype=np.uint8)
for y in range(height):
    data[y, :] = np.linspace(0, 255, width, endpoint=True, dtype=np.uint8)

# Create a floating point data layer
# For demonstration, let's create a gradient with floating point numbers
float_data = np.linspace(0.0, 1.0, width * height, endpoint=True, dtype=np.float32).reshape((height, width))

# Create a color map (palette) for the indexed color layer
color_map = [(i, i, i) for i in range(256)]
rasterio_color_map = {i: color_map[i] for i in range(256)}

# Define geospatial metadata
transform = from_origin(-180, 90, 1.0, 1.0)  # Longitude, latitude, pixel size x, pixel size y
crs = {'init': 'epsg:4326'}  # Coordinate Reference System

output_path = os.path.join(output_dir, 'image_with_geo_color_maps_and_float.tif')

# Convert the data to float32 to match the dtype of float_data
data = data.astype(np.float32)

# Save the image with geospatial metadata, color map, and floating point data using rasterio
with rasterio.open(
    output_path, 'w', driver='GTiff',
    height=height, width=width,
    count=2, dtype='float32',  # Use a single dtype for both bands
    crs=crs, transform=transform
) as dst:
    dst.write(data, 1)  # Write the indexed data to the first band
    dst.write_colormap(1, rasterio_color_map)  # Apply the color map to the first band
    dst.write(float_data, 2)  # Write the floating point data to the second band

print(f"Image with geospatial metadata, color maps, and floating point data saved to {output_path}")