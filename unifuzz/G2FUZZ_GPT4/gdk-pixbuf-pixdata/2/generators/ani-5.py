import os
from PIL import Image, ImageDraw

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

def create_ani_cursor(size, filename):
    """
    Creates a simple cursor of a specified size and saves it to a file.
    """
    # Create a new blank image with transparency
    img = Image.new('RGBA', (size, size), (255, 0, 0, 0))
    
    # Draw a simple shape to represent the cursor
    draw = ImageDraw.Draw(img)
    # Triangle points (simple arrow shape)
    points = [(size * 0.3, size * 0.3), (size * 0.3, size * 0.7), (size * 0.7, size * 0.5)]
    draw.polygon(points, fill='red')
    
    # Save the image in a supported format (e.g., PNG)
    img.save(filename.replace('.ani', '.png'))

# Generate cursors of variable sizes
sizes = [16, 32, 48, 64, 128]  # Different cursor sizes
for size in sizes:
    filename = f'./tmp/cursor_{size}.ani'
    create_ani_cursor(size, filename)