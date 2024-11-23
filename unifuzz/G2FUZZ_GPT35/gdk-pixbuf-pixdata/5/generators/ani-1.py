import os

# Create a directory to save the ani files
os.makedirs('./tmp/', exist_ok=True)

# Generate animation data for ani files
animation_data = {
    'keyframes': [1, 2, 3, 4, 5],
    'motion_paths': ['path1', 'path2', 'path3'],
    'timing_info': {
        'duration': 10,
        'fps': 30
    }
}

# Generate ani files with animation data
for i in range(3):
    file_name = f'./tmp/ani_file_{i + 1}.ani'
    with open(file_name, 'w') as file:
        file.write(f'Animation Data {i + 1}: {animation_data}')