import os

# Create a directory to store the generated 'ani' files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample 'ani' file with palette information
ani_file_content = """
[Animation]
Name=Sample Animation
FrameRate=30
FrameCount=60
Width=640
Height=480

[Palette]
Count=256
PaletteData=0xff0000, 0x00ff00, 0x0000ff, ...
"""

# Save the generated 'ani' file
with open('./tmp/sample.ani', 'w') as f:
    f.write(ani_file_content)

print("Generated 'ani' file saved successfully.")