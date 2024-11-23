import numpy as np
import cv2

# Create a 3-channel image with random pixel values
image = np.random.randint(0, 255, (500, 500, 3), dtype=np.uint8)

# Generate the thumbnail image
thumbnail = cv2.resize(image, (100, 100))

# Define the TIFF parameters
tiff_params = [cv2.IMWRITE_TIFF_RESUNIT, 2, cv2.IMWRITE_TIFF_XDPI, 72, cv2.IMWRITE_TIFF_YDPI, 72, cv2.IMWRITE_TIFF_COMPRESSION, 0]

# Save the image as a TIFF file with layers and thumbnail
cv2.imwrite('./tmp/multi_layer_image_with_thumbnail.tiff', image, tiff_params)