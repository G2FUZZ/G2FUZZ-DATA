import os
from PIL import Image, ImageDraw

# Create the './tmp/' directory if it does not exist
output_dir = "./tmp"
os.makedirs(output_dir, exist_ok=True)

# Function to draw a more complex pattern on the image
def draw_complex_pattern(draw):
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]  # Red, Green, Blue, Yellow
    for i, color in enumerate(colors):
        # Draw rectangles
        draw.rectangle([50 + i * 100, 50, 150 + i * 100, 150], outline=color, width=3)
        # Draw circles
        draw.ellipse([50 + i * 100, 200, 150 + i * 100, 300], outline=color, width=3)
        # Draw lines
        draw.line([400, 50 + i * 100, 550, 100 + i * 100], fill=color, width=3)

# Function to create an image and save it at different compression levels, including grayscale
def create_and_save_images(compression_levels, grayscale=False):
    for level in compression_levels:
        # Create a simple image with a few elements
        img = Image.new('RGB', (800, 600), color = (73, 109, 137))
        d = ImageDraw.Draw(img)
        draw_complex_pattern(d)
        d.text((10,10), f"Compression {level}{' Grayscale' if grayscale else ''}", fill=(255,255,0))
        
        if grayscale:
            # Convert the image to grayscale
            img = img.convert('L')
        
        # Define the directory and filename based on the compression level and whether it is grayscale
        grayscale_suffix = "grayscale" if grayscale else "color"
        subdir = f"{output_dir}/{grayscale_suffix}/{level}"
        os.makedirs(subdir, exist_ok=True)
        filename = f"{subdir}/image_compression_{level}.jpg"
        
        # Save the image with the specified compression level
        img.save(filename, 'JPEG', quality=level)

# List of desired compression levels
compression_levels = [95, 75, 50, 25, 10]

# Generate and save the images in full color
create_and_save_images(compression_levels)

# Generate and save the images in grayscale
create_and_save_images(compression_levels, grayscale=True)

print("Images have been generated and saved with varying compression levels, including grayscale support, featuring complex patterns.")