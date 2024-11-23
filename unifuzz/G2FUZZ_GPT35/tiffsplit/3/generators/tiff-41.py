from PIL import Image

# Create a new RGBA image with transparency
image = Image.new('RGBA', (200, 200), (0, 255, 0, 128))

# Add metadata to the image
metadata = {
    "Author": "John Doe",
    "Description": "A beautiful green image with transparency"
}
image.info['metadata'] = metadata

# Create a new grayscale image
gray_image = Image.new('L', (200, 200))
pixels = gray_image.load()
for i in range(gray_image.size[0]):
    for j in range(gray_image.size[1]):
        pixels[i, j] = i % 256

# Save the images separately
image.save('./tmp/rgba_image.tiff')
gray_image.save('./tmp/gray_image.tiff')

# Open the images again
image = Image.open('./tmp/rgba_image.tiff')
gray_image = Image.open('./tmp/gray_image.tiff')

# Create a multi-layer tiff file
multi_layer_image = Image.new('RGB', (200, 200))
multi_layer_image.paste(image, (0, 0), image)
multi_layer_image.paste(gray_image, (0, 0), gray_image)

# Save the multi-layer image as a TIFF file
multi_layer_image.save('./tmp/multi_layer_image.tiff', save_all=True)