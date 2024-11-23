import os
from PIL import Image

# Create tmp directory if not exists
os.makedirs('./tmp/', exist_ok=True)

# Define parameters for the cursor image
width, height = 32, 32  # Standard dimensions for cursors
color_depth = 32  # 32-bit for full color with alpha channel

# Create an image with transparency
image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

# Drawing an example cursor with some transparency
for x in range(width):
    for y in range(height):
        if x < width / 2:
            image.putpixel((x, y), (255, 0, 0, 128))  # Semi-transparent red half
        else:
            image.putpixel((x, y), (0, 255, 0, 128))  # Semi-transparent green half

# Save the cursor image
image.save('./tmp/cursor.png')

# ANI file creation is not directly supported by widely used Python libraries
# We'll create a basic .ani file manually, but note that this is a simplified example
# and may not be recognized as a valid cursor file without a proper header and content.
ani_header = "anih"
ani_content = "Example content with color depth support."

with open('./tmp/cursor.ani', 'w') as ani_file:
    ani_file.write(ani_header + '\n')
    ani_file.write(ani_content + '\n')

print("ANI file with basic content created in ./tmp/")