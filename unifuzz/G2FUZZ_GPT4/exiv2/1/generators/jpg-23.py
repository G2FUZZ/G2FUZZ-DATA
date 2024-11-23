import os
from PIL import Image, ImageDraw, JpegImagePlugin

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

# Function to create hierarchical storage images
def create_hierarchical_storage_image(base_filename, sizes, quality_levels):
    # Create a base image
    base_img = Image.new('RGB', (800, 600), color = (73, 109, 137))
    d = ImageDraw.Draw(base_img)
    d.text((10,10), "Hierarchical Storage", fill=(255,255,0))

    # Iterate over sizes and quality levels to create images
    for size in sizes:
        for quality in quality_levels:
            # Resize image
            resized_img = base_img.resize(size, Image.ANTIALIAS)
            
            # Define the filename for the current size and quality
            filename = f"{output_dir}/{base_filename}_{size[0]}x{size[1]}_compression_{quality}.jpg"
            
            # Save the resized image with the specified quality
            resized_img.save(filename, 'JPEG', quality=quality)

# New function to create and save an image with JFIF Format feature
def create_and_save_jfif_image(filename, quality=95):
    # Create a simple image with a few elements
    img = Image.new('RGB', (800, 600), color = (73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((10,10), "JFIF Format Example", fill=(255,255,0))
    
    # Define the filename for JFIF format
    filepath = f"{output_dir}/{filename}.jpg"
    
    # Save the image with JFIF format
    # PIL automatically handles the JPEG/JFIF format, but we can explicitly define dpi and other parameters if needed
    img.save(filepath, 'JPEG', quality=quality, dpi=(72, 72), subsampling=0)

# List of desired compression levels
compression_levels = [95, 75, 50, 25, 10]

# Generate and save the images with simple compression
create_and_save_images(compression_levels)

# Define sizes for hierarchical storage (width x height)
sizes = [(800, 600), (640, 480), (320, 240), (160, 120)]

# Generate and save the hierarchical storage images
create_hierarchical_storage_image("hierarchical_storage", sizes, compression_levels)

# Generate and save an image with JFIF format
create_and_save_jfif_image("jfif_example", 95)

print("Images have been generated and saved with varying compression levels, including hierarchical storage and JFIF format.")