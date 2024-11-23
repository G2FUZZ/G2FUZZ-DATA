from PIL import Image, ImageDraw, ImageFont

# Create a new image (200x200 pixels) with RGB color
img = Image.new('RGB', (200, 200), color='blue')

# Add text to the image
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()
draw.text((50, 50), "Hello, World!", fill='white', font=font)

# Save the image in progressive JPEG format with additional complex features
img.save('./tmp/progressive_complex_image.jpg', 'JPEG', quality=95, optimize=True, progressive=True)