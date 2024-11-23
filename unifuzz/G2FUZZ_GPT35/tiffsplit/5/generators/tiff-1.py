from PIL import Image

# Create a new image with some data
data = [(x, x, x) for x in range(256)] * 256
image = Image.new('RGB', (256, 256))
image.putdata(data)

# Save the image with different compression modes
compression_modes = ['raw', 'tiff_lzw', 'tiff_deflate', 'jpeg']
for mode in compression_modes:
    if mode == 'raw':
        image.save(f'./tmp/image_{mode}.tiff')
    else:
        image.save(f'./tmp/image_{mode}.tiff', compression=mode)

print("TIFF files with different compression modes have been saved in the './tmp/' directory.")