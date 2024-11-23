from PIL import Image, ImageDraw, ImageFont

# Create a new RGB image
image_with_text = Image.new('RGB', (200, 200), color='white')
draw = ImageDraw.Draw(image_with_text)

# Add text to the image using a default font
font = ImageFont.load_default()
text = "Hello, World!"
draw.text((50, 50), text, fill='black', font=font)

# Save the image with text as a JPEG file
image_with_text.save('./tmp/image_with_text.jpg', format='JPEG', subsampling=0, quality=95, thumbnail=Image.new('RGB', (32, 32), color='white'))