import numpy as np
from PIL import Image

# Create a simple black and white image
data = np.zeros((100, 100), dtype=np.uint8)
data[25:75, 25:75] = 255  # Add a white square in the middle

# Set some example tags for the first image
tags_page1 = {
    256: 100,  # Image width
    257: 100,  # Image height
    258: 8,    # Bits per sample
    259: 1,    # Compression (1 = no compression)
    262: 0,    # Photometric interpretation (0 = white is zero)
    274: 1,    # Orientation
    277: 1,    # Samples per pixel
    282: (72, 1),  # X resolution
    283: (72, 1),  # Y resolution
}

# Create a new image with the specified tags for the first image
img_page1 = Image.fromarray(data)

# Create a new image with the specified tags for the second image
img_page2 = Image.fromarray(np.flipud(data))  # Flip the image for demonstration

# Save both images as a multipage TIFF file
img_page1.save("./tmp/example_multipage.tiff", tiffinfo=tags_page1, append_images=[img_page2], save_all=True)