import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata file with animation data
animation_data = {
    'Frames': 30,
    'Timing': '60fps'
}

file_path = './tmp/pixdata_animation.txt'
with open(file_path, 'w') as file:
    file.write('Animation data:\n')
    file.write(f'Frames: {animation_data["Frames"]}\n')
    file.write(f'Timing: {animation_data["Timing"]}\n')

print(f'Generated pixdata file with animation data: {file_path}')