from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with 24-bit color (RGB)
width, height = 800, 600
image = Image.new('RGB', (width, height))

# Generate a gradient effect for demonstration
for x in range(width):
    for y in range(height):
        # Calculate color components to create a gradient
        # This is just one way to demonstrate 24-bit color depth
        r = (x // 3) % 256
        g = (y // 3) % 256
        b = (x + y) // 6 % 256
        image.putpixel((x, y), (r, g, b))

# Save the image
image_path = './tmp/gradient_image.jpg'
image.save(image_path, 'JPEG')

print(f"Image saved to {image_path}")