from PIL import Image

# Create a new image with RGB mode
image = Image.new('RGB', (100, 100))

# Set pixel values for the image
pixels = image.load()
for i in range(image.size[0]):
    for j in range(image.size[1]):
        pixels[i, j] = (i, j, 255)  # RGB color values

# Convert the image to YCbCr mode
image_ycbcr = image.convert('YCbCr')

# Save the image as a progressive JPEG file with YCbCr color encoding
image_ycbcr.save("./tmp/progressive_encoding_ycbcr.jpg", "JPEG", quality=95, optimize=True, progressive=True)