from PIL import Image, ImageDraw, ImageFont

# Create a new image with white background
image = Image.new('RGB', (600, 400), 'white')
draw = ImageDraw.Draw(image)

# Set font style
font = ImageFont.load_default()

# Write text on the image
text1 = "Open standard: PNG is an open standard file format,"
text2 = "widely supported by image editing software and web browsers."
draw.text((10, 10), text1, font=font, fill='black')
draw.text((10, 30), text2, font=font, fill='black')

# Add a rectangle shape
draw.rectangle([(50, 50), (200, 150)], outline='black', width=2)

# Add a circle shape
draw.ellipse((250, 50, 400, 150), outline='black', width=2)

# Save the image
image.save('./tmp/complex_structure.png')