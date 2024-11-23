import struct

# Function to create a TGA file with given image data
def create_tga_file(file_path, image_data):
    header = bytearray([0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])  # TGA header for uncompressed RGB image
    width = len(image_data[0])
    height = len(image_data)
    header.extend(struct.pack("<hhB", width, height, 24))  # Add width, height, and bits per pixel to header

    with open(file_path, 'wb') as f:
        f.write(header)
        for row in image_data:
            for pixel in row:
                f.write(bytes(pixel))

# Generate sample image data
image_data = [
    [(255, 0, 0) for _ in range(100)],  # Red pixels
    [(0, 255, 0) for _ in range(100)],  # Green pixels
    [(0, 0, 255) for _ in range(100)]   # Blue pixels
]

# Create and save TGA files with sample image data
for i, pixels in enumerate(image_data):
    file_name = f"./tmp/image_{i}.tga"
    create_tga_file(file_name, pixels)