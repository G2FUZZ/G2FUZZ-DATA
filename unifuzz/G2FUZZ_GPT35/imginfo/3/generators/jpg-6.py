from PIL import Image

# Create an image with a solid color
image = Image.new('RGB', (100, 100), color='red')

# Save the image with different quality settings
quality_settings = [50, 75, 90]

for idx, quality in enumerate(quality_settings, start=1):
    image.save(f'./tmp/image_{idx}.jpg', quality=quality)