from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile

# Create a new image with RGB color mode and size 100x100
img = Image.new('RGB', (100, 100))

# Add JFIF format feature to the image
img.info["jfif"] = 1

# Save the image with JPEG format and color depth of 8 bits per channel
img.save('./tmp/color_depth_example_with_JFIF.jpg', quality=95)