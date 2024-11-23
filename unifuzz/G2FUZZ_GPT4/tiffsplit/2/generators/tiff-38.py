import numpy as np
import tifffile
import os
import json

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a sample large image array (10000x10000 pixels) with random content
height, width = 10000, 10000
data = np.random.randint(0, 256, (height, width), dtype=np.uint8)

# Define tile dimensions - for example, 256x256 pixels
tile_width, tile_height = 256, 256

# Save the image as a tiled TIFF
tifffile.imwrite('./tmp/tiled_image.tiff', data, tile=(tile_width, tile_height))

# Now, let's generate and include non-image data (metadata) in the TIFF file
# For this example, we'll store some simple metadata in JSON format
metadata = {
    "Description": "This is a sample TIFF file with non-image data.",
    "Experiment": "Experiment XYZ",
    "Date": "2023-01-01",
    "Data": {
        "Temperature": 23.5,
        "Pressure": 101.3
    }
}

# Convert the metadata dictionary to a JSON string
metadata_json = json.dumps(metadata)

# Define resolution and its unit (2 = inches, 3 = centimeters)
# As an example, we'll use 300 dots per inch (DPI) for both X and Y resolution, and specify the unit as inches
resolution = (300, 300)
resolution_unit = 2  # 2 represents inches

# Save a new TIFF with the original image data, additional non-image data stored as metadata,
# and specify the X and Y resolution and the resolution unit
tifffile.imwrite('./tmp/tiled_image_with_metadata_and_resolution.tiff', data, tile=(tile_width, tile_height),
                 metadata={'ImageDescription': metadata_json},
                 resolution=resolution, 
                 extratags=[(282, 'f', 1, resolution[0], True),  # Tag 282 (XResolution)
                            (283, 'f', 1, resolution[1], True),  # Tag 283 (YResolution)
                            (296, 'H', 1, resolution_unit, False)])  # Tag 296 (ResolutionUnit)