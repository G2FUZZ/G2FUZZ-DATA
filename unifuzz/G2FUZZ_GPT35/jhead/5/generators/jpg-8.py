from PIL import Image

# Create a sample image
image = Image.new('RGB', (300, 200), color='red')
image.save('./tmp/sample.jpg')

# Lossless rotation of the image
original_image = Image.open('./tmp/sample.jpg')
rotated_image = original_image.transpose(Image.ROTATE_90)
rotated_image.save('./tmp/rotated_sample.jpg')