import numpy as np
from PIL import Image

# Create a list of images to be saved in the multipage TIFF file
images = []
for i in range(5):
    # Generate a random image (100x100 pixels) with random pixel values
    random_image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    images.append(Image.fromarray(random_image))

# Save the images as a multipage TIFF file
multipage_tiff_path = './tmp/multipage_images.tiff'
images[0].save(multipage_tiff_path, save_all=True, append_images=images[1:])