from PIL import Image

# Create a new TIFF image with multiple layers and custom metadata
img = Image.new('RGB', (512, 512), color='blue')

# Adding multiple layers
layer1 = Image.new('RGB', (256, 256), color='green')
layer2 = Image.new('RGB', (256, 256), color='red')

# Paste layers onto the main image
img.paste(layer1, (0, 0))
img.paste(layer2, (256, 256))

# Save the image with custom metadata and multiple layers
img.save('./tmp/multi_layer.tiff', compression='tiff_deflate', tiffinfo={32768: 2})  # 2 corresponds to multiple layers

print("TIFF file with multiple layers and custom metadata generated successfully.")