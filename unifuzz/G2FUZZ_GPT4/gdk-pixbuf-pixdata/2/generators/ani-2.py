import os
import struct

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the path for the .ani file
file_path = './tmp/custom_animation.ani'

# ANI Header specific constants
header = 'RIFF'
list_type = 'ACON'
anih_header = 'anih'
anih_size = 36  # Size of the ANIH structure
frames = 2  # Number of frames in the animation
steps = 2  # Number of steps in the animation (usually the same as frames)
jif_rate = 10  # Jiffies (1/60th of a second); customize for speed
width = 32  # Width of the cursor
height = 32  # Height of the cursor
bit_count = 0  # Color depth, 0 for multiple icons based on display capability
planes = 1  # Number of image planes

# Creating a minimal ANI file with customizable animation speed
with open(file_path, 'wb') as ani_file:
    # Write the RIFF header
    ani_file.write(struct.pack('<4sI4s', header.encode(), 0, list_type.encode()))
    
    # Write the ANIH chunk
    ani_file.write(struct.pack('<4sI', anih_header.encode(), anih_size))
    ani_file.write(struct.pack('<IIIIIIII', anih_size, frames, steps, 0, jif_rate, 0, width, height))
    ani_file.write(struct.pack('<II', bit_count, planes))
    
    # Placeholder for the frame data, since creating actual image data is complex and requires additional files
    # Instead, we'll add a simple note in the file indicating where frame data would go
    frame_note = 'This is a placeholder for frame data.'
    ani_file.write(frame_note.encode())

    # Update the file size in the RIFF header (we need to go back to the start)
    ani_file.seek(4)
    ani_file.write(struct.pack('<I', os.path.getsize(file_path) - 8))

print(f'Custom animation .ani file created at: {file_path}')