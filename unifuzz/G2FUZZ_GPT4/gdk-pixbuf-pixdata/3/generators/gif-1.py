from PIL import Image, ImageDraw
import os

# Create the tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Parameters for the animation
width, height = 200, 200  # Size of the frame
circle_radius = 20
num_frames = 30  # Number of frames in the animation

# Generate frames
frames = []
for i in range(num_frames):
    frame = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(frame)
    # Calculate the circle's position
    x = int((width - circle_radius * 2) * i / num_frames) + circle_radius
    y = height // 2
    draw.ellipse([x - circle_radius, y - circle_radius, x + circle_radius, y + circle_radius], fill='blue')
    frames.append(frame)

# Save frames as an animated GIF
frames[0].save('./tmp/moving_circle.gif',
               save_all=True,
               append_images=frames[1:],
               optimize=False,
               duration=40,  # Frame duration in ms
               loop=0)  # Loop forever