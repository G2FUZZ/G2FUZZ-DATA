from PIL import Image

# Create a sample image
image = Image.new('RGB', (100, 100), color='white')
image.save('./tmp/quality_setting_subsampling.jpg', quality=85, subsampling='4:2:0')  # Subsampling ratio 4:2:0