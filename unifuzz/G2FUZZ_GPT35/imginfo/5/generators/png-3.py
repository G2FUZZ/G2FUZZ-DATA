from PIL import Image
from PIL.PngImagePlugin import PngInfo

# Create a new PNG image
img = Image.new('RGB', (100, 100), color='white')

# Add metadata to the image
metadata = PngInfo()
metadata.add_text('Author', 'John Doe')
metadata.add_text('Copyright', '2022')
metadata.add_text('Color Profile', 'sRGB')

# Save the image with metadata
img.save('./tmp/metadata_example.png', pnginfo=metadata)