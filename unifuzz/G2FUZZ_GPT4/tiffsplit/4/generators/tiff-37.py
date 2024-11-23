from PIL import Image, ImageDraw, PngImagePlugin
import numpy as np
import os
import rasterio
from rasterio.transform import from_origin

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to generate an image with specified mode, color, and optional text
def generate_image(mode, color, width=256, height=256, text=''):
    image = Image.new(mode, (width, height), color)
    draw = ImageDraw.Draw(image)
    if text:
        text_position = (width // 2 - 100, height // 2)
        draw.text(text_position, text, fill='black')
    return image

# Function to add custom metadata to an image
def add_metadata(image, metadata):
    info = PngImagePlugin.PngInfo()
    for key, value in metadata.items():
        info.add_text(key, value)
    return info

# Generate an image with an alpha channel and a gradient effect
rgba_image = generate_image("RGBA", "green")

# Define custom metadata (Note: metadata is shown as an example for formats like PNG)
metadata = {
    "Author": "John Doe",
    "Description": "Image with geospatial metadata and custom PNG metadata"
}

# Define geospatial metadata
transform = from_origin(-180, 90, 1.0, 1.0)  # Example transform (longitude, latitude, pixel size x, pixel size y)
crs = {'init': 'epsg:4326'}  # Example CRS (Coordinate Reference System)

# Since rasterio works with bands rather than color channels, convert image to numpy array and rearrange for rasterio
rgba_array = np.asarray(rgba_image)
data_for_rasterio = np.rollaxis(rgba_array, 2, 0)

output_path = os.path.join(output_dir, 'complex_image_with_geo_metadata.tif')

# Save the image with geospatial metadata using rasterio
with rasterio.open(
    output_path, 'w', driver='GTiff',
    height=256, width=256,
    count=4, dtype=str(rgba_array.dtype),
    crs=crs, transform=transform
) as dst:
    dst.write(data_for_rasterio)

print(f"Image with geospatial metadata and custom metadata saved to {output_path}")