import os

# Create a directory to store 'ani' files
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate animation frames and save them to 'ani' files
num_frames = 5
for i in range(num_frames):
    frame_data = f"Frame {i+1} data"
    file_name = f"animation_frame_{i+1}.ani"
    with open(os.path.join(output_dir, file_name), 'w') as f:
        f.write(frame_data)