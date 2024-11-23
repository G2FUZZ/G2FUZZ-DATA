from PIL import Image, ImageFilter

# Create a new RGB image
img = Image.new('RGB', (100, 100))

# Set pixel data for the image
pixels = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i, j] = (255, 255, 255)  # Set all pixels to white

# Apply compression artifacts by blurring the image
blurred_img = img.filter(ImageFilter.BLUR)

# Save the blurred image with progressive encoding
blurred_img.save('./tmp/progressive_encoding_with_artifacts.jpg', format='JPEG', quality=85, optimize=True, progressive=True)