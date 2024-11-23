import numpy as np
import cv2

# Create a 3-channel image with random pixel values
image = np.random.randint(0, 255, (500, 500, 3), dtype=np.uint8)

# Save the image as a TIFF file with layers
cv2.imwrite('./tmp/multi_layer_image.tiff', image)