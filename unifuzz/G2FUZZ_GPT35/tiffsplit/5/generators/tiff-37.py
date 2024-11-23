import numpy as np
from PIL import Image

# Create a numpy array with the text content for the first layer
text_layer1 = "Layer 1: This is the first layer with some text content."
text_array_layer1 = np.array([ord(char) for char in text_layer1], dtype=np.uint8)
height, width = 10, len(text_layer1) // 10 + 1
text_array_layer1 = np.resize(text_array_layer1, (height, width))

# Create a numpy array with the text content for the second layer
text_layer2 = "Layer 2: This is the second layer with different text content."
text_array_layer2 = np.array([ord(char) for char in text_layer2], dtype=np.uint8)
height, width = 10, len(text_layer2) // 10 + 1
text_array_layer2 = np.resize(text_array_layer2, (height, width))

# Create an image from the numpy arrays representing the layers
image = Image.new('RGB', (width, height*2))
image.paste(Image.fromarray(text_array_layer1), (0, 0))
image.paste(Image.fromarray(text_array_layer2), (0, height))

# Add metadata to the image
metadata = {
    "Author": "John Doe",
    "Date": "2022-01-01",
    "Description": "Example TIFF file with multiple layers and metadata"
}
image.info["metadata"] = metadata

# Save the image with multiple layers and metadata as a TIFF file
image.save("./tmp/multi_layer_with_metadata.tiff", resolution=300.0)