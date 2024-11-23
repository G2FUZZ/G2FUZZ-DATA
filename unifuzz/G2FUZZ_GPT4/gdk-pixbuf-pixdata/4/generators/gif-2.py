from PIL import Image, ImageDraw
import os

# Create the directory for storing output if it doesn't exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Parameters for the GIF
width, height = 200, 200  # Size of each frame
num_frames = 10  # Number of frames in the GIF
circle_radius = 30  # Radius of the circle to be animated
loop_count = 0  # 0 means infinite loop

# Create frames
frames = []
for i in range(num_frames):
    frame = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(frame)
    
    # Calculate the circle's position to make it move
    position = (width // 2 + int(circle_radius * (i / num_frames * 2) * (1 if i < num_frames / 2 else -1)),
                height // 2)
    
    # Draw a circle
    draw.ellipse((position[0] - circle_radius, position[1] - circle_radius,
                  position[0] + circle_radius, position[1] + circle_radius), fill='blue')
    
    frames.append(frame)

# Save frames as an animated GIF
output_path = os.path.join(output_dir, 'animated_circle.gif')
frames[0].save(output_path, save_all=True, append_images=frames[1:], optimize=False, duration=200, loop=loop_count)

print(f'GIF saved to {output_path}')