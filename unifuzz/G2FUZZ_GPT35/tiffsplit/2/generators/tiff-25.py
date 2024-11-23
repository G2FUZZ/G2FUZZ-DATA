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

# Save image as TIFF file with Image Orientation and Text Annotations features
with TiffWriter("./tmp/transparent_image_with_orientation_and_annotations.tiff") as tiff:
    tiff.save(image, software="MyImageProcessingTool", description="Image with additional orientation feature and text annotations: 7. Text Annotations: TIFF files can support text annotations or comments within the image file.")