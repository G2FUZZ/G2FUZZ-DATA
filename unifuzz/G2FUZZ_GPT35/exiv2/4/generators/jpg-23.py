import numpy as np
from PIL import Image

# Create a sample image
data = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)
image = Image.fromarray(data)

# Configure the save options to enable Progressive refinement and set Subsampling ratio to 4:2:0
image.save('./tmp/sample_subsampling.jpg', format='JPEG', quality=95, progressive=True, subsampling='4:2:0')