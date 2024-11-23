from PIL import Image

# Create a sample image
image = Image.new('RGB', (100, 100), color='white')
image.save('./tmp/quality_setting_100.jpg', quality=100)  # Maximum quality
image.save('./tmp/quality_setting_50.jpg', quality=50)  # Medium quality
image.save('./tmp/quality_setting_10.jpg', quality=10)  # Low quality