import numpy as np
from PIL import Image
import scipy.fftpack as fft

# Create a random image
image_data = np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Apply DCT compression
image_data_dct = fft.dct(fft.dct(image_data.T, norm='ortho').T, norm='ortho')

# Save the DCT compressed image with JPEG format
image_dct = Image.fromarray(image_data_dct.astype(np.uint8))
image_dct.save('./tmp/compressed_image_dct.jpg', quality=90, optimize=True, progressive=True)

# Add JFXX extension to the image
jfxx_extension_data = b'JFXX Extension Data'  # Example additional data
with open('./tmp/compressed_image_dct.jpg', 'ab') as f:
    f.write(jfxx_extension_data)

print("JPEG file with DCT compression and JFXX extension generated and saved successfully.")