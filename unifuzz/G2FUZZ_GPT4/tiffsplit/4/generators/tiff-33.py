from PIL import Image
import numpy as np
import os
import rasterio
from rasterio.transform import from_origin

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

def add_custom_tags(custom_tags):
    # Placeholder function for demonstration
    return custom_tags

# Global custom tags for all metadata
global_custom_tags = {
    'GLOBAL_TAG': 'Example of a global tag value',
}

# Generate multiple images with different properties (color maps)
images_data = []
color_maps = []

for i in range(3):
    width, height = 256, 256
    data = np.zeros((height, width), dtype=np.uint8)
    for y in range(height):
        data[y, :] = np.linspace(i * 85, 255 - (i * 85), width, endpoint=True, dtype=np.uint8)
    images_data.append(data)
    
    color_map = [(i, (i + 85) % 256, (255 - i)) for i in range(256)]
    color_maps.append(color_map)

page_custom_tags = [
    {'PAGE_TAG_1': 'First page specific tag'},
    {'PAGE_TAG_2': 'Second page specific tag'},
    {'PAGE_TAG_3': 'Third page specific tag'},
]

output_path = os.path.join(output_dir, 'images_with_geo_and_color_maps.tif')

transform = from_origin(-180, 90, 1.0, 1.0)
crs = {'init': 'epsg:4326'}

with rasterio.open(
    output_path, 'w', driver='GTiff',
    height=height, width=width,
    count=len(images_data), dtype=str(images_data[0].dtype),
    crs=crs, transform=transform
) as dst:
    for i, data in enumerate(images_data):
        rasterio_color_map = {j: color_maps[i][j] for j in range(256)}
        
        meta = dst.meta
        meta.update(add_custom_tags(global_custom_tags))
        meta.update(add_custom_tags(page_custom_tags[i]))
        
        dst.write(data, i+1)
        dst.write_colormap(i+1, rasterio_color_map)
        dst.update_tags(**meta)

print(f"Multipage TIFF with geospatial metadata and color maps saved to {output_path}")