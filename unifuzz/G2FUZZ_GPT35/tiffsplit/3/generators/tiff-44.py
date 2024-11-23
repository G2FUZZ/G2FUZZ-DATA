import numpy as np
from PIL import Image

# Create a list to store multiple image data
images = []

# Generate multiple image data and alpha channel data
for _ in range(5):
    image_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)
    alpha_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)
    images.append(Image.fromarray(np.dstack((image_data, alpha_data))))

# Create additional image layers with different content
layer1 = Image.new('RGBA', (256, 256), (255, 0, 0, 128))
layer2 = Image.new('RGBA', (256, 256), (0, 255, 0, 128))
layer3 = Image.new('RGBA', (256, 256), (0, 0, 255, 128))

# Create a multipage TIFF file with multiple layers and different compression methods
multipage_image = Image.new('RGBA', (256, 256))
multipage_image.paste(images[0], (0, 0))
multipage_image.paste(layer1, (0, 0))
multipage_image.paste(layer2, (0, 0))
multipage_image.paste(layer3, (0, 0))

multipage_image.save('./tmp/multipage_images.tiff', save_all=True, append_images=[images[0], layer1, layer2, layer3], compression='tiff_deflate', tile=(128, 128))