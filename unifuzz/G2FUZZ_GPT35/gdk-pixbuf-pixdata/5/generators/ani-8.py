import os

# Define the content of the ani file
ani_content = """
Features:
1. Resolution: 1920x1080 pixels
2. Frame rate: 30 fps
3. Color depth: 24-bit color
4. Audio support: Stereo sound
5. Compression: H.264
6. Transparency: Yes
7. Interactivity: Clickable elements
8. Scripting support: Advanced 'ani' formats may support scripting languages to create interactive and dynamic animations.
"""

# Create a directory if it does not exist
os.makedirs("./tmp/", exist_ok=True)

# Save the content to a new ani file
file_path = "./tmp/generated.ani"
with open(file_path, "w") as file:
    file.write(ani_content)

print(f"Generated 'ani' file saved at: {file_path}")