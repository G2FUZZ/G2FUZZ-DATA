from PIL import Image, ImageDraw, ImageFont, ExifTags, PngImagePlugin
import os

def create_complex_image_with_thumbnail_and_metadata(size=(800, 600), thumbnail_size=(128, 128), save_path='./tmp/', filename='complex_image_with_thumbnail.jpg'):
    # Ensure the save_path exists
    os.makedirs(save_path, exist_ok=True)
    
    # Create a new image with a gradient background
    image = Image.new('RGB', size)
    draw = ImageDraw.Draw(image)
    for i, color in enumerate(range(255)):
        draw.line([(i, 0), (i, size[1])], fill=(color, 125, 125), width=1)
    
    # Create a more complex drawing
    # Draw multiple shapes
    draw.ellipse([size[0]//2 - 50, size[1]//2 - 50, size[0]//2 + 50, size[1]//2 + 50], fill="green", outline="yellow")
    draw.rectangle([10, 10, 100, 100], fill="red")
    draw.line([(0, 0), size], fill="white", width=3)
    
    # Add custom text
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except IOError:
        font = ImageFont.load_default()
    draw.text((10, size[1] - 50), "Hello, World!", fill="white", font=font)
    
    # Create a thumbnail of the image
    thumbnail = image.copy()
    thumbnail.thumbnail(thumbnail_size)
    
    # Prepare to add EXIF metadata
    exif_data = PngImagePlugin.PngInfo()
    exif_data.add_text("Description", "This is an example of a complex image with a thumbnail and EXIF metadata.")
    exif_data.add_text("Author", "Automated script")
    exif_data.add_text("Software", "Pillow in Python")
    
    # Save the image with EXIF metadata
    image.save(os.path.join(save_path, filename), format='JPEG', quality=85, pnginfo=exif_data)
    
    # Save the thumbnail as a separate file (demonstration purpose)
    thumbnail_save_path = os.path.splitext(os.path.join(save_path, filename))[0] + '_thumbnail.jpg'
    thumbnail.save(thumbnail_save_path, format='JPEG', quality=85)

# Call the function to create and save the complex image
create_complex_image_with_thumbnail_and_metadata()