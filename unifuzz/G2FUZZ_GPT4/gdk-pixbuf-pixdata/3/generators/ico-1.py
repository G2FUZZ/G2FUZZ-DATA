from PIL import Image, ImageDraw
import os

# Directory for saving the generated ICO files
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

def create_icon(sizes=(16, 32, 48, 64, 128, 256)):
    """
    Creates an ICO file containing images of different sizes.
    """
    # Creating a list to hold the images
    icon_images = []
    
    for size in sizes:
        # Create a new image with RGBA mode
        image = Image.new("RGBA", (size, size), (255, 255, 255, 0))
        
        # Creating a drawing context
        draw = ImageDraw.Draw(image)
        
        # Drawing a simple shape that changes with the size of the image
        # Here, we draw a rectangle and a circle
        draw.rectangle([0, 0, size-1, size-1], outline="red", fill="blue")
        draw.ellipse([size//4, size//4, 3*size//4, 3*size//4], outline="green", fill="yellow")
        
        # Adding the image to the list
        icon_images.append(image)
    
    # Saving the images in the icon_images list as a single ICO file
    # The filename will be 'multi_size_icon.ico' in the './tmp/' directory
    icon_filename = os.path.join(output_path, 'multi_size_icon.ico')
    icon_images[0].save(icon_filename, format='ICO', sizes=[(image.width, image.height) for image in icon_images])

# Ensure the output directory exists
output_path = './tmp/'
if not os.path.exists(output_path):
    os.makedirs(output_path)

create_icon()