from PIL import Image, ImageDraw
import os

# Create a directory to store the generated TIFF file
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)  # Corrected variable name

# Function to create a simple image with a single colored rectangle
def create_image(color, size=(100, 100)):
    image = Image.new('RGB', size, "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle([10, 10, 90, 90], fill=color)
    return image

# Create a few images with different colors
images = [
    create_image('red'),
    create_image('green'),
    create_image('blue'),
    create_image('yellow')
]

# Save the images as a multi-page TIFF
images[0].save(
    os.path.join(output_dir, 'multi_page.tiff'),
    save_all=True,
    append_images=images[1:]
)