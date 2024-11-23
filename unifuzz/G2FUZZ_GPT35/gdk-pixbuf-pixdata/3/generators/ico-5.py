import io
from PIL import Image

# Create images
image_formats = ['BMP', 'PNG', 'JPEG', 'GIF']
images = []
for format in image_formats:
    img = Image.new('RGB', (100, 100), color='red')
    images.append((format, img))

# Save images as ICO file
for format, img in images:
    output = io.BytesIO()
    img.save(output, format=format)
    
    with open(f'./tmp/image.{format.lower()}', 'wb') as f:
        f.write(output.getvalue())