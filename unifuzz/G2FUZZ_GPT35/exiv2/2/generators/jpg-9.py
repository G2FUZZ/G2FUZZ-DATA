from PIL import Image, ImageDraw

# Create a new image with a white background
image = Image.new('RGB', (400, 400), color='white')

# Draw a red square on the image
draw = ImageDraw.Draw(image)
draw.rectangle([100, 100, 300, 300], fill='red')

# Save the original image
image.save('./tmp/original.jpg')

# Rotate the image by 90 degrees
rotated_image = image.transpose(Image.ROTATE_90)
rotated_image.save('./tmp/rotated.jpg')