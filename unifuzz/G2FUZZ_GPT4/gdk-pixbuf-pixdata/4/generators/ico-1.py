from PIL import Image, ImageDraw
import os

# Ensure the target directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

def create_icon_file(filename, sizes=[(16, 16), (32, 32), (48, 48), (64, 64)]):
    icon_images = []
    for size in sizes:
        # Create a new image with given size and mode ('RGBA' for transparency support)
        img = Image.new('RGBA', size, color=(255, 255, 255, 0))
        
        # Draw a simple shape on the image as an example
        draw = ImageDraw.Draw(img)
        draw.ellipse((0, 0, size[0]-1, size[1]-1), fill=(255, 0, 0, 255), outline=(0, 0, 0))
        
        # Append image to the list of images for the ICO file
        icon_images.append(img)
    
    # Save the images as a single ICO file containing multiple sizes
    ico_path = os.path.join(output_dir, filename)
    img.save(ico_path, format='ICO', sizes=sizes)

# Call the function with the desired ICO filename
create_icon_file('example.ico')