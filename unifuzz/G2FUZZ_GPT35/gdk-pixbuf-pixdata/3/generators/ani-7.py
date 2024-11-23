import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate 'ani' files with the specified features
ani_content = "Features: \n1. Interactive elements within the animation \n2. Other features..."
ani_file_path = './tmp/ani_file.ani'

with open(ani_file_path, 'w') as file:
    file.write(ani_content)

print(f"Generated 'ani' file with features: {ani_file_path}")