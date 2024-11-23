import numpy as np
import tifffile as tf

# Create metadata
metadata = {
    'Author': 'John Doe',
    'Copyright': '2023',
    'CreationDate': '2023-09-20',
    'CustomTags': {
        'Tag1': 'Value1',
        'Tag2': 'Value2'
    }
}

# Create a dummy image data
image_data = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)

# Save image with metadata
tf.imwrite('./tmp/metadata_example_with_custom_tags.tiff', image_data, metadata=metadata)