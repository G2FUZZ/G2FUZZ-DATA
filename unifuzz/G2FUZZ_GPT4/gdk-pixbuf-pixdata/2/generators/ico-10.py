from PIL import Image, ImageDraw
import os

def create_icon(save_path='./tmp/device_independent_icon.ico'):
    # Ensure the target directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Define icon sizes
    icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    
    icon_images = []
    for size in icon_sizes:
        # Create a new image with white background
        image = Image.new('RGBA', size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)
        
        # Draw a simple shape that scales with the image size
        # Here, we draw a circle that fills the image
        draw.ellipse((0, 0, size[0], size[1]), fill='blue', outline='red')
        
        icon_images.append(image)
    
    # Save the icon with multiple sizes
    icon_images[0].save(save_path, format='ICO', sizes=icon_sizes)

# Generate and save the icon
create_icon()