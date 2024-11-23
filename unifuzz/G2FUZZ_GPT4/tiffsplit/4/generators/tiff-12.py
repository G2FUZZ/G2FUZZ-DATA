from PIL import Image
import numpy as np
import os
import rasterio
from rasterio.transform import from_origin

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate an image with an alpha channel
# Create a 256x256 image with 4 channels (RGBA)
width, height = 256, 256
channels = 4  # Red, Green, Blue, Alpha

# Create an array of bytes representing the image
# For the alpha channel, create a gradient effect from fully opaque to fully transparent
data = np.zeros((height, width, channels), dtype=np.uint8)

# Fill the R, G, B channels with a solid color, e.g., semi-bright green
data[..., :3] = [0, 128, 0]  # RGB

# Create a gradient for the alpha channel
for y in range(height):
    alpha_value = int((y / height) * 255)
    data[y, :, 3] = alpha_value

# Create a temporary PIL image
pil_image = Image.fromarray(data, 'RGBA')

# Convert the PIL image back to a NumPy array
data_with_icc = np.array(pil_image)

# Define geospatial metadata
transform = from_origin(-180, 90, 1.0, 1.0)  # Example transform (longitude, latitude, pixel size x, pixel size y)
crs = {'init': 'epsg:4326'}  # Example CRS (Coordinate Reference System)

# Prepare data for saving with rasterio
# Since rasterio works with bands rather than color channels, and expects data in the shape
# (bands, height, width), we need to rearrange our data.
data_for_rasterio = np.rollaxis(data_with_icc, 2, 0)

output_path = os.path.join(output_dir, 'image_with_geo_metadata.tif')

# Save the image with geospatial metadata using rasterio
with rasterio.open(
    output_path, 'w', driver='GTiff',
    height=height, width=width,
    count=channels, dtype=str(data_with_icc.dtype),
    crs=crs, transform=transform
) as dst:
    dst.write(data_for_rasterio)

print(f"Image with geospatial metadata saved to {output_path}")