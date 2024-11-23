from PIL import Image

def create_image_with_thumbnail(image_path, thumbnail_size=(128, 128)):
    # Create a new image using RGB mode
    image = Image.new('RGB', (800, 600), (255, 200, 150))

    # Create a thumbnail of the image
    thumbnail = image.copy()
    thumbnail.thumbnail(thumbnail_size)

    # Embed the thumbnail in the original image
    image.save(image_path, "JPEG", quality=85, thumbnail=thumbnail)

# Create a directory for the output if it doesn't exist
import os
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate the image with an embedded thumbnail
image_path = os.path.join(output_dir, 'image_with_thumbnail.jpg')
create_image_with_thumbnail(image_path)

print(f"Image with embedded thumbnail saved to {image_path}")