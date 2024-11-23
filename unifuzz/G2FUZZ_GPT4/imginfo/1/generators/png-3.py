from PIL import Image
import numpy as np
import os

# Make sure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create and save an image with a specified color depth
def create_png_with_color_depth(bits, width=100, height=100):
    filename = f'./tmp/image_{bits}bit.png'
    
    if bits == 1:  # 1-bit image (black and white)
        image = Image.new("1", (width, height))
        # Create a simple pattern
        for x in range(width):
            for y in range(height):
                image.putpixel((x, y), x % 2 == y % 2)
                
    elif bits == 8:  # 8-bit image (256 colors)
        image = Image.new("P", (width, height))
        # Create a gradient
        for x in range(width):
            for y in range(height):
                image.putpixel((x, y), (x + y) % 256)
                
    elif bits == 16:  # 16-bit image (65,536 colors)
        # Create a gradient using numpy for simplicity
        array = np.zeros((height, width, 3), dtype=np.uint16)
        for i in range(3):  # Separate channel manipulation for demonstration
            array[:, :, i] = np.linspace(0, 65535, num=width, endpoint=True, dtype=np.uint16)
        image = Image.fromarray(array, mode="I;16")
        
    else:
        print(f"Unsupported color depth: {bits} bits")
        return
    
    image.save(filename)
    print(f"Image saved with {bits}-bit color depth: {filename}")

# Create images with different color depths
create_png_with_color_depth(1)
create_png_with_color_depth(8)
create_png_with_color_depth(16)