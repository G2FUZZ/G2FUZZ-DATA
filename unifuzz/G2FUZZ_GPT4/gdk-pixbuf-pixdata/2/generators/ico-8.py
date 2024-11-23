import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_png_image(size):
    # Create a PNG image with alpha transparency
    img = Image.new('RGBA', size, color=(255, 0, 0, 0))  # Transparent background
    draw = ImageDraw.Draw(img)
    # Draw a red circle with alpha transparency
    draw.ellipse((size[0]//4, size[1]//4, 3*size[0]//4, 3*size[1]//4), fill=(255, 0, 0, 127))
    return img

def create_bmp_image(size):
    # Create a BMP image without alpha transparency (simulating legacy support)
    img = Image.new('RGB', size, color=(0, 255, 0))  # Green background
    draw = ImageDraw.Draw(img)
    # Draw a blue square
    draw.rectangle((size[0]//4, size[1]//4, 3*size[0]//4, 3*size[1]//4), fill=(0, 0, 255))
    return img

def save_ico_with_mixed_content(filename, sizes=[(32, 32), (64, 64), (128, 128)]):
    images = []
    for size in sizes:
        if size[0] <= 64:  # Use BMP for smaller images for legacy support
            img = create_bmp_image(size)
        else:  # Use PNG for larger images to utilize alpha transparency
            img = create_png_image(size)
        images.append(img)
    
    # Saving the images as an ICO file containing a mix of PNG and BMP images
    images[0].save(filename, format='ICO', sizes=[img.size for img in images], append_images=images[1:])

# Generate an ICO file with mixed content
ico_path = './tmp/mixed_content.ico'
save_ico_with_mixed_content(ico_path)

print(f"ICO file with mixed content saved at: {ico_path}")