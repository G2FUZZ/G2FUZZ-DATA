from PIL import Image, ImageDraw

# Create a directory to store the output if it doesn't exist
import os
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a new image with RGBA (Red, Green, Blue, Alpha) mode for transparency
# 200x200 pixels, with a transparent background (0, 0, 0, 0)
image = Image.new('RGBA', (200, 200), (0, 0, 0, 0))

# Initialize ImageDraw to draw on the image
draw = ImageDraw.Draw(image)

# Draw a rectangle with transparency
# The first argument is the coordinates (top left x, top left y, bottom right x, bottom right y)
# The second argument is the fill color, including alpha for transparency (R, G, B, A)
# Here, we draw a red rectangle that is half-transparent
draw.rectangle([50, 50, 150, 150], fill=(255, 0, 0, 128))

# Convert the image to 'P' mode for GIF saving with transparency
image = image.convert('P', palette=Image.ADAPTIVE, colors=255)

# Save the transparent image
transparent_color = 0
image.info['transparency'] = transparent_color
image.save(f'{output_dir}transparent_gif.gif')

print("GIF with transparency created.")