from PIL import Image

# Create a new image with RGB mode
image = Image.new("RGB", (100, 100), "white")

# Save the image in GIF format
image.save("./tmp/blank_image.gif")