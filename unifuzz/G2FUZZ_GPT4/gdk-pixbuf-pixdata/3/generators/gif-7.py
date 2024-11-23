from PIL import Image, GifImagePlugin

# Define the colors for the global color table
colors = [(255, 0, 0),   # Red
          (0, 255, 0),   # Green
          (0, 0, 255),   # Blue
          (255, 255, 0)] # Yellow

# Create a list to hold the frames
frames = []

# Generate frames with solid colors
for color in colors:
    frame = Image.new('RGB', (100, 100), color)
    frames.append(frame)

# Ensure the output directory exists
import os
os.makedirs('./tmp/', exist_ok=True)

# Save the frames as a GIF with a global color table
frames[0].save('./tmp/colored_images.gif',
               save_all=True,
               append_images=frames[1:],
               loop=0,
               palette=sum(colors, ()))  # Flatten the color table for PIL