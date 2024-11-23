from PIL import Image
from PIL.PngImagePlugin import PngInfo

# Create a new PNG image
image = Image.new('RGB', (100, 100), color='white')

# Add metadata to the image
metadata = {
    'Author': 'John Doe',
    'Copyright': '2022',
    'CreationDate': '2022-10-30'
}
png_info = PngInfo()
for key, value in metadata.items():
    png_info.add_text(key, value)

# Save the image with metadata
image.save('./tmp/metadata_example.png', pnginfo=png_info)