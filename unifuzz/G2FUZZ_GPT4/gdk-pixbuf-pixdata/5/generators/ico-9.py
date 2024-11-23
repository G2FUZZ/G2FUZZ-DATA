from PIL import Image, ImageDraw

def create_icon(path):
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]  # Common icon sizes for compatibility
    
    icon_images = []
    
    for size in sizes:
        image = Image.new("RGBA", size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        
        # Create a simple gradient fill
        for i in range(size[0]):
            gradient_color = (int(255 * (i/size[0])), 0, int(255 * (1 - i/size[0])), 255)
            draw.line([(i, 0), (i, size[1])], fill=gradient_color)
        
        icon_images.append(image)
    
    # Save the icon with different sizes for compatibility
    icon_images[0].save(path, format="ICO", sizes=[img.size for img in icon_images])

# Ensure the tmp directory exists
import os
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Create and save the icon
create_icon('./tmp/backwards_compatible_icon.ico')