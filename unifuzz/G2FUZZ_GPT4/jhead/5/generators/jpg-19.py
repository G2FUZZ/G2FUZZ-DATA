from PIL import Image, ImageDraw, ImageFont, ExifTags
import os

def create_complex_image(save_path='./tmp/', filename='complex_image_with_thumbnail.jpg'):
    # Ensure the save_path exists
    os.makedirs(save_path, exist_ok=True)
    
    # Image size
    size = (800, 600)
    thumbnail_size = (128, 128)
    
    # Create a new image with a gradient background
    image = Image.new('RGB', size)
    draw = ImageDraw.Draw(image)
    for i in range(size[1]):
        gradient_color = int(255 * (i/size[1]))
        draw.line([(0, i), (size[0], i)], fill=(gradient_color, gradient_color, 255))
    
    # Draw multiple shapes
    draw.rectangle([10, 10, 100, 100], fill="red", outline="black")
    draw.ellipse([150, 10, 250, 110], fill="green", outline="black")
    draw.polygon([(300, 10), (350, 100), (250, 100)], fill="yellow", outline="black")
    
    # Adding custom text
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except IOError:
        font = ImageFont.load_default()
    draw.text((10, 500), "Complex Image Example", fill="white", font=font)
    
    # Create a semi-transparent watermark
    watermark = Image.new('RGBA', size, (255, 255, 255, 0))
    watermark_draw = ImageDraw.Draw(watermark)
    watermark_text = "© Your Company"
    watermark_draw.text((size[0]-200, size[1]-40), watermark_text, fill=(255, 255, 255, 128), font=font)
    
    # Apply the watermark
    image.paste(watermark, (0, 0), watermark)
    
    # Create a thumbnail of the image
    thumbnail = image.copy()
    thumbnail.thumbnail(thumbnail_size)
    
    # Save the image
    full_path = os.path.join(save_path, filename)
    image.save(full_path, format='JPEG', quality=85)

# Call the function to create and save the complex image
create_complex_image()