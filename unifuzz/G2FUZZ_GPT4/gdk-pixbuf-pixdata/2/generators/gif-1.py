from PIL import Image, ImageDraw

# Create a directory for the output if it doesn't already exist
import os
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Parameters for the animation
width, height = 200, 200  # Size of each frame
num_frames = 10  # Number of frames in the animation

# Create each frame and add it to the frames list
frames = []
for i in range(num_frames):
    # Create a new image with white background
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    
    # Change the color of the rectangle based on the frame
    color = (i * 25, 0, 255 - i * 25)  # Vary the color from blue to red
    draw.rectangle([50, 50, 150, 150], fill=color)
    
    frames.append(img)

# Save frames as an animated GIF
output_path = os.path.join(output_dir, 'animated_rectangle.gif')
frames[0].save(output_path, save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)

print(f"Animated GIF saved at: {output_path}")