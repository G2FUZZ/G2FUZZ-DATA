import io
from PIL import Image

# Create images for different sizes
sizes = [16, 32, 64]

for size in sizes:
    img = Image.new('RGB', (size, size), color='red')
    img_data = io.BytesIO()
    img.save(img_data, format='ICO', sizes=[(size, size)])
    with open(f'./tmp/icon_{size}.ico', 'wb') as f:
        f.write(img_data.getvalue())