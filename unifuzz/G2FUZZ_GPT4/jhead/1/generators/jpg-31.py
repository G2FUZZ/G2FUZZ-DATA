from PIL import Image, ImageDraw
import os

def generate_advanced_image():
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
    
    # Save the image without EXIF data
    image.save('./tmp/advanced_features.jpg', 'JPEG', quality=95, subsampling=0)

    # Generate and save multiple resolutions of the image (image pyramid)
    for scale in [0.5, 0.25, 0.125]:
        resized_image = image.resize((int(image_size[0] * scale), int(image_size[1] * scale)), Image.ANTIALIAS)
        resized_image.save(f'./tmp/resized_{int(scale*100)}.jpg', 'JPEG', quality=90)

generate_advanced_image()