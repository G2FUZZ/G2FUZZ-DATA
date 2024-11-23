import os

# Define the content of the 'ani' file
ani_content = """
Features:
1. Resolution: 1920x1080
2. Frame rate: 30 fps
3. Color depth: True color (24 bit)
4. Compression: H.264
5. Audio: AAC, 48 kHz
6. Scripting capabilities: 'ani' files may support scripting languages for advanced animation control.
"""

# Create a directory to store the 'ani' files
os.makedirs('./tmp/', exist_ok=True)

# Write the content to a new 'ani' file
with open('./tmp/animation.ani', 'w') as f:
    f.write(ani_content)

print("Generated 'ani' file saved in ./tmp/ directory.")