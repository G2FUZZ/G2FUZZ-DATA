from PIL import Image, ImageDraw, ImageFont

# Create a new image with RGBA mode and a transparent background
image = Image.new('RGBA', (200, 200), (255, 255, 255, 0))

# Draw a red rectangle on the image
draw = ImageDraw.Draw(image)
draw.rectangle([50, 50, 150, 150], fill='red')

# Add text annotation to the image using default font
font = ImageFont.load_default()
draw.text((60, 80), "Complex PNG", fill='black', font=font)

# Save the image with a more complex file structure
image.save('./tmp/complex_image.png', compress_level=9, optimize=True)