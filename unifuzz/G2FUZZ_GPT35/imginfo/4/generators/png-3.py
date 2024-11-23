import numpy as np
import cv2

# Create a 100x100 image with 8-bit grayscale color depth
gray_image = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
cv2.imwrite('./tmp/gray_image.png', gray_image)

# Create a 100x100 image with 24-bit RGB color depth
rgb_image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
cv2.imwrite('./tmp/rgb_image.png', cv2.cvtColor(rgb_image, cv2.COLOR_BGR2RGB))

# Create a 100x100 image with 48-bit RGB with an alpha channel color depth
rgba_image = np.random.randint(0, 256, (100, 100, 4), dtype=np.uint8)
cv2.imwrite('./tmp/rgba_image.png', cv2.cvtColor(rgba_image, cv2.COLOR_BGRA2RGBA))