import os

# Create the ./tmp/ directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Define the image data (a simple 2x2 image)
width, height = 2, 2
max_color = 255
# Image data: top left is red, top right is green, bottom left is blue, bottom right is yellow (RGB)
image_data = [
    [255, 0, 0], [0, 255, 0],
    [0, 0, 255], [255, 255, 0]
]

# Generate ASCII PPM (P3 format)
ascii_filename = './tmp/ascii_image.ppm'
with open(ascii_filename, 'w') as f:
    f.write(f'P3\n{width} {height}\n{max_color}\n')
    for row in range(height):
        for col in range(width):
            pixel_data = image_data[row * width + col]
            # Corrected line: Use pixel_data to access RGB values
            f.write(f'{pixel_data[0]} {pixel_data[1]} {pixel_data[2]}\n')

# Generate Binary PPM (P6 format)
binary_filename = './tmp/binary_image.ppm'
with open(binary_filename, 'wb') as f:
    header = f'P6\n{width} {height}\n{max_color}\n'.encode()
    f.write(header)
    for pixel in image_data:
        f.write(bytearray(pixel))

print("PNM files have been generated and saved in './tmp/'.")