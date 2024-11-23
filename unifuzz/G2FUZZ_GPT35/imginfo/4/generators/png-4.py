from PIL import Image
from PIL.PngImagePlugin import PngInfo

# Create a new PNG image
image = Image.new('RGB', (100, 100), color='white')

# Add metadata to the image
metadata = PngInfo()
metadata.add_text('Author', 'John Doe')
metadata.add_text('Copyright', '2021')
metadata.add_text('Creation Date', '2021-10-01')

# Save the image with metadata
image.save('./tmp/metadata_example.png', pnginfo=metadata)