import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a .mp4 file with embedded images
file_path = './tmp/generated_file_with_images.mp4'
with open(file_path, 'w') as file:
    file.write('This is a generated .mp4 file with Embedded Images.')

print(f'Generated .mp4 file with Embedded Images: {file_path}')