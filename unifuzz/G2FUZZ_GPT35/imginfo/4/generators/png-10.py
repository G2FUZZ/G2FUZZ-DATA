from PIL import Image, ImageDraw, ImageFont

# Create a new image with white background
image = Image.new('RGB', (400, 100), 'white')
draw = ImageDraw.Draw(image)

# Set font style
font = ImageFont.load_default()

# Write text on the image
text = "Open standard: PNG is an open standard file format, widely supported by image editing software and web browsers."
draw.text((10, 10), text, font=font, fill='black')

# Save the image
image.save('./tmp/open_standard_png.png')