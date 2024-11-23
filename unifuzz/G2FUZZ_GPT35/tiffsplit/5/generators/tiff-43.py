import numpy as np
from PIL import Image

# Create a numpy array with the text content
text = "Complex features: Adding multiple layers with transparency and metadata to a TIFF file enhances its editing capabilities and information richness."
text_array = np.array([ord(char) for char in text], dtype=np.uint8)

# Reshape the array to a 2D shape
height, width = 10, len(text) // 10 + 1
text_array = np.resize(text_array, (height, width))

# Create an initial image from the numpy array
image = Image.fromarray(text_array)

# Create a new image with transparency
transparent_image = Image.new('RGBA', image.size, (255, 255, 255, 0))
transparent_image.paste(image, (0, 0))

# Add metadata to the image
metadata = {
    "Author": "John Doe",
    "Date": "2022-09-15",
    "Description": "Example of a TIFF file with multiple layers and metadata"
}
image.info["metadata"] = metadata

# Create a thumbnail image
thumbnail_size = (100, 100)
thumbnail = image.copy()
thumbnail.thumbnail(thumbnail_size)

# Save the image with thumbnail as a TIFF file
image.save("./tmp/complex_features.tiff", resolution=300.0, thumbnail=thumbnail)