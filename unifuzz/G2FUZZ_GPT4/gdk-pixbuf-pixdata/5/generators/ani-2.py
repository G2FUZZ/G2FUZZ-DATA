from PIL import Image, ImageDraw
import os

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Define animation parameters
frame_count = 10  # Number of frames in the animation
width, height = 64, 64  # Width and height of the images

# Generate frame images
frames = []
for i in range(frame_count):
    # Create a new image with white background
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    
    # Draw a moving circle
    # The circle's position changes with each frame
    left_up_point = (i * 5, 10)
    right_down_point = (i * 5 + 20, 30)
    draw.ellipse([left_up_point, right_down_point], fill='blue', outline='blue')
    
    # Add the frame to the list
    frames.append(img)

# Save the frames as an animated GIF
gif_path = './tmp/animated.gif'
frames[0].save(gif_path, save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)

print(f"Generated animated GIF saved at {gif_path}")