import numpy as np
from PIL import Image
from PIL.TiffTags import TAGS_V2

# Create a 2D numpy array to represent the image data
image_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)

# Create alpha channel data (transparency values)
alpha_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)

# Create image metadata
metadata = {
    270: "Example Image Description",  # Tag number for ImageDescription
    305: "Python PIL",  # Tag number for Software
    306: "2023:01:01 12:00:00"  # Tag number for DateTime
}

# Save the image data and alpha channel data as a TIFF file with alpha channel and metadata
image_with_metadata = Image.fromarray(np.dstack((image_data, alpha_data)))
image_with_metadata.save('./tmp/image_with_metadata.tiff', compression='tiff_deflate', tile=(128, 128), tiffinfo=metadata)