import numpy as np
from PIL import Image

# Create multiple images
image1 = np.zeros((100, 100, 3), dtype=np.uint8)  # Black image
image2 = np.ones((100, 100, 3), dtype=np.uint8) * 255  # White image

# Save the images as PNG files
Image.fromarray(image1).save('./tmp/image1.png')
Image.fromarray(image2).save('./tmp/image2.png')

print("PNG files containing multiple images have been saved in the './tmp/' directory.")