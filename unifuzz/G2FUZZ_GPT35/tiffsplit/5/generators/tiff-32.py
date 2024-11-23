from PIL import Image

# Create a new image with multiple layers and metadata
data_layer1 = [(x, x, x) for x in range(256)] * 256
data_layer2 = [(x, 255-x, x) for x in range(256)] * 256

image = Image.new('RGB', (256, 256))
image.putdata(data_layer1)

# Create a new image for layer2
image_layer2 = Image.new('RGB', (256, 256))
image_layer2.putdata(data_layer2)

# Add an alpha channel to the images
image.putalpha(255)
image_layer2.putalpha(128)  # Adjust alpha value as needed

# Composite the images to create a multi-layer image
image = Image.alpha_composite(image, image_layer2)

# Add metadata to the image
metadata = {
    'Artist': 'John Doe',
    'Software': 'Python PIL',
    'DateTime': '2022-01-01 12:00:00'
}

# Save the image with metadata
image.info.update(metadata)

# Save the image with different compression modes
compression_modes = ['tiff_lzw', 'tiff_deflate', 'jpeg']
for mode in compression_modes:
    image.save(f'./tmp/image_complex_{mode}.tiff', compression=mode)

print("TIFF files with multiple layers and metadata have been saved in the './tmp/' directory.")