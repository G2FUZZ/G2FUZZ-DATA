from PIL import Image
import os

def generate_image():
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Image size
    width, height = 800, 600
    
    # Create a new image with RGB mode and 24-bit color depth
    image = Image.new('RGB', (width, height))
    
    # Generate a gradient to showcase 24-bit color depth
    for x in range(width):
        for y in range(height):
            # Calculate color components to create a gradient effect
            # Note: Adjust the formulas as needed to create different gradients
            red = (x % 256)  # Red varies with X
            green = (y % 256)  # Green varies with Y
            blue = (x + y) % 256  # Blue varies with both X and Y
            
            # Set the pixel to the calculated color
            image.putpixel((x, y), (red, green, blue))
    
    # Save the image to the ./tmp/ directory with a 24-bit color depth
    file_path = './tmp/gradient_image.jpg'
    image.save(file_path, 'JPEG')
    
    print(f"Image saved to {file_path}")

generate_image()