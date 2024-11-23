import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the image data
# This will create an image of 100x100 pixels
# The image will be divided into four quadrants with different colors
width, height = 100, 100
data = []

# Generate pixel data
for y in range(height):
    row = []
    for x in range(width):
        if x < width // 2 and y < height // 2:
            row.append((255, 0, 0))  # Red, top-left
        elif x >= width // 2 and y < height // 2:
            row.append((0, 255, 0))  # Green, top-right
        elif x < width // 2 and y >= height // 2:
            row.append((0, 0, 255))  # Blue, bottom-left
        else:
            row.append((255, 255, 0))  # Yellow, bottom-right
    data.append(row)

# Create a PPM P6 file (binary encoding)
with open('./tmp/sample_image.ppm', 'wb') as f:
    # Write the header
    f.write(b'P6\n')
    f.write(f'{width} {height}\n'.encode())
    f.write(b'255\n')  # Max color value

    # Write the pixel data
    for row in data:
        for pixel in row:
            f.write(bytes(pixel))

print("PPM file has been saved to ./tmp/sample_image.ppm")