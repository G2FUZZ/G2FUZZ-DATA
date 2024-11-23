from PIL import Image, ImageDraw, ImageFont

# Create a blank image in RGB mode with size 200x200
extended_image = Image.new('RGB', (200, 200), color='white')

# Add text to the image
draw = ImageDraw.Draw(extended_image)
text = "Generated Image"

# Load the default font
font = ImageFont.load_default()
draw.text((10, 10), text, fill='black', font=font)

# Save the image with additional text
extended_image.save('./tmp/extended.jpg', format='JPEG', quality=95, optimize=True, progressive=True)