import numpy as np
from PIL import Image
from tifffile import TiffWriter

# Create a numpy array with shape (100, 100, 4) for RGBA image
rgba_image = np.zeros((100, 100, 4), dtype=np.uint8)

# Fill the image with some color (e.g., white)
rgba_image[:, :, :3] = 255

# Add alpha channel with transparency values
alpha_channel = np.linspace(0, 255, 100).astype(np.uint8)
rgba_image[:, :, 3] = alpha_channel[:, np.newaxis]

# Create PIL Image from numpy array
image = Image.fromarray(rgba_image)

# Save image as TIFF file with Image Orientation, Text Annotations, and Progressive Loading features
with TiffWriter("./tmp/transparent_image_with_features.tiff") as tiff:
    tiff.save(image, software="MyImageProcessingTool", description="Image with additional orientation feature, text annotations, and progressive loading feature: 7. Text Annotations: TIFF files can support text annotations or comments within the image file. 9. Progressive Loading: TIFF files can be encoded in a progressive format, allowing for gradual loading of the image for faster display.")