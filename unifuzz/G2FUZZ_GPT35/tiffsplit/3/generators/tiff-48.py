import numpy as np
from PIL import Image
from PIL.TiffTags import TAGS_V2

# Create a 2D numpy array to represent the image data
image_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)

# Create alpha channel data (transparency values)
alpha_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)

# Create additional layer data
layer_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)

# Create image metadata with custom tags
metadata = {
    270: "Example Image Description",  # Tag number for ImageDescription
    305: "Python PIL",  # Tag number for Software
    306: "2023:01:01 12:00:00",  # Tag number for DateTime
    37510: "Added brightness adjustment",  # Tag number for ImageEditingHistory
    40001: "Custom Tag 1 Value",  # Custom Tag 1
    40002: "Custom Tag 2 Value",  # Custom Tag 2
}

# Save the image data, alpha channel data, and layer data as a multi-layered TIFF file with custom tags
image_with_metadata = Image.fromarray(np.dstack((image_data, alpha_data, layer_data)))
image_with_metadata.save('./tmp/multi_layered_image_with_metadata.tiff', compression='tiff_deflate', tile=(128, 128), tiffinfo=metadata)