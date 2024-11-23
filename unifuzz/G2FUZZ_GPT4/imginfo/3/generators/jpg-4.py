from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a simple image using Pillow
image = Image.new('RGB', (640, 480), color = (73, 109, 137))

# Optionally, draw some shapes or text on the image
draw = ImageDraw.Draw(image)
draw.text((10, 225), "Sample Image", fill=(255, 255, 0))

# Save the image in progressive JPEG format
output_path = os.path.join(output_dir, 'progressive_sample.jpg')
image.save(output_path, 'JPEG', quality=80, progressive=True)

print(f"Image saved to {output_path}")