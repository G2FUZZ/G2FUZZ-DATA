from PIL import Image, ImageDraw, ImageOps, ImageFont
import os

def create_complex_quantized_image(filename, size=(800, 600), base_quantization_level=50, max_depth=5):
    """
    Generates an image with more complex features including:
    - Variable recursion depth
    - Image rotation at each level
    - Variable quantization levels
    """
    # Create the base image
    base_image = Image.new('RGB', size, (255, 255, 255))
    draw = ImageDraw.Draw(base_image)
    try:
        # Try to use a default font
        font = ImageFont.truetype("arial.ttf", 22)
    except IOError:
        # Fallback if the specific font is not found
        font = ImageFont.load_default()

    # Add some content to the image
    draw.rectangle([10, 10, size[0]-10, size[1]-10], outline=(0, 0, 0), width=5)
    draw.text((20, 30), "Complex Hierarchical Storage", fill=(0, 0, 0), font=font)
    
    def add_smaller_images(image, level=1, rotation=0):
        if level > max_depth: 
            return image
        smaller_image = image.copy().resize((int(image.width / 2), int(image.height / 2)))
        rotated_image = smaller_image.rotate(rotation)
        image.paste(rotated_image, (image.width - rotated_image.width, image.height - rotated_image.height))

        # Increment the rotation and change quantization level for variety
        new_rotation = (rotation + 45) % 360
        new_quantization_level = base_quantization_level + level * 10
        quantized_image = rotated_image.quantize(colors=new_quantization_level)
        rgb_image = quantized_image.convert('RGB')

        # Paste the quantized and rotated image back onto the original
        image.paste(rgb_image, (image.width - rotated_image.width, image.height - rotated_image.height))

        return add_smaller_images(image, level + 1, new_rotation)

    # Apply the smaller images onto the base image with recursion
    final_image = add_smaller_images(base_image)

    # Save the final image
    final_image.save(filename)

# Ensure the tmp directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Create and save the complex hierarchical and quantized image
create_complex_quantized_image('./tmp/complex_hierarchical_storage_quantized.jpg')