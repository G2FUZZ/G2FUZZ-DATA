import numpy as np
from PIL import Image, ImageFilter

# Create a numpy array with the text content
text = "Advanced features: Embedding multiple images with different transparency levels in layers, applying filters, and using custom metadata for enhanced visualization and analysis."
text_array = np.array([ord(char) for char in text], dtype=np.uint8)

# Reshape the array to a 2D shape
height, width = 12, len(text) // 12 + 1
text_array = np.resize(text_array, (height, width))

# Create an initial image from the numpy array
image = Image.fromarray(text_array)

# Create a new image with transparency
transparent_image = Image.new('RGBA', image.size, (255, 255, 255, 0))
transparent_image.paste(image, (0, 0))

# Add metadata to the image
metadata = {
    "Author": "Jane Smith",
    "Date": "2023-05-20",
    "Description": "Advanced TIFF file with multiple layers, transparency, and custom metadata"
}
image.info["metadata"] = metadata

# Apply filters to the image (e.g., blur effect)
filtered_image = image.filter(ImageFilter.BLUR)

# Create multiple layers with different transparency levels
layer1 = Image.new('RGBA', image.size, (255, 0, 0, 100))  # Red layer with 50% transparency
layer2 = Image.new('RGBA', image.size, (0, 255, 0, 150))  # Green layer with 75% transparency

# Composite the layers on top of the image
composite_image = Image.alpha_composite(image.convert('RGBA'), layer1)
composite_image = Image.alpha_composite(composite_image, layer2)

# Save the composite image with filters and metadata as a compressed TIFF file
composite_image.save("./tmp/advanced_features.tiff", format='TIFF', compression='tiff_lzw', resolution=300.0)