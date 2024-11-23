import os

# Create a directory to store the generated 'ani' files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample 'ani' file with transparency support
ani_file_content = """
ANIMATION FILE
Version: 1.0
Transparency: True
Frames: 30
Resolution: 1920x1080
FrameRate: 30
<Animation data here>
"""

# Save the generated 'ani' file to ./tmp/sample.ani
with open('./tmp/sample.ani', 'w') as f:
    f.write(ani_file_content)

print("Generated 'ani' file with transparency support saved in ./tmp/sample.ani")