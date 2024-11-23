from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define different resolutions
resolutions = [(640, 480), (800, 600), (1024, 768)]

# Generate and save images
for i, resolution in enumerate(resolutions, start=1):
    # Create a new image with RGB mode and the specified resolution
    image = Image.new('RGB', resolution, 'blue')  # Example with a blue background

    # Save the image in BMP format (considering the limitation)
    image.save(f'./tmp/resolution_{i}.bmp')

print("Images generated and saved in './tmp/' directory.")