from PIL import Image

# Create a new image with RGB mode and size 200x200
img = Image.new('RGB', (200, 200))

# Set a white background
img.paste((255, 255, 255), box=(0, 0, 200, 200))

# Add text with the given feature and comments
from PIL import ImageDraw, ImageFont

draw = ImageDraw.Draw(img)
font = ImageFont.load_default()
text = "Additional Features: This image includes advanced features for JPEG files."
draw.text((10, 10), text, fill=(0, 0, 0), font=font)

# Add Comments feature
comments = b'Comments: JPEG files can have embedded comments for additional information or metadata.'
img.info['comment'] = comments

# Add Progressive Display feature
progressive = True
img.save('./tmp/extended_feature.jpg', quality=95, progressive=progressive)