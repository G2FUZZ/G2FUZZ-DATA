from PIL import Image

# Create a new image with progressive encoding
image = Image.new('RGB', (100, 100))
pixels = image.load()

# Fill the image with some color (e.g., red)
for i in range(image.size[0]):
    for j in range(image.size[1]):
        pixels[i, j] = (255, 0, 0)  # RGB color: red

# Save the image with progressive encoding
image.save('./tmp/progressive_image.jpg', format='JPEG', quality=95, optimize=True, progressive=True)

print("Progressive image created and saved successfully!")