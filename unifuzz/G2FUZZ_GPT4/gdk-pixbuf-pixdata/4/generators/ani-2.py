import os
from PIL import Image
import struct

# Directory to save the .ani file
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to create a frame
def create_frame(color, size=(32, 32)):
    img = Image.new('RGBA', size, color)
    return img

# Frames and their display durations (in jiffies, 1/60th of a second)
frames = [
    (create_frame('red'), 10),  # Display for 1/6th of a second
    (create_frame('green'), 20), # Display for 1/3rd of a second
    (create_frame('blue'), 30),  # Display for half a second
]

# Create an ANI file
ani_path = os.path.join(output_dir, 'animation.ani')

# ANI header structure: RIFF, list, anih (header), and frame data
ani_header = struct.pack('4sI4s4sI36s', b'RIFF', 0, b'ACON', b'LIST', 0, (36).to_bytes(36, byteorder='little'))

# Calculate the total size of the ANI file
total_size = len(ani_header) + sum(len(frame[0].tobytes()) + 8 for frame in frames)  # +8 for each frame's header

# Write the ANI file
with open(ani_path, 'wb') as ani_file:
    # Write the header with the updated total size
    ani_file.write(ani_header[:4] + (total_size - 8).to_bytes(4, byteorder='little') + ani_header[8:16] + (total_size - 24).to_bytes(4, byteorder='little') + ani_header[20:])
    
    # Write each frame
    for frame, duration in frames:
        frame_data = frame.tobytes()
        frame_header = struct.pack('4sI', b'icon', len(frame_data) + 4)  # +4 for the duration field
        ani_file.write(frame_header + duration.to_bytes(4, byteorder='little') + frame_data)

print(f"ANI file saved to {ani_path}")