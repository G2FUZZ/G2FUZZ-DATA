import png
import os

# Create a directory to store the PNG files
os.makedirs('./tmp/', exist_ok=True)

# Define the image data
data = [
    [0, 255, 0, 255] * 4,
    [255, 0, 255, 255] * 4,
    [0, 255, 0, 255] * 4,
    [255, 0, 255, 255] * 4
]

# Create the PNG file with error detection checksum
png.from_array(data, 'RGBA').save('./tmp/error_detection.png')