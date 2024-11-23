from PIL import Image

# Create a new image with RGB mode
image = Image.new('RGB', (100, 100))

# Set pixel values for the image
pixels = image.load()
for i in range(image.size[0]):
    for j in range(image.size[1]):
        pixels[i, j] = (i, j, 255)  # RGB color values

# Save the image as a progressive JPEG file with variable quality and compression level
for quality in range(70, 100, 5):
    for optimize in [True, False]:
        for progressive in [True, False]:
            image.save(f"./tmp/progressive_encoding_quality{quality}_optimize{optimize}_progressive{progressive}.jpg", "JPEG", quality=quality, optimize=optimize, progressive=progressive)