from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define different sizes for scalability
sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

# Create a list to hold the images
icon_images = []

for size in sizes:
    # Create an image with RGB mode and the defined size
    image = Image.new("RGB", size, color=(255, 165, 0))  # Orange background for demonstration
    
    # Add the image to the list
    icon_images.append(image)

# Save the icon with multiple sizes for scalability
icon_path = './tmp/scalable_icon.ico'
# Corrected line: Use 'sizes' instead of 'icon_hits'
icon_images[0].save(icon_path, format='ICO', sizes=sizes)

print(f'Scalable ICO file saved at: {icon_path}')