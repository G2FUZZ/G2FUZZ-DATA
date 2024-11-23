from PIL import Image, ImageDraw, ImageFont
import datetime
import os

# Create a new GIF image
image = Image.new('RGB', (100, 100), color = 'white')

# Add metadata to the image
metadata = {
    "Author": "John Doe",
    "Creation Date": str(datetime.datetime.now()),
    "Comments": "This is a sample GIF file with metadata."
}

# Draw metadata on the image
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

y_offset = 10
for key, value in metadata.items():
    draw.text((10, y_offset), f"{key}: {value}", fill='black', font=font)
    y_offset += 20

# Save the image as a GIF file
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')
image.save('./tmp/metadata.gif', format='GIF')

print("GIF file with metadata has been saved.")