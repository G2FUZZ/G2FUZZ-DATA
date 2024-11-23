from PIL import Image
from PIL.PngImagePlugin import PngInfo

# Create a new PNG image
image = Image.new('RGB', (100, 100), color='white')

# Add metadata to the image
metadata = PngInfo()
metadata.add_text('Description', 'This is a PNG file with metadata')
metadata.add_text('Author', 'Anonymous')
metadata.add_text('Timestamp', '2021-10-01')

# Save the image with metadata
image.save('./tmp/metadata_example.png', pnginfo=metadata)