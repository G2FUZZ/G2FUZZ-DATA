from PIL import Image

# Create a new image with RGB color mode
image = Image.new('RGB', (100, 100), color = 'white')

# Add text to the image
from PIL import ImageDraw, ImageFont

draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

text = "Compatibility: JPG is a widely supported file format that can be opened and viewed on most devices and software applications."
draw.text((10, 10), text, fill='black', font=font)

# Add APP markers to the image
app_marker_data = b'Application-specific data or extensions'
app_marker = b'\xff\xe0' + len(app_marker_data).to_bytes(2, byteorder='big') + app_marker_data
image.info["APP"] = app_marker

# Save the image with APP markers
image.save('./tmp/compatibility_with_APP_markers.jpg')