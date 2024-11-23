import os
from PIL import Image, ImageDraw

# Create the './tmp/' directory if it does not exist
output_dir = "./tmp"
os.makedirs(output_dir, exist_ok=True)

# Function to create an image and save it at different compression levels, including grayscale
def create_and_save_images(compression_levels, grayscale=False):
    for level in compression_levels:
        # Create a simple image with a few elements
        img = Image.new('RGB', (800, 600), color = (73, 109, 137))
        d = ImageDraw.Draw(img)
        d.text((10,10), f"Compression {level}{' Grayscale' if grayscale else ''}", fill=(255,255,0))
        
        if grayscale:
            # Convert the image to grayscale
            img = img.convert('L')
        
        # Define the filename based on the compression level and whether it is grayscale
        grayscale_suffix = "_grayscale" if grayscale else ""
        filename = f"{output_dir}/image_compression_{level}{grayscale_suffix}.jpg"
        
        # Save the image with the specified compression level
        img.save(filename, 'JPEG', quality=level)

# List of desired compression levels
compression_levels = [95, 75, 50, 25, 10]

# Generate and save the images in full color
create_and_save_images(compression_levels)

# Generate and save the images in grayscale
create_and_save_images(compression_levels, grayscale=True)

print("Images have been generated and saved with varying compression levels, including grayscale support.")