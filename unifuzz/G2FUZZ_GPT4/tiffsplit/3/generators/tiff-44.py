from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
directory_path = './tmp/'
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

# The path to the tiff file where you want to save the content
file_path = os.path.join(directory_path, 'example_file.tiff')

# Function to create an image for a specific page
def create_image(page_number, width=100, height=100, color=(255, 255, 255)):
    # Create a new image with white background
    image = Image.new('RGB', (width, height), color)
    draw = ImageDraw.Draw(image)

    # Draw a simple element that changes with page_number
    draw.text((10, 10), f"Page {page_number}", fill=(0, 0, 0))

    return image

# Create a list of images for a 3-page TIFF file
images = [create_image(i) for i in range(1, 4)]

# Save the images as a multi-page TIFF
images[0].save(file_path, save_all=True, append_images=images[1:], compression="tiff_deflate", dpi=(300, 300), metadata={"author": "Author Name", "description": "This is a multi-page TIFF file with custom metadata."})

print("TIFF file saved successfully in ./tmp/")