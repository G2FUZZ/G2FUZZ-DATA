from PIL import Image, ImageDraw

# Create a new image with white background
image = Image.new('RGB', (100, 100), color='white')
draw = ImageDraw.Draw(image)

# Draw a red circle
draw.ellipse((25, 25, 75, 75), fill='red')

# Save the image as a gif file with lossless compression
image.save('./tmp/compressed_image.gif', 'GIF', optimize=True)