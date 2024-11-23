from PIL import Image, ImageDraw
import os

def generate_chroma_subsampling_image():
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)

    # Create an image with a colorful pattern
    image_size = (400, 400)
    image = Image.new('RGB', image_size, 'white')
    draw = ImageDraw.Draw(image)
    
    for i in range(0, 400, 20):
        for j in range(0, 400, 20):
            color = (i % 256, j % 256, (i+j) % 256)
            draw.rectangle([i, j, i+10, j+10], fill=color)
    
    # Save the image with no chroma subsampling (4:4:4)
    image.save('./tmp/no_subsampling.jpg', 'JPEG', quality=95, subsampling=0)

    # Save the image with high chroma subsampling (4:2:0)
    image.save('./tmp/high_subsampling.jpg', 'JPEG', quality=95, subsampling=2)

generate_chroma_subsampling_image()