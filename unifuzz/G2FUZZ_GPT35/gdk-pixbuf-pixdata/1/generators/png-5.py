from PIL import Image

# Create a new RGB image
image = Image.new('RGB', (100, 100))

# Draw a diagonal line
for i in range(100):
    image.putpixel((i, i), (255, 255, 255))

# Save the image in a progressive manner
image.save('./tmp/progressive_rendering.png', 'PNG', optimize=True, progressive=True)

print("Progressive rendering PNG file saved successfully!")