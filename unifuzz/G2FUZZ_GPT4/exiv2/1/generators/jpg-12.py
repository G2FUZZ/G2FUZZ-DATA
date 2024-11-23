import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a main image (example: 800x600, blue background)
main_image = Image.new('RGB', (800, 600), color = 'blue')

# Create a thumbnail of the main image (example: 80x60)
thumbnail = main_image.copy()
thumbnail.thumbnail((80, 60))

# Save the main image
main_image_path = './tmp/main_image.jpg'
main_image.save(main_image_path)

# Save the thumbnail image
thumbnail_path = './tmp/thumbnail.jpg'
thumbnail.save(thumbnail_path)

# Enhanced: Block Encoding
# Create an encoded image (example: 800x600, blue background) with block encoding
def apply_block_encoding(image, block_size=(8, 8)):
    """
    Simulates block encoding by dividing the image into blocks and compressing each block.
    This function doesn't actually compress but demonstrates the partitioning involved in block encoding.
    
    Args:
        image: A PIL Image object.
        block_size: A tuple indicating the size of each block.
    
    Returns:
        A new PIL Image object with "block encoding" simulation.
    """
    # Create a new image to draw the blocks
    encoded_image = Image.new('RGB', image.size, color='white')
    for y in range(0, image.size[1], block_size[1]):
        for x in range(0, image.size[0], block_size[0]):
            block = image.crop((x, y, x + block_size[0], y + block_size[1]))
            # For actual block encoding, compress each block here
            # For demonstration, just paste the block back
            encoded_image.paste(block, (x, y))
    return encoded_image

# Apply block encoding to the main image
encoded_image = apply_block_encoding(main_image)

# Save the encoded image
encoded_image_path = './tmp/encoded_image.jpg'
encoded_image.save(encoded_image_path)