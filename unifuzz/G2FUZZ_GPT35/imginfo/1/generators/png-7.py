from PIL import Image, ImageDraw, ImageFont

# Create a new PNG image
image = Image.new('RGB', (400, 200), color='white')
draw = ImageDraw.Draw(image)

# Define text content and font
text = "PNG files can store text annotations or descriptions within the file."
font = ImageFont.load_default()

# Add text to the image
draw.text((10, 10), text, fill='black', font=font)

# Save the image
image.save('./tmp/text_annotation.png')