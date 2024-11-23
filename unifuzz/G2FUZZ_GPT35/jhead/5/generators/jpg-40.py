from PIL import Image, ImageFilter

# Create a new image with a pattern
image = Image.new('RGB', (200, 200))
pixels = image.load()

# Fill the image with a pattern
for i in range(image.size[0]):
    for j in range(image.size[1]):
        if (i // 50) % 2 == (j // 50) % 2:
            pixels[i, j] = (255, 255, 255)  # RGB color: white
        else:
            pixels[i, j] = (0, 0, 0)  # RGB color: black

# Apply a blur filter to the image
blurred_image = image.filter(ImageFilter.BLUR)

# Save the blurred image with progressive encoding and a higher quality level
blurred_image.save('./tmp/progressive_blurred_image.jpg', format='JPEG', quality=90, optimize=True, progressive=True)

print("Progressive blurred image created and saved successfully!")