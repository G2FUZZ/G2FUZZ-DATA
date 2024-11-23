from PIL import Image, ImageDraw

def create_bmp_with_basic_metadata(output_path):
    # Create an image with a white background
    width, height = 640, 480
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Draw some simple elements and text to mimic metadata
    # This is just to demonstrate, as BMP does not support extensive metadata like JPEG or PNG.
    text = "Author: John Doe\nCopyright: 2023\nSoftware: Pillow"
    draw.text((10, 10), text, fill='black')

    # Save the image as BMP
    image.save(output_path)

# Ensure the ./tmp/ directory exists or create it
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

create_bmp_with_basic_metadata('./tmp/metadata_example.bmp')