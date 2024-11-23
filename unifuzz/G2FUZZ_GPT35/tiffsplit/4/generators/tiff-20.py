import numpy as np
from PIL import Image

# Create a list of images to be saved in the multipage TIFF file
images = []
for i in range(5):
    # Generate a random image (100x100 pixels) with random pixel values
    random_image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    images.append(Image.fromarray(random_image))

# Save the images as a multipage TIFF file with custom tags
multipage_tiff_path = './tmp/multipage_images_with_custom_tags.tiff'

# Custom Tags: Adding custom tags to the TIFF file
custom_tags = {
    700: b'Custom Tag Value 1',
    701: b'Custom Tag Value 2'
}

images[0].save(multipage_tiff_path, save_all=True, append_images=images[1:], dpi=(300.0, 300.0), tiffinfo=custom_tags)