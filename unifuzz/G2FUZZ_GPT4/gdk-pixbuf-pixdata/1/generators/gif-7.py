from PIL import Image, ImageDraw

# Create a directory for the output if it doesn't exist
import os
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create frames
frames = []
for i in range(5):
    # Each frame is a simple square with different positions
    frame = Image.new('P', (100, 100), color=0)
    d = ImageDraw.Draw(frame)
    
    # Use global colors for all frames except the third one
    if i == 2:
        # Define a local color table for this frame by adding colors
        frame.putpalette([
            0, 0, 0,  # Black background
            255, 0, 0,  # Red square (local color)
        ])
        d.rectangle([10 * i, 10 * i, 90 - 10 * i, 90 - 10 * i], fill=1)
    else:
        # Global color table: black, green
        frame.putpalette([
            0, 0, 0,  # Black background
            0, 255, 0,  # Green square
        ])
        d.rectangle([10 * i, 10 * i, 90 - 10 * i, 90 - 10 * i], fill=1)
    
    frames.append(frame)

# Save frames as an animated GIF
frames[0].save(os.path.join(output_dir, 'global_vs_local_color_table.gif'),
               save_all=True, append_images=frames[1:], optimize=False, duration=200, loop=0)