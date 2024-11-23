from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create an image and save it with different compression levels
def create_jpg_with_compression_levels(filename_prefix, compression_levels):
    # Create a simple 100x100 pixel image with a single rectangle
    image = Image.new('RGB', (100, 100), color='blue')
    draw = ImageDraw.Draw(image)
    draw.rectangle([25, 25, 75, 75], fill="red")
    
    # Iterate over the requested compression levels
    for level in compression_levels:
        # The 'quality' parameter controls the compression level in PIL
        # Quality goes from 1 (worst) to 95 (best), 0 and 100 are system values
        filename = f'./tmp/{filename_prefix}_quality_{level}.jpg'
        image.save(filename, 'JPEG', quality=level)
        print(f'Saved {filename} with quality level {level}')

# Define a list of desired compression levels
compression_levels = [10, 30, 50, 70, 90]

# Call the function with a filename prefix and the list of compression levels
create_jpg_with_compression_levels('test_image', compression_levels)