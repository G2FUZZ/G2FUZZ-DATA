from PIL import Image, ImageDraw, ImageFont

# Create a new image with size 256x256
image = Image.new('RGBA', (256, 256), (255, 255, 255, 0))

# Add text to the image using a built-in font
font = ImageFont.load_default()  # Using a built-in font

draw = ImageDraw.Draw(image)
draw.text((10, 10), "Scalability", fill="black", font=font)

# Save the image as an ICO file
image.save("./tmp/scalability_icon.ico")