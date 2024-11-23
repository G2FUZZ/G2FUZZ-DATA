import numpy as np
import tifffile as tiff

# Create a sample image
image = np.random.randint(0, 255, (256, 256), dtype=np.uint8)

# Save the image as a TIFF file with tile structure and annotations
annotations = {
    'Image Annotations': 'TIFF files can include annotations or comments associated with specific regions of the image.'
}

# Convert annotations dictionary to a string
annotations_str = str(annotations)

tiff.imwrite("./tmp/tile_structure_with_annotations.tif", image, tile=(64, 64), description=annotations_str)

print("TIFF file with tile structure and Image Annotations created successfully.")