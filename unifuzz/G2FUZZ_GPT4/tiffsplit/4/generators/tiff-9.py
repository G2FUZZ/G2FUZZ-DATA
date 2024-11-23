from PIL import Image

# Create the directory if it doesn't exist
import os
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Create two images to act as layers
width, height = 800, 600
layer1 = Image.new('RGB', (width, height), color = 'red')
layer2 = Image.new('RGB', (width, height), color = 'blue')

# Save the images as a TIFF with multiple layers
# Note: TIFF format itself does not inherently support layers as in PSD files,
# but we can simulate layered saving by appending images in sequence.
layer1.save('./tmp/multilayer_image.tiff', save_all=True, append_images=[layer2])

print("TIFF file with layers created at './tmp/multilayer_image.tiff'")