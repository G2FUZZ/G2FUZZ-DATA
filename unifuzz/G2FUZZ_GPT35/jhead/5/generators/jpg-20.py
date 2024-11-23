from PIL import Image, ImageDraw, ImageFont

# Create an image with text
image_with_text = Image.new('RGB', (200, 200), color='white')
draw = ImageDraw.Draw(image_with_text)
font = ImageFont.load_default()  # Use a built-in font
draw.text((50, 50), "Hello, World!", fill='black', font=font)
image_with_text.save('./tmp/image_with_text.jpg')