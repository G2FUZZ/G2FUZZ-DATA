import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create a random image
width, height = 400, 300
data = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
image = Image.fromarray(data)

# Add text to the image
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()  # Load default font
text = "Hello, World!"
text_width, text_height = font.getmask(text).getbbox()[2:]
text_position = ((width - text_width) // 2, (height - text_height) // 2)
draw.text(text_position, text, fill=(255, 255, 255), font=font)

# Save the image as jpg with quality set to 95 and progressive mode enabled
image.save("./tmp/complex_image.jpg", format="JPEG", quality=95, optimize=True, progressive=True)