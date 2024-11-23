import numpy as np
import tifffile as tiff

# Create sample data for multiple channels
channel1_data = np.random.randint(0, 255, size=(1024, 1024), dtype=np.uint8)
channel2_data = np.random.randint(0, 255, size=(1024, 1024), dtype=np.uint8)

# Concatenate the channel data arrays
multi_channel_data = np.stack([channel1_data, channel2_data], axis=-1)

# Create metadata for the tiff file
metadata = {
    'Author': 'Jane Smith',
    'Date': '2023-01-15',
    'Description': 'Multi-channel image with tile structure'
}

# Save the multiple channel data and metadata as a TIFF file with tile structure
tiff.imsave('./tmp/multi_channel_image_with_tile_structure.tiff', multi_channel_data, metadata=metadata, tile=(256, 256))