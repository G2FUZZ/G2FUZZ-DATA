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

print("JPEG file with DCT compression generated and saved successfully.")