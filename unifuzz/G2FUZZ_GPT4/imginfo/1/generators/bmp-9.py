from PIL import Image
import os

# Create a directory for saving the file if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define image size (width, height) - adjust these values to increase or decrease file size
image_size = (8000, 8000)  # This will create a very large BMP file

# Define the image color (R, G, B)
image_color = (0, 120, 255)  # Solid blue

# Create a new image with the specified size and color
image = Image.new('RGB', image_size, image_color)

# Define the file path
file_path = os.path.join(output_dir, 'large_image.bmp')

# Save the image as BMP
image.save(file_path)

print(f"Image saved at {file_path}")