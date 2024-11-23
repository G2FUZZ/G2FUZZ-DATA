import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata files with image dimensions
image_dimensions = [(640, 480), (800, 600), (1024, 768)]

for idx, (width, height) in enumerate(image_dimensions, start=1):
    with open(f'./tmp/pixdata_{idx}.txt', 'w') as file:
        file.write(f'Image dimensions: {width}x{height} pixels\n')