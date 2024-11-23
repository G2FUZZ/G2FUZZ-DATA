import os
import json

# Create a directory to save the ani files
os.makedirs('./tmp/', exist_ok=True)

# Generate animation data for ani files with more complex features
animation_data = {
    'keyframes': [1, 2, 3, 4, 5],
    'motion_paths': ['path1', 'path2', 'path3'],
    'timing_info': {
        'duration': 10,
        'fps': 30
    },
    'additional_info': {
        'nested_dict': {
            'key1': 'value1',
            'key2': 'value2'
        },
        'nested_list': [1, 2, 3, 4, 5]
    }
}

# Generate ani files with animation data and additional complex features
for i in range(3):
    file_name = f'./tmp/ani_file_{i + 1}.ani'
    with open(file_name, 'w') as file:
        json.dump(animation_data, file, indent=4)