import os
from PIL import Image, ImageDraw

# Create the './tmp/' directory if it does not exist
output_dir = "./tmp"
os.makedirs(output_dir, exist_ok=True)

# Function to create an image and save it at different compression levels
def create_and_save_images(compression_levels):
    for level in compression_levels:
        # Create a simple image with a few elements
        img = Image.new('RGB', (800, 600), color = (73, 109, 137))
        d = ImageDraw.Draw(img)
        d.text((10,10), f"Compression {level}", fill=(255,255,0))
        
        # Define the filename based on the compression level
        filename = f"{output_dir}/image_compression_{level}.jpg"
        
        # Save the image with the specified compression level
        img.save(filename, 'JPEG', quality=level)

# List of desired compression levels
compression_levels = [95, 75, 50, 25, 10]

# Generate and save the images
create_and_save_images(compression_levels)

print("Images have been generated and saved with varying compression levels.")