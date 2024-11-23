from PIL import Image, ImageDraw

# Create a black image with white text
image = Image.new('RGB', (100, 50), color='black')
text = "Lossless Rotation"
draw = ImageDraw.Draw(image)
draw.text((10, 10), text, fill='white')

# Save the image
image.save('./tmp/lossless_rotation.jpg')