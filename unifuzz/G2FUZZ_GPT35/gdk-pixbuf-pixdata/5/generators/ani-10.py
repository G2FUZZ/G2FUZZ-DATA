import os

# Create a directory if it doesn't already exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate 'ani' files with customization options
file_contents = """
Animation File:
- Playback Speed: 1x
- Color Scheme: RGB
- Effects: Fade-in/out

Customization Options:
- Playback Speed: 1-5x
- Color Scheme: RGB, CMYK
- Effects: Fade, Scale, Rotate
"""

# Save the generated files into the output directory
for i in range(3):
    file_name = f'{output_dir}animation_{i + 1}.ani'
    with open(file_name, 'w') as file:
        file.write(file_contents)

print('Generated files saved in ./tmp/')