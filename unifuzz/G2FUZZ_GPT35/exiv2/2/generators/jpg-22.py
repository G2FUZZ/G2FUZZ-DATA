from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile

# Create a new image with RGB color mode and size 100x100
img = Image.new('RGB', (100, 100))

# Add JFIF format feature to the image
img.info["jfif"] = 1

# Add custom APP markers for application-specific information
app_marker_data = b'My Custom APP Marker Data'
app_marker = b'\xff\xe1' + (len(app_marker_data) + 2).to_bytes(2, 'big') + app_marker_data
img.info["APP"] = app_marker

# Save the image with JPEG format and color depth of 8 bits per channel
img.save('./tmp/color_depth_example_with_JFIF_and_APP.jpg', quality=95)