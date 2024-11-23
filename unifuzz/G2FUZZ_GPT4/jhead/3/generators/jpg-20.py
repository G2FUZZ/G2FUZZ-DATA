from PIL import Image, ImageDraw, ImageFont
import os

def add_exif_data(img, exif_data):
    """Add EXIF data to an image."""
    exif_bytes = None
    if exif_data:  # Ensure there's something to add
        exif_bytes = img.info.get('exif', b'')  # Get existing EXIF data, if any
    return exif_bytes

# Create a directory for the output if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a more complex image
img_size = (400, 300)
image = Image.new('RGB', img_size, color = '#333399')  # A nice shade of blue as background

# Add some custom text
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()  # Use PIL's default font
text_color = (255, 255, 0)  # Yellow text
draw.text((10, 10), "Hello, World!", fill=text_color, font=font)

# Save image
file_path = os.path.join(output_dir, 'complex_image.jpg')
image.save(file_path, 'JPEG')

print(f"Image saved with more complex features at {file_path}")