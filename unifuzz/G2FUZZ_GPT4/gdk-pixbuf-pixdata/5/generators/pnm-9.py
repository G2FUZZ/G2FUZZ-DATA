import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Data for a simple 2x2 image for demonstration ([R,G,B] for each pixel)
pixels = [
    [[255, 0, 0], [0, 255, 0]],
    [[0, 0, 255], [255, 255, 0]]
]

# ASCII PNM (P3) format
ascii_content = 'P3\n2 2\n255\n'
ascii_content += '\n'.join(' '.join(' '.join(str(channel) for channel in pixel) for pixel in row) for row in pixels)

with open('./tmp/ascii_image.ppm', 'w') as file:
    file.write(ascii_content)

# Binary PNM (P6) format
binary_content = b'P6\n2 2\n255\n' + b''.join(bytes(pixel) for row in pixels for pixel in row)

with open('./tmp/binary_image.ppm', 'wb') as file:
    file.write(binary_content)

print("Files saved: ascii_image.ppm, binary_image.ppm")