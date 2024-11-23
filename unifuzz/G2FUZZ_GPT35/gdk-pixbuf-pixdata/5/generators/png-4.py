from PIL import Image
from PIL.PngImagePlugin import PngInfo

# Create a new PNG image
image = Image.new('RGB', (100, 100), color='white')

# Add metadata to the PNG image
metadata = PngInfo()
metadata.add_text('Title', 'Sample PNG Image')
metadata.add_text('Author', 'John Doe')
metadata.add_text('Creation Date', '2022-01-01')

# Save the PNG image with metadata
image.save('./tmp/sample_image.png', pnginfo=metadata)