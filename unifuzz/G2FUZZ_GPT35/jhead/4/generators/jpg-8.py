from PIL import Image

# Create a new image
image = Image.new("RGB", (100, 100), color="white")
image.save("./tmp/original.jpg")

# Rotate the image 90 degrees clockwise without degrading image quality
rotated_image = image.rotate(-90, expand=True)
rotated_image.save("./tmp/rotated.jpg")