from PIL import Image, ImageDraw
import os

# Function to create a frame with a specific background color
def create_frame(size, color):
    frame = Image.new("RGBA", size, color)
    return frame

# Ensure the ./tmp/ directory exists
os.makedirs("./tmp/", exist_ok=True)

# Define the size of the image and the colors for the global color table
image_size = (200, 200)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# Create a list to hold the frames
frames = []

# Generate frames using the global color table
for color in colors:
    frame = create_frame(image_size, color)
    frames.append(frame)

# Save the frames as a GIF using a global color table
frames[0].save('./tmp/animated_global_color_table.gif',
               save_all=True,
               append_images=frames[1:],
               optimize=False,
               duration=500, loop=0)