import os
from PIL import Image, ImageDraw

# Create the tmp directory if it doesn't exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Parameters for the GIF
width, height = 200, 200  # Size of each frame
num_frames = 10  # Number of frames in the GIF
background_color = 'white'
circle_color = 'blue'
circle_radius = 30
delay = 100  # Delay time in milliseconds (1000 milliseconds = 1 second)

# Create each frame
frames = []
for i in range(num_frames):
    # Create a new image with white background
    img = Image.new('RGB', (width, height), color=background_color)
    
    # Create a drawing context
    draw = ImageDraw.Draw(img)
    
    # Calculate the circle's position to make it move
    circle_x = int((width / num_frames) * i + circle_radius)
    circle_y = height // 2
    
    # Draw a circle
    draw.ellipse([circle_x - circle_radius, circle_y - circle_radius, circle_x + circle_radius, circle_y + circle_radius], fill=circle_color)
    
    # Append the frame to the list of frames
    frames.append(img)

# Save the frames as a GIF
frames[0].save(os.path.join(output_dir, 'animated_circle.gif'),
               save_all=True, append_images=frames[1:], optimize=False, duration=delay, loop=0)