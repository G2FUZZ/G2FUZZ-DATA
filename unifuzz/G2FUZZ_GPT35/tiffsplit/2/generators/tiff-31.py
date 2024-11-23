import numpy as np
import tifffile as tf

# Create numpy arrays for multiple channels of image data
channel1_data = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)
channel2_data = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)

# Concatenate the channel data arrays
multi_channel_data = np.stack([channel1_data, channel2_data], axis=-1)

# Create metadata for the tiff file
metadata = {
    'Author': 'John Doe',
    'Date': '2022-12-31',
    'Description': 'Multi-channel image with additional metadata'
}

# Save the multiple channel data and metadata as a TIFF file
filename = './tmp/multi_channel_image_with_metadata.tiff'
tf.imwrite(filename, multi_channel_data, metadata=metadata)