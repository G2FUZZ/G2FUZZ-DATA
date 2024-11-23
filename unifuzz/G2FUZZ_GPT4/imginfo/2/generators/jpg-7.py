from PIL import Image
import os

# Function to create an image of a specified size
def create_image(width, height):
    # Create a new image with RGB mode
    image = Image.new('RGB', (width, height), 'blue')
    return image

# Function to save images at different resolutions
def save_hierarchical_images(base_name, resolutions):
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    for resolution in resolutions:
        # Create an image at the specified resolution
        image = create_image(resolution[0], resolution[1])
        # Construct the filename based on resolution
        filename = f'./tmp/{base_name}_{resolution[0]}x{resolution[1]}.jpg'
        # Save the image
        image.save(filename)
        print(f'Saved: {filename}')

# List of resolutions (width x height)
resolutions = [
    (640, 480),  # Standard Definition
    (1280, 720), # HD
    (1920, 1080),# Full HD
    (3840, 2160) # 4K
]

# Save images at different resolutions
save_hierarchical_images('image', resolutions)