from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
image = Image.new('RGB', (100, 100), color = 'blue')

# Save the image with an optimization option that includes Huffman coding
# and specify Chroma Subsampling using the subsampling argument
# Common subsampling values are '4:4:4' (no subsampling), '4:2:2', and '4:2:0'
# '4:2:0' is a common choice for JPEGs, halving the resolution of the color channels
image.save('./tmp/simple_image_with_huffman_and_subsampling.jpg', 'JPEG', optimize=True, subsampling='4:2:0')

print("Image was saved with Huffman Coding and Chroma Subsampling as part of the JPEG optimization.")