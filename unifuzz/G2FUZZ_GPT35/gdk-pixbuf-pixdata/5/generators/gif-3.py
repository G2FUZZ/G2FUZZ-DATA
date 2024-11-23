from PIL import Image, ImageDraw

# Create a new image
image = Image.new('RGB', (100, 100), color = 'white')

# Draw a red rectangle on the image
draw = ImageDraw.Draw(image)
draw.rectangle([25, 25, 75, 75], fill='red')

# Save the image as a GIF file with lossless compression
image.save('./tmp/lossless_compression.gif', format='GIF')

print("GIF file with lossless compression saved successfully.")