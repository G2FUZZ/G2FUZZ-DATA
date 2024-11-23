from PIL import Image

# Create a new image with a black background
image = Image.new('RGB', (100, 100), color='black')

# Save the original image
image.save('./tmp/original.png')

# Rotate the image by 90 degrees without degrading quality
rotated_image = image.rotate(90, expand=True)
rotated_image.save('./tmp/rotated.png')