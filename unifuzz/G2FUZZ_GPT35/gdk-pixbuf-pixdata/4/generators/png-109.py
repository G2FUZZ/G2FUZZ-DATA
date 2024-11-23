import numpy as np
from PIL import Image

# Create a sample image
image_data = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Add multiple embedded ICC profiles to the image
icc_profile_1 = b'Example ICC Profile Data 1'
icc_profile_2 = b'Example ICC Profile Data 2'
image.info['icc_profile'] = icc_profile_1
image.info['icc_profile_2'] = icc_profile_2

# Add custom metadata to the image
image.info['Author'] = 'John Doe'
image.info['Description'] = 'Sample image with multiple ICC profiles'

# Save the image with embedded ICC profiles and custom metadata
image.save('./tmp/sample_image_with_multiple_icc_profiles.png')