from PIL import Image
import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

def create_gradient_image(width, height, orientation='top-left'):
    """
    Creates a simple horizontal gradient image and saves it with the specified orientation.
    Orientation can be 'top-left' or 'bottom-left'.
    """
    # Create a new image with RGB mode
    image = Image.new("RGB", (width, height))
    
    # Generate a horizontal gradient
    for x in range(width):
        for y in range(height):
            # Gradient from black to white
            gradient_color = int((x / width) * 255)
            image.putpixel((x, y), (gradient_color, gradient_color, gradient_color))
    
    if orientation == 'bottom-left':
        # Flip the image vertically for bottom-left orientation
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
    
    # Save the image as TGA
    image.save(f'./tmp/gradient_{orientation}.tga')

# Create and save the images
create_gradient_image(100, 100, 'top-left')
create_gradient_image(100, 100, 'bottom-left')