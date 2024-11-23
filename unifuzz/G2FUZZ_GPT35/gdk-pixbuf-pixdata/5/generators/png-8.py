from PIL import Image, ImageDraw, ImageFont

# Create a blank image with white background
width, height = 400, 200
image = Image.new('RGB', (width, height), 'white')

# Draw text on the image
draw = ImageDraw.Draw(image)
text = "PNG files support text annotations and descriptions"
font = ImageFont.load_default()
draw.text((10, 10), text, fill='black', font=font)

# Save the image
image.save('./tmp/text_support.png')