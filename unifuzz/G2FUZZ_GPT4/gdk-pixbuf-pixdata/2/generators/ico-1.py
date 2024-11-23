from PIL import Image, ImageDraw
import os

# Define the sizes for the ICO file
sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp', exist_ok=True)

# Create an empty list to hold the images
images = []

for size in sizes:
    # Create a new image with RGBA (includes alpha for transparency)
    img = Image.new("RGBA", size, color=(255, 0, 0, 0))
    
    # Get a drawing context
    draw = ImageDraw.Draw(img)
    
    # Draw a simple shape; for example, a circle that fits the size
    draw.ellipse((0, 0, size[0], size[1]), fill=(255, 165, 0, 255), outline=(0, 0, 0, 255))
    
    # Add the image to the list
    images.append(img)

# Save the images as an ICO file
ico_path = './tmp/multi_size_icon.ico'
images[0].save(ico_path, format='ICO', sizes=[(img.width, img.height) for img in images])

print(f"ICO file with multiple sizes saved to: {ico_path}")