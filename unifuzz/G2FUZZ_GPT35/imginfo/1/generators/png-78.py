from PIL import Image, ImageDraw, ImageFont

# Create a new RGBA image with multiple layers
base = Image.new('RGBA', (200, 200), (255, 255, 255, 255))  # White background
layer1 = Image.new('RGBA', (200, 200), (0, 0, 255, 128))  # Blue with 50% transparency
layer2 = Image.new('RGBA', (200, 200), (0, 255, 0, 128))  # Green with 50% transparency

# Paste the layers onto the base image
base.paste(layer1, (0, 0), mask=layer1)
base.paste(layer2, (50, 50), mask=layer2)

# Add text annotation
draw = ImageDraw.Draw(base)
font = ImageFont.load_default()  # Using default system font
draw.text((10, 10), "Complex PNG File", fill="black", font=font)

# Save the image to a file
base.save('./tmp/complex_image.png')