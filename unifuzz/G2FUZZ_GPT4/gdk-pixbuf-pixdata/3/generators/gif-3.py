from PIL import Image, ImageDraw

# Create a directory for saving the gif if it doesn't exist
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Function to create frames
def create_frame(position, size):
    # Create an image with transparent background
    image = Image.new("RGBA", size, (255, 255, 255, 0))
    # Create a drawing object
    draw = ImageDraw.Draw(image)
    # Draw a blue circle
    draw.ellipse((position, position, position + 30, position + 30), fill=(0, 0, 255, 255))
    return image

# Frame size
size = (100, 100)
# Generate frames
frames = [create_frame(x, size) for x in range(0, 70, 10)]

# Convert frames to a format that supports transparency in GIFs
frames = [frame.convert('P', palette=Image.ADAPTIVE, colors=255) for frame in frames]

# Save frames as a GIF
frames[0].save('./tmp/animated_transparent.gif',
               save_all=True,
               append_images=frames[1:],
               optimize=False,
               duration=100,
               loop=0,
               transparency=0,
               disposal=2)