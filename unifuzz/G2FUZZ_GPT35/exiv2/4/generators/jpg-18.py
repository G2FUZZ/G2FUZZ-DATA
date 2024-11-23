import numpy as np
from PIL import Image

# Create a sample image
data = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)
image = Image.fromarray(data)

# Configure the save options to enable Progressive refinement
image.save('./tmp/sample_progressive.jpg', format='JPEG', quality=95, progressive=True)