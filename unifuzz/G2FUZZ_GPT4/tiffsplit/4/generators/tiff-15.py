from PIL import Image
import numpy as np
import os
import rasterio
from rasterio.transform import from_origin

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate an image with an indexed color (using a color map)
# Create a 256x256 image with a single channel for indexed colors
width, height = 256, 256

# Create an array of bytes representing the image indices
# For simplicity, let's create a gradient effect from 0 to 255
data = np.zeros((height, width), dtype=np.uint8)
for y in range(height):
    data[y, :] = np.linspace(0, 255, width, endpoint=True, dtype=np.uint8)

# Create a color map (palette)
# Each entry in the color map is a 3-tuple representing (R, G, B).
# Here we create a simple grayscale color map where the index corresponds to the intensity.
color_map = [(i, i, i) for i in range(256)]

# Convert the color map to a format suitable for rasterio
# Rasterio expects the color map in a dictionary format where the keys are the indices
# and the values are the RGB tuples.
rasterio_color_map = {i: color_map[i] for i in range(256)}

# Define geospatial metadata
transform = from_origin(-180, 90, 1.0, 1.0)  # Example transform (longitude, latitude, pixel size x, pixel size y)
crs = {'init': 'epsg:4326'}  # Example CRS (Coordinate Reference System)

output_path = os.path.join(output_dir, 'image_with_geo_and_color_maps.tif')

# Save the indexed color image with geospatial metadata and color map using rasterio
with rasterio.open(
    output_path, 'w', driver='GTiff',
    height=height, width=width,
    count=1, dtype=str(data.dtype),
    crs=crs, transform=transform
) as dst:
    dst.write(data, 1)  # Write the indexed data
    dst.write_colormap(1, rasterio_color_map)  # Apply the color map to the first (and only) band

print(f"Image with geospatial metadata and color maps saved to {output_path}")