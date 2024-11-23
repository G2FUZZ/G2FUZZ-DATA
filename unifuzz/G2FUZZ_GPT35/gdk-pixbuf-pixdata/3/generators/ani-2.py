import os

# Define the content of the 'ani' file with transparency feature
ani_content = """
ANIMATION FILE

FEATURES:
- Transparency: Supported

FRAMES:
- Frame 1
- Frame 2
- Frame 3
"""

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Save the generated 'ani' file
with open('./tmp/ani_file.ani', 'w') as file:
    file.write(ani_content)

print("Generated 'ani' file with transparency feature saved in './tmp/' directory.")