from PIL import Image, ImageDraw, ImageFont

# Create an image with text
text_image = Image.new('RGB', (200, 200), color='white')
draw = ImageDraw.Draw(text_image)
font = ImageFont.load_default()
draw.text((50, 50), "Generated Image", fill='black', font=font)
text_image.save('./tmp/text_image.jpg')