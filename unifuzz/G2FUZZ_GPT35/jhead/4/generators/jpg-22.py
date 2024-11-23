from PIL import Image, ImageDraw, ImageFont

# Create a new image with RGB mode
img = Image.new('RGB', (200, 200), color='white')

# Draw text on the image
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()
draw.text((50, 50), "Hello, World!", fill="black", font=font)

img.save('./tmp/complex_image.jpg')