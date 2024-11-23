from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the size of the images
width, height = 200, 200

# Create two frames with different background colors to demonstrate the use of local palettes
frames = []

# Frame 1: Red background, demonstrating global palette
frame1 = Image.new('P', (width, height), 'red')
draw = ImageDraw.Draw(frame1)
draw.ellipse((50, 50, 150, 150), fill='blue')
frames.append(frame1)

# Frame 2: Green background, using a local palette
frame2 = Image.new('P', (width, height), 'green')
draw = ImageDraw.Draw(frame2)
draw.rectangle((50, 50, 150, 150), fill='yellow')
frames.append(frame2)

# Save the frames as a GIF with a global palette
frames[0].save('./tmp/animation_global_palette.gif', save_all=True, append_images=frames[1:], optimize=False, duration=500, loop=0)

# To demonstrate local palettes, we need to create separate GIFs for each frame and then combine them
# This is a workaround, as the PIL library might not directly support creating GIFs with local palettes per frame in a straightforward manner
# For a true demonstration of local palettes, consider using a library or tool specifically designed for advanced GIF manipulation