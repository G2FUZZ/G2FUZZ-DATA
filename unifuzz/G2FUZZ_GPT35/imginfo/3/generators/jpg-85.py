from PIL import Image, ImageDraw, ImageFilter

# Create a new image with transparency
image = Image.new('RGBA', (200, 200), (255, 255, 255, 0))

# Adding multiple layers to the image
layer1 = Image.new('RGBA', (200, 200), (255, 0, 0, 128))
layer2 = Image.new('RGBA', (200, 200), (0, 255, 0, 128))
image = Image.alpha_composite(image, layer1)
image = Image.alpha_composite(image, layer2)

# Applying a filter to the image
image = image.filter(ImageFilter.GaussianBlur(radius=5))

# Adding annotations to the image
draw = ImageDraw.Draw(image)
draw.text((20, 20), "Complex JPG Image", fill=(255, 255, 255, 128))

# Adding metadata to the image
metadata = {
    'Camera Model': 'Nikon D850',
    'Date Taken': '2022-02-15',
    'Exposure Time': '1/50 sec',
    'Aperture': 'f/5.6',
    'ISO': 400,
    'Author': 'John Doe',
    'Description': 'A creatively enhanced image',
}

image.info['metadata'] = metadata

# Convert the image to RGB mode before saving
image = image.convert('RGB')

# Save the image with metadata and complex features
image.save('./tmp/complex_image_example.jpg')