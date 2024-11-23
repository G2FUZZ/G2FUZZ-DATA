from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Path to the TIFF file to be created
file_path = './tmp/example_file.tiff'

# Create a list to hold the image pages
images = []

# Generate multiple images/pages for the TIFF
for i in range(5):  # Creating 5 pages as an example
    # Create a new image with white background, 100x100 pixels
    img = Image.new('RGB', (100, 100), 'white')
    draw = ImageDraw.Draw(img)
    
    # Draw something simple on the image
    # Here, we're just adding text and a line
    draw.text((10, 10), f'Page {i+1}', fill='black')
    draw.line((10, 30, 90, 30), fill='black', width=2)
    
    # Add the image to the list of pages
    images.append(img)

# Save the images as a multi-page TIFF
# The first image is saved using save(), and the rest are appended using save_all()
images[0].save(file_path, save_all=True, append_images=images[1:], compression="tiff_deflate")

print(f'Multi-page TIFF file has been saved to {file_path}')