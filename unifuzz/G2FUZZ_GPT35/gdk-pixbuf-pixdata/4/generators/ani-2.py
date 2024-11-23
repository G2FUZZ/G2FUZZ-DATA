import os

# Create a directory to save the ani files
os.makedirs('./tmp/', exist_ok=True)

# Define the animation frames for the ani files
animation_frames = [
    ['frame1.jpg', 'frame2.jpg', 'frame3.jpg'],
    ['frame4.jpg', 'frame5.jpg'],
    ['frame6.jpg', 'frame7.jpg', 'frame8.jpg', 'frame9.jpg']
]

# Generate ani files with animation frames
for i, frames in enumerate(animation_frames):
    ani_filename = f'./tmp/animation_{i}.ani'
    with open(ani_filename, 'w') as f:
        for frame in frames:
            f.write(frame + '\n')

print('Ani files have been generated and saved in ./tmp/ directory.')