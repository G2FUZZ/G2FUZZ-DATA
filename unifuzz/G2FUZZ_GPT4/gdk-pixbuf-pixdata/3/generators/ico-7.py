from PIL import Image, ImageDraw
import os

def create_icon_set(sizes=(16, 32, 48, 64, 128, 256)):
    # Ensure output directory exists
    output_dir = './tmp/'
    os.makedirs(output_dir, exist_ok=True)
    
    # Create a multi-resolution icon
    icon_filename = os.path.join(output_dir, 'efficient_icon.ico')
    
    icon_images = []
    for size in sizes:
        # Create an image with transparency
        image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        
        # Draw a simple shape that scales with the size
        draw = ImageDraw.Draw(image)
        padding = size // 4
        draw.ellipse((padding, padding, size-padding, size-padding), fill=(0, 120, 255, 255))
        
        # Resize image for the current size
        resized_image = image.resize((size, size), Image.Resampling.LANCZOS)  # Updated line here
        icon_images.append(resized_image)
    
    # Save as a single ICO file
    icon_images[0].save(icon_filename, format='ICO', sizes=[(i, i) for i in sizes])

create_icon_set()