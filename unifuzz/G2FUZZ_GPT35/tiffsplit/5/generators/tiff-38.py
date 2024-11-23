from PIL import Image

# Create a more complex TIFF file with multiple layers, progressive loading, custom metadata, and tiled format
complex_tiff = Image.new('RGBA', (400, 400), color='white')

# Adding multiple layers
layers = [Image.new('RGBA', (400, 400), color='red'),
          Image.new('RGBA', (400, 400), color='blue')]

for i, layer in enumerate(layers):
    complex_tiff.paste(layer, (0, 0), mask=layer)

# Adding custom metadata
metadata = {'Author': 'John Doe', 'Description': 'Complex TIFF with multiple layers'}
tiff_info = {270: 'Layered TIFF', 274: 2, 277: 4, 40000: 'Custom Metadata'}
complex_tiff.save('./tmp/complex_tiff.tif', tiffinfo=tiff_info, metadata=metadata, save_all=True)

# Using tiled format for better performance
tiled_tiff = Image.new('RGBA', (800, 800), color='yellow')
tiled_tiff.save('./tmp/tiled_tiff.tif', tiffinfo={274: 5, 277: 1}, tile=(256, 256))