from PIL import Image, ImageOps

def create_image_with_thumbnail(image_path, thumbnail_path, output_path):
    # Create an example image (for demonstration purposes)
    original_image = Image.new('RGB', (800, 600), 'blue')
    original_image.save(image_path)

    # Open the original image
    with Image.open(image_path) as img:
        # Create a thumbnail
        thumbnail = img.copy()
        thumbnail.thumbnail((160, 120), Image.ANTIALIAS)
        thumbnail.save(thumbnail_path)

        # Embed the thumbnail in the original image's EXIF (requires saving the image again)
        exif = img.info['exif'] if 'exif' in img.info else b''
        img.save(output_path, 'JPEG', exif=exif, thumbnail=thumbnail)
    
    print(f"Image with embedded thumbnail saved to {output_path}")

# Define paths
image_path = './tmp/original_image.jpg'
thumbnail_path = './tmp/thumbnail.jpg'
output_path = './tmp/image_with_thumbnail.jpg'

# Ensure the './tmp/' directory exists
import os
os.makedirs('./tmp/', exist_ok=True)

# Create and save the image with an embedded thumbnail
create_image_with_thumbnail(image_path, thumbnail_path, output_path)