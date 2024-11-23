import os
from PIL import Image

# Ensure the target directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define multiple resolutions
resolutions = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

# Initialize a list to hold the images
images = []

# Generate images for each resolution
for res in resolutions:
    # Create a new image with RGBA mode
    image = Image.new('RGBA', res, color=(255, 0, 0, 0))
    
    # Use a simple drawing example: A blue square
    for x in range(res[0]):
        for y in range(res[1]):
            if 5 < x < res[0] - 5 and 5 < y < res[1] - 5:
                image.putpixel((x, y), (0, 0, 255, 255))
    
    # Append the image to the list of images
    images.append(image)

# Save the list of images as a single ICO file
ico_path = os.path.join(output_dir, 'multi_resolution_icon.ico')
images[0].save(ico_path, format='ICO', sizes=[(img.width, img.height) for img in images])