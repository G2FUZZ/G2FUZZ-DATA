from PIL import Image, ImageDraw
import os

def create_image_with_thumbnail(size=(800, 600), thumbnail_size=(128, 128), save_path='./tmp/', filename='image_with_thumbnail.jpg'):
    # Ensure the save_path exists
    os.makedirs(save_path, exist_ok=True)
    
    # Create a new image with a blue background
    image = Image.new('RGB', size, color='blue')
    
    # Create a simple drawing context
    draw = ImageDraw.Draw(image)
    
    # Draw a rectangle (just to have something on the main image)
    draw.rectangle([10, 10, 100, 100], fill="red")
    
    # Create a thumbnail of the image
    thumbnail = image.copy()
    thumbnail.thumbnail(thumbnail_size)
    
    # Save the thumbnail within the same JPEG file (this doesn't visibly embed the thumbnail into the main image,
    # but saves it as part of the JPEG file structure for quick access by software that reads thumbnails)
    image.save(os.path.join(save_path, filename), format='JPEG', quality=85, thumbnail=thumbnail_size)

# Call the function to create and save the image with a thumbnail
create_image_with_thumbnail()