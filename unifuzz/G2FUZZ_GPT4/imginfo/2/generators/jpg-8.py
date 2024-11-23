import numpy as np
import cv2
import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Function to generate an 8x8 block with a gradient for demonstration
def generate_gradient_block():
    block = np.zeros((8, 8), dtype=np.uint8)
    for i in range(8):
        for j in range(8):
            block[i, j] = (i + j) * 32 % 255  # Simple gradient pattern
    return block

# Function to apply DCT to an 8x8 block
def apply_dct(block):
    # Convert block to float32 for the DCT function
    block_float = np.float32(block)
    # Apply DCT
    dct_block = cv2.dct(block_float)
    # Scale for visibility in JPEG (not a standard step, just for visualization)
    dct_block_vis = np.log(np.abs(dct_block) + 1)
    dct_block_vis = np.uint8(dct_block_vis / np.max(dct_block_vis) * 255)
    return dct_block_vis

# Generate an 8x8 block
block = generate_gradient_block()

# Apply DCT to the block
dct_block = apply_dct(block)

# Create a larger image to save as JPEG, since very small images may not compress well
img_size = 512  # Make a 512x512 image
img = np.tile(dct_block, (img_size // 8, img_size // 8))

# Save the original block and the DCT transformed block as JPEG
cv2.imwrite('./tmp/original_block.jpg', np.tile(block, (img_size // 8, img_size // 8)))
cv2.imwrite('./tmp/dct_block.jpg', img)

print("JPEG files generated and saved in './tmp/'.")