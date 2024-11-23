from PIL import Image

# Create a multipage tiff file with metadata
with Image.new('RGB', (100, 100), color='blue') as img:
    img.save('./tmp/multipage_image.tif', save_all=True, append_images=[img, img], format='TIFF', dpi=(300.0, 300.0), compression='tiff_lzw')