import json
import os

# Create a dictionary representing the 'ani' file content
ani_content = {
    "looping_options": "continuous"
}

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save the 'ani' file with the generated content
file_path = './tmp/animation.ani'
with open(file_path, 'w') as file:
    json.dump(ani_content, file)

print(f"'ani' file successfully generated and saved at: {file_path}")