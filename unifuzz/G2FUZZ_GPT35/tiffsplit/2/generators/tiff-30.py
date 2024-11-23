from PIL import Image

# Create a new image with CMYK mode (4 layers: Cyan, Magenta, Yellow, Black)
image = Image.new('CMYK', (200, 200))

# Create transparency mask layers for each color channel
transparency_cyan = Image.new('L', (200, 200), color=100)  # 0 indicates fully transparent
transparency_magenta = Image.new('L', (200, 200), color=150)
transparency_yellow = Image.new('L', (200, 200), color=200)
transparency_black = Image.new('L', (200, 200), color=50)

# Add the transparency mask layers to the image for each color channel
image.putalpha(transparency_cyan)
image.putalpha(transparency_magenta)
image.putalpha(transparency_yellow)
image.putalpha(transparency_black)

# Save the image with multiple layers and transparencies as a TIFF file
image.save('./tmp/multi_layer_image_with_complex_structure.tiff', format='TIFF')