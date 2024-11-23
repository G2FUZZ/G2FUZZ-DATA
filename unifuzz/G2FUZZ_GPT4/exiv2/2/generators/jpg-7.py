import os
from PIL import Image, ImageDraw

# Create the /tmp directory if it doesn't already exist
os.makedirs('./tmp/', exist_ok=True)

# Function to create and save an image with adjustable quality
def create_and_save_image_with_quality(quality_level, file_name):
    # Create a simple image using PIL
    image = Image.new('RGB', (200, 100), color = (73, 109, 137))
    d = ImageDraw.Draw(image)
    d.text((10,10), f"Quality: {quality_level}", fill=(255,255,0))
    
    # Save the image with the specified quality level
    image_path = f'./tmp/{file_name}'
    image.save(image_path, 'JPEG', quality=quality_level)
    print(f"Image saved at {image_path} with quality level {quality_level}")

# Example usage: Create images with different quality levels
create_and_save_image_with_quality(30, 'image_quality_30.jpg')
create_and_save_image_with_quality(60, 'image_quality_60.jpg')
create_and_save_image_with_quality(90, 'image_quality_90.jpg')