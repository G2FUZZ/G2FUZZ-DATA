import io
from PIL import Image

icon_sizes = [(16, 16), (32, 32), (48, 48)]

for size in icon_sizes:
    icon = Image.new('RGBA', size, color='red')
    with io.BytesIO() as output:
        icon.save(output, format='ICO')
        with open(f'./tmp/icon_{size[0]}x{size[1]}.ico', 'wb') as f:
            f.write(output.getvalue())