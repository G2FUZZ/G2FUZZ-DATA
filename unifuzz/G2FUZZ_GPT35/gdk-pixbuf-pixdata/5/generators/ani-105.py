import os

# Create a directory to store the generated 'ani' files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample 'ani' file with complex file structures
ani_file_content = """
ANIMATION FILE
Version: 2.0
Transparency: True
Frames: 60
Resolution: 3840x2160
FrameRate: 60
Metadata:
    Author: John Doe
    Description: A sample animation with multiple layers
Layers:
    - Name: Background
      Type: Image
      Source: background.png
    - Name: Character
      Type: Sprite
      Source: character.png
      Position: (100, 200)
      Scale: (1.5, 1.5)
    - Name: Text
      Type: Text
      Content: Hello, World!
      Font: Arial
      Size: 24
"""

# Save the generated 'ani' file to ./tmp/sample_extended.ani
with open('./tmp/sample_extended.ani', 'w') as f:
    f.write(ani_file_content)

print("Generated 'ani' file with complex file structures saved in ./tmp/sample_extended.ani")