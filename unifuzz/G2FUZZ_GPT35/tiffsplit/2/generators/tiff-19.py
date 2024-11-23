from PIL import Image

# Create a new image with RGBA mode (4 layers: Red, Green, Blue, Alpha)
image = Image.new('RGBA', (100, 100))

# Create a transparency mask layer
transparency = Image.new('L', (100, 100), color=0)  # 0 indicates fully transparent

# Add the transparency mask layer to the image
image.putalpha(transparency)

# Save the image with layers and transparency as a TIFF file
image.save('./tmp/multi_layer_image_with_transparency.tiff', format='TIFF')