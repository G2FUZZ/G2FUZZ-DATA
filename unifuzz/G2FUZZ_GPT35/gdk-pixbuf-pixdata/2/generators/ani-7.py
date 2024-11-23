import os

# Define the content of the 'ani' file
ani_content = """
Features of the 'ani' file:
1. Resolution: The animation has a resolution of 1920x1080 pixels.
2. Duration: The animation lasts for 10 seconds.
3. Frame Rate: The frame rate of the animation is set to 30 frames per second.
4. Format: The 'ani' file is in MP4 format.
5. Compression: The animation is compressed using H.264 codec.
6. Sound: The animation includes background music and sound effects.
7. Interactivity: Some 'ani' files allow for interactive elements, enabling user input to control or manipulate the animation.
"""

# Create the 'tmp' directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save the 'ani' file with the defined content
with open('./tmp/animation.ani', 'w') as file:
    file.write(ani_content)

print("Generated 'ani' file saved successfully.")