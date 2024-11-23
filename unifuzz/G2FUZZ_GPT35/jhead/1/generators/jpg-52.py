from PIL import Image, ImageDraw

# Create a new RGBA image with transparency and multiple layers
img = Image.new('RGBA', (200, 200), color='white')
draw = ImageDraw.Draw(img)

# Draw a rectangle with a semi-transparent red fill color on the first layer
draw.rectangle([(20, 20), (80, 80)], fill=(255, 0, 0, 128))

# Draw a circle with a semi-transparent blue fill color on the second layer
draw.ellipse([(100, 100), (160, 160)], fill=(0, 0, 255, 128))

# Convert the image to RGB mode before saving as JPEG
rgb_img = img.convert('RGB')

# Save the image with complex file structures
rgb_img.save('./tmp/complex_file_structure.jpg', quality=95)