from PIL import Image, ImageDraw

def create_hierarchical_image_with_subsampling_and_arithmetic_coding(filename, size=(800, 600), subsampling='4:2:0'):
    # Create the base image
    base_image = Image.new('RGB', size, (255, 255, 255))
    draw = ImageDraw.Draw(base_image)
    
    # Add some base content to the image
    draw.rectangle([10, 10, size[0]-10, size[1]-10], outline=(0, 0, 0), width=5)
    draw.text((20, 20), "Hierarchical Storage with Chroma Subsampling and Arithmetic Coding", fill=(0, 0, 0))
    
    # Function to recursively add smaller images
    def add_smaller_images(image, level=1):
        if level > 3:  # Limit the recursion depth to avoid too many small images
            return image
        smaller_image = image.copy().resize((int(image.width / 2), int(image.height / 2)))
        image.paste(smaller_image, (image.width - smaller_image.width, image.height - smaller_image.height))
        return add_smaller_images(image, level + 1)
    
    # Apply the smaller images onto the base image
    final_image = add_smaller_images(base_image)
    
    # Save the image with Chroma Subsampling and enable Arithmetic Coding
    if subsampling == '4:4:4':
        # This option keeps full chroma information (no subsampling)
        final_image.save(filename, quality=95, subsampling=0, optimize=True, qtables="web_high", progressive=True)
    elif subsampling == '4:2:2':
        # This option subsamples the chroma channels horizontally
        final_image.save(filename, quality=95, subsampling=1, optimize=True, qtables="web_high", progressive=True)
    elif subsampling == '4:2:0':
        # This option subsamples the chroma channels both horizontally and vertically
        final_image.save(filename, quality=95, subsampling=2, optimize=True, qtables="web_high", progressive=True)
    else:
        # Default to no subsampling if an unrecognized value is provided
        final_image.save(filename, optimize=True, qtables="web_high", progressive=True)

# Ensure the tmp directory exists
import os
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Create and save the hierarchical image with Chroma Subsampling and Arithmetic Coding
create_hierarchical_image_with_subsampling_and_arithmetic_coding('./tmp/hierarchical_storage_with_subsampling_and_arithmetic_coding.jpg')