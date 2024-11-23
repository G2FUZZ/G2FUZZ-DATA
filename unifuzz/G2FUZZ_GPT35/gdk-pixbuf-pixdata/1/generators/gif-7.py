from PIL import Image, ImageDraw

# Create a new Image object
image = Image.new('RGB', (100, 100), color = 'white')

# Draw a circle on the image
draw = ImageDraw.Draw(image)
draw.ellipse((25, 25, 75, 75), fill='red')

# Save the image as a GIF file
image.save('./tmp/looping.gif', save_all=True, append_images=[image], loop=0)