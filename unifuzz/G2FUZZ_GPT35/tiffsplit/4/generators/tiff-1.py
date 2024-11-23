from PIL import Image

# Create a new image with RGB mode
image = Image.new('RGB', (100, 100))

# Save the image with LZW compression
image.save('./tmp/compressed_image_lzw.tiff', compression='tiff_lzw')

# Save the image with ZIP compression
image.save('./tmp/compressed_image_zip.tiff', compression='tiff_deflate')

# Save the image with JPEG compression
image.save('./tmp/compressed_image_jpeg.tiff', compression='tiff_jpeg')

print("TIFF files with different compression methods have been saved in ./tmp/")