from PIL import Image, ImageDraw, ImageFont

# Create a new image with white background
width, height = 600, 100
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Load a built-in font and write the text
font = ImageFont.load_default()
text = "Wide platform support: PNG files are widely supported across different operating systems and applications, making them a versatile choice for image storage."
draw.text((10, 10), text, font=font, fill='black')

# Save the image as a PNG file
image.save("./tmp/wide_platform_support.png")