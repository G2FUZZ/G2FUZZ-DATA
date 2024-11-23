from PIL import Image, ImageDraw

# Create a new RGBA image
img = Image.new('RGBA', (200, 200), (0, 255, 0, 128))

# Draw a rectangle on the image
draw = ImageDraw.Draw(img)
draw.rectangle([50, 50, 150, 150], fill=(255, 0, 0, 128))

# Create a new layer with a gradient
gradient = Image.new('RGBA', (200, 200), (0, 0, 0, 0))
for y in range(200):
    gradient.paste((y, 255, 255, 255), (0, y, 200, y + 1))

# Composite the gradient layer onto the image
img = Image.alpha_composite(img, gradient)

# Save the image as a TIFF file with compression and multiple layers
img.save('./tmp/extended_transparency_example.tiff', compression='tiff_lzw', save_all=True, append_images=[gradient])