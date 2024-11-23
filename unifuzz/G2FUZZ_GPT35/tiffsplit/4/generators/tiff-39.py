import numpy as np
import cv2
import tifffile

# Create a 3-channel image with random pixel values
image = np.random.randint(0, 255, (500, 500, 3), dtype=np.uint8)

# Create additional layers for the image with the same shape and data type as the main image
additional_layer1 = np.random.randint(0, 255, (500, 500, 3), dtype=np.uint8)
additional_layer2 = np.random.randint(0, 255, (500, 500, 3), dtype=np.uint8)

# Generate the thumbnail image with the same shape and data type as the main image
thumbnail = cv2.resize(image, (500, 500))  # Resize thumbnail to match the shape of other images

# Save the main image
cv2.imwrite('./tmp/image.tiff', image)

# Save additional layers
cv2.imwrite('./tmp/additional_layer1.tiff', additional_layer1)
cv2.imwrite('./tmp/additional_layer2.tiff', additional_layer2)

# Save the thumbnail image
cv2.imwrite('./tmp/thumbnail.tiff', thumbnail)

# Stack the images along a new axis to create a multi-layer image
multi_layer_image = np.stack([image, additional_layer1, additional_layer2, thumbnail])

# Save the multi-layer image as a TIFF file
tifffile.imwrite('./tmp/multi_layer_image_with_thumbnail.tiff', multi_layer_image)