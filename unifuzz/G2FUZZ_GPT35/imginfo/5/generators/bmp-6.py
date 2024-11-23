from PIL import Image

# Create a new image with metadata
image = Image.new('RGB', (100, 100), color='white')
image.info['resolution'] = (300, 300)
image.info['color_profile'] = 'sRGB'
image.info['created_timestamp'] = '2022-01-01 12:00:00'

# Save the image with metadata
image.save('./tmp/metadata_example.bmp')