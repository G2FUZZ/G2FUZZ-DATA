import io
from PIL import Image

# Create images at different resolutions
sizes = [(16, 16), (32, 32), (64, 64)]
images = [Image.new('RGB', size, color='red') for size in sizes]

# Save images to an ICO file
ico_data = io.BytesIO()
images[0].save(ico_data, format='ICO', sizes=[(size[0], size[1]) for size in sizes])

# Write the ICO file to disk
with open('./tmp/icon.ico', 'wb') as f:
    f.write(ico_data.getvalue())