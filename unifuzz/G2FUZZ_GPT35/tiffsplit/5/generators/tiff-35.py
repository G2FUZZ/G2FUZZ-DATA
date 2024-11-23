from PIL import Image, ImageDraw, ImageFont

# Create a new image with multiple layers and metadata
data_layer1 = [(x, x, x) for x in range(256)] * 256
data_layer2 = [(x, 255-x, x) for x in range(256)] * 256

image = Image.new('RGB', (256, 256))
image.putdata(data_layer1)

# Create a new image for layer2 with different blending mode
image_layer2 = Image.new('RGB', (256, 256))
data_layer2_blend = [(255, x, 255-x) for x in range(256)] * 256
image_layer2.putdata(data_layer2_blend)

# Apply blending mode (e.g., overlay) to combine the layers
overlay_image = Image.blend(image, image_layer2, 0.5)

# Add annotations to the image
draw = ImageDraw.Draw(overlay_image)
font = ImageFont.load_default()
draw.text((10, 10), "Complex TIFF Image", fill=(255, 255, 255), font=font)

# Add metadata to the image
metadata = {
    'Artist': 'Jane Smith',
    'Software': 'Python PIL Extended',
    'DateTime': '2022-01-15 10:30:00',
    'Description': 'This is a complex TIFF image with multiple layers and annotations.'
}

# Save the image with metadata and annotations
overlay_image.info.update(metadata)
overlay_image.save('./tmp/image_complex_extended.tiff', compression='tiff_adobe_deflate')

print("A TIFF file with multiple layers, blending mode, annotations, and extended metadata has been saved as 'image_complex_extended.tiff'.")