from PIL import Image

# Create a base image layer
base_image = Image.new('RGBA', (100, 100), (255, 0, 0, 128))

# Create additional image layers with different content
layer1 = Image.new('RGBA', (100, 100), (0, 255, 0, 128))
layer2 = Image.new('RGBA', (100, 100), (0, 0, 255, 128))

# Create a multipage TIFF file with multiple layers and different compression methods
multipage_image = Image.new('RGBA', (100, 100))
multipage_image.paste(base_image, (0, 0))
multipage_image.paste(layer1, (0, 0))
multipage_image.paste(layer2, (0, 0))

multipage_image.save('./tmp/multipage_tiff.tiff', save_all=True, append_images=[base_image, layer1, layer2], compression='tiff_jpeg')