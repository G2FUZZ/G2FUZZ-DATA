from PIL import Image, ImageDraw, ImageFont

# Create a new image with RGB mode
img = Image.new('RGB', (200, 200), color='white')

# Draw text on the image
draw = ImageDraw.Draw(img)
text = "Hello, World!"
font = ImageFont.load_default()  # Use a system default font
draw.text((50, 50), text, fill='black', font=font)

img.save('./tmp/complex_image.jpg')