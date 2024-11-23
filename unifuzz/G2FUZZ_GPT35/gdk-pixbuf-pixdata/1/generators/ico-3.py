import io
from PIL import Image

# Create multiple images with different sizes
image_sizes = [(16, 16), (32, 32), (64, 64)]

images = []
for size in image_sizes:
    new_image = Image.new('RGB', size)
    images.append(new_image)

# Save the images to ICO file
ico_data = io.BytesIO()
images[0].save(ico_data, format='ICO', sizes=[im.size for im in images])

# Save the ICO file to disk
file_path = './tmp/multi_image_icon.ico'
with open(file_path, 'wb') as f:
    f.write(ico_data.getvalue())

print(f'ICO file with multiple images saved to: {file_path}')