from PIL import Image
from PIL import JpegImagePlugin

# Create an image
image = Image.new('RGB', (100, 100), color='red')

# Save the image at different quality levels with Quantization Tables
quality_levels = [10, 50, 80, 100]
for quality in quality_levels:
    image.save(f'./tmp/image_quality_{quality}_with_quantization.jpg', quality=quality, qtables='web_low')