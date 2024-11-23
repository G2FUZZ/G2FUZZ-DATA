from PIL import Image

# Create a new image with mode 'RGB' and size 100x100
image = Image.new('RGB', (100, 100))

# Save the image with quality settings
image.save('./tmp/quality_settings.jpg', quality=90)