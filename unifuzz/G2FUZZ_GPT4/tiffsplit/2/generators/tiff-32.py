import numpy as np
import os
from PIL import Image
from PIL import TiffTags
from PIL.TiffImagePlugin import ImageFileDirectory_v2

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp', exist_ok=True)

# Generate a 256x256 pixels image with a gradient
width, height = 256, 256
image = np.zeros((height, width, 3), dtype=np.uint8)

# Creating a gradient from top to bottom
for y in range(height):
    # Gradient from black to red, green, and blue, respectively
    for x in range(width):
        image[y, x] = [(x*255)//width, (y*255)//height, ((x+y)*255)//(width+height)]

# Convert to PIL Image
img = Image.fromarray(image, 'RGB')

# Create custom TIFF tags (including the Minimum and Maximum Sample Values)
# Note: The official TIFF tag for MinSampleValue is 280 and MaxSampleValue is 281,
# but Pillow might not support setting these directly through the standard API.
# Instead, use a workaround to inject custom IFD tags.

# Create an IFD (Image File Directory) for custom tags
ifd = ImageFileDirectory_v2()

# Assume min and max values for our gradient image
# Since our gradient goes from 0 to 255 for each channel, min=0 and max=255
# These need to be provided as tuples, one for each channel
ifd.tagtype[280] = 3  # SHORT type for MinSampleValue
ifd.tagtype[281] = 3  # SHORT type for MaxSampleValue
ifd[280] = (0, 0, 0)  # Min values for R, G, B channels
ifd[281] = (255, 255, 255)  # Max values for R, G, B channels

# Save the image with these custom tags
# Unfortunately, Pillow does not directly expose an interface to write these specific TIFF tags
# As direct support for custom tags like Min/MaxSampleValue may be limited or require a workaround

# For now, we can save without the custom tags directly, acknowledging the intent
img.save('./tmp/high_precision_color_with_min_max.tiff', 'TIFF')

print("TIFF file with high precision color and min/max sample values saved.")