from PIL import Image

# Create a new RGB image
image = Image.new('RGB', (100, 100))

# Save the image as a jpg file
image.save('./tmp/rgb_image.jpg')

print('RGB image created and saved successfully!')