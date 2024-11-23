from PIL import Image, ImageFile, ImageDraw
import numpy as np
import os

def generate_gradient_image(width, height):
    """Generate a gradient image from black to white."""
    image = Image.new('RGB', (width, height))
    for x in range(width):
        for y in range(height):
            value = int((x / width) * 255)
            image.putpixel((x, y), (value, value, value))
    return image

def apply_custom_quantization(image, luminance_q_table, chrominance_q_table):
    """Apply custom quantization tables to an image."""
    ImageFile.MAXBLOCK = image.size[0] * image.size[1]
    image.encoderinfo = {
        "quality": 85,
        "qtables": [luminance_q_table, chrominance_q_table]
    }
    return image

def create_quantization_tables():
    """Create example luminance and chrominance quantization tables."""
    # These are example tables. Adjust values based on your specific needs.
    luminance_q_table = np.array([
        16, 11, 10, 16, 24, 40, 51, 61,
        12, 12, 14, 19, 26, 58, 60, 55,
        14, 13, 16, 24, 40, 57, 69, 56,
        14, 17, 22, 29, 51, 87, 80, 62,
        18, 22, 37, 56, 68, 109, 103, 77,
        24, 35, 55, 64, 81, 104, 113, 92,
        49, 64, 78, 87, 103, 121, 120, 101,
        72, 92, 95, 98, 112, 100, 103, 99
    ], dtype=np.uint8).reshape((8, 8))

    chrominance_q_table = np.array([
        17, 18, 24, 47, 99, 99, 99, 99,
        18, 21, 26, 66, 99, 99, 99, 99,
        24, 26, 56, 99, 99, 99, 99, 99,
        47, 66, 99, 99, 99, 99, 99, 99,
        99, 99, 99, 99, 99, 99, 99, 99,
        99, 99, 99, 99, 99, 99, 99, 99,
        99, 99, 99, 99, 99, 99, 99, 99,
        99, 99, 99, 99, 99, 99, 99, 99
    ], dtype=np.uint8).reshape((8, 8))
    
    return luminance_q_table, chrominance_q_table

def create_combined_image(images, rows, cols):
    """Combine multiple images into a grid."""
    w, h = images[0].size
    combined_image = Image.new('RGB', (w * cols, h * rows))
    for i, img in enumerate(images):
        combined_image.paste(img, ((i % cols) * w, (i // cols) * h))
    return combined_image

# Ensure ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a base gradient image
base_image = generate_gradient_image(800, 600)

# Create quantization tables
luminance_q_table, chrominance_q_table = create_quantization_tables()

# Generate variations with different compression ratios and quantization tables
images = []
qualities = [10, 50, 85, 100]  # Different JPEG quality settings
for quality in qualities:
    img = base_image.copy()
    img.save(f'./tmp/gradient_quality_{quality}.jpg', 'JPEG', quality=quality)
    images.append(Image.open(f'./tmp/gradient_quality_{quality}.jpg'))

# Generate an image with custom quantization tables
custom_q_img = apply_custom_quantization(base_image.copy(), luminance_q_table, chrominance_q_table)
custom_q_img_path = './tmp/gradient_custom_q_table.jpg'
custom_q_img.save(custom_q_img_path, 'JPEG')
images.append(Image.open(custom_q_img_path))

# Combine all images into a single image
combined_image = create_combined_image(images, 2, 3)
combined_image_path = './tmp/combined_gradient_image.jpg'
combined_image.save(combined_image_path, 'JPEG')

print(f"Combined image saved to {combined_image_path}")