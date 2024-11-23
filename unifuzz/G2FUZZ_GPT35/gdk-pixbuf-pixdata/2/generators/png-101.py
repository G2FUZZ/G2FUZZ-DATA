from PIL import Image, ImageDraw

# Create a new RGBA image with transparency
img = Image.new('RGBA', (200, 200), color='white')

# Draw shapes on different layers
draw = ImageDraw.Draw(img)

# Draw a red rectangle on the first layer
draw.rectangle([25, 25, 175, 175], fill='red')

# Draw a green circle on the second layer
draw.ellipse([50, 50, 150, 150], fill='green')

# Save the image with multiple layers and transparency
img.save('./tmp/complex_image.png')