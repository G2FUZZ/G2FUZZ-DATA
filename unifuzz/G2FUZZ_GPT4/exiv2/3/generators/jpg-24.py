import os
from PIL import Image, ImageDraw, JpegPresets
from cryptography.fernet import Fernet

# Create a directory for saving the images if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

def create_gradient_image(width, height, colors):
    """Create a gradient image from left to right."""
    base = Image.new('RGB', (width, height), colors[0])
    top = Image.new('RGB', (width, height), colors[1])
    mask = Image.new('L', (width, height))
    for y in range(height):
        mask_data = [(int(255 * (x / width))) for x in range(width)]
        mask.putdata(mask_data, 0, y)
    base.paste(top, (0, 0, width, height), mask)
    return base

def encrypt_image(file_path, key):
    """
    Encrypt an image file and save it with .enc extension.
    
    Args:
    - file_path (str): Path to the image file.
    - key (bytes): Encryption key.
    """
    # Read image file
    with open(file_path, 'rb') as file:
        file_data = file.read()
    
    # Encrypt data
    fernet = Fernet(key)
    encrypted = fernet.encrypt(file_data)
    
    # Write the encrypted file
    with open(file_path + '.enc', 'wb') as file:
        file.write(encrypted)

def custom_quantization_table(quality):
    """
    Generate a custom quantization table based on the desired quality.
    This is a placeholder function; you should replace it with your actual quantization logic.
    
    Args:
    - quality (int): Quality level (1-100).
    
    Returns:
    - A 64-element list representing the quantization table.
    """
    # This is a simplified example. Replace it with your actual quantization table logic.
    if quality < 50:
        # Example of a more compressed (lower quality) quantization table
        return [i + quality for i in range(64)]
    else:
        # Example of a less compressed (higher quality) quantization table
        return [i + 100 - quality for i in range(64)]

# Generate a key for encryption
key = Fernet.generate_key()

# Image settings
image_size = (800, 600)
gradient_colors = ('blue', 'red')

# Create a gradient image
image = create_gradient_image(image_size[0], image_size[1], gradient_colors)

# Save the image with different compression qualities and custom quantization tables
compression_levels = {'low': 10, 'medium': 50, 'high': 95}
for quality_level, quality in compression_levels.items():
    file_path = os.path.join(output_dir, f'gradient_quality_{quality_level}.jpg')
    # Apply custom quantization table based on quality
    quantization_table = custom_quantization_table(quality)
    # Pillow does not directly support setting custom quantization tables in this manner,
    # so this example is illustrative. Actual implementation would require a different approach
    # or a library that supports manual quantization table adjustments.
    
    # Save the image with the specified quality
    image.save(file_path, 'JPEG', quality=quality)
    # Encrypt the saved image for DRM
    encrypt_image(file_path, key)

print("Images have been saved with different compression levels and DRM encryption.")