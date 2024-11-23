import os
from PIL import Image

# Create a new GIF image
new_gif = Image.new('RGB', (100, 100), color='white')

# Add text to the GIF image
from PIL import ImageDraw, ImageFont
draw = ImageDraw.Draw(new_gif)
font = ImageFont.load_default()
draw.text((10, 10), "Application-specific extensions", fill='black', font=font)

# Save the GIF image
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')
new_gif.save('./tmp/application_specific_extensions.gif')

print('GIF file with application-specific extensions generated and saved successfully.')