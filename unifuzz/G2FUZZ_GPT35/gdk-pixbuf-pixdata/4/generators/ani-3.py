import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate the 'ani' file with hotspot feature
ani_content = """
ANIFILE
FRAMES 10
HOTSPOT 5 5
DATA
# Binary data for frames
"""

ani_filename = './tmp/sample.ani'

with open(ani_filename, 'w') as f:
    f.write(ani_content)

print(f"'ani' file with hotspot feature generated and saved as {ani_filename}")