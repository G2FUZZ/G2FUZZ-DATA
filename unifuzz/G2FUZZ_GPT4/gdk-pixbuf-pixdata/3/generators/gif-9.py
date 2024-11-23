from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create frames for the GIF
frames = []
for i in range(10):
    # Create a new frame with a black background
    frame = Image.new('RGB', (100, 100), 'black')
    draw = ImageDraw.Draw(frame)
    
    # Draw a moving square
    left_upper = (10 + 3*i, 10 + 3*i)
    right_lower = (30 + 3*i, 30 + 3*i)
    draw.rectangle([left_upper, right_lower], fill='red')
    
    frames.append(frame)

# Save the frames as a GIF
frames[0].save('./tmp/moving_square.gif',
               save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)