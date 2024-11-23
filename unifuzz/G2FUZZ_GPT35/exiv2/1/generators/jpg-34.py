from PIL import Image
from PIL import JpegImagePlugin

# Create an image
image = Image.new('RGB', (100, 100), color='red')

# Add metadata to the image
metadata = {
    'Author': 'John Doe',
    'Description': 'A beautiful red image with added metadata',
    'Date': '2023-01-15'
}
image.info['metadata'] = metadata

# Save the image at different quality levels with Quantization Tables and metadata
quality_levels = [10, 50, 80, 100]
for quality in quality_levels:
    image.save(f'./tmp/image_quality_{quality}_with_quantization_and_metadata.jpg', quality=quality, qtables='web_low')