from PIL import Image

# Create a new image with RGB mode and size 100x100
image = Image.new('RGB', (100, 100))

# Set the pixel values for the entire image
for x in range(100):
    for y in range(100):
        image.putpixel((x, y), (255, 255, 255))  # Set pixel color to white

# Save the image as a jpg file in the ./tmp/ directory
image.save('./tmp/high_compatibility.jpg')