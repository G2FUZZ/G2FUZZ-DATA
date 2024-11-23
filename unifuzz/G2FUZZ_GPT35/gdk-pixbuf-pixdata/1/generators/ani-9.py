import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate 'ani' file with audio support
ani_file_path = './tmp/animation_with_audio.ani'

with open(ani_file_path, 'w') as ani_file:
    ani_file.write("Animation content\n")
    ani_file.write("Audio track synchronized with animation\n")

print(f"'ani' file with audio support generated at: {ani_file_path}")