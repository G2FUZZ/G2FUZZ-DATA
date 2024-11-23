import numpy as np
from PIL import Image

# Create a list of images to be saved in the multipage TIFF file
images = []
for i in range(5):
    # Generate a random image (100x100 pixels) with random pixel values
    random_image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    images.append(Image.fromarray(random_image))

# Save the images as a multipage TIFF file with custom metadata and compression quality
multipage_tiff_path_custom = './tmp/multipage_images_custom.tiff'
metadata = {'author': 'John Doe', 'description': 'Multipage TIFF Example'}
save_kwargs = {'save_all': True, 'append_images': images[1:], 'compression': 'tiff_jpeg', 'dpi': (300, 300), 'quality': 95, 'resolution_unit': 2, 'extra': metadata}
images[0].save(multipage_tiff_path_custom, **save_kwargs)