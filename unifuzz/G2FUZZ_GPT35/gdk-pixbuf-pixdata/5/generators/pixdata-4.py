import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a mock color palette for demonstration
color_palette = {
    0: (255, 255, 255),  # White
    1: (255, 0, 0),      # Red
    2: (0, 255, 0),      # Green
    3: (0, 0, 255)       # Blue
}

# Save the color palette to a file
with open('./tmp/color_palette.pixdata', 'w') as file:
    for pixel_value, color in color_palette.items():
        file.write(f'{pixel_value}: {color}\n')

print("Color palette file saved successfully.")