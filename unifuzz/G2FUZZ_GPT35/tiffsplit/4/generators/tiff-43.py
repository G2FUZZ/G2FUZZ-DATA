from PIL import Image, ImageDraw
from tifffile import TiffWriter

# Create a new RGBA image
image = Image.new('RGBA', (200, 200), (0, 255, 0, 128))

# Draw a rectangle on the image
draw = ImageDraw.Draw(image)
draw.rectangle([50, 50, 150, 150], fill=(255, 0, 0, 128))

# Create a new layer with a gradient
gradient = Image.new('RGBA', (200, 200), (0, 0, 0, 0))
for y in range(200):
    gradient.paste((y, 255, 255, 255), (0, y, 200, y + 1))

# Composite the gradient layer onto the image
image = Image.alpha_composite(image, gradient)

# Add metadata information
metadata = {
    'Author': 'John Doe',
    'Copyright': '2022',
    'Creation Date': '2022-09-15',
    'Compression Options': 'CCITT Group 4',
    'Layers and Alpha Channels': 'Supports layers for image editing and alpha channels for transparency effects',
    'Image Orientation': 'Portrait'  # Adding Image Orientation feature
}

# Save the image with metadata as a TIFF file
with TiffWriter('./tmp/mutated_metadata_example_with_layers_and_orientation.tiff') as tif:
    tif.save(image, metadata=metadata)