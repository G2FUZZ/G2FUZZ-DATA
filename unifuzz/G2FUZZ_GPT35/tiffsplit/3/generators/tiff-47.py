import numpy as np
from PIL import Image

# Create a list to store multiple image data with annotations
images_with_annotations = []

# Generate multiple image data and annotations
for i in range(5):
    image_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)
    annotation = f"Annotation for image {i+1}"
    images_with_annotations.append((Image.fromarray(image_data), annotation))

# Create a new image with layers and annotations
layered_image = Image.new('RGBA', (256, 256), (0, 0, 0, 0))
for image, annotation in images_with_annotations:
    layered_image.paste(image, (0, 0), image)
    layered_image.info['annotations'] = layered_image.info.get('annotations', '') + f"{annotation}\n"

# Save the layered image as a tiff file with annotations
layered_image.save('./tmp/layered_image_with_annotations.tiff', save_all=True, append_images=[], compression='tiff_lzw')