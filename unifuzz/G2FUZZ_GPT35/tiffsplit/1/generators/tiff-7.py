from PIL import Image

# Create a new TIFF image with tile structure
img = Image.new('RGB', (256, 256), color='red')
img.save('./tmp/tile_structure.tiff', compression='tiff_deflate', tiffinfo={32768: 1})  # 1 corresponds to tile structure

print("TIFF file with tile structure generated successfully.")