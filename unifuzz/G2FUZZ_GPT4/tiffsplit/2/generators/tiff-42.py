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
    },
    # Adding the DNG Compatibility metadata
    "DNG Compatibility": "13. DNG Compatibility: Some TIFF files are compatible with the Digital Negative (DNG) specification, a raw image format developed by Adobe, indicating that TIFF can serve as a container for raw image data from digital cameras."
}

# Convert the metadata dictionary to a JSON string
metadata_json = json.dumps(metadata)

# Save a new TIFF with the original image data and additional non-image data stored as metadata
# The metadata is stored in the ImageDescription tag, which is a standard TIFF tag for storing arbitrary text
# Adding the DNG Compatibility information in the metadata
tifffile.imwrite('./tmp/tiled_image_with_metadata_and_DNG.tiff', data, tile=(tile_width, tile_height),
                 metadata={'ImageDescription': metadata_json})