import numpy as np
from PIL import Image

# Create a list of images to be saved in the multipage TIFF file
images = []
for i in range(5):
    # Generate a random image (100x100 pixels) with random pixel values
    random_image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    images.append(Image.fromarray(random_image))

# Set additional file features
resolution = (300, 300)  # Set resolution to 300 dpi
metadata = {'author': 'John Doe', 'description': 'Random images for testing'}  # Add metadata information
compression_quality = 95  # Set compression quality to 95 for JPEG compression

# Save the images as a multipage TIFF file with additional file features
multipage_tiff_path_complex = './tmp/multipage_images_complex.tiff'
images[0].save(multipage_tiff_path_complex, save_all=True, append_images=images[1:], resolution=resolution, dpi=resolution,
                 compression='jpeg', quality=compression_quality, metadata=metadata)