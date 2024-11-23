from PIL import Image, ImageDraw

# Define cursor width, height, and hotspot coordinates
width, height = 32, 32
hotspot_x, hotspot_y = width // 2, height // 2

# Create a new image with transparent background
image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

# Optionally, draw something on your cursor
draw = ImageDraw.Draw(image)
draw.rectangle([0, 0, width-1, height-1], outline="black", fill="white")

# Save directory
save_directory = "./tmp/"

# Make sure the save directory exists
import os
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Save the cursor file
# PIL does not directly support saving .cur files with hotspots
# Thus, we first save as .ico and then manually add the hotspot information
ico_path = os.path.join(save_directory, "cursor.ico")
image.save(ico_path, format='ICO', sizes=[(width, height)])

# Function to add hotspot information to .ico file to convert it into .cur file
def convert_ico_to_cur(ico_path, cur_path, hotspot_x, hotspot_y):
    with open(ico_path, 'rb') as f:
        content = bytearray(f.read())
    
    # ICO and CUR files have the same format except for the bytes at positions 4 and 6
    # which represent the hotspot coordinates (x, y)
    content[4] = hotspot_x & 0xff  # x
    content[5] = (hotspot_x >> 8) & 0xff  # x
    content[6] = hotspot_y & 0xff  # y
    content[7] = (hotspot_y >> 8) & 0xff  # y

    with open(cur_path, 'wb') as f:
        f.write(content)

# Convert the ICO file to CUR file with hotspot
cur_path = os.path.join(save_directory, "cursor.cur")
convert_ico_to_cur(ico_path, cur_path, hotspot_x, hotspot_y)

# Optionally, clean up the ICO file as it's not needed anymore
os.remove(ico_path)

print(f"Cursor file with hotspot saved at: {cur_path}")