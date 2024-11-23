from PIL import Image

# Create a sample image
image = Image.new('RGB', (100, 100), color='white')
image.save('./tmp/quality_setting_progressive.jpg', quality=85, progressive=True)  # Progressive coding