from PIL import Image

# Create a new image with a white background
img = Image.new('RGB', (100, 100), color='white')

# Apply gamma correction to the image
gamma = 2.2
img_with_gamma = img.point(lambda p: int(p / 255 ** (1/gamma)))

# Save the image with gamma correction applied
img_with_gamma.save('./tmp/gamma_corrected_image.png')