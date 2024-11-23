import numpy as np
from PIL import Image

# Create a list of images to be saved in the multipage TIFF file
images = []
for i in range(5):
    # Generate a random image (100x100 pixels) with random pixel values
    random_image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    images.append(Image.fromarray(random_image))

# Add image editing history metadata
metadata = {"ImageDescription": "Image Editing History: Some TIFF files may store a record of editing operations performed on the image."}
images[0].info.update(metadata)

# Save the images as a multipage TIFF file with image editing history
multipage_tiff_path = './tmp/multipage_images_with_history.tiff'
images[0].save(multipage_tiff_path, save_all=True, append_images=images[1:])