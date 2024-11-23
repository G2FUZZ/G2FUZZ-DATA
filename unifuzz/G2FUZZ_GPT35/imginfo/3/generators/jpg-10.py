import numpy as np
from PIL import Image, ImageDraw

# Create a simple image with text
image = Image.new('RGB', (400, 200), color='white')
text = "Artifacting: Lossy compression can lead to visual artifacts in high compression settings."
d = ImageDraw.Draw(image)
d.text((10, 10), text, fill='black')

# Save the image as a jpg file
image.save('./tmp/artifacting.jpg')