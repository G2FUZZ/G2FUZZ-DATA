from PIL import Image, ImageDraw

def create_hierarchical_image_with_subsampling_huffman_and_bit_modes(filename, size=(800, 600), subsampling='4:2:0', bit_mode=8):
    # Create the base image
    base_image = Image.new('RGB', size, (255, 255, 255))
    draw = ImageDraw.Draw(base_image)
    
    # Add some base content to the image
    draw.rectangle([10, 10, size[0]-10, size[1]-10], outline=(0, 0, 0), width=5)
    draw.text((20, 20), "Hierarchical Storage with Chroma Subsampling, Huffman Coding and Bit Modes", fill=(0, 0, 0))
    
    # Function to recursively add smaller images
    def add_smaller_images(image, level=1):
        if level > 3:  # Limit the recursion depth to avoid too many small images
            return image
        smaller_image = image.copy().resize((int(image.width / 2), int(image.height / 2)))
        image.paste(smaller_image, (image.width - smaller_image.width, image.height - smaller_image.height))
        return add_smaller_images(image, level + 1)
    
    # Apply the smaller images onto the base image
    final_image = add_smaller_images(base_image)
    
    # Prepare image save options based on the bit mode
    save_options = {
        "quality": 95,
        "optimize": True
    }
    
    # Adjust subsampling based on input
    if subsampling == '4:4:4':
        save_options["subsampling"] = 0
    elif subsampling == '4:2:2':
        save_options["subsampling"] = 1
    elif subsampling == '4:2:0':
        save_options["subsampling"] = 2
    
    # Adjust for bit modes - PIL doesn't directly support 12-bit JPEG, so this is illustrative only
    if bit_mode == 12:
        print("Note: PIL does not support 12-bit JPEG directly. This mode is illustrative and will still produce an 8-bit JPEG.")
    
    # Save the image with Chroma Subsampling, Huffman Coding, and considering bit modes
    final_image.save(filename, **save_options)

# Ensure the tmp directory exists
import os
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Create and save the hierarchical image with Chroma Subsampling, Huffman Coding, and Bit Modes
create_hierarchical_image_with_subsampling_huffman_and_bit_modes('./tmp/hierarchical_storage_with_subsampling_huffman_and_bit_modes.jpg')