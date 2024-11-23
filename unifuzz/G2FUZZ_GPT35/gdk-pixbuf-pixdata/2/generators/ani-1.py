import os

# Create a directory if it does not exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Number of frames for the animation
num_frames = 10

# Generate animation frames and save them in 'ani' files
for i in range(num_frames):
    frame_content = f"This is frame {i+1} of the animation."
    file_name = f"./tmp/frame_{i+1}.ani"
    with open(file_name, 'w') as file:
        file.write(frame_content)

print(f"Generated {num_frames} 'ani' files in './tmp/' directory.")