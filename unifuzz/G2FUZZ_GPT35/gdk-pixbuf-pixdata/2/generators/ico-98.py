import io
from PIL import Image

# Create images with different color depths and sizes
images = [
    Image.new('RGB', (16, 16), color='red'),
    Image.new('RGB', (32, 32), color='green'),
    Image.new('RGBA', (64, 64), color='blue').convert('P', palette=Image.ADAPTIVE)
]

# Save images to an ICO file with varied color depths and sizes
ico_data = io.BytesIO()
for img in images:
    img.save(ico_data, format='ICO', sizes=[(size, size) for size in range(16, 65, 16)], quality=90)

# Write the ICO file to disk
with open('./tmp/complex_icon.ico', 'wb') as f:
    f.write(ico_data.getvalue())