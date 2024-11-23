from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
image = Image.new('RGB', (100, 100), color = 'blue')

# Save the image with an optimization option that includes Huffman coding
image.save('./tmp/simple_image_with_huffman.jpg', 'JPEG', optimize=True)

print("Image was saved with Huffman Coding as part of the JPEG optimization.")