import io
from PIL import Image

# Create multiple images for the ICO file
images = []
sizes = [(16, 16), (32, 32), (64, 64)]  # Different sizes for the images

for size in sizes:
    new_image = Image.new('RGBA', size)
    images.append(new_image)

# Save the images into ICO format
for i, image in enumerate(images):
    with io.BytesIO() as output:
        image.save(output, format='ICO')
        with open(f'./tmp/icon_{i}.ico', 'wb') as file:
            file.write(output.getvalue())