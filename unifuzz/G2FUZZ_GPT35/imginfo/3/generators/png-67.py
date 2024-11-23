from PIL import Image, ImageDraw, PngImagePlugin

# Create a new RGBA image with transparency
image = Image.new('RGBA', (200, 200), color=(255, 255, 255, 0))

# Add a background layer
draw = ImageDraw.Draw(image)
draw.rectangle([(0, 0), (100, 100)], fill=(255, 0, 0, 128))

# Add a text layer
draw.text((50, 50), "Hello World!", fill=(0, 0, 0, 255))

# Add metadata to the PNG image
metadata = PngImagePlugin.PngInfo()
metadata.add_text('Author', 'Jane Smith')
metadata.add_text('Description', 'This is a complex PNG file with multiple layers and transparency')
metadata.add_text('CreationDate', '2021-10-20')

# Save the PNG image with metadata
image.save('./tmp/complex_png_example.png', pnginfo=metadata)