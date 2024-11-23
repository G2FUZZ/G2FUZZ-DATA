import numpy as np
from PIL import Image

# Create a sample image
image_data = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Add an embedded ICC profile to the image
icc_profile = b'Example ICC Profile Data'
image.info['icc_profile'] = icc_profile

# Save the image with embedded ICC profile
image.save('./tmp/sample_image_with_icc_profile.png')