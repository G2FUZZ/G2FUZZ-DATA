import numpy as np
from PIL import Image

# Create different images with varied resolutions and color modes
data1 = np.random.randint(0, 255, (200, 200), dtype=np.uint8)  # Random image data for page 1
data2 = np.random.randint(0, 255, (150, 150, 3), dtype=np.uint8)  # Random color image data for page 2
data3 = np.random.randint(0, 255, (300, 300), dtype=np.uint8)  # Random image data for page 3

# Create images from the data arrays
img_page1 = Image.fromarray(data1)
img_page2 = Image.fromarray(data2)
img_page3 = Image.fromarray(data3)

# Save multiple images as a multipage TIFF file
img_page1.save("./tmp/complex_multipage_with_text_annotations.tiff", save_all=True, append_images=[img_page2, img_page3])