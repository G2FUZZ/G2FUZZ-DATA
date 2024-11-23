import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample 'ani' file with transparency support
ani_content = """
Animation File Format: ANI
Transparency Support: True
Frame Rate: 30 fps
Resolution: 1920x1080
Frames: 60
Background Color: #FFFFFF
Transparency Color: #00FF00

# Animation frames follow here...
"""

# Save the generated 'ani' file
with open('./tmp/sample.ani', 'w') as file:
    file.write(ani_content)

print("Generated 'ani' file successfully.")