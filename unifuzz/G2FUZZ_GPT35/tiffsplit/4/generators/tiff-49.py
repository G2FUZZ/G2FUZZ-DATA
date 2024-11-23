import numpy as np
from PIL import Image

# Create a list of images to be saved in the multipage TIFF file with layers
images_with_layers = []
for i in range(5):
    # Generate a random image (100x100 pixels) with random pixel values
    random_image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    images_with_layers.append(Image.fromarray(random_image))

# Create another set of images for additional layers
additional_layers = []
for i in range(5):
    # Generate another random image (100x100 pixels) with random pixel values for additional layers
    random_image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    additional_layers.append(Image.fromarray(random_image))

# Save the images with layers and additional layers as a multipage TIFF file with custom tags and different compression settings
multipage_tiff_with_layers_path = './tmp/multipage_images_with_layers.tiff'

# Custom Tags: Adding custom tags to the TIFF file
custom_tags = {
    700: b'Custom Tag Value 1',
    701: b'Custom Tag Value 2'
}

# Save the images with layers and additional layers using different compression settings
images_with_layers[0].save(multipage_tiff_with_layers_path, save_all=True, append_images=images_with_layers[1:], dpi=(300.0, 300.0),
                            compression="tiff_adobe_deflate", tiffinfo=custom_tags)