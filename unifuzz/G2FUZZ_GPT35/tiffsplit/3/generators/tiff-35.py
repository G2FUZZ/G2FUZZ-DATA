from PIL import Image

# Create a new RGB image
base_image = Image.new('RGB', (200, 200), (0, 255, 0))

# Create a new RGBA image with transparency
transparent_image = Image.new('RGBA', (200, 200), (255, 0, 0, 128))

# Create a new CMYK image
cmyk_image = Image.new('CMYK', (200, 200), (0, 0, 0, 0))

# Create a new multilayer TIFF file with compression
with Image.new('RGB', (200, 200)) as multi_layer_image:
    multi_layer_image.save('./tmp/multi_layer_image.tiff', compression='tiff_adobe_deflate', save_all=True, append_images=[base_image, transparent_image, cmyk_image])