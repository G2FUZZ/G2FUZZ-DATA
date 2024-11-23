from PIL import Image, ImageDraw, ImageFont

# Create a new PNG image
image = Image.new('RGB', (400, 200), color='white')

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Specify the font style and size using a built-in font
font = ImageFont.load_default()

# Add text to the image
text = "PNG files can store textual information such as image descriptions or keywords."
draw.text((20, 50), text, fill='black', font=font)

# Save the image to a file
image.save('./tmp/text_support.png')