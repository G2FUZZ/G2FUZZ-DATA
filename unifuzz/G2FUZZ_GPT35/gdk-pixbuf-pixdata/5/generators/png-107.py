from PIL import Image

# Create an RGBA image with transparency
image_rgba = Image.new('RGBA', (200, 200), color=(0, 128, 128, 128))
image_rgba.putpixel((100, 100), (255, 0, 0, 200))  # Set a semi-transparent red pixel
image_rgba.save('./tmp/rgba_image.png')

# Create an image with multiple layers
image_layers = Image.new('RGBA', (200, 200), color=(255, 255, 255, 255))
layer1 = Image.new('RGBA', (200, 200), color=(255, 0, 0, 128))
layer2 = Image.new('RGBA', (200, 200), color=(0, 255, 0, 128))
image_layers = Image.alpha_composite(image_layers, layer1)
image_layers = Image.alpha_composite(image_layers, layer2)
image_layers.save('./tmp/multi_layer_image.png')