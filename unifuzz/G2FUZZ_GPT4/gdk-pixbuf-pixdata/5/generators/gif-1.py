from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected argument name here

# Parameters for the animation
frame_count = 10  # Number of frames in the animation
width, height = 200, 200  # Width and height of the images
circle_radius = 20  # Radius of the circle to be animated
circle_color = 'blue'  # Color of the circle

frames = []  # List to hold the generated frames

for i in range(frame_count):
    # Create a new image with white background
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    
    # Determine the position of the circle in this frame
    position = (width // frame_count * i + circle_radius, height // 2)
    
    # Draw the circle
    draw.ellipse([position[0] - circle_radius, position[1] - circle_radius,
                  position[0] + circle_radius, position[1] + circle_radius], fill=circle_color)
    
    frames.append(img)

# Save the frames as an animated GIF
frames[0].save('./tmp/animated_circle.gif',
               save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)