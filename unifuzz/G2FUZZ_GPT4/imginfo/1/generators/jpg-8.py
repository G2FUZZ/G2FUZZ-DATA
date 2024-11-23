from PIL import Image
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Image size and block size
width, height = 256, 256  # Image dimensions
block_size = 16  # Block size (can be 8x8 or 16x16 as mentioned)

# Create a new image with mode 'RGB'
image = Image.new('RGB', (width, height), "white")
pixels = image.load()

# Fill the image with alternating blocks
for y in range(0, height, block_size):
    for x in range(0, width, block_size):
        for i in range(block_size):
            for j in range(block_size):
                # Check the block's position to decide the color
                if (x // block_size) % 2 == (y // block_size) % 2:
                    pixels[x+i, y+j] = (255, 0, 0)  # Red blocks
                else:
                    pixels[x+i, y+j] = (0, 0, 255)  # Blue blocks

# Save the image
file_path = os.path.join(output_dir, 'block_encoding_demo.jpg')
image.save(file_path, 'JPEG')

print(f"Image saved at {file_path}")