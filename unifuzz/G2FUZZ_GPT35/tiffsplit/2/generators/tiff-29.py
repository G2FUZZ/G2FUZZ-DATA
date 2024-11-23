from PIL import Image
from PIL.TiffTags import TAGS_V2

# Create a new image with some data
data = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
img = Image.new('RGB', (2, 2))
img.putdata(data)

# Set resolution
resolution_unit = 2  # inch
x_resolution_tag = 282  # XResolution tag ID
y_resolution_tag = 283  # YResolution tag ID
resolution_unit_tag = 296  # ResolutionUnit tag ID
x_resolution = (300, 1)  # 300 DPI
y_resolution = (300, 1)  # 300 DPI
img.info.update({x_resolution_tag: x_resolution, y_resolution_tag: y_resolution, resolution_unit_tag: resolution_unit})

# Add metadata
metadata = {
    'Author': 'John Doe',
    'Description': 'Sample TIFF Image with Metadata',
    'Software': 'Python Imaging Library',
}
for tag, value in metadata.items():
    img.info[tag] = value

# Convert color space to CMYK
img_cmyk = img.convert('CMYK')

# Save the image with TIFF format and compression
img_cmyk.save('./tmp/complex_image.tiff', compression='tiff_adobe_deflate')