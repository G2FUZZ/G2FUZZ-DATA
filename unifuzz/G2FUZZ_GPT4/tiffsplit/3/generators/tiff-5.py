from PIL import Image, ImageDraw

# Create the tmp directory if it doesn't exist
import os
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Function to create a simple image for demonstration
def create_image(color, size=(100, 100)):
    image = Image.new("RGB", size, color)
    return image

# Create two simple images to act as layers
layer1 = create_image("red")
layer2 = create_image("blue")

# Saving the images as layers (frames) in a TIFF
layer1.save('./tmp/multi_layer.tiff', save_all=True, append_images=[layer2])

print("TIFF with layers created at ./tmp/multi_layer.tiff")