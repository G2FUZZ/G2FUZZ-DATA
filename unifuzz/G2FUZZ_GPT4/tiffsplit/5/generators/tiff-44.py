import numpy as np
from PIL import Image
import tifffile

def generate_halftone_pattern(width, height, pattern_density):
    """Generates a simple halftone pattern for demonstration."""
    image = np.zeros((height, width), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            intensity = (x + y) % width
            if intensity < width // 3:
                if (x % (3 + pattern_density) == 0 and y % (3 + pattern_density) == 0):
                    image[y, x] = 0
                else:
                    image[y, x] = 255
            elif intensity < 2 * (width // 3):
                if (x % (4 + pattern_density) == 0 and y % (4 + pattern_density) == 0) or (x % (4 + pattern_density) == 2 and y % (4 + pattern_density) == 2):
                    image[y, x] = 0
                else:
                    image[y, x] = 255
            else:
                if (x % (5 + pattern_density) == 0 and y % (5 + pattern_density) == 0):
                    image[y, x] = 0
                else:
                    image[y, x] = 255
    return image

def generate_thumbnail(image, thumbnail_size=(50, 50)):
    """Generates a thumbnail of the given image."""
    image_pil = Image.fromarray(image)
    image_pil.thumbnail(thumbnail_size)
    return np.array(image_pil)

def save_with_subifds(images, file_path):
    """Saves a list of numpy arrays as a multi-page TIFF file with subdirectories for thumbnails."""
    with tifffile.TiffWriter(file_path, bigtiff=True) as tiff:
        for img in images:
            thumbnail = generate_thumbnail(img)
            subifds = [{'shape': thumbnail.shape, 'dtype': thumbnail.dtype}]
            tiff.write(img, compression='jpeg2000', subifds=subifds, metadata={'description': 'Halftone pattern'})
            tiff.write(thumbnail, subfiletype=1, compression='jpeg')

# Parameters for each image
width, height = 300, 300
pattern_densities = [0, 1, 2]  # Different densities for different halftone patterns

# Generate multiple halftone patterns
halftone_images = [generate_halftone_pattern(width, height, pd) for pd in pattern_densities]

# Save the images with thumbnails as subIFDs
save_with_subifds(halftone_images, './tmp/multipage_halftone_example_with_thumbnails.tiff')

print("Multi-page TIFF file with JPEG 2000 compression and thumbnails in subIFDs has been saved.")