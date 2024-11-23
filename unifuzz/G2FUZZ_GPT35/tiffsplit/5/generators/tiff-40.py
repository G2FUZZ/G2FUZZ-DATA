import numpy as np
import tifffile as tf

# Create metadata with additional custom tags
metadata = {
    'Author': 'Jane Smith',
    'Copyright': '2023',
    'CreationDate': '2023-09-25',
    'Description': 'Multi-channel image with custom tags',
    'CustomTag1': 'Value1',
    'CustomTag2': 'Value2'
}

# Create a multi-channel image data with higher bit depth (16-bit)
image_data = np.random.randint(0, 65535, size=(3, 100, 100), dtype=np.uint16)

# Save multi-channel image with metadata and custom tags
tf.imwrite('./tmp/multi_channel_image.tiff', image_data, metadata=metadata)