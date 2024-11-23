import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generating a simple PNM file (PBM, PGM, and PPM formats fall under the PNM umbrella)
# Here, we'll create a simple PPM file, as it supports colors.

# Header for a PPM file
# P3 means this is a PPM file in ASCII encoding.
# 3 3 defines the width and height of the image.
# 255 defines the maximum color value.
header = "P3\n3 3\n255\n"

# Pixel data - a 3x3 image with a colorful pattern
# Each pixel is defined by its RGB values, ranging from 0 to 255.
# The pattern here does not convey any specific meaning, just an example.
pixels = [
    "255 0 0 ", "0 255 0 ", "0 0 255 ",
    "255 255 0 ", "255 255 255 ", "0 255 255 ",
    "0 0 0 ", "128 128 128 ", "255 0 255 "
]

# Joining the header and the pixel data to form the full PPM content
ppm_content = header + "\n".join(pixels)

# Saving the PPM content to a file
file_path = './tmp/example.ppm'
with open(file_path, 'w') as file:
    file.write(ppm_content)

print(f"PPM file saved at {file_path}")