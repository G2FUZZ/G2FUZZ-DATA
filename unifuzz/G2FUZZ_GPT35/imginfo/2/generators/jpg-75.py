import PIL.Image

# Create a new RGB image with size 200x200
image = PIL.Image.new('RGB', (200, 200))

# Set the pixel values for the image with gradient colors
for x in range(200):
    for y in range(200):
        red = x % 256  # Varying red component based on x coordinate
        green = y % 256  # Varying green component based on y coordinate
        blue = (x + y) % 256  # Varying blue component based on sum of x and y coordinates
        image.putpixel((x, y), (red, green, blue))

# Save the image as a jpg file with a more complex color gradient
image.save('./tmp/complex_structure.jpg', 'JPEG')