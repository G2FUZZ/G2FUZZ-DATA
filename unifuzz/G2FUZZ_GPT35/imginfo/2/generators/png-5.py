from PIL import Image
from PIL.PngImagePlugin import PngInfo

# Create a new PNG image
img = Image.new('RGB', (100, 100), color='white')

# Add metadata to the PNG image
metadata = PngInfo()
metadata.add_text('Description', 'This is a PNG file with metadata support')

# Save the image with metadata into ./tmp/
img.save('./tmp/metadata_support.png', pnginfo=metadata)