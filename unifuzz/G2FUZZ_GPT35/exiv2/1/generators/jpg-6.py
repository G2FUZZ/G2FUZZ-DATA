from PIL import Image

# Create an image
image = Image.new('RGB', (100, 100), color='red')

# Save the image at different quality levels
quality_levels = [10, 50, 80, 100]
for quality in quality_levels:
    image.save(f'./tmp/image_quality_{quality}.jpg', quality=quality)