from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected argument name here

# Parameters for the animation
width, height = 200, 200  # Size of the canvas
circle_radius = 20  # Radius of the circle
num_frames = 30  # Number of frames in the animation

# Create each frame
frames = []
for i in range(num_frames):
    # Create a new image with white background
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)

    # Calculate the circle's position
    x = int((width - circle_radius * 2) * (i / (num_frames - 1))) + circle_radius
    
    # Draw the circle
    draw.ellipse((x - circle_radius, height // 2 - circle_radius, x + circle_radius, height // 2 + circle_radius), fill='blue')

    # Add the frame to the list
    frames.append(img)

# Save the frames as an animated GIF
frames[0].save('./tmp/animated_circle.gif', save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)