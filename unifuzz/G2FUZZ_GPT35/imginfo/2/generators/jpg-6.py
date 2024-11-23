import PIL.Image

# Create a new RGB image with size 100x100
image = PIL.Image.new('RGB', (100, 100))

# Set the pixel values for the image
for x in range(100):
    for y in range(100):
        image.putpixel((x, y), (255, 255, 255))  # Set all pixels to white

# Save the image as a jpg file
image.save('./tmp/compatibility.jpg', 'JPEG')