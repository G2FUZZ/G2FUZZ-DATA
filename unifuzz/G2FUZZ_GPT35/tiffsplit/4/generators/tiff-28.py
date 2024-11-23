from PIL import Image

# Create a new image with RGB mode
image = Image.new('RGB', (100, 100))

# Save the image with Progressive Loading
image.save('./tmp/compressed_image_progressive.tiff', compression='tiff_adobe_deflate', save_all=True, progressive=True)

print("TIFF file with Progressive Loading feature has been saved in ./tmp/")