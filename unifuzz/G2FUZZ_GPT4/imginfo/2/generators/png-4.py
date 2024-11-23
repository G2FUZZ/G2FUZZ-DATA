from PIL import Image, PngImagePlugin, ImageDraw  # Import ImageDraw here

# Create a new image with RGB mode and white background
image_size = (100, 100)
image = Image.new("RGB", image_size, "white")

# Optionally, draw something on the image for demonstration
# For simplicity, let's draw a red rectangle
draw = ImageDraw.Draw(image)
draw.rectangle([20, 20, 80, 80], outline="red", width=2)

# Specify PNG info to use Adam7 interlacing
info = PngImagePlugin.PngInfo()
info.add_text("Interlace", "1")

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image with Adam7 interlacing
image.save("./tmp/interlaced_image.png", "PNG", pnginfo=info, interlace=1)