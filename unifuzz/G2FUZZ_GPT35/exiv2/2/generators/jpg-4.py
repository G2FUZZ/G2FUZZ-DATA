from PIL import Image

# Create a gradient image
width, height = 400, 400
image = Image.new('RGB', (width, height))

pixels = []
for y in range(height):
    for x in range(width):
        r = int(x / width * 255)
        g = int(y / height * 255)
        b = 128
        pixels.append((r, g, b))

image.putdata(pixels)

# Save the image in progressive format
image.save('./tmp/progressive_image.jpg', 'JPEG', quality=95, optimize=True, progressive=True)

print("Progressive JPEG image saved successfully.")