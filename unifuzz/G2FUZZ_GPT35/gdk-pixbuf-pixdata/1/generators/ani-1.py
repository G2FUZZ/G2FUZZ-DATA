import os

# Create a directory to store the ani files
os.makedirs('./tmp/', exist_ok=True)

# Define the animation frames
frames = [
    "Frame 1: Character walking",
    "Frame 2: Character jumping",
    "Frame 3: Character running",
    "Frame 4: Character standing"
]

# Generate ani files with animation frames
for i, frame in enumerate(frames):
    file_path = f'./tmp/ani_{i + 1}.ani'
    with open(file_path, 'w') as file:
        file.write(frame)