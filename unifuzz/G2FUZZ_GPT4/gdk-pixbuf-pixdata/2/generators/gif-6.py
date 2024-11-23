from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a list to hold the frames
frames = []

# Define the size of the image
size = (100, 100)

# Create 10 frames
for i in range(10):
    # Create a new frame with white background
    frame = Image.new('RGB', size, (255, 255, 255))
    draw = ImageDraw.Draw(frame)
    
    # Draw a circle that moves across the frame
    draw.ellipse((10 + i * 8, 25, 10 + i * 8 + 50, 75), fill=(255, 0, 0))
    
    # Add the frame to the list
    frames.append(frame)

# Save the frames as an animated GIF
# Loop=0 for infinite looping, loop=1 for looping once, etc.
frames[0].save('./tmp/animated_loop.gif', format='GIF',
               append_images=frames[1:], save_all=True, duration=100, loop=0)