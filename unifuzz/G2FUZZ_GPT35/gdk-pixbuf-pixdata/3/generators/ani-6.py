import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample 'ani' file with audio feature
ani_filename = './tmp/sample.ani'
with open(ani_filename, 'w') as file:
    file.write("Features: Audio - 'ani' files can include sound or audio components synchronized with the animation.")

print(f"Generated 'ani' file with audio feature: {ani_filename}")