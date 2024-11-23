from PIL import Image

# Create a new image with some data
data = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
img = Image.new('RGB', (2, 2))
img.putdata(data)

# Save the image with TIFF format and compression
img.save('./tmp/multi_resolution_image.tiff', compression='tiff_lzw', dpi=(300, 300), save_all=True)