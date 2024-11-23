from PIL import Image

# Create a new image with RGB mode
img = Image.new('RGB', (400, 400), color = 'white')

# Draw a diagonal line
for i in range(400):
    img.putpixel((i, i), (0, 0, 0))

# Save the image in progressive mode
img.save('./tmp/progressive_image.jpg', 'JPEG', quality=95, optimize=True, progressive=True)