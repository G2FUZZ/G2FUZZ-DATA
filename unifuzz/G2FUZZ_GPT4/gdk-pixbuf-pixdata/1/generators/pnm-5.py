import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Specify the path for the new PNM file
file_path = './tmp/example.pnm'

# Image details (a simple 3x2 image with 6 pixels)
width = 3
height = 2
max_color_value = 255
image_data = [
    [255, 0, 0], [0, 255, 0], [0, 0, 255],
    [255, 255, 0], [255, 255, 255], [0, 0, 0]
]

# Write the PNM file
with open(file_path, 'w') as f:
    # Write the header
    f.write(f"P3\n{width} {height}\n{max_color_value}\n")
    # Write the pixel data
    for row in range(height):
        for col in range(width):
            pixel_index = row * width + col
            pixel_data = image_data[pixel_index]
            f.write(f"{pixel_data[0]} {pixel_data[1]} {pixel_data[2]} ")
        f.write("\n")

print(f"PNM file saved to {file_path}")