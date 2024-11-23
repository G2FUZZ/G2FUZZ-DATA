import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple animation of a circle moving across a canvas
frame_count = 10
frames = []
width, height = 200, 200

for i in range(frame_count):
    # Create a new frame with white background
    frame = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(frame)
    
    # Draw a circle that moves across the frame
    # The circle's center moves from 20, 100 to 180, 100
    circle_x = 20 + i * (160 / (frame_count - 1))
    draw.ellipse([circle_x - 10, 90, circle_x + 10, 110], fill='blue')
    
    frames.append(frame)

# Save the frames as an animated GIF
frames[0].save('./tmp/animated_circle.gif',
               save_all=True, append_images=frames[1:],
               optimize=False, duration=100, loop=0)