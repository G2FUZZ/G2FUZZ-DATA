import os
from PIL import Image, ImageDraw

# Create a directory to save the generated JPG files
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to generate an image with adjustable compression
def generate_image_with_compression(filename, compression_level):
    # Create a new image with white background
    image_size = (800, 600)
    image = Image.new('RGB', image_size, color = 'white')
    
    # Add some text to the image
    draw = ImageDraw.Draw(image)
    text = f"Compression Level: {compression_level}"
    draw.text((50, 50), text, fill=(0, 0, 0))
    
    # Save the image with the specified compression level
    image.save(os.path.join(output_dir, filename), quality=compression_level)

# Generate images with different compression levels
compression_levels = [10, 30, 50, 70, 90]
for level in compression_levels:
    filename = f'compression_{level}.jpg'
    generate_image_with_compression(filename, level)

print("Images generated with different compression levels.")